"""Exact-prompt normalization and record checks for technical sessions."""
import argparse
import hashlib
import re
import sys
import unicodedata
from pathlib import Path

_MARKDOWN = re.compile(r"[`*_~]")
_DIGEST = re.compile(r"^[0-9a-f]{64}$")


def normalize_prompt(prompt):
    """Normalize formatting only; this does not deduplicate semantics."""
    text = unicodedata.normalize("NFKC", prompt)
    text = _MARKDOWN.sub("", text)
    return " ".join(text.lower().split())


def signature(prompt):
    normalized = normalize_prompt(prompt)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _as_signature(value):
    value = str(value).strip()
    if value.startswith("sha256:"):
        value = value.split(":", 1)[1]
    return value.lower() if _DIGEST.fullmatch(value) else signature(value)


def prompt_reused(prompt, prior_signatures):
    return signature(prompt) in {_as_signature(value) for value in prior_signatures}


def record_signatures(path):
    """Read normalized signatures from a technical record's variant table."""
    signatures = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[0] not in {"stage", "----"} and not all(set(c) <= {"-"} for c in cells):
            value = cells[2]
            if value and value != "normalized signature":
                signatures.append(value)
    return signatures


def main(argv=None):
    parser = argparse.ArgumentParser(description="Technical question signature helper")
    sub = parser.add_subparsers(dest="command", required=True)
    sig = sub.add_parser("signature", help="print the normalized SHA-256 signature")
    sig.add_argument("prompt")
    check = sub.add_parser("check", help="fail if a prompt matches a record signature")
    check.add_argument("prompt")
    check.add_argument("--record", required=True)
    args = parser.parse_args(argv)
    if args.command == "signature":
        print(signature(args.prompt))
        return 0
    reused = prompt_reused(args.prompt, record_signatures(args.record))
    if reused:
        print(f"reused: {args.prompt}")
        return 1
    print("fresh: prompt signature is new")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
