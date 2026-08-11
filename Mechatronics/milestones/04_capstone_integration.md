# Phase 4 — Capstone & Industrial Integration

## Outcome

Complete, tested, documented workcell. Distributed architecture, safety systems, automated testing, industrial-grade integration.

This phase is about hardening, not adding features. The arm is two QDD actuators from Phase 3, a CAN bus, a hardwired Safety PDU, a gripper, a tool changer, and a harness that a technician could service.

**Physical artifacts of this phase:**
1. 2-DOF Arm — two Phase 3 QDD actuators on the machined base
2. Safety PDU — dual-channel hardwired E-stop, DC-rated contactors, fusing
3. CAN + power harness — shielded, labeled both ends, strain-relieved
4. Electromechanical Gripper — printed linkage, force-limited fingertips
5. Automated Tool Changer — dowel alignment + pogo-pin electrical contacts

**Fabrication & safety envelope (Phase 4):**
- Assembly, harnessing, crimping, laser-cut panels. No new machining services unless a single bracket is genuinely required.
- 48 V bus at real current. Lockout discipline: power off, caps discharged, verified with meter before hands go in.
- NEW hazard: **gravity-loaded arm.** Define the fall path before first power. If de-energize = fall, the fall zone must be clear, or add a brake/counterbalance.
- E-stop is tested with MCU power PULLED. If it only works when firmware runs, it is not a safety system.
- Still no welding, no mains.

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
- [ ] CAN packets error-free between STM32 nodes and ESP32
- [ ] Arm tracks coordinate waypoints, IK working
- [ ] E-Stop physically disconnects motor power
- [ ] HIL: one fault injected, firmware enters safe state
- [ ] **Physical:** arm assembled, moves under control
- [ ] **Physical:** E-stop stops the arm with MCU power pulled

### Full Pass
- [ ] C++ messaging: no dynamic malloc, compile-time types
- [ ] CAN design documented: message IDs, packet structs, termination, error/bus-off recovery, and versioning
- [ ] Smooth multi-axis coordinated motion with dynamics-aware feedforward
- [ ] E-Stop: dual-channel, DC-rated contactors, software-independent
- [ ] HIL: 3+ fault types, automated, documented
- [ ] Workcell: EMI shielding, labels, structural alignment
- [ ] Full cold-boot-to-shutdown, repeatable 3×
- [ ] **Physical:** gripper picks and places a 100 g object
- [ ] **Physical:** tool changer swaps gripper for a second tool; electrical contacts work after swap
- [ ] **Physical:** harness labeled both ends, strain relief at every connector

---

# Milestone 4.1 — CAN + C++ Messaging

> [!info] 📚 Resources — CAN + C++ Messaging
> **Visual:** CAN-bus arbitration/frame explainers.
> **Interactive:** two-node CAN round-trip; 1000-packet stress test; no dynamic allocation.
> **Theory:** CAN frame format; Lospinoso *C++ Crash Course*.

## Deliverable

Object-oriented C++ communication layer, error-free packets across physical CAN between the two QDD Pucks and an ESP32 gateway. No dynamic allocation. Compile-time types.

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
- Run CAN between the two Pucks on the bench BEFORE the arm is assembled. Debugging a bus inside a harness is misery.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 4.2 — Motion Integration + Dynamics-Aware Control

> [!info] 📚 Resources — Motion Integration & Dynamics-Aware Control
> **Visual:** inverse-kinematics / trajectory-shaping videos.
> **Interactive:** Python IK — X,Y→θ1,θ2, straight-line interpolation, feedforward torque.
> **Theory:** Craig Ch 6–7; computed-torque / minimum-jerk trajectories; your 2.5 model.

## Deliverable

The 2-DOF arm — two QDD actuators — tracking coordinated trajectories. IK on the gateway (X, Y → θ1, θ2), minimum-jerk trajectory shaping, and dynamics-aware feedforward from the 2.5 model. Because the joints are backdrivable QDDs, you can also demonstrate impedance behavior: push the arm, it yields and recovers. That demo is your interview story.

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
- [ ] **Backdrivability demo:** with the controller in impedance mode, push the arm by hand; it yields and holds the new pose. Video.
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
>    M(q) is 2×2, C is 2×2, g is 2×1. On an STM32G4 this is fast, but friction models and payload estimation grow the budget. Profile it. If the model eats 80% of the loop, you have a problem.
>
> 8. **First motion of a gravity-loaded arm needs the fall path cleared.** `[HYPOTHESIS]`
>    Before the first powered move: what happens if power drops mid-motion? If the answer is "it falls," make sure nothing — hands included — is in the fall zone. Low speed, low gain for first moves.
>

## Dependencies that waste your week if hit backwards

- Derive IK on paper and verify against FK BEFORE coding. FK(θ1, θ2) should return the original X, Y.
- Single-point moves BEFORE multi-waypoint trajectories.
- Verify repeatability at one point BEFORE tracing paths.
- Get PID-only motion working BEFORE adding feedforward. You need the baseline to measure improvement.
- Verify the dynamics model (Milestone 2.5 sim) against real arm behavior BEFORE putting it in firmware. If the sim doesn't match the real arm, the feedforward will fight the PID.
- Both QDDs characterized on the rig (3.3) BEFORE trusting them in the arm.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 4.3 — Safety PDU + Hardwired E-Stop

> [!info] 📚 Resources — Safety PDU & Hardwired E-Stop
> **Standards:** IEC 62061 / ISO 13849-1 (functional safety); dual-channel E-stop; safe-state definition.
> **Interactive:** build the PDU on DIN rail; test E-stop with MCU power pulled; fault injection on the HIL bench.
> **Fabrication:** DIN rail + DC-rated contactors + NC dual-channel E-stop + fuses; panel via laser-cut acrylic or sheet-metal service.

## Deliverable

A panel-mounted Power Distribution Unit: 48 V in → fuse → dual-channel contactors → per-actuator fused outputs; separate always-live logic rail for the MCUs so faults get logged. The E-stop button drives the contactors DIRECTLY — no MCU in the loop. Plus the automated HIL fault-injection bench.

**Safe state definition (write it before wiring anything):**
- E-stop pressed → contactors open → 48 V bus physically disconnected.
- Arm under gravity: de-energize means fall. If the fall path is not guaranteed clear, document the mitigation (counterbalance, brake, or restricted pose envelope).
- Logic rail stays up → fault logged → CAN broadcasts E_STOP.
- Recovery: release E-stop → reset → re-home → re-arm.

## Pass Condition

### MVM
- [ ] E-stop physically disconnects the 48 V bus (measured with a meter)
- [ ] Pressing E-stop during motion stops the motors
- [ ] Works with MCU power PULLED
- [ ] HIL: one fault injected, firmware enters safe state

### Full Pass
- [ ] Dual-channel: two contactors in series; can explain why one is not enough (contact weld)
- [ ] Contactors are DC-rated at bus voltage/current; datasheet DC rating cited
- [ ] Fuses sized per actuator stall + inrush; documented
- [ ] Logic supply independent of E-stop; MCU logs the event
- [ ] Safe state per axis defined and tested, including the gravity case
- [ ] Hazard analysis documented: single-point failures, failsafe vs fail-operational, acceptance criteria
- [ ] HIL: 3+ fault types (encoder dropout, overcurrent, undervoltage), automated, fault log per `templates/fault_injection_test.md`
- [ ] Recovery procedure documented and rehearsed
- [ ] **Physical:** panel labeled (every terminal, fuse, connector); photo

> [!warning] ⚠️ Landmines
> 1. **Software E-Stop is not a safety E-Stop.** `[COMMUNITY — IEC 62061]`
>    If it goes through the MCU, a firmware crash means no E-Stop. The safety loop must be HARDWIRED: button → contactor → drops bus power.
>
> 2. **Dual-channel means two independent paths.** `[COMMUNITY]`
>    One contact can weld shut. Two in series, forced-guided contacts.
>
> 3. **AC contactor ratings lie on DC buses.** `[COMMUNITY]`
>    DC arcs don't cross zero and don't self-extinguish. A contactor rated 240 VAC may weld shut at 48 VDC. Use the DC rating from the datasheet, with margin.
>
> 4. **The E-stop button must be NC.** `[COMMUNITY]`
>    Wire break must LOOK LIKE a press. NO fails silently. (You learned this in 2.6; here it's enforced with contactors.)
>
> 5. **HIL must not damage real hardware.** `[HYPOTHESIS]`
>    Simulate sensor signals with a secondary MCU. Don't create real overcurrent on the bus. Test the FIRMWARE's response, not hardware survival.
>
> 6. **Define the safe state BEFORE building the safety system.** `[HYPOTHESIS]`
>    "Stop" is not specific. For an arm under gravity, de-energize = fall. Is that safe? Maybe you need a brake or counterbalance.
>
> 7. **Bus capacitors stay charged after E-stop.** `[HYPOTHESIS]`
>    Opening the contactors doesn't drain the Puck's input caps. Bleed resistors or a documented discharge wait before anyone touches the bus. Verify < 1 V with a meter.
>
> 8. **Enable lines and watchdogs are control safety, not power safety.** `[HYPOTHESIS]`
>    Firmware enable/disable and watchdog resets can stop a running controller, but they do not guarantee removal of stored energy or motor power. For a true safe state, define the power path, brakes, counterbalances, and contactor behavior independently of software.
>

## Dependencies that waste your week if hit backwards

- Define the safe state on paper BEFORE wiring anything.
- Test the E-stop with MCU power PULLED before testing with firmware. The hardware path must work independently.
- Build HIL fault injection on a secondary MCU BEFORE connecting it to the production system.
- Wire and cold-test the PDU with a resistive load BEFORE connecting the actuators.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 4.4 — Workcell Integration + Harness

> [!info] 📚 Resources — Workcell Integration
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
- [ ] Braided shielding on motor cables near signal lines; CAN is shielded twisted pair, 120 Ω at both ends
- [ ] Shield grounded at ONE end only (your Phase 3 EMC rule, now at system scale)
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
> 4. **Strain relief is a failure mode, not a style choice.** `[HYPOTHESIS]`
>    A connector that can be levered by cable weight will intermittently disconnect and look like a firmware bug. Every cable gets relief within 30 mm of its connector.
>

## Dependencies that waste your week if hit backwards

- Make a wiring diagram BEFORE re-routing cables. Otherwise you'll disconnect something and forget where it went.
- Test limit switches with software limits DISABLED to verify the hardware path independently.
- Verify CAN + power on the bench (4.1) BEFORE harnessing the arm.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 4.5 — Electromechanical Gripper + Tool Changer

> [!info] 📚 Resources — Gripper & Tool Changer
> **Visual:** Robotiq-style gripper teardowns; quick-changer mechanism videos.
> **Interactive:** design in CAD, print in PETG/nylon, test grip force with your Phase 1 load cell.
> **Theory:** friction cone at the fingertips, linkage mechanical advantage, pogo-pin working stroke (datasheet), dowel alignment.
> **Fabrication:** 3D print (PETG or nylon). Purchased pogo pins, dowel pins, small magnets, adhesive rubber feet. No CNC.

## Deliverable

**Gripper:** two-finger linkage driven by a small servo/stepper, mounted to the arm's end. Fingertips with rubber pads. Holds a 100 g object against gravity; grip force measured with the load cell from Phase 1.7.

**Tool changer:** manual-latch or motorized quick-disconnect at the wrist. Alignment by dowel pins or cone-and-v. Electrical continuity via pogo pins (power + CAN pass-through). Second tool: pen holder or suction stub — anything that proves the swap.

## Pass Condition

### MVM
- [ ] Gripper opens/closes under command
- [ ] Holds 100 g against gravity for 10 s
- [ ] Tool changer: gripper removes and re-attaches by hand, repeatably

### Full Pass
- [ ] Grips 20–60 mm objects without reconfiguration
- [ ] Grip force measured and documented (load cell + uncertainty from Phase 1)
- [ ] Electrical contacts work AFTER a swap (CAN + power verified)
- [ ] Alignment repeatability measured < 0.5 mm (calipers/dial indicator)
- [ ] **Physical:** pick-and-place demo video; labeled; photos

> [!warning] ⚠️ Landmines
> 1. **Printed joints wear.** `[COMMUNITY]`
>    A printed pin joint loosens after hundreds of cycles. Nylon resists wear better than PETG; metal pins in printed holes last longer than printed pins. This is a prototype — know its life, don't pretend otherwise.
>
> 2. **Pogo pins need their working stroke respected.** `[DATASHEET]`
>    Compress to ~70–80% of max travel. Less → intermittent contact. More → pin damage. Design the mating surface depth from the datasheet, not from feel.
>
> 3. **Magnets near the changer corrupt the encoders.** `[HYPOTHESIS]`
>    The QDD's AS5048 sits millimeters away across the wrist. Keep alignment magnets > 30 mm from any encoder, or use dowels instead. You hit the same class of problem on the haptic knob (2.7).
>
> 4. **Grip force is friction × linkage × motor torque.** `[HYPOTHESIS]`
>    Smooth plastic fingertips slip. Rubber pads are cheaper than a bigger motor. Measure, don't guess.
>
> 5. **The tool changer is a seam — write its interface contract.** `[HYPOTHESIS]`
>    Which pins carry power, which carry CAN, what happens if it's swapped mid-command. Use `templates/interface_contract.md`. Seams are where bugs live (you learned this in 1.5).
>

## Dependencies that waste your week if hit backwards

- 4.2 motion working BEFORE gripper testing — the arm must reach the pick pose.
- 4.3 E-stop proven BEFORE any gripper-under-load test.
- Bench-test pogo contact continuity BEFORE mounting the changer on the arm.
- Print and test the linkage standalone BEFORE integrating it with the arm.

> Log sessions in Daily/ notes using the unified template.

---

# Phase 4 Deload / Synthesis

- [ ] Explain the CAN packet structure from memory
- [ ] Derive 2-link IK on paper
- [ ] Write the feedforward torque equation from memory: τ_ff = M(q)q̈ + C(q, q̇)q̇ + g(q)
- [ ] Explain why minimum-jerk trajectories matter, physically
- [ ] Draw the E-Stop circuit from memory, including why the contactors are DC-rated and dual-channel
- [ ] State the safe state per axis from memory, including the gravity case
- [ ] List all HIL fault scenarios and expected firmware responses
- [ ] Run `scripts/versions.sh` and `scripts/cold_tools.sh`

## Phase 4 Retro

Actual time vs. range, 10–20 wk:
Most valuable landmine:
Missing landmine:
What Phase 5 needs from Phase 4:
