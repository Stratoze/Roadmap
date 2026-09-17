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

## Sources
- rigorous | Design of Machinery: An Introduction to the Synthesis and Analysis of Mechanisms and Machines (6th ed.) | Robert L. Norton (McGraw Hill, 2019) | book: ch 2 "Kinematics Fundamentals" (2.4 Drawing Kinematic Diagrams; 2.5 Determining Degree of Freedom or Mobility; 2.11 Intermittent Motion; 2.13 The Grashof Condition; 2.15 Springs as Links; 2.16 Compliant Mechanisms) | https://designofmachinery.com/wp-content/uploads/2018/12/DOM-6ed-Contents-Sample.pdf | for m9-1, m9-2, m9-3, m9-5, m9-6 | verified 2026-09-15
- rigorous | Design of Machinery (6th ed.) | Robert L. Norton | book: ch 3 "Graphical Linkage Synthesis" | https://designofmachinery.com/wp-content/uploads/2018/12/DOM-6ed-Contents-Sample.pdf | for m9-3 | verified 2026-09-15
- rigorous | Design of Machinery (6th ed.) | Robert L. Norton | book: ch 8 "Cam Design" (8.6 Sizing the Cam - Pressure Angle and Radius of Curvature) | https://designofmachinery.com/wp-content/uploads/2018/12/DOM-6ed-Contents-Sample.pdf | for m9-4 | verified 2026-09-15
- rigorous | Design of Machinery (6th ed.) | Robert L. Norton | book: ch 9 "Gear Trains" (9.6 Belt and Chain Drives; 9.9 Epicyclic or Planetary Gear Trains; 9.10 Efficiency of Gear Trains) | https://designofmachinery.com/wp-content/uploads/2018/12/DOM-6ed-Contents-Sample.pdf | for m9-7 | verified 2026-09-15
- reference | ME 363 Mechanics of Machinery - Cam Design handout | King Saud Univ., College of Engineering | doc: me_363_cam_handout | https://faculty.ksu.edu.sa/sites/default/files/me_363_cam_handout.pdf | for m9-4 | verified 2026-09-15
- reference | Spicer Double Cardan Constant Velocity Joint Assemblies (CV catalog, Dec 2001) | Dana / Spicer | doc: Spicer_CV_Catalog_12-2001 | https://patsdriveline.com/wp-content/uploads/2017/06/Spicer_CV_Catalog_12-2001.pdf | for m9-6 | verified 2026-09-15
- reference | Screw University: Screw Backdriving Efficiency | Roton Products, Inc. | page: screw-backdriving-efficiency | https://www.roton.com/screw-university/screw-actions/screw-backdriving-efficiency/ | for m9-7 | verified 2026-09-15
- reference | Calibration (Knowledge Base category) | Prusa Research | interactive: calibration_199 | https://help.prusa3d.com/category/calibration_199 | for m9-8 | verified 2026-09-15
- reference | Tolerance Test Calibration Cube | Printables community model | model: 548480 | https://www.printables.com/model/548480-tolerance-test-calibration-cube | for m9-8 | unverified (HTTP 403 to automated fetch) |
- intuitive | Planetary Reduction Gear with Oldham coupling | thang010146 (Nguyen Duc Thang) | video | https://www.youtube.com/watch?v=78gkc9mPT-w | for m9-6, m9-7 | verified 2026-09-15
- intuitive | Oldham coupling 1 | thang010146 | video | https://www.youtube.com/watch?v=VPVxy9uW45E | for m9-6 | verified 2026-09-15
- intuitive | Oldham coupling 2 | thang010146 | video | https://www.youtube.com/watch?v=M2IlDz_27GY | for m9-6 | verified 2026-09-15
- intuitive | 1. DoF Concept_1 (ME-315 Mechanics of Machines) | ME-315 Mechanics of Machines | video | https://www.youtube.com/watch?v=3-jC-eTAwME | for m9-1, m9-2 | verified 2026-09-15
- intuitive | Geneva Mechanism Working Model | TG Simulation Lab | video | https://www.youtube.com/watch?v=VhJ0mRnuRAk | for m9-5 | verified 2026-09-15
- intuitive | Mechanism animations (channel) | thang010146 (Nguyen Duc Thang) | channel | https://www.youtube.com/thang010146/videos | for m9-1, m9-3, m9-4, m9-5, m9-6, m9-7 | verified 2026-09-15
- interactive | Four-Bar Linkage Simulator (crank-rocker / double-crank / double-rocker, Grashof check, transmission angle, coupler curves) | MechSimulator (Naseel Ibnu Azeez) | interactive: tools/four-bar-linkage | https://mechsimulator.com/tools/four-bar-linkage/ | for m9-1, m9-2, m9-3 | verified 2026-09-15
- interactive | KMODDL - Reuleaux Collection of Mechanisms and Machines | Cornell University Library | page: kmoddl | https://engineering.library.cornell.edu/kmoddl/ | for m9-1, m9-3, m9-6, m9-7 | verified 2026-09-15 (thumbnail verification) |

Source-verification caveats (do not silently upgrade these):
- The pressure-angle **30°** figure is vault-supplied, not source-verified. Norton 8.6 covers pressure angle and radius of curvature, and the KSU handout defines pressure angle, but no fetched page was confirmed to print the numeric limit. State it as a rule of thumb when taught.
- m9-6's compliance half rests on Norton §2.15/§2.16 - chapter titles verified from the TOC, section *content* not fetched. TOC-level locator only.
- Norton has no chapter on couplings (Oldham/U-joint), power screws, or 3D-print tolerance; belts/chains only as §9.6. Those concepts legitimately rest on the non-Norton sources above.
- Erdman/Sandor *Mechanism Design* was **not** verified (B&N 403, WorldCat/LOC 403) - no chapter may be cited for it.

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
