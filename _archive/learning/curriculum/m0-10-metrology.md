# Metrology + Measurement Uncertainty (m0-10)

## Goal
- From `Mechatronics/ROADMAP.md` Phase 0: state measurement results honestly - `X ± U mm (k=2, ~95%)`, naming the instrument.
- Physical artifact: the Phase 0 Metrology Kit and its uncertainty log (feeds every later measurement, 0.10 -> 1.3 current sense -> 3.3 characterization).

## Map
- No bracket yet - this topic opens at first contact.
- Concepts are the milestone's own pass-condition topics; every one has a source before the lesson starts.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| m10-1 | caliper operation and zeroing (outside/inside/depth reads; gentle, consistent jaw force) | - | unknown | 0 | - | - |
| m10-2 | resolution vs accuracy vs precision (0.01 mm resolution but +/-0.03 mm accuracy) | m10-1 | unknown | 0 | - | - |
| m10-3 | repeatability statistics (10 readings, mean, std dev; Type A = s/sqrt(n)) | m10-2 | unknown | 0 | - | - |
| m10-4 | Type B instrument uncertainty (resolution/sqrt(12) + accuracy spec RSS) | m10-3 | unknown | 0 | - | - |
| m10-5 | combined uncertainty and reporting (RSS budget; X +/- U mm (k=2); name the instrument) | m10-4 | unknown | 0 | - | - |
| m10-6 | systematic vs random error (averaging fixes one, not the other) | m10-3 | unknown | 0 | - | - |
| m10-7 | dial indicator + environmental logging (flatness/runout, parallax discipline, ambient temperature) | m10-1 | unknown | 0 | - | - |

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
- Rests on: 0.2 (units and angles), Python plotting for the distributions; feeds every measurement after this
- Teaches: feeds 1.3 (current-sense characterization), 3.3 (Kt/Ke characterization with uncertainty), any reported result
- Lessons: -

## Log
- 2026-09-15 - file created for the Phase 0 foundational sourcing pass (plan §11). Concept rows from the milestone's pass conditions; standards pinned at section granularity by scout + verifier, verdicts dated 2026-09-15. Corrected the milestone's `Lenses` attribution for `dgmNBEEN3gM`: it is a Starrett product demo uploaded by A&M Industrial, not a Starrett channel. No reviews scheduled - rows stay `unknown` until taught.
