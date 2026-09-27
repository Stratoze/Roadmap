# Japanese — Current Session Handoff

**Updated:** 2026-09-27
**Status:** Round closed 2026-09-27; `jp-yokubi-00` introduced, word-order exercise open.

This is the single mutable handoff for the next Japanese session. Read it
before choosing a branch. Curriculum files own concept state; this file owns
the **next action** and current session context. Rewrite this file at the end
of every Japanese session so the next agent never has to infer what to do.

## Start here next time

1. Invoke the `japanese` skill.
2. **Do not open with a generic due-review pass or a conversation warm-up.**
   The frontier is `jp-yokubi-00` and it is already introduced, so continue it
   rather than re-teaching it. A warm-up is for activating grammar that
   already exists; against an unlearned frontier it only produces a detour.
3. First active grammar path: `jp-yokubi-00` → `jp-yokubi-01` →
   `jp-yokubi-02` → `jp-yokubi-03`. Kana are assumed known; the grammar
   sequence starts from sentence anatomy.
4. Use the L1 ramp: Japanese terms/examples with a concise English scaffold;
   move toward Japanese-first as the learner progresses.

## Grammar frontier

- Next concept: `jp-yokubi-00` (Yokubi Lesson 0, sentence anatomy).
- Source locator: <https://yoku.bi/Section1/Part1/Lesson0.html>, reached
  through [[Japanese/SOURCES|the source map]].
- Verify the locator resolves and the spine still matches before teaching.
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
  `Japanese/source-map.json`; it is not a teaching step:

  ```bash
  python3 scripts/build_japanese_curriculum.py
  ```

## Current state

- Active grammar concepts: `jp-yokubi-00` is `seen` (taught 2026-09-27, one
  practised attempt). `jp-yokubi-01` onward still `unknown`; no Japanese due
  reviews yet.
- Reading gate: **0 / 30 actual novel-reading sessions**. Derive the number,
  never hand-count it, with `python3 scripts/review.py usage japanese-reading`.
- Reading mode: English explanation first for sessions 1–30; from session 31
  the learner attempts Japanese first, then English correction. Sentence-analysis
  fallback records `practised` and never counts toward the gate.
- Output: fresh; no backlog to review and no prior output to draw on.
- Immersion: optional input/logging; no quota.
- Anki: 20–30 minutes; vocabulary owner. If the local bridge is available,
  run `python3 scripts/anki_bridge.py due`; otherwise use Anki directly.
- Active source: the Yokubi spine in [[Japanese/SOURCES|the source map]] owns
  sequencing and lesson locators. The pinned markdown is read directly from the
  private checkout; the map's `url` is the public locator for anyone without it,
  and no source text is pre-selected.

## Next action

Teach/continue `jp-yokubi-00` — sentence anatomy, word order.

The exercise open when the round closed: put these seven words into one
sentence, verb last — `が の ない 全然 勉強 アンキ 最近` — then practise the
result, then continue to `jp-yokubi-01`. The earlier topic-ordering exercise
was withdrawn as unsound: it changed two variables at once and pulled the
は/が distinction forward from lesson 3.

```text
one ground-up grammar contrast
→ immediate practice
→ one small reading or sentence-analysis task
→ append evidence events
→ rewrite this file with the next action
```

## Evidence and archive

- Active usage events: curriculum `## Usage events` tables.
- Last Japanese evidence: `jp-yokubi-00` introduced and practised 2026-09-27
  (receipt `_private/learning/receipts/2026-09-27-jp-yokubi-00.md`).
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
- reading session count, re-derived from `review.py usage`;
- last evidence link (`## Evidence and archive`);
- any source blocker or unresolved question
  (`## Source notes and blockers`).

Do not leave this file describing a session that has already happened.
