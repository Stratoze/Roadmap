# Japanese — Current Session Handoff

**Updated:** 2026-10-04
**Status:** new loop live. 2 probes, 2 passes, floor L0. One pending
maintenance job is running in the background (see *Pending maintenance*).

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
   `... session ...` line; read the floor with
   `python3 scripts/progress.py --domain Japanese show`
   rather than inferring it. Note the flag order — `--domain` is **top-level**
   and must precede the subcommand.
5. Active grammar path: `jp-yokubi-00` → `jp-yokubi-01` →
   `jp-yokubi-02` → `jp-yokubi-03`. Kana are assumed known; the grammar
   sequence starts from sentence anatomy.

## Two hard rules learned the hard way

- **Never reuse a probe.** Every probe gets a fresh signature
  (`question_signatures.py` style). The learner called out repeated sentences
  directly — *"do you know how boring that gets?"* A recycled probe is a wasted
  minute of the learner's scarcest resource.
- **Never emit garbled Japanese.** Stray tokens have leaked into tutor output
  more than once. When a sentence must be built rather than recalled, build it
  from a word the learner supplies, and keep it to known grammar only.

## Grammar frontier

- `jp-yokubi-00` (Yokubi Lesson 0, sentence anatomy) is now **passed twice at
  L0**. Coverage reads `jp-yokubi-00: 0` — Level 0 cleared, Level 1 not yet.
- Signatures cleared: `wordorder-adverb-verb-yoku-benkyou` (adverb before
  verb, verb last), `topic-wa-deshi-2026-10-04a` (topic-comment with
  `〜は〜です`).
- Source locator: <https://yoku.bi/Section1/Part1/Lesson0.html>, reached
  through [[Japanese/SOURCES|the source map]]. Read the pinned private
  checkout, not the live site:
  `git clone https://github.com/Stratoze/private-jp _private/private-jp`
  then `git -C _private/private-jp submodule update --init`.

## Current state

- **Progress:** 1 session, 2 probes, 2 passes, **floor L0**. Recent rate
  1.00 (target 0.85); Wilson confidence 0.34 — a readout, **not** a gate.
  Ledgers: `Japanese/probes.jsonl`, `Japanese/progress.jsonl` (append-only).
  One pass short of the 3 needed before a floor move even becomes possible.
- **Anki:** the learner reported no study lately (`最近、anki の勉強が全然ない`).
  Recorded as fact; it does not move the floor. The direct SQLite read is
  stale (collection mtime 2026-10-02, last revlog 2026-09-25), so study time
  cannot be verified locally. Lane `patch`: Kaishi 1.5k — 1501 cards, 1000
  stuck, 414 mature. The 1000 stuck cards are the real target.
- Reading gate: **0 / 30 actual novel-reading sessions**. Derive it with
  `python3 scripts/review.py usage japanese-reading`, never hand-count.
- Reading mode: English explanation first for sessions 1–30; from session 31
  the learner attempts Japanese first.
- Immersion: the encoded library in
  `C:\Users\Kohaku\Videos\ImmersionC` is what the learner actually watches
  (`complete-beginner`, `beginner`). No quota, no log.

## Pending maintenance — encode → verify → replace D:

The learner's standing instruction: **finish the encode, verify it, then
replace the immersion on D:**. Three steps, in order, not to be collapsed.

1. **Encode** — `& python3 "scripts/encode_immersion.py" --workers 6`,
   running as background job `pwsh-11`. Level order is `complete-beginner`,
   `beginner`, `intermediate`, `advanced`. Writes `.part.mp4` and renames
   only on success.
   - Last count (2026-10-04): `complete-beginner` 356 ✅, `beginner` 658 ✅,
     `intermediate` 218 in progress, `advanced` 0 — ~1232 of 1718.
   - `.part.mp4` files sitting at 0 MB are **normal buffering**, not a stall.
     Historical mean is ~819 s/file. Do not kill the run over them.
2. **Verify** — only after the run exits 0:
   `& python3 "scripts/encode_immersion.py" --verify-only`.
   Confirm pairing and sizes before anything on D: is touched.
3. **Replace D:** — **only after the learner approves the verify result.**
   `D:\immersion\advanced` is a junction to
   `C:\Users\Kohaku\Videos\Immersion\advanced`. Originals on D: must not be
   deleted before the verify passes.

Disk: C: ~500 GB free, D: ~29 GB free.

## Next action

**Third fresh probe at L0.** Two passes in hand; the ratchet wants three
consecutive passes at floor plus a recent rate ≥ 0.85 before L1 is even on the
table. Do not drift toward L1 content yet.

The exercise left open by the last round, if it is reused in *shape* but never
in wording: put these seven known words into one sentence, verb last —
`が の ない 全然 勉強 アンキ 最近`. `全然` is in the live stuck set, so it is
consolidation material, not new input.

The earlier topic-ordering exercise stays withdrawn as unsound: it moved two
variables at once and pulled the は/が distinction forward from lesson 3.

```text
brief (keywords, questions, one task, source) → learner studies
→ converse at the floor, one question per message
→ append probes + one session line to the ledgers
→ rewrite this file with the next action
```

## Evidence and archive

- Active usage events: curriculum `## Usage events` tables; progress in the
  append-only ledgers under `Japanese/`.
- Last Japanese evidence: two L0 probes on 2026-10-04, signatures
  `wordorder-adverb-verb-yoku-benkyou` and `topic-wa-deshi-2026-10-04a`.
- Pre-reset evidence: [[_system/learning/archive/japanese-progress-reset-2026-09-26|archived reset record]].
- Raw learner work: `_private/` only.

## Source notes and blockers

- No sourcing blocker is open. `Japanese/source-map.json` carries the current
  verification block and IMABI licence note.

## Close contract

Before ending a Japanese session, update:

- `Updated` date;
- next action and branch (`## Next action`);
- grammar frontier (`## Grammar frontier`);
- the floor and coverage, derived from `progress.py` (never hand-computed);
- the state of the pending maintenance job above, and strike it out when
  step 3 completes;
- reading session count, re-derived from `review.py usage`;
- last evidence link (`## Evidence and archive`);
- any source blocker or unresolved question
  (`## Source notes and blockers`).

Do not leave this file describing a session that has already happened.