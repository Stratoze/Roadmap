import contextlib
import io
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
            self.assertEqual(run.call_count, 2)

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


if __name__ == "__main__":
    unittest.main()
