import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
try:
    import validate_learning
    from question_signatures import prompt_signature, variant_signature
except ImportError:  # pragma: no cover - the validator owns its own tests
    validate_learning = None

TEMPLATE = ROOT / "_templates" / "learning" / "technical_session.md"
SKILL = ROOT / ".dsh" / "skills" / "technical" / "SKILL.md"
ASSESSOR = ROOT / ".dsh" / "agents" / "assessor.md"
MILESTONE = ROOT / "scripts" / "milestone.sh"
BASH = shutil.which("bash")

VARIANT_ROWS = (
    ("cold", "What limits the steady-state error?", "Kp=2; e_ss=0.5 V", "unity feedback"),
    ("fresh transfer", "Why does the same loop settle slower here?", "T=4 s; Kp=0.4", "thermal plant"),
    ("implementation", "Step the discrete update by hand.", "dt=1 s; T=4", "table build"),
)


class TechnicalSessionTests(unittest.TestCase):
    def test_template_contains_required_evidence_stages(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        for heading in ("## Cold conceptual check", "## Break", "## Question variants", "## Implementation/theory test", "## Feynman repair", "## Assessor"):
            self.assertIn(heading, text)
        self.assertIn("| cold | | | |", text)
        self.assertNotIn("| fresh transfer | | | no |", text)
        self.assertNotIn("| implementation | | | no |", text)

    def test_template_demands_real_break_and_variant_evidence(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        self.assertNotIn("pending", text.lower())
        self.assertIn("- Start (ISO):", text)
        self.assertIn("- End (ISO):", text)
        self.assertIn("20 minutes", text)
        # The unfilled rows must stay: a copied template that was never completed
        # has to fail validation instead of reading as a finished record.
        for stage in ("cold", "fresh transfer", "implementation"):
            self.assertIn(f"| {stage} | | | | | | |", text)
        self.assertIn("## Record validity", text)
        self.assertIn("validate_learning.py", text)

    def test_technical_skill_has_the_full_sequence(self):
        text = SKILL.read_text(encoding="utf-8")
        for marker in ("Learner reads", "Cold conceptual check", "Break", "Fresh transfer", "Implementation/theory", "Feynman repair", "Assessor", "question_signatures.py"):
            self.assertIn(marker, text)

    def test_technical_skill_checks_reuse_across_topic_records(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("--record _system/learning/lessons\n", text)
        self.assertNotIn("--record _system/learning/lessons/<topic>", text.split("## Question and test variants")[1])
        self.assertIn("checked across all of them", text)
        self.assertIn("## Record validity", text)
        self.assertIn("scripts/validate_learning.py", text)

    def test_assessor_has_gate_output(self):
        text = ASSESSOR.read_text(encoding="utf-8")
        for field in ("gate_requested", "gate_met", "gate_earned", "partial` or `lapsed", "action: shell"):
            self.assertIn(field, text)

    def test_assessor_gate_block_is_machine_readable(self):
        text = ASSESSOR.read_text(encoding="utf-8")
        self.assertIn("## Gate output contract", text)
        self.assertIn("Never emit the option list", text)
        self.assertIn("## Missing evidence is a failed gate", text)
        for missing in ("20 minutes", "fresh-transfer or implementation", "reused"):
            self.assertIn(missing, text)

    def test_milestone_tag_requires_assessor_gate(self):
        text = MILESTONE.read_text(encoding="utf-8")
        for marker in ("--gate", "--evidence", "gate_earned", "git tag -s"):
            self.assertIn(marker, text)


def filled_record(template):
    """A fully completed technical record built from the shipped template."""
    text = (template
            .replace("{{date:YYYY-MM-DD}}", "2026-10-01")
            .replace("{{title}}", "damping")
            .replace("{{topic}}", "m0-6-power-thermal"))
    text = text.replace("- Start (ISO):", "- Start (ISO): 2026-10-01T10:00:00+09:00")
    text = text.replace("- End (ISO):", "- End (ISO): 2026-10-01T10:24:00+09:00")
    text = text.replace("- Elapsed minutes:", "- Elapsed minutes: 24")
    text = text.replace(
        "- Verified 20-minute interval: (yes only when Start/End above prove at least 20 minutes)",
        "- Verified 20-minute interval: yes",
    )
    rows = [
        f"| {stage} | {prompt} | {values} | {context} | "
        f"sha256:{prompt_signature(prompt)} | sha256:{variant_signature(values, context)} | no |"
        for stage, prompt, values, context in VARIANT_ROWS
    ]
    lines = []
    for line in text.splitlines():
        if any(line.startswith(f"| {stage} | | | |") for stage, _p, _v, _c in VARIANT_ROWS):
            lines.append(rows.pop(0))
        else:
            lines.append(line)
    return "\n".join(lines) + "\n"


@unittest.skipUnless(validate_learning is not None, "validate_learning.py is required")
class TemplateValidatorContractTests(unittest.TestCase):
    """The template is only a record once it carries real break and variant evidence."""

    def errors_for(self, body):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record = root / "_system" / "learning" / "lessons" / "m0-6" / "2026-10-01-record.md"
            record.parent.mkdir(parents=True)
            record.write_text(body, encoding="utf-8")
            errors = []
            with patch.object(validate_learning, "ROOT", root):
                validate_learning.check_technical_records(errors)
            return errors

    def test_a_completed_record_passes_validation(self):
        self.assertEqual(self.errors_for(filled_record(TEMPLATE.read_text(encoding="utf-8"))), [])

    def test_an_unfilled_template_is_not_a_record(self):
        errors = self.errors_for(TEMPLATE.read_text(encoding="utf-8"))
        self.assertTrue(errors)
        self.assertTrue(any("signature" in error for error in errors), errors)
        self.assertTrue(any("break" in error for error in errors), errors)

    def test_a_short_break_is_rejected(self):
        body = filled_record(TEMPLATE.read_text(encoding="utf-8")).replace(
            "2026-10-01T10:24:00+09:00", "2026-10-01T10:04:00+09:00"
        )
        self.assertTrue(any("20 minutes" in error for error in self.errors_for(body)))

    def test_a_reused_variant_is_rejected(self):
        body = filled_record(TEMPLATE.read_text(encoding="utf-8")).replace("| no |", "| yes |")
        self.assertTrue(any("reused" in error for error in self.errors_for(body)))


@unittest.skipUnless(BASH, "bash is required to exercise scripts/milestone.sh")
class MilestoneGateTests(unittest.TestCase):
    def check(self, evidence_text, gate="mvm"):
        with tempfile.TemporaryDirectory() as directory:
            evidence = Path(directory) / "evidence.md"
            evidence.write_text(evidence_text, encoding="utf-8")
            return subprocess.run(
                [BASH, str(MILESTONE), "v-tag", "what proves it",
                 "--gate", gate, "--evidence", str(evidence), "--check-only"],
                cwd=ROOT, capture_output=True, text=True,
            )

    def test_canonical_bullet_gate_record_is_accepted(self):
        result = self.check("- gate_met: yes\n- gate_earned: mvm\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("gate ok", result.stdout)

    def test_placeholder_option_lists_are_refused(self):
        for text in ("- gate_met: yes/no\n- gate_earned: mvm/full/none\n", "- gate_earned: mvm | full | none\n"):
            result = self.check(text)
            self.assertEqual(result.returncode, 2, text)
            self.assertIn("gate_earned", result.stderr)

    def test_lapsed_or_missing_gate_is_refused(self):
        for text in ("- gate_met: no\n- gate_earned: none\n", "no gate fields here\n"):
            result = self.check(text)
            self.assertEqual(result.returncode, 2, text)
            self.assertIn("gate", result.stderr)

    def test_older_gate_claim_cannot_tag_over_a_later_verdict(self):
        result = self.check("- gate_earned: mvm\n- gate_earned: none\n")
        self.assertEqual(result.returncode, 2)
        self.assertIn("last gate_earned", result.stderr)

    def test_gate_must_match_the_earned_gate(self):
        result = self.check("- gate_met: yes\n- gate_earned: full\n", gate="mvm")
        self.assertEqual(result.returncode, 2)
        self.assertIn("not 'mvm'", result.stderr)
        self.assertEqual(self.check("- gate_met: yes\n- gate_earned: full\n", gate="full").returncode, 0)

    def test_gate_met_must_be_yes(self):
        for text in ("- gate_met: no\n- gate_earned: mvm\n", "- gate_earned: mvm\n"):
            result = self.check(text)
            self.assertEqual(result.returncode, 2, text)
            self.assertIn("gate_met", result.stderr)

    def test_bad_arguments_are_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            evidence = Path(directory) / "evidence.md"
            evidence.write_text("- gate_met: yes\n- gate_earned: mvm\n", encoding="utf-8")
            base = [BASH, str(MILESTONE), "v-tag", "msg"]
            for argv in (
                base + ["--gate", "mvm", "--evidence", str(Path(directory) / "absent.md"), "--check-only"],
                base + ["--gate", "mvm"],
                base + ["--gate", "half", "--evidence", str(evidence), "--check-only"],
                base + ["--evidence", str(evidence), "--check-only"],
                base + ["--gate", "mvm", "--evidence", str(evidence), "--unknown"],
            ):
                result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
                self.assertEqual(result.returncode, 2, argv)


if __name__ == "__main__":
    unittest.main()
