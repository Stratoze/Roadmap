# Phase 1 — Agent Rituals (AGENT.md + reminders + vault catch-up)

Status: PLAN — do not implement until user approves this file + reviewer sign-off.
ACTIVE ON FIRST BUILD: Phase 1 is active from the first build commit; Phase 2 is
reference-only until Phase-1 §5 passes. AGENT.md §Hard Rules names the active phase
thereafter. On conflict the active phase's file governs.
Owner session protocol: ask-first, minimal noise. Agent drafts; user supplies verbatim
quotes. Agent NEVER pre-fills the Gap section (learner writes the gap).
Reference convention in both plan files: §X.Y means §X item Y (sections are numbered lists).

## 0. Verified starting facts (2026-09-07, re-check at build time — see §2 item 4)

- Repo `/Users/kohaku/Roadmap`, branch `main`, HEAD `c1142a5` ("daily: 2026-08-28").
- Untracked: `Daily/2026-09-05.md` (engram rebuild: 6 topics, 103 nodes) AND `.opencode/`
  (these plan files). Nothing else dirty. (§1 scopes each add separately — `save.sh`
  runs `git add -A` and MUST NOT be used blindly here.)
- Missing dailies: 08-29 → 09-04, 09-06, 09-07 (today). Week-long loop-history gap.
- Tags exist: `m0.1-fullpass`, `m0.2-mvm`, `m0.2-full`. ROADMAP shows 0.1 ✅, 0.2 ✅, 0.3 ⬜ next.
- No `AGENT.md`/`AGENTS.md`. `.opencode/plan/` exists (this file lives in it).
- `scripts/*.sh` are NOT executable (`-rw-r--r--`): invoke EVERYTHING as
  `bash scripts/<name>.sh`. Fix every `./scripts/` invocation in plans + ROADMAP.
- Global `~/.config/opencode/opencode.jsonc` is schema-only: no engram plugin, no hooks.
- Hermes uninstalled. Sep-5 Telegram crons (learn-nudge/note-nudge) are DEAD by decision:
  do not restore; the loop below replaces them. Verify no remnants at build
  (`crontab -l`, launchd, opencode scheduler) and remove or record.
- Engram runner (verified, use it — never hand-compute scheduling):
  `python3 ~/engram/scripts/engram.py` — `due --cap 12` (authoritative dues),
  `session-start` (engine-native ambient: amnesty-first, plan, decay),
  `doctor` (incl. `probe_gaps`). State dir `~/.claude/learning/`; topic maps live in its
  `graphs/` subdir (`graphs/*.json`). 6 topics / 103 nodes.
- Toolchain (verified 2026-09-07): Apple clang/clangd 21, cmake 4.4.3, python 3.14.7,
  julia 1.12.7, nvim 0.12.5, VSCode + Vim/clangd/Ruff/Julia extensions
  (`~/Library/Application Support/Code/User/settings.json`, 82 lines; `jj`→Esc, space leader).
- KNOWN-BASELINE dirt: `python3 scripts/diagnose.py` reports 2 broken
  (`index.md` → `[[Reading/Reading RoadMap]]`, `[[Reading/Reading Progress]]`) + 1 orphan
  (`Mechatronics/milestones/Phase 0/0.2.md`). Treat as known-baseline, not agent failure;
  fix or carry in the `EXEMPT` block (§5).

## 1. Task 1 — Vault catch-up commit (single batch, minimal noise)

- Commit in TWO scoped steps (never bare `save.sh` while `.opencode/` is untracked):
  1. `git add Daily/2026-09-05.md && git commit -m "daily: 2026-09-05 — engram rebuild, 6 topics, 103 nodes"`
  2. `git add .opencode/plan/ && git commit -m "plans: phase-1 rituals + phase-2 skill-builder (awaiting review)"`
- Missing days 08-29→09-04, 09-06→09-07: ONE batched message listing the dates; user replies
  per day `stub` (one-line `Focus: — / One-liner: no session (backfill)`) or `skip`.
  Never invent activity. Never 8 separate interruptions.
- Acceptance: `git status --short` shows only today's intentional file (if any);
  `git log --oneline -5` shows the catch-up commit(s).

## 2. Task 2 — `AGENT.md` at repo root (opencode auto-loads it; budget ~150 lines)

Required sections (link, don't duplicate; pointers must name exact paths):

1. **Operating contract** — ask-first nudge (§3); drafts-vs-quotes (§4); scope approval
   before landing engram maps; maps-only landings (no pretests/teaching unless asked);
   evidence via `bash scripts/save.sh` / `bash scripts/milestone.sh`; active-phase pointer.
2. **Learning prefs** — the Loop (Predict → Attempt → Compare → Explain gap → Integrate →
   Maintain, `_system/How to Learn.md`), JIT-first, gap-check sizing, AI Use Zones
   Green/Yellow/Red, Anti-Bloat Rule.
3. **Improvement notes** — mined at write time from `_system/Landmine Log.md` clusters +
   recent Daily Gaps (reconstruct-before-using, blank-page re-solves, landmine promotion
   `[VERIFIED — date]`, radians discipline, interface-before-implementation).
4. **Toolchain + re-verify rule** — §0 facts PLUS, verbatim:
   `Re-verify with: bash scripts/versions.sh (covers git/python3/arm-none-eabi-gcc/gcc/
   cmake/make/openocd/kicad-cli) AND clangd --version; julia --version; nvim --version;
   code --list-extensions | grep -i -e vim -e clangd -e ruff -e julia — record drift from §0
   before any toolchain-dependent work.`
5. **Session-start protocol** (§3, exact commands included) and **session-end protocol** (§4).
6. **Hard Rules (single authoritative Forbidden list; interim authority until AGENT.md
   lands: THIS §2 item 6)** — never auto-create notes/reviews; never invent activity; never
   pre-fill Gap; maps-only landings; NEVER AI-generated video (chat directly instead);
   PLAN-marked files need explicit user `approve` before implementation.
   (Video-pair-per-topic and GOAL.md-single-source rules are Phase-2 rules, cited here as
   FORWARD POINTERS ONLY — not enforced during Phase 1.)

## 3. Task 3 — Session-start reminder loop (engine-native, ambient, non-repeating)

On every new session in this repo, before other work, run EXACTLY this (repo root):

```bash
python3 ~/engram/scripts/engram.py session-start
python3 ~/engram/scripts/engram.py due --cap 12
test -f "Daily/$(date +%F).md" && echo "note: exists" || echo "note: missing"
```

Semantics: `session-start` is authoritative (amnesty-first, plan verbatim, decay honored —
never recompute, never contradict it). `due --cap 12` gives the capped sitting.
Fallback ONLY if the runner errors (inline, runnable, read-only — retired = node
`retired` dict present with `restored` None, NEVER `state == 'retired'`):

```bash
python3 -c "import json,glob; [print(f\"{f.split('/')[-1]}:{k}\") for f in glob.glob('/Users/kohaku/.claude/learning/graphs/*.json') for k,n in json.load(open(f))['nodes'].items() if isinstance(n.get('retired'),dict) and n['retired'].get('restored') is None]"
```

and report the runner failure. If the fallback is ever needed, stop: do not hand-compute
dues, report and wait.

Quote retrieval (explicit, runnable): `grep -h -A3 -E "^## (One-liner|Sticky)" Daily/*.md | tail -20`
— cite file + date; if nothing in the last 7 days, say so.

Nudge policy (ambient, no nagging):

- If engine output OR note-missing needs attention: send ONE chat reply:
  `Reviews due: N (topics: …) | unencoded: M. Today's note: missing/exists.`
  + one direct quote with source + one question offering action.
- Silence otherwise (engine silent, note exists). Never repeat after a decline in the
  same day. Never auto-create the note, never auto-start reviews.
  Delivery channel is the chat reply (no Telegram, no hooks).

## 4. Task 4 — Session-end daily flow (agent drafts Predict/Got/One-liner; user owns Gap)

1. Agent drafts Predict / Got / One-liner from session evidence into the Daily Template.
2. Gap section is left as an explicit question to the user — agent MUST NOT pre-fill it.
   User supplies verbatim quotes; agent pastes them unedited, marked as quotes.
3. Refresh `_system/Daily Template.md` line 6 to EXACTLY:
   `- **Domain:** mech / piano / reading / japanese / system / software / science / data-science`
   (line-count lock dropped; shape otherwise unchanged).

## 5. Verification (cold-start test, must pass)

1. Dues > 0 + note missing → exactly one nudge message with a real quote + a question.
   Nothing due + note exists → silence. Decline → no repeat same day.
2. `python3 scripts/diagnose.py` output recorded; no NEW failures vs §0 known-baseline.
   Carried items live in a NEW `EXEMPT` block at the top of `scripts/diagnose.py`
   (format: `# EXEMPT <check>: <target> — <reason> — expires <YYYY-MM-DD>`), which the
   Phase-2 gate reads as authoritative.
3. `git status` clean per §1; `AGENT.md` ≤ ~150 lines; every pointer in it resolves
   (broken pointer = fail).

## Non-goals (explicitly Phase 2 — touch none of it here)

Vault restructure beyond the Phase-0 pilot, GOAL.md, skill registry, machine-gated tags,
engram topic changes, video-lens backfill. Reference-only until Phase 2 is active.
