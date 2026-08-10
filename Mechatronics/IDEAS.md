# Ideas

Future ideas live here so they do not hijack the current milestone.
This is not a backlog. Nothing here is a commitment.
Use one line. If an idea needs a full plan, it is probably not for this file yet.

---

## Maybe later

- **Self-balancing robot (single inverted pendulum on cart).** Teaches state-space control, observer design, real-time pressure. Start with single, not triple. Skills transfer. Could extend Phase 2.5 if the dynamics work goes well.
- **Triple pendulum (sim → hardware).** Nonlinear dynamics, chaos, Lyapunov exponents. The Hypothesis Loop confronting its own limits: your model WILL diverge from reality, and the rate is measurable. Ambitious. Do the single and double first. Revisit after Phase 2.
- **Audio codec / sound tokenization.** FFT → quantize frequency bins → reconstruct → measure error. Weekend version teaches 80% of DSP. Neural codec (SoundStream/EnCodec style) adds ML but the DSP lesson is already complete at the simple stage. Parallel laptop project, no hardware needed. Fills the frequency-domain gap in a motivating way. Revisit during Phase 1 when FFT is fresh.
- **Microphone from scratch (dynamic or electret).** Reverse transducer. Teaches reciprocity, sensitivity, impedance matching, noise floor. Pairs with the speaker build. Weekend project.
- **Solenoid / electromagnetic relay build.** Magnetic circuit → linear force. Inductance vs. position, force vs. air gap, contact bounce. Weekend project, pairs with Phase 0 circuits.
- **Precision/clean-environment mechatronics.** Contamination control, particulates, outgassing, ESD, material compatibility, bakeout/vacuum thinking. Relevant if targeting semiconductor equipment, optics, or ultra-clean motion. Pairs with Phase 4.
- **Force/compliance control.** Impedance/admittance control, torque sensing, contact-rich tasks. Pairs with Phase 4.2 if force sensing exists.
- **Robust/adaptive control.** Loop-shaping, H-infinity intuition, model uncertainty, gain scheduling. Revisit after Phase 2.5 and real arm tuning.
- **Advanced metrology and uncertainty.** GUM-style uncertainty budgets, traceable calibration, instrument uncertainty, low-level measurement. Revisit during Phase 1/3.
- **Stress inoculation drills.** Timed debugging exercises where a fault is introduced and you have 10 minutes to diagnose. Builds state-dependent recall. Pairs with Phase 5. Could also be used at phase gates as a "can you debug cold?" check.
- **Cross-domain coupling exercises.** Explicit prompts: "How does thermal drift from the MOSFET affect your current-sense reading?" or "How does belt compliance change your PID tuning?" Pairs with Phase 2–3. Forces the domains to talk to each other instead of living in silos.

---

## Revisit during 12-week review

Ask:

- Does this fit the current phase?
- Does it remove friction or improve evidence?
- Is it just novelty?
- What would I have to stop doing to make room?
