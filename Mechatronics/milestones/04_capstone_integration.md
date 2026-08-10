# Phase 4 — Capstone & Industrial Integration

## Outcome

Complete, tested, documented workcell. Distributed architecture, safety systems, automated testing, industrial-grade integration.
This phase is about hardening, not adding features.


### Domain Standards Anchoring
This phase simulates professional engineering. To ground it in reality, adopt ONE
domain-specific constraint set for the capstone:

- **Motorsport (F1/FSAE):** Sensor homologation (every sensor must be traceable to a known calibration). Standardized data logging format. ECU must survive vibration and thermal cycling per regulation. Reference: FIA Technical Regulations, FSAE rules.
- **Aerospace:** V-Model with formal verification gates. Requirements traceability (every test maps to a requirement). Reference: NASA Systems Engineering Handbook, DO-178C for software.
- **Industrial automation:** IEC 62061 / ISO 13849 for safety-related control systems. Functional safety integrity levels (SIL). Reference: IEC 62061, ISO 13849-1.

You don't need to implement the full standard. But the capstone's safety milestone (4.3) and verification approach should reference the standard you chose. Document which standard and which clauses apply. This is what separates "I built a robot arm" from "I built a robot arm with a safety case."

---

## Phase Pass Condition

### MVM

- [ ] CAN packets error-free between STM32 and ESP32
- [ ] Arm tracks coordinate waypoints, IK working
- [ ] E-Stop physically disconnects motor power
- [ ] HIL: one fault injected, firmware enters safe state

### Full Pass

- [ ] C++ messaging: no dynamic malloc, compile-time types
- [ ] CAN design documented: message IDs, packet structs, termination, error/bus-off recovery, and versioning
- [ ] Smooth multi-axis coordinated motion with dynamics-aware feedforward
- [ ] E-Stop: dual-channel, hardware contactors, software-independent
- [ ] HIL: 3+ fault types, automated, documented
- [ ] Workcell: EMI shielding, labels, structural alignment
- [ ] Full cold-boot-to-shutdown, repeatable 3×

---

# Milestone 4.1 — CAN + C++ Messaging

> [!info] 📚 Resources — CAN + C++ Messaging
> **Visual:** CAN-bus arbitration/frame explainers.
> **Interactive:** two-node CAN round-trip; 1000-packet stress test; no dynamic allocation.
> **Theory:** CAN frame format; Lospinoso *C++ Crash Course*.


## Deliverable

Object-oriented C++ communication layer, error-free packets across physical CAN. No dynamic allocation. Compile-time types.

## Pass Condition

### MVM

- [ ] CAN frame sent and received
- [ ] Struct-based packet round-trips correctly
- [ ] No malloc/new in the codebase

### Full Pass

- [ ] Abstract CANObject base class
- [ ] 2+ concrete message types
- [ ] Bus-off recovery, overrun detection
- [ ] CAN physical layer verified: termination, common ground, differential waveform, and bit timing/sample point documented
- [ ] Message design documented: IDs, structs, endianness, versioning, timeout/heartbeat behavior
- [ ] Message integrity handled: CRC/checksum or equivalent, sequence numbers, timeout, heartbeat, stale-command handling, and safe default on loss of comms.
- [ ] 1000-packet stress test: zero dropped
- [ ] Compiles `-Wall -Wextra`, zero warnings

> [!warning] ⚠️ Landmines
> 1. **CAN is not UART with extra steps.** `[COMMUNITY]`
>    Multi-master broadcast bus with arbitration. You broadcast a frame with an ID; every node decides whether to process it.
>
> 2. **Termination resistors are not optional.** `[COMMUNITY]`
>    120 Ω at each end. Without them, reflections corrupt frames at higher bit rates. Works at 125k but fails at 500k → check termination.
>
> 3. **No dynamic allocation, no exceptions, no RTTI.** `[COMMUNITY]`
>    malloc fragments over hours. Exceptions add unpredictable timing. Fixed-size buffers, static allocation, compile-time polymorphism.
>
> 4. **CAN bit timing must match on all nodes.** `[COMMUNITY]`
>    Sample point, propagation segment, phase segments — identical on every node. Use a bit timing calculator.
>
> 5. **Message design is part of reliability.** `[HYPOTHESIS]`
> Define IDs, struct layout, endianness, version, timeout, and heartbeat behavior before scaling to multiple nodes. Ambiguous messages become intermittent faults that are painful to diagnose.
>

## Dependencies that waste your week if hit backwards

- Wire transceivers + termination BEFORE writing any CAN code. Verify the physical layer with a scope first.
- Get a basic frame round-tripping BEFORE designing the packet structure or class hierarchy.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 4.2 — Motion Integration + Dynamics-Aware Control

> [!info] 📚 Resources — Motion Integration & Dynamics-Aware Control
> **Visual:** inverse-kinematics / trajectory-shaping videos.
> **Interactive:** Python IK — X,Y→θ1,θ2, straight-line interpolation, feedforward torque.
> **Theory:** Craig Ch 6–7; computed-torque / minimum-jerk trajectories.


## Deliverable

Inverse kinematics on STM32: X, Y → θ1, θ2, smooth joint-interpolated moves between waypoints. Then: add dynamics-aware feedforward from the Milestone 2.5 model, so the arm moves well under its own coupled inertia, not just "joints go to angles."

## Pass Condition

### MVM

- [ ] IK function: given X, Y, returns θ1, θ2
- [ ] Arm moves to a commanded position
- [ ] Can verify: command X, Y, measure tip, compare

### Full Pass

- [ ] Multi-waypoint trajectory, smooth, no jerky stops
- [ ] Workspace limits enforced
- [ ] Repeatable: same point 10×, tip varies < 1 mm
- [ ] Demo: arm traces a straight line or circle
- [ ] **Feedforward torque:** τ_ff = M(q)q̈_des + C(q, q̇)q̇ + g(q) computed in firmware or precomputed per trajectory point. PID handles the residual. Show: tracking error with feedforward < tracking error without.
- [ ] **Trajectory shaping:** minimum-jerk or trapezoidal velocity profile. No infinite acceleration at waypoints. Can explain: a step command in position → infinite acceleration → infinite torque → actuator saturates → tracking error. Shaped trajectory avoids this.
- [ ] **Coupled motion test:** command a fast diagonal move. Without feedforward, joint 1 sags because joint 2's acceleration changes the inertia seen by joint 1. With feedforward, the sag is reduced. Document the difference.
- [ ] Can explain: this is why Milestone 2.5 existed. The dynamics model is not academic. It's in the control loop.

> [!warning] ⚠️ Landmines
> 1. **IK has two solutions, elbow up / down.** `[COMMUNITY]`
>    Pick one convention. If the arm flips mid-trajectory, it swings wildly.
>
> 2. **Joint limits are physical, not just software.** `[HYPOTHESIS]`
>    IK returns θ1 = 200° but the joint stops at 180°. Enforce in software BEFORE commanding motors. Also enforce velocity limits.
>
> 3. **Straight-line in workspace ≠ straight-line in joint space.** `[COMMUNITY]`
>    Linearly interpolating θ1, θ2 → curved tip path. For straight tip, interpolate in X, Y and compute IK each timestep.
>
> 4. **Singularity at full extension.** `[COMMUNITY]`
>    θ2 = 0 → Jacobian singular. Small X, Y changes → huge θ changes. Add a margin from the workspace boundary.
>
> 5. **Feedforward model mismatch is normal.** `[HYPOTHESIS]`
>    Your M(q), C(q, q̇), g(q) model has parameter errors: link mass, CoM location, friction. The feedforward won't be perfect. That's why PID is still there — it handles the residual. If feedforward makes things WORSE, the model is wrong. Check signs, check parameters, check that q̇ and q̈ are in the right frame.
>
> 6. **Minimum-jerk is not optional for smooth motion.** `[COMMUNITY]`
>    A trapezoidal velocity profile has discontinuous acceleration (jerk = ∞ at transitions). The arm jerks. Minimum-jerk (quintic polynomial) or S-curve profiles make acceleration continuous. The difference is visible and audible.
>
> 7. **Don't run the full dynamics model at 1 kHz if it's too slow.** `[HYPOTHESIS]`
>    M(q) is 2×2, C is 2×2, g is 2×1. On an STM32F4, this is fast. But if you add friction models, payload estimation, or higher DOF, compute budget matters. Profile it. If the model takes 200 µs and your loop is 1 ms, you have 80% headroom. If it takes 800 µs, you have a problem.
>

## Dependencies that waste your week if hit backwards

- Derive IK on paper and verify against FK BEFORE coding. FK(θ1, θ2) should return the original X, Y.
- Single-point moves BEFORE multi-waypoint trajectories.
- Verify repeatability at one point BEFORE tracing paths.
- Get PID-only motion working BEFORE adding feedforward. You need the baseline to measure improvement.
- Verify the dynamics model (Milestone 2.5 sim) against real arm behavior BEFORE putting it in firmware. If the sim doesn't match the real arm, the feedforward will fight the PID.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 4.3 — Safety + HIL

> [!info] 📚 Resources — Safety + HIL
> **Standards:** IEC 62061 / ISO 13849 (functional safety); dual-channel E-stop; safe-state definition.
> **Interactive:** fault injection — overcurrent, encoder dropout, undervoltage; verify safe state.


## Deliverable

Hard-wired dual-channel E-Stop, software-independent, plus automated HIL test bench for fault injection.

## Pass Condition

### MVM

- [ ] E-Stop physically disconnects motor DC bus
- [ ] Pressing E-Stop during motion stops motors immediately
- [ ] HIL: one fault injected, firmware enters safe state

### Full Pass

- [ ] E-Stop: dual-channel, electromechanical contactors
- [ ] Works even if MCU is dead, pull MCU power, press E-Stop, motors stop
- [ ] Safe state defined per axis: de-energize, brake, counterbalance, or controlled stop; gravity axes cannot fall dangerously
- [ ] Enable lines, watchdog/heartbeat, brownout, and fault latch behavior documented and tested
- [ ] Hazard analysis performed: single-point failures, fail-safe vs fail-operational behavior, independent safety paths, and acceptance test criteria defined before integration.
- [ ] HIL: 3+ fault types, overcurrent, encoder dropout, undervoltage
- [ ] Fault log recorded
- [ ] Recovery procedure documented

> [!warning] ⚠️ Landmines
> 1. **Software E-Stop is not a safety E-Stop.** `[COMMUNITY — IEC 62061]`
>    If it goes through the MCU, a firmware crash means no E-Stop. The safety loop must be HARDWIRED: button → contactor → drops bus power.
>
> 2. **Dual-channel means two independent paths.** `[COMMUNITY]`
>    One contact can weld shut. Two in series, forced-guided contacts.
>
> 3. **HIL must not damage real hardware.** `[HYPOTHESIS]`
>    Simulate sensor signals with a secondary MCU. Don't create real overcurrent on the bus. Test the FIRMWARE's response, not hardware survival.
>
> 4. **Define the safe state BEFORE building the safety system.** `[HYPOTHESIS]`
>    "Stop" is not specific. For an arm under gravity, de-energize = arm falls. Is that safe? Maybe you need a brake or counterbalance.
>
> 5. **Enable lines and watchdogs are control safety, not power safety.** `[HYPOTHESIS]`
> Firmware enable/disable and watchdog resets can stop a running controller, but they do not guarantee removal of stored energy or motor power. For a true safe state, define the power path, brakes, counterbalances, and contactor behavior independently of software.
>

## Dependencies that waste your week if hit backwards

- Define the safe state on paper BEFORE wiring anything.
- Test the E-Stop with MCU power PULLED before testing with firmware. The hardware path must work independently.
- Build HIL fault injection on a secondary MCU BEFORE connecting it to the production system.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 4.4 — Workcell Polish

> [!info] 📚 Resources — Workcell Polish
> Mostly self-work: labeling, shielding, cable management, cold-boot testing.
> Reference: your own EMC rules from Milestone 3.2.


## Deliverable

Clean, labeled, shielded, industry-grade installation. Everything wired, aligned, tested, documented.

## Pass Condition

### MVM

- [ ] All cables routed, labeled, secured
- [ ] No loose wires or dangling connectors
- [ ] EMI shielding on critical signal lines

### Full Pass

- [ ] Braided shielding on motor cables near signal lines
- [ ] Structural mounting verified, no wobble under load
- [ ] Limit switches installed and tested
- [ ] Cold-boot-to-shutdown repeatable 3×
- [ ] Everything labeled: cables, connectors, boards, rails
- [ ] Harness discipline: strain relief, bend radius, connector locking, service access, and both-end labels verified
- [ ] Human factors reviewed: system state/mode visible at a glance, errors are understandable, warnings are prioritized, controls afford correct use, labels/cable IDs support a tired operator, and a naive user can identify stop/recovery.
- [ ] Photos taken, portfolio

> [!warning] ⚠️ Landmines
> 1. **EMI is the reason your encoder glitches.** `[COMMUNITY]`
>    Motor PWM → broadband noise. Route signal lines perpendicular to power lines. Braided shield on motor cables, grounded at ONE end.
>
> 2. **Labels are not optional documentation.** `[HYPOTHESIS]`
>    In 3 months you won't remember which connector is which. Label both ends of every cable. Every board. Every rail.
>
> 3. **"Polish" is not "add features."** `[HYPOTHESIS]`
>    Do not add a conveyor. Do not add a camera. Tighten what's there. Label it. Shield it. Test it cold. Document it. Done.
>

## Dependencies that waste your week if hit backwards

- Make a wiring diagram BEFORE re-routing cables. Otherwise you'll disconnect something and forget where it went.
- Test limit switches with software limits DISABLED to verify the hardware path independently.

> Log sessions in Daily/ notes using the unified template.

---

# Phase 4 Deload / Synthesis

- [ ] Explain the CAN packet structure from memory
- [ ] Derive 2-link IK on paper
- [ ] Write the feedforward torque equation from memory: τ_ff = M(q)q̈ + C(q, q̇)q̇ + g(q)
- [ ] Explain why minimum-jerk trajectories matter, physically
- [ ] Draw the E-Stop circuit from memory
- [ ] List all HIL fault scenarios and expected firmware responses
- [ ] Run `scripts/versions.sh` and `scripts/cold_tools.sh`

## Phase 4 Retro

Actual time vs. range, 9–18 wk:

Most valuable landmine:

Missing landmine:

What Phase 5 needs from Phase 4:
