# NEXT

No dates. Work top-down, tick [x] when done, never redo a ticked item.
When a list runs out, Claude writes the next 50. What I've learned lives in `Learned/`.

**Every day:** 25 min Japanese (CJ ~5 episodes + next grammar point + Japanese chat) + 25 min technical (next items). Japanese first.
Japanese is the priority, all of it before technical. Free day: CJ 40, grammar up to 3 points, Kaishi 20 min, chat ~25. Tight day (Mon/Thu/Sun): CJ 25, 1 point, Kaishi 10 min, chat ≥5 replies. Grammar: read the point on Tofugu (else Cure Dolly / yoku.bi / Imabi), then Haiku quizzes. Chat: Haiku gives the prompt, chat in a free chat service, paste it back for logging.
Also: Tadoku level 0, one story aloud twice a week · katakana deck 5 min/day until fluent · Kaishi: review the backlog by time (20 min free day, 10 tight), after the grammar quiz; no new cards until under 100 due (AGENTS.md).

## Handoff
Current (Opus 2026-10-21): no open handoff. WEEK.md now runs 10-21 to 11-01 with keys A12-A26, T10-T28, S1-S4. Resolved today: quiz scoring (AGENTS.md "Grammar pace"; 11 や passed on re-score; a clear-word typo is not counted); jp-chat template (kanji with readings, no English glosses, real back-and-forth); the 10-19 and 10-20 "check on Sunday" lines (Learned/japanese.md).
Earlier decisions, kept for the reasons:
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

The day-by-day plan lives in `WEEK.md` (Opus rewrites it each Sunday). Start there.
Pending: photo of the FK drawing for `Mechatronics/portfolio/0.3-2link-fk-tip.md`.

## Technical (60 + S1-S4 + M1-M4)

0.3 Calculus intuition
- [x] 1. Euler loop matches the hand table
- [x] 2. 2-link tip: predicted vs measured, 3 sentences (photo pending)
- [x] 3. MVM: derivative of a polynomial: v(t) = 2t → a(t); p(t) = t³ − 2t → p'(t), p''(t)
- [x] 4. MVM: integrate with limits: position at t = 3 s from v(t) = 2t, x(0) = 0 (units)
- [x] 5. MVM: chain position → velocity → acceleration and back on those two items
- [x] 6. MVM: explain derivative = rate of change, integral = accumulation (formula allowed)
- [x] 7. Full (blank page): same chain on a new item, v(t) = 4t² + t
- [x] 8. Full: power → energy, P(t) = 6t W from 0 to 2 s, answer in joules
- [x] 9. Full: explain why area under v(t) is displacement, no formula

0.4 Statics + free-body diagrams
- [ ] 10. FBD: book resting on a table (every force, arrow, label)
- [ ] 11. FBD: book pushed sideways but not sliding
- [ ] 12. FBD: one link held horizontal by a hand at one end
- [x] 13. Predict, then compute: torque of a 1 N force at 0.1 m, at 90°
- [x] 14. Same force at 45° and 0°: predict which is bigger, then compute
- [ ] 15. Moment arm in plain words: draw it for item 14
- [x] 16. Torque of a link's own weight about the shoulder (weight at the middle)
- [x] 17. That torque at link angles 0°, 45°, 90°: predict, then compute
- [x] 18. Equilibrium: two forces on a seesaw, find the missing one
- [ ] 19. Equilibrium: link held by a hand force, solve for the force
- [ ] 20. 2-link straight out: shoulder torque from both link weights
- [ ] 21. Same arm: elbow torque
- [ ] 22. Add a 50 g weight at the tip: new shoulder and elbow torques
- [ ] 23. Measure: ruler + weight balanced on a pencil, check one torque, 3 sentences
- [ ] 24. List every assumption you made in items 16-23
- [ ] 25. FEM in plain words: what it does and why hand calcs check it
- [ ] 26. 0.4 deliverable: FBD of the 2-link arm holding 0.5 kg at full horizontal extension, shoulder holding torque with units
- [ ] 27. 0.4 Full: what happens to shoulder torque if the elbow extends further
- [ ] 28. 0.4 Full: reaction forces at the base

0.4s Statistics for measurement (added by Opus 2026-10-17, learner's ML/statistics proposal; keys come with the Sunday plan)
- [ ] S1. Measure one length 10 times with a ruler: mean and range, with units
- [ ] S2. Standard deviation of those 10 by hand; what it means in plain words
- [ ] S3. Item 2's tip: is predicted − measured bigger than the spread? Say what that tells you
- [ ] S4. Same mean and standard deviation in Python (numpy); match the hand numbers

0.5 Circuits basics
- [ ] 29. Ohm's law: predict current for 5 V across 1 kΩ, then compute
- [ ] 30. LED + resistor on 5 V: pick the resistor from a datasheet's forward voltage
- [ ] 31. Two resistors in series: predict total, then compute
- [ ] 32. Two in parallel: predict total, then compute
- [ ] 33. Voltage divider: predict the middle voltage
- [ ] 34. KVL in plain words: walk around one loop and add the voltages
- [ ] 35. KCL in plain words: currents into a node
- [ ] 36. Read one datasheet: find max current and max voltage of a part
- [ ] 37. Multimeter: measure a resistor, compare to its color code
- [ ] 38. Build the LED circuit, measure current, 3 sentences
- [ ] 39. Build the divider, measure the middle voltage, 3 sentences
- [ ] 40. Potentiometer as a divider: predict voltage at 3 knob positions
- [ ] 41. Measure those 3 positions, 3 sentences
- [ ] 42. Arduino analogRead: predict the number for 2.5 V
- [ ] 43. Read a pot with analogRead, compare to prediction

0.5m First machine learning: calibration (added by Opus 2026-10-17)
- [ ] M1. Record 6 pairs (knob angle, analogRead number); plot them
- [ ] M2. Fit a straight line by least squares in Python on 5 pairs; predict the 6th, compare
- [ ] M3. Plain words: why this fit is a machine learning model; what the training data and the test point were
- [ ] M4. The fit's error vs the spread from S2: is the model good enough for the arm?

0.6 Power + thermal
- [ ] 44. P = VI: power of the LED circuit, predict then compute
- [ ] 45. Power in the resistor (I²R) vs the LED
- [ ] 46. Power budget: Arduino + 2 pots + LED from USB 5 V
- [ ] 47. Efficiency in plain words, one example
- [ ] 48. Thermal resistance in plain words: why parts get hot
- [ ] 49. Temperature rise of a resistor from its datasheet
- [ ] 50. Feel-check: which part warms up, and does it match the prediction
- [ ] 51. Write the 0.6 three sentences

0.7 Materials + failure
- [ ] 52. Stress = force / area: predict, then compute for a wire
- [ ] 53. Strain in plain words; stretch a rubber band, measure
- [ ] 54. Stress-strain curve: sketch one, label the regions
- [ ] 55. Factor of safety: choose one for a cardboard link
- [ ] 56. Cardboard vs wood vs aluminum for the arm link: compare 3 properties
- [ ] 57. Fatigue in plain words: bend a paperclip until it breaks, count
- [ ] 58. Predict where the cardboard link would fail under the tip weight
- [ ] 59. Test it, 3 sentences
- [ ] 60. Pick the capstone link material and write why

## Japanese grammar (50, one point per lesson; pace in AGENTS.md "Grammar pace")

- [x] 1. に (point) / で (stage, tool) / を
- [x] 2. Counters 冊 / 本 / 台, [noun]を[count][verb]
- [x] 3. ます / ました / ません / ませんでした
- [x] 4. は vs が
- [x] 5. あります / います
- [x] 6. これ / それ / あれ / どれ
- [x] 7. ここ / そこ / あそこ / どこ
- [x] 8. の (my, the teacher's)
- [x] 9. も (also)
- [x] 10. と (and, with)
- [x] 11. や (and so on)
- [x] 12. へ vs に
- [ ] 13. に for time (３時に)
- [ ] 14. 時 / 分, telling time
- [ ] 15. 曜日, days of the week
- [x] 16. Counter つ (ひとつ, ふたつ)
- [ ] 17. Counter 人 (ひとり, ふたり)
- [ ] 18. い-adjectives: たかい / たかくない
- [ ] 19. い-adjectives past: たかかった / たかくなかった
- [ ] 20. な-adjectives: しずかです / しずかじゃないです
- [ ] 21. Adjective + noun (たかい山, しずかな町)
- [ ] 22. ～ましょう / ～ましょうか
- [ ] 23. ～ませんか (invitation)
- [ ] 24. ～たい (want to)
- [ ] 25. から (because) / から・まで (from, until)
- [ ] 26. もう / まだ
- [ ] 27. Dictionary form (plain present)
- [ ] 28. て-form: making it
- [ ] 29. ～てください
- [ ] 30. ～ています (doing now)
- [ ] 31. ～ています (state: 住んでいます)
- [ ] 32. ～てもいいです
- [ ] 33. ～てはいけません
- [ ] 34. ～て, ～て (linking actions)
- [ ] 35. ない-form
- [ ] 36. ～ないでください
- [ ] 37. た-form (plain past)
- [ ] 38. ～たことがあります
- [ ] 39. Plain speech: だ / だった
- [ ] 40. ～と思います
- [ ] 41. ～と言いました
- [ ] 42. ～前に / ～た後で
- [ ] 43. ～とき
- [ ] 44. ～ので / ～けど
- [ ] 45. より / ほど, comparing two things
- [ ] 46. 一番 (the most)
- [ ] 47. ～なる (become)
- [ ] 48. Potential form (読める, 行ける)
- [ ] 49. あげる / くれる / もらう
- [ ] 50. Question word + か / も (なにか, だれも)
