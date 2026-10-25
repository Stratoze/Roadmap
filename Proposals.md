# Opus inbox

Everything waiting on Opus, in one place. Pull-based: nothing runs on its
own, no schedule. Haiku adds items; only the learner calls Opus; when
called, Opus works **Open** top-down and moves each item to **Done** with
its decision. Haiku never acts on an item here.

## How items get here (Haiku)

1. **Proposals** from the learner or from Haiku: one item each, with date
   and source. Never anywhere else (`AGENTS.md` "Files").
2. **Audit lines:** any "check for Opus" (or older "check on Sunday") line in `Learned/` gets an item
   pointing to it.
3. **Pull signals.** At session start, check these; if one is true and not
   already listed, add an item:
   - A `BACKLOG.md` queue (grammar, technical, chat openers) has 5 or
     fewer keyed items left → "Refill <queue>: next keys from <item>."
   - The next item in a queue has no key → "Keys needed from <item>." (That
     item is skipped until then.)
   - 7 days or more since the last audit (see below) → "Audit due: the
     learner pastes one Japanese chat and one tutor chat."
   - The learner says Haiku accepted a wrong answer → "Move <task type> to
     Sonnet?"
   Last audit: 2026-10-25 (Opus).
4. If **Open** has any item, tell the learner once at session start:
   "Opus inbox: N open (top: <first item>)." Do not push further.

## Open

### Refill: chat openers and grammar keys
- Chat openers: 10 left. Grammar keys: G12b-G26 (15 items, ~5-8 sessions
  at current pace). Technical keys run to S4 (18 items). Not urgent; do it
  at the next Opus call so no queue runs dry. Grammar keys from G27,
  technical from T29, then M1-M4 after T43.

## Done

### 2026-10-25: pull-based backlog instead of a weekly plan (learner's request)
- Adopted, Opus 2026-10-25. `WEEK.md` and `NEXT.md` merged into
  `BACKLOG.md`: ordered queues (grammar, chat openers, technical), each
  item with its prompt, key and `Result:` line. No dates; a missed day
  leaves the queue where it was. Opus refills when the inbox signals it;
  audits are pulled every 7 days. `AGENTS.md` and all four skills updated.

### 2026-10-23: proposals need one designated home (learner's request)
- Adopted, Opus 2026-10-25. `AGENTS.md` "Files" now names this file as the
  only home for proposals, with Haiku's end-of-session sweep of `Learned/`,
  `Daily/` and `BACKLOG.md`.

### 2026-10-23: technical floor counts solved items, not minutes (learner's request)
- Adopted, Opus 2026-10-25. `AGENTS.md` "Daily floor": met by one item that
  passed its check today, or by 25 min on items. An item whose answer the
  tutor gave away does not count. `daily-note` skill updated to match.

### 2026-10-23: item 8 circular reason (for Opus to review)
- Reviewed, Opus 2026-10-25. The reason was circular and should not have
  been accepted as an explanation, but the tick stands: item 8's check is
  the number (12 J), and the reason was earned on item 9. Noted in
  `Learned/technical.md`.

### 2026-10-23: tech-tutor master prompt (learner's request)
- Adopted, Opus 2026-10-25. The exercise now opens the prompt, rule 0 makes
  the tutor restate it in its first message, and rule 10 says "Correct." is
  not enough on `end`: it must print the three headed parts.

### 2026-10-23: grammar 12 quiz does not test へ
- Adopted, Opus 2026-10-25. A12 gets follow-up question 5 (へ written,
  pronounced "e"), asked once on Mon 10-26 before the new point. It does
  not change the pass on 12.

### 2026-10-23: two chat corrections flagged "check on Sunday"
- Audited, Opus 2026-10-25, in `Learned/japanese.md`: the 電車の本 rewrite
  was a wrong guess (spelling slip was コンピューター); the 机や… correction
  is void (the learner was right).

### 2026-10-20: should a one-kana typo count against a grammar quiz?
- Raised in the grammar 11 log. Answered by the scoring rule in `AGENTS.md`
  (Opus, 2026-10-21): a typo that leaves the word clear is noted, not counted.
- Source: `Learned/japanese.md`, 2026-10-20 grammar 11 entry.
