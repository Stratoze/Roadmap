import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import session_state  # noqa: E402


class SessionStateTests(unittest.TestCase):
    def test_init_creates_three_explicit_session_blocks(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "2026-09-27.md"
            with patch.object(session_state, "today_note", return_value=path):
                text = session_state.ensure_note(path)
                self.assertEqual(len(session_state.checklist(text)), 3)
                self.assertIn("session-1", text)
                self.assertIn("session-3", text)

    def test_template_and_script_checklist_labels_match(self):
        template = (ROOT / "_templates" / "daily.md").read_text(encoding="utf-8")
        for key, label in session_state.DEFAULT_LINES.items():
            self.assertIn(f"{key} — {label} — pending", template)

    def test_explicit_state_transitions_preserve_body(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "2026-09-27.md"
            with patch.object(session_state, "today_note", return_value=path):
                text = session_state.ensure_note(path)
                text = session_state.update_item(text, "session-1", "in_progress")
                text = session_state.update_item(text, "session-1", "done")
                self.assertIn("[x] session-1", text)
                self.assertIn("Japanese deliberate session", text)

    def test_today_does_not_create_a_note(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "2026-09-27.md"
            with patch.object(session_state, "ROOT", Path(directory)), \
                    patch.object(session_state, "today_note", return_value=path), \
                    patch.object(session_state, "run_readonly", return_value=(True, "")):
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    self.assertEqual(session_state.report_today(), 0)
            self.assertFalse(path.exists())
            self.assertIn("no daily note", buffer.getvalue())

    def test_failing_helper_is_reported_as_unavailable_not_zero_due(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "2026-09-27.md"
            with patch.object(session_state, "ROOT", Path(directory)), \
                    patch.object(session_state, "today_note", return_value=path), \
                    patch.object(session_state, "run_readonly", return_value=(False, "unavailable: error: broken")) as run:
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    self.assertEqual(session_state.report_today(), 0)
            text = buffer.getvalue()
            self.assertIn("Due review: unavailable", text)
            self.assertNotIn("Due review: 0 item(s)", text)
            self.assertIn("Anki: 20–30 minutes — unavailable", text)
            # review.py due, anki_bridge.py iplusone, anki_bridge.py due.
            self.assertEqual(run.call_count, 3)

    def test_run_readonly_fails_closed_on_nonzero_exit(self):
        result = subprocess.CompletedProcess(args=[], returncode=2, stdout="", stderr="error: no curriculum file\n")
        with patch.object(session_state.subprocess, "run", return_value=result):
            ok, message = session_state.run_readonly(["python3", "scripts/review.py", "due"])
        self.assertFalse(ok)
        self.assertIn("unavailable", message)
        self.assertIn("error: no curriculum file", message)

    def test_run_readonly_reports_success_output(self):
        result = subprocess.CompletedProcess(args=[], returncode=0, stdout="japanese-grammar | c1 | review | 2 | - | 2026-01-01\n", stderr="")
        with patch.object(session_state.subprocess, "run", return_value=result):
            ok, message = session_state.run_readonly(["python3", "scripts/review.py", "due"])
        self.assertTrue(ok)
        self.assertIn("japanese-grammar | c1", message)


class HandoffSummaryTests(unittest.TestCase):
    FENCE = "`" * 3

    def _summary(self, body, name="handoff.md"):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / name
            path.write_text(body, encoding="utf-8")
            return session_state.handoff_summary(path)

    def test_reports_status_and_next_action(self):
        summary = self._summary(
            "# T\n\n**Status:** fresh reset.\n\n## Next action\n\nRun one fresh Japanese session:\n"
        )
        self.assertIn("status=fresh reset.", summary)
        self.assertIn("next=Run one fresh Japanese session", summary)

    def test_strips_the_trailing_colon_of_a_heading_line(self):
        summary = self._summary("# T\n\n**Status:** s.\n\n## Next action\n\nDo the thing:\n")
        self.assertTrue(summary.endswith("next=Do the thing"), summary)

    def test_skips_code_fences_and_finds_the_first_real_line(self):
        body = "# T\n\n**Status:** idle.\n\n## Next action\n\n" + self.FENCE + "text\nonly a block\n" + self.FENCE + "\n"
        self.assertIn("next=only a block", self._summary(body))

    def test_handles_crlf_line_endings(self):
        body = "# T\r\n\r\n**Status:** crlf status.\r\n\r\n## Next action\r\n\r\nRun the CRLF thing:\r\n"
        summary = self._summary(body)
        self.assertIn("status=crlf status.", summary)
        self.assertIn("next=Run the CRLF thing", summary)

    def test_missing_status_is_reported_not_hidden(self):
        self.assertIn("status=status unavailable", self._summary("# T\n\n## Next action\n\nDo it.\n"))

    def test_no_next_action_section_gives_an_actionable_pointer(self):
        summary = self._summary("# T\n\n**Status:** nothing pending.\n")
        self.assertIn("next=no explicit next-action section", summary)

    def test_untargeted_technical_handoff_names_the_missing_step(self):
        summary = self._summary("# T\n\n**Status:** no active target selected.\n")
        self.assertIn("next=learner names a target", summary)

    def test_missing_file_is_reported(self):
        self.assertEqual(session_state.handoff_summary(Path("does/not/exist.md")), "missing")


class IPlusOneLaneTests(unittest.TestCase):
    def _lane(self, ok, output):
        with patch.object(session_state, "run_readonly", return_value=(ok, output)):
            return session_state.iplusone_lane()

    def test_lane_is_read_from_the_bridge(self):
        payload = json.dumps({"lane": "patch", "unlearned_total": 9, "stuck_total": 1000})
        lane = self._lane(True, payload)
        self.assertIn("lane=patch", lane)
        self.assertIn("unlearned=9", lane)
        self.assertIn("stuck=1000", lane)

    def test_unreachable_anki_fails_closed_not_open(self):
        """An unavailable bridge must not read as permission to use new words."""
        lane = self._lane(False, "unavailable: error: connection refused")
        self.assertIn("lane=unavailable", lane)
        self.assertIn("do not assume new words are fine", lane)
        self.assertNotIn("lane=stretch", lane)

    def test_unparsable_output_fails_closed(self):
        lane = self._lane(True, "not json at all")
        self.assertIn("lane=unreadable", lane)
        self.assertIn("do not assume new words are fine", lane)

    def test_stretch_lane_is_reported_when_nothing_is_pending(self):
        payload = json.dumps({"lane": "stretch", "unlearned_total": 0, "stuck_total": 4})
        self.assertIn("lane=stretch", self._lane(True, payload))

    def test_today_surfaces_the_lane_on_the_japanese_line(self):
        payload = json.dumps({"lane": "patch", "unlearned_total": 9, "stuck_total": 1000})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "2026-09-27.md"
            with patch.object(session_state, "ROOT", Path(directory)), \
                    patch.object(session_state, "today_note", return_value=path), \
                    patch.object(session_state, "run_readonly", return_value=(True, payload)):
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    self.assertEqual(session_state.report_today(), 0)
            self.assertIn("i+1 lane=patch", buffer.getvalue())

    def test_lane_survives_a_bridge_that_never_returns(self):
        with patch.object(session_state, "run_readonly", return_value=(False, "")):
            self.assertIn("lane=unavailable", session_state.iplusone_lane())


if __name__ == "__main__":
    unittest.main()
