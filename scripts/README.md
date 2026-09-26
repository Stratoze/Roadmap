# scripts

## The loop (used every session)
- `review.py due | frontier | schedule <topic> <id> [rung] | next <topic> <id> hit|hard|miss | selftest` — transparent spaced-review scheduler (ladder 1, 3, 7, 16, 35, 90 days). Rows are created only by the `study` skill; this script never upserts. Topic names are the `curriculum/<domain>-<slug>.md` stem (e.g. `math-odes`).
- `review.py due` and `review.py frontier` answer two different questions and must not be merged. `due` answers "is my evidence for this concept stale?" and ignores prerequisites entirely — a learner may learn out of order, and withholding a concept they demonstrably learned defeats spaced review. `frontier` answers "what can I usefully teach next?" and reports only the roots of the unlearned forest: unlearned concepts whose own prerequisites are already learned, plus a count of what is blocked behind them. Ordering is otherwise owned by the `technical` and `map` skills.
- `review.py usage <topic>` — read-only derived usage freshness; usage events never change review state.
- `review.py usage <topic> <id> <introduced|practised|produced|mined|reading_session> <evidence-path> [public-note]` — append an idempotent usage event; the evidence path must exist. `reading_session` counts only an actual novel-reading session; fallback analysis uses `practised` on its separate concept.
- `diagnose.py` — vault link health (broken links + orphan notes). Exit 0 = clean. The `EXEMPT` block at the top is authoritative for carried failures. Ignores code fences; `_templates/`, `Daily/`, `Changelog/`, `_private/` never count as orphans.
- `question_signatures.py signature "<prompt>" --values "<values>" --context "<context>"` / `check ... --record _system/learning/lessons` — exact prompt and test-variant normalization/non-reuse check across the whole lesson corpus.
- `anki_bridge.py status|due` — optional local AnkiConnect read-only status/due counts. `propose` writes nothing; `add-approved` requires explicit deck/model/field mapping plus `--approved-by` and an approval-evidence file under `_private/**/approval/`.
- `anki_bridge.py iplusone` — read-only. Decides which lane the next Japanese conversation should use: `stretch` (nothing pending, so a new word is the i+1 move), `patch` (unlearned cards pending, so new words are blocked — take a known word the learner keeps failing), or `hold`. Counts come from AnkiConnect's own search operators, never from `cardsInfo.due` arithmetic: for review cards `due` is a raw day offset, not days-from-today, and computing it locally invents a due date. A *stuck* word is `reps>=10` and `interval<7d` (both configurable with `--reps-min` / `--interval-max`): known enough times that failing is meaningful, but not consolidated. Never writes and never reschedules.
- `session_state.py today|init|start <id>|done <id>|pause <id>` — daily checklist and explicit session state transitions.
- `build_japanese_source_map.py` / `build_japanese_curriculum.py` — generate/verify the public Japanese source map and Yokubi concept table; the curriculum checker refuses destructive rewrites.
- `python3 -m unittest discover -s scripts/tests -p "test_*.py"` — executable tests for review usage, question signatures, source schema, and technical-session records.
- `validate_learning.py` — read-only checks for canonical curriculum resource headings, stale references, and protected paths; pass `--base <commit>` to include committed changes in the protected-path audit.

## Evidence (milestone workflow)
- `save.sh "scope: what changed"` — `git add -A` + commit. Refuses if `_private/` exists and isn't gitignored.
- `milestone.sh <tag> "<what proves it>" --gate mvm|full --evidence <assessor-record>` — after committing the evidence and completed ROADMAP checkbox, verify the assessor gate and create the signed tag. Full Pass tags separately.

## Diagnostics (as needed)
- `versions.sh` — toolchain snapshot; run before toolchain-dependent work.
- `diagnose.py` — link/orphan check; run after structural changes.

## Running the suite, and the sandbox
- The suite is `python3 -m unittest discover -s scripts/tests -p "test_*.py"`.
- **Under the default `workspace-write` sandbox it cannot pass, and the failures
  are not regressions.** `tempfile.mkdtemp()` creates `0700` directories that the
  sandbox then refuses to write into, so every test using
  `tempfile.TemporaryDirectory()` raises `PermissionError` before it exercises
  any logic. `test_technical_session` additionally spawns a child process and
  fails the same way (`STATUS_DLL_INIT_FAILED`).
- Judge these by exception type. A `PermissionError` here means "not run", never
  "broken". To confirm a real failure, re-run under `danger-full-access`: 138
  passed / 2 skipped, and the same 7 subprocess tests fail there too, so they
  are environmental in both modes.
- **Escalation default:** omit the sandbox-permission parameter and let the
  operation run in the session's current mode. Escalate only as a fallback when
  the mode genuinely cannot do the job. Approval is auto-reviewed by another
  model, so a justified fallback is cheap and a refused one costs only an
  unvalidated claim. Never work around a denial by retrying a different way.

## Measuring cold-start cost
Cold-start — how many steps a fresh agent needs to answer "what's next?" — is a
maintained metric (learner's own, 2026-09-26), not a one-off. After changing
anything a fresh agent must read to branch, re-measure it.

Method: spawn a fresh agent, give it **only** the prompt `what's next?`, let it
finish, then ask that same agent how many steps it took and what it had to
infer. Score the step count *and* whether the answer was aligned and current. If
it is stale, find which document lied.

**Spawn it as a team member, not a background subagent.** `send_message` reaches
team members only; a finished background subagent is unresumable, so the
self-audit half silently becomes unobtainable and you get alignment but no
number.

**Define the unit before quoting a trend.** The original baselines ("12 steps",
"6 steps") never said whether a step was a tool call or a round, so a later
6-calls/3-rounds reading is not strictly comparable. Record all three: tool
calls, rounds, and files read. Current measurement, 2026-09-26 after `b7ebf21`:
**6 calls, 3 rounds, 3 files read** (the `session_state.py` output plus the two
`CURRENT.md` files), against a pre-`554e611` baseline of 12. Alignment confirmed:
the probe verified `Mechatronics/CURRENT.md`'s claim that `review.py frontier`
reports c2 and c9 as ready, rather than trusting it.

Windows git-bash notes: invoke shell scripts with `bash scripts/*.sh` (not `+x`);
Python output needs `PYTHONIOENCODING=utf-8`. Repo is LF (`* text=auto eol=lf`).
