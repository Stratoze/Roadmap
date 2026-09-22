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

## Sources
Levels: Kuphaldt LEC Vol. I is **beginner**, assumes nothing, free (CC BY). *The Art of Electronics* 3rd ed. is **intermediate**, assumes KVL/Ohm which 0.5 already covers, and is the best single read for m6-1/m6-2. Erickson & Maksimovic is **advanced** (wants signals/Laplace later).

- rigorous | The Art of Electronics (3rd ed.) | Horowitz & Hill | book: ch 9 "NINE: Voltage Regulation and Power Conversion" §9.4 "Heat and power design"; ch 3 "THREE: Field-Effect Transistors" §3.5 "Power MOSFETs" | https://artofelectronics.net/the-book/table-of-contents/ | for m6-1, m6-2, m6-3 | verified 2026-09-15
- rigorous | Lessons In Electric Circuits, Vol. I (DC), free CC BY, rev. 2021-11-06 | Tony R. Kuphaldt | book: ch 2 "OHM'S LAW" §"Power in electric circuits" | https://www.ibiblio.org/kuphaldt/electricCircuits/DC/DC_2.html | for m6-1 | verified 2026-09-15
- rigorous | Lessons In Electric Circuits, Vol. I (DC) | Tony R. Kuphaldt | book: ch 11 "BATTERIES AND POWER SYSTEMS" | https://www.ibiblio.org/kuphaldt/electricCircuits/DC/DC_11.html | for m6-4 | verified 2026-09-15
- rigorous | DRV8874 H-Bridge Motor Driver datasheet (200 mOhm HS+LS, 4.5-37 V, 6 A peak) | Texas Instruments | doc SLVSF66A sec 8.2.1.2.2 "Power Dissipation and Output Current Capability" (p.21), sec 6.4 "Thermal Information" (p.5) | https://www.ti.com/lit/ds/symlink/drv8874.pdf | for m6-1, m6-2, m6-3, m6-4 | verified 2026-09-15
- rigorous | DRV8871 6.5-45 V Brushed DC Motor Driver datasheet (3.6 A peak) | Texas Instruments | doc SLVSCY9B sec 10.4 "Power Dissipation", sec 10.3 "Thermal Considerations" (p.15) | https://www.ti.com/lit/ds/symlink/drv8871.pdf | for m6-1, m6-2, m6-4 | verified 2026-09-15
- rigorous | CSD18532Q5B 60 V N-Channel NexFET Power MOSFET datasheet | Texas Instruments | doc SLPS322E sec 4.3 Fig. 4-8 "Normalized On-State Resistance vs Temperature" (p.5); sec 4.2 "Thermal Information" (RthetaJA 40 C/W on 1-in^2 2 oz Cu, RthetaJC 0.8 C/W) | https://www.ti.com/lit/ds/symlink/csd18532q5b.pdf | for m6-2, m6-3 | verified 2026-09-15
- rigorous | Semiconductor and IC Package Thermal Metrics | Darvin Edwards & Hiep Nguyen, TI | doc SPRA953D sec 2 "RthetaJC Junction-to-Case" (Eq. 5, p.7: the RthetaJC + RthetaCS + RthetaSA path) | https://www.ti.com/lit/an/spra953c/spra953c.pdf | for m6-2 | verified 2026-09-15
- interactive | Circuit Simulator Applet (animated schematic + power/current plots) | Paul Falstad | interactive: circuit | https://www.falstad.com/circuit/ | for m6-1 | verified 2026-09-15
- intuitive (substitute) | Why Electronics Need Cooling - transistor heat sink | The Engineering Mindset | video | https://www.youtube.com/watch?v=LC5o2jC3yaw | for m6-1, m6-2 | verified 2026-09-15
- unverified | Fundamentals of Power Electronics (3rd ed., Springer 2020, ISBN 9783030438791) - advanced | Erickson & Maksimovic | book: no section claimed | https://openlibrary.org/books/OL28227058M.json | for m6-1, m6-5 | unverified 2026-09-15
- rejected | Power Electronics: Converters, Applications, and Design (3rd ed.) | Mohan, Undeland & Robbins | book: - | - | - | rejected 2026-09-15 - publisher page's "Table of Contents" is only a nav label; no chapter titles obtainable

No book found (explicit, per the books-first rule):
- **m6-3** (Rds(on) tempco): AOE §3.5 is title-verified only; its interior was not read, so it is not claimed to state the 25->150 C doubling. Verified locator is the datasheet curve (CSD18532Q5B Fig. 4-8) plus DRV8874 §8.2.1.2.2.
- **m6-4** (system power budget): no book covers it as a whole. AOE ch 9 has no power-budget section; LEC ch 11 is battery ratings only (partial). Substitutes: DRV8874 §8.2.1.2.2 (peak vs continuous/RMS, PCB-dependent), DRV8871 §10.4. Fuse sizing has no verified external source - `Mechatronics/resources/SAFETY_CARD.md` already covers it.
- **m6-5** (efficiency scope): no book section is titled around it. Nearest title-verified coverage is AOE §9.4/§9.6.

Erickson is `unverified` deliberately: link.springer.com serves a Client Challenge page for every DOI/ISBN/chapter URL tried, Open Library carries no `table_of_contents` record for the 2007/2012 or 2020 editions, and the archive.org scans are access-restricted (`djvu.txt` returns 401). **Do not cite a chapter number for it.**

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
