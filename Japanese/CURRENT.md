# Japanese — Current Session Handoff

**Updated:** 2026-10-04
**Status:** new loop live. 7 probes, 4 passes, floor L0. The immersion swap is
complete — `D:/immersion` now holds the encoded tree (see *Pending
maintenance*, struck out).

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

- **Progress:** the ledgers contain 7 probes, 4 passes, **floor L0**. The open
  `progress.jsonl` session line still covers only the first probe; close it at
  the end of the session rather than hand-editing it now.
  Ledgers: `Japanese/probes.jsonl`, `Japanese/progress.jsonl` (append-only).
- **Anki:** the learner reported no study lately (`最近、anki の勉強が全然ない`).
  Recorded as fact; it does not move the floor. The direct SQLite read is
  stale (collection mtime 2026-10-02, last revlog 2026-09-25), so study time
  cannot be verified locally. Lane `patch`: Kaishi 1.5k — 1501 cards, 1000
  stuck, 414 mature. The 1000 stuck cards are the real target.
- Reading gate: **0 / 30 actual novel-reading sessions**. Derive it with
  `python3 scripts/review.py usage japanese-reading`, never hand-count.
- Reading mode: English explanation first for sessions 1–30; from session 31
  the learner attempts Japanese first.
- Immersion: the encoded library in `D:/immersion` is what the learner
  actually watches (`complete-beginner`, `beginner`). No quota, no log. The
  only gap is the `0463` intermediate video (corrupt source, subtitle present;
  re-download wanted).

## Pending maintenance — ~~encode → verify → replace D~~ DONE 2026-10-04

1. ~~**Encode**~~ — full pass plus targeted retry: all 1718 jobs scanned,
   1717 outputs produced. The five 61–91-minute timeouts were fixed with a
   duration-aware timeout (`--match` rerun, job `pwsh-671`, exit 0).
2. ~~**Verify**~~ — `--deep-verify` (job `pwsh-774`): all 1717 outputs probe
   clean with source-matching durations. Pairing check clean. Spot-probed 8
   files on D after the move: all good.
3. ~~**Replace D**~~ — done with learner approval: D originals (207.5 GB)
   deleted, `advanced` junction link removed (target untouched at the time),
   encoded tree moved `ImmersionC` → `D:/immersion` (job `pwsh-777`, all
   robocopy codes 1), old `C:\...\Videos\Immersion\advanced` originals
   (43.4 GB) deleted (job `pwsh-787`). Final D counts: complete-beginner
   356/356, beginner 657/657, intermediate 536/537, advanced 168/168.

One known gap, not corruption in the tree: `0463.intermediate.日本の夏祭り`
has no video because its source download is truncated (`moov atom not
found`); its subtitle is on D. Re-download that one source whenever it is
wanted — it is the only file missing from `D:/immersion`.

Disk after swap: D ~125 GB free, C ~455 GB free plus the 43 GB reclaimed.

## Next action

**The binary search has bracketed the edge.** Since the L1 probe, the record
is: L1 pass (`negative-shinai-choice-2026-10-04d`), L3 miss
(`sentence-topic-order-watashi-mainichi-2026-10-04e`), L2 pass
(`short-answer-hai-benkyou-suru-2026-10-04f`), L3 miss
(`sentence-topic-order-anata-mainichi-2026-10-04g`). Both L3 misses are the
same error: the time word fronted before the topic (`毎日、あなたは...`
instead of `あなたは毎日...`). L1 and L2 pass; L3 fails twice on word order.
The learner decides whether the floor moves.
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
- Last Japanese evidence: two L0 passes on 2026-10-04, signatures
  `wordorder-adverb-verb-yoku-benkyou` and `topic-wa-deshi-2026-10-04a`,
  followed by one ambiguous L0 negative-attachment miss,
  `negative-shinai-attachment-2026-10-04c`; then L1 pass
  `negative-shinai-choice-2026-10-04d`, L3 miss
  `sentence-topic-order-watashi-mainichi-2026-10-04e`, and L2 pass
  `short-answer-hai-benkyou-suru-2026-10-04f`, followed by a second L3 miss
  on the same ordering error,
  `sentence-topic-order-anata-mainichi-2026-10-04g`.
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