import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class TechnicalSessionTests(unittest.TestCase):
    def test_template_contains_required_evidence_stages(self):
        text = (ROOT / "_templates" / "learning" / "technical_session.md").read_text(encoding="utf-8")
        for heading in ("## Cold conceptual check", "## Break", "## Fresh transfer", "## Implementation/theory test", "## Feynman repair", "## Assessor"):
            self.assertIn(heading, text)
        self.assertIn("| cold | | | |", text)
        self.assertNotIn("| fresh transfer | | | no |", text)
        self.assertNotIn("| implementation | | | no |", text)

    def test_technical_skill_has_the_full_sequence(self):
        text = (ROOT / ".dsh" / "skills" / "technical" / "SKILL.md").read_text(encoding="utf-8")
        for marker in ("Learner reads", "Cold conceptual check", "Break", "Fresh transfer", "Implementation/theory", "Feynman repair", "Assessor", "question_signatures.py"):
            self.assertIn(marker, text)

    def test_assessor_has_gate_output(self):
        text = (ROOT / ".dsh" / "agents" / "assessor.md").read_text(encoding="utf-8")
        for field in ("gate_requested", "gate_met", "gate_earned", "partial` or `lapsed", "action: shell"):
            self.assertIn(field, text)


if __name__ == "__main__":
    unittest.main()
