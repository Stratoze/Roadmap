# Roadmap

Checklist / book index. Update only when a milestone changes state.
Do not maintain this weekly.

**Legend:**
⬜ not started · 🔨 active · ✅ complete

## Completion & Evidence — how a milestone becomes "done"

1. Meet every **MVM** checkbox for the milestone.
2. Commit the evidence: `./scripts/save.sh "phaseN: <what you proved>"`
3. Tag it (the permanent proof): `./scripts/milestone.sh m<N>.<M>-mvm "<what proves it>"`
4. Flip its status ⬜→✅ above, then `./scripts/save.sh "roadmap: mark m<N>.<M> complete"`

Tag names: `m0.1-mvm`, `m0.1-full` (Full Pass), phase gates `p0-complete`.
The **tag** is the durable, timestamped evidence. The **✅** is the at-a-glance state.
No daily pushing, no new repo per milestone.

## The Masterpiece Standard

The portfolio is NOT a flea market of 30 desk toys. It is a dependency tree of
artifacts where each one proves a phase's skills AND feeds the next phase:

| Phase | Artifact                                                            | What it proves                                         | Feeds into              |
| ----- | ------------------------------------------------------------------- | ------------------------------------------------------ | ----------------------- |
| 0     | Parametric Mechanism Testbed + Metrology Kit                        | kinematics vocabulary, measurement uncertainty         | every measurement after |
| 1     | Hand-Wound Voice Coil Actuator + 3D-Printed Dynamometer             | Lorentz force, motor characterization, first soldering | QDD sizing in Phase 3   |
| 2     | Force-Feedback Haptic Knob + Inverted Pendulum Cart                 | FOC + impedance control + state-space on real hardware | QDD firmware in Phase 3 |
| 3     | Quasi-Direct Drive (QDD) Actuator: CNC housing + Puck PCB + gearbox | CAD, FEA, 4-layer PCB, EMC, machine elements           | the arm's joints        |
| 4     | 2-DOF Arm (two QDDs) + Safety PDU + Gripper + Tool Changer          | integration, CAN, functional safety, harnessing        | the portfolio hero      |
| 5     | Exploded-View Pedestal + Bench Museum                               | communication of the whole system                      | the interview           |

Every physical deliverable is judged by: *"Does this look like something a Tier-1
robotics supplier would ship, or a science fair project?"* Mount it, label it,
photograph it, characterize it. An uncharacterized artifact is a claim, not evidence.

## Fabrication & Safety Progression

You only use tools and voltages that the CURRENT phase has taught you.
No welding. No manual CNC. No mains — ever, in this roadmap.

| Phase | Primary fabrication | Secondary | Voltage ceiling | New skills introduced | NOT allowed yet |
| --- | --- | --- | --- | --- | --- |
| 0 | Cardboard, hand tools, 3D print (FDM) | Hobby knife, calipers, dial indicator | USB / 5V only | Calipers, measurement uncertainty, print tolerance calibration | Soldering, power tools |
| 1 | 3D print (FDM) | Through-hole soldering on perfboard | ≤ 24V DC | First soldering, current-limited supply, magnet-wire winding | SMD, CNC, metal cutting |
| 2 | 3D print, bolt-together aluminum extrusion | SMD optional (hot air) | ≤ 24V DC | Linear rail assembly, moving-mechanism safety | CNC services, > 24V |
| 3 | CNC services (SendCutSend/Xometry), JLCPCB | SMD reflow (hotplate), resin print optional | 48V DC bus enters | Bearing fits, GD&T, 4-layer layout, hotplate reflow, capacitor discharge | Welding, manual mill/lathe |
| 4 | Assembly of Phase 3 parts, laser-cut panels | Harnessing, crimping, DIN rail | 48V DC | Hardwired safety circuits, EMI harness discipline | Welding |
| 5 | Acrylic/wood display, laser-cut service | — | — | Presentation fabrication | — |

## Phase 0 — Foundations & Vocabulary

|**Milestone**|**Status**|
|---|---|
|[0.1 — Problem-Solving + Toolchain](milestones/00_foundations.md)|✅|
|[0.2 — Vectors + Trig](milestones/00_foundations.md)|✅|
|[0.3 — Calculus Intuition](milestones/00_foundations.md)|⬜|
|[0.4 — Statics + FBDs + FEM Intuition](milestones/00_foundations.md)|⬜|
|[0.5 — Circuits Basics](milestones/00_foundations.md)|⬜|
|[0.6 — Power + Thermal](milestones/00_foundations.md)|⬜|
|[0.7 — Materials + Failure + Selection](milestones/00_foundations.md)|⬜|
|[0.8 — Manufacturing + DFMA](milestones/00_foundations.md)|⬜|
|[0.9 — Mechanisms + Kinematic Elements + Physical Testbed](milestones/00_foundations.md)|⬜|
|[0.10 — Metrology + Measurement Uncertainty](milestones/00_foundations.md)|⬜|

## Phase 1 — Signals, Actuators, Dynamics

|**Milestone**|**Status**|
|---|---|
|[1.1 — I2C Sensor + Telemetry](milestones/01_signals_actuators_dynamics.md)|⬜|
|[1.2 — Noise + Filtering + Frequency Domain](milestones/01_signals_actuators_dynamics.md)|⬜|
|[1.3 — H-Bridge + BLDC Commutation](milestones/01_signals_actuators_dynamics.md)|⬜|
|[1.4 — Dynamics Model + Pendulum Rig](milestones/01_signals_actuators_dynamics.md)|⬜|
|[1.5 — Integration + Sensor Fusion + Calibration](milestones/01_signals_actuators_dynamics.md)|⬜|
|[1.6 — Stepper + Microstepping](milestones/01_signals_actuators_dynamics.md)|⬜|
|[1.7 — Voice Coil Actuator + Motor Test Rig](milestones/01_signals_actuators_dynamics.md)|⬜|

## Phase 2 — Embedded Architecture & Real-Time Control

|**Milestone**|**Status**|
|---|---|
|[2.1 — Bare-Metal STM32 + SPI + UART](milestones/02_embedded_realtime_control.md)|⬜|
|[2.2 — PID Theory + Tuning](milestones/02_embedded_realtime_control.md)|⬜|
|[2.3 — FOC Closed-Loop](milestones/02_embedded_realtime_control.md)|⬜|
|[2.4 — FreeRTOS Multi-Task](milestones/02_embedded_realtime_control.md)|⬜|
|[2.5 — Multi-DOF Dynamics + State-Space](milestones/02_embedded_realtime_control.md)|⬜|
|[2.6 — Limit Switches + Homing + State Machines](milestones/02_embedded_realtime_control.md)|⬜|
|[2.7 — Integrated Sub-System: Haptic Knob](milestones/02_embedded_realtime_control.md)|⬜|
|[2.8 — Inverted Pendulum Cart](milestones/02_embedded_realtime_control.md)|⬜|

## Phase 3 — Model-Based Design & Verification

|**Milestone**|**Status**|
|---|---|
|[3.0 — SIL Verification Gate](milestones/03_mech_pcb_verification.md)|⬜|
|[3.1 — QDD Actuator: CAD + Machine Elements + FEA](milestones/03_mech_pcb_verification.md)|⬜|
|[3.2 — The Puck: Custom FOC Driver PCB](milestones/03_mech_pcb_verification.md)|⬜|
|[3.3 — QDD Actuator Assembly + Characterization](milestones/03_mech_pcb_verification.md)|⬜|
|[3.4 — HIL Validation Gate](milestones/03_mech_pcb_verification.md)|⬜|

## Phase 4 — Capstone & Industrial Integration

|**Milestone**|**Status**|
|---|---|
|[4.1 — CAN + C++ Messaging](milestones/04_capstone_integration.md)|⬜|
|[4.2 — Motion + Dynamics-Aware Control](milestones/04_capstone_integration.md)|⬜|
|[4.3 — Safety PDU + Hardwired E-Stop](milestones/04_capstone_integration.md)|⬜|
|[4.4 — Workcell Integration + Harness](milestones/04_capstone_integration.md) (example — exit checklist, no new skill)|⬜|
|[4.5 — Electromechanical Gripper + Tool Changer](milestones/04_capstone_integration.md) (stretch example — optional)|⬜|

## Phase 5 — Portfolio & Delivery

|**Milestone**|**Status**|
|---|---|
|[5.1 — Portfolio + Documentation](milestones/05_portfolio_delivery.md)|⬜|
|[5.2 — Exploded-View Pedestal + Bench Museum](milestones/05_portfolio_delivery.md) (optional example — presentation, no new skill)|⬜|

## Calibration

|**Phase**|**Planned**|**Actual**|
|---|---|---|
|Phase 0|8–14 wk||
|Phase 1|12–20 wk||
|Phase 2|12–26 wk||
|Phase 3|12–22 wk||
|Phase 4|10–20 wk||
|Phase 5|4–8 wk||

_Planned = MVM scope; Full Pass multiplies the work, so schedule it separately. Update actuals only at phase completion._

## Resource Map

Learning resources are injected at the top of each milestone file — open the milestone, not a table.

## Reference

- [[Mechatronics/resources/SAFETY_CARD|Safety Card]] — read before any hardware work
- [[Mechatronics/resources/CONVENTIONS|Conventions]] — units, naming, coordinates
- [[Mechatronics/resources/FIELD_NOTES|Field Notes]] — career radar, reviewed at 12-week check
- [[Mechatronics/resources/LAB_INFRASTRUCTURE|Lab Infrastructure]] — tools, budget, sourcing

## Speed Runs

One per phase. Plus optional "from scratch" builds.

- **Phase 0** — LED blinky + motor spin on breadboard, video it (~1 wk)
- **Phase 0 opt** — Speaker from scratch: cup+magnet+coil → hear F=BIL (~1 weekend)
- **Phase 0 opt** — Generator from scratch: hand-crank magnet past a coil, light an LED (~1 weekend)
- **Phase 1** — IMU → PlotJuggler, post screenshot + explanation (~3 days)
- **Phase 2** — Port SimpleFOC to your STM32 in a weekend (~1 wk)
- **Phase 3** — Order a PCB from JLCPCB, modify one thing; FEA one bracket (~2 wk)
- **Phase 4** — Contribute a bug-fix/doc upstream (~1 wk of your time)

> **Note:** "Your time" = hours you spend, not calendar days.
>
> Speed Runs produce something explainable to someone outside your head.
>
> That's the Hypothesis Loop aimed outward. Free byproduct, not extra task.
>
> The "from scratch" builds are optional but recommended. They make the equations physical. A speaker is a linear motor you can hear. A generator is a motor run backwards. Neither requires a roadmap entry — they're weekend speed runs that change how the theory feels.
>
> The mechanism speed run is now folded into Milestone 0.9's physical testbed. Cardboard four-bars take 20 minutes. Seeing the Grashof condition change a crank-rocker into a double-rocker by flipping which link you hold is worth more than a page of derivation.

## Physical Artifact Dependency Tree

```
Phase 0: Metrology Kit + Mechanism Testbed
    │  (every later measurement inherits these skills)
    ▼
Phase 1: VCA + 3D-printed motor test rig (dynamometer frame)
    │  (you must be able to MEASURE a motor before you DESIGN one)
    ▼
Phase 2: Haptic Knob + Inverted Pendulum Cart
    │  (proves FOC + impedance + state-space on integrated hardware;
    │   the knob IS the QDD control stack in miniature)
    ▼
Phase 3: QDD Actuator = CNC housing + Puck PCB + planetary gearbox + dual encoders
    │  (the joint for the capstone arm)
    ▼
Phase 4: 2-DOF Arm (two QDDs) + Safety PDU + Gripper + Tool Changer
    │  (the portfolio hero)
    ▼
Phase 5: Exploded-View Pedestal + Bench Museum
```

Each artifact requires the skills of its phase. You cannot design the Puck PCB
without the analog front-end knowledge from Phase 1.3. You cannot build the QDD
without FOC from 2.3 and machine elements from 3.1. The dependency tree IS the curriculum.

## Skill Spine (the roadmap teaches verbs, not machines)

The spine is transferable verbs — derive, measure, drive, coordinate,
power, prove safe-state, calibrate, verify SIL→HIL. Artifacts are reference
instances that prove the verbs, not the goal. The 2-DOF arm is the reference
hero; it is not the definition of done.

- A project belongs in the graded path only if it teaches a NEW transferable
  skill. Pure integration/polish with no new verb is an example, not a gate:
  4.4 (harness at scale), 5.2 (display), and conditionally 4.5 (end-effector)
  are tagged as such above. Do them for the portfolio, or fold 4.4 into the
  4.2/4.3 exit checklist — zero skill is lost either way.
- Custom-project rule: when a phase arrives, you or the AI may propose a
  substitute project that hits the SAME verbs. State the verbs, the evidence
  plots, and the safety envelope before starting; if it teaches no new verb,
  it goes in the example pool, not the graded path.
- Phase-4b (optional, after the hero): a second machine — e.g. a 3-axis CNC —
  reusing the spine (stepper sizing, homing, fits, PDU, harness, calibration).
  Gated behind 4.3 safety PLUS a spindle/process addendum (cutting physics,
  G-code/CAM chain, tramming/squareness, interlocked extraction enclosure).
- Non-claim: this roadmap alone does not qualify you to build a cutting
  machine, touch mains/VFD power, or run pressure/fluid systems unsupervised.
  Those are post-roadmap addenda with their own safety cases.
