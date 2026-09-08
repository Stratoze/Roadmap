# AGENT.md — Operating Contract for AI Sessions in This Vault

Active phase: **Phase 1** (`./.opencode/plan/phase-1-agent-and-rituals.md`).
Phase 2 (`./.opencode/plan/phase-2-skill-builder.md`) is reference-only until
Phase-1 verification passes. This file is the authority on conflict for rituals.

## Operating contract (ask-first, minimal noise)

Ask-first: surface nudges as ONE short message with a question — never act silently
on reminders, reviews, or notes. Daily loop is Q&A in flow: agent asks Target +
Predict at session start, Got + Gap at close; learner answers in their own words.
Scope approval before landing
engram maps; maps-only landings (no pretests/teaching unless asked).
Evidence via `bash scripts/save.sh` / `bash scripts/milestone.sh` (scripts are NOT +x).

## Session-start protocol (every session, before other work)

Run verbatim (repo root):
`[ -n "$ENGRAM_RUNNER" ] || { echo 'ENGRAM_RUNNER unset — see _system/engram/README.md'; exit 1; }`
`$ENGRAM_RUNNER session-start`
`$ENGRAM_RUNNER due --cap 12`
`test -f "Daily/$(date +%F).md" && echo "note: exists" || echo "note: missing"`
Quote source: `grep -h -A3 -E "^## (One-liner|Sticky)" Daily/*.md | tail -20`
If dues need attention OR note missing: ONE chat reply (chat only — no Telegram, no hooks) —
`Reviews due: N (topics: …) | unencoded: M. Today's note: missing/exists.`
+ one direct quote (file + date) + one question offering action.
Else silence. Never repeat after a same-day decline. Never auto-create/auto-start.
Fallback if runner errors (inline, runnable, read-only — retired = node `retired`
dict present with `restored` None, NEVER `state == 'retired'`):
`python3 -c "import json,glob,os; [print(f\"{f.split('/')[-1]}:{k}\") for f in glob.glob(os.environ['ENGRAM_HOME']+'/graphs/*.json') for k,n in json.load(open(f))['nodes'].items() if isinstance(n.get('retired'),dict) and n['retired'].get('restored') is None]"`
Then stop and report the runner failure. Do not hand-compute dues.

## Session-end protocol (daily Q&A in flow; dailies are the learner's)

Target + Predict are asked at session start, Got + Gap at close — as part of the
day's procedure, never out of nowhere. Learner answers in their own words; agent
formats only (links, indent, template shape) and pastes quotes verbatim, marked.
If Got is missing, vague, or faulty (no mechanism, no numbers), the agent says so
and asks once more — then drops it till tomorrow. Gap is the learner's own
words — NEVER pre-fill it. Agent session activity goes to `Changelog/YYYY-MM.md`
(monthly, append-only), never into Daily files.
Template: `_system/Daily Template.md`.

## Learning prefs (see `_system/How to Learn.md` — link, don't duplicate)

## Improvement notes (mined 2026-09-07 from Landmine Log + recent Gaps)

- Predict the HARD STEP + failure mode, not the load ("reasonable load" predicts nothing).
- No empty Got/Gap — agent asks until answered or explicitly deferred; blank = session failed to close.
- Blank-page re-solves (blank-page rule): claim mastery only from memory, not from notes.
- Verify before claiming: 08-27 slips (12.4→12.60, `(x,-y)` rotation sign) were caught
  by verification, not by feel. Recompute, don't nod.
- Day-tasks-first (anti-creep); estimate the DAY before the plan.
- reconstruct-before-using: rebuild from memory before reaching for aids or notes.
- When a landmine fires, promote it: `[VERIFIED — date]` into the owning file.
- Radians in code, always. Interface before implementation. Telemetry out of hot paths.

## Toolchain (re-verify before toolchain-dependent work)

Re-verify with: `bash scripts/versions.sh` (covers git/python3/arm-none-eabi-gcc/gcc/
cmake/make/openocd/kicad-cli) AND `clangd --version; julia --version; nvim --version;
code --list-extensions | grep -i -e vim -e clangd -e ruff -e julia` — record drift
from the facts below (full rule: Phase-1 plan §2 item 4,
`./.opencode/plan/phase-1-agent-and-rituals.md`).
Facts (2026-09-07): Apple clang/clangd 21 · cmake 4.4.3 · python 3.14.7 ·
julia 1.12.7 · nvim 0.12.5. VSCode Vim (`jj`→Esc, space leader) + clangd + Ruff + Julia
(`~/Library/Application Support/Code/User/settings.json`).
Engram runner: `$ENGRAM_RUNNER` (see `_system/engram/README.md`) — never hand-compute scheduling.
Health: `python3 scripts/diagnose.py` (known-baseline in Phase-1 plan §0; EXEMPT block
at the top of the script is authoritative for carried failures).

## Hard Rules (authoritative Forbidden list; interim authority = this section)

- PLAN-marked files implement ONLY on explicit user `approve`.
- Never auto-create notes/reviews; never invent activity; never pre-fill Gap.
- Maps-only engram landings (no pretests/teaching unless asked); scope approval first.
- NEVER AI-generated video (chat directly instead).
- (Phase-2 forward pointers, NOT enforced in Phase 1 and not yet built — absence is
  expected, do not "fix" by creating: video-pair-per-topic rule, GOAL.md-single-source
  (`Mechatronics/GOAL.md`), skill registry (`Mechatronics/skills/registry.md`),
  machine-gated tags.)
- Evidence via `bash scripts/save.sh` / `bash scripts/milestone.sh`; status lives ONLY
  in the ROADMAP table — never duplicate ✅.
