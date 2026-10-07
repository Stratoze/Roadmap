# Statics + FBDs + FEM Intuition (m0-4)

## Goal
- From `Mechatronics/ROADMAP.md` Phase 0: FBD of the 2-link arm holding 0.5 kg at full horizontal extension, and the holding torque at the shoulder joint.
- Feeds 0.5 (circuits is separate), but directly feeds 0.7 (stress = F/A) and 0.9 (torque and mechanical advantage).

## Map
- No bracket yet - this topic opens at first contact. Priors: 0.2 vectors are complete, so force components are available; no statics course.
- `[proposed]` topics from the tree relevant here: none - this file covers the milestone's own pass conditions.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| m4-1 | free body diagrams (isolate the body, label all forces, correct directions) | - | unknown | 0 | - | - |
| m4-2 | equilibrium equations (sum(F)=0 and sum(tau)=0 applied correctly) | m4-1 | unknown | 0 | - | - |
| m4-3 | torque and moment arm (tau = F x d-perp; the arm changes with angle) | m4-2 | unknown | 0 | - | - |
| m4-4 | reaction forces and geometric sensitivity (solve base reactions; predict torque change when the elbow extends) | m4-3 | unknown | 0 | - | - |
| m4-5 | FEM intuition (discretize -> element stiffness -> assemble -> BCs -> displacements -> stress; hand calc validates FEA) | m4-2 | unknown | 0 | - | - |
| m4-6 | FEA toolchain awareness (Solid Edge -> STEP -> PrePoMax/CalculiX pipeline) | m4-5 | unknown | 0 | - | - |

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
- Rests on: 0.2 (vectors - forces are vectors, and the arm geometry is the same 2-link arm)
- Teaches: feeds 0.7 (stress = F/A from an FBD), 0.9 (torque and mechanical advantage), 3.1 (hand calcs before FEA)
- Lessons: -

## Log
- 2026-09-15 - file created for the Phase 0 foundational sourcing pass (plan §11), then re-run book-first under §11b. Two corrections: a non-existent video citation removed, and the Shigley reference narrowed from "ch 3" to "§3-1". Baker & Haynes (free, beginner, full text) is the new primary read. m4-6 has no book - it is tool-level (PrePoMax/CalculiX), recorded as such. No reviews scheduled - rows stay `unknown` until taught.
