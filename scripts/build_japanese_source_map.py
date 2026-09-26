#!/usr/bin/env python3
"""Build the public Japanese source map from a private source checkout.

The raw sources stay in the private repository. This script writes only
structure, provenance, and locators to the public Roadmap vault. It never
touches curriculum state.

Provenance is verified, not asserted:

- the private checkout's `origin` must be the declared private repository;
- the Yokubi checkout's `origin` must be the declared Yokubi repository;
- when a private root is given, both sources must live inside it;
- every SUMMARY lesson must carry a unique numeric lesson id, so concept ids
  are stable and a silently dropped lesson cannot shorten the spine.

Any failed check aborts before anything is written.
"""
import argparse
import datetime as dt
import hashlib
import html as html_lib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"^\s*[*-]\s+\[([^\]]+)\]\(([^)]+)\)\s*$")
LESSON_RE = re.compile(r"Lesson (\d+):\s*(.*)")
YOKUBI_PRIVATE_SUBPATH = "sources/yokubi"
YOKUBI_URL_BASE = "https://yoku.bi/"


class SourceError(Exception):
    """A provenance or source-integrity check failed."""


def git_value(root, *args):
    return subprocess.run(
        ["git", "-C", str(root), *args], text=True, encoding="utf-8",
        errors="replace", capture_output=True, check=True,
    ).stdout.strip()


def normalize_repo(url):
    """Compare repository URLs without trailing slash or .git noise."""
    return url.strip().rstrip("/").removesuffix(".git").lower()


def check_remote(root, expected, label):
    """Fail unless `root` is a git checkout whose origin is `expected`."""
    try:
        actual = git_value(root, "remote", "get-url", "origin")
    except (subprocess.CalledProcessError, OSError) as exc:
        raise SourceError(f"{label}: cannot read the origin remote of {root} ({exc})") from exc
    if normalize_repo(actual) != normalize_repo(expected):
        raise SourceError(f"{label} repository mismatch: {actual} != {expected}")
    return actual


def is_inside(child, parent):
    try:
        return child.resolve().is_relative_to(parent.resolve())
    except OSError:
        return False


def source_relative(path, private_root):
    """The private-repository-relative POSIX path recorded in the map."""
    if private_root and is_inside(path, private_root):
        return path.resolve().relative_to(private_root.resolve()).as_posix()
    return path.name


def yokubi_lessons(root, private_root):
    """Ordered lesson structure from the Yokubi SUMMARY table of contents.

    Raises on anything that would produce an unstable or colliding concept id.
    """
    summary = root / "src" / "SUMMARY.md"
    if not summary.is_file():
        raise SourceError(f"Yokubi summary not found: {summary}")
    lessons = []
    seen = set()
    for number, line in enumerate(summary.read_text(encoding="utf-8").splitlines(), start=1):
        match = LINK_RE.match(line)
        if not match or not match.group(1).lower().startswith("lesson "):
            continue
        title, rel = match.groups()
        numbered = LESSON_RE.match(title)
        if not numbered:
            raise SourceError(
                f"{summary.name}:{number}: lesson title has no numeric id: {title!r}"
            )
        lesson_number = int(numbered.group(1))
        lesson_title = numbered.group(2).strip()
        if lesson_number in seen:
            raise SourceError(f"{summary.name}:{number}: duplicate lesson number {lesson_number}")
        seen.add(lesson_number)
        target = PurePosixPath(rel.lstrip("/"))
        if target.suffix != ".md":
            raise SourceError(
                f"{summary.name}:{number}: lesson path is not a markdown file: {rel!r}"
            )
        public_path = f"{YOKUBI_PRIVATE_SUBPATH}/{target.as_posix()}"
        lessons.append({
            "id": f"yokubi-lesson-{lesson_number}",
            "lesson": lesson_number,
            "title": lesson_title,
            "path": public_path,
            "url": YOKUBI_URL_BASE + PurePosixPath(target.with_suffix(".html")).as_posix(),
        })
    if not lessons:
        raise SourceError(f"no lessons found in {summary}")
    if sorted(seen) != list(range(len(seen))):
        raise SourceError(f"lesson numbers are not contiguous from 0: {sorted(seen)}")
    if private_root and root.resolve() != (private_root / YOKUBI_PRIVATE_SUBPATH).resolve():
        raise SourceError(
            f"yokubi root {root} is not the declared private subpath {YOKUBI_PRIVATE_SUBPATH}"
        )
    return lessons


def imabi_anchors(path):
    """Structural anchor index for the local IMABI mirror.

    Labels are derived from heading text only; no prose is copied.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    anchors = []
    seen = set()
    heading_re = re.compile(r"<h[1-6][^>]*>(.*?)</h[1-6]>", re.IGNORECASE | re.DOTALL)
    for block in heading_re.findall(text):
        ids = re.findall(r'<a[^>]+id="([^"]+)"', block, re.IGNORECASE)
        label = html_lib.unescape(re.sub(r"<[^>]+>", " ", block))
        label = " ".join(label.split())
        for anchor_id in ids:
            if anchor_id in seen:
                continue
            seen.add(anchor_id)
            anchors.append({"id": anchor_id, "label": label})
    for anchor_id in re.findall(r'\bid="([^"]+)"', text):
        if anchor_id not in seen:
            seen.add(anchor_id)
            anchors.append({"id": anchor_id, "label": ""})
    return anchors


def build(args):
    checks = {}
    if args.private_root:
        if not args.private_root.is_dir():
            raise SourceError(f"private root is not a directory: {args.private_root}")
        check_remote(args.private_root, args.private_repo, "private")
        checks["private_repository"] = True
    else:
        checks["private_repository"] = False

    check_remote(args.yokubi_root, args.yokubi_repo, "yokubi")
    checks["yokubi_repository"] = True

    if not args.imabi_file.is_file():
        raise SourceError(f"IMABI mirror not found: {args.imabi_file}")
    checks["imabi_present"] = True

    inside = {}
    if args.private_root:
        inside["yokubi"] = is_inside(args.yokubi_root, args.private_root)
        inside["imabi"] = is_inside(args.imabi_file, args.private_root)
        for name, ok in inside.items():
            if not ok:
                raise SourceError(
                    f"{name} source is outside the declared private root {args.private_root}"
                )
    else:
        inside = {"yokubi": False, "imabi": False}
    checks["sources_inside_private_root"] = all(inside.values())

    lessons = yokubi_lessons(args.yokubi_root, args.private_root)
    anchors = imabi_anchors(args.imabi_file)
    imabi_digest = hashlib.sha256(args.imabi_file.read_bytes()).hexdigest()

    return {
        "generated": dt.date.today().isoformat(),
        "private_source_repository": args.private_repo,
        "private_root_verified": bool(args.private_root) and all(checks.values()),
        "verification": {
            **checks,
            "yokubi_root_inside_private_root": inside["yokubi"],
            "imabi_file_inside_private_root": inside["imabi"],
        },
        "yokubi": {
            "repository": args.yokubi_repo,
            "commit": git_value(args.yokubi_root, "rev-parse", "HEAD"),
            "license": "CC-BY-4.0",
            "role": "ordered beginner grammar spine",
            "lessons": lessons,
        },
        "imabi": {
            "local_file": source_relative(args.imabi_file, args.private_root),
            "sha256": imabi_digest,
            "provenance": "local mirror; verify disputed claims against the live source",
            "license": "unverified local mirror; derived structural index only",
            "role": "reference index and nuance map",
            "anchors": anchors,
        },
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--yokubi-root", required=True, type=Path)
    parser.add_argument("--imabi-file", required=True, type=Path)
    parser.add_argument("--private-repo", default="https://github.com/Stratoze/private-jp")
    parser.add_argument("--private-root", type=Path, help="private repository checkout to verify against --private-repo")
    parser.add_argument("--yokubi-repo", default="https://github.com/Morgawr/yokubi")
    parser.add_argument(
        "--allow-unverified", action="store_true",
        help="permit writing a map that does not record a verified private root",
    )
    parser.add_argument("--output", type=Path, default=ROOT / "Japanese" / "source-map.json")
    args = parser.parse_args(argv)

    try:
        data = build(args)
    except (SourceError, subprocess.CalledProcessError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        print("no changes written; the private source map was not regenerated.", file=sys.stderr)
        return 2

    if args.output.is_file() and not args.allow_unverified:
        try:
            previous = json.loads(args.output.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            previous = {}
        if previous.get("private_root_verified") and not data["private_root_verified"]:
            print(
                f"error: {args.output} already records a verified private root; "
                "refusing to overwrite it with an unverified map.",
                file=sys.stderr,
            )
            return 2

    if not data["private_root_verified"] and not args.allow_unverified:
        print(
            "error: private provenance is not verified. Pass --private-root (and the "
            "matching --private-repo) to verify the checkout, or --allow-unverified to "
            "record an explicitly unverified map.",
            file=sys.stderr,
        )
        return 2

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    verified = data["private_root_verified"]
    print(
        f"wrote {args.output} ({len(data['yokubi']['lessons'])} Yokubi lessons, "
        f"{len(data['imabi']['anchors'])} IMABI anchors, private provenance "
        f"{'verified' if verified else 'NOT verified'})"
    )
    return 0 if verified else 1


if __name__ == "__main__":
    raise SystemExit(main())
