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

## Sources
- rigorous | Materials Selection in Mechanical Design (3rd ed.) | Michael F. Ashby | book: ch 4 "Material property charts", ch 5 "Materials selection - the basics", App. B "Material indices" | https://archive.org/download/ashby-materials-selection-in-mechanical-design-third-edition/Ashby-Materials%20Selection%20in%20Mechanical%20Design%20Third%20Edition.pdf | for m7-4, m7-7, m7-8 | verified 2026-09-15
- rigorous | Materials Science and Engineering: An Introduction (10th ed.) | Callister & Rethwisch | book: ch 6 "Mechanical Properties of Metals" | https://bcs.wiley.com/he-bcs/Books?action=contents&itemId=1119405491&bcsId=10955 | for m7-1, m7-2 | verified 2026-09-15
- rigorous | Materials Science and Engineering: An Introduction (10th ed.) | Callister & Rethwisch | book: ch 3 "The Structure of Crystalline Solids", ch 7 "Dislocations and Strengthening Mechanisms" | https://bcs.wiley.com/he-bcs/Books?action=contents&itemId=1119405491&bcsId=10955 | for m7-3 | verified 2026-09-15
- rigorous | Materials Science and Engineering: An Introduction (10th ed.) | Callister & Rethwisch | book: ch 8 "Failure" | https://bcs.wiley.com/he-bcs/Books?action=contents&itemId=1119405491&bcsId=10955 | for m7-5, m7-8 | verified 2026-09-15
- rigorous | Materials Science and Engineering: An Introduction (10th ed.) | Callister & Rethwisch | book: ch 10 "Phase Transformations in Metals", ch 11 "Applications and Processing of Metal Alloys" | https://bcs.wiley.com/he-bcs/Books?action=contents&itemId=1119405491&bcsId=10955 | for m7-6 | verified 2026-09-15
- rigorous | Materials Science and Engineering: An Introduction (10th ed.) | Callister & Rethwisch | book: ch 17 "Corrosion and Degradation of Materials" | https://bcs.wiley.com/he-bcs/Books?action=contents&itemId=1119405491&bcsId=10955 | for m7-6, m7-8 | verified 2026-09-15
- intuitive | An Introduction to Stress and Strain | The Efficient Engineer | video | https://www.youtube.com/watch?v=aQf6Q8t1FQE | for m7-1, m7-2 | verified 2026-09-15
- intuitive | Understanding Material Strength, Ductility and Toughness | The Efficient Engineer | video | https://www.youtube.com/watch?v=WSRqJdT2COE | for m7-2, m7-4 | verified 2026-09-15
- intuitive | Understanding Fatigue Failure and S-N Curves | The Efficient Engineer | video | https://www.youtube.com/watch?v=o-6V_JoRX1g | for m7-5 | verified 2026-09-15
- intuitive | Ductile and Brittle Fracture | Taylor Sparks (Univ. of Utah) | video | https://www.youtube.com/watch?v=LRKzOui_kS8 | for m7-3, m7-8 | verified 2026-09-15
- intuitive | Day 11 Crack Growth and Fatigue | Taylor Sparks (Univ. of Utah) | video | https://www.youtube.com/watch?v=wOg6_C7rzWQ | for m7-5, m7-8 | verified 2026-09-15
- intuitive | Creep test with 3D printed plastic materials: PLA, PETG, ASA, Nylon | My Tech Fun | video (chaptered) | https://www.youtube.com/watch?v=88pk2cNOeGE | for m7-6 | verified 2026-09-15
- interactive | Material Selection Charts: Young's modulus - Density (with exercises) | DoITPoMS, University of Cambridge | interactive: stiffness-density/NS6Chart | https://www-materials.eng.cam.ac.uk/mpsite/interactive_charts/stiffness-density/NS6Chart.html | for m7-2, m7-7 | verified 2026-09-15
- interactive | Material Selection Charts index (11 charts incl. Strength-Density, Strength-Toughness) | DoITPoMS, University of Cambridge | interactive: interactive_charts | https://www-materials.eng.cam.ac.uk/mpsite/interactive_charts/ | for m7-4, m7-7, m7-8 | verified 2026-09-15
- reference | 6061 aluminium alloy (6061-O / -T4 / -T6 property tables) | Wikipedia | page: 6061_aluminium_alloy | https://en.wikipedia.org/wiki/6061_aluminium_alloy | for m7-1, m7-6 | verified 2026-09-15
- reference | Galvanic corrosion (galvanic series, Al+steel couple) | Wikipedia | page: Galvanic_corrosion | https://en.wikipedia.org/wiki/Galvanic_corrosion | for m7-6 | verified 2026-09-15

Edition caveat: Ashby chapter numbers shift between editions - ch 4/ch 5 are the **3rd edition** (Butterworth-Heinemann, 2005), verified from the full-text TOC. Later editions renumber; ScienceDirect returned 403 for the 5e/6e TOCs. Do not cite ch 4/ch 5 without naming the edition. Callister 10e is the verified edition; 6e matches on ch 6/7/8/17 but differs on ch 11.

- blocker 2026-09-15 m7-5: "The Goodman / mean-stress construction has no verified locator. Callister ch 8 covers S-N and the endurance limit, but the Goodman diagram lives in Shigley's Mechanical Engineering Design ch 'Fatigue Failure Resulting from Variable Loading', and no publisher or library TOC for Shigley could be fetched (every reachable hit was a lecture PDF or a slide dump). Taught from Callister ch 8; refill the dossier with Shigley when a TOC loads."

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
