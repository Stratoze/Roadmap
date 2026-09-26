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
                + variant_row("cold", "What is the force?", "m=5", "lift"),
            )
            self.assertEqual(self.check(root), [])

    def test_reused_or_malformed_variant_is_rejected(self):
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
            errors = self.check(root)
            self.assertTrue(any("reused" in error for error in errors), errors)

    def test_cold_check_may_disclose_a_repeat_honestly(self):
        """An agent must be able to record the truth on a permitted repeat."""
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
                + variant_row("cold", "What is the force?", "m=5", "lift"),
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

    def test_repeated_prompt_in_the_same_topic_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(
                root,
                "math-odes",
                "2026-09-27-a.md",
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("cold", "What is the force?", "m=5", "lift")
                + variant_row("fresh transfer", "What is the force?", "m=9", "push"),
            )
            write_record(
                root,
                "math-odes",
                "2026-09-28-b.md",
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("cold", "What is the force?", "m=7", "haul"),
            )
            errors = self.check(root)
            # Only the fresh transfer is a violation: it re-asked the question
            # the cold check had just spent. The later cold check re-asking the
            # same concept is retention testing, which the decision allows.
            self.assertEqual(
                sum("reuses a prompt signature" in error for error in errors),
                1,
                errors,
            )
            self.assertTrue(any("fresh transfer" in error for error in errors), errors)

    def test_cold_check_may_repeat_a_concept(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(
                root,
                "math-odes",
                "2026-09-27-a.md",
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("cold", "Define equilibrium.", "-", "-"),
            )
            write_record(
                root,
                "math-odes",
                "2026-09-28-b.md",
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("cold", "Define equilibrium.", "-", "-"),
            )
            self.assertEqual(self.check(root), [])

    def test_cold_check_after_a_transfer_still_fails_a_transfer(self):
        """The stage being checked decides, not the stage that used it first."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(
                root,
                "math-odes",
                "2026-09-27-a.md",
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("cold", "Find the applied force.", "m=5 kg", "vertical lift"),
            )
            write_record(
                root,
                "math-odes",
                "2026-09-28-b.md",
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("implementation", "Find the applied force.", "m=5 kg", "vertical lift"),
            )
            errors = self.check(root)
            self.assertTrue(any("reuses a variant signature" in error for error in errors), errors)

    def test_repeated_test_instance_in_the_same_topic_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_record(
                root,
                "math-odes",
                "2026-09-27-a.md",
                "## Technical record status: legacy\n\n## Question variants\n"
                + VARIANT_HEADER
                + variant_row("cold", "Find the applied force.", "m=5 kg", "vertical lift")
                + variant_row("implementation", "Compute the load.", "m=5 kg", "vertical lift"),
            )
            errors = self.check(root)
            self.assertTrue(any("reuses a variant signature" in error for error in errors), errors)

    def test_same_prompt_in_another_topic_scope_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for topic in ("math-odes", "physics"):
                write_record(
                    root,
                    topic,
                    "2026-09-27-record.md",
                    "## Technical record status: legacy\n\n## Question variants\n"
                    + VARIANT_HEADER
                    + variant_row("fresh transfer", "What is the force?", "m=5", "lift"),
                )
            errors = self.check(root)
            self.assertTrue(any("reuses a prompt signature" in error for error in errors), errors)

    def test_cold_check_may_repeat_across_topics(self):
        """Reuse is corpus-wide, but a cold check re-asking a concept is allowed."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for topic in ("math-odes", "physics"):
                write_record(
                    root,
                    topic,
                    "2026-09-27-record.md",
                    "## Technical record status: legacy\n\n## Question variants\n"
                    + VARIANT_HEADER
                    + variant_row("cold", "What is the force?", "m=5", "lift"),
                )
            self.assertEqual(self.check(root), [])

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
