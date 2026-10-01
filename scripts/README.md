# scripts

## The loop (used every session)
- `review.py due | frontier | schedule <topic> <id> [rung] | next <topic> <id> hit|hard|miss | selftest` — transparent spaced-review scheduler (ladder 1, 3, 7, 16, 35, 90 days). Rows are created only by the `study` skill; this script never upserts. Topic names are the `curriculum/<domain>-<slug>.md` stem (e.g. `math-odes`).
- `review.py due` and `review.py frontier` answer two different questions and must not be merged. `due` answers "is my evidence for this concept stale?" and ignores prerequisites entirely — a learner may learn out of order, and withholding a concept they demonstrably learned defeats spaced review. `frontier` answers "what can I usefully teach next?" and reports only the roots of the unlearned forest: unlearned concepts whose own prerequisites are already learned, plus a count of what is blocked behind them. Ordering is otherwise owned by the `technical` and `map` skills.
- `review.py usage <topic>` — read-only derived usage freshness; usage events never change review state.
- `review.py usage <topic> <id> <introduced|practised|produced|mined|reading_session> <evidence-path> [public-note]` — append an idempotent usage event; the evidence path must exist. `reading_session` counts only an actual novel-reading session; fallback analysis uses `practised` on its separate concept.
- `diagnose.py` — vault link health (broken links + orphan notes). Exit 0 = clean. The `EXEMPT` block at the top of the script carries any knowingly-accepted failures and is currently empty. Ignores code fences; `_templates/`, `Daily/`, `Changelog/`, `_private/` never count as orphans.
- `question_signatures.py signature "<prompt>" --values "<values>" --context "<context>"` / `check ... --record _system/learning/lessons` — exact prompt and test-variant normalization/non-reuse check across the whole lesson corpus.
- `anki_bridge.py status|due|due-offline` — AnkiConnect read path. `due` falls back to a direct collection read when AnkiConnect is unreachable (usually: the server is not bound). `due-offline` forces the direct read. `propose` writes nothing; `add-approved` requires explicit deck/model/field mapping plus `--approved-by` and an approval-evidence file under `_private/**/approval/`.
- `anki_bridge.py iplusone` — read-only. Reports which lane the known-set is in: `stretch` (nothing unlearned pending), `patch` (unlearned pending, so consolidation rather than new input), or `hold`. Under the 2026-09-29 loop this informs **topic choice**, not a hard gate on introducing a word — new vocabulary now enters through the learner's own mining, so the tutor reads this to pick topics that surface vocabulary they are about to need. Counts come from AnkiConnect's own search operators, never from `cardsInfo.due` arithmetic: for review cards `due` is a raw day offset, not days-from-today, and computing it locally invents a due date. A *stuck* word is `reps>=10` and `interval<7d`. Never writes and never reschedules.
- `anki_read.py summary|decks` — read-only **direct SQLite** reader for the Anki collection; the default way to see the known-set, deck counts, and stuck words, and it works while Anki is closed. Snapshot-copies before opening, because a WAL-mode database cannot be opened read-only in place (`database is locked`) and `tempfile`'s 0700 dirs are blocked by the workspace sandbox. Two schema facts it encodes: `decks.name` and `notetypes.name` are `COLLATE unicase`, which plain SQLite cannot resolve, so all name lookups happen in Python; and it **fails loudly** (`SchemaMismatch`) on any layout other than the verified upstream Anki 26.9b3 shape rather than guessing. Reports collection mtime because a direct read cannot see AnkiWeb sync — escalate to `anki_bridge.py` when a synced collection is needed. Never writes. Scratch is `.anki-read-cache/` (gitignored); override with `ANKI_READ_SCRATCH`.
- `progress.py probe|session|show|dashboard` — owns progress state for the learn → test → record loop (`_system/learning/loop.md`), the way `review.py` owns review state. `probe <domain> <concept> <level> <pass|miss>` appends one probe line; `session <domain> --floor-start/--floor-end/--probes/--pass/--miss/--peak-level` appends one session line; `show` prints a text dashboard; `dashboard` writes a self-contained `progress.html`. Ledgers are append-only per domain: `<domain>/probes.jsonl`, `<domain>/progress.jsonl`. Scoring: advance the floor on 3 consecutive passes at the floor **and** a recent pass rate ≥ 0.85; drop on 2 consecutive misses; report a Wilson lower bound as a *confidence* readout (not an advance gate — a small-n gate would pin the floor at L0 for weeks) and an OLS velocity slope over the last 10 sessions. The page reads the JSONL directly, so **no script run is needed to view progress**. Never hand-compute a floor or score.
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
calls, rounds, and files read. A measurement missing any of the three is not
comparable to one that has all three, and should be marked incomplete rather
than quoted alongside.

Measurements, 2026-09-26:

- "what's next?", after `b7ebf21` — **6 calls, 3 rounds, 3 files read** (the
  `session_state.py` output plus the two `CURRENT.md` files), against a
  pre-`554e611` baseline of 12. Alignment confirmed: the probe verified
  `Mechatronics/CURRENT.md`'s claim that `review.py frontier` reports c2 and c9
  as ready, rather than trusting it.
- "Japanese session, plan the opening", after `2cdc82e` — **9 calls, 4 blocks,
  3 reasoning turns, 5 files read** (2 `CURRENT.md`, the japanese skill, the
  curriculum table, `How to Learn`, `learner.md`, `learning/README`). Alignment confirmed, and the probe earned its keep twice:
  it reported the `stuck_samples` as `����` (a real encoding defect in
  `anki_bridge.py`, now fixed), and it found that the i+1 lane was reachable
  *only* by reading the japanese skill. An agent that had not opened that file
  would have planned around due counts alone and opened with a new word on a
  `patch` lane. The lane is now also printed by `session_state.py today`, so the
  invariant is visible without loading a skill.

**Test the wiring, not just the code.** Both defects above were invisible to
the unit tests, which passed throughout. A command can work perfectly and still
never be reached, or be reached and produce unusable output.


Windows git-bash notes: invoke shell scripts with `bash scripts/*.sh` (not `+x`);
Python output needs `PYTHONIOENCODING=utf-8`. Repo is LF (`* text=auto eol=lf`).
