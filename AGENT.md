# AGENT.md - Operating Contract for AI Sessions in This Vault

Active system: **Vault Learning System**
(`.opencode/plan/vault-learning-system.md`). The predecessor system is
retired and its store deleted. This file is the authority on conflict for rituals and session
protocol, and it is self-sufficient: a fresh clone plus this file should be
enough to run the system without any external memory.

## Operating contract (ask-first, minimal noise)

Ask-first: surface nudges as ONE short message with a question - never act
silently on reminders, reviews, or notes. Daily loop is Q&A in flow: agent asks
Target + Predict at session start, Got + Gap at close; learner answers in their
own words. Evidence via `bash scripts/save.sh` / `bash scripts/milestone.sh`
(scripts are NOT +x; invoke with `bash`).

## Session-start protocol (every session, before other work)

Run verbatim (repo root):

```bash
python3 scripts/review.py due
test -f "Daily/$(date +%F).md" && echo "note: exists" || echo "note: missing"
```

If the due output is non-empty OR the note is missing: ONE chat reply -
`Due: N (topics: ...) | Today's note: missing/exists.` + optionally one direct
quote from the last 7 days (file + date) + one question offering action.
Otherwise silence. Never repeat after a same-day decline. Never auto-create or
auto-start. No hooks, no Telegram, no background jobs.

## Session-end protocol (daily Q&A in flow; dailies are the learner's)

Target + Predict at session start, Got + Gap at close - as part of the day's
procedure. Learner answers in their own words; the agent formats only and pastes
quotes verbatim, marked. If Got is missing, vague, or faulty, say so and ask
once more - then drop it till tomorrow. Gap is the learner's own words - NEVER
pre-fill it. Agent activity goes to `Changelog/YYYY-MM.md` (monthly,
append-only), never into Daily files. Template: `_system/Daily Template.md`.

## Learning system (read before teaching or reviewing)

- `_system/How to Learn.md` - the method (Loop, 3-tier unblock, AI use zones).
- `_system/learning/README.md` - system layout + private store rules.
- `_system/learning/learner.md` - preferences + standing orders (canonical;
  OpenViking is a mirror only).
- `_system/learning/topic-tree.md` - the curriculum map + theory links.
- Plan of record: `.opencode/plan/vault-learning-system.md`.
- Skills: `study`, `map`, `resources`, `review` (project `.opencode/skills/`).
- Agents: `scout`, `verifier`, `assessor` (project `.opencode/agents/`).
- Reviews: `python3 scripts/review.py due|schedule|next`. Never hand-compute
  scheduling; never re-expose material before a cold recall probe.
- Raw learner text goes to `_private/learning/` only (private companion repo).
  If `_private/.git` is missing, pause verbatim capture, say so, and continue
  with public summaries.

## Review-loop format (learner-pinned: readability over brevity)

Reveals in plain sentences that explain the blindspot - never dense one-liners
or buzzword summaries. After each reveal STOP and invite questions; the next
probe only when the learner moves on (unless a hard reason not to, stated
aloud).

## Improvement notes (mined from Landmine Log + recent Gaps)

- Predict the HARD STEP + failure mode, not the load.
- No empty Got/Gap - the agent asks until answered or explicitly deferred;
  blank = session failed to close.
- Blank-page re-solves: claim mastery only from memory, not from notes.
- Verify before claiming: recompute, don't nod.
- Day-tasks-first (anti-creep); estimate the DAY before the plan.
- Reconstruct-before-using: rebuild from memory before reaching for aids.
- When a landmine fires, promote it: `[VERIFIED - date]` into the owning file.
- Radians in code, always. Interface before implementation. Telemetry out of
  hot paths.

## Toolchain (re-verify before toolchain-dependent work)

Re-verify with: `bash scripts/versions.sh` AND `clangd --version; julia
--version; nvim --version; code --list-extensions | grep -i -e vim -e clangd
-e ruff -e julia` - record drift from the facts below before toolchain work.

Facts (2026-09-07, Mac reference; this machine is Windows git-bash with python
3.13.11): Apple clang/clangd 21 - cmake 4.4.3 - python 3.14.7 - julia 1.12.7 -
nvim 0.12.5.

Health: `python3 scripts/diagnose.py`. The EXEMPT block at the top of the
script is authoritative for carried failures.

## Hard Rules (authoritative Forbidden list)

- PLAN-marked files implement ONLY on explicit user `approve`.
- Never auto-create notes or reviews; never invent activity; never pre-fill Gap.
- Scope approval before landing curriculum changes; maps-only landings.
- NEVER AI-generated video (chat directly instead).
- The learner produces: never write the artifact they are building (code,
  derivation, solution). AI scaffolds, executes, verifies, reviews.
- Raw verbatim learner text never enters the public repo (`_private/` only).
- Evidence via `bash scripts/save.sh` / `bash scripts/milestone.sh`; status
  lives ONLY in the ROADMAP table - never duplicate.
