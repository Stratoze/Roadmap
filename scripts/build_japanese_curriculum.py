#!/usr/bin/env python3
"""Verify the Yokubi-ordered Japanese grammar structure without touching SRS state.

The public grammar table owns concept state (state / rung / next_review /
evidence). This script only *compares* the source-derived columns - id, aim,
and prereqs - against `Japanese/source-map.json` and prints a diff. It never
writes to the curriculum file, so a regeneration can never destroy learner SRS
state or evidence.
"""
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "Japanese" / "source-map.json"
TARGET = ROOT / "_system" / "learning" / "curriculum" / "japanese-grammar.md"
HEADER = ("id", "aim", "prereqs")
LOCATOR_RE = re.compile(r"yokubi-lesson-(\d+)")


class StructureError(Exception):
    """The public table cannot be compared to the source map at all."""


def concept_id(number):
    return f"jp-yokubi-{number:02d}"


def generated_structure(lessons):
    """The id/aim/prereqs columns the source map implies, header row included."""
    rows = [HEADER]
    previous = "-"
    numbers = []
    for lesson in lessons:
        number = lesson.get("lesson")
        if number is None:
            raise StructureError(f"source lesson has no numeric lesson id: {lesson}")
        if lesson.get("id") != f"yokubi-lesson-{number}":
            raise StructureError(f"source lesson id does not match its lesson number: {lesson}")
        numbers.append(number)
        rows.append((concept_id(number), lesson["title"], previous))
        previous = concept_id(number)
    if len(set(numbers)) != len(numbers):
        duplicates = sorted({n for n in numbers if numbers.count(n) > 1})
        raise StructureError(f"duplicate lesson numbers in the source map: {duplicates}")
    return rows


def current_structure(text):
    """The id/aim/prereqs columns actually written in the public table.

    Returns the header row followed by one tuple per concept row, so the result
    is directly comparable with :func:`generated_structure`.
    """
    try:
        start = text.index("## Concepts")
        end = text.index("## Resources", start)
    except ValueError as exc:
        raise StructureError(f"grammar file is missing the Concepts/Resources headings: {exc}") from exc
    rows = [HEADER]
    seen = set()
    for line in text[start:end].splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 7:
            continue
        if tuple(cells[:3]) == HEADER or all(set(cell) <= {"-"} for cell in cells):
            continue
        if cells[0] in seen:
            raise StructureError(f"duplicate concept id in the grammar table: {cells[0]}")
        seen.add(cells[0])
        rows.append(tuple(cells[:3]))
    return rows


def evidence_cells(text):
    cells_by_id = {}
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) == 7:
            cells_by_id.setdefault(cells[0], cells[6])
    return cells_by_id


def locator_mismatches(text):
    """Concept ids whose evidence cell cites the wrong Yokubi lesson.

    Only rows that still name a `yokubi-lesson-N` locator are checked, so real
    learner evidence written into the same cell later never trips this guard.
    """
    problems = []
    for concept, evidence in evidence_cells(text).items():
        cited = LOCATOR_RE.search(evidence)
        if not cited:
            continue
        expected = concept_id(int(cited.group(1)))
        if concept != expected:
            problems.append(
                f"{concept}: evidence cites {cited.group(0)}, which maps to {expected}"
            )
    return problems


def diff_lines(current_lines, expected_lines):
    """One diff line at a time, whatever the platform difflib does with lineterm.

    Some builds of `difflib._format_unified_diff` yield lines without
    appending `lineterm`, which collapses the whole diff onto a single output
    line. The diff is what a reviewer reads before changing the curriculum, so
    it must be split back apart here instead of trusted.
    """
    for chunk in difflib.unified_diff(
        current_lines, expected_lines,
        fromfile="current structure", tofile="source-map structure",
    ):
        for line in chunk.split("\n"):
            if line:
                yield line


def format_diff(expected, actual):
    current_lines = [" | ".join(row) for row in actual]
    expected_lines = [" | ".join(row) for row in expected]
    return "\n".join(diff_lines(current_lines, expected_lines)) + "\n"


def main(argv=None):
    try:
        data = json.loads(MAP.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"error: cannot read {MAP}: {exc}", file=sys.stderr)
        return 2
    try:
        expected = generated_structure(data["yokubi"]["lessons"])
        text = TARGET.read_text(encoding="utf-8")
        actual = current_structure(text)
    except (StructureError, OSError, KeyError) as exc:
        print(f"error: cannot compare the grammar table: {exc}", file=sys.stderr)
        return 2

    locators = locator_mismatches(text)
    for problem in locators:
        print(f"error: source locator mismatch: {problem}", file=sys.stderr)

    if actual != expected:
        print(
            "grammar structure differs from the source map; no changes written. "
            "Review the diff and update the id/aim/prereqs cells deliberately:\n",
        )
        print(format_diff(expected, actual))
        return 2
    if locators:
        print("error: source locators disagree with the concept ids; no changes written", file=sys.stderr)
        return 2
    print(f"verified {len(expected) - 1} Yokubi concept rows in {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
