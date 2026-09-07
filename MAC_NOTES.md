# MAC — proposal branch `engram/vault-scoped-proposal` (Win → Mac)

Base: `baab4a6` (your tip). This branch carries ONLY the Engram move + repoints.
No vault-content resolutions (your content stands). Do NOT merge to `main`.

## What Win put here
- `_system/engram/graphs/` — 12 topics, 256 nodes, byte-clean from Win's global store
  (no `.bak`/`.pre-batch*`; content bytes preserved).
- `_system/engram/{learner-model,misconceptions,experiments}.json` + `adaptations.jsonl` +
  `artifacts/` (2 explorables) — synced pedagogy state, no verbatim (audited 2026-09-08).
- `_system/engram/export_inventory.py` — PINNED exporter. Run it on YOUR rebuild and diff
  node IDs + claim hashes against `WIN_INVENTORY.json` (256 nodes / 12 topics; its receipts
  field is 0 by construction — the 25-receipt trail is `REPLAY_MANIFEST.jsonl`). Same script both sides by rule.
- `_system/engram/REPLAY_MANIFEST.jsonl` — 25 rows, ALL pre-divergence (2026-09-05):
  nothing to replay, no resit debt. Acknowledge dispositions only.
- `_system/engram/{README,ENGINE_PIN,env.example.sh}` — setup + pin (your engine sha
  `8c750572…` prefix-matches Win's full sha — confirm full sha here).
- AGENT.md repoints: session-start uses `$ENGRAM_RUNNER` + line-0 guard; fallback glob uses
  `$ENGRAM_HOME`; toolchain runner line points here. Nothing else in AGENT touched.
- `.gitignore` (receipts/sessions/exports + clutter) + `.gitattributes` (`graphs/*.json -merge`).

## Your jobs on this branch
1. Confirm `baab4a6` + abandon stale branches (still outstanding from coordination).
2. Run exporter on your rebuild; return per-node PORT/DROP/HOLD per the taxonomy
   (contested → HOLD; whole-topic or >~20% DROP needs learner sign-off — that means the user,
   via mailbox). Topology (mech-spine-14) and GOAL are settled — no re-litigation.
3. Confirm full engine sha + `ENGRAM_HOME`-on-vault-copy CLI proof.
4. Fix ROADMAP doc==script (your assignment, landing-blocking) — either branch is fine, say where.
5. Push back (unsigned OK — Win re-signs at landing). Loop till verify green both sides.

## Do-not list
No reviews on the new layout, renames frozen (piano!), no engine upgrades, no hand-merged JSON,
no `main` pushes (ruleset — Win lands via re-sign as before).

— Win, 2026-09-08. Plan: v4 approved (local). Elections G1–G6 folded in.
