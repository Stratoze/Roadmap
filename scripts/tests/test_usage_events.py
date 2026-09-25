import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import review  # noqa: E402


class UsageEventTests(unittest.TestCase):
    def test_append_is_idempotent_and_stays_inside_table(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evidence = root / "evidence.md"
            evidence.write_text("evidence", encoding="utf-8")
            topic = root / "topic.md"
            original = """# Topic

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| c1 | aim | - | review | 2 | 2099-01-01 | keep |

## Usage events
| date | event_id | concept/item_ref | event | evidence | public note |
|------|----------|------------------|-------|----------|-------------|

Usage events are appended by the session skill. This prose must stay below the table.
"""
            topic.write_text(original, encoding="utf-8")
            with patch.object(review, "ROOT", root):
                self.assertEqual(review.append_usage(topic, "topic", "c1", "practised", "evidence.md", "try"), 0)
                self.assertEqual(review.append_usage(topic, "topic", "c1", "practised", "evidence.md", "try"), 0)
            text = topic.read_text(encoding="utf-8")
            self.assertEqual(text.count("| c1 | aim | - | review | 2 | 2099-01-01 | keep |"), 1)
            self.assertEqual(len(list(review.read_usage_rows(text))), 1)
            self.assertLess(text.index("| 20"), text.index("Usage events are appended"))

    def test_reading_sessions_are_counted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            curriculum = root / "curriculum"
            curriculum.mkdir()
            evidence = root / "lesson.md"
            evidence.write_text("evidence", encoding="utf-8")
            topic = curriculum / "japanese-reading.md"
            topic.write_text(
                "# Reading\n\n## Usage events\n"
                "| date | event_id | concept/item_ref | event | evidence | public note |\n"
                "|------|----------|------------------|-------|----------|-------------|\n",
                encoding="utf-8",
            )
            with patch.object(review, "ROOT", root), patch.object(review, "CURRICULUM", curriculum):
                self.assertEqual(review.append_usage(topic, "japanese-reading", "read-30-session-gate", "reading_session", str(evidence), "page"), 0)
                self.assertEqual(review.append_usage(topic, "japanese-reading", "read-30-session-gate", "reading_session", str(evidence), "page two"), 0)
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    self.assertEqual(review.derived_usage("japanese-reading"), 0)
            self.assertIn("sessions=2", output.getvalue())

    def test_long_public_note_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evidence = root / "evidence.md"
            evidence.write_text("evidence", encoding="utf-8")
            topic = root / "topic.md"
            topic.write_text("# Topic\n", encoding="utf-8")
            with patch.object(review, "ROOT", root):
                self.assertEqual(review.append_usage(topic, "topic", "c1", "produced", "evidence.md", "x" * 241), 2)
    def test_missing_evidence_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            topic = root / "topic.md"
            topic.write_text("# Topic\n", encoding="utf-8")
            with patch.object(review, "ROOT", root):
                self.assertEqual(review.append_usage(topic, "topic", "c1", "produced", "missing.md", ""), 2)


if __name__ == "__main__":
    unittest.main()
