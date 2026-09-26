"""Structural checks on the public Japanese source spine and its curriculum.

These are the invariants that keep the source map, the grammar table, the
handoff, and the reading gate from drifting apart silently. They read the vault;
they never write to it.
"""
import json
import os
import re
import sys
import unittest
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
CURRICULUM = ROOT / "_system" / "learning" / "curriculum"
JAPANESE = ROOT / "Japanese"
SOURCE_MAP = JAPANESE / "source-map.json"
SOURCES_DOC = JAPANESE / "SOURCES.md"
CURRENT = JAPANESE / "CURRENT.md"

JAPANESE_TOPICS = ["japanese-grammar", "japanese-output", "japanese-reading", "japanese-immersion"]
PRIVATE_REPO = "https://github.com/Stratoze/private-jp"
YOKUBI_HOST = "yoku.bi"
PRIVATE_SOURCE_PREFIX = "sources/yokubi/"

LIVE = os.environ.get("JAPANESE_SOURCE_LIVE_CHECK") == "1"
GATE_COUNT_RE = re.compile(r"(\d+)\s+actual(?:\s+novel)?[- ]reading sessions", re.IGNORECASE)
# The switch happens after the 30th session; "until session 30" reads as if the
# 30th session is already the transition and has no defined language order.
AMBIGUOUS_SWITCH_RE = re.compile(r"until\s+session\s+\d+", re.IGNORECASE)


def source_map():
    return json.loads(SOURCE_MAP.read_text(encoding="utf-8"))


def concept_rows(path):
    """Every 7-cell concept row in a curriculum file, as cell lists."""
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) == 7 and cells[0] not in ("id",) and not all(set(c) <= {"-"} for c in cells):
            rows.append(cells)
    return rows


def expected_url(lesson):
    relative = lesson["path"][len(PRIVATE_SOURCE_PREFIX):]
    return "https://" + YOKUBI_HOST + "/" + re.sub(r"\.md$", ".html", relative)


def head_status(url):
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "vault-source-check"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except OSError:
        return None


class SourceSchemaTests(unittest.TestCase):
    def test_all_curriculum_files_use_canonical_resources_heading(self):
        files = sorted(CURRICULUM.glob("*.md"))
        self.assertTrue(files)
        missing = [path.name for path in files if "## Resources" not in path.read_text(encoding="utf-8")]
        self.assertEqual(missing, [])

    def test_no_legacy_sources_heading(self):
        legacy = [path.name for path in CURRICULUM.glob("*.md") if "## Sources" in path.read_text(encoding="utf-8")]
        self.assertEqual(legacy, [])

    def test_source_map_and_yokubi_curriculum_are_aligned(self):
        lessons = source_map()["yokubi"]["lessons"]
        self.assertTrue(lessons)
        self.assertTrue(all(lesson["url"].endswith(".html") for lesson in lessons))
        grammar = (CURRICULUM / "japanese-grammar.md").read_text(encoding="utf-8")
        for lesson in lessons:
            self.assertIsNotNone(lesson["lesson"])
            self.assertIn(f"jp-yokubi-{lesson['lesson']:02d}", grammar)

    def test_grammar_table_has_exactly_one_row_per_lesson(self):
        data = source_map()
        lessons = data["yokubi"]["lessons"]
        rows = [r for r in concept_rows(CURRICULUM / "japanese-grammar.md")
                if re.fullmatch(r"jp-yokubi-\d{2}", r[0])]
        self.assertEqual(len(rows), len(lessons))
        self.assertEqual([r[0] for r in rows], [f"jp-yokubi-{l['lesson']:02d}" for l in lessons])

    def test_lesson_numbers_are_contiguous_and_unique(self):
        numbers = [lesson["lesson"] for lesson in source_map()["yokubi"]["lessons"]]
        self.assertEqual(sorted(numbers), list(range(len(numbers))))

    def test_lesson_ids_match_their_lesson_number(self):
        for lesson in source_map()["yokubi"]["lessons"]:
            self.assertEqual(lesson["id"], f"yokubi-lesson-{lesson['lesson']}")

    def test_every_locator_is_a_derived_yoku_bi_html_url(self):
        for lesson in source_map()["yokubi"]["lessons"]:
            self.assertTrue(lesson["path"].startswith(PRIVATE_SOURCE_PREFIX), lesson["path"])
            self.assertTrue(lesson["path"].endswith(".md"), lesson["path"])
            parts = urlsplit(lesson["url"])
            self.assertEqual(parts.scheme, "https", lesson["url"])
            self.assertEqual(parts.netloc, YOKUBI_HOST, lesson["url"])
            self.assertEqual(lesson["url"], expected_url(lesson), lesson["url"])

    def test_no_duplicate_yoku_bi_urls(self):
        urls = [lesson["url"] for lesson in source_map()["yokubi"]["lessons"]]
        self.assertEqual(len(set(urls)), len(urls))

    @unittest.skipUnless(LIVE, "set JAPANESE_SOURCE_LIVE_CHECK=1 to hit yoku.bi")
    def test_locator_urls_are_live(self):
        urls = [lesson["url"] for lesson in source_map()["yokubi"]["lessons"]]
        with ThreadPoolExecutor(max_workers=8) as pool:
            statuses = list(pool.map(head_status, urls))
        broken = [url for url, status in zip(urls, statuses) if status != 200]
        self.assertEqual(broken, [])

    def test_pinned_commit_and_digest_are_recorded(self):
        data = source_map()
        self.assertRegex(data["yokubi"]["commit"], r"^[0-9a-f]{40}$")
        self.assertRegex(data["imabi"]["sha256"], r"^[0-9a-f]{64}$")

    def test_imabi_mirror_is_not_claimed_as_verified(self):
        """The IMABI mirror must never read as a verified or licensed source."""
        imabi = source_map()["imabi"]
        claims = " ".join(str(imabi.get(key, "")) for key in ("license", "provenance", "role")).lower()
        self.assertIn("live source", claims)
        for forbidden in ("verified mirror", "cc-by", "public domain"):
            self.assertNotIn(forbidden, claims)

    def test_sources_doc_agrees_with_the_map(self):
        doc = SOURCES_DOC.read_text(encoding="utf-8")
        self.assertIn(PRIVATE_REPO, doc)
        self.assertIn(source_map()["private_source_repository"], doc)
        self.assertIn("verified", doc)
        # IMABI is a derived index over an unverified mirror; the doc must say so.
        self.assertIn("unverified", doc.lower())


class JapaneseCurriculumGraphTests(unittest.TestCase):
    def test_no_dangling_prerequisite_ids(self):
        known = set()
        for topic in JAPANESE_TOPICS:
            known.update(row[0] for row in concept_rows(CURRICULUM / f"{topic}.md"))
        self.assertTrue(known)
        dangling = []
        for topic in JAPANESE_TOPICS:
            for row in concept_rows(CURRICULUM / f"{topic}.md"):
                if row[2] in ("", "-"):
                    continue
                for prereq in [p.strip() for p in re.split(r"[,\s]+", row[2]) if p.strip()]:
                    if prereq not in known:
                        dangling.append(f"{topic}:{row[0]} -> {prereq}")
        self.assertEqual(dangling, [])

    def test_prerequisites_point_backwards(self):
        """A concept may not require something sequenced after it."""
        for topic in JAPANESE_TOPICS:
            for row in concept_rows(CURRICULUM / f"{topic}.md"):
                for prereq in [p.strip() for p in re.split(r"[,\s]+", row[2]) if p.strip()]:
                    if re.fullmatch(r"jp-yokubi-(\d{2})", prereq) and re.fullmatch(r"jp-yokubi-(\d{2})", row[0]):
                        self.assertLess(int(prereq[-2:]), int(row[0][-2:]), f"{row[0]} -> {prereq}")

    def test_grammar_source_locator_matches_the_concept_id(self):
        if str(ROOT / "scripts") not in sys.path:
            sys.path.insert(0, str(ROOT / "scripts"))
        import build_japanese_curriculum as builder
        text = (CURRICULUM / "japanese-grammar.md").read_text(encoding="utf-8")
        self.assertEqual(builder.locator_mismatches(text), [])


class ReadingGateWordingTests(unittest.TestCase):
    def files(self):
        return [JAPANESE / "Index.md", CURRENT, SOURCES_DOC] + [
            CURRICULUM / f"{topic}.md" for topic in JAPANESE_TOPICS
        ]

    def test_gate_is_stated_as_thirty_sessions_wherever_it_is_stated(self):
        for path in self.files():
            for number in GATE_COUNT_RE.findall(path.read_text(encoding="utf-8")):
                self.assertEqual(number, "30", f"{path.name} states a {number}-session gate")

    def test_the_language_order_switch_is_unambiguous(self):
        for path in self.files():
            text = path.read_text(encoding="utf-8")
            found = AMBIGUOUS_SWITCH_RE.findall(text)
            self.assertEqual(found, [], f"{path.name} uses an ambiguous switch: {found}")

    def test_current_handoff_names_the_gate_command(self):
        self.assertIn("review.py usage japanese-reading", CURRENT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
