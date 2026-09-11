#!/usr/bin/env python3
"""review.py - transparent spaced-review scheduler for the vault learning system.

Commands:
  due                          list concepts due today
  schedule <topic> <id> [rung] set next_review = today + ladder[rung]
                               (rung defaults to the current rung, else 0)
  next <topic> <id> hit|hard|miss
                               apply a review outcome
  selftest                     in-memory fixture checks

Ladder: 1, 3, 7, 16, 35, 90 days (rung 0..5).
Rules: hit -> rung+1 (cap 5) and state solid at rung >= 4; hard -> same rung;
miss -> rung-1 (floor 0); a miss demotes solid -> review. Rows are created only
by the study skill - this script never upserts.

Exit codes: 0 ok, 1 selftest failure, 2 bad input / unknown row.
"""
import datetime as dt
import re
import sys
from pathlib import Path

LADDER = [1, 3, 7, 16, 35, 90]
ROOT = Path(__file__).resolve().parent.parent
CURRICULUM = ROOT / "_system" / "learning" / "curriculum"
CELLS = 7
SEP_RE = re.compile(r"^:?-+:?$")


def read_rows(text):
    """Yield (line_index, cells) for concept rows inside a `## Concepts` section."""
    lines = text.split("\n")
    in_concepts = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("## "):
            in_concepts = stripped == "## Concepts"
            continue
        if not in_concepts or not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) != CELLS:
            print(f"warning: malformed row at {CURRICULUM.name}:{i + 1}", file=sys.stderr)
            continue
        if cells[0] == "id" or all(SEP_RE.fullmatch(c) for c in cells):
            continue
        yield i, cells


def load(topic):
    path = CURRICULUM / f"{topic}.md"
    if not path.is_file():
        print(f"error: no curriculum file for topic '{topic}'", file=sys.stderr)
        return None
    return path


def find_row(path, concept_id):
    text = path.read_text(encoding="utf-8")
    hits = [r for r in read_rows(text) if r[1][0] == concept_id]
    if len(hits) != 1:
        print(f"error: id '{concept_id}' found {len(hits)} times in {path.name}", file=sys.stderr)
        return None
    return text, hits[0][0], hits[0][1]


def write_row(path, text, line_no, cells):
    lines = text.split("\n")
    lines[line_no] = "| " + " | ".join(cells) + " |"
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def format_row(topic, cells):
    return f"{topic} | {cells[0]} | {cells[3]} | {cells[4]} | {cells[5]}"


def apply_outcome(state, rung, outcome):
    if outcome == "hit":
        rung = min(rung + 1, len(LADDER) - 1)
        if rung >= 4:
            state = "solid"
    elif outcome == "miss":
        if state == "solid":
            state = "review"
        rung = max(rung - 1, 0)
    return state, rung


def cmd_due():
    today = dt.date.today()
    rows = []
    for path in sorted(CURRICULUM.glob("*.md")):
        for _, cells in read_rows(path.read_text(encoding="utf-8")):
            try:
                when = dt.date.fromisoformat(cells[5])
            except ValueError:
                continue
            if when <= today:
                rows.append(format_row(path.stem, cells))
    for row in sorted(rows):
        print(row)
    return 0


def cmd_schedule(topic, concept_id, rung_arg):
    path = load(topic)
    if path is None:
        return 2
    found = find_row(path, concept_id)
    if found is None:
        return 2
    text, line_no, cells = found
    try:
        current = int(cells[4])
    except ValueError:
        current = 0
    rung = int(rung_arg) if rung_arg is not None else current
    if not 0 <= rung < len(LADDER):
        print(f"error: rung must be 0..{len(LADDER) - 1}", file=sys.stderr)
        return 2
    if cells[3] in ("unknown", "seen"):
        cells[3] = "review"
    cells[4] = str(rung)
    cells[5] = (dt.date.today() + dt.timedelta(days=LADDER[rung])).isoformat()
    write_row(path, text, line_no, cells)
    print(format_row(topic, cells))
    return 0


def cmd_next(topic, concept_id, outcome):
    path = load(topic)
    if path is None:
        return 2
    found = find_row(path, concept_id)
    if found is None:
        return 2
    text, line_no, cells = found
    try:
        rung = int(cells[4])
    except ValueError:
        rung = 0
    state, rung = apply_outcome(cells[3], rung, outcome)
    cells[3] = state
    cells[4] = str(rung)
    cells[5] = (dt.date.today() + dt.timedelta(days=LADDER[rung])).isoformat()
    write_row(path, text, line_no, cells)
    print(format_row(topic, cells))
    return 0


def cmd_selftest():
    fixture = (
        "# t\n\n## Concepts\n"
        "| id | aim | prereqs | state | rung | next_review | evidence |\n"
        "|----|-----|---------|-------|------|-------------|----------|\n"
        "| c1 | aim one | - | review | 2 | 2026-09-12 | - |\n"
        "| c2 | aim two | c1 | unknown | 0 | - | - |\n"
    )
    rows = list(read_rows(fixture))
    assert [c[0] for _, c in rows] == ["c1", "c2"], rows

    state, rung = apply_outcome("review", 2, "hit")
    assert (state, rung) == ("review", 3), (state, rung)
    state, rung = apply_outcome("review", 3, "hit")
    assert (state, rung) == ("solid", 4), (state, rung)
    state, rung = apply_outcome("solid", 4, "miss")
    assert (state, rung) == ("review", 3), (state, rung)
    state, rung = apply_outcome("review", 0, "miss")
    assert (state, rung) == ("review", 0), (state, rung)
    state, rung = apply_outcome("review", 3, "hard")
    assert (state, rung) == ("review", 3), (state, rung)
    state, rung = apply_outcome("unknown", 0, "miss")
    assert (state, rung) == ("unknown", 0), (state, rung)

    cells = rows[0][1]
    cells[4] = "3"
    lines = fixture.split("\n")
    lines[rows[0][0]] = "| " + " | ".join(cells) + " |"
    assert "| c1 | aim one | - | review | 3 | 2026-09-12 | - |" in lines

    print("selftest ok")
    return 0


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if not argv:
        print(__doc__.strip())
        return 2
    cmd, rest = argv[0], argv[1:]
    if cmd == "due" and not rest:
        return cmd_due()
    if cmd == "schedule" and 2 <= len(rest) <= 3:
        return cmd_schedule(rest[0], rest[1], rest[2] if len(rest) == 3 else None)
    if cmd == "next" and len(rest) == 3 and rest[2] in ("hit", "hard", "miss"):
        return cmd_next(rest[0], rest[1], rest[2])
    if cmd == "selftest" and not rest:
        return cmd_selftest()
    print("usage: review.py due | schedule <topic> <id> [rung] | next <topic> <id> hit|hard|miss | selftest", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
