#!/usr/bin/env python3
"""Read-only validation for the approved learning-system layout."""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURRICULUM = ROOT / "_system" / "learning" / "curriculum"
REMOVED_REFS = [
    "docs/agents/issue-tracker", "docs/agents/triage-labels", "docs/agents/domain",
    "scripts/cold_tools.sh", "harness-opencode", "harness-codex",
]
PROTECTED_PREFIXES = (
    "Daily/", "_private/", "_system/learning/lessons/", "Mechatronics/milestones/evidence/",
    "Mechatronics/docs/captures/", "Mechatronics/data/", "Mechatronics/resources/SAFETY_CARD.md",
    "_system/Landmine Log.md", "Changelog/",
)
EXCLUDED_REF_FILES = {
    "docs/agents/japanese-tutor-and-lean-system-plan.md",
    "scripts/validate_learning.py",
}
# Explicitly approved privacy migration: remove raw learner quotations from the
# public Japanese lesson and create the user-requested daily note.
APPROVED_MIGRATION_PATHS = {
    "Daily/2026-09-25.md",
    "_system/learning/lessons/japanese-grammar/2026-09-14-godan-e-row-potential.md",
}
BLOCKER_RE = re.compile(r"^- blocker \d{4}-\d{2}-\d{2} [^:]+:")


def curriculum_files():
    return sorted(CURRICULUM.glob("*.md"))


def section(text, heading):
    marker = f"## {heading}"
    start = text.find(marker)
    if start < 0:
        return ""
    end = text.find("\n## ", start + len(marker))
    return text[start:] if end < 0 else text[start:end]


def git_changed_paths():
    result = subprocess.run(
        ["git", "status", "--porcelain"], cwd=ROOT, text=True, encoding="utf-8", errors="replace", capture_output=True, check=False
    )
    paths = []
    for line in result.stdout.splitlines():
        if len(line) < 4:
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append(path.replace("\\", "/"))
    return paths


def check_sources(errors):
    for path in curriculum_files():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        if "## Sources" in text:
            errors.append(f"legacy source heading: {rel}")
        if "## Resources" not in text:
            errors.append(f"missing canonical resources heading: {rel}")
            continue
        for line in section(text, "Resources").splitlines():
            stripped = line.strip()
            if stripped.startswith("- blocker ") and not BLOCKER_RE.fullmatch(stripped):
                errors.append(f"malformed source blocker: {rel}: {stripped}")
            if not stripped.startswith("- ") or "http" not in stripped:
                continue
            if " for " not in stripped or not any(v in stripped for v in ("verified ", "unverified", "rejected")):
                errors.append(f"source entry lacks concept ids/verdict: {rel}: {stripped}")


def check_removed_references(errors):
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or ".scratch" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel in EXCLUDED_REF_FILES or rel.startswith(("_system/learning/archive/", "Changelog/")):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for removed in REMOVED_REFS:
            if removed in text:
                errors.append(f"live reference to removed path {removed}: {rel}")


def check_protected(errors):
    for rel in git_changed_paths():
        if rel in EXCLUDED_REF_FILES or rel in APPROVED_MIGRATION_PATHS:
            continue
        if rel.startswith("Changelog/"):
            diff = subprocess.run(
                ["git", "diff", "HEAD", "--unified=0", "--", rel], cwd=ROOT, text=True,
                encoding="utf-8", errors="replace", capture_output=True, check=False,
            ).stdout or ""
            removed = {line[1:].strip() for line in diff.splitlines() if line.startswith("-") and not line.startswith("---")}
            added = {line[1:].strip() for line in diff.splitlines() if line.startswith("+") and not line.startswith("+++")}
            if removed - added:
                errors.append(f"Changelog change is not append-only: {rel}")
            continue
        if any(rel == prefix or rel.startswith(prefix) for prefix in PROTECTED_PREFIXES):
            errors.append(f"protected path changed: {rel}")


def check_technical_records(errors):
    lessons = ROOT / "_system" / "learning" / "lessons"
    for path in lessons.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "## Break" not in text:
            continue
        rel = path.relative_to(ROOT).as_posix()
        start = re.search(r"^- Start \(ISO\):\s*(\S+)", text, re.MULTILINE)
        end = re.search(r"^- End \(ISO\):\s*(\S+)", text, re.MULTILINE)
        if not start or not end:
            errors.append(f"technical record missing break timestamps: {rel}")
        else:
            try:
                started = dt.datetime.fromisoformat(start.group(1).replace("Z", "+00:00"))
                ended = dt.datetime.fromisoformat(end.group(1).replace("Z", "+00:00"))
                if (ended - started).total_seconds() < 20 * 60:
                    errors.append(f"technical record break is under 20 minutes: {rel}")
            except ValueError:
                errors.append(f"technical record has invalid break timestamp: {rel}")
        variants = section(text, "Question variants")
        for line in variants.splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) != 4 or cells[0] in {"stage", "----"}:
                continue
            if cells[3].lower() == "yes":
                errors.append(f"technical record marks a prompt reused: {rel}")
            if cells[2] and not re.fullmatch(r"(?:sha256:)?[0-9a-f]{64}", cells[2]):
                errors.append(f"technical record has an invalid prompt signature: {rel}")


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-git", action="store_true", help="skip working-tree protection checks")
    args = parser.parse_args(argv)
    errors = []
    check_sources(errors)
    check_technical_records(errors)
    check_removed_references(errors)
    if not args.no_git:
        check_protected(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("learning validation ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
