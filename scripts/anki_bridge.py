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


# --- i+1 lane selection (read-only) -------------------------------------
#
# Two lanes, and they are not the same thing:
#
#   stretch - a genuinely new word. Legitimate only when nothing is pending,
#             because introducing new material on top of unlearned cards is
#             how a backlog silently becomes permanent.
#   patch   - a word the learner has met enough times that failing it means
#             something, but whose interval has collapsed. Not new input: it is
#             consolidation, and it should be labelled as such in conversation.
#
# The gate is a selection aid, not a scheduler. It never writes and never
# reschedules; Anki owns the due queue.

STUCK_REPS_MIN = 10
STUCK_INTERVAL_MAX_DAYS = 7
DEFAULT_WATCHED_DECKS = ("Kaishi 1.5k", "Lapis")

# Which field holds the word, per note type. Read-only display only - nothing
# is ever written from this map.
WORD_FIELD_BY_MODEL = {
    "Kaishi 1.5k": "Word",
    "Lapis": "Expression",
}


def _escape_deck(deck):
    return str(deck).replace("\\", "\\\\").replace('"', '\\"')


def _count(client, query):
    return len(client.call("findCards", query=query) or [])


def stuck_query(deck, reps_min=STUCK_REPS_MIN, interval_max=STUCK_INTERVAL_MAX_DAYS):
    return (
        f'deck:"{_escape_deck(deck)}" '
        f"prop:reps>={int(reps_min)} prop:ivl<{int(interval_max)}"
    )


def deck_lane_counts(client, deck, reps_min=STUCK_REPS_MIN, interval_max=STUCK_INTERVAL_MAX_DAYS):
    """Counts from AnkiConnect's own search operators, never local arithmetic.

    `cardsInfo.due` is a raw day offset for review cards, not days-from-today,
    so counting due-ness locally reports nonsense. Ask the server instead.
    """
    base = f'deck:"{_escape_deck(deck)}"'
    return {
        "deck": deck,
        "unlearned_new": _count(client, f"{base} is:new"),
        "unlearned_learning": _count(client, f"{base} is:learn"),
        "stuck": _count(client, stuck_query(deck, reps_min, interval_max)),
    }


def sample_stuck_words(client, deck, limit):
    """Name a few stuck words so the conversation has something concrete."""
    if limit <= 0:
        return []
    cards = client.call("findCards", query=stuck_query(deck)) or []
    if not cards:
        return []
    info = client.call("cardsInfo", cards=list(cards)[:limit]) or []
    note_ids = [c.get("note") for c in info if c.get("note")]
    if not note_ids:
        return []
    words = []
    for note in client.call("notesInfo", notes=note_ids) or []:
        model = note.get("modelName")
        field = WORD_FIELD_BY_MODEL.get(model)
        fields = note.get("fields") or {}
        if not field or field not in fields:
            continue
        value = str((fields[field] or {}).get("value") or "").strip()
        if value:
            words.append({"word": value, "model": model})
    return words


def iplusone(client, decks=DEFAULT_WATCHED_DECKS, sample=5,
             reps_min=STUCK_REPS_MIN, interval_max=STUCK_INTERVAL_MAX_DAYS):
    """Decide which lane the next Japanese conversation should use."""
    rows = [
        deck_lane_counts(client, deck, reps_min, interval_max)
        for deck in decks
    ]
    unlearned = sum(r["unlearned_new"] + r["unlearned_learning"] for r in rows)
    stuck = sum(r["stuck"] for r in rows)
    stretch = unlearned == 0
    patch = stuck > 0

    if stretch:
        lane = "stretch"
        why = "caught up on unlearned cards, so new material is the i+1 lane"
    elif patch:
        lane = "patch"
        why = f"{unlearned} unlearned card(s) pending block new words; patch a known word instead"
    else:
        lane = "hold"
        why = f"{unlearned} unlearned card(s) pending and nothing stuck to patch; clear those first"

    payload = {
        "lane": lane,
        "why": why,
        "stretch_available": stretch,
        "patch_available": patch,
        "unlearned_total": unlearned,
        "stuck_total": stuck,
        "threshold": {"reps_min": reps_min, "interval_max_days": interval_max},
        "decks": rows,
    }
    if patch and sample > 0:
        for deck in decks:
            words = sample_stuck_words(client, deck, sample)
            if words:
                payload["stuck_samples"] = words
                break
    return payload


def print_iplusone(client, decks, sample, reps_min, interval_max):
    payload = iplusone(client, decks, sample, reps_min, interval_max)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return payload


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=os.environ.get("ANKI_CONNECT_URL", DEFAULT_URL))
    parser.add_argument("--key", default=os.environ.get("ANKI_API_KEY"))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="show AnkiConnect version and deck names")
    sub.add_parser("due", help="show due counts by deck; read-only")
    lanes = sub.add_parser(
        "iplusone",
        help="decide the i+1 lane (stretch/patch) for the next Japanese session; read-only",
    )
    lanes.add_argument("--deck", action="append", dest="decks",
                       help="deck to watch; repeatable. Default: Kaishi 1.5k and Lapis")
    lanes.add_argument("--sample", type=int, default=5,
                       help="how many stuck words to name (0 disables)")
    lanes.add_argument("--reps-min", type=int, default=STUCK_REPS_MIN)
    lanes.add_argument("--interval-max", type=int, default=STUCK_INTERVAL_MAX_DAYS)
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
    elif args.command == "iplusone":
        print_iplusone(
            client,
            tuple(args.decks) if args.decks else DEFAULT_WATCHED_DECKS,
            max(0, args.sample),
            args.reps_min,
            args.interval_max,
        )
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
