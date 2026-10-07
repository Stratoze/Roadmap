#!/usr/bin/env python3
"""Read the Anki collection directly, with no GUI and with Anki closed.

Why this exists: AnkiConnect is an in-process HTTP server, so it only answers
while Anki is running (https://github.com/FooSoft/anki-connect/issues/411).
The tutor needs the known-set, due, and stuck counts to choose conversation
topics and to test against real vocabulary, and that must work when Anki is
closed. So this reads the collection file itself.

Method: snapshot-copy `collection.anki2` (+ `-wal`/`-shm`) to a temp directory
and open the copy read-only. Copying first is required because a WAL-mode
database opened read-only in place still fails with `database is locked` (SQLite
needs to create/read the `-shm` index). The real collection is never opened for
writing and never locked.

Safety contract, agreed 2026-09-29:
  * READ-ONLY. This script has no write path to Anki at all.
  * FAIL LOUD. If the schema does not match the verified upstream layout, raise
    `SchemaMismatch` rather than guess. A wrong-but-plausible reading is worse
    than an error.
  * NEVER CLAIM FRESHNESS. Reports collection mtime. Direct reads cannot see
    AnkiWeb sync; when the learner studies on another device, the collection is
    stale until Anki syncs, and the caller must escalate to AnkiConnect then.

Writes and sync remain on `scripts/anki_bridge.py` (AnkiConnect), approval-gated.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DEFAULT_COLLECTION = os.path.join(
    os.environ.get("APPDATA", ""), "Anki2", "Kohaku", "collection.anki2"
)

# The verified shape: upstream Anki 26.9b3 stores decks/notetypes/fields/templates
# in their own tables. A fork that reshapes these must be caught loudly, not
# silently misread.
REQUIRED_COLUMNS = {
    "cards": {"id", "nid", "did", "ord", "type", "queue", "due", "ivl",
              "factor", "reps", "lapses"},
    "notes": {"id", "mid", "tags", "flds"},
    "decks": {"id", "name"},
    # notetypes.name drives `_word_field`, so a fork that drops or reshapes it
    # would make stuck_words silently return nothing. It is required for that
    # reason, not because the query needs any other column.
    "notetypes": {"id", "name"},
}
REQUIRED_TABLES = set(REQUIRED_COLUMNS)

# Anki queue/type codes. queue: -1 suspended, 0 new, 1 learning, 2 review,
# 3 day-learn(relearning). Card type: 0 new, 1 learning, 2 review, 3 relearning.
STUCK_REPS_MIN = 10
STUCK_INTERVAL_MAX_DAYS = 7
UNLEARNED_QUEUES = (0, 1)          # new or in learning
DAY_LEARN_QUEUE = 3                # day-learn (relearning)
DEFAULT_WATCHED_DECKS = ("Kaishi 1.5k", "Lapis")


class AnkiReadError(RuntimeError):
    """Base for every failure this reader raises."""


class SchemaMismatch(AnkiReadError):
    """The collection does not match the verified schema. Refuse to guess."""


class CollectionMissing(AnkiReadError):
    """No readable collection file."""


# --- snapshot --------------------------------------------------------------

def _sibling(path: str, suffix: str) -> str | None:
    candidate = path + suffix
    return candidate if os.path.exists(candidate) else None


def snapshot_collection(collection_path: str) -> str:
    """Copy the collection (plus WAL sidecars) to a scratch dir; return its path.

    Copying is what makes a read-only open safe: the live database is never
    opened, so this can run while Anki is closed with zero lock contention.

    The scratch directory lives under the vault rather than the system temp
    dir. `tempfile.mkdtemp()` creates a 0700 directory that the workspace-write
    sandbox then refuses to write into (documented in `scripts/README.md`),
    whether it targets the system temp or a supplied parent; a plain unique
    directory with default permissions is writable. Set ANKI_READ_SCRATCH to
    override the location. It is gitignored and cleaned up after each read.
    """
    collection_path = os.path.abspath(os.path.expanduser(collection_path))
    if not os.path.exists(collection_path):
        raise CollectionMissing(f"no collection at {collection_path}")
    scratch_root = (
        os.environ.get("ANKI_READ_SCRATCH")
        or os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            ".anki-read-cache")
    )
    os.makedirs(scratch_root, exist_ok=True)
    # Deliberately NOT tempfile.mkdtemp: that creates the directory 0700, which
    # the workspace-write sandbox then refuses to write into (see
    # scripts/README.md). A plain unique dir keeps default permissions.
    temp_dir = os.path.join(
        scratch_root,
        f"snap-{os.getpid()}-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f')}")
    os.makedirs(temp_dir, exist_ok=True)
    target = os.path.join(temp_dir, "collection.anki2")
    shutil.copyfile(collection_path, target)
    for suffix in ("-wal", "-shm"):
        source = _sibling(collection_path, suffix)
        if source:
            try:
                shutil.copyfile(source, target + suffix)
            except OSError:
                # A WAL that cannot be copied is not fatal; the snapshot is
                # still consistent as of the last checkpoint.
                pass
    return target


def collection_mtime(collection_path: str) -> str | None:
    collection_path = os.path.abspath(os.path.expanduser(collection_path))
    if not os.path.exists(collection_path):
        return None
    stamp = os.path.getmtime(collection_path)
    return datetime.fromtimestamp(stamp, tz=timezone.utc).isoformat(timespec="seconds")


# --- schema guard ----------------------------------------------------------

def assert_schema(cursor: sqlite3.Cursor) -> None:
    """Refuse to read a schema we have not verified. Fail loud, never guess."""
    tables = {row[0] for row in cursor.execute(
        "select name from sqlite_master where type='table'")}
    missing_tables = REQUIRED_TABLES - tables
    if missing_tables:
        raise SchemaMismatch(
            "collection is missing required table(s): "
            f"{', '.join(sorted(missing_tables))}. "
            "This is likely a different Anki version or a reshaped fork; "
            "read via AnkiConnect instead."
        )
    problems = []
    for table, required in REQUIRED_COLUMNS.items():
        have = {row[1] for row in cursor.execute(f"pragma table_info({table})")}
        missing = required - have
        if missing:
            problems.append(f"{table}: {', '.join(sorted(missing))}")
    if problems:
        raise SchemaMismatch(
            "collection schema does not match the verified layout ("
            + "; ".join(problems) + "). Read via AnkiConnect instead."
        )


# --- open / query ----------------------------------------------------------

def open_readonly(collection_path: str):
    """Snapshot-copy and open read-only. Returns (conn, temp_dir, real_path).

    If the schema guard rejects the snapshot, the snapshot is removed before the
    error propagates, so a failed read never leaves a collection copy behind.
    """
    real_path = os.path.abspath(os.path.expanduser(collection_path))
    snapshot = snapshot_collection(real_path)
    temp_dir = os.path.dirname(snapshot)
    try:
        conn = sqlite3.connect(
            "file:" + snapshot.replace("\\", "/") + "?mode=ro", uri=True)
        assert_schema(conn.cursor())
    except BaseException:
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise
    return conn, temp_dir, real_path


def prune_snapshots() -> None:
    """Remove leftover snapshot dirs from an earlier crash or failed read."""
    scratch_root = (
        os.environ.get("ANKI_READ_SCRATCH")
        or os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            ".anki-read-cache")
    )
    if not os.path.isdir(scratch_root):
        return
    for name in os.listdir(scratch_root):
        if name.startswith("snap-"):
            shutil.rmtree(os.path.join(scratch_root, name), ignore_errors=True)


def _escape(deck: str) -> str:
    return str(deck).replace("\\", "\\\\").replace('"', '\\"')


# Anki-custom collation. `decks.name` and `notetypes.name` are declared
# COLLATE unicase, which a plain SQLite connection cannot resolve. Any SQL that
# compares or orders those two columns raises "no such collation sequence:
# unicase". So name lookups and sorting happen in Python, never in SQL.
UNICASED_COLUMNS = (("decks", "name"), ("notetypes", "name"))


def _name_to_id(cursor: sqlite3.Cursor, table: str, name: str) -> int | None:
    """Resolve a unicase name to its id in Python (exact, then casefold)."""
    if (table, "name") not in UNICASED_COLUMNS:
        raise AnkiReadError(f"unexpected collation assumption for {table}.name")
    target = str(name)
    rows = cursor.execute(f"select id, name from {table}").fetchall()
    for row_id, row_name in rows:
        if row_name == target:
            return row_id
    folded = target.casefold()
    for row_id, row_name in rows:
        if str(row_name).casefold() == folded:
            return row_id
    return None


def deck_names(cursor: sqlite3.Cursor) -> list:
    # Sorted in Python (unicase name column - see UNICASED_COLUMNS above).
    rows = [row[0] for row in cursor.execute("select name from decks")]
    return sorted(rows, key=lambda value: str(value).casefold())


def deck_counts(cursor: sqlite3.Cursor) -> dict:
    """Per-deck card totals and unlearned/stuck counts, computed locally.

    Safe to compute locally because unlike `cardsInfo.due` these are counts of
    queue membership, not day offsets - there is no AnkiWeb offset to
    misinterpret. `due` is deliberately NOT reported here; that stays with
    AnkiConnect, which owns day arithmetic.
    """
    counts = {}
    for deck_id, name in sorted(
            cursor.execute("select id, name from decks").fetchall(),
            key=lambda row: str(row[1]).casefold()):
        rows = list(cursor.execute(
            "select queue, type, reps, ivl from cards where did = ?", (deck_id,)))
        unlearned = sum(1 for q, _t, _r, _i in rows if q in UNLEARNED_QUEUES)
        relearning = sum(1 for q, _t, _r, _i in rows if q == DAY_LEARN_QUEUE)
        stuck = sum(1 for _q, _t, reps, ivl in rows
                    if reps >= STUCK_REPS_MIN and ivl < STUCK_INTERVAL_MAX_DAYS)
        mature = sum(1 for _q, _t, _r, ivl in rows if ivl >= STUCK_INTERVAL_MAX_DAYS)
        counts[name] = {
            "total": len(rows),
            "unlearned": unlearned,
            "relearning": relearning,
            "stuck": stuck,
            "mature": mature,
        }
    return counts


def _word_field(model_name: str) -> str | None:
    # Mirrors anki_bridge.WORD_FIELD_BY_MODEL. Kept local so this reader stays
    # importable without the bridge.
    return {"Kaishi 1.5k": "Word", "Lapis": "Expression"}.get(model_name)


def stuck_words(cursor: sqlite3.Cursor, deck: str, limit: int = 5) -> list:
    """Name up to `limit` stuck words in a deck.

    A card is stuck when it has been seen enough times that failing means
    something, but its interval has collapsed. The word is field 0 of the note
    for both watched decks; `_word_field` gates on the note type so a note from
    an unknown model is skipped rather than mislabelled.

    The join is done in Python, not SQL: some Anki columns carry a custom
    `unicase` collation that a plain SQLite connection cannot resolve, so any
    cross-table join that touches such a column raises "no such collation
    sequence". Fetching each table plainly (which works) and joining here
    sidesteps that without pretending to be Anki's collation.
    """
    if limit <= 0:
        return []
    deck_id = _name_to_id(cursor, "decks", deck)
    if deck_id is None:
        return []
    cards = cursor.execute(
        "select nid, reps, ivl from cards where did = ? "
        "and reps >= ? and ivl < ?",
        (deck_id, STUCK_REPS_MIN, STUCK_INTERVAL_MAX_DAYS)).fetchall()
    if not cards:
        return []
    model_by_note = dict(
        cursor.execute("select id, mid from notes").fetchall())
    model_name = dict(cursor.execute("select id, name from notetypes").fetchall())
    flds_by_note = dict(
        cursor.execute("select id, flds from notes where id in (%s)"
                       % ",".join("?" * len(cards)),
                       [nid for nid, _r, _i in cards]).fetchall())
    words = []
    seen = set()
    for nid, _reps, _ivl in cards:
        flds = flds_by_note.get(nid)
        if flds is None:
            continue
        model = model_name.get(model_by_note.get(nid))
        if not model or not _word_field(model):
            continue
        values = flds.split("\x1f")
        word = values[0].strip() if values else ""
        if word and word not in seen:
            seen.add(word)
            words.append({"word": word, "model": model})
            if len(words) >= limit:
                break
    return words


def daily_activity(cursor: sqlite3.Cursor) -> dict:
    """Per-day review counts and study minutes from revlog, plus streaks.

    `revlog.id` is the review timestamp in milliseconds and `revlog.time` is
    the milliseconds spent on that card, so both facts come from Anki's own
    review history rather than from the tutor timing anything. Read-only.

    Returns `{days: {YYYY-MM-DD: {reviews, minutes}}, streak: {...}}`. Days are
    local-time dates; Anki records UTC milliseconds, and the learner reads the
    grid in their own day, so the conversion happens here rather than being
    left to the caller.
    """
    days: dict = {}
    for row_id, spent in cursor.execute("select id, time from revlog"):
        stamp = datetime.fromtimestamp(row_id / 1000, tz=timezone.utc).astimezone()
        key = stamp.date().isoformat()
        entry = days.setdefault(key, {"reviews": 0, "ms": 0})
        entry["reviews"] += 1
        entry["ms"] += max(0, int(spent or 0))
    for entry in days.values():
        entry["minutes"] = round(entry["ms"] / 60000.0, 1)
    return {"days": days, "streak": streak_summary(days)}


def streak_summary(days: dict, today: str | None = None) -> dict:
    """Current and longest run of consecutive days with at least one review.

    `current` counts back from today; today itself not yet being studied does
    not break a streak that ran through yesterday, which is the usual and
    intended behaviour for a daily habit.
    """
    if not days:
        return {"current": 0, "longest": 0, "last_active": None}
    active = sorted(days)
    longest = run = 1
    for previous, current in zip(active, active[1:]):
        if _days_between(previous, current) == 1:
            run += 1
        else:
            run = 1
        longest = max(longest, run)
    if today is None:
        today = datetime.now().astimezone().date().isoformat()
    current = 0
    cursor_day = today
    if cursor_day not in days:
        # Allow the streak to still count if yesterday was active.
        cursor_day = _shift_day(today, -1)
    while cursor_day in days:
        current += 1
        cursor_day = _shift_day(cursor_day, -1)
    return {"current": current, "longest": longest, "last_active": active[-1]}


def _shift_day(iso_day: str, delta: int) -> str:
    from datetime import date, timedelta
    return (date.fromisoformat(iso_day) + timedelta(days=delta)).isoformat()


def _days_between(earlier: str, later: str) -> int:
    from datetime import date
    return (date.fromisoformat(later) - date.fromisoformat(earlier)).days


def summary(collection_path: str = DEFAULT_COLLECTION) -> dict:
    """Full read-only report: decks, counts, mtime, freshness caveat."""
    prune_snapshots()
    conn, temp_dir, real_path = open_readonly(collection_path)
    try:
        cursor = conn.cursor()
        payload = {
            "source": "direct-sqlite",
            "collection": real_path,
            "mtime": collection_mtime(real_path),
            "decks": deck_names(cursor),
            "counts": deck_counts(cursor),
            "freshness": "direct read cannot see AnkiWeb sync; escalate to "
                         "AnkiConnect when you need a synced collection",
            "stuck_samples": {},
            "activity": daily_activity(cursor),
        }
        for deck in DEFAULT_WATCHED_DECKS:
            if deck in payload["counts"]:
                payload["stuck_samples"][deck] = stuck_words(cursor, deck, limit=5)
        return payload
    finally:
        conn.close()
        shutil.rmtree(temp_dir, ignore_errors=True)


# --- CLI -------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(description="read the Anki collection directly")
    parser.add_argument("--collection", default=DEFAULT_COLLECTION)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("summary", help="deck names, counts, activity, mtime; read-only")
    sub.add_parser("decks", help="deck names only; read-only")
    activity = sub.add_parser(
        "activity", help="daily review counts, study minutes, and streaks; read-only")
    activity.add_argument("--days", type=int, default=91,
                          help="how many trailing days of daily detail to emit")
    return parser


def run(args):
    prune_snapshots()
    if args.command == "decks":
        conn, temp_dir, _ = open_readonly(args.collection)
        try:
            for name in deck_names(conn.cursor()):
                print(name)
        finally:
            conn.close()
            shutil.rmtree(temp_dir, ignore_errors=True)
        return 0
    if args.command == "summary":
        print(json.dumps(summary(args.collection), ensure_ascii=False, indent=2))
        return 0
    if args.command == "activity":
        conn, temp_dir, _ = open_readonly(args.collection)
        try:
            payload = daily_activity(conn.cursor())
        finally:
            conn.close()
            shutil.rmtree(temp_dir, ignore_errors=True)
        days = payload["days"]
        trailing = sorted(days)[-max(1, args.days):]
        total_minutes = sum(days[d]["minutes"] for d in trailing)
        total_reviews = sum(days[d]["reviews"] for d in trailing)
        print(f"days active (last {args.days}): {len(trailing)}")
        print(f"reviews: {total_reviews}   study time: {total_minutes / 60:.1f} h")
        print(f"streak: {payload['streak']['current']} current, "
              f"{payload['streak']['longest']} longest, "
              f"last active {payload['streak']['last_active']}")
        if trailing:
            busiest = max(trailing, key=lambda d: days[d]["minutes"])
            print(f"busiest day: {busiest} ({days[busiest]['minutes']} min, "
                  f"{days[busiest]['reviews']} reviews)")
        print()
        print("date        reviews  minutes")
        for day in trailing:
            print(f"{day}  {days[day]['reviews']:>6}  {days[day]['minutes']:>6.1f}")
        return 0
    raise AnkiReadError(f"unknown command {args.command!r}")


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    args = build_parser().parse_args(argv)
    try:
        return run(args)
    except AnkiReadError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
