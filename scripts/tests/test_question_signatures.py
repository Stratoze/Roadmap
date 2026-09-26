import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import question_signatures  # noqa: E402
from question_signatures import (  # noqa: E402
    normalize_prompt,
    prompt_reused,
    prompt_signature,
    record_signatures,
    variant_signature,
)


class QuestionSignatureTests(unittest.TestCase):
    def test_normalization_ignores_formatting_only(self):
        self.assertEqual(normalize_prompt("  **What is `x`?**  "), "what is x?")

    def test_exact_prompt_reuse_is_detected(self):
        first = prompt_signature("What is the derivative of x^2?")
        self.assertTrue(prompt_reused("What is the derivative of x^2?", [first]))
        self.assertFalse(prompt_reused("What is the derivative of 2x?", [first]))

    def test_same_values_are_detected_even_with_new_wording(self):
        values = "m=5 kg; a=2 m/s^2"
        context = "vertical lift"
        first = variant_signature(values, context)
        self.assertTrue(prompt_reused("Find the applied force.", [first], values, context))
        self.assertFalse(prompt_reused("Find the applied force.", [first], "m=12 kg; a=2 m/s^2", context))

    def test_prompt_and_variant_are_checked_independently(self):
        prompt_digest = prompt_signature("What force is needed?")
        variant_digest = variant_signature("m=5 kg", "lift")
        records = {"prompt": {prompt_digest}, "variant": {variant_digest}}
        self.assertTrue(prompt_reused("What force is needed?", records["prompt"]))
        self.assertTrue(prompt_reused("What force is required?", records["variant"], "m=5 kg", "lift"))

    def test_record_signatures_are_read_from_variant_table(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "session.md"
            prompt_digest = prompt_signature("What is the derivative of x^2?")
            variant_digest = variant_signature("x=2; y=3", "toy example")
            path.write_text(
                "## Question variants\n"
                "| stage | prompt | values/conditions | context | prompt signature | variant signature | reused? |\n"
                "|---|---|---|---|---|---|---|\n"
                f"| cold | derivative question | x=2; y=3 | toy example | sha256:{prompt_digest} | sha256:{variant_digest} | no |\n",
                encoding="utf-8",
            )
            records = record_signatures(path)
            self.assertIn(prompt_digest, records["prompt"])
            self.assertIn(variant_digest, records["variant"])


def variant_row(prompt, values, context):
    return (
        f"| fresh transfer | {prompt} | {values} | {context} | "
        f"sha256:{prompt_signature(prompt)} | sha256:{variant_signature(values, context)} | no |\n"
    )


TABLE = (
    "## Question variants\n"
    "| stage | prompt | values/conditions | context | prompt signature | variant signature | reused? |\n"
    "|---|---|---|---|---|---|---|\n"
)


class CrossRecordTests(unittest.TestCase):
    def write_record(self, path, prompt, values, context):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(TABLE + variant_row(prompt, values, context), encoding="utf-8")
        return path

    def run_cli(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = question_signatures.main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_a_single_record_also_counts_its_sibling_topic_records(self):
        with tempfile.TemporaryDirectory() as directory:
            topic = Path(directory) / "math-odes"
            self.write_record(topic / "2026-09-01-earlier.md", "Find the applied force.", "m=5 kg; a=2", "lift")
            later = self.write_record(topic / "2026-09-22-later.md", "What is the damping term?", "k=3", "spring")
            records = record_signatures(later)
            self.assertIn(prompt_signature("Find the applied force."), records["prompt"])
            self.assertIn(variant_signature("m=5 kg; a=2", "lift"), records["variant"])
            self.assertIn(prompt_signature("What is the damping term?"), records["prompt"])
            self.assertIn(variant_signature("k=3", "spring"), records["variant"])

    def test_reuse_is_checked_across_separate_record_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            first = self.write_record(base / "math-odes" / "a.md", "Find the applied force.", "m=5 kg; a=2", "lift")
            second = self.write_record(base / "statics" / "b.md", "Where is the centre of mass?", "L1=1 m; L2=2 m", "two rods")
            records = record_signatures([first, second])
            self.assertEqual(len(records["prompt"]), 2)
            self.assertEqual(len(records["variant"]), 2)
            self.assertTrue(prompt_reused("Where is the centre of mass?", records["prompt"]))
            self.assertTrue(prompt_reused("anything", records["variant"], "m=5 kg; a=2", "lift"))
            self.assertFalse(prompt_reused("Where is the resultant force?", records["prompt"]))

    def test_check_command_covers_every_named_record(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            self.write_record(base / "math-odes" / "a.md", "Find the applied force.", "m=5 kg; a=2", "lift")
            self.write_record(base / "statics" / "b.md", "Where is the centre of mass?", "L1=1 m; L2=2 m", "two rods")
            argv = [
                "check", "Where is the centre of mass?",
                "--values", "L1=1 m; L2=2 m",
                "--context", "two rods",
                "--record", str(base / "math-odes"), str(base / "statics"),
            ]
            code, out, _err = self.run_cli(argv)
            self.assertEqual(code, 1)
            self.assertIn("reused", out)
            argv[1] = "Where is the resultant force?"
            argv[3] = "L1=1 m; L2=9 m"
            code, out, _err = self.run_cli(argv)
            self.assertEqual(code, 0)
            self.assertIn("fresh", out)

    def test_missing_record_path_is_an_error_not_a_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            code, _out, err = self.run_cli(["check", "anything", "--record", str(Path(directory) / "absent")])
            self.assertEqual(code, 2)
            self.assertIn("does not exist", err)


if __name__ == "__main__":
    unittest.main()
