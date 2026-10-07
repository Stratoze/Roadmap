# Vectors, Trig, Frames of Reference (m0-2)

## Goal
- From `Mechatronics/ROADMAP.md` Phase 0: hand-calculate forward kinematics for a 2-link planar arm - given link lengths and joint angles, find the tip X, Y.
- Already complete (MVM + Full Pass, tested 2026-08-21) - this file holds the concept aims and a JIT source pointer; the historical verification record is in [[_system/learning/archive/source-ledger|source ledger]]. It is not to be re-taught.

## Map
- Pre-system topic: opens through **intake** (compressed cold verify per concept), never a full re-teach (standing order 3).
- Status: complete in [[Mechatronics/ROADMAP|the ROADMAP]]; concept rows remain intake placeholders and are not a claim of missing knowledge.
- Gate record: pre-system intake; MVM/Full Pass history and evidence live in the milestone evidence record, so it is not silently re-assessed.
- Bracket floor (from the evidence file, 2026-08-21): converted theta2 to world frame instead of plugging in 60 deg - frame reasoning was present before the system.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| m2-1 | vector addition and components (each link is a vector; the second link's base moves with the first) | - | unknown | 0 | - | - |
| m2-2 | 2-link planar forward kinematics (derive tip X,Y by hand from theta1, theta2, L1, L2) | m2-1 | unknown | 0 | - | - |
| m2-3 | vector diagram literacy (draw the diagram before plugging into formulas) | m2-1 | unknown | 0 | - | - |
| m2-4 | world vs link frames (express a point in either frame; rotate the base; add a third link) | m2-2 | unknown | 0 | - | - |
| m2-5 | radians vs degrees (silent code bug; everything in software is radians) | m2-1 | unknown | 0 | - | - |
| m2-6 | atan2 vs atan (quadrant ranges; robotics always uses atan2(y, x)) | m2-5 | unknown | 0 | - | - |
| m2-7 | dot product as projection (physical meaning; angle between vectors) | m2-1 | unknown | 0 | - | - |

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
- Rests on: 0.1 (binary-search debugging, I/O framing)
- Teaches: feeds 0.4 (statics of the same 2-link arm), 2.5 (multi-DOF dynamics), 4.2 (IK - the inverse of this FK)
- Lessons: -

## Log
- 2026-09-15 - file created for the Phase 0 foundational sourcing pass (plan §11). Concept rows from the milestone's pass conditions; every id has at least one verified locator - no gaps. Craig ch 2 was named in the milestone's own prose and independently TOC-verified (3rd ed.). No reviews scheduled - intake only.
