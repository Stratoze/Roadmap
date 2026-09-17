# Vectors, Trig, Frames of Reference (m0-2)

## Goal
- From `Mechatronics/ROADMAP.md` Phase 0: hand-calculate forward kinematics for a 2-link planar arm - given link lengths and joint angles, find the tip X, Y.
- Already complete (MVM + Full Pass, tested 2026-08-21) - this file exists so later lessons have verified sources, not to re-teach it.

## Map
- Pre-system topic: opens through **intake** (compressed cold verify per concept), never a full re-teach (standing order 3).
- Bracket floor (from the evidence file, 2026-08-21): converted theta2 to world frame instead of plugging in 60 deg - frame reasoning was present before the system.

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| m2-1 | vector addition and components (each link is a vector; the second link's base moves with the first) | - | unknown | 0 | - | - |
| m2-2 | 2-link planar forward kinematics (derive tip X,Y by hand from theta1, theta2, L1, L2) | m2-1 | unknown | 0 | - | - |
| m2-3 | vector diagram literacy (draw the diagram before plugging into formulas) | m2-1 | unknown | 0 | - | - |
| m2-4 | world vs link frames (express a point in either frame; rotate the base; add a third link) | m2-2 | unknown | 0 | - | - |
| m2-5 | radians vs degrees (silent code bug; everything in software is radians) | m2-1 | unknown | 0 | - | - |
| m2-6 | atan2 vs atan (quadrant ranges; robotics always uses atan2(y, x)) | m2-5 | unknown | 0 | - | - |
| m2-7 | dot product as projection (physical meaning; angle between vectors) | m2-1 | unknown | 0 | - | - |

## Sources
- rigorous | Introduction to Robotics: Mechanics and Control (3rd ed.) | John J. Craig | book: ch 2 "Spatial descriptions and transformations" | - | for m2-1, m2-2, m2-4 | verified 2026-09-15
- rigorous | Modern Robotics: Mechanics, Planning, and Control | Kevin M. Lynch & Frank C. Park | book: ch 3 "Rigid-Body Motions" + ch 4 "Forward Kinematics" | https://hades.mech.northwestern.edu/index.php/Modern_Robotics | for m2-2, m2-4 | verified 2026-09-15
- intuitive | Vectors - Chapter 1, Essence of linear algebra | 3Blue1Brown (Grant Sanderson) | video | https://www.youtube.com/watch?v=fNk_zzaMoSs | for m2-1, m2-3 | verified 2026-09-15
- intuitive | Linear combinations, span, and basis vectors - Chapter 2 | 3Blue1Brown (Grant Sanderson) | video | https://www.youtube.com/watch?v=k7RM-ot2NWY | for m2-1, m2-3 | verified 2026-09-15
- intuitive | Dot products and duality - Chapter 9 | 3Blue1Brown (Grant Sanderson) | video | https://www.youtube.com/watch?v=LyGKycYT2v0 | for m2-7 | verified 2026-09-15
- intuitive | Change of basis - Chapter 13 | 3Blue1Brown (Grant Sanderson) | video | https://www.youtube.com/watch?v=P2LTAUO1TdA | for m2-4 | verified 2026-09-15
- intuitive | Analyzing a 2-joint planar robot arm | Prof. Peter Corke, Robot Academy (QUT) | video | https://robotacademy.net.au/lesson/analyzing-a-2-joint-planar-robot-arm/ | for m2-1, m2-2, m2-4 | verified 2026-09-15
- intuitive | Radians | Rod Pierce, Math is Fun | page: "Radians" | https://www.mathsisfun.com/geometry/radians.html | for m2-5 | verified 2026-09-15
- interactive | An introduction to vectors | Frank & Nykamp, Math Insight (Univ. of Minnesota) | interactive: vector_introduction | https://mathinsight.org/vector_introduction | for m2-1, m2-3 | verified 2026-09-15
- interactive | The dot product | Duane Q. Nykamp, Math Insight (Univ. of Minnesota) | interactive: dot_product | https://mathinsight.org/dot_product | for m2-7 | verified 2026-09-15
- reference | math - Mathematical functions | Python Software Foundation | docs: library/math | https://docs.python.org/3/library/math.html | for m2-5, m2-6 | verified 2026-09-15
- reference | atan2 | Wikipedia | page: "Definition and computation" | https://en.wikipedia.org/wiki/Atan2 | for m2-6 | verified 2026-09-15
- rejected | Introduction-to-Robotics-Craig.pdf (university mirror), Scribd and pubhtml5 copies | unattributed | - | - | - | rejected 2026-09-15 - pirated mirrors, not citable; pubhtml5 exposes no TOC text

Edition caveat: the fetched Craig TOC is the **3rd edition** (ch 2 "Spatial descriptions and transformations" at p. 19). A 4th edition exists (Pearson 2017); its TOC was not fetched, so ch 2 is verified for the 3rd ed. only. Topology is unchanged in the 4th, but do not claim the locator for an edition nobody checked.

## Misconceptions
-

## Problems
| id | problem | source | theory | attempts | status |
|----|---------|--------|--------|----------|--------|
| - | - | - | - | - | - |

## Links
- Rests on: 0.1 (binary-search debugging, I/O framing)
- Teaches: feeds 0.4 (statics of the same 2-link arm), 2.5 (multi-DOF dynamics), 4.2 (IK - the inverse of this FK)
- Lessons: -

## Log
- 2026-09-15 - file created for the Phase 0 foundational sourcing pass (plan §11). Concept rows from the milestone's pass conditions; every id has at least one verified locator - no gaps. Craig ch 2 was named in the milestone's own prose and independently TOC-verified (3rd ed.). No reviews scheduled - intake only.
