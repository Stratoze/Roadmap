# Power, Efficiency, Thermal (m0-6)

## Goal
- From `Mechatronics/ROADMAP.md` Phase 0: H-bridge at 2 A, 12 V, Rds(on) = 0.05 ohm, two switches in series - calculate input power, heat loss, efficiency (conduction losses only; switching and gate-drive losses return in 1.3/2.3), and decide whether a heatsink is needed.
- Single most useful artifact for this milestone is **not a book**: TI's DRV8874 datasheet is a real H-bridge in this exact regime and states the conduction-loss formula, the Rds(on)-vs-temperature caveat, the full Rth chain, and peak-vs-continuous current in one PDF.

## Map
- No bracket yet - this topic opens at first contact. Priors: 0.5 (Ohm, KVL/KCL) is the direct prerequisite.
- Concepts are the milestone's own pass-condition topics.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| m6-1 | power and conduction loss (P_in = V*I, P_loss = I^2 R; H-bridge efficiency at 2 A, 12 V, Rds 0.05 ohm) | - | unknown | 0 | - | - |
| m6-2 | thermal resistance chain (Rth_j-c + Rth_c-hs + Rth_hs-amb; junction temperature estimate) | m6-1 | unknown | 0 | - | - |
| m6-3 | Rds(on) temperature dependence (25 C datasheet value can double at 150 C) | m6-1 | unknown | 0 | - | - |
| m6-4 | system power budget (rails, loads per mode, peak vs nominal, fuse/regulator margin) | m6-2 | unknown | 0 | - | - |
| m6-5 | efficiency scope (conversion-stage efficiency is not system or motor efficiency) | m6-1 | unknown | 0 | - | - |

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
- Rests on: 0.5 (Ohm's law, KVL, and the LED resistor problem is the same arithmetic)
- Teaches: feeds 1.3 (H-bridge build, current-sense front end, PWM frequency trade), 3.2 (48 V rail, buck efficiency, trace widths, FET temperature), 4.3 (DC-rated contactor and fuse sizing)
- Lessons: -

## Log
- 2026-09-15 - file created for the Phase 0 foundational sourcing pass (plan §11), then re-run book-first under §11b. The milestone's own "Horowitz & Hill power/thermal" prose was right but unnamed; it now names AOE ch 9 §9.4 explicitly and adds the DRV8874 datasheet as the worked H-bridge artifact. Three concepts (m6-3, m6-4, m6-5) are recorded as having **no book found**, with datasheets as the honest substitute. No reviews scheduled - rows stay `unknown` until taught.
