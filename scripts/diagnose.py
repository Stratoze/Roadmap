#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
diagnose.py - Obsidian vault link health checker.

Finds:
  BROKEN LINKS : [[wikilinks]] and [markdown](links) whose target file
                 does not exist.
  ORPHAN NOTES : .md files that receive no incoming link from any note.

Notes:
  * Links inside ``` code fences are ignored (avoids false positives from
    the many code examples in the milestone files).
  * _templates/ is scanned for links but never reported as broken/orphan
    (it is full of {{placeholders}} and is invoked by the Templater plugin).
  * Heading anchors (#...) are NOT validated - only file existence.

Usage:
    python diagnose.py [path/to/vault]      (default: current directory)

Exit codes: 0 = clean, 1 = issues found, 2 = bad usage.
"""
import re
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

# ---- config ----------------------------------------------------------------
# Folders ignored for ORPHAN detection. Templates are plugin-invoked;
# journals/logs are append-only and not meant to be linked. Add more here
# (e.g. "docs") if you consider folder-READMEs acceptable as orphans.
ORPHAN_EXCLUDE_DIRS = {"_templates", "journal", "Daily", "Logs"}
# Files allowed to have zero incoming links (entry points).
ENTRY_POINTS = {"index.md", "README.md"}
# ----------------------------------------------------------------------------

WIKILINK = re.compile(r"\[\[([^\[\]]+?)\]\]")
MDLINK   = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
FENCE    = re.compile(r"^\s*(```|~~~)")


def strip_fences(text):
    out, infence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            infence = not infence
            continue
        if not infence:
            out.append(line)
    return "\n".join(out)


def md_files(vault):
    for p in sorted(vault.rglob("*.md")):
        dirs = p.relative_to(vault).parts[:-1]
        if any(part.startswith(".") for part in dirs):   # .obsidian/.git/.trash
            continue
        yield p


def resolve_wiki(target, vault, by_name):
    """Return list of matching Paths, or None if the link is broken."""
    t = target.split("|")[0].split("#")[0].strip()
    if not t:
        return []                                   # [[#heading]] self-link
    if t.lower().endswith(".md"):
        t = t[:-3]
    if "/" in t or "\\" in t:                       # path-style, vault-root relative
        cand = vault / (t.replace("\\", "/") + ".md")
        return [cand] if cand.exists() else None
    hits = by_name.get(t.lower() + ".md")           # basename-style
    return hits if hits else None


def resolve_md(target, src):
    """Return a Path, the string 'skip', or None if broken."""
    t = target.strip()
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*://", t) or t.startswith("mailto:"):
        return "skip"                               # external URL
    if t.startswith("#"):
        return "skip"                               # same-file anchor
    t = t.split('"')[0].split("#")[0].strip()       # drop title + anchor
    if not t:
        return "skip"
    t = urllib.parse.unquote(t)
    cand = (src.parent / t).resolve()
    return cand if cand.exists() else None


def main():
    vault = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    if not vault.is_dir():
        print(f"ERROR: not a directory: {vault}")
        return 2

    files = list(md_files(vault))
    by_name = defaultdict(list)
    for p in files:
        by_name[p.name.lower()].append(p)

    broken   = defaultdict(list)
    incoming = set()

    for src in files:
        in_templates = "_templates" in src.relative_to(vault).parts
        text = strip_fences(src.read_text(encoding="utf-8", errors="replace"))

        for m in WIKILINK.finditer(text):
            raw = m.group(1)
            res = resolve_wiki(raw, vault, by_name)
            if res is None:
                if not in_templates:
                    broken[src].append(f"[[{raw}]]")
            else:
                incoming.update(res)

        for m in MDLINK.finditer(text):
            raw = m.group(1)
            res = resolve_md(raw, src)
            if res is None:
                if not in_templates:
                    broken[src].append(f"[...]({raw})")
            elif isinstance(res, Path):
                incoming.add(res)

    orphans = defaultdict(list)
    for p in files:
        parts = p.relative_to(vault).parts
        if any(part in ORPHAN_EXCLUDE_DIRS for part in parts[:-1]):
            continue
        if p.name in ENTRY_POINTS or p in incoming:
            continue
        folder = str(Path(*parts[:-1])) if len(parts) > 1 else "(root)"
        orphans[folder].append(p.name)

    n_broken  = sum(len(v) for v in broken.values())
    n_orphans = sum(len(v) for v in orphans.values())

    print(f"Vault: {vault}")
    print(f"Scanned {len(files)} notes.\n")

    if broken:
        print(f"BROKEN LINKS  ({n_broken})")
        for src in sorted(broken, key=str):
            print(f"  {src.relative_to(vault)}")
            for link in broken[src]:
                print(f"      -> {link}")
        print()
    else:
        print("BROKEN LINKS  none\n")

    if orphans:
        print(f"ORPHAN NOTES  ({n_orphans})  [no incoming links]")
        for folder in sorted(orphans):
            print(f"  {folder}/")
            for name in sorted(orphans[folder]):
                print(f"      {name}")
        print()
    else:
        print("ORPHAN NOTES  none\n")

    print(f"Result: {n_broken} broken link(s), {n_orphans} orphan(s).")
    return 1 if (broken or orphans) else 0


if __name__ == "__main__":
    raise SystemExit(main())
