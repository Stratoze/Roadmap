import datetime as dt
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import review  # noqa: E402


class ReviewTests(unittest.TestCase):
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
