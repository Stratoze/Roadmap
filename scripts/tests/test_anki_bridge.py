import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import anki_bridge  # noqa: E402


class FakeAnki:
    def __init__(self, note_id=123):
        self.note_id = note_id
        self.created = None
        self.calls = 0

    def version(self):
        return 6

    def decks(self):
        return ["Kaishi 1.5k", "Lapis::Immersion"]

    def due(self, deck):
        return 1000 if deck == "Kaishi 1.5k" else 0

    def add_note(self, deck, model, fields, tags):
        self.calls += 1
        self.created = (deck, model, fields, tags)
        return self.note_id


ADD_ARGS = [
    "add-approved", "猫",
    "--deck", "Lapis::Immersion",
    "--model", "Basic",
    "--front", "猫",
    "--back", "cat",
    "--approved-by", "learner",
    "--approval-evidence", "PLACEHOLDER",
]


class AnkiBridgeTests(unittest.TestCase):
    def test_due_is_read_only_and_deck_names_are_discovered(self):
        client = FakeAnki()
        self.assertEqual(client.decks(), ["Kaishi 1.5k", "Lapis::Immersion"])
        self.assertEqual(client.due("Kaishi 1.5k"), 1000)

    def test_add_note_requires_explicit_mapping(self):
        client = FakeAnki()
        note_id = client.add_note("Lapis::Immersion", "Basic", {"Front": "猫", "Back": "cat"}, ["japanese"])
        self.assertEqual(note_id, 123)
        self.assertEqual(client.created[0], "Lapis::Immersion")

    def test_api_key_refuses_non_loopback_url(self):
        with self.assertRaises(RuntimeError):
            anki_bridge.AnkiConnect("http://example.com:8765", "secret")

    def test_named_arguments_travel_inside_params(self):
        payload = anki_bridge.build_payload("addNote", {"note": {"deckName": "Lapis"}})
        self.assertEqual(payload["action"], "addNote")
        self.assertEqual(payload["version"], 6)
        self.assertEqual(payload["params"], {"note": {"deckName": "Lapis"}})
        # A flattened request is what silently zeroed every deck's due count.
        self.assertNotIn("note", {key for key in payload if key != "params"})
        self.assertNotIn("key", payload)

    def test_api_key_is_sent_for_both_server_conventions(self):
        payload = anki_bridge.build_payload("version", {}, "secret")
        self.assertEqual(payload["key"], "secret")
        self.assertEqual(payload["params"]["key"], "secret")
        self.assertEqual(anki_bridge.build_payload("version", {})["params"], {})

    def test_due_query_reaches_the_server_with_its_deck(self):
        sent = {}

        class FakeResponse:
            def __enter__(self):
                return self

            def __exit__(self, *exc):
                return False

            def read(self):
                return json.dumps({"result": [1, 2, 3], "error": None}).encode("utf-8")

        def fake_urlopen(request, timeout=None):
            sent["payload"] = json.loads(request.data.decode("utf-8"))
            return FakeResponse()

        client = anki_bridge.AnkiConnect()
        with patch.object(anki_bridge.urllib.request, "urlopen", fake_urlopen):
            self.assertEqual(client.due("Kaishi 1.5k"), 3)
        self.assertEqual(sent["payload"]["action"], "findCards")
        self.assertIn('deck:"Kaishi 1.5k"', sent["payload"]["params"]["query"])

    def test_read_only_commands_never_open_a_write_path(self):
        client = FakeAnki()
        out, err = io.StringIO(), io.StringIO()
        with patch.object(anki_bridge, "client_from_args", return_value=client), \
             contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            self.assertEqual(anki_bridge.main(["status"]), 0)
            self.assertEqual(anki_bridge.main(["due"]), 0)
        self.assertEqual(client.calls, 0)
        self.assertEqual(err.getvalue(), "")

    def test_propose_needs_no_live_anki(self):
        def refuse(_args):
            raise AssertionError("propose must not build a client")

        out, err = io.StringIO(), io.StringIO()
        with patch.object(anki_bridge, "client_from_args", refuse), \
             contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            self.assertEqual(anki_bridge.main(["propose", "猫"]), 0)
        self.assertIn("proposal-only", out.getvalue())
        self.assertEqual(err.getvalue(), "")


class PrivateRootFixture:
    """Point the approval gate at a throwaway `_private` root."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.private = self.base / "_private"
        patcher = patch.object(anki_bridge, "PRIVATE_ROOT", str(self.private))
        patcher.start()
        self.addCleanup(patcher.stop)

    def write(self, relative, text="approved by the learner\n"):
        path = self.base / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def add_argv(self, evidence):
        return [str(evidence) if part == "PLACEHOLDER" else part for part in ADD_ARGS]

    def run_main(self, argv, client):
        out, err = io.StringIO(), io.StringIO()
        with patch.object(anki_bridge, "client_from_args", return_value=client), \
             contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = anki_bridge.main(argv)
        return code, out.getvalue(), err.getvalue()


class ApprovalEvidencePathTests(PrivateRootFixture, unittest.TestCase):
    def test_real_private_approval_path_is_accepted(self):
        path = self.write("_private/learning/approval/anki-2026-10-01.md")
        self.assertEqual(anki_bridge.approval_evidence_path(str(path)), str(path.resolve()))

    def test_private_path_without_an_approval_component_is_refused(self):
        path = self.write("_private/learning/verbatim/session.md")
        with self.assertRaises(RuntimeError) as caught:
            anki_bridge.approval_evidence_path(str(path))
        self.assertIn("approval", str(caught.exception))

    def test_outside_private_is_refused_even_when_named_approval(self):
        path = self.write("public/approval.md")
        with self.assertRaises(RuntimeError) as caught:
            anki_bridge.approval_evidence_path(str(path))
        self.assertIn("_private", str(caught.exception))

    def test_private_name_prefix_confusion_is_refused(self):
        path = self.write("_private-backup/approval.md")
        with self.assertRaises(RuntimeError):
            anki_bridge.approval_evidence_path(str(path))

    def test_missing_or_non_file_evidence_is_refused(self):
        with self.assertRaises(RuntimeError):
            anki_bridge.approval_evidence_path(str(self.private / "learning" / "approval" / "nope.md"))
        directory = self.private / "learning" / "approval"
        directory.mkdir(parents=True)
        with self.assertRaises(RuntimeError):
            anki_bridge.approval_evidence_path(str(directory))
        with self.assertRaises(RuntimeError):
            anki_bridge.approval_evidence_path("   ")

    def test_symlink_escaping_private_is_refused(self):
        outside = self.write("elsewhere/approval.md")
        link = self.private / "learning" / "approval" / "link.md"
        try:
            link.symlink_to(outside)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        with self.assertRaises(RuntimeError):
            anki_bridge.approval_evidence_path(str(link))


class ApprovedWriteTests(PrivateRootFixture, unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.approval = self.write("_private/learning/approval/anki.md")

    def test_approved_note_is_created_once_and_reported(self):
        client = FakeAnki(note_id=987654)
        code, out, err = self.run_main(self.add_argv(self.approval), client)
        self.assertEqual(code, 0)
        self.assertEqual(client.calls, 1)
        self.assertIn('"note_id": 987654', out)
        self.assertIn('"status": "created"', out)
        self.assertEqual(err, "")

    def test_missing_approval_never_reaches_anki(self):
        client = FakeAnki()
        code, out, err = self.run_main(self.add_argv(self.base / "public" / "note.md"), client)
        self.assertEqual(code, 2)
        self.assertEqual(client.calls, 0)
        self.assertEqual(out, "")
        self.assertIn("approval evidence", err)

    def test_refused_creation_fails_clearly_instead_of_reporting_success(self):
        client = FakeAnki(note_id=None)
        code, out, err = self.run_main(self.add_argv(self.approval), client)
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertIn("no note id", err)
        self.assertIn("nothing was added", err)

    def test_empty_field_is_refused_before_the_write(self):
        client = FakeAnki()
        argv = self.add_argv(self.approval)
        argv[argv.index("--back") + 1] = "   "
        code, _out, err = self.run_main(argv, client)
        self.assertEqual(code, 2)
        self.assertEqual(client.calls, 0)
        self.assertIn("must not be empty", err)

    def test_blank_approver_is_refused(self):
        client = FakeAnki()
        argv = self.add_argv(self.approval)
        argv[argv.index("--approved-by") + 1] = "  "
        code, _out, err = self.run_main(argv, client)
        self.assertEqual(code, 2)
        self.assertEqual(client.calls, 0)
        self.assertIn("--approved-by", err)


if __name__ == "__main__":
    unittest.main()
