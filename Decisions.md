# Decisions

Why the rules are what they are. Not read at session start; read it
before changing a rule. Newest sections first.

## Rule reasons (from `AGENTS.md`)

- Haiku does not chat or correct Japanese: it "corrected" a correct sentence and miscounted exchanges (2026-10-14).
- Haiku does not write quiz questions or keys: the A9 quiz was invented by Haiku when A9 had no question list (2026-10-17).
- Grill is Sonnet: Haiku drifted off the question list (2026-10-12).
- Technical tutoring goes to a free chat AI via `tech-tutor`, not Sonnet: Sonnet cost made the learner skip [S] tasks, so drawings sat undone 4 days (2026-10-17).
- Quiz answers in kana or keyboard kanji, never romaji: picking the right kanji already needs the reading (2026-10-17).
- Grammar scoring counts only the point's own forms: 11 や was held two days by misses not about や (2026-10-21).
- Opus is manual-only; no scheduled tasks (learner, 2026-10-21).
- Kaishi: no reset; the learner's RWKV-scheduler fork keeps its memory model only if the history stays (2026-10-17).
- Japanese is the priority track (learner, 2026-10-14). Free day about 2 h 15 min (learner agreed 2026-10-17).
- Push after each item so nothing is lost if a session dies (learner, 2026-10-17).
- Transcripts stay in the chat service: the cloud container is wiped and `_private/` is never pushed.
- 2026-10-25: `Learned/` split into a short status file (read at session start) and `Learned/log/` (append-only history), and rule reasons moved here, to cut what every session loads (learner: history in the docs was hurting performance).

## Proposals decided (from `Proposals.md`)

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

## Earlier decisions (from `NEXT.md`)

Decided by Opus 2026-10-17 (Sat, called early):
- jp-chat template: role, culture rule (soft no), vocabulary (1-2 new words per line, glossed once), and `end` prints corrections + new words + transcript. All in `.claude/skills/jp-chat/SKILL.md`. (Superseded: glosses dropped 10-21; transcripts stay in the chat service.)
- Grammar pace: up to 3 points on a free day until 2026-11-15, then 1 a day. Rule in AGENTS.md "Grammar pace". Keys A10-A14 are in WEEK.md.
- Push after each item: now in AGENTS.md "Git".
- Project choice (mini self-driving car / QDD robot / feng shui AI): no new project until Phase 0 is done (item 17 of 60 now). When it is, the QDD robot is first choice: it reuses the 2-link arm's statics, circuits and kinematics, and fits "robots". The self-driving car is second. The feng shui AI is off-goal; keep it as a hobby idea, not a milestone.
- ML and statistics (learner's main ask, missed in the first pass): yes, inside the technical track, not as a third daily track. Statistics block S1-S4 after 0.4 (measurement spread: every portfolio entry already compares predicted vs measured, and that comparison means nothing without spread). First ML block M1-M4 after item 43 (fit a line to the arm's own potentiometer data: least squares is the simplest ML model, and the capstone needs that calibration). Later ML (classification, neural nets, learning control) is planned when Phase 0 ends, on the robot's own data. Not RL now: it needs a simulator and an evaluator first, which is tool-building, and the floor is 25 min.
- Weight, food, exercise logging: not in this repo. Advice on diet needs a qualified source (doctor or dietitian); a plain notes app is enough for logging.
- Second pass, same day, after the learner said proposals were missing: the 10-17 chat (17 replies) was logged and audited (it had only been filed as a proposal); quiz answers may be kanji from the keyboard, never romaji; drawing items 10, 11, 12, 15 go to Haiku as typed lines against the keys; the teacher-check task moved to Wed 10-21 class.
- Technical round moved to Haiku + free chat AI (`tech-tutor` skill), learner's proposal. Sonnet is now only for coursework grilling. Keys get a Given / Answer / Check split so Haiku never leaks an answer; T17, T18 rewritten that way, the Sunday plan writes the rest that way. Sunday audit now takes one technical tutor chat as well.
- Kaishi (~1249 overdue): no reset, the learner reviews it down (their proposal; reset would wipe the RWKV scheduler's history). Rule in AGENTS.md.
- Flow reviewed with the learner 2026-10-17: free day ~2 h 15 min (CJ 40, grammar up to 3, Kaishi 20 min, chat 25, technical 25); tight day CJ 25, 1 point, Kaishi 10 min, chat ≥5, technical 25. Transcripts stay in the chat service (cloud container gets wiped); only the end summaries are pasted to Haiku. Sunday plan must write about 15 grammar keys a week (keys end at A14) and every technical key as Given / Answer / Check.
- Opus 2026-10-21: quiz scoring rule (only the point's own forms count); jp-chat template (kanji with readings, no English glosses, real back-and-forth).
- Opus 2026-10-25: `WEEK.md` and `NEXT.md` replaced by this backlog (learner's request): the day-by-day plan kept going stale whenever a day was missed, and Opus is manual-only, so a weekly rewrite can't be relied on.

## Fitness (2026-10-26)

- Haiku classifies (food name, grams, source) and `fit.py` does the maths:
  Haiku's arithmetic and memory of food values are its weakest points.
- Scale or label first, photo last: photo portions and hidden oil are the
  biggest error. Weekly calibration meals (photo estimate, then weigh)
  measure Haiku's photo error instead of guessing it.
- Images sent in chat are not saved as files, so the log keeps a written
  `--note` of what the photo showed.
- Formula target first, then measured maintenance from intake and the
  weight trend: the formula is off by hundreds of kcal for many people.
- No vitamins or minerals: a photo cannot estimate them, and logging them
  costs time for no decision.
- No reminders (Opus runs only when called); the skill asks at session start.
