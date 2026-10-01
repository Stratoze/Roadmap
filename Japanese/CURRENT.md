# Japanese — Current Session Handoff

**Updated:** 2026-09-29
**Status:** loop inverted 2026-09-29 — learn → test → record. No session run
under the new loop yet; the Japanese floor starts at L0.

This is the single mutable handoff for the next Japanese session. Read it
before choosing a branch, and read `_system/learning/loop.md` for the loop, the
ladder, and the rules. Curriculum files own concept state; this file owns the
**next action** and current session context. Rewrite this file at the end of
every Japanese session so the next agent never has to infer what to do.

## Start here next time

1. Invoke the `japanese` skill.
2. **Schedule a brief, do not teach.** Hand over keywords, questions to answer
   yourself, one offline task, and the source locator — then stop and let the
   learner study.
3. When they return: test at the Japanese floor, one question per message,
   staying inside the known set plus today's one keyword. No i+1 from you.
4. Record with `python3 scripts/progress.py probe ...` per probe and one
   `... session ...` line; read the floor with `python3 scripts/progress.py show`
   rather than inferring it.
5. Active grammar path: `jp-yokubi-00` → `jp-yokubi-01` →
   `jp-yokubi-02` → `jp-yokubi-03`. Kana are assumed known; the grammar
   sequence starts from sentence anatomy.
6. Use the L1 ramp: Japanese terms/examples with a concise English scaffold;
   move toward Japanese-first as the learner progresses.

## Grammar frontier

- Next concept: `jp-yokubi-00` (Yokubi Lesson 0, sentence anatomy). It is
  `seen` (introduced 2026-09-27 under the retired teach-first loop, one
  practised attempt); under the new loop the next step is to *test* it, not
  re-teach it.
- Source locator: <https://yoku.bi/Section1/Part1/Lesson0.html>, reached
  through [[Japanese/SOURCES|the source map]].
- Verify the locator resolves and the spine still matches before briefing.
  Read the lesson from `_private/private-jp/sources/yokubi/src/...`, at the
  commit pinned in [[Japanese/SOURCES|the source map]] — not from yoku.bi,
  whose HTML is neither pinned nor the same artifact. `_private/` is
  gitignored, so the checkout is per-machine and can be missing; both sources
  live in the private repository, so one clone restores them:
  `git clone https://github.com/Stratoze/private-jp _private/private-jp`
  then `git -C _private/private-jp submodule update --init`.
  `build_japanese_curriculum.py` is **read-only** — it prints
  `verified N Yokubi concept rows` and writes nothing, so run it freely
  mid-session. Only `build_japanese_source_map.py` regenerates and writes
  `Japanese/source-map.json`; it is not a briefing step:

  ```bash
  python3 scripts/build_japanese_curriculum.py
  ```

## Current state

- **Progress:** no sessions recorded under the new loop yet. Japanese floor = 0.
  Ledgers: `Japanese/probes.jsonl`, `Japanese/progress.jsonl` (append-only).
- Active grammar concepts: `jp-yokubi-00` is `seen`; `jp-yokubi-01` onward still
  `unknown`; no Japanese due reviews yet.
- **Anki:** read the known-set with `python3 scripts/anki_read.py summary`
  (works with Anki closed). Escalate to `python3 scripts/anki_bridge.py iplusone`
  for true due counts or a synced collection. Live state 2026-09-29: lane
  `patch`, Kaishi 1.5k 1501 cards / 1000 stuck / 414 mature, and **Lapis empty
  (0 cards)** — so Lapis-based vocabulary routing has nothing to draw from yet.
  The learner mines new words; the tutor never adds a card.
- Reading gate: **0 / 30 actual novel-reading sessions**. Derive the number,
  never hand-count it, with `python3 scripts/review.py usage japanese-reading`.
- Reading mode: English explanation first for sessions 1–30; from session 31
  the learner attempts Japanese first, then English correction. Sentence-analysis
  fallback records `practised` and never counts toward the gate.
- Output: fresh; no backlog to review and no prior output to draw on.
- Immersion: optional input/logging; no quota.

## Next action

Brief and then test `jp-yokubi-00` — sentence anatomy, word order — at floor
L0, using only the learner's known vocabulary. The exercise that was open when
the round closed: put these seven words into one sentence, verb last —
`が の ない 全然 勉強 アンキ 最近`. Note that `全然` appears in the live stuck
set, so it is consolidation material here rather than new input. Then continue
to `jp-yokubi-01` by briefing, not teaching. The earlier topic-ordering exercise
was withdrawn as unsound: it changed two variables at once and pulled the
は/が distinction forward from lesson 3.

```text
brief (keywords, questions, one task, source) → learner studies
→ converse at the floor, one question per message
→ append probes + one session line to the ledgers
→ rewrite this file with the next action
```

## Evidence and archive

- Active usage events: curriculum `## Usage events` tables; progress in the
  append-only ledgers under `Japanese/`.
- Last Japanese evidence: `jp-yokubi-00` introduced and practised 2026-09-27
  (receipt `_private/learning/receipts/2026-09-27-jp-yokubi-00.md`), under the
  retired teach-first loop. No new-loop evidence yet.
- Pre-reset evidence: [[_system/learning/archive/japanese-progress-reset-2026-09-26|archived reset record]].
- Raw learner work: `_private/` only.

## Source notes and blockers

- No sourcing blocker is open. `Japanese/source-map.json` was regenerated from
  the verified private checkout; it carries the current verification block and
  IMABI licence note.

## Close contract

Before ending a Japanese session, update:

- `Updated` date;
- next action and branch (`## Next action`);
- grammar frontier (`## Grammar frontier`);
- the floor and coverage, derived from `progress.py` (never hand-computed);
- reading session count, re-derived from `review.py usage`;
- last evidence link (`## Evidence and archive`);
- any source blocker or unresolved question
  (`## Source notes and blockers`).

Do not leave this file describing a session that has already happened.
