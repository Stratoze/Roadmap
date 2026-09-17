
# Phase 0 — Foundations & Vocabulary

## Outcome

The physics, math, and reasoning base that everything else depends on.
Vectors, calculus intuition, statics, circuits, power, materials, manufacturing, the kinematic vocabulary of machines, and the metrology to measure what you build.

You don't need to master these before building. You need them at "Applied" level — you've solved a real problem with each one, not just followed a derivation.

**Physical artifacts of this phase:**
1. Parametric Mechanism Testbed — 3D-printed (or cardboard) baseplate with 5+ interchangeable mechanisms
2. Metrology Kit — calipers + dial indicator + documented measurement uncertainty

**Fabrication & safety envelope (Phase 0):**
- Cardboard, hand tools, hobby knife, 3D printer only.
- NO soldering. NO power tools. USB / 5V only for the blinky speed run.
- Eye protection when clipping anything. Cut away from your body.

---

## Phase Sources — the foundational spine

Catch-all texts for the whole phase: when a lesson's own citation does not cover something and a *blocker* fires, look here before asking the AI. Verified 2026-09-15; level is stated because a correct book at the wrong level is useless. Each also has a milestone-level section citation in the topic files under `_system/learning/curriculum/m0-*.md`.

| Discipline | Book | Level | Why it is the spine |
|---|---|---|---|
| Math | Strang, Herman et al., *Calculus Volume 1* (OpenStax, free) | beginner | Owns derivative-as-rate and the net-change theorem, which 0.3 and every controller after it rest on |
| Physics | *Classical Mechanics* 8.01SC (MIT OpenCourseWare, free) | beginner-intermediate | Newton's laws through rotation, with worked examples and problem sets; covers the conservation-law framing 0.1 asks for |
| Statics | Baker & Haynes, *Engineering Statics: Open and Interactive* (free, CC BY-NC-SA) | beginner | FBDs, equilibrium, moments - no statics prerequisite, so it is usable cold |
| Circuits | Horowitz & Hill, *The Art of Electronics* (3rd ed.) | intermediate | The reference for 0.5, 0.6 and every analog front end through Phase 3; assumes only Ohm/KVL |
| Materials | Callister & Rethwisch, *Materials Science and Engineering: An Introduction* (10th ed.) | intermediate | Stress-strain, dislocations, failure, corrosion in one place; pairs with Ashby for *selection* |
| Materials selection | Ashby, *Materials Selection in Mechanical Design* (3rd ed.) | intermediate | Property charts and material indices - the E/rho vs sigma_y/rho reasoning in 0.7 |
| Manufacturing | Kalpakjian & Schmid, *Manufacturing Engineering and Technology* (8th ed.) | intermediate, **skim by section** | The process taxonomy for 0.8; 1200+ pp., a reference not a read-through |
| DFMA | Boothroyd, Dewhurst & Knight, *Product Design for Manufacture and Assembly* | intermediate | The DFA method itself; ch 3 is self-contained |
| Mechanisms | Norton, *Design of Machinery* (6th ed.) | intermediate | Kinematic diagrams, mobility, Grashof, cams, gear trains - 0.9's vocabulary |

Not on this list, deliberately: Feynman Lectures Vol. I (the right home for the conservation-law framing, but `feynmanlectures.caltech.edu` returns 403 to automated fetch, so it stays uncited per the no-unverified-claims rule), and Erickson & Maksimovic *Fundamentals of Power Electronics* (no fetchable TOC). Add either once a TOC or a reachable copy is verified.

---

## Phase Pass Condition

### MVM
- [ ] Can re-solve each milestone task with notes open
- [ ] Can explain each concept aloud, Feynman test — stumble = gap
- [ ] Git repo + log + vault review queue started (first review done)
- [ ] Can state basic measurement sanity: voltage across, current through, scope ground/probe discipline, current-limited supply default (state, not perform — scopes and bench supplies are Phase 1 tools)
- [ ] Can look at a part and name the manufacturing process that made it
- [ ] Can look at a mechanism and name it, count its DOF, and state its input→output motion
- [ ] **Physical:** mechanism testbed assembled, ≥ 3 mechanisms, photographed
- [ ] **Physical:** one 3D-printed part measured with calipers, uncertainty stated

### Full Pass
- [ ] Can re-solve each milestone task from memory, blank page
- [ ] One-page synthesis sheet: one paragraph per concept
- [ ] Safety setup reflexive — not something you have to remember
- [ ] Can do a simple power budget: voltage rails, expected current, wire/fuse/connector sizing, and thermal loss intuition
- [ ] Can select a material for a given load/environment using Ashby reasoning
- [ ] Can sketch a DFM/DFA critique of a simple part
- [ ] Can draw the kinematic diagram of any mechanism from 0.9 and explain where it's used
- [ ] **Physical:** testbed has 5+ mechanisms with kinematic diagrams posted beside them
- [ ] **Physical:** metrology log with Type A + Type B uncertainty committed to `data/processed/`

---

## Milestone 0.1 — Problem-Solving Framework + Toolchain

> [!info] 📚 Resources — Problem-Solving & Toolchain
> **Read:** Polya, *How to Solve It* — ch 6 "Four phases" (the problem-solving frame). Decomposition: Simon, *The Sciences of the Artificial* (3rd ed.) ch 8 "The Architecture of Complexity: Hierarchic Systems". Debugging: Agans, *Debugging* ch 8 "Divide and Conquer". First principles / the conservation law doing the work: MIT 8.01SC *Classical Mechanics* — Week 8 "Potential Energy and Energy Conservation" (Lesson 24 "Conservation of Energy") and Week 7 "Kinetic Energy and Work" (Lesson 20).
> **Visual:** your own [[_system/How to Learn]] (functional decomposition, first principles); Veritasium *The Science of Thinking*; TED-Ed *A clever way to estimate enormous numbers* (Fermi).
> **Interactive:** set up the toolchain and flash a blinky. That *is* the milestone — stop when it blinks. Wokwi if no board is at hand.
> **Theory:** not zero-theory: Polya's four phases for the problem-solving frame, Simon ch 8 for hierarchic decomposition. Git: Pro Git ch 1. Reviews: Anki Manual "Getting Started" / "Deck Options".

<a id="m0-1"></a>
Lenses - m0-1
Rigorous: Learning How to Learn | Barbara Oakley | https://www.youtube.com/watch?v=O96fE1E-rf8 | approved
Intuitive: The Science of Thinking | Veritasium | https://www.youtube.com/watch?v=UBVV8pch1dM | approved
Book: ch 6 "Four phases" | How to Solve It (Princeton Science Library 2014) | George Polya | https://press.princeton.edu/books/paperback/9780691164076/how-to-solve-it | verified 2026-09-15
Book: ch 8 "The Architecture of Complexity: Hierarchic Systems" | The Sciences of the Artificial (3rd ed.) | Herbert A. Simon | - | verified 2026-09-15
Book: ch 8 "Divide and Conquer" (see also ch 4 "Make It Fail") | Debugging: The 9 Indispensable Rules | David J. Agans | - | verified 2026-09-15
Book: ch 1 "Getting Started" | Pro Git (2nd ed.) | Chacon & Straub | https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control | verified 2026-09-15
Interactive: set up the toolchain and flash a blinky. That *is* the milestone - stop when it blinks.   Theory: none. This is an environment milestone, not a theory one.

### Deliverable

Working dev environment, local Git repo with first commit, vault review queue started, and a problem-solving vocabulary you can use when stuck.

## Pass Condition

### MVM
- [x] Git repo initialized, first meaningful commit
- [x] Editor, terminal, toolchain verified
- [x] Anki deck created
- [x] Can state: "What is the Input, Output, and Transformation here?"

### Full Pass
- [x] Flashlight deconstruction: black boxes, energy chain, first principles
- [x] Can apply binary-search debugging to a simple fault
- [x] Can Fermi-estimate before computing, within an order of magnitude

> [!warning] ⚠️ Landmines
> 1. **"Setting up the environment" is not the work.** `[HYPOTHESIS]`
>    The toolchain is done when you can compile and flash a blinky. Stop there.
>
> 2. **Functional decomposition is harder than it looks.** `[HYPOTHESIS]`
>    The discipline is defining the interface between boxes precisely enough that the boxes could be built independently.
>
> 3. **First principles ≠ deriving everything from scratch.** `[HYPOTHESIS]`
>    It means finding the conservation law doing the work: energy, Newton, Kirchhoff, or information flow. When stuck, ask which one applies.
>

## Dependencies that waste your week if hit backwards

- Don't configure 15 tools before verifying ONE compiles. Blink first, configure later.

> Evidence: [[Mechatronics/milestones/evidence/0.1-toolchain|personal evidence 0.1]] (MVM `m0.1-mvm` · Full `m0.1-fullpass` — see note below)

> [!note] Record note (forward annotation, history intact)
> The 0.1 evidence file is thin: no Fermi number, no blinky artifact pointer, one wrong LED mechanism in the prose. Boxes stay checked (earned in August); from 0.3 on, every numeric result needs units + tolerance (analytic-exact results state their exactness instead) and every physical pass needs an artifact pointer per the evidence convention. Tags keep their names (convention standardized at `m<phase>.<n>-(mvm|full)` going forward).


---

# Milestone 0.2 — Vectors, Trig, Frames of Reference

> [!info] 📚 Resources — Vectors, Trig & Frames
> **Read:** Craig, *Introduction to Robotics: Mechanics and Control* (3rd ed.) — ch 2 "Spatial descriptions and transformations". Free companion: Lynch & Park, *Modern Robotics* ch 3 "Rigid-Body Motions" + ch 4 "Forward Kinematics".
> **Visual:** *(substitute only)* 3Blue1Brown *Essence of Linear Algebra* (vectors, linear combinations); Peter Corke (QUT Robot Academy) *Analyzing a 2-joint planar robot arm* — the closest single source to this milestone's deliverable.
> **Interactive:** plot the 2-link arm tip in Python for a few (θ1,θ2); see the vector add. Math Insight applets for tail-to-head addition and live dot-product projection.
> **Theory:** frames & transformations — only what forward kinematics needs. `math.radians`/`math.atan2` docs for the two code landmines (radians; quadrant-correct angle).

<a id="m0-2"></a>
Lenses - m0-2
Rigorous: Vectors - Chapter 1, Essence of linear algebra | 3Blue1Brown | https://www.youtube.com/watch?v=fNk_zzaMoSs | approved
Intuitive: Vectors - Precalculus | Khan Academy | https://www.youtube.com/playlist?list=PLSQl0a2vh4HCmCL_bFUJSuCAV4P_D18oi | approved
Book: ch 2 "Spatial descriptions and transformations" | Introduction to Robotics: Mechanics and Control (3rd ed.) | John J. Craig | - | verified 2026-09-15
Book: ch 3 "Rigid-Body Motions" + ch 4 "Forward Kinematics" | Modern Robotics: Mechanics, Planning, and Control | Lynch & Park | https://hades.mech.northwestern.edu/index.php/Modern_Robotics | verified 2026-09-15
Interactive: plot the 2-link arm tip in Python for a few (th1,th2); see the vector add.   Theory: Craig Introduction to Robotics Ch 2 (frames and transformations) / Khan Academy - only what forward kinematics needs.

## Deliverable

Hand-calculated forward kinematics for a 2-link planar arm. Given link lengths and joint angles, find the tip position, X, Y.

## Pass Condition

### MVM
- [x] Can calculate tip position for given θ1, θ2, L1, L2
- [x] Understands world frame vs. link frame
- [x] Can draw the vector diagram, not just plug into a formula

### Full Pass
- [x] Can modify: add a third link, rotate the base, change reference frame
- [x] Dot product has physical meaning: projection

> [!warning] ⚠️ Landmines
> 1. **Multi-link kinematics requires vector addition.** `[HYPOTHESIS]`
>    The second link's base moves with the first. Treat each link as a vector, add them. Don't compute joint angles independently.
>
> 2. **Radians vs. degrees will bite you in code.** `[COMMUNITY]`
>    Everything in software uses radians. No error message when you mix them.
>
> 3. **atan2 is not atan.** `[COMMUNITY]`
>    atan returns -90° to 90°. atan2(y, x) returns -180° to 180°. For robotics, always atan2.
>
> >
> > Evidence: [[Mechatronics/milestones/evidence/0.2-3link-fk|personal evidence 0.2]] (MVM `m0.2-mvm` · Full `m0.2-full`)

---

# Milestone 0.3 — Calculus Intuition

> [!info] 📚 Resources — Calculus Intuition
> **Read:** OpenStax *Calculus Volume 1* — ch 3 §3.4 "Derivatives as Rates of Change", ch 5 §5.1 "Approximating Areas" + §5.4 "Integration Formulas and the Net Change Theorem", ch 4 §4.10 "Antiderivatives", ch 6 §6.5 "Physical Applications". (The old "no textbook required" line is dropped: the net-change theorem *is* the theory here.)
> **Visual:** *(substitute only)* 3Blue1Brown *Essence of Calculus* ch 2 "The paradox of the derivative" → ch 8 "Integration and the fundamental theorem of calculus" → ch 10 "Higher order derivatives". *(Ch 1-3 does not cover integration; ch 8/10 are the ones this milestone needs.)*
> **Interactive:** Desmos (desmos.com/calculator) — plot y=2x, shade 0→3 with the integral command; area reads 9. Confirm with `scipy.integrate.quad(lambda t: 2*t, 0, 3)` → (9.0, ~1e-13). Agreement to 6 decimals passes. MIT 18.01SC mathlets (drag the secant into a tangent) for the limit idea.
> **Theory:** intuition over symbolic fluency — net change theorem (integral of a rate = net change) is the load-bearing piece. Physics side: OpenStax *University Physics Volume 1* §7.4 "Power".

<a id="m0-3"></a>
Lenses - m0-3
Rigorous: The essence of calculus | 3Blue1Brown | https://www.youtube.com/watch?v=WUvTyaaNkzM | approved
Intuitive: Calculus 1 Lecture 1.1: An Introduction to Limits | Professor Leonard | https://www.youtube.com/watch?v=54_XRjHhZzI | approved
Book: ch 3 §3.4 "Derivatives as Rates of Change"; ch 5 §5.1 "Approximating Areas"; ch 5 §5.4 "Integration Formulas and the Net Change Theorem"; ch 4 §4.10 "Antiderivatives"; ch 6 §6.5 "Physical Applications" | Calculus Volume 1 (OpenStax) | Strang, Herman et al. | https://openstax.org/books/calculus-volume-1/pages/5-4-integration-formulas-and-the-net-change-theorem | verified 2026-09-15
Book: lesson 10 "The Theory of Derivatives"; lesson 11 "The Fundamental Theorem Of Calculus" | Calculus, Better Explained (web lessons) | Kalid Azad | https://betterexplained.com/calculus/lesson-11/ | verified 2026-09-15
Book: ch 7 §7.4 "Power" | University Physics Volume 1 (OpenStax) | Moebs, Ling, Sanny | https://openstax.org/books/university-physics-volume-1/pages/7-4-power | verified 2026-09-15
Interactive: Desmos - plot y=2x, shade 0 to 3 with the integral command; area reads 9.   Theory: intuition over symbolic fluency. (No textbook required - video + doing is the whole theory here.)

## Deliverable

Given v(t) = 2t m/s with x(0) = 0: derive acceleration, calculate position at t = 3 s by integration, explain the physical meaning of the area under the curve (in words a peer would accept — the MVM bar; the Full bar below bans the formula).

## Pass Condition

### MVM (test items: v(t) = 2t, p(t) = t³ − 2t, degree ≤ 3; open notes)
- [ ] Can take a derivative of a polynomial
- [ ] Can integrate a polynomial with limits
- [ ] Can chain: position → velocity → acceleration and back (on the same two test items)
- [ ] Can explain: derivative = rate of change, integral = accumulation (formula allowed)

### Full Pass (blank page; new items, e.g. v(t) = 4t² + t)
- [ ] Power → Energy by integration, same idea, different domain (numbers: P(t) = 6t W, 0→2 s → E in joules)
- [ ] Can explain why area under v(t) is displacement without the formula

> [!warning] ⚠️ Landmines
> 1. **Calculus intuition ≠ calculus computation.** `[HYPOTHESIS]`
>    If you can compute ∫2t dt = t² but can't explain why integrating velocity gives position, the intuition is missing.
>
> 2. **You don't need symbolic fluency for embedded work.** `[HYPOTHESIS]`
>    Digital controllers use discrete approximations. But you need the continuous intuition to know if your approximation is correct.
>
>

---

# Milestone 0.4 — Statics + Free Body Diagrams

> [!info] 📚 Resources — Statics & FBDs
> **Read:** Baker & Haynes, *Engineering Statics: Open and Interactive* — **beginner, no statics prerequisite, free full text, has figures and exercise sets**; the right primary for a self-taught learner. ch 4 "Moments and Static Equivalence" §4.1 "Direction of a Moment" + §4.2 "Magnitude of a Moment"; ch 5 "Rigid Body Equilibrium" §5.2 "Free Body Diagrams" + §5.3 "Equations of Equilibrium" + §5.4 "2D Rigid Body Equilibrium". Second voice: Moore et al., *Mechanics Map* ch 3 "Static Equilibrium in Rigid Body Systems" §3.1 "Moment of a Force about a Point", §3.6 "Equilibrium Analysis for a Rigid Body".
> **Visual:** *(substitute only — the two open textbooks are the spine)* The Efficient Engineer *Understanding the Finite Element Method* for the FEM concept; Jeff Hanson's *Online Statics Course* (94 lessons) for FBD problems. **The old prose anchor "The Efficient Engineer *Understanding Statics*" was wrong — that channel has no such video; same-titled videos elsewhere are unverified, so it is dropped.**
> **Interactive:** PhET *Balancing Act* — 15 min for torque intuition before the math. Then the textbook exercises: Baker & Haynes §4.8 and §5.8, Mechanics Map §3.7.
> **Theory:** τ = F·d⊥ — the moment arm shrinks as it rotates to perpendicular (Baker & Haynes §4.2). For FEM: Fish & Belytschko, *A First Course in Finite Elements* ch 2 "Direct Approach for Discrete Systems" (discretize → element stiffness → assemble → BCs → displacement → stress) and §8.2 "Verification and Validation". Shigley 9th ed. **§3-1** "Equilibrium and Free-Body Diagrams" only — the chapter itself, ch 3, is "Load and Stress Analysis", so read the one section and skip the rest until Phase 3.

<a id="m0-4"></a>
Lenses - m0-4
Rigorous: Online Statics Course | Jeff Hanson | https://www.youtube.com/playlist?list=PLRqDfxcafc23LXGoItpkYMKtUdHaQwSDC | verified 2026-09-15
Intuitive: Forces and free-body diagrams | AP Physics | Khan Academy | https://www.youtube.com/watch?v=i447NWNpScM | approved
Book: ch 4 "Moments and Static Equivalence" §4.1 "Direction of a Moment", §4.2 "Magnitude of a Moment"; ch 5 "Rigid Body Equilibrium" §5.2 "Free Body Diagrams", §5.3 "Equations of Equilibrium", §5.4 "2D Rigid Body Equilibrium" | Engineering Statics: Open and Interactive (free, CC BY-NC-SA) | Baker & Haynes | https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Engineering_Statics%3A_Open_and_Interactive_(Baker_and_Haynes) | verified 2026-09-15
Book: ch 3 "Static Equilibrium in Rigid Body Systems" §3.1 "Moment of a Force about a Point", §3.6 "Equilibrium Analysis for a Rigid Body", §3.7 "Chapter 3 Homework Problems" | Mechanics Map (free, CC BY-NC-SA) | Moore et al. | https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Mechanics_Map_(Moore_et_al.) | verified 2026-09-15
Book: ch 2 "Direct Approach for Discrete Systems"; ch 8 §8.2 "Verification and Validation" | A First Course in Finite Elements | Fish & Belytschko | https://www.wiley.com/en-us/A+First+Course+in+Finite+Elements-p-9780470035801 | verified 2026-09-15
Book: ch 3 "Load and Stress Analysis" §3-1 "Equilibrium and Free-Body Diagrams" (pp. 72-75, 9th ed.) - read the section only, not the chapter | Shigley's Mechanical Engineering Design | Budynas & Nisbett | - | verified 2026-09-15
Interactive: PhET Balancing Act - 15 min for torque intuition before the math.   Theory: Shigley Ch 3 (equilibrium and FBDs). Skip the rest until Phase 3.

## Deliverable

FBD of the 2-link arm holding 0.5 kg at full horizontal extension. Calculate holding torque at the shoulder joint.

## Pass Condition

### MVM
- [ ] FBD drawn with all forces labeled, directions correct
- [ ] ΣF = 0 and Στ = 0 applied correctly
- [ ] Torque = F × perpendicular distance
- [ ] Numerical answer with units

### Full Pass
- [ ] Can identify what happens to torque if elbow extends further
- [ ] Can solve for reaction forces at the base
- [ ] **FEM intuition:** Can explain what FEM does in one paragraph: discretize geometry into elements → each element has a stiffness relation → assemble into global system → apply boundary conditions → solve for displacements → derive stresses. Can explain: the mesh is an approximation; finer mesh → more accurate but more compute; boundary conditions dominate the result more than mesh density; a point load creates infinite stress (artifact, not reality); hand calcs validate FEA, not the other way around. **Tool awareness:** in Phase 3 you will run FEA in PrePoMax (free, open-source GUI wrapping the CalculiX solver). You design in Solid Edge, export STEP, import into PrePoMax. The hand calc from THIS milestone is what you validate the PrePoMax result against. Install nothing now. Just know the pipeline exists.

> [!warning] ⚠️ Landmines
> 1. **Torque is force times PERPENDICULAR distance.** `[COMMUNITY]`
>    τ = F × d⊥. For a non-horizontal arm, the moment arm changes.
>
> 2. **Signs are arbitrary but must be consistent.** `[HYPOTHESIS]`
>    Choose CW = positive or CCW = positive. Write it down. Don't flip mid-problem.
>
> 3. **Static analysis assumes no motion.** `[HYPOTHESIS]`
>    This gives holding torque. Dynamic torque, acceleration, requires inertia. Motor sizing needs both.
>
> 4. **FEM is not a black box that gives the right answer.** `[HYPOTHESIS]`
>    Garbage in → garbage out. If your boundary conditions are wrong, the prettiest color contour is meaningless. The hand calc from THIS milestone is what you validate the FEA against in Phase 3. Learn what FEM does now, so you're not trusting a color picture blindly later.
>
>

---

# Milestone 0.5 — Circuits Basics

> [!info] 📚 Resources — Circuits Basics
> **Read:** Horowitz & Hill, *The Art of Electronics* (3rd ed.) — ch 1 "ONE: Foundations" (1.2 "Voltage, current and resistance"; 1.6 "Diodes and diode circuits"); hands-on DC laws + meters: Hayes & Abrams, *Learning the Art of Electronics* (2nd ed.) ch 1N "DC Circuits" / 1L "Lab: DC Circuits".
> **Visual:** *(substitute only)* GreatScott! *Electronic Basics #8: LEDs and current limiting resistors* and *#16: Resistors*; w2aew *#9: Basic 1X and 10X Oscilloscope Probe tutorial* — the probe/ground discipline is the one thing here a book handles poorly.
> **Interactive:** Falstad — build LED+resistor, watch current, then measure it. PhET *Circuit Construction Kit: DC* for KCL/multi-loop.
> **Theory:** KVL + Ohm only. Rizzoni ch 1-2 as backup; AoE ch 1 is the primary and is verified.

<a id="m0-5"></a>
Lenses - m0-5
Rigorous: Electronic Basics #16: Resistors | GreatScott! | https://www.youtube.com/watch?v=7w5I-KbJ1Sg | approved
Intuitive: Electronic Basics #8: Everything about LEDs and current limiting resistors | GreatScott! | https://www.youtube.com/watch?v=Qlayua3yjuE | approved
Book: ch 1 "ONE: Foundations" (1.2 Voltage, current and resistance; 1.6 Diodes and diode circuits; Appendix O The Oscilloscope) | The Art of Electronics (3rd ed.) | Horowitz & Hill | https://artofelectronics.net/the-book/table-of-contents/ | verified 2026-09-15
Book: ch 1N "DC Circuits" (1N.2 Three laws) + ch 1L "Lab: DC Circuits" (1L.2 Meters, VOM and DVM) + ch 13N.3 "Sketchy datasheets for LED and phototransistor" | Learning the Art of Electronics (2nd ed.) | Hayes & Abrams | https://learningtheartofelectronics.com/about-the-book/table-of-contents/ | verified 2026-09-15
Interactive: Falstad - build LED+resistor, watch current, then measure it.   Theory: Rizzoni Ch 1-2 / Horowitz and Hill intro. KVL + Ohm only.

## Deliverable

Calculate the current-limiting resistor for an LED, Vf = 2.2V, If = 20mA, from a 5V pin. Simulate in Falstad. Verify with multimeter on real hardware.

## Pass Condition

### MVM
- [ ] Correct resistor value using KVL + Ohm's Law
- [ ] Physical intuition: voltage = pressure, current = flow, resistance = opposition
- [ ] Simulation matches calculation

### Full Pass
- [ ] KCL at a branching node
- [ ] KVL around a multi-component loop
- [ ] Can read a datasheet for Vf and If max
- [ ] Can explain measurement setup: DMM in parallel for voltage, in series for current; scope probe ground and 1x/10x settings

> [!warning] ⚠️ Landmines
> 1. **Voltage is ACROSS, current is THROUGH.** `[COMMUNITY]`
>    Voltage: probes in parallel. Current: meter in series, break the circuit.
>
> 2. **Absolute maximum ratings are not guidelines.** `[COMMUNITY]`
>    20mA LED at 25mA continuously dies early. Design below max, not at it.
>
> 3. **Falstad is a teaching tool, not precision.** `[HYPOTHESIS]`
>    Use it for topology and direction. Use a real multimeter for real numbers.
>
>

---

# Milestone 0.6 — Power, Efficiency, Thermal

> [!info] 📚 Resources — Power, Efficiency & Thermal
> **Read:** Horowitz & Hill, *The Art of Electronics* (3rd ed.) — **intermediate, assumes KVL/Ohm which 0.5 already covers**; ch 9 "NINE: Voltage Regulation and Power Conversion" §9.4 "Heat and power design"; ch 3 "THREE: Field-Effect Transistors" §3.5 "Power MOSFETs" for the device side. Beginner, no assumed background, free: Kuphaldt, *Lessons In Electric Circuits* Vol. I ch 2 "OHM'S LAW" §"Power in electric circuits".
> **Worked artifact:** TI **DRV8874** datasheet (SLVSF66A) — a real H-bridge in this milestone's exact regime. §8.2.1.2.2 "Power Dissipation and Output Current Capability" (p. 21) states P = I_RMS² × (R_DS(on)_HS + R_DS(on)_LS), the RDS(on)-vs-temperature caveat, and peak-vs-continuous current; §6.4 "Thermal Information" (p. 5). Companion: DRV8871 (SLVSCY9B) §10.3/§10.4; SPRA953D on the Rθ chain; CSD18532Q5B Fig. 4-8 for normalized RDS(on) vs temperature.
> **Visual:** *(substitute only)* The Engineering Mindset — *Why Electronics Need Cooling - transistor heat sink*.
> **Interactive:** hand-calc the H-bridge loss, confirm with a SPICE power readout. Falstad — build the H-bridge, plot load power vs I²R loss.
> **Theory:** P = VI = I²R (LEC Vol. I ch 2), then the junction-temperature chain RθJC + RθCS + RθSA. Reading RθJA in a datasheet is the load-bearing skill.

<a id="m0-6"></a>
Lenses - m0-6
Rigorous: DIY Buck Converter - How to step down DC voltage efficiently | GreatScott! | https://www.youtube.com/watch?v=m8rK9gU30v4 | approved
Intuitive: Inductors Explained - The basics how inductors work working principle | The Engineering Mindset | https://www.youtube.com/watch?v=KSylo01n5FY | approved
Book: ch 9 "NINE: Voltage Regulation and Power Conversion" §9.4 "Heat and power design"; ch 3 "THREE: Field-Effect Transistors" §3.5 "Power MOSFETs" (3rd ed.) | The Art of Electronics | Horowitz & Hill | https://artofelectronics.net/the-book/table-of-contents/ | verified 2026-09-15
Book: ch 2 "OHM'S LAW" §"Power in electric circuits"; ch 11 "BATTERIES AND POWER SYSTEMS" (Vol. I, DC; free, CC BY) | Lessons In Electric Circuits | Tony R. Kuphaldt | https://www.ibiblio.org/kuphaldt/electricCircuits/DC/DC_2.html | verified 2026-09-15
Book: doc SLVSF66A sec 8.2.1.2.2 "Power Dissipation and Output Current Capability" (p.21) + sec 6.4 "Thermal Information" (p.5) | DRV8874 H-Bridge Motor Driver datasheet | Texas Instruments | https://www.ti.com/lit/ds/symlink/drv8874.pdf | verified 2026-09-15
Book: doc SLPS322E sec 4.3 Fig. 4-8 "Normalized On-State Resistance vs Temperature" + sec 4.2 "Thermal Information" (RthetaJA 40 C/W on 1-in^2 2 oz Cu) | CSD18532Q5B 60 V NexFET Power MOSFET datasheet | Texas Instruments | https://www.ti.com/lit/ds/symlink/csd18532q5b.pdf | verified 2026-09-15
Book: doc SPRA953D sec 2 "RthetaJC Junction-to-Case" (Eq. 5: RthetaJC + RthetaCS + RthetaSA) | Semiconductor and IC Package Thermal Metrics | Edwards & Nguyen, TI | https://www.ti.com/lit/an/spra953c/spra953c.pdf | verified 2026-09-15
Unverified: ch ? (TOC not fetchable - no section claimed) | Fundamentals of Power Electronics (3rd ed., Springer 2020) | Erickson & Maksimovic | https://openlibrary.org/books/OL28227058M.json | unverified 2026-09-15
Interactive: hand-calc the H-bridge loss, confirm with a SPICE power readout.   Theory: Horowitz and Hill power/thermal; reading RthJA in a datasheet.

## Deliverable

H-bridge: 2A at 12V, Rds(on) = 0.05Ω, two switches in series. Calculate input power, heat loss, efficiency (conduction losses only — switching/gate-drive losses return in Phase 1.3/2.3). Heatsink needed?

## Pass Condition

### MVM
- [ ] P_in = V × I correct
- [ ] P_loss = I² × R_total correct
- [ ] Efficiency as percentage
- [ ] Knows what thermal resistance means
- [ ] System power budget sketched (rails, loads, peak vs nominal, fuse margin) — promoted from Full; the paper calc alone is superseded by 1.3 hardware measurement

### Full Pass
- [ ] Can find Rth_ja in a datasheet, estimate junction temperature
- [ ] Can apply to a real MOSFET
- [ ] Can sketch a system power budget: rails, loads, modes, peak vs nominal, fuse/regulator margin

> [!warning] ⚠️ Landmines
> 1. **Efficiency applies to the conversion stage, not the system.** `[HYPOTHESIS]`
>    H-bridge efficiency ≠ motor efficiency. Don't confuse them.
>
> 2. **Thermal resistance is additive in series.** `[COMMUNITY]`
>    Rth_j-c + Rth_c-hs + Rth_hs-amb. One alone gives the wrong answer.
>
> 3. **Rds_on increases with temperature.** `[COMMUNITY]`
>    Datasheet value is at 25°C. At 150°C it can be 2× higher.
>
>

---

# Milestone 0.7 — Materials, Failure, and Selection

> [!info] 📚 Resources — Materials, Failure & Selection
> **Read:** Ashby, *Materials Selection in Mechanical Design* (3rd ed.) — ch 4 "Material property charts" + ch 5 "Materials selection — the basics" (App. B "Material indices"). Mechanism half: Callister & Rethwisch, *Materials Science and Engineering* (10th ed.) ch 6 "Mechanical Properties of Metals", ch 7 "Dislocations and Strengthening Mechanisms", ch 8 "Failure", ch 17 "Corrosion and Degradation".
> **Visual:** *(substitute only)* The Efficient Engineer — *An Introduction to Stress and Strain*, *Understanding Material Strength, Ductility and Toughness*, *Understanding Fatigue Failure and S-N Curves*; Taylor Sparks *Ductile and Brittle Fracture*.
> **Interactive:** Cambridge DoITPoMS interactive charts — Young's modulus–Density (with exercises) and the 11-chart index. *(MatWeb 403s to automated fetch and is dropped.)*
> **Theory:** Ashby ch 5 §5.3 "Attribute limits and material indices" for the performance-index derivation; Callister ch 8 "Failure" for the fatigue S-N basis.

<a id="m0-7"></a>
Lenses - m0-7
Rigorous: Mechanics of Materials: Lesson 1 - Intro to Solids, Statics Review Example Problem | Jeff Hanson | https://www.youtube.com/watch?v=Y8tXHk3irqE | approved
Intuitive: An Introduction to Stress and Strain | The Efficient Engineer | https://www.youtube.com/watch?v=aQf6Q8t1FQE | approved
Book: ch 4 "Material property charts" + ch 5 "Materials selection - the basics" + App. B "Material indices" (3rd ed.) | Materials Selection in Mechanical Design | Michael F. Ashby | https://archive.org/download/ashby-materials-selection-in-mechanical-design-third-edition/Ashby-Materials%20Selection%20in%20Mechanical%20Design%20Third%20Edition.pdf | verified 2026-09-15
Book: ch 6 "Mechanical Properties of Metals"; ch 3 "The Structure of Crystalline Solids"; ch 7 "Dislocations and Strengthening Mechanisms"; ch 8 "Failure"; ch 17 "Corrosion and Degradation of Materials" (10th ed.) | Materials Science and Engineering: An Introduction | Callister & Rethwisch | https://bcs.wiley.com/he-bcs/Books?action=contents&itemId=1119405491&bcsId=10955 | verified 2026-09-15
Interactive: Cambridge DoITPoMS material selection charts - Young's modulus vs density, with exercises (MatWeb dropped: 403).   Theory: Ashby Materials Selection (indices chapter); Callister for crystal/fatigue.

## Deliverable

5mm diameter 6061-T6 rod, yield ≈ 276 MPa, FoS = 3. Calculate allowable stress and maximum axial tensile force. Then: select a material for the 2-DOF arm links using Ashby-style reasoning, and explain why cyclic loading changes the answer.

## Pass Condition

### MVM
- [ ] Allowable stress = yield / FoS
- [ ] Stress = F/A, rearranged for force
- [ ] Circular area = πr²
- [ ] Answer in Newtons
- [ ] Can explain WHY FoS > 1: load uncertainty, material variation, fatigue

### Full Pass
Depth rule: state correctly + apply to one example each. (derive) marks the three derivation gates; the rest are vocabulary with an example.
**A — mechanical behavior:** stress-strain, crystals, dislocations, hardness, toughness, fatigue.
- [ ] **Stress-strain curve anatomy (derive):** Can draw and label: elastic region (linear, slope = E), yield point (0.2% offset for metals without sharp yield), strain hardening region, ultimate tensile strength, necking, fracture. Can explain: area under the curve = toughness (energy to fracture). Peak stress = strength. Slope = stiffness. These are three different properties.
- [ ] **Crystal structure matters:** FCC (aluminum, copper, austenitic stainless) → close-packed planes glide easily → ductile. BCC (iron at room temp, tungsten) → high lattice friction (Peierls stress) on non-close-packed planes → stronger but less ductile at low temperature, ductile-brittle transition temperature exists. HCP (titanium, magnesium, zinc) → fewest slip systems → anisotropic, limited formability. Can explain: this is WHY aluminum bends and cast iron snaps.
- [ ] **Dislocations and work hardening:** Metals are 100–1000× weaker than theoretical bond strength because dislocations let planes slide incrementally. Cold working multiplies dislocations → they tangle → harder to move → material gets stronger but less ductile. This is why bending a paperclip back and forth makes it harder to bend, then it breaks.
- [ ] **Hardness:** Rockwell, Brinell, Vickers — all measure resistance to indentation. Correlates with tensile strength (empirical, not fundamental). Useful because it's a quick, non-destructive proxy. Can explain: harder ≠ tougher. A file is hard and brittle. A spring is tough and moderately hard.
- [ ] **Toughness vs. strength:** Strength = peak stress. Toughness = energy absorbed before fracture (area under stress-strain). A material can be strong but not tough (ceramic, hardened steel) or tough but not strong (rubber, annealed copper). Impact loading demands toughness. Static loading demands strength. Fatigue demands both.
- [ ] Fatigue (derive): S-N curve read, endurance limit identified, Goodman diagram sketched for a simple case
- [ ] Can explain: cyclic loading fails BELOW yield. Why.
**B — families + environment:** tempers, polymers, corrosion.
- [ ] Can explain 6061-T6 vs. 6061-O: precipitation hardening, solution treatment, aging. Not just "different strength."
- [ ] Polymer awareness: PLA vs. PETG vs. nylon — stiffness, creep, temperature limits. Which 3D-print material for a structural bracket? Why?
- [ ] Corrosion: galvanic series. Aluminum + steel fastener = problem. What's the fix?
**C — selection + failure analysis:** Ashby, fractography, wear/tribology.
- [ ] Ashby reasoning (derive): plot E/ρ vs. σ_y/ρ for aluminum, steel, titanium, CFRP, PLA. Which material for a stiff, light arm link? Can explain the trade-off.
- [ ] Failure analysis: can look at a fracture surface and distinguish ductile (dimpled) from brittle (flat, granular) from fatigue (beach marks).
- [ ] Can explain wear/tribology, stress concentration/notch sensitivity, fracture toughness, surface finish/coatings, and environment-assisted failure as separate design constraints.

> [!warning] ⚠️ Landmines
> 1. **Yield ≠ ultimate ≠ fatigue limit.** `[COMMUNITY]`
>    Yield: permanent deformation. Ultimate: fracture. Fatigue: failure after repeated cycling, well below yield. Your arm joints cycle thousands of times. Fatigue is the design constraint, not yield.
>
> 2. **FoS is not a buffer for not knowing the load.** `[HYPOTHESIS]`
>    Estimate the load first. FoS accounts for uncertainty in the estimate.
>
> 3. **6061-T6 ≠ generic aluminum.** `[COMMUNITY]`
>    -T6 is a heat treatment: solution treat → quench → artificial age. Precipitates (Mg₂Si) block dislocation motion. Annealed 6061-O has ~⅕ the yield strength (~55 MPa vs ~276 MPa). Verify alloy AND temper of your stock.
>
> 4. **Polymers creep at room temperature.** `[COMMUNITY]`
>    A 3D-printed bracket holding a static load will deform over weeks. PLA glass transition is ~60°C. Near a motor or in a hot car, it softens. PETG and nylon are better but still creep. This is not a footnote — it's a design constraint for any printed structural part.
>
> 5. **Galvanic corrosion is silent and structural.** `[COMMUNITY]`
>    Aluminum (anodic) + steel (cathodic) + moisture = aluminum dissolves. Anodize, isolate with nylon washers, or use stainless/aluminum fasteners. This kills outdoor or long-life builds.
>
> 6. **Ashby charts are selection tools, not answer keys.** `[HYPOTHESIS]`
>    The chart says CFRP is stiffer per unit weight than aluminum. It doesn't tell you about cost, machinability, joint design, or impact resistance. The chart narrows the field. Engineering judgment picks the winner.
>
> 7. **Hardness ≠ toughness ≠ strength.** `[COMMUNITY]`
>    These are three different properties that get conflated. A hardened gear tooth is hard (wear resistant) but can be brittle (low toughness). A leaf spring is tough (absorbs energy) but not particularly hard. Know which property your application demands.
>
> 8. **The ductile-brittle transition is real and kills.** `[COMMUNITY]`
>    BCC metals (structural steel) become brittle below a transition temperature. The Titanic's hull steel, Liberty ships in cold Atlantic. If your mechanism operates outdoors in winter, this matters. FCC metals (aluminum, copper) don't have this transition — another reason aluminum is popular.
>

## Dependencies that waste your week if hit backwards

- Do the basic stress/FoS calculation FIRST. The fatigue and selection reasoning builds on it.
- Draw the stress-strain curve from memory BEFORE reading about fatigue mechanisms. The curve is the map; fatigue is a territory on it.
- Look at real fracture surfaces (photos are fine) BEFORE reading about failure modes. The visual anchors the theory.


---

# Milestone 0.8 — Manufacturing Processes + DFMA

> [!info] 📚 Resources — Manufacturing & DFMA
> **Read:** Kalpakjian & Schmid, *Manufacturing Engineering and Technology* (8th ed.) — **intermediate, a reference to skim by section, not read cover to cover**; it assumes basic materials/strength (0.1-0.7). ch 10 "Fundamentals of Metal Casting", ch 12 "Metal Casting: Design, Materials, and Economics", ch 16 "Sheet-Metal Forming Processes and Equipment", ch 21 "Fundamentals of Machining", ch 23 "Machining Processes: Turning and Hole Making", ch 32 "Brazing, Soldering, Adhesive-bonding, and Mechanical Fastening", ch 34 "Surface Treatments, Coatings, and Cleaning". Then Boothroyd, Dewhurst & Knight, *Product Design for Manufacture and Assembly* — ch 3 "Product Design for Manual Assembly" is the single best DFA read and is self-contained.
> **Visual:** *(substitute only — the spine of this milestone is the two books above)* TriMech Group, *What is a K-Factor? - Sheet Metal Bend Allowance Explained*.
> **Interactive:** 3D-print a bracket, then redesign it for a mill; note what changed. Engineering LibreTexts *Design for Various Manufacturing Methods* ch 2 for the CNC / sheet-metal / casting / injection-molding rule lists — audit your own bracket against each list.
> **Theory:** Boothroyd-Dewhurst DFA (part-count minimum, z-axis assembly, self-locating features, fastener elimination). Tolerance economics: Jensen, *Introduction to Mechanical Design and Manufacturing* ch "Types of Cutting and Machining Process and Tolerances". Audit tier (advanced, look things up one process at a time): Bralla, *Design for Manufacturability Handbook* (2nd ed.).

<a id="m0-8"></a>
Lenses - m0-8
Rigorous: G and M Code - Titan Teaches Manual Programming on a CNC Machine | TITANS of CNC | https://www.youtube.com/watch?v=5XihF05K4yM | approved
Intuitive: Vertical Mill Tutorial 1: The Basics | Blondihacks | https://www.youtube.com/watch?v=FyuG-B95PQs | approved
Book: Introduction I.1 "What Is Manufacturing?" + I.3 "Design for Manufacture, Assembly, Disassembly, and Service"; ch 10 "Fundamentals of Metal Casting"; ch 12 "Metal Casting: Design, Materials, and Economics"; ch 16 "Sheet-Metal Forming Processes and Equipment"; ch 21 "Fundamentals of Machining"; ch 23 "Machining Processes: Turning and Hole Making"; ch 32 "Brazing, Soldering, Adhesive-bonding, and Mechanical Fastening"; ch 34 "Surface Treatments, Coatings, and Cleaning" (8th ed.) | Manufacturing Engineering and Technology | Kalpakjian & Schmid | - | verified 2026-09-15
Book: ch 2 "Selection of Materials and Processes"; ch 3 "Product Design for Manual Assembly"; ch 7 "Design for Machining"; ch 8 "Design for Injection Molding"; ch 9 "Design for Sheet Metalworking"; ch 10 "Design for Die Casting" (2nd ed.) | Product Design for Manufacture and Assembly | Boothroyd, Dewhurst & Knight | - | verified 2026-09-15
Book: Section 1 "General Design Principles for Manufacturability"; Section 3 "Metal Stampings"; Section 4 "Designing for Machining"; Section 5 "Castings"; Section 7 "Design for Assembly (DFA)"; Section 8 "Polished and Plated Surfaces" (2nd ed.) | Design for Manufacturability Handbook | James G. Bralla (ed.) | - | verified 2026-09-15
Book: ch "Types of Cutting and Machining Process and Tolerances" -> "Machining Cost and Tolerance", "Expected Tolerances" | Introduction to Mechanical Design and Manufacturing (open, CC BY-NC) | David Jensen | https://uark.pressbooks.pub/mechanicaldesign/chapter/types-of-cutting-and-machining-pocess-and-tolerances/ | verified 2026-09-15
Interactive: 3D-print a bracket, then redesign it for a mill; note what changed.   Theory: Boothroyd-Dewhurst DFA; GD and T only for fits you will use.

## Deliverable

Take a simple L-bracket: design it for CNC milling, then redesign the same function for sheet metal bending. Document what changed, what became impossible, what became free. Then: redesign it for minimum part count and fastest assembly. Write 5 DFM rules and 3 DFA rules you'll follow in Phase 3.

## Pass Condition

### MVM
- [ ] Can name the 4 primary manufacturing families: machining, forming, casting, molding
- [ ] Can state 3 things a 3-axis CNC mill cannot do (internal sharp corners, undercuts without special tooling, features on non-accessible faces)
- [ ] Can state 3 sheet metal constraints (minimum bend radius, K-factor for flat pattern, grain direction)
- [ ] Bracket sketch for CNC with DFM annotations
- [ ] Bracket sketch for sheet metal with DFM annotations

### Full Pass
- [ ] Can explain: casting needs draft angles and fillets. Why. (Pattern removal, stress concentration.)
- [ ] Can explain: injection molding needs uniform wall thickness, draft, ribs instead of thick sections. Why. (Sink marks, warpage, cycle time.)
- [ ] Can name 2 joining methods beyond bolts: adhesives, brazing, rivets (welding is BANNED in this roadmap — name it only to rule it out). When each is appropriate.
- [ ] Can name 2 surface treatments and why: anodizing (corrosion + wear), powder coat (corrosion + aesthetics), plating, passivation.
- [ ] **DFA — Design for Assembly:**
- Can explain the Boothroyd-Dewhurst principles: minimize part count (does this part NEED to be separate?), design for z-axis assembly (parts stack downward, no flipping), self-locating features (dowels, tabs, asymmetric holes — parts can only go together one way), minimize fasteners (snap-fits, adhesives replace screws — welds excluded: banned in this roadmap), avoid flexible parts (cables, O-rings, gaskets are hard to automate).
- Can look at a 5-part assembly and identify: which parts could be merged? Which fasteners could be eliminated? Which features would make assembly foolproof?
- Can explain: the cheapest part is the part you didn't design. The cheapest fastener is the one you didn't add. Assembly time often exceeds manufacturing time.
- [ ] 5 personal DFM rules written down, specific enough to check against in Phase 3
- [ ] 3 personal DFA rules written down
- [ ] Can look at a part photo and identify the likely manufacturing process

> [!warning] ⚠️ Landmines
> 1. **CNC design rules ≠ 3D print design rules.** `[HYPOTHESIS]`
>    A 3D printer can make internal cavities, overhangs, and organic shapes. A mill cannot. Internal sharp corners are impossible — the tool is round. Undercuts require special tooling or multi-axis. If you design for 3D print and send it to a machine shop, you'll get a confused email or an expensive part.
>
> 2. **Sheet metal is not "thin CNC."** `[COMMUNITY]`
>    Bend radius is a function of material and thickness. The flat pattern is NOT the bent shape unfolded naively — the K-factor accounts for neutral axis shift. Get this wrong and your holes don't line up after bending.
>
> 3. **DFM is a design constraint, not a post-review.** `[HYPOTHESIS]`
>    "Can this be made?" should be asked at sketch stage. Redesigning after CAD is done costs 5× more than designing correctly the first time. The 5 rules you write here become a checklist in Phase 3.
>
> 4. **You don't need to master these processes. You need to not be surprised by them.** `[HYPOTHESIS]`
>    The goal is vocabulary and constraints. When the machine shop says "we can't hold that tolerance on a thin wall" or "this needs a fillet," you should know what they mean and why. Not how to run the machine yourself.
>
> 5. **Tolerances cost money nonlinearly.** `[COMMUNITY]`
>    ±0.5mm is nearly free. ±0.1mm is normal. ±0.01mm is expensive. ±0.005mm is very expensive. Only tighten tolerances where function demands it. A bearing seat needs tight tolerance. A cosmetic cover does not.
>
> 6. **DFA is not "make it easy to assemble." It's "make it impossible to assemble wrong."** `[COMMUNITY]`
>    Self-locating features, asymmetric hole patterns, keyed connectors. If a part CAN go in backwards, it WILL go in backwards, at 2 AM, during a debug session, when you're tired. Poka-yoke is not optional polish. It's the difference between a 10-minute assembly and a 2-hour mystery.
>
> 7. **Part count is the highest-leverage DFA variable.** `[COMMUNITY — Boothroyd-Dewhurst]`
>    Every additional part adds: one manufacturing operation, one inventory line, one assembly step, one potential failure point, one tolerance stack contributor. Before adding a part, ask: does it NEED to move relative to its neighbor? Does it NEED a different material? Does it NEED to be separate for service? If no to all three, merge it.
>

## Dependencies that waste your week if hit backwards

- Do the CNC bracket sketch BEFORE the sheet metal one. Machining is more intuitive; forming introduces the flat-pattern complication.
- Do the DFA redesign AFTER the DFM sketches. You need to know what's manufacturable before you can judge what's assemblable.
- Write the DFM + DFA rules BEFORE Phase 3, not during. You'll forget them under CAD pressure.


---

# Milestone 0.9 — Mechanisms & Kinematic Elements + Physical Testbed

> [!info] 📚 Resources — Mechanisms & Kinematic Elements
> **Read:** Norton, *Design of Machinery* (6th ed.) — ch 2 "Kinematics Fundamentals" (§2.4 Drawing Kinematic Diagrams, §2.5 Determining Degree of Freedom or Mobility, §2.11 Intermittent Motion, §2.13 The Grashof Condition); ch 8 "Cam Design" (§8.6 Sizing the Cam — Pressure Angle and Radius of Curvature); ch 9 "Gear Trains" (§9.9 Epicyclic or Planetary Gear Trains, §9.10 Efficiency of Gear Trains).
> **Visual:** *(substitute only — there is no book for mechanism-watching)* thang010146 (Dr. Nguyen Duc Thang) mechanism animations; Clickspring clockmaking; *507 Mechanical Movements*.
> **Interactive:** MechSimulator four-bar linkage sim (link sliders, live Grashof check s+l ≤ p+q, transmission angle, coupler curves); Cornell KMODDL Reuleaux collection. GeoGebra/linkage sim — build a four-bar, flip the grounded link, watch the TYPE change (the Grashof inequality never changes — only which link is grounded does).
> **Theory:** Gruebler/Kutzbach mobility and Grashof rotatability — DOF = 3(n−1) − 2j₁ − j₂. Norton §2.5 and §2.13.
> **Fabrication:** 3D printer (FDM, PLA). No printer yet → cardboard + brass split pins. Same kinematics; Prusa *Calibration* category for print tolerance.

<a id="m0-9"></a>
Lenses - m0-9
Rigorous: Clockmaking - How To Make A Clock In The Home Machine Shop - Part 4 | Clickspring | https://www.youtube.com/watch?v=ZSXDIraHz3k | approved
Intuitive: Mechanical Models | Proto G Engineering (NOT thang010146 - oEmbed check 2026-09-15) | https://www.youtube.com/playlist?list=PLHGVjZ_tV_gwDwoV_0CX7QguS_Vkx2yzV | unverified 2026-09-15
Intuitive: Mechanism animations (channel) | thang010146 (Nguyen Duc Thang) | https://www.youtube.com/thang010146/videos | verified 2026-09-15
Book: ch 2 "Kinematics Fundamentals" (2.4, 2.5, 2.11, 2.13); ch 3 "Graphical Linkage Synthesis"; ch 8 "Cam Design" (8.6); ch 9 "Gear Trains" (9.9, 9.10) | Design of Machinery (6th ed.) | Robert L. Norton | https://designofmachinery.com/wp-content/uploads/2018/12/DOM-6ed-Contents-Sample.pdf | verified 2026-09-15
Interactive: GeoGebra/linkage sim - build a four-bar, flip the grounded link, watch the TYPE change.   Theory: Norton Design of Machinery Ch 1-5; Gruebler's equation.

## Deliverable

**Theory:** For each of 12 mechanisms: kinematic diagram, DOF via Gruebler's, input→output motion, mechanical advantage behavior, one real-world application.

**Physical artifact: the Parametric Mechanism Testbed.**
A baseplate (3D-printed or cardboard) with interchangeable mechanism modules that swap in and out by hand. This is the first portfolio artifact. It must be photographed and labeled, not left as a pile of parts.

**Fabrication constraints (Phase 0 envelope):**
- PLA, 0.2 mm layers. Pins: 3 mm steel dowel pins or printed axles.
- Print a tolerance calibration cube FIRST. A printed 3.0 mm hole will not fit a 3 mm pin. Print holes at 3.2–3.3 mm clearance. Measure with calipers (Milestone 0.10).
- NO adhesives beyond hot glue for cardboard versions. NO power tools.
- This is a demonstration model, not a machine. PLA joints wear after ~100 cycles. That is acceptable here and you should be able to say why.

## Pass Condition

### MVM
- [ ] 3 mechanisms modeled physically on the testbed
- [ ] Kinematic diagram drawn for each: links as lines, joints as symbols (revolute = circle, prismatic = square, cam = contact point)
- [ ] DOF counted using Gruebler's equation: DOF = 3(n-1) - 2j₁ - j₂ (planar). Can explain: n = links, j₁ = full joints (revolute/prismatic), j₂ = half joints (cam contact)
- [ ] Input→output motion stated for each: "continuous rotation → oscillation," "rotation → linear translation," etc.
- [ ] One real-world application named for each
- [ ] **Physical:** modules swap by hand, no tools; testbed photographed

### Full Pass
Depth rule: each mechanism below is its own sign-off (diagram + DOF + motion + application); state correctly + one example. This is a multiple of the MVM — spread across the phase, not one sitting.
- [ ] All 12 mechanisms below covered (diagram + DOF + motion + application)
- [ ] **Four-bar linkage:** Can explain Grashof condition (s + l ≤ p + q). Can identify: crank-rocker (shortest link is a side link, adjacent to ground, and driven), double-crank / drag-link (shortest link is ground), double-rocker (shortest link is the coupler; non-Grashof s + l > p + q is always double-rocker). Re-grounding the same four bars changes the type — the Grashof inequality itself does not change. Can explain: the same four bars behave completely differently depending on which link is grounded and driven.
- [ ] **Slider-crank:** Can explain: this is a four-bar with one revolute joint replaced by a prismatic joint. Engine piston = slider-crank. Can explain dead-center positions and why a flywheel is needed.
- [ ] **CAM and follower:** Can explain: the cam profile IS the motion program. Follower displacement, velocity, acceleration are determined by the profile shape. Can explain pressure angle and why > 30° causes jamming/side-loading. Can explain undercutting and why it limits how aggressive the profile can be.
- [ ] **Geneva mechanism:** Can explain: converts continuous rotation to intermittent rotation (indexing). The driver has a pin that engages slots in the driven wheel. Can explain: the driven wheel dwells (locks) between engagements. Can explain: acceleration is HIGH at pin entry — not suitable for high speed without modification. Application: film projectors, indexing tables, mechanical watches.
- [ ] **Ratchet and pawl:** Can explain: permits motion in one direction, blocks the other. Can explain: this is NOT a precision indexing mechanism — backlash is inherent. Application: winches, socket wrenches, anti-backdrive on lead screws, bicycle freewheel.
- [ ] **Scotch yoke:** Can explain: converts rotation to pure sinusoidal linear motion (x = r·sin θ). Simpler than slider-crank AND lower peak acceleration at finite rod length (the crank's rod angularity adds a 2nd harmonic on top of the sine). Application: some pumps, valve actuators, vibration testing.
- [ ] **Oldham coupling:** Can explain: connects two parallel but offset shafts. Three discs: two attached to shafts, one floating with perpendicular tongues. Accommodates parallel misalignment but NOT angular misalignment. Can explain: the center disc traces a circle. Application: encoders, stepper motor connections where shafts aren't perfectly aligned.
- [ ] **Universal joint (Hooke's joint):** Can explain: connects two shafts at an angle. Can explain: output velocity is NOT constant even if input is — it oscillates at 2× shaft speed. Can explain: a double Cardan (two U-joints phased correctly) cancels the velocity fluctuation. Application: driveshafts, steering columns.
- [ ] **Leaf spring / compliant mechanism:** Can explain: a leaf spring is a structural element with DESIGNED compliance. It stores energy, provides suspension, and can act as a flexure (no friction, no wear, no backlash). Can explain: fatigue life is the design constraint — the spring cycles millions of times. Application: vehicle suspension, MEMS flexures, compliant grippers, electrical contacts.
- [ ] **Planetary gear (epicyclic):** Can explain: sun + planets + ring + carrier. Can explain the ratio formula: ω_s·N_s + ω_r·N_r = ω_c·(N_s + N_r). Can explain: load is shared across planets → compact, high torque density. Can explain: one element must be held fixed (or two inputs needed) to get a defined ratio. Application: automatic transmissions, robot joint reducers, drill drivers.
- [ ] **Ball screw / lead screw:** Can explain: converts rotation to linear motion. Ball screw: recirculating balls → low friction (~90% efficient), backdrivable. Lead screw (Acme/trapezoidal): sliding contact → high friction (~30-50% efficient), often self-locking. Can explain: backdrivability matters — if the load can drive the screw backwards, you need a brake or a self-locking screw. Application: CNC machines (ball screw), vises (lead screw), 3D printers (lead screw).
- [ ] **Belt and chain drive:** Can explain: timing belts (toothed) maintain synchronization, no slip. V-belts rely on friction, can slip (sometimes a feature — overload protection). Roller chains: high strength, positive engagement, need lubrication. Can explain: tensioning matters — too loose → skip/slap, too tight → bearing overload. Application: 3D printers (GT2 timing belt), motorcycles (chain), automotive accessories (serpentine belt).
- [ ] **Physical:** 5+ modules on the testbed; kinematic diagrams posted beside them; 60-second video narrating each mechanism

> [!warning] ⚠️ Landmines
> 1. **Gruebler's equation counts DOF, not motion quality.** `[HYPOTHESIS]`
>    A four-bar with DOF = 1 can be a crank-rocker, double-crank, or double-rocker depending on which link is grounded and the Grashof condition. DOF tells you HOW MANY inputs you need. It doesn't tell you WHAT the output does.
>
> 2. **CAM pressure angle is not a suggestion.** `[COMMUNITY]`
>    Pressure angle > 30° → the follower side-loads against its guide → friction → jamming → wear. The cam profile must be designed to keep pressure angle bounded. You can't just draw a "nice shape" and expect it to work.
>
> 3. **Geneva mechanisms have brutal acceleration spikes.** `[COMMUNITY]`
>    At the moment the driving pin enters the slot, the driven wheel goes from zero velocity to finite velocity nearly instantaneously. This is a jerk (derivative of acceleration) spike. At high speed, this causes impact, noise, and wear. Modified Geneva (curved slots, multi-pin) reduces this but doesn't eliminate it.
>
> 4. **Ratchet and pawl is NOT precision.** `[HYPOTHESIS]`
>    The pawl rides on the ratchet teeth. There's always backlash (the angular play between pawl and tooth). For precision indexing, use a Geneva, a cam indexer, or a servo. Ratchets are for holding and rough indexing.
>
> 5. **Leaf springs are not "weak springs."** `[COMMUNITY]`
>    A leaf spring in a truck suspension carries tons. It's a structural element with designed compliance. The design constraint is fatigue life, not stiffness. If you 3D-print a "leaf spring" in PLA, it will creep and fail. Spring steel (high-carbon, hardened and tempered) or composite (GFRP/CFRP) is the material.
>
> 6. **Planetary gear load sharing is not automatic.** `[COMMUNITY]`
>    In theory, 3 planets share the load equally. In practice, manufacturing tolerances mean one planet carries more. This is why high-quality planetary gears have floating sun gears or compliant planet mounts. If you buy a cheap planetary gearbox and it fails, it's usually the most-loaded planet.
>
> 7. **Backdrivability is a safety question, not just an efficiency question.** `[HYPOTHESIS]`
>    A ball screw is backdrivable: if the motor loses power, the load falls. A lead screw with a low helix angle is self-locking: the load holds. For a gravity-loaded axis (your arm's shoulder), this matters. If you use a backdrivable transmission, you need a brake or counterbalance. This connects directly to Phase 4's safety milestone.
>
> 8. **A mechanism is not a machine.** `[HYPOTHESIS]`
>    A mechanism transmits/transforms motion. A machine transmits/transforms motion AND force/energy. The four-bar in your car's windshield wiper is a mechanism. The wiper motor + linkage + blade is a machine. Know the difference: mechanism design is kinematics (geometry of motion). Machine design adds kinetics (forces, torques, power).
>
> 9. **Print tolerance is a landmine, not a footnote.** `[HYPOTHESIS]`
>    Every printed hole needs clearance compensation. Calibrate once (calibration cube + calipers), then use one compensation value for the whole testbed. If you skip calibration, you'll reprint every module once.
>
> 10. **PLA joints wear; that's the lesson, not a failure.** `[COMMUNITY]`
>     After 50–100 cycles a press-fit PLA pin loosens. Document it. This is exactly why Phase 3 uses CNC aluminum + real bearings. Feeling the difference IS the curriculum.
>

## Dependencies that waste your week if hit backwards

- Learn Gruebler's equation FIRST. It's the sanity check for every mechanism. If your diagram says DOF = 2 but you only have one motor, something's wrong.
- Draw the kinematic diagram BEFORE building the physical/CAD model. The diagram strips away the geometry and shows the topology. If the diagram is wrong, the model is wrong.
- Study the four-bar FIRST. It's the foundation. Slider-crank is a four-bar variant. Geneva is a modified four-bar. Understanding Grashof unlocks the rest.
- Do the leaf spring / compliant mechanism AFTER the rigid-body mechanisms. Compliance is a design choice that replaces joints. You need to understand joints first.
- Print the calibration cube BEFORE printing mechanism modules. Measure, compensate, then print.


---

# Milestone 0.10 — Metrology + Measurement Uncertainty

> [!info] 📚 Resources — Metrology & Measurement
> **Read:** NPL *Callipers and micrometers* (GPG40) — "Set-up, preparation and measurements" + "Factors affecting calliper performance"; then NPL GPG11 sec 7.1/7.4 and JCGM 100:2008 (GUM) sec 5-7 for the uncertainty budget.
> **Visual:** *(substitute only)* Mitutoyo America *How To Read A Mitutoyo Dial Caliper*; Travers Tool *How To Read A Dial Indicator*; Khan Academy *Precision in measurement* — useful for instrument hand-skills, which the NPL guides describe but do not demonstrate.
> **Interactive:** measure the same printed cube 10×; compute mean, std dev, uncertainty. NIST Uncertainty Machine (uncertainty.nist.gov) checks the RSS budget.
> **Theory:** GUM basics — resolution vs accuracy, repeatability, systematic vs random error. JCGM 100:2008 sec 4.2/4.3 (Type A / Type B).

<a id="m0-10"></a>
Lenses - m0-10
Rigorous: Precision in measurement | Science toolkit | Khan Academy | https://www.youtube.com/watch?v=ClW4x6OPDPQ | approved
Intuitive: Measuring with English and Metric Dial Calipers | Starrett product demo (uploaded by A&M Industrial) | https://www.youtube.com/watch?v=dgmNBEEN3gM | approved
Book: NPL GPG40 "Callipers and micrometers" sec "Set-up, preparation and measurements" + "Factors affecting calliper performance" | National Physical Laboratory | NPL | https://www.npl.co.uk/resources/gpgs/callipers-micrometers | verified 2026-09-15
Book: NPL GPG11 "A Beginner's Guide to Uncertainty of Measurement" sec 3.5/3.6, 5.1, 7.1, 7.4, 9 | Stephanie Bell, NPL | NPL | https://www.npl.co.uk/resources/gpgs/beginners-guide-measurement-uncertainty-gpg11 | verified 2026-09-15
Book: JCGM 100:2008 (GUM) sec 4.2 "Type A evaluation", 4.3 "Type B evaluation", 5 "Combined standard uncertainty", 6 "Expanded uncertainty", 7 "Reporting" | JCGM/WG1 | BIPM | https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf/cb0ef43f-baa5-11cf-3f85-4dcd86f77bd6 | verified 2026-09-15
Interactive: measure the same printed cube 10x; compute mean, std dev, uncertainty in a spreadsheet or Python.   Theory: GUM basics - resolution vs accuracy, repeatability, systematic vs random error.

## Deliverable

A documented measurement of a testbed part from Milestone 0.9:
- Nominal dimension (from CAD or drawing)
- Measured dimension (mean of 10 readings)
- Type A uncertainty (repeatability: std dev / √n)
- Type B uncertainty (instrument: resolution / √12 for quantization, PLUS accuracy spec / calibration offset / thermal — RSS them; a ±0.03 mm caliper is dominated by accuracy, not its 0.01 mm resolution)
- Combined uncertainty (root-sum-square)
- Stated as: `dimension = X ± U mm (k=2, ~95%)`

This is the foundation of every characterization in Phases 1–4. A torque constant measured
with a sloppy lever-arm length is worthless. Metrology first, always.

**Fabrication constraints (Phase 0 envelope):** no fabrication. You measure what you already printed. Tools: calipers, dial indicator (if owned), steel ruler.

## Pass Condition

### MVM
- [ ] Can read calipers correctly (outside, inside, depth) and zero them
- [ ] Can state a measured dimension with units
- [ ] Understands: resolution ≠ accuracy ≠ precision

### Full Pass
- [ ] 10 repeated measurements recorded in `data/raw/`
- [ ] Type A and Type B uncertainty computed; combined by RSS
- [ ] Measurement stated with uncertainty and coverage factor
- [ ] Can explain systematic vs random error, and why averaging fixes one but not the other
- [ ] Can explain why "25.43 mm" is meaningless without stating the instrument
- [ ] Dial indicator used to check flatness or runout of a printed part (if available)
- [ ] Ambient temperature noted in the log (habit-building for later phases)

> [!warning] ⚠️ Landmines
> 1. **Caliper resolution is not caliper accuracy.** `[COMMUNITY]`
>    A $30 caliper reads 0.01 mm but may be accurate to ±0.03 mm. Check it against a known dimension (gauge pin, drill bit shank with stamped size) and record the offset.
>
> 2. **3D-printed dimensions are not your CAD.** `[HYPOTHESIS]`
>    FDM shrinks with material and process (calibrated PLA ~0.1–0.3% in XY; ABS/nylon differ — measure your printer, don't trust a universal number). A 25 mm cube prints at ~24.95 mm. That is a PROCESS error, not a measurement error. Your uncertainty budget covers the measurement; the CAD-to-part gap is a separate, documented thing.
>
> 3. **Squeezing the caliper lies.** `[HYPOTHESIS]`
>    Too much jaw force deforms PLA and reads small. Use the thumb roller gently; same force every reading, which is why you repeat 10×.
>
> 4. **Parallax on dial indicators.** `[COMMUNITY]`
>    Read the face straight-on. Angled reads are ±0.02 mm off.
>
> 5. **Uncertainty is not "I'm not sure."** `[HYPOTHESIS]`
>    It is a quantitative claim about where the true value lies. Stating it is what separates a lab report from a guess, and it is exactly what you'll attach to the QDD's torque constant in Phase 3.
>

## Dependencies that waste your week if hit backwards

- Buy calipers BEFORE this milestone.
- Measure a part FROM Milestone 0.9 so the two artifacts connect.
- Finish this BEFORE Phase 1: the VCA's lever arm, the load cell calibration, and every Phase 3 bearing fit inherit this skill.


---

# Phase 0 Deload / Synthesis

No new inputs.
- [ ] Re-solve all 10 milestone deliverables from memory, blank page
- [ ] Red-pen every hesitation
- [ ] One-page synthesis sheet
- [ ] Safety setup verified and reflexive
- [ ] 5 DFM rules + 3 DFA rules readable and specific
- [ ] Can draw kinematic diagrams for 3 mechanisms from memory
- [ ] Can draw and label a stress-strain curve from memory
- [ ] Can state a measurement with its uncertainty from memory
- [ ] **Physical:** testbed photographed and labeled; metrology log committed
- [ ] Run `scripts/versions.sh`

## Phase 0 Retro

Actual time vs. range, 8–14 wk:
Most useful concept for what comes next:
What I'd tell someone starting Phase 0:
Missing landmine:
