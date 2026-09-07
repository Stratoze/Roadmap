#!/usr/bin/env python3
"""Pinned inventory exporter for the vault-scope reconciliation (v4 P0).

Reads a store's graphs/<topic>.json files, writes inventory JSON to stdout:
  {topic: {"file": name, "nodes": {node_id: {"claim_hash": ..., "kind": ..., "state": ...}},
           "count": N}, "_totals": {...}}

Canonical claim hash (BOTH sides must run THIS script — never one hash per engine):
  sha256 of the claim string after normalization:
    1. .lower()
    2. drop every char whose unicodedata category starts with "P" (punctuation)
       or "Z" (separator/whitespace), including ASCII space and underscores? NO —
       underscore "_" is category Pc (punctuation, connector) and IS dropped.
       Letters (L*) and numbers (N*) in ANY script (incl. Japanese kana/kanji) are kept.
    3. utf-8 encode, sha256 hexdigest.
Empty-after-normalization claims hash as "EMPTY" (flagged, never silently matched).

Near-misses (same concept, different wording/ID) WILL hash differently by design;
they go to the human-adjudication queue, never auto-matched.

Usage: python3 export_inventory.py <graphs-dir> [receipts-dir]
Exit 0 always on success; prints JSON to stdout (redirect to a file for the manifest).
Line endings: LF. Read-only: never writes to the store.
"""
import hashlib
import io
import json
import os
import sys
import unicodedata


def canon(text):
    out = []
    for ch in (text or "").lower():
        cat = unicodedata.category(ch)
        if cat[0] in ("P", "Z"):
            continue
        out.append(ch)
    norm = "".join(out)
    if not norm:
        return "EMPTY"
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def sha_file(path):
    h = hashlib.sha256()
    with io.open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    graphs = sys.argv[1] if len(sys.argv) > 1 else "graphs"
    rdir = sys.argv[2] if len(sys.argv) > 2 else None
    inv = {}
    total_nodes = 0
    receipt_counts = {}
    if rdir and os.path.isdir(rdir):
        for fn in sorted(os.listdir(rdir)):
            if fn.endswith(".jsonl"):
                with io.open(os.path.join(rdir, fn), encoding="utf-8") as f:
                    receipt_counts[fn[:-6]] = sum(1 for _ in f)
    for fn in sorted(os.listdir(graphs)):
        if not fn.endswith(".json") or ".bak" in fn or ".pre-batch" in fn:
            continue
        topic = fn[:-5]
        with io.open(os.path.join(graphs, fn), encoding="utf-8") as f:
            g = json.load(f)
        nodes = {}
        for nid in sorted(g.get("nodes", {})):
            n = g["nodes"][nid]
            nodes[nid] = {
                "claim_hash": canon(n.get("claim", "")),
                "kind": n.get("kind"),
                "state": (n.get("fsrs") or {}).get("state", n.get("state")),
            }
        inv[topic] = {
            "file": fn,
            "file_sha256": sha_file(os.path.join(graphs, fn)),
            "nodes": nodes,
            "count": len(nodes),
            "receipts": receipt_counts.get(topic, 0),
        }
        total_nodes += len(nodes)
    inv["_totals"] = {
        "topics": len(inv),
        "nodes": total_nodes,
        "receipts": sum(receipt_counts.values()),
    }
    sys.stdout.write(json.dumps(inv, ensure_ascii=False, indent=1, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
