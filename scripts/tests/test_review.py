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


class ReviewTests(unittest.TestCase):
    HEADER = (
        "| id | aim | prereqs | state | rung | next_review | evidence |\n"
        "|----|-----|---------|-------|------|-------------|----------|\n"
    )

    def _due_output(self, root):
        output = io.StringIO()
        with patch.object(review, "CURRICULUM", root), contextlib.redirect_stdout(output):
            self.assertEqual(review.cmd_due(), 0)
        return output.getvalue()

    def test_due_hides_items_whose_prerequisites_are_unmet(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "topic.md").write_text(
                "# t\n\n## Concepts\n"
                + self.HEADER
                + "| a | no prereq | - | review | 0 | 2000-01-01 | - |\n"
                + "| b | needs a | a | review | 0 | 2000-01-01 | - |\n"
                + "| c | needs x, unlearned | x | review | 0 | 2000-01-01 | - |\n"
                + "| x | not learned yet | - | unknown | 0 | 2000-01-01 | - |\n",
                encoding="utf-8",
            )
            output = self._due_output(root)
            # a and b are due: b's prerequisite a is learned.
            self.assertIn("| a |", output)
            self.assertIn("| b |", output)
            # c's prerequisite x is still unknown, so c must not be offered.
            # cmd_due gates on prerequisites, not on state, so x itself is
            # still listed by date -- that is existing behaviour, not the gate.
            self.assertNotIn("| c |", output)

    def test_due_resolves_prerequisites_across_topic_files(self):
        """Regression: a per-file state map hid cross-file dependents forever."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "base.md").write_text(
                "# base\n\n## Concepts\n"
                + self.HEADER
                + "| shared | learned in another file | - | review | 0 | 2000-01-01 | - |\n",
                encoding="utf-8",
            )
            (root / "dependent.md").write_text(
                "# dependent\n\n## Concepts\n"
                + self.HEADER
                + "| child | depends on a concept in base.md | shared | review | 0 | 2000-01-01 | - |\n",
                encoding="utf-8",
            )
            output = self._due_output(root)
            self.assertIn("| child |", output)

    def test_due_warns_on_dangling_prerequisite_instead_of_hiding_silently(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "topic.md").write_text(
                "# t\n\n## Concepts\n"
                + self.HEADER
                + "| a | typo in the prereq cell | does-not-exist | review | 0 | 2000-01-01 | - |\n",
                encoding="utf-8",
            )
            output = io.StringIO()
            errors = io.StringIO()
            with (
                patch.object(review, "CURRICULUM", root),
                contextlib.redirect_stdout(output),
                contextlib.redirect_stderr(errors),
            ):
                self.assertEqual(review.cmd_due(), 0)
            self.assertNotIn("| a |", output.getvalue())
            self.assertIn("does-not-exist", errors.getvalue())

    def test_due_ignores_rows_with_an_unparsable_date(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "topic.md").write_text(
                "# t\n\n## Concepts\n"
                + self.HEADER
                + "| a | no date yet | - | review | 0 | - | - |\n",
                encoding="utf-8",
            )
            self.assertEqual(self._due_output(root), "")

    def test_concept_parser_keeps_seven_column_rows(self):
        text = """# t

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| c1 | aim | - | review | 2 | 2099-01-01 | evidence |
"""
        self.assertEqual([cells[0] for _, cells in review.read_rows(text)], ["c1"])

    def test_usage_parser_ignores_header_and_separator(self):
        text = """# t

## Usage events
| date | event_id | concept/item_ref | event | evidence | public note |
|------|----------|------------------|-------|----------|-------------|
| 2026-09-27 | e1 | c1 | practised | scripts/review.py | try |
"""
        rows = list(review.read_usage_rows(text))
        self.assertEqual(len(rows), 1)
        self.assertIsNone(rows[0][2])

    def test_usage_event_id_is_stable(self):
        first = review.usage_event_id("topic", "id", "produced", "scripts/review.py", "2026-09-27")
        second = review.usage_event_id("topic", "id", "produced", "scripts/review.py", "2026-09-27")
        self.assertEqual(first, second)
        self.assertEqual(len(first), 12)

    def test_outcome_ladder(self):
        self.assertEqual(review.apply_outcome("review", 2, "hit"), ("review", 3))
        self.assertEqual(review.apply_outcome("review", 3, "hit"), ("solid", 4))
        self.assertEqual(review.apply_outcome("solid", 4, "miss"), ("review", 3))
        self.assertEqual(review.apply_outcome("review", 0, "miss"), ("review", 0))
        self.assertEqual(review.apply_outcome("review", 3, "hard"), ("review", 3))
        self.assertEqual(review.apply_outcome("unknown", 0, "hit"), ("review", 1))
        self.assertEqual(review.apply_outcome("seen", 0, "hard"), ("review", 0))
        self.assertEqual(review.apply_outcome("solid", 4, "hard"), ("review", 4))

    def test_reading_gate_id_is_the_single_source(self):
        self.assertEqual(review.READING_GATE_TOPIC, "japanese-reading")
        self.assertEqual(review.READING_GATE_ID, "read-30-session-gate")
        self.assertEqual(review.READING_GATE, ("japanese-reading", "read-30-session-gate"))
        self.assertEqual(review.BASELINE_USAGE_IDS, {"japanese-reading": ["read-30-session-gate"]})
        self.assertIn("read-30-session-gate", review.__doc__)
        curriculum = ROOT / "_system" / "learning" / "curriculum" / "japanese-reading.md"
        self.assertIn(f"| {review.READING_GATE_ID} |", curriculum.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
