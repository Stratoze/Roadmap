#!/usr/bin/env python3
"""Read-only validation for the approved learning-system layout."""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

from question_signatures import prompt_signature, variant_signature

ROOT = Path(__file__).resolve().parent.parent
CURRICULUM = ROOT / "_system" / "learning" / "curriculum"
REMOVED_REFS = [
    "docs/agents/issue-tracker", "docs/agents/triage-labels", "docs/agents/domain",
    "scripts/cold_tools.sh", "harness-opencode", "harness-codex",
]
PROTECTED_PREFIXES = (
    "Daily/", "_system/learning/lessons/", "Mechatronics/milestones/evidence/",
    "Mechatronics/docs/captures/", "Mechatronics/data/", "Mechatronics/resources/SAFETY_CARD.md",
    "_system/Landmine Log.md", "Changelog/",
)
EXCLUDED_REF_FILES = {
    "docs/agents/japanese-tutor-and-lean-system-plan.md",
    "scripts/validate_learning.py",
}
# Explicitly approved one-time migrations: privacy cleanup, Japanese reset
# handoff, and technical-session metadata. Entries expire and must be removed
# after review.
MIGRATION_ALLOWLIST = {
    "Daily/2026-09-25.md": "2026-10-03",
    "_system/learning/lessons/japanese-grammar/2026-09-14-godan-e-row-potential.md": "2026-10-03",
    "_system/learning/lessons/math-odes/2026-09-22-cooling-rule-and-euler.md": "2026-10-03",
}
BLOCKER_RE = re.compile(r"^- blocker \d{4}-\d{2}-\d{2} [^:]+:")
SEP_RE = re.compile(r"^:?-+:?$")
DAILY_NOTE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")
# A new date-stamped daily note is the normal session output, not protected
# learner history. Editing or deleting an existing note stays protected.
ADDED_STATUSES = {"A", "??"}
# Technical records are recognised by any of these markers. Widening the set
# means a partially written record is still held to the break/variant rules
# instead of slipping through unrecognised.
TECHNICAL_MARKERS = (
    "type: technical",
    "## Technical record status:",
    "## Cold conceptual check",
    "## Question variants",
    "## Break",
    "## Assessor",
)
LEGACY_STATUS_MARKER = "## Technical record status: legacy"
GATE_CLAIM_RE = re.compile(r"gate_(?:earned|met)\s*:\s*(?:mvm|full|yes)\b", re.IGNORECASE)


def curriculum_files():
    return sorted(CURRICULUM.glob("*.md"))


def section(text, heading):
    marker = f"## {heading}"
    start = text.find(marker)
    if start < 0:
        return ""
    end = text.find("\n## ", start + len(marker))
    return text[start:] if end < 0 else text[start:end]


def parse_porcelain_z(stdout):
    """Parse `git status --porcelain -z` into {path: {status letters}}.

    In `-z` output the new path of a rename comes first and the original path
    follows as the next NUL-separated entry, so the original is skipped instead
    of replacing the path.
    """
    changes = {}
    entries = stdout.split("\0")
    index = 0
    while index < len(entries):
        entry = entries[index]
        index += 1
        if not entry or len(entry) < 4:
            continue
        status = entry[:2].strip() or "?"
        path = entry[3:]
        if "R" in entry[:2] or "C" in entry[:2]:
            index += 1
        changes.setdefault(path.replace("\\", "/"), set()).add(status)
    return changes


def git_changed_paths(base=None):
    """Return sorted (status, path) pairs for working-tree and range changes."""
    result = subprocess.run(
        ["git", "-c", "core.quotepath=false", "status", "--porcelain", "-z", "--untracked-files=all"],
        cwd=ROOT, text=True, encoding="utf-8", errors="replace", capture_output=True, check=False,
    )
    changes = parse_porcelain_z(result.stdout)
    if base:
        committed = subprocess.run(
            ["git", "-c", "core.quotepath=false", "diff", "--name-status", f"{base}..HEAD"],
            cwd=ROOT, text=True, encoding="utf-8", errors="replace", capture_output=True, check=False,
        )
        for line in committed.stdout.splitlines():
            parts = [part.strip().replace("\\", "/") for part in line.split("\t") if part.strip()]
            if len(parts) < 2:
                continue
            changes.setdefault(parts[-1], set()).update(parts[0][:1])
    return sorted((status, path) for path, status in changes.items())


def is_new_daily_note(statuses, rel):
    """A newly created date-stamped daily note is never a protected change."""
    if not statuses or statuses - ADDED_STATUSES:
        return False
    return rel.startswith("Daily/") and bool(DAILY_NOTE_RE.fullmatch(rel[len("Daily/"):]))


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
        if not path.is_file() or ".git" in path.parts or ".scratch" in path.parts or "_private" in path.parts or ".obsidian" in path.parts or ".venv" in path.parts:
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


def migration_allowed(rel):
    expiry = MIGRATION_ALLOWLIST.get(rel)
    return bool(expiry and dt.date.today() <= dt.date.fromisoformat(expiry))


def check_protected(errors, base=None):
    for statuses, rel in git_changed_paths(base):
        if rel in EXCLUDED_REF_FILES or migration_allowed(rel):
            continue
        if is_new_daily_note(statuses, rel):
            continue
        if rel.startswith("Changelog/"):
            # Per-commit, not net-diff. A whole-range set comparison cannot see a
            # mid-range rewrite: a commit that removes a line and re-adds a
            # changed version nets to zero removed lines across the range, so the
            # violation passes even though the individual commit edited history.
            # Each commit must be append-only on its own.
            revisions = subprocess.run(
                ["git", "log", "--format=%H", (f"{base}..HEAD" if base else "HEAD"), "--", rel],
                cwd=ROOT, text=True, encoding="utf-8", errors="replace",
                capture_output=True, check=False,
            ).stdout or ""
            for sha in revisions.split():
                diff = subprocess.run(
                    ["git", "show", "--format=", "--unified=0", sha, "--", rel],
                    cwd=ROOT, text=True, encoding="utf-8", errors="replace",
                    capture_output=True, check=False,
                ).stdout or ""
                removed = {
                    line[1:].strip()
                    for line in diff.splitlines()
                    if line.startswith("-") and not line.startswith("---")
                }
                added = {
                    line[1:].strip()
                    for line in diff.splitlines()
                    if line.startswith("+") and not line.startswith("+++")
                }
                if removed - added:
                    errors.append(
                        f"Changelog change is not append-only: {rel} (commit {sha[:7]} rewrote "
                        f"{len(removed - added)} line(s))"
                    )
                    break
            continue
        if any(rel == prefix or rel.startswith(prefix) for prefix in PROTECTED_PREFIXES):
            errors.append(f"protected path changed: {rel}")


def check_handoffs(errors):
    required = {
        "Japanese/CURRENT.md": "Japanese/CURRENT",
        "Mechatronics/CURRENT.md": "Mechatronics/CURRENT",
        "Japanese/SOURCES.md": "Japanese/SOURCES",
        "Japanese/source-map.json": "Japanese/source-map",
        "scripts/session_state.py": "scripts/session_state.py",
        "scripts/anki_bridge.py": "scripts/anki_bridge.py",
    }
    for rel, label in required.items():
        if not (ROOT / rel).exists():
            errors.append(f"missing handoff/tool: {label}")
    current = ROOT / "Japanese" / "CURRENT.md"
    if current.exists():
        text = current.read_text(encoding="utf-8")
        for marker in ("conversation warm-up", "grammar contrast", "rewrite"):
            if marker not in text:
                errors.append(f"Japanese handoff missing {marker}")
    target = ROOT / "Mechatronics" / "CURRENT.md"
    if target.exists():
        text = target.read_text(encoding="utf-8")
        for marker in ("dependency", "Phase-0", "Next action"):
            if marker not in text:
                errors.append(f"technical handoff missing {marker}")


def signature_record_text(path, rel, errors):
    """Read a lesson record; a missing or unreadable record fails closed."""
    if not path.is_file():
        errors.append(f"technical record path is missing: {rel}")
        return None
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        errors.append(f"technical record is unreadable: {rel}: {exc}")
        return None


def is_plain_concept_check(stage, values, context):
    """True when a cold row is a genuine conceptual probe, not a reused test.

    A cold conceptual check may re-ask a concept - that is retention testing,
    and the learner's decision scopes the reuse ban to fresh transfer and
    implementation. But the exemption must not become a blank pass: a cold row
    that carries a real value set or lab condition is describing a *test
    instance*, and a test instance may not repeat whatever the stage. So the
    exemption holds only when the row records no instance - the placeholder `-`
    used throughout these records for "not applicable".
    """
    if str(stage).strip().lower() != "cold":
        return False
    return all(not str(part).strip() or str(part).strip() == "-"
               for part in (values, context))


def row_exempts_cold_reuse(cells):
    """`is_plain_concept_check` for a raw variant-table row."""
    if len(cells) == 4:
        return is_plain_concept_check(cells[0], "", "")
    return is_plain_concept_check(cells[0], cells[2], cells[3])


def variant_rows(text, rel, errors):
    """Yield validated (stage, prompt, values, context) rows of the variant table."""
    variants = section(text, "Question variants")
    for line in variants.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or all(SEP_RE.fullmatch(cell) for cell in cells):
            continue
        if cells[0] == "stage":
            continue
        if len(cells) not in {4, 7}:
            errors.append(f"technical record has malformed question variant row: {rel}")
            continue
        if len(cells) == 4:
            signature_cells = [cells[2]]
            reused_cell = cells[3]
        else:
            signature_cells = [cells[4], cells[5]]
            reused_cell = cells[6]
        # `reused?` is a violation only where repeating is actually forbidden.
        # A cold conceptual check re-asking a concept is retention testing, so
        # marking it honestly must not fail the record - otherwise the two
        # checks disagree and an agent cannot record the truth.
        is_cold = row_exempts_cold_reuse(cells)
        if not is_cold and reused_cell.strip().lower() in {"yes", "true", "1", "reused"}:
            errors.append(f"technical record marks a prompt reused: {rel}")
        for signature_cell in signature_cells:
            if not signature_cell or not re.fullmatch(r"(?:sha256:)?[0-9a-f]{64}", signature_cell):
                errors.append(f"technical record has a missing/invalid prompt/variant signature: {rel}")
        if len(cells) == 4:
            expected_prompt = "sha256:" + prompt_signature(cells[1])
            if cells[2].lower() != expected_prompt.lower():
                errors.append(f"technical record prompt signature does not match stored prompt: {rel}")
        else:
            expected_prompt = "sha256:" + prompt_signature(cells[1])
            expected_variant = "sha256:" + variant_signature(cells[2], cells[3])
            if cells[4].lower() != expected_prompt.lower() or cells[5].lower() != expected_variant.lower():
                errors.append(f"technical record signature does not match stored prompt/variant: {rel}")
        yield cells[0], cells[1], cells[2] if len(cells) == 7 else "", cells[3] if len(cells) == 7 else ""


def check_signature_reuse(errors, records):
    """A test item may not repeat for fresh transfer or implementation.

    Per the learner's decision (2026-09-26, "same concept/equation: allowed.
    Same exact test item, value set, or lab condition: forbidden for fresh
    transfer and implementation. Full Pass requires a new scenario").

    The stage being checked decides, not the stage that used it first. A cold
    conceptual check may re-ask a concept - retrieving a known concept is the
    whole point, and it is how retention is tested. But a fresh transfer or
    implementation row may not reuse a prompt or a test instance, whether that
    signature was first spent on a cold check or on an earlier transfer.

    The cold exemption is deliberately narrow: it applies only to a genuine
    conceptual probe, which records no value set or lab condition (see
    `row_exempts_cold_reuse`). A cold row carrying real values is describing a
    test instance, and a test instance may not repeat whatever the stage.
    """
    seen = {"prompt": {}, "variant": {}}
    for topic, rel, rows in records:
        for stage, prompt, values, context in rows:
            plain = is_plain_concept_check(stage, values, context)
            for kind, digest in (
                ("prompt", prompt_signature(prompt)),
                # A pure concept check has no test instance, so it produces no
                # variant signature to reuse.
                ("variant", None if plain else (
                    variant_signature(values, context) if values or context else None
                )),
            ):
                if digest is None:
                    continue
                first = seen[kind].get(digest)
                if first and not plain:
                    errors.append(
                        f"technical record reuses a {kind} signature: {rel} (stage '{stage}') "
                        f"already used in {first}"
                    )
                if not first:
                    seen[kind][digest] = f"{rel} (stage '{stage}')"


def check_technical_records(errors):
    lessons = ROOT / "_system" / "learning" / "lessons"
    signature_records = []
    for path in sorted(lessons.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        text = signature_record_text(path, rel, errors)
        if text is None:
            continue
        is_technical = any(marker in text for marker in TECHNICAL_MARKERS)
        if not is_technical:
            continue
        has_break = "## Break" in text
        has_variants = "## Question variants" in text
        legacy = LEGACY_STATUS_MARKER in text
        if has_break:
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
        if not has_break and not legacy:
            errors.append(f"technical record missing break evidence: {rel}")
        if legacy and GATE_CLAIM_RE.search(text):
            errors.append(f"legacy technical record claims a gate: {rel}")
        if not has_variants:
            errors.append(f"technical record missing question variants: {rel}")
            continue
        rows = list(variant_rows(text, rel, errors))
        if rows:
            signature_records.append((path.parent.name, rel, rows))
    check_signature_reuse(errors, signature_records)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-git", action="store_true", help="skip working-tree protection checks")
    parser.add_argument("--base", help="also check committed changes from this base commit through HEAD")
    args = parser.parse_args(argv)
    errors = []
    check_sources(errors)
    check_handoffs(errors)
    check_technical_records(errors)
    check_removed_references(errors)
    if not args.no_git:
        check_protected(errors, args.base)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("learning validation ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
