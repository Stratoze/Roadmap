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

## Sources
- rigorous | Engineering Statics: Open and Interactive (free, CC BY-NC-SA) - **beginner, no statics prerequisite; the right primary for a self-taught learner** | Baker & Haynes | book: ch 4 "Moments and Static Equivalence" §4.1 "Direction of a Moment", §4.2 "Magnitude of a Moment"; ch 5 "Rigid Body Equilibrium" §5.2 "Free Body Diagrams", §5.3 "Equations of Equilibrium", §5.4 "2D Rigid Body Equilibrium" | https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Engineering_Statics%3A_Open_and_Interactive_(Baker_and_Haynes) | for m4-1, m4-2, m4-3, m4-4 | verified 2026-09-15
- rigorous | Mechanics Map (free, CC BY-NC-SA) - **beginner to intermediate, slightly more calculus-tinged; good second voice** | Moore et al. | book: ch 3 "Static Equilibrium in Rigid Body Systems" §3.1 "Moment of a Force about a Point (Scalar Calculation)", §3.6 "Equilibrium Analysis for a Rigid Body", §3.7 "Chapter 3 Homework Problems" | https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Mechanics_Map_(Moore_et_al.) | for m4-1, m4-2, m4-3, m4-4 | verified 2026-09-15
- reference | Shigley's Mechanical Engineering Design (9th ed., McGraw-Hill 2011) - **intermediate reference; assumes you can already do FBDs** | Budynas & Nisbett | book: ch 3 "Load and Stress Analysis" §3-1 "Equilibrium and Free-Body Diagrams" (pp. 72-75) | - | for m4-4 | verified 2026-09-15
- rigorous | A First Course in Finite Elements (Wiley, 2007, ISBN 978-0-470-03580-1) - **intermediate; assumes calculus + mechanics of materials** | Fish & Belytschko | book: ch 2 "Direct Approach for Discrete Systems"; ch 6 §6.1 "Divergence Theorem and Green's Formula"; ch 8 §8.2 "Verification and Validation" | https://www.wiley.com/en-us/A+First+Course+in+Finite+Elements-p-9780470035801 | for m4-5, m4-6 | verified 2026-09-15
- interactive | Textbook exercise sets: Baker & Haynes §4.8 + §5.8; Mechanics Map §3.7 | Baker & Haynes / Moore et al. | book: ch 4 §4.8 "Exercises", ch 5 §5.8 "Exercises" | https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Engineering_Statics%3A_Open_and_Interactive_(Baker_and_Haynes)/04%3A_Moments_and_Static_Equivalence/4.08%3A_Exercises | for m4-1, m4-2, m4-4 | verified 2026-09-15
- interactive | PhET Balancing Act | University of Colorado Boulder | interactive: balancing-act | https://phet.colorado.edu/en/simulations/balancing-act | for m4-3 | verified 2026-09-15
- intuitive | Understanding the Finite Element Method | The Efficient Engineer | video | https://www.youtube.com/watch?v=GHjopp47vvQ | for m4-5 | verified 2026-09-15
- intuitive (substitute) | Online Statics Course (94 lessons) | Jeff Hanson (@1234jhanson) | video playlist | https://www.youtube.com/playlist?list=PLRqDfxcafc23LXGoItpkYMKtUdHaQwSDC | for m4-1, m4-3, m4-4 | verified 2026-09-15
- intuitive (substitute) | Chapter 3 Introduction (embedded video) | Jacob Moore, on the Mechanics Map ch 3 page | video (short chapter intro) | https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Mechanics_Map_(Moore_et_al.)/03%3A_Static_Equilibrium_in_Rigid_Body_Systems/3.00%3A_Video_Introduction_to_Chapter_3 | for m4-1, m4-2 | verified 2026-09-15
- reference | PrePoMax (free FEA pre/post-processor) | PrePoMax project | tool | https://prepomax.fs.um.si/ | for m4-6 | verified 2026-09-15
- reference | CalculiX (solver; manual ccx_2.21) | Guido Dhondt | tool | http://www.dhondt.de/ | for m4-6 | verified 2026-09-15
- rejected | Understanding Statics | The Efficient Engineer (attributed) | video | - | - | rejected 2026-09-15 - **no such video exists on that channel**; same-titled videos belong to other, unverified creators

Corrections to the milestone's own prose (do not restore the old text):
- The old anchor "The Efficient Engineer *Understanding Statics*" cites a video that does not exist. Verified dead. The channel is real and its *Understanding the Finite Element Method* is genuine and is used for m4-5 instead.
- "Shigley Ch 3 (equilibrium & FBDs)" was misleading: Shigley 9th ed. ch 3 is titled "Load and Stress Analysis"; only §3-1 "Equilibrium and Free-Body Diagrams" is statics. Read that section and stop.

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
