# Japanese — Current Session Handoff

**Updated:** 2026-10-04
**Status:** new loop live. 3 probes, 2 passes, floor L0. The full encode pass
finished with six known failures; five long-video retries are now running in
the background (see *Pending maintenance*).

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

- **Progress:** the ledgers contain 3 probes, 2 passes, **floor L0**. The open
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
- Immersion: the encoded library in
  `C:\Users\Kohaku\Videos\ImmersionC` is what the learner actually watches
  (`complete-beginner`, `beginner`). No quota, no log.

## Pending maintenance — encode → verify → replace D:

The learner's standing instruction: **finish the encode, verify it, then
replace the immersion on D:**. Three steps, in order, not to be collapsed.

1. **Encode** — the full pass has scanned all 1718 jobs: 488 newly encoded,
   1224 skipped, 6 failed. Former background job `pwsh-11` is finished, exit 1.
   - Five failures are 61–91-minute sources that exceeded the old fixed
     3600-second timeout. `scripts/encode_immersion.py` now uses a
     duration-aware timeout and supports targeted reruns with `--match`.
     Active retry: background job `pwsh-671` with
     `--match 1116 0483 0644 0823 1120 --workers 2`.
   - One source is unrecoverable by encoding:
     `0463.intermediate.日本の夏祭り...mp4` reports `moov atom not found`.
     Its subtitle is already copied, and no duplicate source was found, so it
     needs a fresh download rather than another encode attempt.
   - Removed the output-only `MANUAL-TEST.mp4` artifact and normalized the
     redundant `0967...mp4.vtt` subtitle name.
   - `.part.mp4` files sitting at 0 MB are **normal buffering**, not a stall.
     Historical mean is ~819 s/file. Do not kill the run over them.
2. **Verify** — only after the retry exits 0 **and** the corrupt `0463`
   source is either replaced or explicitly deferred:
   `& python3 "scripts/encode_immersion.py" --verify-only`.
   Confirm pairing and sizes before anything on D: is touched.
3. **Replace D:** — **only after the learner approves the verify result.**
   `D:\immersion\advanced` is a junction to
   `C:\Users\Kohaku\Videos\Immersion\advanced`. Originals on D: must not be
   deleted before the verify passes.

Disk: C: ~500 GB free, D: ~29 GB free.

## Next action

**Score the open clean L1 probe before opening anything else.** It was built
from mature Kaishi vocabulary after the earlier negative probe proved
ambiguous: standalone `勉強` can be the noun “study” or the front of
`勉強する`.

> “(I) don’t study” is:
>
> A. べんきょう しない
> B. べんきょう は ない

The prior ambiguous miss stays recorded; do not re-litigate it. If the learner
answers A, continue the requested binary search upward with deck-backed words.
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
  `negative-shinai-attachment-2026-10-04c`.
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