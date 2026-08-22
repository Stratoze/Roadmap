
# Phase 0 — Foundations & Vocabulary

## Outcome

The physics, math, and reasoning base that everything else depends on.
Vectors, calculus intuition, statics, circuits, power, materials, manufacturing, the kinematic vocabulary of machines, and the metrology to measure what you build.

You don't need to master these before building. You need them at "Applied" level — you've solved a real problem with each one, not just followed a derivation.

The test: close the notes and solve a new version of the problem.
If you can, move on. If you can't, find the gap and close it.

**Physical artifacts of this phase:**
1. Parametric Mechanism Testbed — 3D-printed (or cardboard) baseplate with 5+ interchangeable mechanisms
2. Metrology Kit — calipers + dial indicator + documented measurement uncertainty

**Fabrication & safety envelope (Phase 0):**
- Cardboard, hand tools, hobby knife, 3D printer only.
- NO soldering. NO power tools. USB / 5V only for the blinky speed run.
- Eye protection when clipping anything. Cut away from your body.

---

## Phase Pass Condition

### MVM
- [ ] Can re-solve each milestone task with notes open
- [ ] Can explain each concept aloud, Feynman test — stumble = gap
- [ ] Git repo + log + Anki deck operational
- [ ] Can state basic measurement sanity: voltage across, current through, scope ground/probe discipline, current-limited supply default
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
> **Visual:** your own [[_system/How to Learn]] (functional decomposition, first principles).
> **Interactive:** set up the toolchain and flash a blinky. That *is* the milestone — stop when it blinks.
> **Theory:** none. This is an environment milestone, not a theory one.

### Deliverable

Working dev environment, local Git repo with first commit, Anki deck, and a problem-solving vocabulary you can use when stuck.

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

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 0.2 — Vectors, Trig, Frames of Reference

> [!info] 📚 Resources — Vectors, Trig & Frames
> **Visual:** 3Blue1Brown *Essence of Linear Algebra* (vectors, linear combinations).
> **Interactive:** plot the 2-link arm tip in Python for a few (θ1,θ2); see the vector add.
> **Theory:** Craig *Introduction to Robotics* Ch 2 (frames & transformations) / Khan Academy — only what forward kinematics needs.

## Deliverable

Hand-calculated forward kinematics for a 2-link planar arm. Given link lengths and joint angles, find the tip position, X, Y.

## Pass Condition

### MVM
- [x] Can calculate tip position for given θ1, θ2, L1, L2
- [x] Understands world frame vs. link frame
- [x] Can draw the vector diagram, not just plug into a formula

### Full Pass
- [ ] Can modify: add a third link, rotate the base, change reference frame
- [ ] Dot product has physical meaning: projection

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
> > Log sessions in Daily/ notes using the unified template.
>

---

# Milestone 0.3 — Calculus Intuition

> [!info] 📚 Resources — Calculus Intuition
> **Visual:** 3Blue1Brown *Essence of Calculus* (derivative=rate, integral=accumulation).
> **Interactive:** Desmos — plot v(t)=2t, shade area to t=3, see it equals position. Confirm with scipy.
> **Theory:** intuition over symbolic fluency. Ulaby appendix.

## Deliverable

Given v(t) = 2t m/s: derive acceleration, calculate position at t = 3s by integration, explain the physical meaning of the area under the curve.

## Pass Condition

### MVM
- [ ] Can take a derivative of a polynomial
- [ ] Can integrate a polynomial with limits
- [ ] Can chain: position → velocity → acceleration and back
- [ ] Can explain: derivative = rate of change, integral = accumulation

### Full Pass
- [ ] Power → Energy by integration, same idea, different domain
- [ ] Can explain why area under v(t) is displacement without the formula

> [!warning] ⚠️ Landmines
> 1. **Calculus intuition ≠ calculus computation.** `[HYPOTHESIS]`
>    If you can compute ∫2t dt = t² but can't explain why integrating velocity gives position, the intuition is missing.
>
> 2. **You don't need symbolic fluency for embedded work.** `[HYPOTHESIS]`
>    Digital controllers use discrete approximations. But you need the continuous intuition to know if your approximation is correct.
>
> > Log sessions in Daily/ notes using the unified template.
>

---

# Milestone 0.4 — Statics + Free Body Diagrams

> [!info] 📚 Resources — Statics & FBDs
> **Visual:** The Efficient Engineer *Understanding Statics*; Jeffrey Hanson statics playlist (FBD gold standard).
> **Interactive:** PhET *Balancing Act* — 15 min for torque intuition before the math.
> **Theory:** Shigley Ch 3 (equilibrium & FBDs). Skip the rest until Phase 3.

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
> > Log sessions in Daily/ notes using the unified template.
>

---

# Milestone 0.5 — Circuits Basics

> [!info] 📚 Resources — Circuits Basics
> **Visual:** Efficient Engineer / ElectroBOOM (voltage=pressure, current=flow).
> **Interactive:** Falstad — build LED+resistor, watch current, then measure it.
> **Theory:** Rizzoni Ch 1–2 / Horowitz & Hill intro. KVL + Ohm only.

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
> > Log sessions in Daily/ notes using the unified template.
>

---

# Milestone 0.6 — Power, Efficiency, Thermal

> [!info] 📚 Resources — Power, Efficiency & Thermal
> **Visual:** Efficient Engineer heat-transfer videos.
> **Interactive:** hand-calc the H-bridge loss, confirm with a SPICE power readout.
> **Theory:** Horowitz & Hill power/thermal; reading RθJA in a datasheet.

## Deliverable

H-bridge: 2A at 12V, Rds(on) = 0.05Ω, two switches in series. Calculate input power, heat loss, efficiency. Heatsink needed?

## Pass Condition

### MVM
- [ ] P_in = V × I correct
- [ ] P_loss = I² × R_total correct
- [ ] Efficiency as percentage
- [ ] Knows what thermal resistance means

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
> > Log sessions in Daily/ notes using the unified template.
>

---

# Milestone 0.7 — Materials, Failure, and Selection

> [!info] 📚 Resources — Materials, Failure & Selection
> **Visual:** Efficient Engineer fatigue / stress-strain / ductile-vs-brittle.
> **Interactive:** MatWeb or Ansys Granta edu — look up 6061-T6, plot E/ρ vs σy/ρ.
> **Theory:** Ashby *Materials Selection* (indices chapter); Callister for crystal/fatigue.

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
- [ ] **Stress-strain curve anatomy:** Can draw and label: elastic region (linear, slope = E), yield point (0.2% offset for metals without sharp yield), strain hardening region, ultimate tensile strength, necking, fracture. Can explain: area under the curve = toughness (energy to fracture). Peak stress = strength. Slope = stiffness. These are three different properties.
- [ ] **Crystal structure matters:** FCC (aluminum, copper, austenitic stainless) → many slip systems → ductile. BCC (iron at room temp, tungsten) → fewer slip systems → stronger but less ductile, ductile-brittle transition temperature exists. HCP (titanium, magnesium, zinc) → fewest slip systems → anisotropic, limited formability. Can explain: this is WHY aluminum bends and cast iron snaps.
- [ ] **Dislocations and work hardening:** Metals are 100–1000× weaker than theoretical bond strength because dislocations let planes slide incrementally. Cold working multiplies dislocations → they tangle → harder to move → material gets stronger but less ductile. This is why bending a paperclip back and forth makes it harder to bend, then it breaks.
- [ ] **Hardness:** Rockwell, Brinell, Vickers — all measure resistance to indentation. Correlates with tensile strength (empirical, not fundamental). Useful because it's a quick, non-destructive proxy. Can explain: harder ≠ tougher. A file is hard and brittle. A spring is tough and moderately hard.
- [ ] **Toughness vs. strength:** Strength = peak stress. Toughness = energy absorbed before fracture (area under stress-strain). A material can be strong but not tough (ceramic, hardened steel) or tough but not strong (rubber, annealed copper). Impact loading demands toughness. Static loading demands strength. Fatigue demands both.
- [ ] Fatigue: S-N curve read, endurance limit identified, Goodman diagram sketched for a simple case
- [ ] Can explain: cyclic loading fails BELOW yield. Why.
- [ ] Can explain 6061-T6 vs. 6061-O: precipitation hardening, solution treatment, aging. Not just "different strength."
- [ ] Polymer awareness: PLA vs. PETG vs. nylon — stiffness, creep, temperature limits. Which 3D-print material for a structural bracket? Why?
- [ ] Corrosion: galvanic series. Aluminum + steel fastener = problem. What's the fix?
- [ ] Ashby reasoning: plot E/ρ vs. σ_y/ρ for aluminum, steel, titanium, CFRP, PLA. Which material for a stiff, light arm link? Can explain the trade-off.
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
>    -T6 is a heat treatment: solution treat → quench → artificial age. Precipitates (Mg₂Si) block dislocation motion. Annealed 6061-O has ~⅓ the yield strength. Verify alloy AND temper of your stock.
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

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 0.8 — Manufacturing Processes + DFMA

> [!info] 📚 Resources — Manufacturing & DFMA
> **Visual:** NYC CNC / This Old Tony / Real Engineering (real machining & sheet metal).
> **Interactive:** 3D-print a bracket, then redesign it for a mill; note what changed.
> **Theory:** Boothroyd-Dewhurst DFA; GD&T only for fits you'll use.

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
- [ ] Can name 2 joining methods beyond bolts: welding (TIG/MIG), adhesives, brazing, rivets. When each is appropriate.
- [ ] Can name 2 surface treatments and why: anodizing (corrosion + wear), powder coat (corrosion + aesthetics), plating, passivation.
- [ ] **DFA — Design for Assembly:**
- Can explain the Boothroyd-Dewhurst principles: minimize part count (does this part NEED to be separate?), design for z-axis assembly (parts stack downward, no flipping), self-locating features (dowels, tabs, asymmetric holes — parts can only go together one way), minimize fasteners (snap-fits, welds, adhesives replace screws), avoid flexible parts (cables, O-rings, gaskets are hard to automate).
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

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 0.9 — Mechanisms & Kinematic Elements + Physical Testbed

> [!info] 📚 Resources — Mechanisms & Kinematic Elements
> **Visual:** Thang010146 (mechanism animations); *507 Mechanical Movements*.
> **Interactive:** GeoGebra/linkage sim — build a four-bar, flip the grounded link, watch Grashof change it.
> **Theory:** Norton *Design of Machinery* Ch 1–5; Gruebler's equation.
> **Fabrication:** 3D printer (FDM, PLA). No printer yet → cardboard + brass split pins. Same kinematics.

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
- [ ] All 12 mechanisms below covered (diagram + DOF + motion + application)
- [ ] **Four-bar linkage:** Can explain Grashof condition (s + l ≤ p + q). Can identify: crank-rocker (shortest link is input), double-crank (shortest link is ground), double-rocker (shortest link is coupler). Can explain: the same four bars behave completely differently depending on which link is grounded.
- [ ] **Slider-crank:** Can explain: this is a four-bar with one revolute joint replaced by a prismatic joint. Engine piston = slider-crank. Can explain dead-center positions and why a flywheel is needed.
- [ ] **CAM and follower:** Can explain: the cam profile IS the motion program. Follower displacement, velocity, acceleration are determined by the profile shape. Can explain pressure angle and why > 30° causes jamming/side-loading. Can explain undercutting and why it limits how aggressive the profile can be.
- [ ] **Geneva mechanism:** Can explain: converts continuous rotation to intermittent rotation (indexing). The driver has a pin that engages slots in the driven wheel. Can explain: the driven wheel dwells (locks) between engagements. Can explain: acceleration is HIGH at pin entry — not suitable for high speed without modification. Application: film projectors, indexing tables, mechanical watches.
- [ ] **Ratchet and pawl:** Can explain: permits motion in one direction, blocks the other. Can explain: this is NOT a precision indexing mechanism — backlash is inherent. Application: winches, socket wrenches, anti-backdrive on lead screws, bicycle freewheel.
- [ ] **Scotch yoke:** Can explain: converts rotation to pure sinusoidal linear motion (x = r·sin θ). Simpler than slider-crank but higher peak acceleration. Application: some pumps, valve actuators, vibration testing.
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

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 0.10 — Metrology + Measurement Uncertainty

> [!info] 📚 Resources — Metrology & Measurement
> **Visual:** Mitutoyo/Starrett "how to read calipers and dial indicators" videos.
> **Interactive:** measure the same printed cube 10×; compute mean, std dev, uncertainty in a spreadsheet or Python.
> **Theory:** GUM basics — resolution vs accuracy, repeatability, systematic vs random error.

## Deliverable

A documented measurement of a testbed part from Milestone 0.9:
- Nominal dimension (from CAD or drawing)
- Measured dimension (mean of 10 readings)
- Type A uncertainty (repeatability: std dev / √n)
- Type B uncertainty (instrument resolution: resolution / √12)
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
>    FDM shrinks ~0.1–0.3% in XY. A 25 mm cube prints at ~24.95 mm. That is a PROCESS error, not a measurement error. Your uncertainty budget covers the measurement; the CAD-to-part gap is a separate, documented thing.
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

> Log sessions in Daily/ notes using the unified template.

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
