# Engram store (vault-scoped) — READ THIS BEFORE REVIEWING HERE

This directory is the Engram FSRS store, moved in-repo so Win + Mac sync via git.
Engine stays OUTSIDE the repo (version-pinned plugin / standalone script — see ENGINE_PIN).

## Layout
- `graphs/<topic>.json` — claims/probes/rubrics + per-node FSRS state. SYNCED. Never hand-merge
  (`graphs/*.json -merge` in `.gitattributes` forces conflicts; only resolution is abort + replay).
- `learner-model.json`, `misconceptions.json`, `experiments.json`, `adaptations.jsonl` — SYNCED
  pedagogy state (no verbatim learner text; interests/commitment-cue are public-by-commit — accepted).
- `artifacts/` — tutor-built explorables referenced by nodes. SYNCED.
- `export_inventory.py` — PINNED exporter (both sides run THIS script; canonical claim hash spec
  in its header). Never one-hash-per-engine.
- `WIN_INVENTORY.json` — Win's P0 node inventory (256 nodes / 12 topics; receipts=0 here by
  construction — run the exporter WITH a receipts dir to count them; the 25-receipt trail lives
  in `REPLAY_MANIFEST.jsonl`). Mac diffs node IDs + claim hashes against its rebuild here.
- `REPLAY_MANIFEST.jsonl` — grade-only audit trail (no `production` text, ever). All 25 Win rows are
  PRE-divergence (2026-09-05): nothing to replay, no resit debt — Mac dispositions acknowledge only.
- `receipts/`, `sessions.jsonl`, `exports/` — LOCAL-ONLY, gitignored (verbatim `production` text).
  Never committed to this public repo.

## Setup (per machine, once)
1. Copy `env.example.sh` values into your shell rc (`~/.zshrc` Mac, `~/.bashrc` Win-git-bash):
   `ENGRAM_RUNNER` (how to invoke YOUR engine) + `ENGRAM_HOME` (this directory's absolute path).
2. Verify: `$ENGRAM_RUNNER doctor` reports this directory as home and `ok:true`.
3. Never review with a dirty store; `git fetch` before AND before committing; never `--force` push
   store paths; never `pull --rebase` them (export manifest → `reset --hard @{u}` → re-apply).

## Sync protocol
Pull-before-review, commit per session, push promptly. History kept, no squash.
Topic dispositions: PORT / DROP (coded reason) / HOLD (default when contested).
DROP-quota: whole topic or >~20% of nodes needs learner sign-off. PORT = interval reset.

## Line endings (load-bearing)
Repo is LF (`* text=auto eol=lf`). Hash gates compare COMMITTED/STAGED blobs
(`git show HEAD:<path>`, `git rev-parse :<path>`) — never working-tree files.
Reason: the engine opens JSON in text mode, so Windows reviews rewrite CRLF into the
working tree (content-identical, every-line-diff). After any Windows review, normalize
before committing: `python3 -c` strip `\r` over touched store files (see v4 plan), then
`git add`. macOS text-mode writes LF natively — no step needed there.
