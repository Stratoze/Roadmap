---
name: daily-note
description: Write today's Daily/YYYY-MM-DD.md at the end of a session. Use when the session ends or the learner reports minutes.
---

# daily-note

Parents read these notes. Accurate, not flattering.

1. Run `TZ=Asia/Tokyo date` for the date and end time.
2. Collect facts only from: what the learner said this session, the clock, files that exist. Never guess minutes. If the learner did not report minutes, write "time not reported".
3. Write `Daily/YYYY-MM-DD.md` in exactly this format (copy of `Daily/TEMPLATE.md`):

```
---
date: "YYYY-MM-DD"
tags: [daily]
---
**Japanese:** <what was done, minutes, source of the minutes>
**Technical:** <items done with result, minutes>
**Next:** <tomorrow's one step per track, from WEEK.md>
```

4. Floor check, one sentence per track that missed it: "The 25-min technical floor was not met today."
5. Coursework never counts toward the floor. Write it as "Coursework (not counted): ...".
6. A track with nothing done: "Nothing logged."
7. If a note for today already exists, add to it; corrections change the fact, never soften it.

Example line: `**Japanese:** Comprehensible Japanese 25 min (learner-reported). Grammar 5 あります / います: taught, 4/5 quiz right (slip: ほんを あります). Chat: 5 exchanges.`
