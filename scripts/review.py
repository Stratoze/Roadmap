#!/usr/bin/env python3
"""review.py - transparent spaced-review and usage scheduler for the vault.

Commands:
  due                          list concepts due today
  schedule <topic> <id> [rung] set next_review = today + ladder[rung]
  next <topic> <id> hit|hard|miss
  usage <topic>                list derived usage freshness for a topic
  usage <topic> <id> <event> <evidence-path> [public-note]
                               append an idempotent usage event
  selftest                     in-memory fixture checks

Ladder: 1, 3, 7, 16, 35, 90 days (rung 0..5).
Usage events are append-only and never change review state or rung. `reading_session` counts an actual novel-reading session; sentence-analysis fallback uses `practised` on its separate concept and does not increment the reading gate. A `reading_session` event is only valid on the single gate pair `japanese-reading` / `read-30-session-gate`; any other topic/id fails closed instead of being silently dropped.
"""
import datetime as dt
import hashlib
import re
import sys
from pathlib import Path

LADDER = [1, 3, 7, 16, 35, 90]
ROOT = Path(__file__).resolve().parent.parent
CURRICULUM = ROOT / "_system" / "learning" / "curriculum"
CONCEPT_CELLS = 7
USAGE_CELLS = 6
USAGE_EVENTS = {"introduced", "practised", "produced", "mined", "reading_session"}
READING_GATE_TOPIC = "japanese-reading"
READING_GATE_ID = "read-30-session-gate"
READING_GATE = (READING_GATE_TOPIC, READING_GATE_ID)
BASELINE_USAGE_IDS = {READING_GATE_TOPIC: [READING_GATE_ID]}
SEP_RE = re.compile(r"^:?-+:?$")


def write_text(path, text):
    path.write_text(text, encoding="utf-8", newline="\n")


def read_rows(text):
    """Yield (line_index, cells) for concept rows inside `## Concepts`."""
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
        if len(cells) != CONCEPT_CELLS:
            print(f"warning: malformed concept row at line {i + 1}", file=sys.stderr)
            continue
        if cells[0] == "id" or all(SEP_RE.fullmatch(c) for c in cells):
            continue
        yield i, cells


def usage_section_bounds(lines):
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "## Usage events":
            start = i
            break
    if start is None:
        return None, None
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].strip().startswith("## "):
            end = i
            break
    return start, end


def read_usage_rows(text):
    """Yield usage event rows and collect malformed rows separately."""
    lines = text.split("\n")
    start, end = usage_section_bounds(lines)
    if start is None:
        return
    for i in range(start + 1, end):
        stripped = lines[i].strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) != USAGE_CELLS:
            yield i, cells, "malformed"
            continue
        if cells[0] == "date" or all(SEP_RE.fullmatch(c) for c in cells):
            continue
        if cells[3] not in USAGE_EVENTS:
            yield i, cells, "event"
            continue
        yield i, cells, None


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
    write_text(path, "\n".join(lines))


def format_row(topic, cells):
    return f"{topic} | {cells[0]} | {cells[3]} | {cells[4]} | {cells[5]}"


def apply_outcome(state, rung, outcome):
    if state in {"unknown", "seen"} and outcome in {"hit", "hard"}:
        state = "review"
    if outcome == "hit":
        rung = min(rung + 1, len(LADDER) - 1)
        if rung >= 4:
            state = "solid"
    elif outcome == "hard":
        if state == "solid":
            state = "review"
    elif outcome == "miss":
        if state == "solid":
            state = "review"
        rung = max(rung - 1, 0)
    return state, rung


def usage_event_id(topic, concept_id, event, evidence, date, public_note=""):
    raw = "|".join((date, topic, concept_id, event, evidence, public_note))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]


def evidence_path(value):
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    return path


MAX_PUBLIC_NOTE = 240


def valid_public_note(note):
    return not note or (len(note) <= MAX_PUBLIC_NOTE and "\n" not in note and "|" not in note)


def usage_insert_at(lines, start, end):
    """Insert after the last usage-table row, before any prose in the section."""
    last_table_line = start + 2
    for i in range(start + 1, end):
        stripped = lines[i].strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            last_table_line = i
        elif last_table_line >= start + 2:
            break
    return last_table_line + 1


def append_usage(path, topic, concept_id, event, evidence, public_note):
    if event not in USAGE_EVENTS:
        print(f"error: usage event must be one of {sorted(USAGE_EVENTS)}", file=sys.stderr)
        return 2
    if not concept_id or "|" in concept_id or "\n" in concept_id:
        print("error: usage id must be a non-empty table-safe value", file=sys.stderr)
        return 2
    if event == "reading_session" and (topic, concept_id) != READING_GATE:
        print(
            f"error: reading_session must use {READING_GATE_TOPIC} / {READING_GATE_ID}",
            file=sys.stderr,
        )
        return 2
    if not valid_public_note(public_note):
        print("error: public note must be one table cell", file=sys.stderr)
        return 2
    resolved = evidence_path(evidence)
    if not resolved.exists():
        print(f"error: evidence path does not exist: {evidence}", file=sys.stderr)
        return 2
    if not resolved.is_file():
        print(f"error: evidence path is not a file: {evidence}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    date = dt.date.today().isoformat()
    event_id = usage_event_id(topic, concept_id, event, evidence, date, public_note)
    rows = list(read_usage_rows(text))
    if any(problem is not None for _, _, problem in rows):
        print("error: malformed usage event section; fix it before appending", file=sys.stderr)
        return 2
    if any(cells[1] == event_id for _, cells, problem in rows):
        print(f"idempotent: {topic} | {concept_id} | {event_id}")
        return 0

    lines = text.split("\n")
    start, end = usage_section_bounds(lines)
    header = [
        "## Usage events",
        "| date | event_id | concept/item_ref | event | evidence | public note |",
        "|------|----------|------------------|-------|----------|-------------|",
    ]
    row = f"| {date} | {event_id} | {concept_id} | {event} | {evidence} | {public_note or '-'} |"
    if start is None:
        if lines and lines[-1] == "":
            lines.pop()
        lines.extend(["", *header, row, ""])
    else:
        lines.insert(usage_insert_at(lines, start, end), row)
    write_text(path, "\n".join(lines))
    print(f"{topic} | {concept_id} | {event} | {date} | {event_id}")
    return 0


def derived_usage(topic):
    path = load(topic)
    if path is None:
        return 2
    text = path.read_text(encoding="utf-8")
    rows = []
    for line_no, cells, problem in read_usage_rows(text):
        if problem is not None:
            print(f"error: usage row {line_no + 1} is {problem}", file=sys.stderr)
            return 2
        rows.append(cells)
    rows.sort(key=lambda cells: cells[0])
    latest = {}
    for concept_id in BASELINE_USAGE_IDS.get(topic, []):
        latest[concept_id] = {"last_used": "-", "last_clean_use": "-", "last_event": "-", "sessions": 0}
    for date, event_id, concept_id, event, evidence, note in rows:
        try:
            dt.date.fromisoformat(date)
        except ValueError:
            print(f"error: invalid usage date in row {event_id}", file=sys.stderr)
            return 2
        if event == "reading_session" and (topic, concept_id) != READING_GATE:
            print(
                f"error: reading_session row {event_id} must use {READING_GATE_TOPIC} / "
                f"{READING_GATE_ID}, not {topic} / {concept_id}",
                file=sys.stderr,
            )
            return 2
        state = latest.setdefault(
            concept_id,
            {"last_used": "-", "last_clean_use": "-", "last_event": "-", "sessions": 0},
        )
        state["last_event"] = f"{date}:{event}"
        if event in {"practised", "produced"} or (event == "reading_session" and (topic, concept_id) == READING_GATE):
            state["last_used"] = date
        if event == "reading_session" and (topic, concept_id) == READING_GATE:
            state["sessions"] += 1
        if event == "produced":
            state["last_clean_use"] = date
    for concept_id in sorted(latest):
        state = latest[concept_id]
        print(
            f"{topic} | {concept_id} | {state['last_used']} | "
            f"{state['last_clean_use']} | sessions={state['sessions']} | {state['last_event']}"
        )
    return 0


def concept_index():
    """Every curriculum concept keyed by id, across all topic files.

    The map is global because prereqs legitimately cross files (japanese-reading
    depends on japanese-grammar's first concept). A per-file map resolves those
    ids to None and hides the dependent concept forever, even after its prereq
    is met.
    """
    states = {}
    for path in sorted(CURRICULUM.glob("*.md")):
        for _, cells in read_rows(path.read_text(encoding="utf-8")):
            states.setdefault(cells[0], cells[3])
    return states


def unmet_prerequisites(states, cells):
    """Prereq ids that are not yet learned; ids absent everywhere are dangling."""
    unmet = []
    for item in cells[2].split(","):
        item = item.strip()
        if not item or item == "-":
            continue
        if states.get(item) not in {"review", "solid"}:
            unmet.append(item)
    return unmet


def cmd_due():
    """Concepts whose own evidence is due.

    Deliberately does NOT filter on prerequisites. Two different questions are
    easy to conflate here:

      - Is my evidence for this concept stale?      -> this is `due`
      - Can I usefully *teach* this concept now?    -> this is `frontier`

    Learners legitimately learn out of order, and withholding a concept you
    demonstrably learned defeats the point of spaced review. A prerequisite is
    a teaching-order recommendation, not a law. Enforcing it against the review
    queue produced the incoherent output where c5 was offered while its own
    stated prerequisite c4 was withheld. Ordering is owned by the technical and
    map skills, and made inspectable by `frontier`.
    """
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


def cmd_frontier():
    """Concepts ready to teach, and how much is queued behind them.

    This is the teaching gate that `due` deliberately is not. It reports only
    the *roots* of the unlearned forest -- an unlearned concept whose own
    prerequisites are already learned. Everything downstream is reachable by
    teaching these first, so listing all 150 blocked rows would be noise, and
    noise is exactly what a cold agent has to sift through.
    """
    states = concept_index()
    ready = []
    blocked = 0
    dangling = []
    for path in sorted(CURRICULUM.glob("*.md")):
        for _, cells in read_rows(path.read_text(encoding="utf-8")):
            if cells[3] in {"review", "solid"}:
                continue
            unmet = unmet_prerequisites(states, cells)
            missing = [item for item in unmet if item not in states]
            if missing:
                dangling.append((path.stem, cells[0], missing))
            if unmet:
                blocked += 1
            else:
                ready.append((path.stem, cells[0], cells[3]))
    for topic, concept_id, state in sorted(ready):
        print(f"{topic} | {concept_id} | {state} | ready to teach")
    print(f"\n{len(ready)} ready; {blocked} blocked behind unmet prerequisites")
    for topic, concept_id, missing in dangling:
        print(
            f"warning: {topic}: {concept_id} references unknown prereq "
            f"{', '.join(missing)}; treating it as unmet",
            file=sys.stderr,
        )
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
    try:
        rung = int(rung_arg) if rung_arg is not None else current
    except (TypeError, ValueError):
        print(f"error: rung must be an integer 0..{len(LADDER) - 1}", file=sys.stderr)
        return 2
    if not 0 <= rung < len(LADDER):
        print(f"error: rung must be 0..{len(LADDER) - 1}", file=sys.stderr)
        return 2
    if cells[3] in ("unknown", "seen"):
        cells[3] = "review"
    elif cells[3] == "solid" and rung == 0:
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
        "\n## Usage events\n"
        "| date | event_id | concept/item_ref | event | evidence | public note |\n"
        "|------|----------|------------------|-------|----------|-------------|\n"
        "| 2026-09-12 | e1 | c1 | practised | scripts/review.py | attempt |\n"
        "| 2026-09-13 | e2 | c1 | produced | scripts/review.py | clean |\n"
    )
    rows = list(read_rows(fixture))
    assert [c[0] for _, c in rows] == ["c1", "c2"], rows
    usage = list(read_usage_rows(fixture))
    assert len(usage) == 2, usage
    assert all(problem is None for _, _, problem in usage), usage

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
    event_id = usage_event_id("t", "c1", "produced", "scripts/review.py", "2026-09-13")
    assert len(event_id) == 12
    assert event_id == usage_event_id("t", "c1", "produced", "scripts/review.py", "2026-09-13")

    assert READING_GATE == ("japanese-reading", "read-30-session-gate"), READING_GATE
    assert BASELINE_USAGE_IDS == {READING_GATE_TOPIC: [READING_GATE_ID]}, BASELINE_USAGE_IDS
    assert "read-30-session-gate" in __doc__, "module docstring must name the reading gate id"

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
    if cmd == "frontier" and not rest:
        return cmd_frontier()
    if cmd == "usage" and len(rest) == 1:
        return derived_usage(rest[0])
    if cmd == "usage" and len(rest) in (4, 5):
        topic, concept_id, event, evidence = rest[:4]
        note = rest[4] if len(rest) == 5 else ""
        path = load(topic)
        if path is None:
            return 2
        return append_usage(path, topic, concept_id, event, evidence, note)
    if cmd == "schedule" and 2 <= len(rest) <= 3:
        return cmd_schedule(rest[0], rest[1], rest[2] if len(rest) == 3 else None)
    if cmd == "next" and len(rest) == 3 and rest[2] in ("hit", "hard", "miss"):
        return cmd_next(rest[0], rest[1], rest[2])
    if cmd == "selftest" and not rest:
        return cmd_selftest()
    print("usage: review.py due | frontier | schedule <topic> <id> [rung] | next <topic> <id> hit|hard|miss | usage <topic> | usage <topic> <id> <event> <evidence> [note] | selftest", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
