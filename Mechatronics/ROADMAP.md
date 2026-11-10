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

## Project order (2026-11-11)

Mechatronics + AI, both project-based. Budget order: 3D printer and
tools first (they also print the SO-101 later), then the capstone parts.
Statics items come in when the build needs them. The AI track
(`AI/PROJECTS.md`) ends at imitation learning, which is what the SO-101
does: the two tracks meet at the arm.

## Projects (2026-11-11; each has its own goal and pulls in its theory)

Aim: StuffMadeHere-style building (learner): CAD, mechanisms,
electronics, embedded code, control, vision, fast iteration. Theory is
taught when a project question needs it, Veritasium style (`Prompts/`).

| # | Project | Its goal | Theory it pulls in |
|---|---|---|---|
| M1 | Capstone arm (below) | hand-moved 2-link arm knows its tip within 1 cm | trig, statics, circuits, measurement, CAD for printing |
| M2 | A joint holds itself | one motor holds an arm link at a set angle, resists a push | motors and gearing, feedback and PID, embedded C, filtering |
| M3 | SO-101 | printed, assembled, a learned policy does one task | dynamics, servos, LeRobot; meets the AI track |
| M4 | A StuffMadeHere-style machine | e.g. a vision-guided launcher that hits a moving target | mechanisms (gears, bearings, linkages), computer vision, control timing |
| M5 | Own robot joint | quasi-direct-drive BLDC joint, own driver PCB, CAN | motor control, PCB design (KiCad), power and thermal |

After M1-M5: the practical core of a mechatronics degree (build,
sense, actuate, control, learn), lighter on its pure theory
(thermodynamics, fluids, vibrations). Enough for a robot-learning lab;
a portfolio that shows it. M1 milestones are below; M2+ are keyed by
Opus when the project before is near done.

## M1 in simulation (no hardware yet, 2026-11-11)

Prompts: `bash Prompts/give.sh M1.1` (and so on). Statics items T11-T22
run alongside on the phone; M1.2 uses them.

- [ ] M1.1 Arm simulator: draw the arm, sliders, tip position (Python).
  Result:
- [ ] M1.2 Simulator shows gravity torque at each joint.
  Result:
- [ ] M1.3 Wokwi Arduino: knobs → angles → tip position.
  Result:
- [ ] M1.4 CAD the links in Onshape, ready to print.
  Result:

When hardware comes: print M1.4, wire M1.3 for real, check with a ruler.

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

What a lab will also look for (linear algebra, robot programming,
control, papers, a research plan) is in `PATH.md`; Opus keys it once the
target labs are chosen.

## Safety

USB/5V only, breadboard and jumper wires, hand tools and FDM printing.
No mains, no soldering, no power tools.

## After the capstone (parked; now M2-M5 above)

Long-term goal: a 2-joint arm with quasi-direct-drive motors (BLDC, own
driver board, motor control, CAN). Its topics wait here: materials,
manufacturing, mechanisms, power and thermal, sensors and filtering,
motors, embedded C, control. Pick the next project after the capstone,
ideally with a lab in Japan.

Other files in `Mechatronics/` (CURRENT, milestones, skills, goals, IDEAS,
scripts) are from the old system and unused.
