import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from question_signatures import normalize_prompt, prompt_reused, record_signatures, signature  # noqa: E402


class QuestionSignatureTests(unittest.TestCase):
    def test_normalization_ignores_formatting_only(self):
        self.assertEqual(normalize_prompt("  **What is `x`?**  "), "what is x?")

    def test_exact_prompt_reuse_is_detected(self):
        first = signature("What is the derivative of x^2?")
        self.assertTrue(prompt_reused("What is the derivative of x^2?", [first]))
        self.assertFalse(prompt_reused("What is the derivative of 2x?", [first]))

    def test_record_signatures_are_read_from_variant_table(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "session.md"
            digest = signature("What is the derivative of x^2?")
            path.write_text(
                "## Question variants\n"
                "| stage | prompt summary | normalized signature | reused? |\n"
                "|---|---|---|---|\n"
                f"| cold | derivative question | sha256:{digest} | no |\n",
                encoding="utf-8",
            )
            self.assertEqual(record_signatures(path), [f"sha256:{digest}"])
            self.assertTrue(prompt_reused("What is the derivative of x^2?", record_signatures(path)))


if __name__ == "__main__":
    unittest.main()
