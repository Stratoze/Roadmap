# ODEs — orientation (exponential decay)

## Goal
- Scoping answer (2026-09-11): "oh, i want to be able to use it for EPIC stuff, but first let's say for the everyday stuff first, by when ? idk, probably as soon as possible but not like i know a realistic time line on this, and considering we are juggling like 20 subjects, probably a month for a good level ?"
- By when: ~1 month for a good level (learner's estimate, uncertain; pacing holds one strand at a time across the subject juggle)

## Map
- Provisional (2026-09-11): floor symbolic calculus chain both ways with limits + Euler step with run/rise picture; ceiling solving y'=-y (shape/method). Detail: `_system/learning/maps/overview.md`.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| c1 | ODE = unknown is a function; solve means find it, check by plugging in | - | review | 0 | 2026-09-26 | lesson 2026-09-22 (read cooling and dN/dt rules as rules of change) |
| c2 | Slope field = the rule drawn globally, one arrow per point | c1 | unknown | 0 | - | - |
| c3 | Solution curves thread the arrows; the initial point picks one | c2 | unknown | 0 | - | - |
| c4 | Euler chaining = walk the arrows; smaller steps hug the true curve | c3 | review | 0 | 2026-09-26 | lesson 2026-09-22 (wrote the Euler loop unaided; found the sign fix) |
| c5 | y' = ky means proportional rate, so exponential shape | c4 | review | 0 | 2026-09-26 | lesson 2026-09-22 (growth vs decay transfer check) |
| c6 | Rate constant sets timescale (1/abs(k), half-life) | c5 | review | 0 | 2026-09-26 | lesson 2026-09-22 (1/k settling: 7 / 13 / 152 min) |
| c7 | Equilibria plus stability on a phase line | c3 | review | 0 | 2026-09-26 | lesson 2026-09-22 (fixed point 50 stable; P=0 unstable) |
| c8 | Second order needs two starting values (spring preview) | c3 | unknown | 0 | - | - |
| c9 | Forcing/input as the control entry point (preview only) | c7 | unknown | 0 | - | - |

## Field scan (scout, 2026-09-11 — awaiting prune with learner)
- ODE = unknown is a function (solve = find it; check by differentiate-and-plug-in)
- Slope field as the rule-of-change picture (one short arrow per (t,y))
- Solution = curve threading the arrows; IC picks one
- Euler chaining = walk the arrows (smaller dt hugs the curve)
- y'=ky = proportional-rate shape (exponential, not polynomial)
- Rate constant sets timescale (1/|k|, half-life)
- Equilibria + 1D stability on a phase line
- Second order needs two states (y(0) and y'(0))
- Forcing/input as the control entry point (preview only)
- Deferred: separation/integrating factor, characteristic equation, Laplace, systems/matrix form, nonlinearity theorems

## Resources
- rigorous | Lecture 1: The Geometrical View of y'=f(x,y) | Prof. Arthur Mattuck, MIT OCW 18.03 | video: Lecture 1 | https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/resources/lecture-1-the-geometrical-view-of-y-f-x-y | for c1, c2, c3 | verified 2026-09-11
- rigorous | Euler's Method | MIT OCW 18.03SC | page: Euler's Method | https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/resources/eulers-method | for c4 | verified 2026-09-11
- rigorous | Exponential Growth and Decay (Calc Vol 2 §2.8) | OpenStax | book: §2.8 | https://openstax.org/books/calculus-volume-2/pages/2-8-exponential-growth-and-decay | for c5, c6 | verified 2026-09-11
- interactive | Slope field and Euler's Method | talljerome, GeoGebra | interactive: slope field/Euler | https://www.geogebra.org/m/yrvqthte | for c2, c4 | verified 2026-09-11

Historical alternatives and unverified decisions are in [[_system/learning/archive/source-ledger|source ledger]].
## Usage events
| date | event_id | concept/item_ref | event | evidence | public note |
|------|----------|------------------|-------|----------|-------------|

## Misconceptions
- 2026-09-11 - integrate-against-y: solved y'=-y by integrating -y over y (evidence: `_private/learning/verbatim/2026-09-11-map-r3.md`)
- 2026-09-22 - k read as a multiplier, not a rate: the per-step update `T -= k*gap` at dt=1 looks like "shrink by k", which pulled `dP/dt = 0.5P` into a decay reading ("halves toward 0"). The sign of k decides growth vs decay; the size sets only the timescale. (evidence: lesson 2026-09-22)
- 2026-09-22 - update sign inverted: `T -= const_change * gap` with `const_change = -0.07` added heat instead of removing it, and the loop never terminated. (evidence: lesson 2026-09-22)

## Problems
| id | problem | source | theory | attempts | status |
|----|---------|--------|--------|----------|--------|
| p1 | Cup at 90, room 20, loses 0.07 of the gap per minute - when does it first reach 60? | authored | rate rule, Euler step | 1 | solved (minute 8) |
| p2 | Does the cup ever reach room temperature exactly? | authored | fixed point, asymptote | 1 | solved (only T=20 steps to 20; T==20 never fires in double) |
| p3 | One 30-minute step with the slope frozen at the start | authored | step size, Euler instability | 1 | solved (T=-57; the method breaks, not the rule) |
| p4 | Read `dP/dt = 0.5P` - growth or decay, and what shape? | authored | sign of k, rate tied to P itself | 1 | attempted (read as decay; corrected) |
| p5 | Read `dN/dt = -0.3(N - 50)` - direction, fixed point, autonomy | authored | stable equilibrium, autonomous equation | 1 | solved |
| p6 | Change k from -0.3 to -0.03 - what changes, and by how much? | authored | rate constant sets timescale | 1 | solved (slower, ~10x: 13 to 152 min) |

## Links
- Rests on: calculus chain (derivative/integral, limits); Euler stepping picture
- Teaches: dynamics and control models downstream
- Lessons: [[_system/learning/lessons/math-odes/2026-09-22-cooling-rule-and-euler|2026-09-22 - cooling rule and Euler]]

## Log
- 2026-09-11 - topic opened from the strand-1 bracket; scoping pending; field scan + resource pipeline started.
- 2026-09-11 - scoping landed (everyday first, EPIC later, ~1 month); all nine aims kept as unknown rows; orientation opened video-first.
- 2026-09-22 - first study session. Cooling rule -> learner-written Euler loop (sign bug found by running it) -> gap form -> algebraic fixed point -> frozen 30-minute step diverging to -57 -> convergence table -> growth vs decay on `dP/dt = 0.5P` (misread, corrected) -> stable vs unstable equilibria on `dN/dt = -0.3(N - 50)`. c1, c4, c5, c6, c7 scheduled at rung 0; c2/c3/c8/c9 untouched. Lesson note written; verbatim captured to `_private/learning/verbatim/2026-09-22-odes-euler.md`.
