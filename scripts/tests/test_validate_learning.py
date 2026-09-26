import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_learning  # noqa: E402
from question_signatures import prompt_signature, variant_signature  # noqa: E402

VARIANT_HEADER = (
    "| stage | prompt | values/conditions | context | prompt signature | "
    "variant signature | reused? |\n"
    "|-------|----------------|------------------|---------|------------------|------------------|---------|\n"
)


def variant_row(stage, prompt, values, context):
    return (
        f"| {stage} | {prompt} | {values} | {context} | "
        f"sha256:{prompt_signature(prompt)} | sha256:{variant_signature(values, context)} | no |\n"
    )


def write_record(root, topic, name, text):
    path = root / "_system" / "learning" / "lessons" / topic / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


class ValidateLearningTests(unittest.TestCase):
    def check(self, root):
        errors = []
        with patch.object(validate_learning, "ROOT", root):
            validate_learning.check_technical_records(errors)
        return errors

    def test_valid_separator_and_variant_table_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(
                root,
                "math-odes",
                "record.md",
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("cold", "What is the force?", "-", "-"),
            )
            self.assertEqual(self.check(root), [])

    def test_bare_reused_yes_is_disclosure_not_a_reason(self):
        """`reused? = yes` records that a repeat happened; it does not excuse it."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record = root / "_system" / "learning" / "lessons" / "math-odes" / "record.md"
            record.parent.mkdir(parents=True)
            record.write_text(
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("fresh transfer", "What is the force?", "m=5", "lift").replace("| no |", "| yes |"),
                encoding="utf-8",
            )
            # A single row cannot be a repeat, so the bare yes is simply recorded.
            self.assertEqual(self.check(root), [])

    def test_technical_record_requires_break_and_variants(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(root, "math-odes", "2026-09-27-record.md", "type: technical\n\n# Session\n")
            errors = self.check(root)
            self.assertTrue(any("missing break evidence" in error for error in errors), errors)
            self.assertTrue(any("missing question variants" in error for error in errors), errors)

    def test_legacy_marker_exempts_break_but_not_variants(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(root, "math-odes", "2026-09-27-record.md", "## Technical record status: legacy\n")
            errors = self.check(root)
            self.assertTrue(any("missing question variants" in error for error in errors), errors)
            self.assertFalse(any("missing break evidence" in error for error in errors), errors)

    def test_legacy_marker_cannot_be_used_to_claim_a_gate(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(
                root,
                "math-odes",
                "2026-09-27-record.md",
                "## Technical record status: legacy\n\n- gate_earned: mvm\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("cold", "What is the force?", "-", "-"),
            )
            errors = self.check(root)
            self.assertTrue(any("claims a gate" in error for error in errors), errors)

    def test_partially_written_technical_record_is_still_recognised(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(
                root,
                "math-odes",
                "2026-09-27-record.md",
                "## Cold conceptual check\n\n- Prompt: what is the force?\n",
            )
            errors = self.check(root)
            self.assertTrue(any("missing break evidence" in error for error in errors), errors)
            self.assertTrue(any("missing question variants" in error for error in errors), errors)

    def test_study_record_without_technical_markers_is_ignored(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(
                root,
                "japanese-grammar",
                "2026-09-14-potential.md",
                "# Godan potential\n\n## Attempts\n- learner work\n",
            )
            self.assertEqual(self.check(root), [])

    def test_same_question_with_same_values_and_scenario_is_refused(self):
        """The learner's rule: the same question, value and scenario must not
        happen twice - not after a day, not after a year."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for day, stage in (("2026-09-27", "cold"), ("2026-09-28", "fresh transfer")):
                write_record(
                    root,
                    "math-odes",
                    f"{day}-a.md",
                    "## Technical record status: legacy\n\n## Question variants\n"
                    + VARIANT_HEADER
                    + variant_row(stage, "Find the applied force.", "m=5 kg", "vertical lift"),
                )
            errors = self.check(root)
            self.assertTrue(any("test instance" in e for e in errors), errors)

    def test_same_question_with_different_values_is_a_different_instance(self):
        """Change the numbers and it is a new test, not a repeat."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(
                root, "math-odes", "2026-01-05-a.md",
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("cold", "Find the applied force.", "m=5 kg", "vertical lift"),
            )
            write_record(
                root, "math-odes", "2026-09-28-b.md",
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("cold", "Find the applied force.", "m=12 kg", "tilted push"),
            )
            self.assertEqual(self.check(root), [])

    def test_bare_reused_yes_is_disclosure_not_a_reason(self):
        """`reused? = yes` records that a repeat happened; it does not excuse it."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record = root / "_system" / "learning" / "lessons" / "math-odes" / "record.md"
            record.parent.mkdir(parents=True)
            record.write_text(
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("cold", "What is the force?", "m=5", "lift").replace("| no |", "| yes |"),
                encoding="utf-8",
            )
            # A single row cannot be a repeat, so the bare yes is simply recorded.
            self.assertEqual(self.check(root), [])

    def test_a_question_may_be_asked_twice_after_the_cooldown(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for day, values in (("2026-01-05", "m=5 kg"), ("2026-09-28", "m=12 kg")):
                write_record(
                    root, "math-odes", f"{day}-a.md",
                    "## Technical record status: legacy\n\n## Question variants\n"
                    + VARIANT_HEADER
                    + variant_row("cold", "Find the applied force.", values, "vertical lift"),
                )
            self.assertEqual(self.check(root), [])

    def test_a_question_repeated_inside_the_cooldown_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for day, values in (("2026-09-20", "m=5 kg"), ("2026-09-28", "m=12 kg")):
                write_record(
                    root, "math-odes", f"{day}-a.md",
                    "## Technical record status: legacy\n\n## Question variants\n"
                    + VARIANT_HEADER
                    + variant_row("cold", "Find the applied force.", values, "vertical lift"),
                )
            errors = self.check(root)
            self.assertTrue(any("cooldown" in e for e in errors), errors)

    def test_a_third_use_of_a_question_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for day, values in (
                ("2026-01-05", "m=5 kg"), ("2026-05-05", "m=12 kg"), ("2026-09-28", "m=20 kg")
            ):
                write_record(
                    root, "math-odes", f"{day}-a.md",
                    "## Technical record status: legacy\n\n## Question variants\n"
                    + VARIANT_HEADER
                    + variant_row("cold", "Find the applied force.", values, "vertical lift"),
                )
            errors = self.check(root)
            self.assertTrue(any("used more than 2 time(s)" in e for e in errors), errors)

    def test_a_recorded_reason_allows_the_repeat(self):
        """The escape hatch: "unless you can give a good reason"."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for day in ("2026-09-27", "2026-09-28"):
                write_record(
                    root, "math-odes", f"{day}-a.md",
                    "## Technical record status: legacy\n\n## Question variants\n"
                    + VARIANT_HEADER
                    + variant_row(
                        "cold", "Find the applied force.", "m=5 kg", "vertical lift"
                    ).replace("| no |", "| confirming retention after a lapse |"),
                )
            self.assertEqual(self.check(root), [])

    def test_a_bare_yes_is_not_a_reason(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for day in ("2026-09-27", "2026-09-28"):
                write_record(
                    root, "math-odes", f"{day}-a.md",
                    "## Technical record status: legacy\n\n## Question variants\n"
                    + VARIANT_HEADER
                    + variant_row("cold", "Find the applied force.", "m=5 kg", "vertical lift")
                    .replace("| no |", "| yes |"),
                )
            errors = self.check(root)
            self.assertTrue(any("no recorded reason" in e for e in errors), errors)

    def test_a_pure_concept_check_may_repeat_with_new_values(self):
        """Same concept, different numbers - the first-principles case."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for day, values in (("2026-01-05", "m=5 kg"), ("2026-09-28", "m=12 kg")):
                write_record(
                    root, "math-odes", f"{day}-a.md",
                    "## Technical record status: legacy\n\n## Question variants\n"
                    + VARIANT_HEADER
                    + variant_row("cold", "Define equilibrium.", values, "vertical lift"),
                )
            self.assertEqual(self.check(root), [])

    def test_reuse_is_checked_across_topics(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for topic in ("math-odes", "physics"):
                write_record(
                    root, topic, "2026-09-27-a.md",
                    "## Technical record status: legacy\n\n## Question variants\n"
                    + VARIANT_HEADER
                    + variant_row("fresh transfer", "Find the applied force.", "m=5 kg", "vertical lift"),
                )
            errors = self.check(root)
            self.assertTrue(any("test instance" in e for e in errors), errors)

    def test_missing_signature_record_path_fails_closed(self):
        errors = []
        text = validate_learning.signature_record_text(
            Path("does/not/exist.md"), "does/not/exist.md", errors
        )
        self.assertIsNone(text)
        self.assertEqual(errors, ["technical record path is missing: does/not/exist.md"])

    def test_signature_mismatch_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(
                root,
                "math-odes",
                "2026-09-27-record.md",
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + "| cold | What is the force? | m=5 | lift | sha256:" + "0" * 64 + " | sha256:" + "1" * 64 + " | no |\n",
            )
            errors = self.check(root)
            self.assertTrue(any("does not match stored prompt/variant" in error for error in errors), errors)


class ProtectedPathTests(unittest.TestCase):
    def check(self, statuses):
        errors = []
        with patch.object(validate_learning, "git_changed_paths", return_value=statuses):
            validate_learning.check_protected(errors)
        return errors

    def test_new_daily_note_is_allowed(self):
        self.assertEqual(self.check([({"??"}, "Daily/2026-09-26.md")]), [])
        self.assertEqual(self.check([({"A"}, "Daily/2026-09-26.md")]), [])

    def test_changed_existing_daily_note_is_still_blocked(self):
        errors = self.check([({"M"}, "Daily/2026-09-20.md")])
        self.assertEqual(errors, ["protected path changed: Daily/2026-09-20.md"])
        self.assertEqual(
            self.check([({"D"}, "Daily/2026-09-20.md")]),
            ["protected path changed: Daily/2026-09-20.md"],
        )

    def test_new_non_daily_file_under_daily_is_blocked(self):
        self.assertEqual(
            self.check([({"??"}, "Daily/scratch.md")]),
            ["protected path changed: Daily/scratch.md"],
        )

    def test_other_protected_paths_are_unchanged(self):
        self.assertEqual(
            self.check([({"M"}, "_system/learning/lessons/math-odes/2026-09-30-new-lesson.md")]),
            ["protected path changed: _system/learning/lessons/math-odes/2026-09-30-new-lesson.md"],
        )
        self.assertEqual(self.check([({"M"}, "scripts/review.py")]), [])

    def test_approved_migration_allowlist_still_wins(self):
        self.assertEqual(self.check([({"M"}, "Daily/2026-09-25.md")]), [])

    def test_porcelain_rename_keeps_the_new_path(self):
        parsed = validate_learning.parse_porcelain_z("R  Daily/2026-09-26.md\0Daily/2026-09-25.md\0?? Daily/2026-09-27.md\0")
        self.assertEqual(sorted(parsed), ["Daily/2026-09-26.md", "Daily/2026-09-27.md"])
        self.assertEqual(parsed["Daily/2026-09-26.md"], {"R"})
        self.assertEqual(parsed["Daily/2026-09-27.md"], {"??"})
        self.assertTrue(validate_learning.is_new_daily_note(parsed["Daily/2026-09-27.md"], "Daily/2026-09-27.md"))

    def test_porcelain_status_is_one_value_not_one_character(self):
        parsed = validate_learning.parse_porcelain_z("?? Daily/2026-09-27.md\0 M Daily/2026-09-20.md\0A  Daily/2026-09-28.md\0")
        self.assertEqual(parsed["Daily/2026-09-27.md"], {"??"})
        self.assertEqual(parsed["Daily/2026-09-20.md"], {"M"})
        self.assertEqual(parsed["Daily/2026-09-28.md"], {"A"})


if __name__ == "__main__":
    unittest.main()
