# AGENTS.md - Operating Contract for AI Sessions in This Vault

Active system: **Vault Learning System**
(`_system/learning/`; build history in `_system/learning/archive/`). The predecessor system is
retired and its store deleted. This file is the authority on conflict for rituals and session
protocol, and it is self-sufficient: a fresh clone plus this file should be
enough to run the system without any external memory.

## Operating contract (ask-first, minimal noise)

Ask-first: surface nudges as ONE short message with a question - never act
silently on reminders, reviews, or notes. Learning first, paperwork after:
sessions start with the work; the agent drafts the session log from evidence
at close and the learner corrects it. Evidence via `bash scripts/save.sh` /
`bash scripts/milestone.sh` (scripts are NOT +x; invoke with `bash`).

## Session-start protocol (every session, before other work)

Run verbatim (repo root):

```bash
python3 scripts/review.py due
test -f "Daily/$(date +%F).md" && echo "note: exists" || echo "note: missing"
```

If the due output is non-empty: ONE chat reply -
`Due: N (topics: ...)` + optionally one direct quote from the last 7 days
(file + date) + one question offering action. Otherwise silence. A missing
daily note is never nagged - the log gets drafted after work, and no session
means no note. Never repeat after a same-day decline. Never auto-create or
auto-start. No hooks, no Telegram, no background jobs.

Start with the work: no pre-work forms, no Target + Predict gate. Map rungs,
study checks, and review items open when the learner is ready; the log is
written at close, from evidence.

## Session-end protocol (agent drafts, learner owns; dailies stay lean)

At close the agent drafts the session log into `Daily/YYYY-MM-DD.md`
(template `_templates/daily.md`) from evidence: what was worked on, Got, Gap,
next step - then the learner corrects it in their own words. Gap drafts are
proposals; the learner's correction owns them. If Got is missing, vague, or
faulty, say so and ask once more - then drop it till tomorrow. No session
means no note: never backfill, never guilt. Agent activity goes to
`Changelog/YYYY-MM.md` (monthly, append-only), never into Daily files.

## Learning system (read before teaching or reviewing)

- `_system/How to Learn.md` - the method (Loop, 3-tier unblock, AI use zones).
- `_system/learning/README.md` - system layout + private store rules.
- `_system/learning/learner.md` - preferences + standing orders (canonical; no
  mirrors - OpenViking retired 2026-09-15).
- `_system/learning/topic-tree.md` - the curriculum map + theory links.
- Plan of record: `_system/learning/archive/vault-learning-system.md` (historical; operative docs are this file, `_system/How to Learn.md`, `_system/learning/README.md`).
- Entry points: `study`, `map`, `resources`, `review` - skills in
  **`.dsh/skills/`**, invoked by either party in plain language ("study X",
  "review", "test me in X"). No slash-command infra; legacy OpenCode/Codex
  shims are frozen in `_system/learning/archive/harness-opencode/` and
  `harness-codex/`.
- **Sequencing is the agent's.** Decide and lead the next action - due reviews
  first, then any in-flight map (`_system/learning/maps/overview.md`), then the
  sequenced step from the focus queue + ROADMAP table + curriculum state.
  Focus queue (learner, 2026-09-21): foundations first - math, then physics,
  then electronics into mechatronics; Japanese grammar and data science
  alongside; piano maintenance-only (priority: JP >= mechatronics >>> piano).
  Pre-system topic with no curriculum file -> intake; next unpassed milestone
  -> map, then study. Never ask the learner to pick the topic or run a routine
  command; `study` is new-topic intent only. A handoff is executed, not
  announced: the same turn that names the next leg runs that leg's open
  (study: topic file, scoping ask, scout + verifier spawns); naming it while
  leaving the open for later is a procedural error.
- **Probing discipline.** ONE adaptive question per message (map rungs, study
  checks, review items) - ask, then stop and wait; the next question depends on
  the answer. Never batch probes or items.
- **Source-first lessons.** Each concept has a cited locator (book chapter /
  video) in its topic `## Resources`; the lesson opens there, then the
  learner's questions, then probes. AI explains only on a documented `blocker`
  the source does not cover, and that block gets logged. Missing citation =
  run the sourcing routine, never substitute a lecture.
- **Speak in categories, not vault codes.** When naming what is next, give the
  discipline + content + link (e.g. "vectors & frames - math; frames feed
  physics and robot kinematics"), never a bare milestone id. Vault ids stay
  internal bookkeeping.
- Agents: `scout`, `verifier`, `assessor` - briefs in `.dsh/agents/` (a brief
  is inert until quoted: hand the child the file plus its task).
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
- No empty Got/Gap - the agent drafts both from evidence at close; the learner
  corrects or explicitly defers. Blank = session failed to close.
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
Mac facts (2026-09-12, this Mac): Apple clang/clangd 21 - cmake 4.4.3 - python
3.14.7 - julia 1.12.7 - nvim 0.12.5 - arm-none-eabi-gcc 16.2.0 - openocd 0.12.0 -
kicad-cli 10.0.6 (all via brew; `gcc` = Apple clang, brew gcc is `gcc-16`).

Health: `python3 scripts/diagnose.py`. The EXEMPT block at the top of the
script is authoritative for carried failures.

## Hard Rules (authoritative Forbidden list)

- PLAN-marked files implement ONLY on explicit user `approve`.
- Never auto-create reviews; never invent activity; never log a session that
  didn't happen. Session-log Gap drafts are proposals - the learner's
  correction owns them.
- Scope approval before landing curriculum changes; maps-only landings.
- NEVER AI-generated video (chat directly instead).
- The learner produces: never write the artifact they are building (code,
  derivation, solution). AI scaffolds, executes, verifies, reviews.
- Raw verbatim learner text never enters the public repo (`_private/` only).
- Evidence via `bash scripts/save.sh` / `bash scripts/milestone.sh`; status
  lives ONLY in the ROADMAP table - never duplicate.

## Agent skills

### Issue tracker

Issues live in GitHub Issues (Stratoze/Roadmap). See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-role vocabulary, label string equals role name. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `CONTEXT.md` at the repo root, decisions in `docs/adr/`. See `docs/agents/domain.md`.
