import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CURRICULUM = ROOT / "_system" / "learning" / "curriculum"


class SourceSchemaTests(unittest.TestCase):
    def test_all_curriculum_files_use_canonical_resources_heading(self):
        files = sorted(CURRICULUM.glob("*.md"))
        self.assertTrue(files)
        missing = [path.name for path in files if "## Resources" not in path.read_text(encoding="utf-8")]
        self.assertEqual(missing, [])

    def test_no_legacy_sources_heading(self):
        legacy = [path.name for path in CURRICULUM.glob("*.md") if "## Sources" in path.read_text(encoding="utf-8")]
        self.assertEqual(legacy, [])


if __name__ == "__main__":
    unittest.main()
