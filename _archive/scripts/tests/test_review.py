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

    def _frontier_output(self, root):
        output = io.StringIO()
        errors = io.StringIO()
        with (
            patch.object(review, "CURRICULUM", root),
            contextlib.redirect_stdout(output),
            contextlib.redirect_stderr(errors),
        ):
            self.assertEqual(review.cmd_frontier(), 0)
        return output.getvalue(), errors.getvalue()

    # --- due: evidence is stale, regardless of teaching order ---

    def test_due_ignores_unmet_prerequisites(self):
        """Regression: due once withheld concepts the learner had learned.

        Learners learn out of order. Withholding a concept you demonstrably
        learned defeats spaced review, and produced the incoherent queue where
        c5 was offered while its own prerequisite c4 was withheld.
        """
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "topic.md").write_text(
                "# t\n\n## Concepts\n"
                + self.HEADER
                + "| a | no prereq | - | review | 0 | 2000-01-01 | - |\n"
                + "| c | needs x, which was never taught | x | review | 0 | 2000-01-01 | - |\n"
                + "| x | never taught | - | unknown | 0 | - | - |\n",
                encoding="utf-8",
            )
            output = self._due_output(root)
            self.assertIn("| a |", output)
            # c's prerequisite is unknown, but c itself has real evidence.
            self.assertIn("| c |", output)

    def test_due_resolves_prerequisites_across_topic_files(self):
        """The concept index is global; a per-file map broke this."""
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

    # --- frontier: teaching order, the job `due` no longer does ---

    def test_frontier_lists_only_the_roots_of_the_unlearned_forest(self):
        """Downstream rows are reachable, so listing them is pure noise."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "topic.md").write_text(
                "# t\n\n## Concepts\n"
                + self.HEADER
                + "| base | learned | - | review | 0 | - | - |\n"
                + "| mid | needs base, not taught yet | base | unknown | 0 | - | - |\n"
                + "| deep | needs mid | mid | unknown | 0 | - | - |\n",
                encoding="utf-8",
            )
            output, errors = self._frontier_output(root)
            # `mid` is the only thing teachable right now.
            self.assertIn("| mid |", output)
            self.assertNotIn("| deep |", output)
            self.assertEqual(errors, "")
            self.assertIn("1 ready; 1 blocked", output)

    def test_frontier_treats_seen_as_unlearned_but_offerable(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "topic.md").write_text(
                "# t\n\n## Concepts\n"
                + self.HEADER
                + "| exposed | touched but not learned | - | seen | 0 | - | - |\n",
                encoding="utf-8",
            )
            output, _ = self._frontier_output(root)
            self.assertIn("| exposed |", output)
            self.assertIn("seen", output)

    def test_frontier_skips_learned_concepts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "topic.md").write_text(
                "# t\n\n## Concepts\n"
                + self.HEADER
                + "| done | learned | - | solid | 0 | - | - |\n"
                + "| kept | in rotation | - | review | 0 | - | - |\n",
                encoding="utf-8",
            )
            output, _ = self._frontier_output(root)
            self.assertNotIn("| done |", output)
            self.assertNotIn("| kept |", output)
            self.assertIn("0 ready; 0 blocked", output)

    def test_frontier_resolves_prerequisites_across_topic_files(self):
        """Regression: a per-file state map reported these as blocked forever."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "base.md").write_text(
                "# base\n\n## Concepts\n"
                + self.HEADER
                + "| shared | learned in another file | - | review | 0 | - | - |\n",
                encoding="utf-8",
            )
            (root / "dependent.md").write_text(
                "# dependent\n\n## Concepts\n"
                + self.HEADER
                + "| child | needs shared, in base.md | shared | unknown | 0 | - | - |\n",
                encoding="utf-8",
            )
            output, _ = self._frontier_output(root)
            self.assertIn("| child |", output)
            self.assertIn("1 ready; 0 blocked", output)

    def test_frontier_warns_on_a_dangling_prerequisite(self):
        """A typo must not silently strand a concept forever."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "topic.md").write_text(
                "# t\n\n## Concepts\n"
                + self.HEADER
                + "| a | typo in the prereq cell | does-not-exist | unknown | 0 | - | - |\n",
                encoding="utf-8",
            )
            output, errors = self._frontier_output(root)
            self.assertIn("does-not-exist", errors)
            self.assertNotIn("| a | ready", output)
            self.assertIn("0 ready; 1 blocked", output)

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
