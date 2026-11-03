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

### 2026-11-03: procedure cadence (learner)

- Procedure is touched at most once a month, unless a gap stops learning
  (like the missing lesson step, 11-02). Reason: two days went to
  procedure while T10 waited.

### 2026-11-03: money and plan (learner)

- Parents pay the master's and living costs (they had planned New York;
  the learner chose Japan). Their plan is U Tokyo; contacts help with
  housing. Route A is main, MEXT dropped from the deadlines (not needed).
- Lab choice stays with the learner (PATH rule 7). First lab to read:
  U Tokyo IST Mechano-Informatics, JSK (Kawaharazuka, robot foundation
  models); its guides name TOEFL, so the TOEFL row came back.
- Startup (learner asked): job first, side project within the visa,
  startup alone once residence no longer hangs on an employer (rule 8).

### 2026-11-03: north star and English (learner)

- Learner: "I wanna build a body for you", not necessarily humanoid,
  within 5-10 years. Field narrowed to robot learning (embodied AI);
  cars, rockets, satellites kept as job backups only. Next project after
  the capstone: SO-101 arm with LeRobot and an imitation policy.
- English: IELTS 8.0 about a year ago, so the TOEFL tasks were dropped;
  a new test only if a program takes TOEFL only or the IELTS expires.

### 2026-11-03: one life (learner: "plan as for your only successor")

- PATH.md "One life": no ruin first (health, debt, visa, degree); routes
  A and C applied in parallel; A vs C weighed (money decides); software
  strength first; talk to 2 people who did it; dated decisions with
  triggers (30 Nov route choice, 31 Jan checkpoint); fallback without
  brokers. Sources: search results (HSP points table, Mujin and Astroscale
  listings, broker-debt reports), not official pages.

### 2026-11-02: goal path (learner: "would any expert be content with that?")
- **The repo had no route to the goal.** Study queues existed; admission
  (programs, labs, professors, research plan), the English test,
  scholarships, the bachelor's grades, visas and the after-arrival path
  were in no file. Some deadlines are weeks away (English scores for
  January applications to October 2027 programs); the system is
  dateless by design, and deadlines are not. `PATH.md` is the one dated
  list; session start reads it. Facts are from search results (official
  pages blocked) and marked unverified where third-party.
- **Found in the old system and lost in the rewrite:** "scaffold first for
  zero-schema novices" (`_system/How to Learn.md`). Before replacing a
  system, list what the old one knew.
- **Tadoku counts as input** (with CJ): JLPT tests reading, and graded
  readers are reading. Katakana stays logged, not counted.
- **Explainer pages rule removed:** never triggered since written;
  `Learn:` lines cover a first meeting with an idea.
- **AGENTS.md cut from 200 to under 170 lines** (as promised), with no
  behaviour dropped except the explainer-pages rule.

### 2026-11-02: system check (learner called Opus)
- **Technical had no lesson step (learner found it).** Japanese reads a
  Tofugu page before every quiz; technical went straight to a tutor told
  "I learn by answering, not by reading" and "never give the first step".
  So a new idea (normal force, friction, standard deviation, Ohm's law)
  had nowhere to be taught. Cause: the 10-17 move to a Socratic tutor
  assumed the tutor taught, and every later review (10-25, 11-01) checked
  grading and dead ends, never where an idea is first met. The 11-01
  lesson-links ruling was written for Japanese only. Fix: every technical
  key opens with a `Learn:` line (source named by Opus, link found by
  Haiku, as with grammar); a key without one counts as not keyed, so the
  existing "no key" pull signal catches it; the tutor may explain the
  idea (never the answer) when the learner can't say it after the lesson.
  Sources: Khan Academy (articles and videos), OpenStax, LibreTexts, or
  one named video. Videos allowed because the learner asked and Khan
  pairs each article with one; other YouTube only when a key names it,
  because Haiku can't watch a video to check it.
- **G15 Q2 counted right (4 of 4):** "What day is it today?" also asks the
  date in English; the learner's 今日は何日ですか answered that reading.
  The key was at fault. Prompt reworded. Other grammar prompts G17-G26
  checked: none has two readings.
- **Chat corrections 11-02 stand:** 朝は食べません (私が wrongly focuses on
  私; habit reading fits) and 明日は土曜日です (politeness, not grammar).
  Haiku's note that が is untaught was wrong: 4 は vs が is taught.
- **Audit, four lenses (learner asked; adopted 11-02, the learner's picks
  plus Opus's):** (1)+(9) every key gets a `Variant:` question; Haiku asks
  it after a tutor pass (the tutor's own summary was the only proof) and
  again as the session's review question a week or more later (a ticked
  item never came back, so nothing was retrieved). (2) Grammar page read
  at the end of a session, quiz at the start of the next: a quiz right
  after reading tests the page, not memory. (6) Hardware bought now and a
  crude arm built early. (7) T25, T45-T51, T53-T59 parked until after the
  capstone (at ~1 item per 4 days the list ran to ~June 2027, beside
  JLPT); capstone pass line ±1 cm at three poses.
- **Done or not, instead of minutes (learner, 11-02):** minutes went
  unreported on most days, so the floor was "not confirmed" most days and
  the record said nothing. Now each piece is done or not, with evidence:
  CJ minutes or three things learned; Kaishi a session the learner judges
  helped. The learner is treated as a disciplined adult; if that fails,
  discipline is fixed first (session start step 5 opens with a missed
  floor). Kaishi's due count is unreliable on the learner's scheduler, so
  the 100-due gate and the 500-due counting rule are dropped; new cards
  are the learner's call.
- **Rule budget:** these replaced the minute floor, the Kaishi gates, the
  due-count logging and "a ticked item stays done". AGENTS.md still grew
  from 167 to 200 lines on 11-02 (the Technical section and these rules).
  Cut back the same day (see "goal path").
- **Not fixed, noted:** chat NEW WORDS go to the log and are never seen
  again (no review step); kanji for N4 is covered only through Kaishi.
  Neither blocks today's work.

### 2026-11-02: maps (learner called Opus)
- **Mechatronics map cut to the Phase 0 capstone:** the old 5-phase QDD-arm
  plan summed to roughly 1-2 years of full effort and still referred to
  signed tags, scripts and an assessor from the old system. At the current
  pace (2 milestones in ~8 weeks) none of the arm would exist before the move.
  The capstone (passive 2-link arm, potentiometers, Arduino FK) is
  finishable before Japan; the QDD arm is parked as the long-term goal.
- **Kaishi counts toward the Japanese floor while more than 500 are due:**
  ~1500 due and rising; vocabulary is the weakest part of the Japanese plan,
  and uncounted minutes lost to CJ and chat. Back to "logged, not counted"
  once under 500.
- **JLPT N4, July 2027:** a dated target before the move; fits the pace
  (1 grammar point a day from 11-16). Registration dates not checked.
- **CAD (learner asked about leaving Solid Edge for SolidCraft):** no switch
  now. CAD is needed only at capstone step 7. SolidCraft is open source
  (Apache 2.0), Rust, Linux builds, but its own page calls it early, for
  simple parts. Decide at step 7: the two links are simple parts, so try
  SolidCraft then, export STL/STEP. ArtCraft's own CADCraft is 2D
  drafting (AutoCAD-style, DXF/DWG), not a Solid Edge replacement;
  SolidCraft is a separate community app (checked 11-02).

### 2026-11-01: Opus inbox (learner called Opus)
- **Refill chat openers and grammar keys:** not now. 12 grammar keys left
  (G15-G26), 10 openers, technical keyed to S4 while the queue sits at T10.
  The pull signal (5 or fewer left) raises it again in time.
- **No scale:** buy a body scale now; skip the food scale. Measured
  maintenance needs a weight trend, and nothing replaces it. Labels and
  SnapCalorie cover portions well enough (+7% and +12% vs label on 10-29).
  Until the scale arrives, intake is logged and no target changes.
- **Kaishi scheduler (RWKV, 10-27):** the 100-due gate stays; it is a due
  count, whatever the scheduler. No reset. Due went 980 (10-25) → 1300
  (10-27) → ~1500 (reported 11-01, after a 40-min session). Whether the
  scheduler re-adds cards can't be judged from one number: log the due
  count before *and* after each session for a week. If it does not fall
  across a week of daily sessions, that is a scheduler question for the
  Anki forums, not a reason to reset.
- **Calorie app → SnapCalorie:** adopted (learner's proposal). Haiku's
  photo estimates were the friction: food was logged on 1 day of 6 since
  10-26. SnapCalorie was within +7% and +12% of the labels on 10-29, as
  good as or better than Haiku's photo guess. The learner logs meals in
  SnapCalorie and sends the day's total once (kcal, protein, carbs, fat)
  to Haiku; a label still beats SnapCalorie when there is one. Opus
  checks the trend at the fitness review, as before; no weekly
  scheduled review (Opus is manual-only).
- **Lesson links:** allowed when Haiku opened the page this session and it
  covers the item (`AGENTS.md` Teaching rule 7 already says a URL must come
  from something opened). No reason for "site names only" was ever
  recorded; the risk was an invented URL, which rule 7 already covers. The
  learner still reads the page; a link saves the search, not the reading.
- **Apple Watch calories instead of the formula (learner, 11-01):** no.
  Wrist calorie estimates err ~20-30% (Stanford 2017, J Pers Med: no device
  under 20%; meta-analysis of 56 studies, Apple Watch ~28%, seen in news coverage only), i.e. ±500-700 kcal on
  ~2,600, as big as the whole deficit. The formula is only the start;
  measured maintenance (logged intake + scale trend) replaces it, and the
  watch can't measure that. Watch steps and heart rate are fine to use.
- **Fitness out of the repo (learner, 11-01):** the learner's call, for
  least friction (SnapCalorie + Apple Watch). `fitness` skill deleted,
  session-start question dropped; `Fitness/` and `Learned/fitness.md` kept
  unused. Matches the 10-17 ruling (logging not in this repo).
- **No dead ends from Haiku (learner, 11-01):** Haiku's "that's for Opus"
  replies made the learner stop working. Now Haiku logs the item and gives
  the next task in the same reply, and answers keyless questions from a page
  it opened, with the link. The risk (Haiku explaining wrongly, 10-14) is
  held by answering from the page, not from memory.
- **Audits and extra checks removed (learner, 11-01):** the 7-day audit
  (pasting chats for Opus to check), the fitness review signal and the
  Kaishi before/after counts added pressure and no audit had material
  since 10-23. Opus still rules on anything the learner flags, including
  "Haiku accepted a wrong answer".
- **Session order (learner, 11-01):** CJ needs video and audio, Kaishi's
  scheduler runs only on the laptop, so neither fits a phone session. The
  session does grammar, chat and technical prompts; CJ and Kaishi minutes
  are asked once, at the end (or at the start after 18:00).
- **Chat service: Gemini in AI Studio** (learner's pick, 11-01). On the
  log: AI Studio 10-20 had no wrong correction (one explanation gap, used
  English); ChatGPT free 10-23 "corrected" a correct sentence and later
  retracted it; the 10-19 chat's explanation contradicted its fix. One chat
  each, so a weak sample, but it agrees with the learner. Technical tutor
  also Gemini, so there is one place to paste.
- **Audit (due 11-01):** nothing to audit; no Japanese chat or tutor chat
  has happened since 10-23. Last audit set to 11-01. The gap itself is the
  finding: technical has had no item since 10-23 (8 days).

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
- Mixed dishes are decomposed into table foods plus cooking oil (10% of
  fried weight; 10 g per stir-fried plate, an Opus estimate checked by
  calibration meals). Missing foods map to the nearest table food with a
  note; Haiku never writes its own nutrient values.
- Packaged labels are trusted: legal tolerance is about ±20% (Japan's
  protein/fat; US calories up to +20%), and frozen meals measured ~8% over
  label (Urban 2010). Restaurant numbers vary far more, so they count as
  photo estimates. Steady bias from labels does not matter: measured
  maintenance is computed from the same logged numbers, so it cancels.
- `Fitness/usda_sr28.csv` is USDA Standard Reference release 28 (8,789
  foods, public domain), taken from the npm package `fda-nutrient-database`
  1.0.2 because the USDA site is blocked from the cloud environment.
  Spot-checked 2026-10-26: goat roasted P 27.1 F 3.0; chicken breast
  roasted P 31.0 F 3.6. `foods.csv` stays first because it holds Japanese
  foods and unit sizes.

## Clock (2026-10-26)

- The clock is Vietnam time, where the learner lives until the move to
  Japan (~September 2027). Tokyo time had been assumed by mistake; it put
  anything logged after 22:00 local on the next day.
- Times in `Daily/` and `Learned/log/` before 2026-10-26 are Tokyo time:
  subtract 2 h for the learner's local time. They stay as written.
