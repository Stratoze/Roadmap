# Circuits Basics (m0-5)

## Goal
- From `Mechatronics/ROADMAP.md` Phase 0: circuits basics at "Applied" level - solved a real problem with it, not just followed a derivation.
- Physical artifact context: feeds the Phase 0 metrology kit and every later measurement.
- By when: none (roadmap-sequenced).

## Map
- No bracket yet - this topic opens at first contact. Priors: none recorded on DC circuits.
- Concepts below are the milestone's own pass-condition topics (taken from the topic tree and `00_foundations.md`), listed so every lesson has a source before it starts.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| m5-1 | Ohm's law + KVL resistor sizing (LED current-limiting resistor: Vf 2.2 V, 20 mA, 5 V) | - | unknown | 0 | - | - |
| m5-2 | circuit intuition (voltage=pressure, current=flow, resistance=opposition; confirm in Falstad) | - | unknown | 0 | - | - |
| m5-3 | KCL + multi-loop KVL (branch node currents; loops with multiple components) | m5-1 | unknown | 0 | - | - |
| m5-4 | datasheet reading (find Vf and If(max); design below absolute maximum) | m5-1 | unknown | 0 | - | - |
| m5-5 | measurement discipline (DMM parallel/series; scope probe ground and 1x/10x) | m5-3 | unknown | 0 | - | - |
| m5-6 | real-hardware verification (multimeter reading matches calculation and simulation) | m5-5 | unknown | 0 | - | - |

## Sources
- rigorous | The Art of Electronics (3rd ed.) | Paul Horowitz & Winfield Hill | book: ch 1 "ONE: Foundations" (1.2 "Voltage, current and resistance"; 1.6 "Diodes and diode circuits"; Appendix O "The Oscilloscope") | https://artofelectronics.net/the-book/table-of-contents/ | for m5-1, m5-2, m5-3, m5-4, m5-5 | verified 2026-09-15
- rigorous | Learning the Art of Electronics: A Hands-on Approach (2nd ed.) | Thomas C. Hayes & David Abrams (with Paul Horowitz) | book: ch 1N "DC Circuits" (1N.2 "Three laws") + ch 1L "Lab: DC Circuits" (1L.2 "Meters, VOM and DVM") + ch 13N.3 "Sketchy datasheets for LED and phototransistor" | https://learningtheartofelectronics.com/about-the-book/table-of-contents/ | for m5-1, m5-3, m5-4, m5-5, m5-6 | verified 2026-09-15
- intuitive | Electronic Basics #8: Everything about LEDs and current limiting resistors | GreatScott! | video | https://www.youtube.com/watch?v=Qlayua3yjuE | for m5-1, m5-4, m5-6 | verified 2026-09-15
- intuitive | Electronic Basics #16: Resistors | GreatScott! | video | https://www.youtube.com/watch?v=7w5I-KbJ1Sg | for m5-1, m5-2 | verified 2026-09-15
- intuitive | #9: Basic 1X and 10X Oscilloscope Probe tutorial | w2aew (Alan Wolke, W2AEW) | video | https://www.youtube.com/watch?v=SX4HGNWBe5M | for m5-5 | verified 2026-09-15
- interactive | Falstad Circuit Simulator - "Ohm's Law" demo (+ "Diode I/V Curve") | Paul Falstad | interactive: e-ohms | https://www.falstad.com/circuit/e-ohms.html | for m5-1, m5-2, m5-6 | verified 2026-09-15
- interactive | Circuit Construction Kit: DC | PhET, University of Colorado Boulder | interactive: circuit-construction-kit-dc | https://phet.colorado.edu/en/simulations/circuit-construction-kit-dc | for m5-1, m5-2, m5-3 | verified 2026-09-15
- rejected | Microelectronic Circuits (8th ed.) | Sedra & Smith | book: ch 1 "Signals and Amplifiers" | - | - | rejected 2026-09-15 - amplifier-centric, no KVL/KCL treatment; wrong anchor for this milestone

No source found: m5-4 has no fetchable standalone LED datasheet (PDF fetches unsupported by the reader; alldatasheet/DigiKey/Farnell/onsemi all blocked). LAoE 13N.3 covers *how* to read a sketchy datasheet; for the actual numbers the learner opens the specific part's datasheet directly (e.g. Kingbright L-53SRC-E). That is a deliberate gap, not an omission.

## Misconceptions
-

## Problems
| id | problem | source | theory | attempts | status |
|----|---------|--------|--------|----------|--------|
| - | - | - | - | - | - |

## Links
- Rests on: none (Phase 0 foundation); feeds every later measurement (0.10 metrology, 1.3 current sense, 3.2 power)
- Teaches: feeds Phase 0.6 power/thermal, 0.10 metrology, Phase 1 current-sense front ends
- Lessons: -

## Log
- 2026-09-15 - file created for the Phase 0 foundational sourcing pass (plan §11). Concept rows from the milestone's own pass conditions; sources pinned at section granularity by scout + verifier, verdicts dated 2026-09-15. No reviews scheduled - rows stay `unknown` until taught or intaked.
