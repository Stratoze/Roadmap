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

## Sources
- rigorous | JCGM 100:2008 Evaluation of measurement data - Guide to the expression of uncertainty in measurement (GUM) | JCGM/WG1 | doc JCGM 100:2008 sec 4.2 "Type A evaluation of standard uncertainty", sec 4.3 "Type B evaluation of standard uncertainty", sec 5 "Determining combined standard uncertainty", sec 6 "Determining expanded uncertainty", sec 7 "Reporting uncertainty" | https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf/cb0ef43f-baa5-11cf-3f85-4dcd86f77bd6 | for m10-3, m10-4, m10-5 | verified 2026-09-15
- rigorous | NIST Technical Note 1297: Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results | Taylor & Kuyatt (NIST) | doc NIST TN 1297 sec 2 "Classification of Components of Uncertainty", sec 3 "Type A Evaluation", sec 4 "Type B Evaluation" (4.6 rectangular distribution), sec 5 "Combined Standard Uncertainty", sec 6 "Expanded Uncertainty", sec 7 "Reporting Uncertainty" | https://www.nist.gov/pml/nist-technical-note-1297 | for m10-3, m10-4, m10-5, m10-6 | verified 2026-09-15
- rigorous | Callipers and micrometers (Measurement Good Practice Guide No. 40) | National Physical Laboratory | doc NPL GPG40 sec "Operating principles", "Set-up, preparation and measurements", "Factors affecting calliper performance", "Periodic inspection and calibration" | https://www.npl.co.uk/resources/gpgs/callipers-micrometers | for m10-1, m10-2, m10-5, m10-7 | verified 2026-09-15
- rigorous | A Beginner's Guide to Uncertainty of Measurement (Measurement Good Practice Guide No. 11, Issue 2) | Stephanie Bell, NPL | doc NPL GPG11 sec 3.5 "Spread ... standard deviation", sec 3.6 "Calculating an estimated standard deviation", sec 5.1 "Random or systematic", sec 5.2.2 "Uniform or rectangular distribution", sec 7.1 "Standard uncertainty" (7.1.1 Type A, 7.1.2 Type B), sec 7.2.1 "Summation in quadrature", sec 7.4 "Coverage factor k", sec 9 "Example" | https://www.npl.co.uk/resources/gpgs/beginners-guide-measurement-uncertainty-gpg11 | for m10-3, m10-4, m10-5, m10-6 | verified 2026-09-15
- interactive | NIST Uncertainty Machine (v1.6.4) | NIST Physical Measurement Laboratory | interactive: preloaded "Gauge" example | https://uncertainty.nist.gov/ | for m10-3, m10-4, m10-5 | verified 2026-09-15
- intuitive | How To Read A Mitutoyo Dial Caliper | Mitutoyo America Corporation | video | https://www.youtube.com/watch?v=PAev56PoNts | for m10-1, m10-2 | verified 2026-09-15
- intuitive | Measuring with English and Metric Dial Calipers | Starrett product demo (uploaded by A&M Industrial) | video | https://www.youtube.com/watch?v=dgmNBEEN3gM | for m10-1, m10-2 | verified 2026-09-15
- intuitive | How To Read A Dial Indicator | Travers Tool Co. (Kurt Repsher) | video (embedded + step-by-step article) | https://solutions.travers.com/metalworking-machining/measuring-inspection/how-to-read-a-dial-indicator | for m10-1, m10-7 | verified 2026-09-15
- intuitive | Precision in measurement | Science toolkit, Khan Academy | video | https://www.youtube.com/watch?v=ClW4x6OPDPQ | for m10-2 | verified 2026-09-15
- rejected | Geometric Inspection Methods FULL GUIDE (Flatness to Total Runout) | channel "Mechanical Design Engineering" | video | - | - | rejected 2026-09-15 - creator identity not verifiable as an established educator

Formula note for m10-4: NIST TN 1297 sec 4.6 gives `u = a/sqrt(3)` for a rectangular distribution about a *half-width* `a`; the milestone's `resolution/sqrt(12)` is the same quantity when `resolution` is the full interval `2a` and the error is rounding. One-sentence clarification when taught - the learner is told sqrt(12), and it is correct as written.

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
