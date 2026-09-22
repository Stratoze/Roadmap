# 2026-09-22 — cooling rule, Euler's method, growth vs decay

Topic: [[math-odes]] · Theory: calculus chain (derivative as slope, rise/run) ·
Previous lesson: none (first note for this topic)

## Target
Read a differential equation as a rule of change, and walk it forward by hand.
Orientation for ODEs, aims c1 and c4–c7.

## Predict (summary)
The learner's first reading of the cup rule produced a working loop, but with the
update sign inverted — it heated instead of cooled. On `dP/dt = 0.5P` the first
reading was "the rate is half of P, so it halves toward 0" — decay, not growth.

## Orientation
Video-first per standing order 5. Offered 3Blue1Brown "Differential equations,
studying the unsolvable", the Isoclines mathlet, and Mattuck 18.03 L1 as the
rigorous pass. Learner chose 3Blue1Brown over Professor Leonard (intuitive lens
first). Learner then reported the video did not answer "what a differential
equation is" — orientation was re-pitched in plain words from the rule itself.

## Attempts
- **Cooling problem** (cup 90, room 20, k = 0.07/min, target 60). Learner wrote
  the update loop unaided — gap, update, clock, stop condition. Sign error:
  `T -= const_change * gap` with `const_change = -0.07` added heat. Run
  confirmed climbing 90 → 140.3 over 8 minutes, `while T > 60` never false.
- **Corrected** to `T += const_change * gap`: crossing at minute 8, T = 59.171.
- **"Does T ever reach 20?"** solved algebraically by the learner:
  `20 = T - 0.07(T - 20)` gives T = 20, so only 20 steps to 20. The learner's
  proposed simulation check (`T == 20` / `T < 20`) fires neither branch — the
  loop stalls at T = 20.000000000000025 near minute 490.
- **30-minute batching**: learner took 30 one-minute steps and printed once (not
  a single coarse step), then found the delta/gap ratio constant at −0.88663.
- **Single frozen 30-minute step**: −4.9 × 30 = −147 → T = −57. The learner's
  objection ("I don't think that's how it works") was the correct physical read;
  the method was broken, not the rule.
- **Convergence** at t = 8: dt 1 → 0.0001 gave error −8.1e-01 → −7.8e-05; each
  10× smaller step cut the error 10×.
- **Transfer, `dP/dt = 0.5P`**: first read as decay toward 0; corrected —
  positive k grows, the rate is tied to P itself, P = 0 is unstable both sides.
- **Transfer, `dN/dt = -0.3(N - 50)`**: correct on every count — fixed point at
  50, attracting from both sides, distance sets speed, and with no explicit t on
  the right the point cannot move (autonomous).

## Feedback
- The sign of k decides growth versus decay; the magnitude sets the timescale.
  Settling to within 0.5 of the target took minute 7 / 13 / 152 for
  k = 1.5 / 0.3 / 0.03 — tracking 1/k.
- With dt = 1 the discrete update looks like a multiplier ("shrink by 7%"),
  which is what pulled the reading toward "shrink" and away from "rate".
- An e was introduced without derivation; learner rejected it and was right —
  separation of variables is deferred by the plan, so the closed form should not
  have appeared.
- Learner's closing read: k is "just a constant... nothing interesting". Half
  right — it changes nothing about the shape, everything about the clock.

## Reflection (summary)
The learner challenged the session directly ("not sure i learnt anything"),
arguing that the skills exercised were pre-existing. The objection was accepted
as correct. The blank-page test was then changed to a rule the learner had not
seen, which exposed a real gap (growth versus decay) that the loop-writing had
hidden. The learner also corrected the agent twice: a misattributed number
(0.1134 was the agent's, not theirs) and the undelivered derivation of e.

## Confidence
Not collected. `_private/` **is** cloned and healthy — the earlier "paused"
claim was an agent error, not a blocker. The real reason is a process miss:
confidence bands were never asked this session. Verbatim for 2026-09-22 was
written after the fact from the session transcript to
`_private/learning/verbatim/2026-09-22-odes-euler.md`.

## Links
- Topic: [[math-odes]]
- Theory: calculus chain — derivative as slope, rise/run; links forward to
  dynamics and control models downstream
- Problems: p1 cup cooling, p2 fixed point, p3 frozen step, p4 growth vs decay,
  p5 stable equilibrium, p6 timescale
- Previous lesson: none

## Next
Closed form for proportional-rate rules — where `e^-kt` and the 0.1225 come
from. Needs separation of variables, deferred by the plan; a fresh arc, not an
add-on.
