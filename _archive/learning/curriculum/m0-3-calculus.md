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

## Resources

Active source selected JIT through the `resources` skill when the concept activates. Historical candidates and verification decisions are in [[_system/learning/archive/source-ledger|source ledger]].

## Usage events
| date | event_id | concept/item_ref | event | evidence | public note |
|------|----------|------------------|-------|----------|-------------|

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
