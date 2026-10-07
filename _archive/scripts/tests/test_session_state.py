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
            # review.py due, anki_bridge.py iplusone, review.py frontier,
            # anki_bridge.py due.
            self.assertEqual(run.call_count, 4)

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


class TechnicalNextTests(unittest.TestCase):
    ROADMAP = (
        "| Phase | Milestone | Status | Deliverable | Depends on | Search keywords | Safety/evidence boundary |\n"
        "|---|---|---|---|---|---|---|\n"
        "| 0 | [0.1 Toolchain](milestones/f.md) | ✅ | setup | — | a; b | clean |\n"
        "| 0 | [0.3 Calculus](milestones/f.md) | ⬜ | derivative meaning | 0.1 | rate; Euler | formula is not evidence |\n"
    )
    MILESTONE = (
        "# Milestone 0.1 — Toolchain\n\n### MVM\n- [ ] a generic item\n\n"
        "# Milestone 0.3 — Calculus\n\n### MVM\n- [ ] take a derivative\n- [ ] integrate with limits\n\n"
        "### Full Pass\n- [ ] chain position to acceleration\n"
    )

    def _vault(self, root):
        (root / "Mechatronics" / "milestones").mkdir(parents=True)
        (root / "Mechatronics" / "ROADMAP.md").write_text(self.ROADMAP, encoding="utf-8")
        (root / "Mechatronics" / "milestones" / "f.md").write_text(self.MILESTONE, encoding="utf-8")
        return root

    def test_first_open_milestone_is_reported_with_deps_and_keywords(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self._vault(Path(directory))
            with patch.object(session_state, "ROOT", root):
                out = "\n".join(session_state.technical_next())
            self.assertIn("0.3 Calculus", out)
            self.assertIn("derivative meaning", out)
            self.assertIn("rate; Euler", out)
            self.assertIn("formula is not evidence", out)

    def test_met_dependencies_are_not_reported_as_unmet(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self._vault(Path(directory))
            with patch.object(session_state, "ROOT", root):
                out = "\n".join(session_state.technical_next())
            self.assertIn("all met", out)
            self.assertNotIn("UNMET", out)

    def test_unmet_dependency_is_named(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self._vault(Path(directory))
            roadmap = (root / "Mechatronics" / "ROADMAP.md").read_text(encoding="utf-8")
            # 0.9 has no row at all, so 0.3 is still the first open milestone
            # but one of its dependencies cannot be met.
            (root / "Mechatronics" / "ROADMAP.md").write_text(
                roadmap.replace("| derivative meaning | 0.1 |", "| derivative meaning | 0.1, 0.9 |"),
                encoding="utf-8",
            )
            with patch.object(session_state, "ROOT", root):
                out = "\n".join(session_state.technical_next())
            self.assertIn("0.3 Calculus", out)
            self.assertIn("UNMET: 0.9", out)

    def test_pass_items_are_scoped_to_the_chosen_milestone(self):
        """A milestone file holds a pass bar per milestone plus a generic one."""
        with tempfile.TemporaryDirectory() as directory:
            root = self._vault(Path(directory))
            with patch.object(session_state, "ROOT", root):
                out = "\n".join(session_state.technical_next())
            self.assertIn("take a derivative", out)
            self.assertIn("chain position to acceleration", out)
            self.assertNotIn("a generic item", out)

    def test_no_open_milestone_says_so(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "Mechatronics").mkdir()
            (root / "Mechatronics" / "ROADMAP.md").write_text(
                self.ROADMAP.replace("⬜", "✅"), encoding="utf-8"
            )
            with patch.object(session_state, "ROOT", root):
                out = "\n".join(session_state.technical_next())
            self.assertIn("every milestone", out)

    def test_missing_roadmap_degrades_quietly(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(session_state, "ROOT", Path(directory)):
                self.assertEqual(session_state.technical_next(), [])

    def test_ready_to_teach_reports_technical_concepts_only(self):
        output = (
            "math-odes | c2 | unknown | ready to teach\n"
            "math-odes | c9 | unknown | ready to teach\n"
            "m0-1-problem-solving | m1-1 | unknown | ready to teach\n"
            "jp-yokubi-00 | unknown | ready to teach\n"
            "21 ready; 137 blocked behind unmet prerequisites\n"
        )
        with patch.object(session_state, "run_readonly", return_value=(True, output)):
            line = session_state.technical_ready()
        self.assertIn("math-odes/c2", line)
        self.assertIn("math-odes/c9", line)
        # The m0-* files mirror the ROADMAP rows already printed; repeating them
        # is noise, and Japanese is the other lane entirely.
        self.assertNotIn("m1-1", line)
        self.assertNotIn("jp-yokubi", line)

    def test_ready_to_teach_fails_closed_when_frontier_is_down(self):
        with patch.object(session_state, "run_readonly", return_value=(False, "broken")):
            line = session_state.technical_ready()
        self.assertIn("unknown", line)

    def test_ready_to_teach_says_so_when_nothing_is_unblocked(self):
        output = "jp-yokubi-00 | unknown | ready to teach\n21 ready; 0 blocked\n"
        with patch.object(session_state, "run_readonly", return_value=(True, output)):
            line = session_state.technical_ready()
        self.assertIn("no open technical concept", line)


if __name__ == "__main__":
    unittest.main()
