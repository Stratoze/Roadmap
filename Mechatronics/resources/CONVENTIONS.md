# Conventions

This file prevents seam bugs: unit mistakes, sign errors, coordinate confusion, naming drift, and messy evidence.
If a project needs a different convention, write it down in that project's README or interface contract.

---

## Units

Use SI unless a datasheet or tool forces otherwise.

| Quantity | Preferred unit |
| --- | --- |
| Length | m, mm for CAD dimensions |
| Mass | kg |
| Force | N |
| Torque | N·m |
| Angle in code/math | radians |
| Angle in human notes | degrees allowed, but label clearly |
| Angular velocity | rad/s |
| Voltage | V |
| Current | A |
| Resistance | Ω |
| Power | W |
| Temperature | °C |
| Frequency | Hz |
| Time | s, ms, µs |

Rules:

- Every numeric measurement gets a unit.
- Firmware interfaces state units in names or comments.
- Convert at the boundary, not randomly inside logic.

---

## Temporal horizon
When documenting a design decision, test, or FMEA entry, state the temporal horizon:
- **t=0:** instantaneous failure mode (shoot-through, short circuit, impact)
- **t=cycles:** fatigue, wear, connector mating cycles
- **t=hours:** creep, corrosion, thermal aging, electromigration
- **t=thermal cycles:** solder joint fatigue, coating delamination

Example:
## Coordinates and frames

Default for 2D arm work unless otherwise stated:

- World frame: +X right, +Y up.
- Joint angles: positive counterclockwise.
- θ1: shoulder angle from +X.
- θ2: elbow angle relative to link 1.
- Use `atan2(y, x)`, not `atan(y/x)`.
- Code uses radians.

If a sensor or motor uses a different frame, document the transform at the interface.

---

## Electrical conventions

- Voltage is measured across a component.
- Current flows through a component.
- Current measurement requires a series path or a known shunt/clamp method.
- Power-up defaults should be safe: drivers disabled, PWM off, current limit set.
- First power-on uses a current-limited supply.
- Motor phase order must be documented before tuning.

---

## Firmware naming

Prefer explicit units and direction:

```c
float angle_rad;
float velocity_rad_s;
float current_a;
uint32_t loop_period_us;
```

Avoid names like:

```c
float value;
float angle;   // degrees or radians?
float speed;   // linear or angular?
```

---

## File naming

Use dates for evidence and logs:

```txt
YYYY-MM-DD_short_description.ext
```

Examples:

```txt
2026-08-02_scope_back_emf_phase_ab.png
2026-08-02_imu_static_raw.csv
2026-08-02_pid_step_response.png
```

Use lowercase with underscores for generated or long-lived project files.

---

## Commit messages

Keep them boring and searchable.

Examples:

```txt
phase0: add LED resistor calculation
phase1: verify MPU6050 WHO_AM_I over I2C
phase1: capture raw IMU noise baseline
phase2: add 1 kHz timer ISR on STM32
phase3: update motor shield schematic after footprint review
```

Format:

```txt
scope: specific change
```

---

## Decision records

Write two lines when the choice is non-obvious:

```txt
DECISION: Chose star ground over ground pour.
WHY: High di/dt motor return would modulate ADC reference.
```

Use `templates/decision_record.md` only when the decision needs more detail.
