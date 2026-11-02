# Mechatronics map

A map only: the work and its keys are in `BACKLOG.md` (technical queue).
Rewritten 2026-11-02; the old 5-phase plan is in git history.

## Goal before Japan (~September 2027)

**Phase 0 capstone:** a passive 2-link arm with potentiometer joints. An
Arduino reads both angles and computes the tip position live (forward
kinematics); the learner checks it against a ruler. Proof goes in
`Mechatronics/portfolio/`: photo or video, code or hand calculation, and
three sentences (predicted, measured, why they differ). **Pass line:** the
tip is within ±1 cm of the FK prediction at three poses.

Hardware comes early: parts bought now and a crude cardboard arm built
before the theory ends, so the theory items serve a real build. Items the
passive arm does not need (FEM, power and thermal, materials and fatigue)
are parked in `BACKLOG.md` until after the capstone.

Small, finishable, and something to show a professor.

## Steps to the capstone

| # | Step | Status | Where |
|---|---|---|---|
| 1 | Frames + 2-link forward kinematics (radians) | ✅ | done 2026-09 |
| 2 | Calculus intuition: rate, area, Euler step | ✅ | photo of FK drawing still missing (learner task) |
| 3 | Statics: free-body diagrams, torque, equilibrium | 🔨 | T10-T28 |
| 4 | Measurement: repeat, mean, spread, predicted vs measured | ⬜ | S1-S4 |
| 5 | Circuits: Ohm's law, series/parallel, voltage divider, potentiometer | ⬜ | T29+ (not keyed yet) |
| 6 | Arduino: read a potentiometer, ADC count → angle, FK printed live | ⬜ | not keyed yet |
| 7 | Build: two links (cardboard or printed), potentiometers at the joints | ⬜ | not keyed yet |
| 8 | Capstone check against a ruler, portfolio page | ⬜ | not keyed yet |

CAD is needed only at step 7, and only if the links are printed.

## Safety

USB/5V only, breadboard and jumper wires, hand tools and FDM printing.
No mains, no soldering, no power tools.

## After the capstone (parked, not planned)

Long-term goal: a 2-joint arm with quasi-direct-drive motors (BLDC, own
driver board, motor control, CAN). Its topics wait here: materials,
manufacturing, mechanisms, power and thermal, sensors and filtering,
motors, embedded C, control. Pick the next project after the capstone,
ideally with a lab in Japan.

Other files in `Mechatronics/` (CURRENT, milestones, skills, goals, IDEAS,
scripts) are from the old system and unused.
