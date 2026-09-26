"""Exact technical prompt and test-variant signatures."""
import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

_MARKDOWN = re.compile(r"[`*_~]")
_DIGEST = re.compile(r"^[0-9a-f]{64}$")


def normalize_part(value):
    text = unicodedata.normalize("NFKC", str(value or ""))
    text = _MARKDOWN.sub("", text)
    return " ".join(text.lower().split())


def normalize_prompt(prompt):
    return normalize_part(prompt)


def _digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def prompt_signature(prompt):
    return _digest(normalize_prompt(prompt))


def variant_signature(values, context):
    canonical = json.dumps([normalize_part(values), normalize_part(context)], ensure_ascii=False, separators=(",", ":"))
    return _digest(canonical)


def signature(prompt, values="", context=""):
    if values or context:
        return variant_signature(values, context)
    return prompt_signature(prompt)


def _as_digest(value):
    value = str(value).strip()
    if value.startswith("sha256:"):
        value = value.split(":", 1)[1]
    return value.lower() if _DIGEST.fullmatch(value) else None


def prompt_reused(prompt, prior_signatures, values="", context=""):
    prior = {_as_digest(value) for value in prior_signatures}
    prior.discard(None)
    target = variant_signature(values, context) if values or context else prompt_signature(prompt)
    return target in prior


def _record_files(path):
    target = Path(path)
    if not target.exists():
        raise ValueError(f"record path does not exist: {path}")
    if target.is_file():
        # A single record still means its topic: the other records beside it count too.
        return [target, *sorted(other for other in target.parent.glob("*.md") if other != target)]
    return sorted(target.rglob("*.md"))


def _collect(record, result):
    for line in record.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or all(not cell for cell in cells):
            continue
        if cells[0] in {"stage", "----"} or all(set(cell) <= {"-"} for cell in cells):
            continue
        if len(cells) == 4:
            digest = _as_digest(cells[2])
            if digest:
                result["prompt"].add(digest)
        elif len(cells) == 7:
            prompt_digest = _as_digest(cells[4])
            variant_digest = _as_digest(cells[5])
            if prompt_digest:
                result["prompt"].add(prompt_digest)
            if variant_digest:
                result["variant"].add(variant_digest)
    return result


def record_signatures(paths):
    """Read prompt and variant signatures across one or more records/topic directories."""
    if isinstance(paths, (str, Path)):
        paths = [paths]
    result = {"prompt": set(), "variant": set()}
    seen = set()
    for path in paths:
        for record in _record_files(path):
            resolved = record.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            _collect(record, result)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Technical prompt/variant signature helper")
    sub = parser.add_subparsers(dest="command", required=True)
    sig = sub.add_parser("signature", help="print prompt or variant SHA-256")
    sig.add_argument("prompt", nargs="?")
    sig.add_argument("--values", default="")
    sig.add_argument("--context", default="")
    check = sub.add_parser("check", help="fail if a prompt or test variant matches any record")
    check.add_argument("prompt")
    check.add_argument("--values", default="")
    check.add_argument("--context", default="")
    check.add_argument(
        "--record", required=True, nargs="+",
        help="record file, topic directory, or several of them; reuse is checked across all of them",
    )
    check.add_argument(
        "--stage", default="fresh transfer", choices=["cold", "fresh transfer", "implementation"],
        help=(
            "which stage this question is for. `cold` is a conceptual check and may "
            "re-ask a known concept, so a match is reported but does not fail. The "
            "other stages forbid reuse, per the learner's 2026-09-26 decision."
        ),
    )
    args = parser.parse_args(argv)
    if args.command == "signature":
        print(signature(args.prompt or "", args.values, args.context))
        return 0
    try:
        records = record_signatures(args.record)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    prompt_hit = prompt_reused(args.prompt, records["prompt"])
    variant_hit = bool(args.values or args.context) and prompt_reused(args.prompt, records["variant"], args.values, args.context)
    is_cold = args.stage == "cold"
    if prompt_hit or variant_hit:
        if is_cold:
            # Reporting a match is still useful - the caller may want to know a
            # concept was asked before - but a cold check is allowed to repeat,
            # so it must not block the question.
            print(
                "match: signature is already in the record, but a cold conceptual "
                "check may re-ask a concept; recording reused? = yes is correct here"
            )
            return 0
        print("reused: prompt or test-variant signature is already in the record")
        return 1
    print("fresh: prompt or test-variant signature is new")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
