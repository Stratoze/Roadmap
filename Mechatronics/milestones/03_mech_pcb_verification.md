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
- [ ] 2-DOF arm CAD assembly, interference-free
- [ ] Hand calcs: FoS > 2 on critical links
- [ ] FEA runs, roughly matches hand calcs
- [ ] Bearing selected for each joint: type, size, fit, life calc documented
- [ ] Motor + transmission sized for each axis: torque-speed, inertia ratio, acceleration
- [ ] Belt and lead screw pairing documented: backlash, stiffness, reflected inertia,
      efficiency, backdrivability, and safety braking if needed
- [ ] System power budget documented: every rail, every load, every mode
- [ ] PCB schematic passes ERC, layout passes DRC
- [ ] Power stage designed: regulator topology chosen, bootstrap sized, inrush handled
- [ ] EMC design rules applied: ground plane, switching node, trace routing
- [ ] Board powers up through current-limited supply
- [ ] HIL exit gate passed (see Phase Exit Gate below)

### Full Pass

- [ ] GD&T drawings with tolerance stack-up, release-ready
- [ ] FEA validated against hand calcs within 20%
- [ ] Shaft design: diameter, keyway or clamping, retaining method, critical speed checked
- [ ] Fastener selection: bolt grade, preload, torque spec, joint stiffness considered
- [ ] Fits documented: bearing-to-shaft, bearing-to-housing, with tolerance classes
- [ ] DFM review completed against Phase 0 rules before sending to fab
- [ ] Star grounding verified
- [ ] Trace widths sized for stall current
- [ ] Power stage: buck converter or LDO designed with component values, not copied blindly
- [ ] EMC: can explain why the layout passes or fails, not just "it looks right"
- [ ] Connectors/harness: pinouts, labels, strain relief, shielding/grounding, and
      service access considered
- [ ] Board runs FOC firmware, ported from eval board
- [ ] HIL: 3+ fault types injected, firmware enters safe state for each
- [ ] Mini-FMEA completed for both mechanical and electrical subsystems
      using `templates/fmea.md`

---

## Pre-Design Requirements

Fill `templates/requirements_brief.md` before opening CAD or KiCad.

### Motor + Transmission Sizing (required before CAD)

For each axis, document:

- [ ] **Load torque:** gravity (worst-case pose), friction (bearing + seal), payload.
      Sum = continuous torque requirement.
- [ ] **Acceleration torque:** τ_acc = J_total × α. J_total = J_motor + J_load_reflected.
      For a gear/belt/lead screw with ratio N: J_load_reflected = J_load / N².
      This is why high reduction ratios make the load "look lighter" to the motor.
- [ ] **Torque-speed check:** plot the motor's torque-speed curve. Mark the operating
      point (continuous torque at max speed). Verify it's inside the curve, with margin.
      If not: bigger motor, higher supply voltage, or higher reduction ratio.
- [ ] **Inertia ratio:** J_load_reflected / J_motor. Target < 10:1 for responsive control.
      > 10:1 → the load dominates, the controller fights the mechanics, tuning is painful.
      If ratio is too high: increase reduction ratio (reduces reflected inertia by N²).
- [ ] **Transmission selection:**
      - Timing belt (GT2): low backlash (~0.1–0.3mm), moderate precision, good for long
        travel, low cost. Ratio = driven_teeth / driver_teeth.
      - Lead screw (T8, TR8): high force, self-locking (Acme), lower speed, backlash in
        nut. For Z-axes and linear stages.
      - Ball screw: high efficiency (~90%), backdrivable, precise, expensive. For CNC and
        high-performance axes.
      - Direct drive: no transmission. Zero backlash. Requires high-torque motor. For
        joints where precision matters more than speed.
- [ ] **Belt drive details:** tooth engagement, belt tension, pulley inertia, bearing load
      from tension, and expected backlash/compliance documented.
- [ ] **Lead screw details:** efficiency, self-locking/backdrivability, critical speed,
      column buckling, nut backlash, and anti-backlash or brake requirement documented.
- [ ] **Motor + transmission pairing documented:** "Axis 1: NEMA17 + GT2 20T→60T (3:1),
      reflected inertia = X, acceleration torque = Y, continuous torque = Z. Operating
      point is inside the torque-speed curve with 30% margin."

### System Power Budget (required before schematic)

Before opening KiCad, document:

- [ ] **Every rail:** list all voltage rails needed (e.g., 3.3V logic, 5V sensors,
      12V gate drive, 24–48V motor bus).
- [ ] **Every load on each rail:** MCU (active/sleep), sensors, gate drivers, fans, LEDs,
      encoder, communication transceivers. Current per load per mode.
- [ ] **Every operating mode:** idle (MCU running, motors off), active (motors running
      nominal), peak (motors stalled, all peripherals on). Sum per rail per mode.
- [ ] **Regulator sizing:** for each rail, choose topology (LDO vs. buck) and size with
      30% margin above peak load. Document why: "3.3V rail: peak load 450 mA, LDO at 5V
      input dissipates 0.77W — acceptable. Buck not needed." Or: "12V→3.3V at 1A: LDO
      dissipates 8.7W — buck converter required."
- [ ] **Fuse / protection sizing:** input fuse rated for peak current + inrush. Document:
      "Input fuse: 5A slow-blow. Peak motor current 4A × 2 axes = 8A. Inrush 12A for 10ms.
      Slow-blow survives inrush, clears sustained overcurrent."
- [ ] **Battery / supply sizing:** if battery-powered: capacity (Ah) × voltage = energy
      (Wh). Divide by average power = runtime. If bench-powered: supply must deliver peak
      current without current-limiting.

This is not optional. If you skip the power budget, you'll discover at power-on that the
3.3V rail sags under load, or the fuse blows on startup, or the regulator overheats.
The budget takes 1 hour. Redesigning the power stage after layout takes 2 weeks.

### Mini-FMEA (required before design, updated after)

Complete `templates/fmea.md` for both the mechanical assembly and the electrical system
BEFORE opening CAD or KiCad. Update it after fabrication and bring-up with what you
actually encountered.

This is not a homework exercise. The FMEA forces you to ask "what can go wrong?" BEFORE
you build. Every high-risk item (Severity × Occurrence ≥ 12) must have a documented
mitigation before design proceeds.

---

# Milestone 3.1 — CAD + Machine Elements + FEA + Drawings

> [!info] 📚 Resources — CAD, Machine Elements, FEA & Drawings
> **Visual:** Solid Edge CE tutorials; Jakub Michalski (YouTube) for PrePoMax FEA.
> **Interactive:** model → export STEP → PrePoMax/CalculiX static stress → validate vs hand calc. FreeCAD as macOS STEP viewer.
> **Theory:** SKF/NSK bearing-fit tables; fastener preload; GD&T; Shigley for elements.


## Deliverable

Complete 2-DOF arm in Solid Edge Community Edition (free, no student ID): parametric
parts, selected bearings with fits, sized shafts, specified fasteners, motor mounts,
verified by hand calcs and FEA in PrePoMax (free, open-source, CalculiX solver), with
manufacturing drawings and a DFM review.

**Tool pipeline:** Solid Edge CE (Windows) → export `.STEP` → PrePoMax (Windows,
portable, no install) → static stress / modal / buckling. On macOS: FreeCAD opens STEP
natively for quick viewing, measurement, and light edits without booting Windows.

This is not just "draw the arm." This is "design the joints so they actually rotate
smoothly under load, survive fatigue, and can be manufactured."

## Dependency on SIL Gate

The motor and transmission selections from the Pre-Design Requirements are INFORMED by
the SIL simulation results. If the SIL gate revealed that the controller struggles with
the coupled dynamics at certain configurations, the mechanical design must account for
this: stiffer links, better bearings, or different transmission ratios. The SIL results
are an INPUT to the mechanical design, not an afterthought.

## Pass Condition

### MVM

- [ ] Assembly modeled, interference-free
- [ ] At least one Poka-yoke feature
- [ ] Hand calc: worst-case bending stress, FoS documented
- [ ] FEA: static stress run, max stress location identified
- [ ] Bearing selected for each joint: type (deep groove ball, angular contact, etc.),
      size from load rating, documented

### Full Pass

- [ ] All parts fully parametric
- [ ] Real bearings and motor mounts from datasheets
- [ ] **Bearing fits:** shaft tolerance (e.g., k6 for inner ring rotating load), housing
      tolerance (e.g., H7 for outer ring stationary). Can explain WHY: interference fit on
      the rotating ring prevents creep; clearance fit on the stationary ring allows thermal
      expansion.
- [ ] **Bearing life:** L10 life calculated for expected load and speed. Can explain:
      L10 = (C/P)^p × 10⁶ revolutions. C = dynamic load rating, P = equivalent load,
      p = 3 for ball bearings.
- [ ] **Shaft design:** diameter from torsional and bending stress. Keyway or clamp-style
      coupling. Retaining rings or shoulders for axial location. Critical speed estimated
      (even roughly): if the arm never spins fast, document why it's not a concern.
- [ ] **Fastener design:** bolt grade (8.8, 10.9, 12.9), preload target, torque spec.
      Can explain: preload creates clamping force. The joint stiffness determines how much
      additional load the bolt sees. Loose joint → bolt sees full cyclic load → fatigue.
      Tight joint → bolt sees a fraction.
- [ ] **Springs / counterbalance:** if the arm is gravity-loaded, document the holding
      torque. Is a counterbalance spring needed? If yes: spring rate, preload, geometry.
      If no: document why the motors can hold static load continuously without overheating.
- [ ] Hand calcs: bending, shear, torsion on critical link
- [ ] FEA validated vs. hand calcs, within 20%, explain discrepancy
- [ ] Mesh convergence checked: run 3 mesh densities in PrePoMax, plot max stress vs.
      element count, confirm < 5% change between finest two
- [ ] PrePoMax workflow documented: STEP import → material assignment → mesh (tetra
      dominant) → boundary conditions → solve → probe max stress → compare to hand calc.
      Screenshots in `docs/captures/`
- [ ] FreeCAD verified as macOS STEP viewer: opened the arm assembly, measured a critical
      dimension, confirmed it matches Solid Edge
- [ ] GD&T drawings: flatness, concentricity, pin fits
- [ ] Tolerance stack-up: worst-case AND RSS
- [ ] **DFM review:** check every part against the 5 rules from Milestone 0.8. Document:
      can this be made on a 3-axis mill? Are there internal sharp corners? Are tolerances
      tighter than necessary? Is the material appropriate for the process?
- [ ] Transmission integration checked: belt tensioner/idler, lead screw support/coupling,
      anti-backlash, bearing retention, and motor/shaft alignment documented
- [ ] Robust design reviewed: performance sensitivity to tolerance stack, wear, assembly
      variation, and thermal expansion; critical tolerances justified, non-critical
      tolerances loosened.
- [ ] Drawings sent for fabrication

> [!warning] ⚠️ Landmines
> 1. **CAD without constraints is sculpture.** `[HYPOTHESIS]`
>    Fully constrained sketches. Proper mates. Change one dimension → assembly updates,
>    doesn't explode.
> 2. **FEA without hand calcs is a pretty picture.** `[COMMUNITY]`
>    Estimate max stress by hand, σ = Mc/I, τ = Tr/J, BEFORE running FEA. FEA always gives
>    a number. The question is whether it's right.
> 3. **Boundary conditions are where FEA goes wrong.** `[COMMUNITY]`
>    Max stress at a constraint point → BCs are wrong. Point loads → infinite stress. Fix
>    the model, not the mesh.
> 4. **Tolerance stack-up kills assemblies.** `[HYPOTHESIS]`
>    ±0.1mm per joint × 5 joints = ±0.5mm at tip. Calculate BEFORE ordering.
> 5. **3D printing ≠ CNC design rules.** `[HYPOTHESIS]`
>    Layer adhesion direction matters. Orient prints so layers are perpendicular to primary
>    load.
> 6. **Bearing fit is not "snug."** `[COMMUNITY]`
>    A bearing on a shaft with too-loose a fit will spin on the shaft (fretting corrosion,
>    destroys both surfaces). Too tight and you can't assemble it, or you preload the bearing
>    radially and reduce its life. The fit is specified by ISO tolerance classes for a reason.
>    Look up the bearing manufacturer's recommendation (SKF, NSK, Timken all publish fit
>    tables).
> 7. **Bearing life is load-dependent, not time-dependent.** `[COMMUNITY]`
>    L10 life scales with (C/P)³. Double the load → ⅛ the life. If your arm is heavier than
>    expected, or the payload is higher, bearing life drops dramatically. Calculate with
>    worst-case load, not nominal.
> 8. **Fastener preload is the design variable, not torque.** `[COMMUNITY]`
>    Torque is how you ACHIEVE preload. But friction (thread + under-head) consumes 85–90%
>    of applied torque. The same torque on a lubricated vs. dry bolt gives wildly different
>    preload. For critical joints: specify preload, use torque + friction coefficient, or use
>    a torque-angle method.
> 9. **A bearing without a retention method will walk.** `[HYPOTHESIS]`
>    Axial loads, vibration, and thermal cycling cause bearings to migrate. Shoulders,
>    retaining rings, end caps, or threaded locknuts. Every bearing needs an axial location
>    method on both inner and outer rings.
> 10. **DFM review is not optional polish.** `[HYPOTHESIS]`
>     The 5 rules from Milestone 0.8 exist for this moment. Check them. If a part has an
>     internal sharp corner, the machine shop will email you. If a tolerance is ±0.01mm where
>     ±0.1mm works, you're paying 5× for no reason. 30 minutes of DFM review saves weeks of
>     fab back-and-forth.
> 11. **Solid Edge Community Edition exports STEP freely, but cannot open other people's
>     native `.par`/`.asm` files.** `[COMMUNITY]`
>     This means: your workflow is always Solid Edge → STEP → everything else. If a supplier
>     sends you a native Solid Edge file, you can't open it on CE. Ask for STEP or IGES.
>     This is the only real limitation. Plan your file exchanges accordingly.
> 12. **PrePoMax is Windows-only and portable (no installer), but it is not a toy.**
>     `[COMMUNITY]`
>     It wraps CalculiX, the same solver used in academic and industrial FEA. The GUI is
>     clean and modern. But: it has no native macOS build. Run it via Parallels, Boot Camp,
>     or a Windows VM on your Mac. The portable `.zip` means you can run it from a USB stick.
>     Latest version: v2.5.2. Forum: prepomax.discourse.group. Jakub Michalski's YouTube
>     series (50+ tutorials) is the best learning resource.
> 13. **PrePoMax boundary conditions are where your FEA goes wrong, not the mesh.**
>     `[HYPOTHESIS]`
>     Same principle as landmine 3, but specific to the tool: PrePoMax lets you apply point
>     loads and fixed constraints easily. A point load on a sharp corner gives infinite
>     stress. A fixed constraint on a single face over-constrains the model. Distribute loads
>     over areas. Constrain only what's physically restrained. The pretty colour contour is
>     meaningless if the BCs are wrong.
> 14. **FreeCAD on macOS is a STEP viewer, not your primary CAD tool.** `[HYPOTHESIS]`
>     FreeCAD's FEM workbench also wraps CalculiX and can import STEP files. But its GUI is
>     less polished than PrePoMax's, and the learning curve is steeper. Use FreeCAD for:
>     opening STEP files on macOS, quick measurements, light geometry edits. Use PrePoMax
>     for: actual FEA. Use Solid Edge for: actual design. Don't try to do everything in one
>     tool.
> 15. **Skipping the SIL gate makes mechanical design blind.** `[HYPOTHESIS]`
>     If you design the arm without knowing whether the controller can handle the coupled
>     dynamics, you may over-design (heavy, expensive) or under-design (flexible, unstable).
>     The SIL results tell you where the mechanical margins actually need to be.
>

## Dependencies that waste your week if hit backwards

- **Complete the SIL gate BEFORE opening CAD.** The simulation results inform motor
  selection, transmission ratios, and structural stiffness requirements.
- Define constraints on paper, work envelope, payload, motor selections, material,
  manufacturing method, BEFORE opening CAD.
- **Complete the motor + transmission sizing (Pre-Design section above) BEFORE opening
  CAD.** The motor dimensions, shaft size, and transmission geometry constrain the entire
  joint design. If you design the housing first and then discover the motor doesn't fit,
  you redesign everything.
- Hand calcs BEFORE FEA. You need the hand calc to validate the FEA.
- Verify motor mounting dimensions against the actual motor datasheet BEFORE finalizing
  the joint housing.
- Select bearings BEFORE designing the housing bore and shaft diameter. The bearing is a
  purchased component with fixed dimensions. The shaft and housing are designed AROUND the
  bearing, not the other way around.
- Do the DFM review BEFORE sending drawings to fab. Not after. Not "I'll fix it when they
  ask questions."
- **Complete the Mini-FMEA BEFORE design.** The FMEA may reveal that a design choice you
  were about to make has a high-risk failure mode. Catch it before CAD, not after fab.
- **Install and verify the Solid Edge → STEP → PrePoMax pipeline BEFORE starting the arm
  design.** Model a simple L-bracket in Solid Edge, export STEP, open in PrePoMax, run a
  static analysis, compare to hand calc. If the pipeline doesn't work, you discover it on
  a 30-minute bracket, not on the 5-week arm assembly.
- **Verify FreeCAD opens your STEP files on macOS BEFORE you need it in a hurry.** Export
  a test part from Solid Edge, open in FreeCAD, measure a dimension. If it works, you have
  a macOS fallback. If it doesn't, you know now.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 3.2 — First Custom PCB + Power Stage + EMC

> [!info] 📚 Resources — PCB, Power Stage & EMC
> **Visual:** Phil's Lab (mixed-signal / motor-driver PCB) — best practical walkthrough.
> **Interactive:** KiCad 9 — schematic → footprint check → layout → DRC; built-in PCB Calculator for trace width.
> **Theory:** TI SLVA404 (buck layout); IPC-2221; ground-plane & switching-node EMC rules.


## Deliverable

Custom STM32 motor driver shield: designed in KiCad, power stage designed (not copied),
EMC design rules applied, manufactured, assembled, powered up with verified rails.

## Dependency on SIL Gate

The FOC firmware that will run on this board has already been validated in simulation
during the SIL gate. The PCB design is informed by the SIL results: if the simulation
revealed that the current loop needs > 100 kHz bandwidth, the analog front-end component
selection must support it. If the simulation showed that the anti-aliasing filter adds
critical phase lag, the filter component values are constrained by the simulation, not
chosen by guesswork.

## BOM Sanity

Before finalizing schematic:

- [ ] Every IC has manufacturer part number.
- [ ] Every IC has orderable distributor SKU.
- [ ] Every critical part has at least one substitute.
- [ ] Package matches footprint.
- [ ] Voltage/current/thermal ratings checked.
- [ ] Stock exists today or lead time is acceptable.

## Power Stage Design (required before layout)

- [ ] **Logic rail:** 3.3V for MCU, sensors, logic. If total logic current < 300mA and
      input is 5V: LDO is fine (simple, low noise). If > 300mA or input is 12–48V: buck
      converter (efficient, but noisier). Document the decision and why.
- [ ] **Gate driver supply:** typically 10–15V for MOSFET gate drive. If the main supply
      is 12V, a simple LDO or resistor-zener may suffice. If 24–48V, a buck converter or
      isolated supply is needed.
- [ ] **Bootstrap capacitor:** for high-side gate drive in half-bridge configurations.
      C_boot ≥ Q_g × V_gs / ΔV. Q_g = total gate charge from MOSFET datasheet. ΔV =
      allowable droop (typically 0.5–1V). If C_boot is too small, the high-side gate
      voltage sags during long on-times → MOSFET enters linear region → overheats → dies.
- [ ] **Inrush current:** large capacitors on the power rail look like a short at power-on.
      Add an NTC thermistor, a series resistor + relay bypass, or a soft-start circuit.
      Without it: the supply current-limits, the voltage sags, the MCU brown-outs, and you
      spend a day debugging "random" resets.
- [ ] **Reverse polarity protection:** series diode (simple, 0.3–0.7V drop), P-MOSFET
      (low drop, more complex), or ideal diode controller. If someone plugs the supply in
      backwards, the board should not smoke.
- [ ] **Test points:** critical rails, current-sense outputs, PWM/gate signals, and
      communication lines have probe points or headers for bring-up and debug.
- [ ] **Power sequencing:** logic rail must be stable before the MCU starts. Gate driver
      supply must be stable before PWM outputs enable. If the MCU starts before the gate
      driver is ready, the PWM pins may float → MOSFETs partially on → shoot-through.
      Use enable pins, power-good signals, or RC delays.
- [ ] **Can explain:** why a buck converter instead of an LDO at high current
      (P_loss = (V_in - V_out) × I. At 12V→3.3V, 1A: LDO dissipates 8.7W. Buck dissipates
      ~0.5W). Why bootstrap needs refresh (the cap charges when the low-side FET is on;
      if the high-side stays on too long, the cap drains). Why inrush matters (capacitor
      impedance at t=0 is ~0).

## EMC Design (required before and during layout)

This is not a polish step. This is not "add shielding at the end." EMC is a layout
discipline. Get it wrong and the board radiates, the encoder glitches, the ADC reads
noise, and you can't tell if the problem is firmware or hardware.

- [ ] **Ground plane strategy:** solid, unbroken ground plane on at least one inner layer
      (4-layer board) or the bottom layer (2-layer board). No splits. No moats. No "analog
      ground" and "digital ground" separated by a gap. One plane. Separate analog and
      digital circuits by PLACEMENT (analog near the connector, digital near the MCU), not
      by plane splits. Can explain: a split plane forces return currents to detour around
      the split. Loop area increases. Radiation increases. The detour path also has higher
      inductance → more noise coupling.
- [ ] **Switching node management:** the LX/SW node on a buck converter or gate driver
      switches between 0V and VIN at MHz frequencies with nanosecond edges. This is a
      broadband RF source. Keep the switching node trace SHORT (< 5mm), NARROW, and on an
      inner layer if possible. Do NOT route sensitive signals (encoder, ADC, SPI) near it.
      Do NOT place the inductor directly over a ground plane gap. Can explain: the
      switching node has high dV/dt (volts per nanosecond). Any copper near it couples
      capacitively. The inductor has high dI/dt and radiates magnetically. Both are noise
      sources.
- [ ] **Input capacitor placement:** the input capacitor to a buck converter must be < 5mm
      from the VIN and GND pins. The loop formed by (VIN pin → cap → GND pin → back to
      VIN) carries the full switching current at MHz frequencies. If this loop is large,
      it radiates. Place the cap first. Route everything else around it.
- [ ] **Signal routing:** encoder signals, SPI, I2C, UART — route away from motor traces
      and switching nodes. If they must cross, cross at 90° (minimizes parallel run
      length). Motor power traces: wide, short, on outer layers if possible, with ground
      plane underneath for shielding. Can explain: parallel runs create capacitive and
      inductive coupling. 90° crossings minimize the coupling area.
- [ ] **Cables and connectors:** motor cables shielded/twisted, signal cables separated,
      shield grounding strategy defined, and connector strain relief considered.
- [ ] **Decoupling:** 100 nF ceramic on every MCU power pin, < 3mm from the pin. 10 µF
      bulk per rail, near the regulator output. Can explain: the 100 nF handles
      high-frequency transients (ns timescale). The 10 µF handles medium-frequency (µs).
      The regulator handles low-frequency (ms). Each has a different impedance-vs-frequency
      curve. You need all three.
- [ ] **Can explain why PWM creates EMI:** the motor phase voltage switches between 0V and
      Vbus at 10–20 kHz with ~50 ns edges. The Fourier transform of a 50 ns edge has
      significant energy up to ~1/(π × 50ns) ≈ 6 MHz. The motor cables act as antennas.
      The switching loop (FET → motor → shunt → back) has high dI/dt. Both radiate. The
      fix: slow the edges (gate resistor), shorten the loops, shield the cables, filter
      the outputs.

## KiCad Learning Resources (verified)

| Resource | Link | Use when |
| :--- | :--- | :--- |
| KiCad 9 Official Docs | <https://docs.kicad.org/> | Reference. Always. |
| KiCad Forum | <https://forum.kicad.info/> | Stuck on a specific footprint or DRC error |
| Phil's Lab (YouTube) | Search "Phil's Lab KiCad" | Best mixed-signal PCB design walkthroughs. Watch his STM32 + motor driver series before starting your schematic |
| Shane Colton (YouTube) | Search "Shane Colton KiCad" | Good beginner-to-intermediate KiCad 8/9 tutorials |
| DigiKey KiCad Tutorial Series | <https://www.digikey.com/en/maker/kicad> | Step-by-step from blank project to fab output |
| KiCad PCB Calculator (built-in) | Tools → PCB Calculator in KiCad | Trace width, via current, thermal. Use IPC-2221 tables. Don't guess trace widths |

## Pass Condition

### MVM

- [ ] Board powers up, no shorts
- [ ] All rails within ±10%
- [ ] Motor driver switches a load on command

### Full Pass

- [ ] ERC + DRC clean
- [ ] Gerbers accepted by fab
- [ ] Rails within ±5%
- [ ] No solder bridges under microscope
- [ ] FOC firmware ported and running
- [ ] Star grounding verified
- [ ] **Power stage verified:** buck converter efficiency measured (> 85% expected). LDO
      dropout verified. Bootstrap capacitor voltage measured under load (should not droop
      > ΔV). Inrush current measured on scope (should be limited). Reverse polarity tested
      (board survives).
- [ ] **EMC verified:** encoder reading stable while motor runs at 50% duty. ADC current
      reading noise < 5% of full scale with motor switching. If encoder glitches or ADC
      noise is excessive: identify the coupling path (conducted? radiated? ground bounce?)
      and fix the layout, not the firmware.
- [ ] Power-stage reliability checked: MOSFET SOA, component derating, transient thermal
      impedance, regulator stability/compensation, and connector/wire lifecycle considered.

> [!warning] ⚠️ Landmines
> 1. **Footprint mismatch kills the board.** `[COMMUNITY]`
>    For every non-trivial IC: open datasheet → "Recommended PCB Land Pattern."
>    Cross-reference pad count, pin 1, courtyard. SOT-23-5 vs SOT-23-6, SOIC-8 vs
>    SOIC-8-EP, flipped pin 1. 5 min per IC. Missing it costs a 3-week fab cycle.
>    **#1 because it ends the milestone.**
> 2. **Draw ground return paths as arrows BEFORE layout.** `[COMMUNITY]`
>    Motor return, ADC return, MCU return. If two arrows share a trace segment before the
>    star point, that's noise injection.
> 3. **Trace width for stall current, not nominal.** `[COMMUNITY — IPC-2221]`
>    Stall is 3–5× running. Size for stall.
> 4. **Decoupling: < 3 mm means < 3 mm.** `[COMMUNITY]`
>    100 nF ceramic 2 cm away is decoration. Place decoupling first, then route.
> 5. **Fab wait IS the deload.** `[HYPOTHESIS]`
>    1–3 weeks. Don't start new theory. Documentation, cold-toolchain touches, synthesis.
> 6. **Stencil for QFP/LQFP.** `[HYPOTHESIS]`
>    Hand-soldering 48-pin LQFP is painful. Order the stencil. Paste + hotplate or reflow.
>    If hand-soldering: flux is not optional.
> 7. **Bootstrap capacitor is not "just a cap."** `[COMMUNITY]`
>    Too small → high-side gate sags → MOSFET linear region → thermal destruction. Too
>    large → slow charge → startup delay. The value comes from Q_g and allowable droop.
>    Calculate it. Don't copy 1µF from a reference design without checking.
> 8. **Buck converter layout is not forgiving.** `[COMMUNITY]`
>    The input capacitor must be < 5mm from the VIN and GND pins. The switch node (LX)
>    trace must be short and narrow (it's a high dV/dt antenna). The feedback resistor
>    divider must route away from the inductor and switch node. Get the layout wrong →
>    oscillation, EMI, or regulator instability. Follow the datasheet layout example exactly.
> 9. **Power sequencing is not "it'll probably be fine."** `[HYPOTHESIS]`
>    If the MCU starts before the gate driver supply is stable, the PWM outputs may be in an
>    undefined state. On some MCUs, GPIO pins float at reset. Floating PWM → MOSFETs
>    partially on → shoot-through → dead board. Use the gate driver's enable pin, held low
>    until the logic rail is good.
> 10. **Ground plane splits are the #1 EMC mistake.** `[COMMUNITY]`
>     If you split the ground plane (analog ground / digital ground / power ground) and
>     route a signal across the split, the return current has to detour around the split.
>     Loop area increases. EMI increases. The fix: one solid ground plane. Separate analog
>     and digital by PLACEMENT, not by plane splits. Star grounding is for the power
>     distribution topology, not for splitting the ground plane.
> 11. **The switching node is an antenna.** `[COMMUNITY]`
>     The LX pin on a buck converter switches between 0V and VIN at MHz frequencies with
>     nanosecond edges. This is a broadband RF source. Keep the LX trace short (< 5mm),
>     narrow, and away from sensitive signals. A copper pour under it (on the same layer,
>     connected to ground) acts as a shield. Do NOT clear the ground plane under the
>     switching node — the ground plane IS the shield.
> 12. **Power budget is not "add up the currents."** `[HYPOTHESIS]`
>     Include inrush (capacitors charging), startup (all rails ramping simultaneously), and
>     worst-case operating (all motors stalled, all LEDs on, MCU at max clock). The fuse and
>     supply must survive the worst case, not the nominal case. If you budget for nominal and
>     test at peak, the fuse blows and you think the board is broken.
>

## Dependencies that waste your week if hit backwards

- **Complete the SIL gate BEFORE schematic.** The simulation constrains component choices:
  amplifier bandwidth, filter cutoff, ADC sample rate. Design the schematic informed by
  simulation, not by reference designs.
- Verify ALL IC footprints against datasheet land patterns BEFORE opening KiCad. This is
  Step 0, not Step 2.
- Draw the ground return path diagram BEFORE layout. Star ground is a routing constraint,
  not an afterthought.
- Know your current-sensing topology, from FOC milestone, BEFORE choosing the ADC/sense
  resistor topology on the schematic.
- **Design the power stage on paper BEFORE opening KiCad.** Regulator topology, component
  values, bootstrap cap, inrush method. The schematic is just drawing what you already
  decided. If you design the power stage inside KiCad, you'll route it wrong and redo the
  layout.
- **Complete the system power budget BEFORE choosing regulators.** You can't choose a
  regulator without knowing the load. You can't size a fuse without knowing the peak. The
  budget is the input to the schematic, not an afterthought.
- **Apply EMC rules DURING layout, not after.** You can't "add EMC" to a finished layout.
  The ground plane, component placement, and trace routing ARE the EMC design. If you route
  first and "check EMC" later, you'll redo the layout.
- Order the stencil at the same time as the PCB. Don't wait.

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
- [ ] Re-derive bending stress and FoS for the critical link
- [ ] Explain what FEA boundary conditions you used and why
- [ ] Explain bearing fit selections from memory: which ring gets interference, which gets
      clearance, why
- [ ] Explain fastener preload: why it matters, how torque relates, what happens if the
      joint is loose
- [ ] Explain the motor + transmission sizing: inertia ratio, reflected load, torque-speed
      margin
- [ ] Explain the power stage: why buck vs LDO, bootstrap cap sizing, inrush, sequencing
- [ ] Explain the system power budget: every rail, every load, every mode, worst case
- [ ] Explain the SIL→HIL flow: what was verified in simulation, what was verified on
      hardware, where they diverged and why
- [ ] Review and update the Mini-FMEA with actual failure modes encountered during
      fabrication and bring-up
- [ ] Run `scripts/versions.sh` and `scripts/cold_tools.sh`

## Phase 3 Retro

Actual time vs. range, 10–19 wk:
Most valuable landmine:
Missing landmine:
SIL prediction vs. HIL reality — biggest surprise:
What Phase 4 needs from Phase 3:
