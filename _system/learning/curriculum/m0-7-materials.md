# Materials, Failure, and Selection (m0-7)

## Goal
- From `Mechatronics/ROADMAP.md` Phase 0: select a material for a given load/environment using Ashby reasoning, and read a failure honestly.
- Feeds 3.1 (QDD actuator sizing, machine elements) and every FoS decision after this.

## Map
- No bracket yet - this topic opens at first contact.
- Concepts are the milestone's own pass-condition topics; every one has a source before the lesson starts.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| m7-1 | stress, allowable stress, FoS (sigma = F/A; allowable = yield/FoS; why FoS > 1) | - | unknown | 0 | - | - |
| m7-2 | stress-strain curve anatomy (elastic slope E, 0.2% offset yield, strain hardening, UTS, necking, fracture) | m7-1 | unknown | 0 | - | - |
| m7-3 | crystal structure and dislocations (FCC/BCC/HCP slip; work hardening; why Al bends and cast iron snaps) | m7-2 | unknown | 0 | - | - |
| m7-4 | strength vs toughness vs hardness (match to static/impact/fatigue loading) | m7-2 | unknown | 0 | - | - |
| m7-5 | fatigue (S-N curve, endurance limit; cyclic failure below yield) | m7-2 | unknown | 0 | - | - |
| m7-6 | tempers, polymers, corrosion (6061-T6 vs -O; PLA/PETG/nylon creep; galvanic Al+steel) | m7-3 | unknown | 0 | - | - |
| m7-7 | Ashby selection reasoning (plot E/rho vs sigma_y/rho; pick a stiff-light arm link) | m7-2 | unknown | 0 | - | - |
| m7-8 | failure analysis + design constraints (fracture surfaces; wear, stress concentration, coatings) | m7-5 | unknown | 0 | - | - |

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
- Rests on: 0.4 (statics - stress is force over area from an FBD)
- Teaches: feeds 3.1 (actuator sizing, bearing life, shaft design), 0.9 (testbed materials and PLA wear)
- Lessons: -

## Log
- 2026-09-15 - file created for the Phase 0 foundational sourcing pass (plan §11). Replaced the milestone's MatWeb interactive with Cambridge DoITPoMS (MatWeb 403s to automated fetch and verifies no named datasheet). No reviews scheduled - rows stay `unknown` until taught.
