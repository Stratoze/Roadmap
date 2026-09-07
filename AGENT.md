# AGENT.md — Operating Contract for AI Sessions in This Vault

Active phase: **Phase 1** (`./.opencode/plan/phase-1-agent-and-rituals.md`).
Phase 2 file is reference-only until Phase-1 verification passes.
Plans implement ONLY on explicit user `approve`. This file is the authority on conflict.

## Session-start protocol (every session, before other work)

Run verbatim (repo root):
`python3 ~/engram/scripts/engram.py session-start`
`python3 ~/engram/scripts/engram.py due --cap 12`
`test -f "Daily/$(date +%F).md" && echo "note: exists" || echo "note: missing"`
Quote source: `grep -h -A3 -E "^## (One-liner|Sticky)" Daily/*.md | tail -20`
If dues need attention OR note missing: ONE chat reply —
`Reviews due: N (topics: …) | unencoded: M. Today's note: missing/exists.`
+ one direct quote (file + date) + one question offering action.
Else silence. Never repeat after a same-day decline. Never auto-create/auto-start.
(Fallback if runner errors: inline JSON snippet in Phase-1 §3; then stop and report.)

## Session-end protocol (agent drafts, user quotes)

Draft Predict / Got / One-liner from session evidence into today's note.
Gap is left as an explicit question — NEVER pre-fill it.
User quotes pasted verbatim, marked as quotes. Template: `_system/Daily Template.md`.

## Learning prefs (see `_system/How to Learn.md` — link, don't duplicate)

Loop: Predict → Attempt → Compare → Explain gap → Integrate → Maintain.
JIT-first (course-finishing is progress theater); gap-check chunk sizing;
AI Use Zones Green/Yellow/Red (scaffold, never solve — Yellow zone);
Anti-Bloat Rule (default deletion).

## Improvement notes (mined 2026-09-07 from Landmine Log + recent Gaps)

- Predict the HARD STEP + failure mode, not the load ("reasonable load" predicts nothing).
- No empty Got/Gap — session-end draft fills them; blank = session failed to close.
- Verify before claiming: 08-27 slips (12.4→12.60, `(x,-y)` rotation sign) were caught
  by verification, not by feel. Recompute, don't nod.
- Day-tasks-first (anti-creep); estimate the DAY before the plan.
- Radians in code, always. Interface before implementation. Telemetry out of hot paths.

## Toolchain (re-verify per §2 item 4 before toolchain-dependent work)

Apple clang/clangd 21 · cmake 4.4.3 · python 3.14.7 · julia 1.12.7 · nvim 0.12.5.
VSCode Vim (`jj`→Esc, space leader) + clangd + Ruff + Julia
(`~/Library/Application Support/Code/User/settings.json`).
Engram runner: `python3 ~/engram/scripts/engram.py` — never hand-compute scheduling.
`scripts/*.sh` are NOT +x: run as `bash scripts/<name>.sh`.

## Hard Rules (authoritative Forbidden list; interim authority = this section)

- Never auto-create notes/reviews; never invent activity; never pre-fill Gap.
- Maps-only engram landings (no pretests/teaching unless asked); scope approval first.
- NEVER AI-generated video (chat directly instead).
- (Phase-2 forward pointers, NOT enforced in Phase 1: video-pair-per-topic rule,
  GOAL.md-single-source, skill registry, machine-gated tags.)
- Evidence via `bash scripts/save.sh` / `bash scripts/milestone.sh`; status lives ONLY
  in the ROADMAP table — never duplicate ✅.
