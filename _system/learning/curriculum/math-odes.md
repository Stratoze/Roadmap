# ODEs — orientation (exponential decay)

## Goal
- Scoping answer (2026-09-11): "oh, i want to be able to use it for EPIC stuff, but first let's say for the everyday stuff first, by when ? idk, probably as soon as possible but not like i know a realistic time line on this, and considering we are juggling like 20 subjects, probably a month for a good level ?"
- By when: ~1 month for a good level (learner's estimate, uncertain; pacing holds one strand at a time across the subject juggle)

## Map
- Provisional (2026-09-11): floor symbolic calculus chain both ways with limits + Euler step with run/rise picture; ceiling solving y'=-y (shape/method). Detail: `_system/learning/overview-map.md`.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| c1 | ODE = unknown is a function; solve means find it, check by plugging in | - | unknown | 0 | - | - |
| c2 | Slope field = the rule drawn globally, one arrow per point | c1 | unknown | 0 | - | - |
| c3 | Solution curves thread the arrows; the initial point picks one | c2 | unknown | 0 | - | - |
| c4 | Euler chaining = walk the arrows; smaller steps hug the true curve | c3 | unknown | 0 | - | - |
| c5 | y' = ky means proportional rate, so exponential shape | c4 | unknown | 0 | - | - |
| c6 | Rate constant sets timescale (1/abs(k), half-life) | c5 | unknown | 0 | - | - |
| c7 | Equilibria plus stability on a phase line | c3 | unknown | 0 | - | - |
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
- intuitive | Differential equations, studying the unsolvable | Grant Sanderson (3Blue1Brown) | https://www.3blue1brown.com/lessons/differential-equations | verified 2026-09-11
- intuitive | Differential equations introduction | Khan Academy | https://www.khanacademy.org/math/differential-equations/first-order-differential-equations/differential-equations-intro/v/differential-equation-introduction | unverified (stale URL path; migrated page exists, needs browser check)
- intuitive | Slope fields introduction | Khan Academy | https://www.khanacademy.org/math/ap-calculus-ab/ab-differential-equations-new/ab-7-3/v/creating-a-slope-field | unverified (fetch JS-walled; search-confirmed, needs browser check)
- intuitive | Euler's method | Khan Academy | https://www.khanacademy.org/math/differential-equations/first-order-differential-equations/eulers-method-tutorial/v/eulers-method | unverified (stale URL path + fetch wall; migrated page exists, needs browser check)
- intuitive | Worked example: Euler's method | Khan Academy | https://www.khanacademy.org/math/differential-equations/first-order-differential-equations/eulers-method-tutorial/v/example-eulers-method-exercise | unverified (stale URL path + fetch wall; migrated page exists, needs browser check)
- rigorous | Lecture 2: Euler's Numerical Method for y'=f(x,y) | Prof. Arthur Mattuck, MIT OCW 18.03 | https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/resources/lecture-2-eulers-numerical-method-for-y-f-x-y | verified 2026-09-11
- rigorous | Euler's Method | MIT OCW 18.03SC | https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/resources/eulers-method | verified 2026-09-11
- rigorous | Lecture 1: The Geometrical View of y'=f(x,y) | Prof. Arthur Mattuck, MIT OCW 18.03 | https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/resources/lecture-1-the-geometrical-view-of-y-f-x-y | verified 2026-09-11
- intuitive | Introduction to Differential Equations | Professor Leonard | https://www.youtube.com/watch?v=EWVSxND_iWA | verified 2026-09-11
- interactive | Isoclines | MIT Mathlets | https://mathlets.org/mathlets/isoclines | verified 2026-09-11
- interactive | Euler's Method | MIT Mathlets | https://mathlets.org/mathlets/eulers-method | verified 2026-09-11
- interactive | Slope field and Euler's Method | talljerome, GeoGebra | https://www.geogebra.org/m/yrvqthte | verified 2026-09-11
- reference | Definitions + Direction Fields | Paul Dawkins, Paul's Online Math Notes | https://tutorial.math.lamar.edu/classes/de/definitions.aspx | verified 2026-09-11
- rigorous | Exponential Growth and Decay (Calc Vol 2 §2.8) | OpenStax | https://openstax.org/books/calculus-volume-2/pages/2-8-exponential-growth-and-decay | verified 2026-09-11
- reference | Exponential growth and decay: a differential equation | Math Insight (UMN) | https://mathinsight.org/exponential_growth_decay_differential_equation_refresher | verified 2026-09-11

## Misconceptions
- 2026-09-11 - integrate-against-y: solved y'=-y by integrating -y over y (evidence: `_private/learning/verbatim/2026-09-11-map-r3.md`)

## Problems
| id | problem | source | theory | attempts | status |
|----|---------|--------|--------|----------|--------|

## Links
- Rests on: calculus chain (derivative/integral, limits); Euler stepping picture
- Teaches: dynamics and control models downstream
- Lessons: -

## Log
- 2026-09-11 - topic opened from the strand-1 bracket; scoping pending; field scan + resource pipeline started.
- 2026-09-11 - scoping landed (everyday first, EPIC later, ~1 month); all nine aims kept as unknown rows; orientation opened video-first.
