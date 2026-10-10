# NEXT

No dates. Work top-down, tick [x] when done, never redo a ticked item.
When a list runs out, Claude writes the next 50. What I've learned lives in `Learned/`.

**Every day:** 25 min Japanese (CJ ~5 episodes + next grammar point) + 25 min technical (next items). Japanese first.
Also: Tadoku level 0, one story aloud twice a week · katakana deck 5 min/day until fluent · Kaishi reviews only after both floors (cap 100, never counted).

## Handoff (overwrite each session; last: 2026-10-10 10:36 JST)

Next session, in this order:
1. **Technical:** item 7 (blank page, v = 4t² + t). Today's technical was 10:12–10:36 ≈ 24 min, 1 min short of the floor.
2. **Japanese lesson:** grammar item 4, は vs が. Learner reads Tofugu's は/が article first (https://www.tofugu.com/japanese-grammar/), Claude then quizzes; open with one Japanese line.
3. **Immersion:** learner reports today's CJ minutes (~5 episodes planned on the bus). Then Claude writes `Daily/2026-10-10.md` (JP lesson ≈ 09:41–09:49 + ます practice; Japanese chat ≈ 10:41–10:55; technical ≈ 24 min, items 3–6).
Pending: photo of the FK drawing for `Mechatronics/portfolio/0.3-2link-fk-tip.md`. Tue 10/13: run `tools/check_progress.py` on the PC.

## Technical (60)

0.3 Calculus intuition
- [x] 1. Euler loop matches the hand table
- [x] 2. 2-link tip: predicted vs measured, 3 sentences (photo pending)
- [x] 3. MVM: derivative of a polynomial: v(t) = 2t → a(t); p(t) = t³ − 2t → p'(t), p''(t)
- [x] 4. MVM: integrate with limits: position at t = 3 s from v(t) = 2t, x(0) = 0 (units)
- [x] 5. MVM: chain position → velocity → acceleration and back on those two items
- [x] 6. MVM: explain derivative = rate of change, integral = accumulation (formula allowed)
- [ ] 7. Full (blank page): same chain on a new item, v(t) = 4t² + t
- [ ] 8. Full: power → energy, P(t) = 6t W from 0 to 2 s, answer in joules
- [ ] 9. Full: explain why area under v(t) is displacement, no formula

0.4 Statics + free-body diagrams
- [ ] 10. FBD: book resting on a table (every force, arrow, label)
- [ ] 11. FBD: book pushed sideways but not sliding
- [ ] 12. FBD: one link held horizontal by a hand at one end
- [ ] 13. Predict, then compute: torque of a 1 N force at 0.1 m, at 90°
- [ ] 14. Same force at 45° and 0°: predict which is bigger, then compute
- [ ] 15. Moment arm in plain words: draw it for item 14
- [ ] 16. Torque of a link's own weight about the shoulder (weight at the middle)
- [ ] 17. That torque at link angles 0°, 45°, 90°: predict, then compute
- [ ] 18. Equilibrium: two forces on a seesaw, find the missing one
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

## Japanese grammar (50, one new point per lesson, then practice)

- [x] 1. に (point) / で (stage, tool) / を
- [x] 2. Counters 冊 / 本 / 台, [noun]を[count][verb]
- [x] 3. ます / ました / ません / ませんでした
- [ ] 4. は vs が
- [ ] 5. あります / います
- [ ] 6. これ / それ / あれ / どれ
- [ ] 7. ここ / そこ / あそこ / どこ
- [ ] 8. の (my, the teacher's)
- [ ] 9. も (also)
- [ ] 10. と (and, with)
- [ ] 11. や (and so on)
- [ ] 12. へ vs に
- [ ] 13. に for time (３時に)
- [ ] 14. 時 / 分, telling time
- [ ] 15. 曜日, days of the week
- [ ] 16. Counter つ (ひとつ, ふたつ)
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
