# Ideas

Future ideas live here so they do not hijack the current milestone.
This is not a backlog. Nothing here is a commitment.
Use one line. If an idea needs a full plan, it is probably not for this file yet.

---

## Core Portfolio Artifacts (The Masterpiece Paradigm)

These are NOT optional. They ARE the milestones. Each lives in its milestone file
with pass conditions, landmines, and dependencies.

- **Phase 0:** Parametric Mechanism Testbed + Metrology Kit (Milestones 0.9, 0.10)
- **Phase 1:** Hand-Wound Voice Coil Actuator + 3D-Printed Motor Test Rig (Milestone 1.7)
- **Phase 2:** Force-Feedback Haptic Knob + Inverted Pendulum Cart (Milestones 2.7, 2.8)
- **Phase 3:** Quasi-Direct Drive Actuator — CNC housing + Puck PCB + gearbox (Milestones 3.1–3.3)
- **Phase 4:** 2-DOF Arm + Safety PDU + Gripper + Tool Changer (Milestones 4.2–4.5)
- **Phase 5:** Exploded-View Pedestal + Bench Museum (Milestone 5.2)

## Maybe later

- **Triple pendulum (sim → hardware).** Nonlinear dynamics, chaos. Do the single (Phase 1) and inverted cart (Phase 2) first. Revisit after Phase 2.
- **Audio codec / sound tokenization.** FFT → quantize → reconstruct. Weekend DSP project, no hardware. Revisit during Phase 1 when FFT is fresh.
- **Microphone from scratch (dynamic or electret).** Reverse transducer. Pairs with the speaker build. Weekend project.
- **Solenoid / electromagnetic relay build.** Magnetic circuit → linear force. Pairs with the VCA from Phase 1.7. Weekend project after Phase 1.
- **Precision/clean-environment mechatronics.** Contamination control, ESD, vacuum thinking. Pairs with Phase 4.
- **Force/compliance control.** Impedance/admittance control, contact-rich tasks. The QDD's backdrivability makes this possible. Pairs with Phase 4.2.
- **Robust/adaptive control.** Loop-shaping, H-infinity intuition, gain scheduling. Revisit after Phase 2.5 and real arm tuning.
- **Advanced metrology and uncertainty.** GUM-style budgets, traceable calibration. Revisit during Phase 1/3.
- **Stress inoculation drills.** Timed debugging exercises. Pairs with Phase 5.
- **Cross-domain coupling exercises.** "How does MOSFET thermal drift affect current sense?" Pairs with Phase 2–3.
- **Cycloidal drive (resin-printed or CNC).** Only after the QDD works, and only if planetary backlash proves insufficient. Revisit end of Phase 3.
- **6-axis force/torque sensor.** Machined cross + strain gauges. Requires Phase 3 CNC + instrumentation knowledge. Revisit after Phase 3.
- **Welding / metal fabrication.** NOT in this roadmap. Requires a course, PPE, dedicated space. If ever: only after Phase 4, only with instruction.
- **Manual CNC / lathe / mill.** NOT in this roadmap. Use services (SendCutSend/Xometry) instead. If ever: makerspace course first, never solo.
- **Mains-powered anything.** Never in this roadmap. Bench supplies and purchased AC-DC bricks only.

---

## Revisit during 12-week review

Ask:
- Does this fit the current phase?
- Does it remove friction or improve evidence?
- Is it just novelty?
- What would I have to stop doing to make room?
- Does it feed the Physical Artifact Dependency Tree, or distract from it?
