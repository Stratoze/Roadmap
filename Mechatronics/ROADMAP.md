# Mechatronics Roadmap

Raw delivery contract: **what must be delivered, what it depends on, search
keywords, and the safety/evidence boundary**. It is the only active milestone
status source. It is not a book/video library.

Legend: ⬜ not started · 🔨 active · ✅ complete

## Completion and evidence

1. Meet the milestone's MVM criteria and collect the learner's evidence.
2. Flip the milestone checkbox in this file.
3. Commit the evidence and completed checkbox together.
4. Create the signed tag on that clean commit:

```bash
bash scripts/milestone.sh <tag> "<what proves it>"
```

The tag is the durable proof and points at the commit containing the evidence
and the completed checkbox. Full Pass tags separately. Never use
`save.sh` for a broad cleanup commit.

## Master deliverables and dependency edges

| Phase | Milestone | Status | Deliverable | Depends on | Search keywords | Safety/evidence boundary |
|---|---|---|---|---|---|---|
| 0 | [0.1 Problem Solving + Toolchain](milestones/00_foundations.md) | ✅ | Reproducible toolchain, baseline commit, input/output reasoning | — | problem decomposition; Fermi estimate; binary-search debug; git baseline | Clean repo; no hardware claim without artifact |
| 0 | [0.2 Vectors + Frames](milestones/00_foundations.md) | ✅ | 2-link planar FK with frames and radians | 0.1 | vector components; forward kinematics; world/link frame; atan2 | Verify diagram before calculation; code uses radians |
| 0 | [0.3 Calculus Intuition](milestones/00_foundations.md) | ⬜ | Derivative/integral meaning and kinematic chains | 0.1, 0.2 | rate of change; accumulation; net change; Euler step | Formula is not the evidence; explain the model |
| 0 | [0.4 Statics + FBDs](milestones/00_foundations.md) | ⬜ | FBD, equilibrium, torque, FEM intuition | 0.2 | free-body diagram; moment arm; equilibrium; FEM validation | Hand calculation validates FEA; label assumptions |
| 0 | [0.5 Circuits Basics](milestones/00_foundations.md) | ⬜ | resistor sizing, KVL/KCL, datasheet and measurement discipline | 0.1 | Ohm's law; KVL; KCL; LED; DMM; oscilloscope | USB/5V only; current limit; datasheet limits |
| 0 | [0.6 Power + Thermal](milestones/00_foundations.md) | ⬜ | power budget, conduction loss, thermal chain | 0.5 | P=VI; I²R; efficiency; Rth; Rds(on) | Datasheet conditions; no final thermal claim without measurement |
| 0 | [0.7 Materials + Failure](milestones/00_foundations.md) | ⬜ | material selection, stress/strain, fatigue and failure | 0.4 | Ashby; stress-strain; fatigue; FoS; corrosion | Factor-of-safety and failure evidence required |
| 0 | [0.8 Manufacturing + DFMA](milestones/00_foundations.md) | ⬜ | manufacturing constraints and personal DFM/DFA rules | 0.7 | DFM; DFA; tolerance; casting; sheet metal; CNC | FDM/hand tools only in Phase 0 |
| 0 | [0.9 Mechanisms + Testbed](milestones/00_foundations.md) | ⬜ | kinematic testbed and mechanism vocabulary | 0.2, 0.4 | Grübler; Grashof; linkage; cam; backlash | Cardboard/hand tools; measure before modifying |
| 0 | [0.10 Metrology](milestones/00_foundations.md) | ⬜ | calibrated measurements with uncertainty | 0.6, 0.9 | uncertainty; RSS; resolution; accuracy; repeatability | Name instrument and report uncertainty |
| 1 | [1.1 I2C Sensor + Telemetry](milestones/01_signals_actuators_dynamics.md) | ⬜ | sensor read, register-level telemetry, reproducible data | 0.5, 0.10 | I2C; register; ADC; telemetry; PlotJuggler | Current-limited supply; no mains |
| 1 | [1.2 Noise, Filtering, and Frequency Domain](milestones/01_signals_actuators_dynamics.md) | ⬜ | noise diagnosis, filtering and frequency evidence | 1.1 | aliasing; FFT; window; filter; SNR | Preserve raw data; state sample rate |
| 1 | [1.3 H-Bridge, BLDC Commutation + Characterization](milestones/01_signals_actuators_dynamics.md) | ⬜ | characterized H-bridge and BLDC drive | 0.6, 1.1 | H-bridge; PWM; back-EMF; commutation; Kt | ≤24V DC; current limit; scope at safe points |
| 1 | [1.4 Pendulum Dynamics](milestones/01_signals_actuators_dynamics.md) | ⬜ | model and hardware validation of pendulum dynamics | 0.3, 1.2 | EOM; solve_ivp; phase portrait; validation | Model error and uncertainty reported |
| 1 | [1.5 Sensor Fusion](milestones/01_signals_actuators_dynamics.md) | ⬜ | calibrated fusion with stated error | 1.1, 1.2 | complementary filter; calibration; uncertainty | No fused claim without raw/error comparison |
| 1 | [1.6 Stepper + Microstepping](milestones/01_signals_actuators_dynamics.md) | ⬜ | current-limited stepper characterization | 0.5, 0.6 | stepper; microstepping; resonance; torque-speed | Current limit and thermal margin |
| 1 | [1.7 Voice Coil Actuator + Motor Test Rig](milestones/01_signals_actuators_dynamics.md) | ⬜ | actuator/dynamometer characterization | 0.4, 0.6, 1.3 | Lorentz force; voice coil; load cell; Kt/Ke | Mechanical travel and current limits |
| 2 | [2.1 Bare-Metal STM32](milestones/02_embedded_realtime_control.md) | ⬜ | register-level firmware foundation | 0.5, 1.1 | STM32; linker; CMake; OpenOCD; GDB | Current-limited bench supply; no mains |
| 2 | [2.2 PID in Simulation](milestones/02_embedded_realtime_control.md) | ⬜ | plant, PID, windup and bandwidth evidence | 0.3, 1.4 | PID; step response; windup; Bode; tuning | Simulation claims separate from hardware |
| 2 | [2.3 FOC Closed Loop](milestones/02_embedded_realtime_control.md) | ⬜ | current/torque loop with logged evidence | 1.3, 2.1, 2.2 | Clarke; Park; PWM; Id/Iq; bandwidth | Independent current limit; no red-zone final values |
| 2 | [2.4 FreeRTOS Firmware](milestones/02_embedded_realtime_control.md) | ⬜ | concurrent firmware with timing proof | 2.1, 2.3 | FreeRTOS; ISR; WCET; watchdog; priority inversion | Timing and watchdog evidence required |
| 2 | [2.5 Multi-DOF Dynamics + State-Space Control](milestones/02_embedded_realtime_control.md) | ⬜ | 2-link model and state-space control | 0.3, 0.4, 2.2 | Lagrangian; state-space; LQR; controllability | Model assumptions and validation stated |
| 2 | [2.6 Homing + State Machines](milestones/02_embedded_realtime_control.md) | ⬜ | safe homing and fault-aware state machine | 2.1, 2.4 | limit switch; homing; debounce; FAULT; statechart | Fail-safe stops; no motion without guard |
| 2 | [2.7 Haptic Knob](milestones/02_embedded_realtime_control.md) | ⬜ | integrated impedance-control subsystem | 2.3, 2.6 | impedance; admittance; detent; force feedback | Force/current limits; fault injection |
| 2 | [2.8 Inverted Pendulum Cart](milestones/02_embedded_realtime_control.md) | ⬜ | stabilized cart with fault evidence | 2.5, 2.6 | LQR; state feedback; cart; limits | Mechanical guards; E-stop path tested |
| 3 | [3.0 SIL Verification Gate](milestones/03_mech_pcb_verification.md) | ⬜ | model/instruction verification before hardware | 2.3–2.6 | SIL; requirements trace; fault injection | Gate cannot be bypassed by prose |
| 3 | [3.1 QDD CAD + Machine Elements](milestones/03_mech_pcb_verification.md) | ⬜ | manufacturable QDD housing and drawings | 0.7, 0.8, 0.9, 3.0 | CAD; FEA; bearing; tolerance; drawings | Hand calc before FEA; services before manual machining |
| 3 | [3.2 Puck PCB](milestones/03_mech_pcb_verification.md) | ⬜ | FOC driver PCB with power/EMC evidence | 2.3, 3.0, 3.1 | PCB; current sense; layout; EMC; creepage | Current/power/thermal limits in validation plan |
| 3 | [3.3 QDD Assembly + Characterization](milestones/03_mech_pcb_verification.md) | ⬜ | integrated joint with Kt/Ke/thermal data | 3.1, 3.2 | characterization; Kt; Ke; backlash; thermal | Safe current/torque envelope; uncertainty reported |
| 3 | [3.4 HIL Validation Gate](milestones/03_mech_pcb_verification.md) | ⬜ | hardware-in-loop fault and performance evidence | 3.0, 3.3 | HIL; fault injection; coverage; timing | Gate requires reproducible artifacts |
| 4 | [4.1 CAN + C++ Messaging](milestones/04_capstone_integration.md) | ⬜ | reliable distributed message/interface layer | 2.4, 3.4 | CAN; C++; protocol; timing; fault | Bus fault and watchdog behavior tested |
| 4 | [4.2 Motion Integration](milestones/04_capstone_integration.md) | ⬜ | dynamics-aware arm motion and tracking | 2.5, 4.1 | inverse kinematics; trajectory; tracking; limits | Workspace and joint limits enforced |
| 4 | [4.3 Safety PDU + E-Stop](milestones/04_capstone_integration.md) | ⬜ | hardwired safe power distribution and stop | 3.3, 3.4 | PDU; E-stop; contactor; fuse; safety relay | No mains; safety card and hardwired stop required |
| 4 | [4.4 Workcell Integration](milestones/04_capstone_integration.md) | ⬜ | serviceable, EMC-controlled integration | 4.1–4.3 | harness; EMC; crimp; labeling; operability | 48V ceiling; strain relief and cold-boot checks |
| 4 | [4.5 Electromechanical Gripper + Tool Changer](milestones/04_capstone_integration.md) | ⬜ | separable end-effector interface | 0.9, 4.2 | gripper; tool changer; interface; force | Interface and stored-energy limits verified |
| 5 | [5.1 Portfolio + Documentation](milestones/05_portfolio_delivery.md) | ⬜ | reproducible portfolio and evidence narrative | 3.4, 4.4, 4.5 | documentation; requirements trace; demo; limitations | Every claim links to evidence; no invented results |
| 5 | [5.2 Display / Bench Museum](milestones/05_portfolio_delivery.md) | ⬜ | optional communication/presentation artifact | 5.1 | exploded view; labeling; presentation | Optional example; no new skill claim |

## Fabrication and safety envelope

| Phase | Tools allowed | Voltage ceiling | Explicitly not allowed |
|---|---|---|---|
| 0 | Cardboard, hand tools, FDM, calipers | USB/5V | Soldering, power tools |
| 1 | FDM, hand tools, through-hole soldering | ≤24V DC | SMD, CNC, metal cutting |
| 2 | FDM, extrusion, optional SMD | ≤24V DC | CNC services, >24V |
| 3 | CNC/PCB services, controlled assembly | 48V DC bus | Welding, manual mill/lathe |
| 4 | Assembly, laser-cut panels, crimping/DIN rail | 48V DC | Welding |
| 5 | Display/laser-cut/wood/acrylic services | As tested | Mains or unverified powered systems |

The safety card and milestone landmines are authoritative for the details.

## Artifact dependency tree

```text
Phase 0 metrology + mechanism testbed
  → Phase 1 measured motor/actuator characterization
    → Phase 2 control and embedded integration
      → Phase 3 characterized QDD joint
        → Phase 4 safe arm, workcell, and interfaces
          → Phase 5 evidence-backed portfolio
```

## Skill Spine

Detailed transferable-skill ownership and assessment policy lives in
[[Mechatronics/skills/registry|skill registry]] and the assessor brief. The
roadmap only records the milestone deliverable and evidence boundary.

## Speed runs

Speed runs are optional recommendations, not commitments. They live in
[[Mechatronics/IDEAS|Ideas]]. After a phase is complete, ask whether the
learner wants the next speed run or wants to move on.

## Calibration

| Phase | Planned | Actual |
|---|---|---|
| Phase 0 | 8–14 weeks | 2/10 in ~2.5 weeks (partial) |
| Phase 1 | 12–20 weeks | |
| Phase 2 | 12–26 weeks | |
| Phase 3 | 12–22 weeks | |
| Phase 4 | 10–20 weeks | |
| Phase 5 | 4–8 weeks | |

Planned means MVM scope. Full Pass is separate work.

## Active references

- [[Mechatronics/resources/SAFETY_CARD|Safety Card]]
- [[Mechatronics/resources/CONVENTIONS|Conventions]]
- [[Mechatronics/resources/FIELD_NOTES|Field Notes]]
- [[Mechatronics/resources/LAB_INFRASTRUCTURE|Lab Infrastructure]]
- [[Mechatronics/milestones/evidence/Index|Evidence index]]

An uncharacterized artifact is a claim, not evidence. This roadmap does not
qualify the learner to build a cutting machine, touch mains/VFD power, or run
pressure/fluid systems unsupervised; those require separate safety cases.
