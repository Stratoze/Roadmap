# Mechanisms & Kinematic Elements + Physical Testbed (m0-9)

## Goal
- From `Mechatronics/ROADMAP.md` Phase 0: for each of 12 mechanisms, give the kinematic diagram, DOF via Gruebler's, input->output motion, mechanical advantage behavior, and one real-world application.
- Physical artifact: the **Parametric Mechanism Testbed** - the first portfolio artifact. Must be photographed and labeled, not left as a pile of parts.

## Map
- No bracket yet - this topic opens at first contact.
- Concepts are the milestone's own pass-condition topics; every one has a source before the lesson starts.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| m9-1 | kinematic diagrams + motion vocabulary (links/joints/symbols; state input -> output; mechanism vs machine) | - | unknown | 0 | - | - |
| m9-2 | Gruebler's equation (DOF = 3(n-1) - 2j1 - j2; count inputs for planar mechanisms) | m9-1 | unknown | 0 | - | - |
| m9-3 | four-bar linkage + Grashof (s + l <= p + q; crank-rocker families; dead centers and flywheel) | m9-2 | unknown | 0 | - | - |
| m9-4 | cam and follower (profile IS the motion program; pressure angle; undercutting) | m9-1 | unknown | 0 | - | - |
| m9-5 | intermittent mechanisms (Geneva dwell/entry jerk, ratchet and pawl, Scotch yoke) | m9-2 | unknown | 0 | - | - |
| m9-6 | couplings and compliance (Oldham, U-joint ripple + double Cardan, leaf spring as designed compliance) | m9-1 | unknown | 0 | - | - |
| m9-7 | power transmission and backdrivability (planetary ratios; ball vs lead screw efficiency/self-locking; belts/chains) | m9-1 | unknown | 0 | - | - |
| m9-8 | testbed fabrication + print tolerance (calibration cube, hole clearance, hand-swap modules, PLA wear logging) | m9-3, m9-6 | unknown | 0 | - | - |

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
- Rests on: 0.2 (vectors and frames - joint angles are vector directions), 0.4 (torque and moment arm for mechanical advantage)
- Teaches: feeds 3.1 (machine elements and QDD actuator design), 4.5 (gripper linkage), the testbed's kinematic diagrams feed every later mechanism decision
- Lessons: -

## Log
- 2026-09-15 - file created for the Phase 0 foundational sourcing pass (plan §11). **Corrected a live vault error**: the existing `Lenses - m0-9` line attributed playlist `PLHGVjZ_tV_gwDwoV_0CX7QguS_Vkx2yzV` to thang010146; oEmbed returns "Mechanical Models" by **Proto G Engineering**. That line is now marked `unverified` with the real attribution, and a verified thang010146 channel link was added alongside it. Norton ch 2/3/8/9 verified from the author's official TOC PDF. No reviews scheduled - rows stay `unknown` until taught.
