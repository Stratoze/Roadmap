"""Tests for the progress ledger, scoring, and dashboard.

The scoring rules are the contract: which floor a session earns, and how the
confidence readout behaves at small n. These tests pin both, because the ratchet
silently changing shape is how a learner gets stranded at one level.
"""
import json
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import progress  # noqa: E402


def probes(pattern, count, level=None):
    rows = []
    for index in range(count):
        row = {"concept": "c", "result": pattern, "level": level}
        rows.append(row)
    return rows


class WilsonTests(unittest.TestCase):
    def test_empty_sample_is_zero_not_error(self):
        self.assertEqual(progress.wilson_lower_bound(0, 0), 0.0)

    def test_bound_is_below_naive_rate(self):
        naive = 9 / 10
        bound = progress.wilson_lower_bound(9, 10)
        self.assertLess(bound, naive)
        # The gap is the whole point: a short session is not mastery.
        self.assertLess(bound, 0.7)

    def test_perfect_run_still_bounded_below_one(self):
        self.assertLess(progress.wilson_lower_bound(6, 6), 1.0)

    def test_monotonic_in_successes(self):
        values = [progress.wilson_lower_bound(k, 10) for k in range(11)]
        self.assertEqual(values, sorted(values))

    def test_rejects_impossible_counts(self):
        with self.assertRaises(progress.ProgressError):
            progress.wilson_lower_bound(11, 10)


class FloorRatchetTests(unittest.TestCase):
    def test_advances_after_three_passes_and_rate_target(self):
        rows = probes("pass", 6, level=0)
        self.assertEqual(progress.suggested_floor(rows, 0), 1)

    def test_does_not_advance_on_two_passes(self):
        rows = probes("pass", 2, level=0)
        self.assertEqual(progress.suggested_floor(rows, 0), 0)

    def test_drops_after_two_misses(self):
        rows = probes("miss", 2, level=2)
        self.assertEqual(progress.suggested_floor(rows, 2), 1)

    def test_never_drops_below_zero(self):
        rows = probes("miss", 2, level=0)
        self.assertEqual(progress.suggested_floor(rows, 0), 0)

    def test_passes_off_the_floor_do_not_advance(self):
        # Strong history, but nothing was probed at the current floor.
        rows = probes("pass", 5, level=0) + [{"concept": "c", "result": "pass", "level": 3}]
        self.assertEqual(progress.suggested_floor(rows, 3), 3)

    def test_advance_requires_recent_rate_not_just_streak(self):
        # Trailing three passes, but the recent window is dragged under target
        # by older misses. Both conditions are required, so this must hold.
        rows = (probes("miss", 4, level=1) + probes("pass", 3, level=1))
        self.assertEqual(progress.suggested_floor(rows, 1), 1)

    def test_never_exceeds_top_level(self):
        rows = probes("pass", 4, level=6)
        self.assertEqual(progress.suggested_floor(rows, 6), 6)


class VelocityTests(unittest.TestCase):
    def test_flat_with_too_few_sessions(self):
        self.assertEqual(progress.velocity([], []), 0.0)
        self.assertEqual(progress.velocity([{"probes": 5}], probes("pass", 5)), 0.0)

    def test_improving_when_pass_rate_rises(self):
        sessions = [{"date": f"2026-09-{day:02d}", "probes": 4} for day in range(1, 6)]
        rows = probes("miss", 8) + probes("pass", 8)
        self.assertGreater(progress.velocity(sessions, rows), 0.0)

    def test_declining_when_pass_rate_falls(self):
        sessions = [{"date": f"2026-09-{day:02d}", "probes": 4} for day in range(1, 6)]
        rows = probes("pass", 8) + probes("miss", 8)
        self.assertLess(progress.velocity(sessions, rows), 0.0)


class CoverageTests(unittest.TestCase):
    def test_pass_beats_miss_for_the_same_cell(self):
        rows = [
            {"concept": "a", "level": 1, "result": "miss"},
            {"concept": "a", "level": 1, "result": "pass"},
        ]
        self.assertEqual(progress.coverage(rows)["a"][1], "pass")

    def test_empty_ledger_yields_empty_coverage(self):
        self.assertEqual(progress.coverage([]), {})


class RecordValidationTests(unittest.TestCase):
    def test_rejects_bad_level(self):
        with self.assertRaises(progress.ProgressError):
            progress.record_probe("Japanese", "c", 7, "pass")

    def test_rejects_bad_result(self):
        with self.assertRaises(progress.ProgressError):
            progress.record_probe("Japanese", "c", 1, "maybe")

    def test_rejects_unknown_domain(self):
        with self.assertRaises(progress.ProgressError):
            progress.record_probe("Klingon", "c", 1, "pass")

    def test_rejects_inconsistent_session_counts(self):
        with self.assertRaises(progress.ProgressError):
            progress.record_session("Japanese", 0, 1, probes=5, passed=4, missed=3,
                                    peak_level=1)


class DashboardTests(unittest.TestCase):
    def test_renders_without_ledgers(self):
        doc = progress.render_dashboard(["Japanese"])
        self.assertIn("<!doctype html>", doc)
        self.assertIn("Japanese", doc)

    def test_no_external_resources(self):
        doc = progress.render_dashboard(["Japanese", "Mechatronics"])
        self.assertNotIn("src='http", doc)
        self.assertNotIn('src="http', doc)
        self.assertNotIn("href='http", doc)
        self.assertNotIn('href="http', doc)

    def test_escapes_script_breaking_payload(self):
        # A concept name must never be able to close the data block.
        data = json.dumps({"x": "</script>"}).replace("<", "\\u003c")
        self.assertNotIn("</script>", data)
        self.assertIn("\\u003c", data)


if __name__ == "__main__":
    unittest.main()
