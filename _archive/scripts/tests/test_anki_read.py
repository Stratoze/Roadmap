"""Tests for the direct Anki collection reader.

The contract this file defends, chosen by the learner on 2026-09-29:
read-only, and FAIL LOUD on an unfamiliar schema. A wrong-but-plausible reading
of the learner's vocabulary is worse than an error, so the schema guard is the
most important thing here - these tests build deliberately-wrong collections and
prove the reader refuses them instead of guessing.

Collections are built in-process from the verified upstream Anki 26.9b3 DDL,
including its `COLLATE unicase` name columns, which is what forced the
Python-side name resolution.
"""
import os
import sqlite3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import anki_read  # noqa: E402

DDL = [
    """CREATE TABLE decks (
      id integer PRIMARY KEY NOT NULL,
      name text NOT NULL COLLATE unicase,
      mtime_secs integer NOT NULL, usn integer NOT NULL,
      common blob NOT NULL, kind blob NOT NULL)""",
    """CREATE TABLE notetypes (
      id integer NOT NULL PRIMARY KEY,
      name text NOT NULL COLLATE unicase,
      mtime_secs integer NOT NULL, usn integer NOT NULL, config blob NOT NULL)""",
    """CREATE TABLE notes (
      id integer PRIMARY KEY, guid text NOT NULL, mid integer NOT NULL,
      mod integer NOT NULL, usn integer NOT NULL, tags text NOT NULL,
      flds text NOT NULL, sfld integer NOT NULL, csum integer NOT NULL,
      flags integer NOT NULL, data text NOT NULL)""",
    """CREATE TABLE cards (
      id integer PRIMARY KEY, nid integer NOT NULL, did integer NOT NULL,
      ord integer NOT NULL, mod integer NOT NULL, usn integer NOT NULL,
      type integer NOT NULL, queue integer NOT NULL, due integer NOT NULL,
      ivl integer NOT NULL, factor integer NOT NULL, reps integer NOT NULL,
      lapses integer NOT NULL, left integer NOT NULL, odue integer NOT NULL,
      odid integer NOT NULL, flags integer NOT NULL, data text NOT NULL)""",
]

KAISHI_DECK = 1748323260993
LAPIS_DECK = 1786775303380
KAISHI_MODEL = 1708628080880


def _scratch_root():
    # Workspace-writable scratch, not tempfile: mkdtemp's 0700 dirs are refused
    # by the workspace-write sandbox (documented in scripts/README.md).
    root = os.path.join(ROOT, ".anki-read-cache", "tests")
    os.makedirs(root, exist_ok=True)
    return root


def make_tmpdir():
    """A unique, writable temp dir that works under the default sandbox."""
    import time
    path = os.path.join(
        _scratch_root(),
        f"t-{os.getpid()}-{time.time_ns()}")
    os.makedirs(path, exist_ok=True)
    return path


def build_connection(path):
    """sqlite3 connection that can CREATE Anki's `COLLATE unicase` columns.

    Anki registers its custom `unicase` collation at startup, so its DDL can
    be created there. Plain sqlite3 cannot, so the fixture registers a stand-in
    (case-insensitive, matching unicase's intent) *before* creating the schema.
    This stand-in is only used to build the fixture; the reader itself never
    relies on it, because the reader resolves unicase names in Python precisely
    so it does not need a custom collation.
    """
    conn = sqlite3.connect(path)
    conn.create_collation(
        "unicase", lambda a, b: (a.lower() > b.lower()) - (a.lower() < b.lower()))
    return conn


def build_collection(path, decks=("Kaishi 1.5k", "Lapis"), cards=(), notes=()):
    """Create a schema-accurate collection at `path`."""
    conn = build_connection(path)
    for statement in DDL:
        conn.execute(statement)
    for deck_id, name in ((KAISHI_DECK, "Kaishi 1.5k"), (LAPIS_DECK, "Lapis")):
        if name in decks:
            conn.execute(
                "insert into decks values (?,?,?,?,?,?)",
                (deck_id, name, 0, 0, b"", b""))
    conn.execute(
        "insert into notetypes values (?,?,?,?,?)",
        (KAISHI_MODEL, "Kaishi 1.5k", 0, 0, b""))
    for note_id, model, flds in notes:
        conn.execute(
            "insert into notes values (?,?,?,?,?,?,?,?,?,?,?)",
            (note_id, "g", model, 0, 0, " ", flds, 0, 0, 0, ""))
    for card_id, note_id, deck_id, queue, ivl, reps in cards:
        conn.execute(
            "insert into cards values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (card_id, note_id, deck_id, 0, 0, 0, 2, queue, 0,
             ivl, 2500, reps, 0, 0, 0, 0, 0, ""))
    conn.commit()
    conn.close()
    return str(path)


class SchemaGuardTests(unittest.TestCase):
    """The fail-loud contract."""

    def setUp(self):
        self.tmp = make_tmpdir()
        self.addCleanup(self._cleanup)

    def _cleanup(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_rejects_missing_table(self):
        path = os.path.join(self.tmp, "bad.anki2")
        conn = sqlite3.connect(path)
        conn.execute("create table cards (id integer primary key, nid integer,"
                     " did integer, ord integer, type integer, queue integer,"
                     " due integer, ivl integer, factor integer, reps integer,"
                     " lapses integer)")
        conn.execute("create table notes (id integer primary key, mid integer,"
                     " tags text, flds text)")
        conn.commit()
        conn.close()
        with self.assertRaises(anki_read.SchemaMismatch) as caught:
            anki_read.assert_schema(
                sqlite3.connect("file:" + path.replace("\\", "/") + "?mode=ro",
                                uri=True).cursor())
        self.assertIn("decks", str(caught.exception))

    def test_rejects_missing_column(self):
        path = os.path.join(self.tmp, "nocol.anki2")
        build_collection(path)
        conn = sqlite3.connect(path)
        conn.execute("alter table notetypes rename to notetypes_old")
        conn.execute("create table notetypes (id integer primary key)")
        conn.commit()
        conn.close()
        with self.assertRaises(anki_read.SchemaMismatch) as caught:
            anki_read.assert_schema(
                sqlite3.connect("file:" + path.replace("\\", "/") + "?mode=ro",
                                uri=True).cursor())
        self.assertIn("notetypes", str(caught.exception))

    def test_accepts_the_verified_layout(self):
        path = build_collection(os.path.join(self.tmp, "ok.anki2"))
        cursor = sqlite3.connect("file:" + path.replace("\\", "/") + "?mode=ro",
                                 uri=True).cursor()
        anki_read.assert_schema(cursor)  # must not raise


class MissingFileTests(unittest.TestCase):
    def test_missing_collection_raises(self):
        with self.assertRaises(anki_read.CollectionMissing):
            anki_read.snapshot_collection(os.path.join("nope", "absent.anki2"))


class UncaseCollationTests(unittest.TestCase):
    """`decks.name` and `notetypes.name` are COLLATE unicase.

    Any SQL comparison or ordering on them raises 'no such collation sequence'
    in a plain SQLite connection, so name lookups are resolved in Python. These
    tests pin that behaviour because a regression here fails at runtime only.
    """

    def setUp(self):
        self.tmp = make_tmpdir()
        self.addCleanup(self._cleanup)
        self.path = build_collection(os.path.join(self.tmp, "c.anki2"))
        self.conn = sqlite3.connect(
            "file:" + self.path.replace("\\", "/") + "?mode=ro", uri=True)
        self.addCleanup(self.conn.close)

    def _cleanup(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_naive_sql_comparison_would_fail(self):
        # Documents the constraint the Python-side lookup exists to satisfy.
        with self.assertRaises(sqlite3.OperationalError):
            self.conn.cursor().execute(
                "select id from decks where name = ?", ("Kaishi 1.5k",)).fetchone()

    def test_python_name_lookup_succeeds(self):
        cursor = self.conn.cursor()
        self.assertEqual(anki_read._name_to_id(cursor, "decks", "Kaishi 1.5k"),
                         KAISHI_DECK)

    def test_python_name_lookup_is_case_insensitive_fallback(self):
        cursor = self.conn.cursor()
        self.assertEqual(anki_read._name_to_id(cursor, "decks", "kaishi 1.5k"),
                         KAISHI_DECK)

    def test_unknown_name_returns_none(self):
        cursor = self.conn.cursor()
        self.assertIsNone(anki_read._name_to_id(cursor, "decks", "Nonexistent"))

    def test_deck_names_sorted_without_sql_order(self):
        names = anki_read.deck_names(self.conn.cursor())
        self.assertEqual(names, ["Kaishi 1.5k", "Lapis"])

    def test_name_to_id_guards_unexpected_tables(self):
        with self.assertRaises(anki_read.AnkiReadError):
            anki_read._name_to_id(self.conn.cursor(), "cards", "x")


class CountTests(unittest.TestCase):
    def setUp(self):
        self.tmp = make_tmpdir()
        self.addCleanup(self._cleanup)
        notes = [(1000 + i, KAISHI_MODEL, f"word{i}\x1f") for i in range(6)]
        cards = [
            (1, 1000, KAISHI_DECK, 2, 30, 12),   # mature, many reps
            (2, 1001, KAISHI_DECK, 2, 30, 12),
            (3, 1002, KAISHI_DECK, 2, 3, 15),    # stuck: many reps, tiny ivl
            (4, 1003, KAISHI_DECK, 2, 3, 15),
            (5, 1004, KAISHI_DECK, 0, 0, 0),     # new
            (6, 1005, KAISHI_DECK, 1, 0, 0),     # learning
        ]
        self.path = build_collection(
            os.path.join(self.tmp, "counts.anki2"), cards=cards, notes=notes)
        self.conn = sqlite3.connect(
            "file:" + self.path.replace("\\", "/") + "?mode=ro", uri=True)
        self.addCleanup(self.conn.close)

    def _cleanup(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_counts_classify_cards(self):
        counts = anki_read.deck_counts(self.conn.cursor())["Kaishi 1.5k"]
        self.assertEqual(counts["total"], 6)
        self.assertEqual(counts["unlearned"], 2)   # new + learning
        self.assertEqual(counts["mature"], 2)      # ivl >= 7
        self.assertEqual(counts["stuck"], 2)       # reps>=10, ivl<7

    def test_stuck_words_returns_the_stuck_set(self):
        words = anki_read.stuck_words(self.conn.cursor(), "Kaishi 1.5k", limit=10)
        found = {entry["word"] for entry in words}
        self.assertEqual(found, {"word2", "word3"})

    def test_stuck_words_respects_limit(self):
        words = anki_read.stuck_words(self.conn.cursor(), "Kaishi 1.5k", limit=1)
        self.assertEqual(len(words), 1)

    def test_stuck_words_unknown_deck_is_empty(self):
        self.assertEqual(
            anki_read.stuck_words(self.conn.cursor(), "Nonexistent", 5), [])

    def test_empty_lapis_deck_reports_zero(self):
        counts = anki_read.deck_counts(self.conn.cursor())["Lapis"]
        self.assertEqual(counts["total"], 0)


if __name__ == "__main__":
    unittest.main()
