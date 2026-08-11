# Phase 3 — Model-Based Design & Verification

## Outcome

Professional-grade physical and electrical design, verified through a V-Model lifecycle.
From "works on the breadboard" to "manufacturable, reliable, documented."

This phase follows the V-Model: you ENTER with a software-in-the-loop proof that your
Phase 2 control algorithms work against a simulated plant, you DESIGN the mechanical and
electrical hardware informed by that proof, and you EXIT with a hardware-in-the-loop
validation that the physical controller behaves correctly against the real plant model.

The CAD is not the engineering. The PCB layout is not the engineering. The engineering is
knowing what the CAD is telling the machine shop to do, what the PCB layout is telling the
electromagnetic field to do, and having simulation evidence that the system will behave
correctly BEFORE you commit to fabrication.

**Physical artifact of this phase: the Quasi-Direct Drive (QDD) Actuator.**
- CNC-machined 6061-T6 housing (service-made)
- The Puck: custom circular 4-layer FOC driver PCB (JLCPCB/PCBWay)
- Purchased planetary gearbox (9:1–10:1) + BLDC stator/rotor
- Dual AS5048 encoders (motor side + output side)

This is the joint your Phase 4 arm is built from. Two of them.

**Fabrication & safety envelope (Phase 3):**
- NEW: CNC services (SendCutSend/Xometry/PCBWay). You design CAD; they machine. You never touch the machine.
- NEW: 4-layer PCB fabrication + stencil + hotplate/hot-air reflow. SMD now required.
- NEW: **48 V DC bus.** Read the 48 V section of the SAFETY_CARD before powering anything. Fuse before power. Discharge capacitors before touching.
- NEW: machined parts arrive with burrs — deburr before handling.
- Still NO welding, NO manual mill/lathe, NO mains.
- CNC discipline: order ONLY after (1) 3D-printed prototype fits, (2) FEA passes, (3) DFM review against your Phase 0 rules. A bad STEP sent early is money burned.

---

## Phase Entry Gate: Software-in-the-Loop Verification

Before opening CAD or KiCad, prove that your Phase 2 control stack works against a
simulated plant. This is the left side of the V: you verify the software against the model
before the hardware exists.

### Deliverable

Run the Phase 2 FOC firmware logic (or a faithful Python/C++ model of it) against the
Milestone 2.5 two-link arm dynamics model in a closed-loop simulation. Demonstrate that
the controller tracks commanded trajectories within acceptable error bounds.

### Pass Condition

- [ ] The Phase 2 FOC current loop model tracks Iq/Id step commands in simulation
with < 10% overshoot and < 5% steady-state error.
- [ ] The Phase 2.5 state-space model (or PID + feedforward) tracks a multi-waypoint
trajectory in simulation. Tracking error documented.
- [ ] The simulation includes actuator limits: torque saturation, current limits,
velocity limits. The controller handles saturation gracefully (anti-windup,
no divergence).
- [ ] The simulation includes the anti-aliasing filter phase lag from Milestone 1.3
analog front end. The control loop remains stable with the filter in the loop.
- [ ] All simulation scripts committed to `simulations/python/` with experiment notes
using `templates/experiment_note.md`.
- [ ] Results plotted and saved to `docs/captures/`.

### Why this gate exists

If you skip SIL and go straight to CAD/PCB, you will discover control problems during
hardware bring-up. Fixing a control algorithm in simulation costs an afternoon. Fixing it
after the PCB is fabricated and the arm is assembled costs weeks. The V-Model exists to
make failures cheap by finding them early.

### Landmines

1. **"I already tested FOC on hardware in Phase 2."** `[HYPOTHESIS]`
Phase 2 tested FOC on a single motor on a bench. Phase 3 requires the FULL control
stack (FOC + dynamics-aware feedforward + trajectory shaping) running against the
COUPLED two-link arm model. These are different problems. The coupled dynamics
introduce interactions that single-motor tests cannot reveal.
2. **Simulation without actuator limits is a lie.** `[HYPOTHESIS]`
If your sim allows infinite torque, the controller looks great. Add saturation.
If the controller winds up or diverges with saturation, fix it NOW, not on hardware.

---

## Phase Pass Condition

### MVM
- [ ] SIL gate passed (see Phase Entry Gate above)
- [ ] QDD actuator CAD assembly, interference-free
- [ ] Hand calcs: FoS > 2 on critical features
- [ ] FEA runs, roughly matches hand calcs
- [ ] Bearing selected: type, size, fit class, life calc documented
- [ ] Motor + gearbox sized: torque-speed, reflected inertia ratio, acceleration
- [ ] System power budget documented: every rail, every load, every mode
- [ ] Puck schematic passes ERC, layout passes DRC
- [ ] Power stage designed: regulator topology, bootstrap, inrush
- [ ] EMC rules applied: ground plane, switching node, routing
- [ ] Board powers up through current-limited supply
- [ ] 3D-printed QDD prototype assembled and checked before any CNC order
- [ ] HIL exit gate passed (see Phase Exit Gate below)

### Full Pass
- [ ] GD&T drawings with tolerance stack-up, release-ready
- [ ] FEA validated against hand calcs within 20%
- [ ] Shaft design: diameter, retaining method, axial location
- [ ] Fastener selection: bolt grade, preload, torque spec
- [ ] Fits documented: bearing-to-shaft, bearing-to-housing, with tolerance classes
- [ ] DFM review completed against Phase 0 rules before sending to fab
- [ ] Star grounding verified
- [ ] Trace widths sized for stall current
- [ ] Power stage: buck designed with computed values, not copied blindly
- [ ] EMC: can explain why the layout passes or fails
- [ ] Board runs FOC firmware ported from Phase 2
- [ ] QDD assembled: shaft turns smoothly by hand, zero axial play, backdrivable
- [ ] QDD characterized on the Phase 1 rig: Kt, Ke, torque-speed, backdrivability, thermal
- [ ] HIL: 3+ fault types injected, firmware enters safe state for each
- [ ] Mini-FMEA completed for mechanical and electrical using `templates/fmea.md`

---

## Pre-Design Requirements

Fill `templates/requirements_brief.md` before opening CAD or KiCad.

### Actuator Sizing (required before CAD)

Document:
- [ ] **Load torque:** gravity worst-case pose, friction, payload. Sum = continuous requirement.
- [ ] **Acceleration torque:** τ_acc = J_total × α, with J_load_reflected = J_load / N².
- [ ] **Torque-speed check:** operating point inside the motor curve with ≥ 30% margin.
- [ ] **Inertia ratio:** J_load_reflected / J_motor < 10:1. QDD targets LOW reflected inertia for backdrivability — this is the whole point. Document the ratio and the backdrivability target (output moves with < 0.5 N·m hand torque, motor unpowered).
- [ ] **Transmission:** planetary 9:1–10:1 purchased. You design the integration (coupling, bearings, housing), not the gears.
- [ ] **Gearbox choice documented:** backlash spec, efficiency, rated torque vs your worst case.

### System Power Budget (required before schematic)

Before opening KiCad, document:
- [ ] **Every rail:** 3.3 V logic, gate-drive rail, 48 V motor bus.
- [ ] **Every load per rail per mode:** idle, active, peak (stalled).
- [ ] **Regulator sizing** with 30% margin; LDO vs buck justified by dissipation.
- [ ] **Fuse sizing:** stall current + inrush. Slow-blow documented.
- [ ] **Supply sizing:** peak deliverable without current-limiting in normal operation.

### Mini-FMEA (required before design, updated after)

Complete `templates/fmea.md` for mechanical and electrical BEFORE design. Every item with
Severity × Occurrence ≥ 12 or RPN ≥ 48 needs a documented mitigation before proceeding.

---

# Milestone 3.1 — QDD Actuator: CAD + Machine Elements + FEA + Drawings

> [!info] 📚 Resources — QDD Mechanical Design
> **Visual:** MIT Mini Cheetah / Ben Katz actuator teardowns; Solid Edge CE tutorials; Jakub Michalski PrePoMax series.
> **Interactive:** model → STEP → PrePoMax static stress → validate vs hand calc. FreeCAD as macOS STEP viewer.
> **Theory:** SKF/NSK bearing-fit tables; fastener preload; GD&T; Shigley machine elements.
> **Fabrication:** Solid Edge CE for design; 3D print for prototype; CNC service for final housing.

## Deliverable

Complete QDD actuator mechanical design in Solid Edge CE: housing (two halves or tube + end caps), output shaft, bearing arrangement, gearbox integration, motor mounting, Puck mounting + cable exit, verified by hand calcs and FEA, with manufacturing drawings and a DFM review.

**Design sequence (this order is the lesson):**
1. Model the purchased parts first (motor, gearbox, bearings, encoders) from datasheets.
2. Design the integration around them: shaft, bearing seats, coupling, housing, Puck pocket, cable exit.
3. Print the whole assembly in PETG. Assemble. Find every interference. Fix in CAD.
4. FEA the housing (static stress at worst-case torque; note max stress location).
5. DFM review against your Phase 0 rules. Internal sharp corners → fillets. Tolerances: H7 housing bores, k6 shaft fits, called out on drawings.
6. THEN order CNC (1–2 housings, 6061-T6, as-machined; anodize optional and bearing bores masked if used).

## Pass Condition

### MVM
- [ ] Assembly modeled, interference-free
- [ ] At least one Poka-yoke feature
- [ ] Hand calc: worst-case stress on output shaft/housing, FoS documented
- [ ] FEA: static stress run, max stress location identified
- [ ] Bearing selected with fit classes documented
- [ ] **3D-printed prototype assembled; motor + gearbox + bearings fit**

### Full Pass
- [ ] All parts fully parametric
- [ ] **Bearing fits:** interference on the rotating ring, clearance on the stationary, per manufacturer tables; can explain why
- [ ] **Bearing life:** L10 = (C/P)³ × 10⁶ rev calculated at worst-case load
- [ ] **Shaft:** diameter from combined torsion + bending; axial location by shoulders/retaining rings
- [ ] **Fasteners:** grade, preload, torque spec; can explain joint stiffness vs fatigue
- [ ] Hand calcs for bending/shear/torsion on the critical feature
- [ ] FEA within 20% of hand calc; mesh convergence (3 densities, < 5% change between finest two)
- [ ] GD&T: concentricity of bearing bores, flatness of mating faces, perpendicularity
- [ ] Tolerance stack-up: worst-case AND RSS for the bearing→gearbox→shaft chain
- [ ] DFM review documented against Phase 0 rules; every part checked for 3-axis manufacturability
- [ ] CNC order placed AFTER prototype + FEA + DFM; parts received, deburred, assembled
- [ ] Housing + rotor assembly spins freely, no rubbing

> [!warning] ⚠️ Landmines
> 1. **CAD without constraints is sculpture.** `[HYPOTHESIS]`
>    Fully constrained sketches. Proper mates. Change one dimension → assembly updates, doesn't explode.
> 2. **FEA without hand calcs is a pretty picture.** `[COMMUNITY]`
>    Estimate max stress by hand, σ = Mc/I, τ = Tr/J, BEFORE running FEA. FEA always gives a number. The question is whether it's right.
> 3. **Boundary conditions are where FEA goes wrong.** `[COMMUNITY]`
>    Max stress at a constraint point → BCs are wrong. Point loads → infinite stress. Fix the model, not the mesh.
> 4. **Tolerance stack-up kills assemblies.** `[HYPOTHESIS]`
>    ±0.1mm per joint × 5 joints = ±0.5mm at tip. Calculate BEFORE ordering.
> 5. **3D printing ≠ CNC design rules.** `[HYPOTHESIS]`
>    The prototype is printed; the final part is milled. Internal sharp corners that print fine are impossible on a 3-axis mill. Redesign for the mill before ordering.
> 6. **Bearing fit is not "snug."** `[COMMUNITY]`
>    Too loose → the ring creeps on its seat and frets both surfaces. Too tight → assembly damage and radial preload that kills life. Use the ISO fit class from the bearing maker's table and put it on the drawing.
> 7. **Ordering CNC before the printed prototype is how you buy paperweights.** `[HYPOTHESIS]`
>    The print will reveal a 0.2 mm error somewhere — motor doesn't seat, Puck interferes, bolts foul the gearbox. Find it in $2 of PETG, not $150 of aluminum.
> 8. **Anodize grows into bores.** `[COMMUNITY]`
>    Type II adds ~10–25 µm per surface. A bearing bore that was a perfect fit becomes a press fit or impossible. Mask bearing bores or skip anodize.
> 9. **The cable exit is a design feature, not an afterthought.** `[HYPOTHESIS]`
>    The Puck's single connector (power + CAN) must exit the housing in a direction compatible with the arm's sweep. Decide it now; you can't drill it later without chips everywhere.
> 10. **Skipping the SIL gate makes mechanical design blind.** `[HYPOTHESIS]`
>     If the controller can't handle the coupled dynamics, you'll over-build (heavy, slow) or under-build (flexible, resonant). SIL tells you where the margins need to be.
>

## Dependencies that waste your week if hit backwards

- **SIL gate BEFORE CAD.**
- Motor + gearbox sizing (Pre-Design) BEFORE housing geometry — the purchased parts constrain everything.
- Hand calcs BEFORE FEA.
- Bearings selected BEFORE bore/shaft dimensions — you design around purchased bearings, never the reverse.
- Print + assemble the prototype BEFORE ordering CNC.
- DFM review BEFORE sending STEP files, not after the shop emails you questions.
- Verify the Solid Edge → STEP → PrePoMax pipeline on a 30-minute bracket BEFORE trusting it with the actuator.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 3.2 — The Puck: Custom FOC Driver PCB

> [!info] 📚 Resources — The Puck PCB
> **Visual:** Phil's Lab STM32 motor driver PCB series — watch before opening KiCad.
> **Interactive:** KiCad 9 — schematic → footprints → 4-layer layout → DRC → Gerbers → JLCPCB. Built-in PCB Calculator (IPC-2221) for trace widths.
> **Theory:** TI SLVA404 (buck layout); IPC-2221; ground-plane & switching-node EMC; your own Phase 1 analog front-end experience.
> **Fabrication:** JLCPCB/PCBWay 4-layer + stencil; hotplate or hot-air reflow. NEW soldering territory — budget time to learn it.

## Deliverable

**The Puck:** a circular, 4-layer PCB mounting on the back of the QDD motor:
STM32G4 (G431/G474) + 3-phase gate driver (DRV8323-class, integrated sense amps) +
3 low-side shunts + AS5048 SPI header (motor side) + second SPI header (output encoder) +
CAN-FD transceiver + 48 V input with reverse-polarity protection + buck to logic +
ONE connector out (power + CAN).

The circular form factor is deliberate: it's how real actuator makers (ODrive-class, MIT Cheetah-class) package drives — short motor phase traces, no external 3-phase cabling, one shielded cable leaving the joint.

## BOM Sanity

Before finalizing schematic:
- [ ] Every IC has manufacturer part number
- [ ] Every IC has orderable distributor SKU
- [ ] Every critical part has at least one substitute
- [ ] Package matches footprint
- [ ] Voltage/current/thermal ratings checked (48 V bus headroom included)
- [ ] Stock exists today or lead time acceptable

## Power Stage Design (required before layout)

- [ ] **Logic rail:** buck from 48 V to 3.3 V (an LDO at 48 V input is a heater — justify any LDO by dissipation math)
- [ ] **Gate drive supply** derived and sequenced
- [ ] **Bootstrap capacitor** computed: C_boot ≥ Q_g × V_gs / ΔV
- [ ] **Inrush:** NTC or soft-start; without it the supply current-limits and the MCU brown-outs
- [ ] **Reverse polarity protection:** the board survives a backwards plug
- [ ] **Test points** on rails, sense outputs, PWM, CAN
- [ ] **Sequencing:** logic stable before MCU runs; gate driver enabled only after rails good

## EMC Design (required before and during layout)

- [ ] **One solid ground plane** on layer 2. No splits. Analog/digital separated by placement.
- [ ] **Switching node** short (< 5 mm), narrow, away from encoder/SPI traces
- [ ] **Buck input cap** < 5 mm from VIN/GND pins; placed first
- [ ] **Motor phase traces** wide, short, sized for stall current
- [ ] **Encoder SPI** routed away from switching; 90° crossings where unavoidable
- [ ] **Decoupling:** 100 nF on every MCU power pin < 3 mm; 10 µF bulk per rail
- [ ] Can explain why the 50 ns PWM edges radiate and what each layout rule does about it

## Pass Condition

### MVM
- [ ] ERC + DRC clean; Gerbers accepted by fab
- [ ] Board assembled (stencil + hotplate or hot air)
- [ ] Powers up through current-limited supply, rails within ±10%
- [ ] MCU boots; blinky; CAN transceiver responds

### Full Pass
- [ ] Rails within ±5%; bootstrap voltage stable under load
- [ ] No solder bridges under magnification; rework logged honestly
- [ ] FOC firmware from Phase 2 ported; motor spins under Puck control
- [ ] Current sensing verified: inject known current, ADC matches within tolerance; offset calibrated
- [ ] AS5048 SPI verified at 1 kHz
- [ ] CAN-FD verified against a second node
- [ ] Buck efficiency measured > 85%
- [ ] EMC check: encoder stable while motor runs 50% duty; ADC noise < 5% FS under switching
- [ ] Thermal check: MOSFET temperature under continuous load (thermocouple), below limit
- [ ] Reverse polarity test: board survives
- [ ] **Physical:** Puck mounted in the housing from 3.1; fits; connector exit correct; photographed

> [!warning] ⚠️ Landmines
> 1. **Footprint mismatch kills the board.** `[COMMUNITY]`
>    For every non-trivial IC: datasheet → "Recommended PCB Land Pattern." Cross-reference pad count, pin 1, courtyard. SOT-23-5 vs SOT-23-6, SOIC-8 vs SOIC-8-EP, flipped pin 1. 5 min per IC. Missing it costs a 3-week fab cycle. **#1 because it ends the milestone.**
> 2. **Draw ground return paths as arrows BEFORE layout.** `[COMMUNITY]`
>    Motor return, ADC return, MCU return. If two arrows share a trace segment before the star point, that's noise injection.
> 3. **Trace width for stall current, not nominal.** `[COMMUNITY — IPC-2221]`
>    Stall is 3–5× running. Size for stall.
> 4. **Decoupling: < 3 mm means < 3 mm.** `[COMMUNITY]`
>    100 nF ceramic 2 cm away is decoration. Place decoupling first, then route.
> 5. **Fab wait IS the deload.** `[HYPOTHESIS]`
>    1–3 weeks. Don't start new theory. Documentation, cold-toolchain touches, synthesis.
> 6. **QFN parts need the hotplate path figured out BEFORE the board arrives.** `[HYPOTHESIS]`
>    Order the stencil with the PCB. Practice paste + reflow on a scrap board if you've never done it. Flux is not optional for hand-touch-up.
> 7. **Bootstrap capacitor is not "just a cap."** `[COMMUNITY]`
>    Too small → high-side gate sags → MOSFET linear region → thermal destruction. Too large → slow charge → startup delay. Compute from Q_g and allowable droop.
> 8. **Buck layout is not forgiving.** `[COMMUNITY]`
>    Input cap placement, switch node, feedback routing — follow the datasheet example exactly. Wrong → oscillation, EMI, dead regulator.
> 9. **Power sequencing is not "it'll probably be fine."** `[HYPOTHESIS]`
>    If the MCU starts before the gate driver supply is stable, PWM pins may float → MOSFETs partially on → shoot-through. Hold gate-driver enable low until rails are good.
> 10. **Ground plane splits are the #1 EMC mistake.** `[COMMUNITY]`
>     One solid plane. Separate analog/digital by placement. Star grounding is a power topology, not a plane split.
> 11. **The switching node is an antenna.** `[COMMUNITY]`
>     Short, narrow, and the ground plane under it is the shield — don't clear it away.
> 12. **48 V changes the fuse math.** `[HYPOTHESIS]`
>     Phase 1 habits (24 V, small currents) underestimate fault energy. Fuse for stall + inrush, and use a DC-rated fuse/holder.
>

## Dependencies that waste your week if hit backwards

- **SIL gate BEFORE schematic** — the sim constrains amplifier bandwidth and filter cutoffs.
- Verify ALL footprints BEFORE opening the layout editor.
- Ground return diagram BEFORE layout.
- Current-sensing topology decision (from 2.3) BEFORE choosing sense resistors/amplifiers.
- Power stage designed on paper BEFORE KiCad.
- System power budget BEFORE regulator selection.
- EMC rules applied DURING layout, never after.
- Order the stencil WITH the boards.
- Bench-test the Puck with the motor BEFORE mounting it in the housing — once it's inside, you can't probe.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 3.3 — QDD Actuator Assembly + Characterization

> [!info] 📚 Resources — QDD Assembly & Characterization
> **Visual:** actuator assembly videos (Mini Cheetah class); your own Phase 1 characterization captures as the template.
> **Interactive:** assemble → FOC on the Puck → characterize on the Phase 1 test rig.
> **Theory:** reflected inertia J_ref = J_motor × N² + J_gearbox; backdrivability as the QDD's defining property; encoder offset calibration (1.3); bearing preload.
> **Fabrication:** assembly only. Hand tools + press fits. 48 V bus — follow SAFETY_CARD.

## Deliverable

Assemble the QDD from 3.1 + 3.2 components and characterize it on the Phase 1 motor test rig (upgraded with a proper lever arm and your calibrated load cell). This milestone turns parts into a qualified component with a documented torque constant, efficiency, and backdrivability — the same rigor you'll demand of the arm in Phase 4.

**Assembly sequence:**
1. Press bearings into housing (correct fit from 3.1; slow, square pressure).
2. Output shaft through bearings; axial location by shoulder + retaining ring.
3. Gearbox to motor; couple to output shaft (alignment matters).
4. Puck mounted on motor rear; AS5048 magnet on output shaft at datasheet gap.
5. Wire, close housing, torque fasteners to spec.
6. Verify by hand: smooth rotation, zero axial play, backdrivable.

**Characterization tests (all logged with `templates/characterization.md`):**
- Kt: command Iq steps, measure output torque, slope × ratio check
- Ke: hand-spin output, measure phase voltage vs speed
- Torque-speed curve: 5+ points
- Backdrivability: hand torque to move output with motor unpowered (< 0.5 N·m target)
- Thermal: 10 min continuous rated torque, temperature logged
- Current-loop bandwidth: step response

## Pass Condition

### MVM
- [ ] Actuator assembled; shaft smooth by hand; no binding or axial play
- [ ] FOC runs on the Puck; motor spins
- [ ] Output encoder tracks shaft position
- [ ] Holds torque against a gentle push

### Full Pass
- [ ] Kt measured with uncertainty; compared to motor Kt × ratio; discrepancy explained
- [ ] Torque-speed curve plotted; continuous operating region identified
- [ ] Backdrivability measured and documented — the QDD's signature property
- [ ] Thermal test passed; temperature documented
- [ ] Current-loop bandwidth measured, compared to SIL prediction
- [ ] Encoder offset calibration documented
- [ ] **Physical:** labeled, photographed next to CAD rendering; all data in `data/processed/`

> [!warning] ⚠️ Landmines
> 1. **Bearing preload/axial location is the assembly.** `[HYPOTHESIS]`
>    Un-located bearings → axial play → encoder wobble → noisy FOC that looks like a firmware bug. Circlips/shoulders/shims on both bearings.
> 2. **Coupling misalignment eats bearings.** `[COMMUNITY]`
>    Motor shaft and gearbox input must be coaxial (< 0.05 mm) or use a flexible coupling. Radial load on motor bearings = early death and noise.
> 3. **First power-on inside a closed housing is the scariest moment of the phase.** `[HYPOTHESIS]`
>    Current limit ON. 10% duty first. Listen and feel for rubbing/oscillation. Power off instantly at anything odd. You tested the Puck on the bench in 3.2 precisely so this moment has no firmware surprises.
> 4. **Backdrivability failing means the design point failed, not the assembly.** `[HYPOTHESIS]`
>    If the output won't turn easily unpowered: ratio too high, bearings overtight, or motor cogging dominates. Diagnose with the gearbox disconnected to isolate.
> 5. **Encoder alignment before closing the housing.** `[HYPOTHESIS]`
>    Energize a phase pair, let the rotor settle, read the encoder — that's the offset. Do it while you can still reach things.
> 6. **48 V habits start here.** `[HYPOTHESIS]`
>    Fuse before power. Discharge bus caps before touching. One hand near the switch. This is rehearsal for Phase 4.
>

## Dependencies that waste your week if hit backwards

- 3.1 housing + 3.2 Puck verified separately BEFORE assembly.
- Puck + motor bench-tested BEFORE the housing closes.
- Encoder offset calibrated BEFORE final assembly.
- Characterize on the rig BEFORE the actuator ever goes near the arm (Phase 4).

> Log sessions in Daily/ notes using the unified template.

---

## Phase Exit Gate: Hardware-in-the-Loop Validation

After the PCB is fabricated, assembled, and powered up, and after the mechanical arm is
assembled, you validate the INTEGRATED system using HIL testing. This is the right side of
the V: you verify that the physical hardware behaves correctly against the model that
informed its design.

### Deliverable

Connect the custom PCB (running Phase 2 FOC firmware) to the physical arm. Run the same
trajectory commands that were validated in the SIL gate. Compare hardware behavior to
simulation predictions. Then inject faults and verify safe responses.

### Pass Condition

- [ ] The arm tracks the same multi-waypoint trajectory used in SIL. Tracking error
compared to SIL prediction. Discrepancy documented and explained (friction, backlash,
unmodeled dynamics, sensor noise).
- [ ] FOC current loop bandwidth measured on hardware. Compared to simulation prediction.
If hardware bandwidth < simulation bandwidth, identify why (analog front-end
limitations, ADC latency, PWM timing).
- [ ] **Fault injection (minimum 3 types):**
- Encoder dropout: disconnect encoder mid-motion. Firmware detects loss and enters
safe state (de-energize or controlled stop).
- Overcurrent: command a current exceeding the limit. Firmware detects and shuts
down the drive.
- Undervoltage: sag the bus voltage below threshold. Firmware detects and enters
safe state.
- [ ] Each fault injection uses `templates/fault_injection_test.md`.
- [ ] Fault log recorded: what was injected, what the firmware did, what it should have
done, pass/fail.
- [ ] Recovery procedure documented for each fault type.

### Landmines

1. **HIL must not damage real hardware.** `[HYPOTHESIS]`
Simulate sensor failures by disconnecting signals, not by creating real overcurrent on
the bus. Test the FIRMWARE's response, not hardware survival. Use current-limited
supply during fault injection.
2. **If HIL results diverge significantly from SIL, the model is wrong.** `[HYPOTHESIS]`
Small differences are expected (friction, backlash, sensor noise). Large differences
(> 2× tracking error) mean the plant model used in SIL doesn't match reality. Update
the model, don't just tune the gains.
3. **Don't skip the fault injection because "it works."** `[HYPOTHESIS]`
The system working under nominal conditions tells you nothing about what happens when
something goes wrong. In aerospace and motorsport, the fault response is the design.
The nominal behavior is the easy part.

---

# Phase 3 Deload / Synthesis

- [ ] Re-draw the ground return path diagram from memory
- [ ] Explain star grounding vs. ground pour, when each is appropriate
- [ ] Explain why ground plane splits are wrong and what to do instead
- [ ] Explain switching node EMC: why it radiates, how to contain it
- [ ] Re-derive bending stress and FoS for the critical feature
- [ ] Explain what FEA boundary conditions you used and why
- [ ] Explain bearing fit selections from memory: which ring gets interference, which gets clearance, why
- [ ] Explain fastener preload: why it matters, how torque relates, what happens if the joint is loose
- [ ] Explain the motor + gearbox sizing: inertia ratio, reflected load, torque-speed margin
- [ ] Explain the power stage: why buck vs LDO, bootstrap cap sizing, inrush, sequencing
- [ ] Explain the system power budget: every rail, every load, every mode, worst case
- [ ] State the QDD's measured Kt, backdrivability, and thermal limit from memory
- [ ] Explain the SIL→HIL flow: what was verified in simulation, what was verified on hardware, where they diverged and why
- [ ] Review and update the Mini-FMEA with actual failure modes encountered during fabrication and bring-up
- [ ] Run `scripts/versions.sh` and `scripts/cold_tools.sh`

## Phase 3 Retro

Actual time vs. range, 12–22 wk:
Most valuable landmine:
Missing landmine:
SIL prediction vs. HIL reality — biggest surprise:
What Phase 4 needs from Phase 3:
