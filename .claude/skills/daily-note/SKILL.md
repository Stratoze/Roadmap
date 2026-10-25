---
name: daily-note
description: Write or update today's Daily/YYYY-MM-DD.md note for the learner's Roadmap. Use this at the end of every study session, and whenever the learner reports minutes ("I watched 30 min of CJ", "did 20 min of katakana"), finishes a BACKLOG.md item, or says they are stopping for the day, even if they don't ask for a note.
---

# daily-note

The learner's parents read these notes to see what actually happened. A note
that flatters or guesses is worse than no note, because it breaks their trust
in every other note. So: only facts, plainly said.

## Steps

1. Run `TZ=Asia/Tokyo date` for the date. The learner is in Japan; the
   container clock is not.
2. Gather facts from three sources only: what the learner said this session,
   the clock, and files that exist (ticks and `Result:` lines in `BACKLOG.md`). If the
   learner did not give minutes, write "time not reported" rather than an
   estimate, because a guessed number reads as a measured one.
3. If `Daily/<date>.md` already exists, edit it instead of starting over.
   When a fact changes, change the fact; do not soften it ("almost met").
4. Write it in this exact format (from `Daily/TEMPLATE.md`):

```
---
date: "YYYY-MM-DD"
tags: [daily]
---
**Japanese:** <what was done, minutes, who reported them>
**Technical:** <items done with result, minutes>
**Next:** <tomorrow's step per track: unfinished items first, then the next items in BACKLOG.md>
```

## Next line

Unfinished work comes first. If an item's check did not pass today (e.g. a
grammar quiz 3/5, an item done only with the answer given), tomorrow's step
is to finish it, not the next item in `BACKLOG.md`. Moving on blindly
would skip a point the learner has not got yet.

## What counts

- Floor: 25 min Japanese; technical is met by one item that passed its
  check today or by 25 min on items (AGENTS.md "Daily floor"). If a track
  missed it, add the sentence "The <track> floor was not met today." A missed day is not
  made up by a longer day, so never net minutes across days.
- Japanese floor: Comprehensible Japanese, the grammar lesson, the Japanese
  chat. Katakana, Tadoku and Anki are logged but not counted.
- Coursework (school projects) never counts. Log it inside **Technical:** as
  "Coursework (not counted): ...".
- A track with nothing done: "Nothing logged."
- Include mistakes that matter (a slip, an item needing hints). Parents and
  the next session both need them.

## Example

```
**Japanese:** Comprehensible Japanese 25 min (learner-reported). Grammar 5 あります / います: taught, quiz 4/5 (slip: ほんを あります → ほんが あります). Chat: 5 exchanges.
**Technical:** Item 8 done: 12 J (predicted 6 J; forgot area of a triangle is half). ~15 min by clock. (Item passed its check, so the technical floor is met.)
**Next:** Technical: item 9. Japanese: grammar 6, これ / それ / あれ / どれ.
```
