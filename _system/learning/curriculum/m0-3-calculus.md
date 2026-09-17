# Calculus Intuition (m0-3)

## Goal
- From `Mechatronics/ROADMAP.md` Phase 0: given v(t) = 2t m/s with x(0) = 0, derive acceleration, calculate position at t = 3 s by integration, and explain the physical meaning of the area under the curve in words.
- This is the next milestone in sequence (0.1 and 0.2 complete); the Full Pass bar bans the formula, so the *intuition* is the deliverable.

## Map
- No bracket yet - this topic opens at first contact. Priors: 0.1 and 0.2 are complete, so algebraic fluency and vector reasoning are assumed.
- Concepts are the milestone's own pass-condition topics; every one has a source before the lesson starts.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| m3-1 | derivative as rate of change (differentiate polynomials; read v(t) as slope of x(t)) | - | unknown | 0 | - | - |
| m3-2 | integral as accumulation (integrate polynomials with limits; area under curve) | m3-1 | unknown | 0 | - | - |
| m3-3 | kinematic chain both ways (position -> velocity -> acceleration and back on polynomials) | m3-2 | unknown | 0 | - | - |
| m3-4 | area under v(t) is displacement (explain in words without the formula) | m3-2 | unknown | 0 | - | - |
| m3-5 | power -> energy by integration (P(t) = 6t W over 0..2 s) | m3-2 | unknown | 0 | - | - |
| m3-6 | continuous intuition for discrete controllers (know when a discrete approximation is valid) | m3-2 | unknown | 0 | - | - |

## Sources
- rigorous | Calculus Volume 1 (OpenStax) | Strang, Herman et al. | book: ch 3 §3.4 "Derivatives as Rates of Change" | https://openstax.org/books/calculus-volume-1/pages/3-4-derivatives-as-rates-of-change | for m3-1, m3-2 | verified 2026-09-15
- rigorous | Calculus Volume 1 (OpenStax) | Strang, Herman et al. | book: ch 5 §5.1 "Approximating Areas" | https://openstax.org/books/calculus-volume-1/pages/5-1-approximating-areas | for m3-2, m3-4 | verified 2026-09-15
- rigorous | Calculus Volume 1 (OpenStax) | Strang, Herman et al. | book: ch 5 §5.4 "Integration Formulas and the Net Change Theorem" | https://openstax.org/books/calculus-volume-1/pages/5-4-integration-formulas-and-the-net-change-theorem | for m3-2, m3-3, m3-4, m3-5 | verified 2026-09-15
- rigorous | Calculus Volume 1 (OpenStax) | Strang, Herman et al. | book: ch 4 §4.10 "Antiderivatives" | https://openstax.org/books/calculus-volume-1/pages/4-10-antiderivatives | for m3-3 | verified 2026-09-15
- rigorous | Calculus Volume 1 (OpenStax) | Strang, Herman et al. | book: ch 6 §6.5 "Physical Applications" | https://openstax.org/books/calculus-volume-1/pages/6-5-physical-applications | for m3-5 | verified 2026-09-15
- reference | University Physics Volume 1 (OpenStax) | Moebs, Ling, Sanny | book: ch 7 §7.4 "Power" | https://openstax.org/books/university-physics-volume-1/pages/7-4-power | for m3-5 | verified 2026-09-15
- intuitive | Essence of Calculus ch 2 "The paradox of the derivative" | 3Blue1Brown (Grant Sanderson) | video | https://www.youtube.com/watch?v=9vKqVkMQHKk | for m3-1 | verified 2026-09-15
- intuitive | Essence of Calculus ch 8 "Integration and the fundamental theorem of calculus" | 3Blue1Brown | video | https://www.youtube.com/watch?v=rfG8ce4nNh0 | for m3-2, m3-4 | verified 2026-09-15
- intuitive | Essence of Calculus ch 10 "Higher order derivatives" | 3Blue1Brown | video | https://www.youtube.com/watch?v=BLkz5LGWihw | for m3-3 | verified 2026-09-15
- intuitive | Calculus, Better Explained - lesson 10 "The Theory of Derivatives" | Kalid Azad | book: lesson 10 | https://betterexplained.com/calculus/lesson-10/ | for m3-1, m3-6 | verified 2026-09-15
- intuitive | Calculus, Better Explained - lesson 11 "The Fundamental Theorem Of Calculus" | Kalid Azad | book: lesson 11 | https://betterexplained.com/calculus/lesson-11/ | for m3-1, m3-2, m3-3, m3-4 | verified 2026-09-15
- interactive | 18.01SC Single Variable Calculus - Mathlets ("Secant Approximation", "Tangent Approximation") | MIT OpenCourseWare (Prof. David Jerison) | interactive: secantApproximation | https://ocw.mit.edu/ans7870/18/18.01SC/f10/mathlets/secantApproximation.html | for m3-1, m3-6 | verified 2026-09-15
- interactive | 18.01SC Unit 3 Part A "Definition of the Definite Integral and First Fundamental Theorem" (Sessions 44-48) | MIT OpenCourseWare | page: unit-3/part-a | https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-3-the-definite-integral-and-its-applications/part-a-definition-of-the-definite-integral-and-first-fundamental-theorem/ | for m3-2, m3-4 | verified 2026-09-15
- interactive | Desmos Graphing Calculator | Desmos Studio PBC | interactive: calculator | https://www.desmos.com/calculator | for m3-2, m3-5 | verified 2026-09-15

Correction logged: the milestone previously said "No textbook required - video + doing is the whole theory here." That is dropped. The net-change theorem is the theory this milestone rests on, and OpenStax *Calculus Volume 1* §5.4 is where it lives. Also: the old `Visual:` line pointed at *Essence of Calculus* ch 1-3, which contains no integration; ch 8 (integration/FTC) and ch 10 (higher-order derivatives) are the episodes m3-2/m3-3 actually need.

No source found: **m3-6** has no published treatment of "when a discrete approximation of a continuous controller is valid". Closest verified material is BetterExplained lesson 10 (discrete step vs ideal continuous derivative) plus the MIT mathlet (secant -> tangent limit). A controls-specific anchor was not fetch-verifiable (Franklin/Powell *Feedback Control of Dynamic Systems* TOC pages 404'd; Astrom & Murray *Feedback Systems* refused connections) - both stay uncited rather than guessed. Re-run sourcing when 2.2 (discrete PID) makes this load-bearing.

## Misconceptions
-

## Problems
| id | problem | source | theory | attempts | status |
|----|---------|--------|--------|----------|--------|
| - | - | - | - | - | - |

## Links
- Rests on: 0.1 (Fermi estimation, binary-search debugging), 0.2 (vectors - velocity is a vector)
- Teaches: feeds 1.4 (pendulum equation of motion and solve_ivp), 2.2 (discrete PID and sampling time), 2.5 (Lagrangian dynamics)
- Lessons: -

## Log
- 2026-09-15 - file created for the Phase 0 foundational sourcing pass (plan §11). Two corrections to the milestone's own resource block: the "no textbook required" claim is replaced by the OpenStax net-change anchor, and the `Visual:` line is re-pointed from *Essence of Calculus* ch 1-3 to ch 8 + ch 10 (ch 1-3 has no integration). m3-6 carries an explicit no-source-found note. No reviews scheduled - rows stay `unknown` until taught.
