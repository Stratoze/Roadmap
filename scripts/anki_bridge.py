#!/usr/bin/env python3
"""Optional local AnkiConnect bridge for Japanese vocabulary.

`status`, `due`, and `propose` are read-only: they never open a write path and
`propose` never needs a reachable Anki. Only `add-approved` writes, and it
requires an explicit word, deck, model, field mapping, an approver, and an
approval record stored on a real `_private/.../approval...` path.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from urllib.parse import urlparse

DEFAULT_URL = "http://127.0.0.1:8765"
LOOPBACK_HOSTS = {"127.0.0.1", "localhost", "::1"}
PRIVATE_ROOT = os.path.realpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "_private")
)


def build_payload(action, params, api_key=None):
    """AnkiConnect takes its named arguments inside a `params` object.

    A flattened request is silently dropped for reads - which made every deck
    report 0 due - and rejected outright for `addNote`.
    """
    payload = {"action": action, "version": 6, "params": dict(params)}
    if api_key:
        # Implementations read the key from the request root or from params.
        payload["key"] = api_key
        payload["params"]["key"] = api_key
    return payload


class AnkiConnect:
    def __init__(self, url=DEFAULT_URL, api_key=None, timeout=3):
        self.url = url
        self.api_key = api_key or None
        self.timeout = timeout
        if self.api_key and urlparse(url).hostname not in LOOPBACK_HOSTS:
            raise RuntimeError("refusing to send an Anki API key to a non-loopback URL")

    def call(self, action, **params):
        request = urllib.request.Request(
            self.url,
            data=json.dumps(build_payload(action, params, self.api_key)).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, OSError, ValueError,
                json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise RuntimeError(f"AnkiConnect unavailable at {self.url}: {exc}") from exc
        if not isinstance(body, dict):
            raise RuntimeError("AnkiConnect returned a non-object response")
        if body.get("error"):
            raise RuntimeError(body["error"])
        return body.get("result")

    def version(self):
        return self.call("version")

    def decks(self):
        return self.call("deckNames") or []

    def due(self, deck):
        safe_deck = deck.replace("\\", "\\\\").replace('"', '\\"')
        query = f'deck:"{safe_deck}" -is:suspended is:due'
        return len(self.call("findCards", query=query) or [])

    def add_note(self, deck, model, fields, tags):
        return self.call(
            "addNote",
            note={"deckName": deck, "modelName": model, "fields": fields, "tags": tags},
        )


def client_from_args(args):
    return AnkiConnect(args.url, args.key)


def approval_evidence_path(value):
    """Resolve --approval-evidence to a real file under `_private/` on an approval path.

    The gate is a path gate, not a name hint: the file must really live under the
    vault `_private/` root (after symlink resolution) and at least one component
    of that relative path must be an approval path.
    """
    raw = str(value or "").strip()
    if not raw:
        raise RuntimeError("--approval-evidence must name a file under _private/")
    path = os.path.realpath(os.path.abspath(raw))
    if not os.path.isfile(path):
        raise RuntimeError(f"approval evidence is not a file: {raw}")
    try:
        relative = os.path.relpath(path, PRIVATE_ROOT)
    except ValueError:  # different Windows drive
        relative = os.pardir
    parts = [part for part in relative.split(os.sep) if part not in ("", os.curdir)]
    if os.path.isabs(relative) or parts[:1] == [os.pardir]:
        raise RuntimeError(
            f"approval evidence must live under {os.path.basename(PRIVATE_ROOT)}/: {raw}"
        )
    if not any("approval" in part.lower() for part in parts):
        raise RuntimeError(
            f"approval evidence must sit on an approval path under _private/ "
            f"(one component must contain 'approval'): {raw}"
        )
    return path


def approved_note(client, deck, model, fields, tags):
    """Create exactly one approved note. A refused creation is a failure, not a success line."""
    if not str(deck).strip() or not str(model).strip():
        raise RuntimeError("--deck and --model are required to create a note")
    empty = sorted(name for name, value in fields.items() if not str(value).strip())
    if empty:
        raise RuntimeError(f"note fields must not be empty: {', '.join(empty)}")
    note_id = client.add_note(deck, model, fields, tags)
    if note_id is None or isinstance(note_id, bool) or note_id == "" or note_id == 0:
        raise RuntimeError(
            "AnkiConnect returned no note id: the note was not created "
            "(duplicate note, unknown model/field, or a refused write); nothing was added"
        )
    return note_id


def print_status(client):
    print(f"AnkiConnect: {client.version()}")
    print("Decks:")
    for deck in client.decks():
        print(f"  - {deck}")


def print_due(client):
    for deck in client.decks():
        print(f"{deck}: {client.due(deck)} due")


def parse_fields(args):
    return {args.front_field: args.front, args.back_field: args.back}


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=os.environ.get("ANKI_CONNECT_URL", DEFAULT_URL))
    parser.add_argument("--key", default=os.environ.get("ANKI_API_KEY"))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="show AnkiConnect version and deck names")
    sub.add_parser("due", help="show due counts by deck; read-only")
    propose = sub.add_parser("propose", help="print an approval-gated mining proposal; writes nothing")
    propose.add_argument("word")
    propose.add_argument("--reading", default="")
    propose.add_argument("--sentence", default="")
    propose.add_argument("--tags", default="japanese,immersion")
    add = sub.add_parser("add-approved", help="create one explicitly approved note")
    add.add_argument("word")
    add.add_argument("--deck", required=True)
    add.add_argument("--model", required=True)
    add.add_argument("--front-field", default="Front")
    add.add_argument("--back-field", default="Back")
    add.add_argument("--front", required=True)
    add.add_argument("--back", required=True)
    add.add_argument("--tags", default="japanese,immersion")
    add.add_argument("--approved-by", required=True)
    add.add_argument("--approval-evidence", required=True)
    return parser


def run(args):
    if args.command == "propose":
        print(json.dumps({
            "status": "proposal-only",
            "word": args.word,
            "reading": args.reading,
            "sentence": args.sentence,
            "tags": args.tags,
            "action": "ask learner for approval before add-approved",
        }, ensure_ascii=False))
        return 0
    if args.command == "add-approved":
        # Gate first: nothing is opened towards Anki until the approval record is real.
        evidence = approval_evidence_path(args.approval_evidence)
        approver = str(args.approved_by).strip()
        if not approver:
            raise RuntimeError("--approved-by must name the learner or the approver")
        client = client_from_args(args)
        note_id = approved_note(client, args.deck, args.model, parse_fields(args), args.tags.split(","))
        print(json.dumps({
            "status": "created", "note_id": note_id, "word": args.word,
            "approved_by": approver, "approval_evidence": evidence,
        }, ensure_ascii=False))
        return 0
    client = client_from_args(args)
    if args.command == "status":
        print_status(client)
    elif args.command == "due":
        print_due(client)
    return 0


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        return run(args)
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
