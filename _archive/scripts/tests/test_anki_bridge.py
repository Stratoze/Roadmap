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


class FakeLaneAnki:
    """Answers findCards the way the server does, by operator, not by arithmetic.

    Recording every action is the point: the lane code must never reach a write
    action, and the test asserts that rather than trusting the code path.
    """

    def __init__(self, new=0, learn=0, stuck=0, notes=(), decks=("Kaishi 1.5k", "Lapis")):
        self.counts = {"new": new, "learn": learn, "stuck": stuck}
        self.notes = list(notes)
        self.decks = list(decks)
        self.actions = []

    def call(self, action, **params):
        self.actions.append((action, params))
        if action == "findCards":
            query = params["query"]
            if "is:new" in query:
                n = self.counts["new"]
            elif "is:learn" in query:
                n = self.counts["learn"]
            elif "prop:ivl<" in query:
                n = self.counts["stuck"]
            else:
                n = 0
            return list(range(n))
        if action == "cardsInfo":
            return [{"note": 900 + i} for i, _ in enumerate(params["cards"])]
        if action == "notesInfo":
            return self.notes[: len(params["notes"])]
        if action == "addNote":
            raise AssertionError("the i+1 lane must never write")
        raise AssertionError(f"unexpected action {action}")

    def writes(self):
        return [a for a, _ in self.actions if a == "addNote"]

    def queries(self):
        return [p["query"] for a, p in self.actions if a == "findCards"]


def kaishi_note(word):
    return {"modelName": "Kaishi 1.5k", "fields": {"Word": {"value": word}}}


class IPlusOneLaneTests(unittest.TestCase):
    def test_pending_cards_block_the_stretch_lane(self):
        client = FakeLaneAnki(new=1, learn=8, stuck=1000)
        result = anki_bridge.iplusone(client, decks=("Kaishi 1.5k",), sample=0)
        self.assertEqual(result["lane"], "patch")
        self.assertFalse(result["stretch_available"])
        self.assertTrue(result["patch_available"])
        self.assertEqual(result["unlearned_total"], 9)
        self.assertEqual(result["stuck_total"], 1000)

    def test_caught_up_opens_the_stretch_lane(self):
        client = FakeLaneAnki(new=0, learn=0, stuck=1000)
        result = anki_bridge.iplusone(client, decks=("Kaishi 1.5k",), sample=0)
        self.assertEqual(result["lane"], "stretch")
        self.assertTrue(result["stretch_available"])
        # A patch lane is still offered rather than silently dropped.
        self.assertTrue(result["patch_available"])

    def test_hold_when_nothing_is_available(self):
        client = FakeLaneAnki(new=0, learn=5, stuck=0)
        result = anki_bridge.iplusone(client, decks=("Kaishi 1.5k",), sample=0)
        self.assertEqual(result["lane"], "hold")
        self.assertFalse(result["stretch_available"])
        self.assertFalse(result["patch_available"])

    def test_lane_counts_come_from_server_operators(self):
        client = FakeLaneAnki(new=2, learn=3, stuck=7)
        anki_bridge.deck_lane_counts(client, "Kaishi 1.5k")
        queries = client.queries()
        self.assertIn('deck:"Kaishi 1.5k" is:new', queries)
        self.assertIn('deck:"Kaishi 1.5k" is:learn', queries)
        # Never cardsInfo.due arithmetic: for review cards that is a raw day
        # offset, and counting it locally invents a due date.
        self.assertIn('deck:"Kaishi 1.5k" prop:reps>=10 prop:ivl<7', queries)

    def test_threshold_is_configurable_and_reported(self):
        client = FakeLaneAnki(stuck=5)
        result = anki_bridge.iplusone(
            client, decks=("Kaishi 1.5k",), sample=0, reps_min=20, interval_max=3
        )
        self.assertEqual(result["threshold"], {"reps_min": 20, "interval_max_days": 3})
        self.assertTrue(
            any("prop:reps>=20 prop:ivl<3" in q for q in client.queries()),
            client.queries(),
        )

    def test_deck_names_are_escaped(self):
        client = FakeLaneAnki()
        anki_bridge.deck_lane_counts(client, 'we"ird\\deck')
        self.assertIn('deck:"we\\"ird\\\\deck" is:new', client.queries())

    def test_stuck_words_are_named_by_model_field(self):
        client = FakeLaneAnki(stuck=3, notes=[kaishi_note("あまり"), kaishi_note("全然")])
        result = anki_bridge.iplusone(client, decks=("Kaishi 1.5k",), sample=2)
        self.assertEqual([w["word"] for w in result["stuck_samples"]], ["あまり", "全然"])
        self.assertEqual(result["stuck_samples"][0]["model"], "Kaishi 1.5k")

    def test_note_with_no_word_field_mapping_is_skipped_not_guessed(self):
        client = FakeLaneAnki(
            stuck=2,
            notes=[{"modelName": "Basic", "fields": {"Front": {"value": "x"}}}, kaishi_note("置く")],
        )
        result = anki_bridge.iplusone(client, decks=("Kaishi 1.5k",), sample=2)
        self.assertEqual([w["word"] for w in result["stuck_samples"]], ["置く"])

    def test_lane_never_writes(self):
        client = FakeLaneAnki(new=1, learn=1, stuck=5, notes=[kaishi_note("置く")])
        anki_bridge.iplusone(client, sample=3)
        self.assertEqual(client.writes(), [])
        self.assertEqual({a for a, _ in client.actions}, {"findCards", "cardsInfo", "notesInfo"})

    def test_empty_deck_reports_zero_rather_than_failing(self):
        client = FakeLaneAnki()
        result = anki_bridge.iplusone(client, decks=("Lapis",), sample=5)
        self.assertEqual(result["unlearned_total"], 0)
        self.assertEqual(result["stuck_total"], 0)
        self.assertEqual(result["lane"], "stretch")
        self.assertNotIn("stuck_samples", result)

    def test_iplusone_command_runs_read_only(self):
        client = FakeLaneAnki(new=1, learn=0, stuck=3, notes=[kaishi_note("置く")])
        out, err = io.StringIO(), io.StringIO()
        with patch.object(anki_bridge, "client_from_args", return_value=client), \
             contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            self.assertEqual(anki_bridge.main(["iplusone"]), 0)
        payload = json.loads(out.getvalue())
        self.assertEqual(payload["lane"], "patch")
        self.assertEqual(err.getvalue(), "")
        self.assertEqual(client.writes(), [])


class EncodingRecorder(io.StringIO):
    def __init__(self):
        super().__init__()
        self.reconfigured = {}

    def reconfigure(self, **kwargs):
        self.reconfigured.update(kwargs)


class IPlusOneEncodingTests(unittest.TestCase):
    def test_main_configures_utf8_so_japanese_survives_the_console(self):
        """Regression: a fresh agent got stuck words back as replacement chars.

        The bridge is the script that emits Japanese. Without this guard the
        Windows console codepage turns あまり into ����, which silently costs
        the command its entire point.
        """
        recorder = EncodingRecorder()
        client = FakeLaneAnki()
        with patch.object(anki_bridge, "client_from_args", return_value=client), \
             patch.object(anki_bridge.sys, "stdout", recorder), \
             patch.object(anki_bridge.sys, "stderr", recorder):
            self.assertEqual(anki_bridge.main(["iplusone"]), 0)
        self.assertEqual(recorder.reconfigured.get("encoding"), "utf-8")
        self.assertEqual(recorder.reconfigured.get("errors"), "replace")

    def test_a_stream_without_reconfigure_is_tolerated(self):
        class Old:
            def write(self, _text):
                return 0

            def flush(self):
                pass

        client = FakeLaneAnki()
        with patch.object(anki_bridge, "client_from_args", return_value=client), \
             patch.object(anki_bridge.sys, "stdout", Old()), \
             patch.object(anki_bridge.sys, "stderr", Old()):
            self.assertEqual(anki_bridge.main(["iplusone"]), 0)


if __name__ == "__main__":
    unittest.main()
