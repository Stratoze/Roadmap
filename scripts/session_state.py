#!/usr/bin/env python3
"""Read and explicitly update the daily session checklist."""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKLIST_IDS = ("session-1", "session-2", "session-3")
DEFAULT_LINES = {
    "session-1": "Japanese deliberate session (conversation + one grammar contrast)",
    "session-2": "Anki 20–30m + due review (30m cap)",
    "session-3": "Target-driven technical session",
}
ITEM_RE = re.compile(r"^-\s+\[( |x|~)\]\s+(session-[123])\s*—\s*(.*)$")


def today_note():
    return ROOT / "Daily" / f"{dt.date.today().isoformat()}.md"


def read_note(path):
    return path.read_text(encoding="utf-8") if path.exists() else None


def ensure_note(path):
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if "## Session checklist" not in text:
            block = "\n## Session checklist\n" + "\n".join(
                f"- [ ] {key} — {value} — pending" for key, value in DEFAULT_LINES.items()
            ) + "\n"
            text = text.rstrip() + "\n\n" + block
            path.write_text(text, encoding="utf-8", newline="\n")
        return text
    text = (
        "---\n"
        f"date: \"{dt.date.today().isoformat()}\"\n"
        "tags: [daily]\n"
        "---\n\n"
        "## Session checklist\n"
        + "\n".join(f"- [ ] {key} — {value} — pending" for key, value in DEFAULT_LINES.items())
        + "\n"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return text


def checklist(text):
    found = {}
    for line in text.splitlines():
        match = ITEM_RE.match(line)
        if match:
            mark, key, body = match.groups()
            found[key] = {"mark": mark, "body": body}
    return found


def update_item(text, key, state):
    lines = text.splitlines()
    for index, line in enumerate(lines):
        match = ITEM_RE.match(line)
        if not match or match.group(2) != key:
            continue
        body = re.sub(r"\s+—\s+(pending|in_progress|paused|done)$", "", match.group(3))
        mark = {"pending": " ", "in_progress": "~", "paused": "~", "done": "x"}[state]
        suffix = {"pending": "pending", "in_progress": "in_progress", "paused": "paused", "done": "done"}[state]
        lines[index] = f"- [{mark}] {key} — {body} — {suffix}"
        return "\n".join(lines) + "\n"
    raise ValueError(f"unknown checklist id: {key}")


def run_readonly(command):
    """Run a read-only helper; a non-zero exit fails closed as unavailable."""
    try:
        result = subprocess.run(command, cwd=ROOT, text=True, encoding="utf-8", errors="replace", capture_output=True, check=False)
    except OSError as exc:
        return False, f"unavailable: {exc}"
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip().splitlines()
        reason = detail[-1] if detail else f"exit {result.returncode}"
        return False, f"unavailable: {reason}"
    return True, result.stdout.strip() or result.stderr.strip() or "no output"


def handoff_summary(path):
    if not path.is_file():
        return "missing"
    text = path.read_text(encoding="utf-8")
    status = re.search(r"^\*\*Status:\*\*\s*(.+)$", text, re.MULTILINE)
    next_heading = re.search(r"^## Next action[ \t]*\r?\n([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    next_line = "-"
    if next_heading:
        for line in next_heading.group(1).splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("```") and not stripped.startswith("#"):
                next_line = stripped
                break
    status_text = status.group(1).strip() if status else "status unavailable"
    if next_line == "-":
        match = re.search(r"^- Next action:[ \t]*(.*)$", text, re.MULTILINE)
        if match and match.group(1).strip():
            next_line = match.group(1).strip()
    if next_line == "-" and "no active target" in status_text.lower():
        next_line = "learner names a target; ask one scoping question"
    if next_line == "-":
        next_line = "no explicit next-action section; read the handoff file"
    # A heading line like "Run one fresh Japanese session:" reads as a
    # truncated fragment in the one-line summary.
    next_line = next_line.rstrip(":").strip() or next_line
    return f"status={status_text} | next={next_line}"


def iplusone_lane():
    """The i+1 lane for the Japanese branch, or a reason it is unavailable.

    The gate is written down in the japanese skill, so an agent that never
    opens that file would plan a session around due counts alone and open with
    a new word on a `patch` lane. Surfacing the lane here makes the invariant
    visible from the first command, without duplicating the frontier or the
    reading count, which the curriculum and CURRENT.md already own.
    """
    ok, out = run_readonly([
        sys.executable, str(ROOT / "scripts" / "anki_bridge.py"), "iplusone", "--sample", "0"
    ])
    if not ok:
        return "lane=unavailable — ask the learner; do not assume new words are fine"
    try:
        payload = json.loads(out)
    except (ValueError, TypeError):
        return "lane=unreadable — ask the learner; do not assume new words are fine"
    lane = payload.get("lane", "unknown")
    unlearned = payload.get("unlearned_total", "?")
    stuck = payload.get("stuck_total", "?")
    return f"lane={lane} (unlearned={unlearned}, stuck={stuck})"


def report_today():
    path = today_note()
    if not path.exists():
        print(f"no daily note: {path.relative_to(ROOT).as_posix()}")
        print("next: run `python3 scripts/session_state.py init` when ready to start the checklist")
    else:
        text = read_note(path)
        items = checklist(text)
        print(f"Daily: {path.relative_to(ROOT).as_posix()}")
        if not items:
            print("checklist missing: run `python3 scripts/session_state.py init` to add it")
        for key in CHECKLIST_IDS:
            item = items.get(key)
            if item:
                state = {" ": "pending", "~": "paused/in_progress", "x": "done"}[item["mark"]]
                print(f"  {key}: {state} — {item['body']}")
        next_key = next((key for key in CHECKLIST_IDS if key in items and items[key]["mark"] != "x"), None)
        if next_key:
            print(f"next: {next_key} — {items[next_key]['body']}")
    print(f"Japanese handoff: Japanese/CURRENT.md | {handoff_summary(ROOT / 'Japanese' / 'CURRENT.md')}")
    print(f"  i+1 {iplusone_lane()}")
    print(f"Technical handoff: Mechatronics/CURRENT.md | {handoff_summary(ROOT / 'Mechatronics' / 'CURRENT.md')}")
    ok, due = run_readonly([sys.executable, str(ROOT / "scripts" / "review.py"), "due"])
    if not ok:
        print(f"Due review: {due} — treat as unknown, not as zero; resolve before the review slot")
    else:
        due_items = [
            line for line in due.splitlines()
            if " | " in line and not line.lstrip().startswith(("error:", "Traceback"))
        ]
        print(f"Due review: {len(due_items)} item(s) returned; cap at 30 minutes when larger")
    anki_ok, anki = run_readonly([sys.executable, str(ROOT / "scripts" / "anki_bridge.py"), "due"])
    if not anki_ok:
        print("Anki: 20–30 minutes — unavailable: " + anki.replace("unavailable: ", ""))
    else:
        print("Anki: 20–30 minutes — " + anki.replace("\n", "; "))
    return 0


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("today", help="read today's checklist and next action")
    sub.add_parser("init", help="create today's checklist if absent")
    for name in ("start", "done", "pause"):
        command = sub.add_parser(name, help=f"mark a checklist item {name}")
        command.add_argument("id", choices=CHECKLIST_IDS)
    args = parser.parse_args(argv)
    path = today_note()
    if args.command == "today":
        return report_today()
    text = ensure_note(path)
    if args.command == "init":
        print(f"initialized: {path.relative_to(ROOT)}")
        return 0
    state = {"start": "in_progress", "done": "done", "pause": "paused"}[args.command]
    try:
        path.write_text(update_item(text, args.id, state), encoding="utf-8", newline="\n")
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(f"{args.id}: {state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
