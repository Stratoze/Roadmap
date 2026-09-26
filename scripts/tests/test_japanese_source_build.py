"""Source-side tests for the Japanese spine.

The curriculum checker must verify the public grammar table without ever
writing to it, and the source-map builder must verify provenance before it
writes anything.
"""
import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import build_japanese_curriculum as builder  # noqa: E402
import build_japanese_source_map as sourcer  # noqa: E402

GRAMMAR = ROOT / "_system" / "learning" / "curriculum" / "japanese-grammar.md"
COMMITTED_MAP = ROOT / "Japanese" / "source-map.json"

SUMMARY = """\
# Summary

* [Introduction](README.md)

* [Lesson 0: The anatomy of Japanese sentences](Section1/Part1/Lesson0.md)
* [Lesson 1: State of being with だ and です](Section1/Part1/Lesson1.md)
* [Lesson 2: Nouns, pronouns](Section1/Part2/Lesson2.md)
"""

IMABI = """\
<html><body>
<h2><a id="beginnersi"></a>Beginners I</h2>
<h3><a id="vowels"></a>The Vowels of Japanese</h3>
<div id="grammarindex"></div>
</body></html>
"""


def git(root, *args):
    return subprocess.run(
        ["git", "-C", str(root), "-c", "user.email=source@example.invalid",
         "-c", "user.name=Source Fixture", "-c", "commit.gpgsign=false", *args],
        text=True, encoding="utf-8", errors="replace", capture_output=True, check=True,
    ).stdout


class SourceFixture:
    """A throwaway private repository with a Yokubi checkout inside it."""

    def __init__(self, root, private_repo, yokubi_repo, summary=SUMMARY, imabi=IMABI):
        self.root = root
        self.private_repo = private_repo
        self.yokubi_repo = yokubi_repo
        self.private = root / "private-jp"
        self.yokubi = self.private / "sources" / "yokubi"
        self.yokubi.mkdir(parents=True, exist_ok=True)
        (self.yokubi / "src").mkdir()
        (self.yokubi / "src" / "SUMMARY.md").write_text(summary, encoding="utf-8", newline="\n")
        for lesson in range(3):
            path = self.yokubi / f"Section1/Part1/Lesson{lesson}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"# Lesson {lesson}\n", encoding="utf-8", newline="\n")
        (self.yokubi / "Section1/Part2").mkdir(parents=True, exist_ok=True)
        (self.yokubi / "Section1" / "Part2" / "Lesson2.md").write_text("# L2\n", encoding="utf-8", newline="\n")
        git(self.yokubi, "init", "-q")
        git(self.yokubi, "remote", "add", "origin", yokubi_repo)
        git(self.yokubi, "add", "-A")
        git(self.yokubi, "commit", "-qm", "yokubi fixture")

        self.imabi = self.private / "sources" / "今日 IMABI.html"
        self.imabi.parent.mkdir(parents=True, exist_ok=True)
        self.imabi.write_text(imabi, encoding="utf-8", newline="\n")
        git(self.private, "init", "-q")
        git(self.private, "remote", "add", "origin", private_repo)
        git(self.private, "add", "-A")
        git(self.private, "commit", "-qm", "private fixture")

    def argv(self, output, *extra):
        return [
            "--private-root", str(self.private),
            "--private-repo", self.private_repo,
            "--yokubi-root", str(self.yokubi),
            "--yokubi-repo", self.yokubi_repo,
            "--imabi-file", str(self.imabi),
            "--output", str(output),
            *extra,
        ]


PRIVATE_REPO = "https://github.com/Stratoze/private-jp"
YOKUBI_REPO = "https://github.com/Morgawr/yokubi"


class CurriculumAlignmentTests(unittest.TestCase):
    def setUp(self):
        self.original = GRAMMAR.read_text(encoding="utf-8")

    def write_grammar(self, text, target):
        target.write_text(text, encoding="utf-8", newline="\n")
        return target

    def run_builder(self, map_path, target):
        with patch.object(builder, "MAP", map_path), patch.object(builder, "TARGET", target):
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(io.StringIO()):
                code = builder.main([])
            return code, buffer.getvalue()

    def temp_pair(self, directory):
        root = Path(directory)
        map_path = root / "source-map.json"
        map_path.write_text(COMMITTED_MAP.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
        return map_path, root / "japanese-grammar.md"

    def test_current_grammar_table_matches_source_map(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(builder.main([]), 0)

    def test_changed_table_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            map_path, target_path = self.temp_pair(directory)
            changed = self.original.replace("| jp-yokubi-00 |", "| jp-yokubi-00-changed |", 1)
            self.write_grammar(changed, target_path)
            code, _ = self.run_builder(map_path, target_path)
            self.assertEqual(code, 2)
            self.assertIn("jp-yokubi-00-changed", target_path.read_text(encoding="utf-8"))

    def test_whole_table_is_untouched_by_the_checker(self):
        with tempfile.TemporaryDirectory() as directory:
            map_path, target_path = self.temp_pair(directory)
            self.write_grammar(self.original, target_path)
            before = target_path.read_bytes()
            self.run_builder(map_path, target_path)
            self.run_builder(map_path, target_path)
            self.assertEqual(target_path.read_bytes(), before)

    def test_wrong_source_locator_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            map_path, target_path = self.temp_pair(directory)
            # Aim and prereqs still match the source map; only the evidence locator moves.
            changed = self.original.replace(
                "| jp-yokubi-07 | Negated verbs | jp-yokubi-06 | unknown | 0 | - | source map: yokubi-lesson-7 |",
                "| jp-yokubi-07 | Negated verbs | jp-yokubi-06 | unknown | 0 | - | source map: yokubi-lesson-8 |",
            )
            self.assertNotEqual(changed, self.original)
            self.write_grammar(changed, target_path)
            stderr = io.StringIO()
            with patch.object(builder, "MAP", map_path), patch.object(builder, "TARGET", target_path):
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(stderr):
                    code = builder.main([])
            self.assertEqual(code, 2)
            self.assertIn("yokubi-lesson-8", stderr.getvalue())

    def test_learner_evidence_replacing_the_locator_is_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            map_path, target_path = self.temp_pair(directory)
            changed = self.original.replace(
                "| jp-yokubi-07 | Negated verbs | jp-yokubi-06 | unknown | 0 | - | source map: yokubi-lesson-7 |",
                "| jp-yokubi-07 | Negated verbs | jp-yokubi-06 | seen | 1 | 2026-09-27 | session 2026-09-26 |",
            )
            self.assertNotEqual(changed, self.original)
            self.write_grammar(changed, target_path)
            code, _ = self.run_builder(map_path, target_path)
            self.assertEqual(code, 0)

    def test_duplicate_concept_id_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            map_path, target_path = self.temp_pair(directory)
            row = "| jp-yokubi-07 | Negated verbs | jp-yokubi-06 | unknown | 0 | - | source map: yokubi-lesson-7 |"
            self.write_grammar(self.original.replace(row, row + "\n" + row, 1), target_path)
            with patch.object(builder, "MAP", map_path), patch.object(builder, "TARGET", target_path):
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(builder.main([]), 2)

    def test_missing_concepts_heading_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            map_path, target_path = self.temp_pair(directory)
            broken = self.original.replace("## Concepts", "## Notes", 1)
            self.write_grammar(broken, target_path)
            with patch.object(builder, "MAP", map_path), patch.object(builder, "TARGET", target_path):
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(builder.main([]), 2)

    def test_diff_output_is_one_row_per_line(self):
        with tempfile.TemporaryDirectory() as directory:
            map_path, target_path = self.temp_pair(directory)
            self.write_grammar(self.original.replace("| jp-yokubi-00 |", "| jp-yokubi-00-x |", 1), target_path)
            _, out = self.run_builder(map_path, target_path)
            rows = [line for line in out.splitlines() if line.startswith(("+", "-", " "))]
            self.assertGreaterEqual(len(rows), 4)
            self.assertTrue(any(line.startswith("-jp-yokubi-00-x") for line in rows))

    def test_committed_map_lesson_numbers_are_contiguous_and_unique(self):
        lessons = json.loads(COMMITTED_MAP.read_text(encoding="utf-8"))["yokubi"]["lessons"]
        numbers = [lesson["lesson"] for lesson in lessons]
        self.assertEqual(sorted(numbers), list(range(len(numbers))))
        self.assertEqual(len(set(numbers)), len(numbers))


class SourceMapBuildTests(unittest.TestCase):
    def build(self, directory, summary=SUMMARY, imabi=IMABI, *extra):
        root = Path(directory)
        fixture = SourceFixture(root, PRIVATE_REPO, YOKUBI_REPO, summary=summary, imabi=imabi)
        output = root / "source-map.json"
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(io.StringIO()):
            code = sourcer.main(fixture.argv(output, *extra))
        return code, output, buffer.getvalue(), fixture

    def test_verified_build_records_derived_locators(self):
        with tempfile.TemporaryDirectory() as directory:
            code, output, _, _ = self.build(directory)
            self.assertEqual(code, 0)
            data = json.loads(output.read_text(encoding="utf-8"))
            self.assertTrue(data["private_root_verified"])
            self.assertTrue(all(data["verification"].values()), data["verification"])
            lessons = data["yokubi"]["lessons"]
            self.assertEqual([l["lesson"] for l in lessons], [0, 1, 2])
            self.assertEqual(lessons[0]["id"], "yokubi-lesson-0")
            self.assertEqual(lessons[0]["path"], "sources/yokubi/Section1/Part1/Lesson0.md")
            self.assertEqual(lessons[0]["url"], "https://yoku.bi/Section1/Part1/Lesson0.html")
            self.assertEqual(lessons[2]["url"], "https://yoku.bi/Section1/Part2/Lesson2.html")
            self.assertEqual(data["imabi"]["local_file"], "sources/今日 IMABI.html")
            self.assertEqual(len(data["imabi"]["sha256"]), 64)
            self.assertEqual([a["id"] for a in data["imabi"]["anchors"]],
                             ["beginnersi", "vowels", "grammarindex"])
            self.assertEqual(data["imabi"]["anchors"][0]["label"], "Beginners I")

    def test_rejects_yokubi_remote_mismatch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = SourceFixture(root, PRIVATE_REPO, "https://example.invalid/other-yokubi")
            output = root / "source-map.json"
            argv = fixture.argv(output)
            # the checkout points somewhere else, but the run declares the real repository
            argv[argv.index("--yokubi-repo") + 1] = YOKUBI_REPO
            stderr = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(stderr):
                code = sourcer.main(argv)
            self.assertEqual(code, 2)
            self.assertIn("yokubi repository mismatch", stderr.getvalue())
            self.assertFalse(output.exists())

    def test_rejects_private_remote_mismatch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = SourceFixture(root, "https://example.invalid/other-private", YOKUBI_REPO)
            output = root / "source-map.json"
            argv = fixture.argv(output)
            argv[argv.index("--private-repo") + 1] = PRIVATE_REPO
            stderr = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(stderr):
                code = sourcer.main(argv)
            self.assertEqual(code, 2)
            self.assertIn("private repository mismatch", stderr.getvalue())
            self.assertFalse(output.exists())

    def test_rejects_source_outside_the_private_root(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = SourceFixture(root, PRIVATE_REPO, YOKUBI_REPO)
            outside = root / "stray-yokubi"
            outside.mkdir()
            (outside / "src").mkdir()
            (outside / "src" / "SUMMARY.md").write_text(SUMMARY, encoding="utf-8", newline="\n")
            git(outside, "init", "-q")
            git(outside, "remote", "add", "origin", YOKUBI_REPO)
            git(outside, "add", "-A")
            git(outside, "commit", "-qm", "stray")
            argv = fixture.argv(root / "source-map.json")
            argv[argv.index("--yokubi-root") + 1] = str(outside)
            stderr = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(stderr):
                code = sourcer.main(argv)
            self.assertEqual(code, 2)
            self.assertIn("outside the declared private root", stderr.getvalue())

    def test_unverified_build_needs_an_explicit_override(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = SourceFixture(root, PRIVATE_REPO, YOKUBI_REPO)
            output = root / "source-map.json"
            argv = [
                "--yokubi-root", str(fixture.yokubi),
                "--yokubi-repo", YOKUBI_REPO,
                "--imabi-file", str(fixture.imabi),
                "--output", str(output),
            ]
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(sourcer.main(argv), 2)
            self.assertFalse(output.exists())

    def test_verified_map_is_not_downgraded_to_an_unverified_one(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "source-map.json"
            _, _, _, fixture = self.build(directory)
            self.assertTrue(json.loads(output.read_text(encoding="utf-8"))["private_root_verified"])
            argv = [
                "--yokubi-root", str(fixture.yokubi),
                "--yokubi-repo", YOKUBI_REPO,
                "--imabi-file", str(fixture.imabi),
                "--output", str(output),
            ]
            stderr = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(stderr):
                self.assertEqual(sourcer.main(argv), 2)
            self.assertIn("refusing to overwrite", stderr.getvalue())
            self.assertTrue(json.loads(output.read_text(encoding="utf-8"))["private_root_verified"])

    def test_duplicate_lesson_numbers_abort_the_build(self):
        summary = SUMMARY + "* [Lesson 1: Duplicate again](Section1/Part1/Lesson1b.md)\n"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = SourceFixture(root, PRIVATE_REPO, YOKUBI_REPO, summary=summary)
            output = root / "source-map.json"
            stderr = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(stderr):
                code = sourcer.main(fixture.argv(output))
            self.assertEqual(code, 2)
            self.assertIn("duplicate lesson number", stderr.getvalue())
            self.assertFalse(output.exists())

    def test_non_numeric_lesson_title_aborts_the_build(self):
        summary = SUMMARY + "* [Lesson Appendix: Extra](Section1/Part1/Appendix.md)\n"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = SourceFixture(root, PRIVATE_REPO, YOKUBI_REPO, summary=summary)
            output = root / "source-map.json"
            stderr = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(stderr):
                code = sourcer.main(fixture.argv(output))
            self.assertEqual(code, 2)
            self.assertIn("no numeric id", stderr.getvalue())
            self.assertFalse(output.exists())

    def test_missing_imabi_mirror_aborts_the_build(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = SourceFixture(root, PRIVATE_REPO, YOKUBI_REPO)
            fixture.imabi.unlink()
            output = root / "source-map.json"
            stderr = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(stderr):
                code = sourcer.main(fixture.argv(output))
            self.assertEqual(code, 2)
            self.assertIn("IMABI mirror not found", stderr.getvalue())
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
