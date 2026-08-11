# Phase 1 — Signals, Actuators, Dynamics

## Outcome

Real sensors, real motors, real noise. The bridge between paper physics and hardware that misbehaves.

By the end: you've read a sensor at the register level, understood noise in the frequency domain, built an H-bridge from discrete parts with a proper analog current-sense front end, spun a BLDC with sinusoidal commutation and encoder feedback, driven a stepper with microstepping, fused gyro and accelerometer into a stable calibrated angle, compared a simulation to reality, **wound your own voice coil actuator, and built the 3D-printed test rig you will characterize motors on for the rest of the roadmap.**

This phase is where the analog world meets the digital one. Every sensor produces an analog signal. Every actuator is driven by analog power. The MCU sits in the middle, and the quality of everything downstream depends on the analog stages on both sides.

**Physical artifacts of this phase:**
1. Hand-Wound Voice Coil Actuator (Milestone 1.7)
2. 3D-Printed Motor Test Rig (Milestone 1.7)
3. IMU telemetry module on perfboard — your first soldered board (Milestone 1.1)
4. 3D-printed pendulum rig (Milestone 1.4)

**Fabrication & safety envelope (Phase 1):**
- 3D printing (PETG for flexures), through-hole soldering on perfboard.
- ≤ 24 V DC. Current-limited bench supply ALWAYS. No mains. No LiPo.
- First soldering: practice 5 joints on scrap before the real board. Iron in stand. Ventilation. Eye protection clipping leads.
- Spinning motors: secured before power. Nothing loose near the shaft.

### Modeling Language: Bond Graphs

Throughout this phase, you will encounter energy transduction across domains: electrical
energy becomes mechanical motion (motors), mechanical motion becomes electrical signals
(encoders, back-EMF), thermal energy limits electrical performance (MOSFET heating).
Bond graphs provide a unified graphical language for modeling this energy flow. Each
"bond" represents a power pair (effort × flow): voltage × current in electrical domains,
force × velocity in mechanical domains, pressure × flow rate in hydraulic domains. The
same graphical elements (source, storage, dissipation, transformation) apply across all
domains.

You don't need to master bond graph formalism in Phase 1. But adopt the HABIT: when you
encounter a transducer or energy conversion, ask: "What is the effort? What is the flow?
Where does the power go? What stores it? What dissipates it?" This is the bond graph
question, even if you never draw the graph. It prevents the component-catalog thinking
where a motor is "a thing that spins" instead of "an electromechanical energy transducer
with coupling coefficient Ke = Kt."

The speaker-as-microphone insight from your IDEAS.md is exactly this: same bond graph,
reversed causality. When you build the speaker in Phase 0 speed runs, you're building a
bond graph in physical form. The VCA in Milestone 1.7 is the same bond graph built to spec.

---

## Phase Pass Condition

### MVM
- [ ] Live IMU data in PlotJuggler
- [ ] Filtered vs. raw overlay visible
- [ ] FFT of IMU noise: can identify dominant frequency peaks
- [ ] H-bridge drives brushed DC motor: PWM speed + direction, no shoot-through
- [ ] Current sense analog front end wired: shunt → amplifier → ADC, waveform verified on scope
- [ ] Physical BLDC spinning with sinusoidal commutation, video
- [ ] Encoder read: quadrature or SPI, position and velocity computed
- [ ] Stepper driven with microstepping: full → half → 1/16, video
- [ ] Can explain I2C pull-ups, addressing, ACK/NACK, and common failure modes
- [ ] Can compare I2C, SPI, UART, and CAN at block level: speed, topology, noise, failure modes
- [ ] Can explain analog front-end basics: offset, gain, bandwidth, aliasing, and why scope verification matters
- [ ] Pendulum simulated in Python
- [ ] Physical pendulum drop logged, compared to sim
- [ ] IMU tilt angle from complementary filter, calibrated (offset removed)
- [ ] **Physical:** VCA assembled; force vs current measured; moves visibly under command
- [ ] **Physical:** motor test rig assembled; load cell calibrated with a known mass
- [ ] **Physical:** IMU module soldered on perfboard, labeled, photographed

### Full Pass
- [ ] Back-EMF measured, pole pairs verified, phase resistance documented
- [ ] Sim vs. real comparison with error margin
- [ ] IMU → complementary filter → motor in one integrated loop
- [ ] Can explain aliasing and why sample rate matters
- [ ] Can explain ADC resolution vs. ENOB, and why analog noise floor matters
- [ ] Can explain chopper drive and decay modes in stepper driver
- [ ] Can explain why H-bridge needs flyback diodes and deadtime
- [ ] Can explain current sense amplifier: gain, bandwidth, CMRR, offset
- [ ] Can explain encoder calibration: electrical offset, why it's needed for FOC
- [ ] Can explain I2C, SPI, UART, CAN, RS-485 tradeoffs: topology, speed, noise immunity, failure modes
- [ ] Can explain calibration as a recurring primitive: offset, scale, alignment, temperature drift
- [ ] Can explain braking/coast/freewheel behavior in motor drives
- [ ] **Physical:** VCA force constant (N/A) measured with uncertainty; compared to F = BILN prediction
- [ ] **Physical:** torque-speed curve of one motor measured on the rig, plotted
- [ ] Phase synthesis from memory

---

# Milestone 1.1 — I2C Sensor + Telemetry

> [!info] 📚 Resources — I2C Sensor + Telemetry
> **Visual:** any clear "I2C protocol explained" (start/address/ACK/stop).
> **Interactive:** Velxio (self-hosted, free) — wire MPU6050+ESP32, verify WHO_AM_I before hardware. Logic analyzer on SDA/SCL.
> **Theory:** MPU6050 register map/datasheet; I2C spec basics.

## Deliverable

ESP32 reading raw MPU6050 registers over I2C, streaming live in PlotJuggler. No library abstractions.

**Physical artifact:** by the end of this milestone the circuit transitions from breadboard to a **soldered perfboard** — your first soldered artifact. Label it "IMU Telemetry v1", date it, photograph it.

**First-soldering protocol:** practice 5 joints on scrap → inspect (shiny, concave = good; dull, ball-shaped = reflow it) → then solder the real board. Through-hole only. No SMD in this phase.

## Pass Condition

### MVM
- [ ] Raw register values change when you move the board
- [ ] Data visible in serial monitor
- [ ] **Physical:** circuit works on breadboard

### Full Pass
- [ ] Data in PlotJuggler, not serial monitor
- [ ] Multi-axis, real-time, labeled
- [ ] Can explain I2C: START, address, R/W, ACK, STOP
- [ ] Can explain I2C pull-up sizing, bus capacitance, address conflicts, clock stretching, and bus hang recovery
- [ ] Telemetry format is versioned and defined before firmware loop
- [ ] **ADC fundamentals:** Can explain: the MPU6050 has an internal 16-bit ADC. Resolution = full-scale range / 2^16. But resolution ≠ accuracy. ENOB (effective number of bits) is lower due to noise. Can explain: sampling rate must be > 2× the highest frequency of interest (Nyquist). Can explain: input impedance matters — a high-impedance source with a sample-and-hold capacitor gives wrong readings if the source can't charge the cap fast enough. These principles apply to EVERY ADC you'll use: the STM32's internal ADC, external SPI ADCs, the current-sense ADC in Phase 2.
- [ ] **Physical:** board soldered, inspected, labeled, photo in `docs/captures/`

> [!warning] ⚠️ Landmines
> 1. **MPU6050 address depends on AD0 pin.** `[COMMUNITY]`
>    AD0 low → 0x68, high → 0x69. Can't talk to it? Check this first. Then check pull-ups, 4.7kΩ on SDA/SCL.
>
> 2. **Must wake the MPU6050 from sleep.** `[COMMUNITY]`
>    Write 0x00 to PWR_MGMT_1, 0x6B, first. All-zeros = sleeping, not broken.
>
> 3. **WHO_AM_I is your sanity check.** `[COMMUNITY]`
>    Register 0x75 returns 0x68. If not, the bus is broken. Debug the bus, not the accelerometer.
>
> 4. **Raw values need scaling.** `[COMMUNITY — MPU6050 datasheet]`
>    16-bit output is a count. Divide by sensitivity, depends on configured full-scale range, to get m/s² or °/s.
>
> 5. **PlotJuggler needs structured output.** `[HYPOTHESIS]`
>    Define the CSV format BEFORE writing the firmware loop. Changing it later is annoying.
>
> 6. **ADC resolution is not ADC accuracy.** `[COMMUNITY]`
>    A 16-bit ADC with ±2g range gives 0.061 mg/LSB resolution. But if the noise floor is 5 LSB, your effective resolution is ~13 bits. The datasheet's "noise density" spec tells you the real story. Don't design to the resolution number. Design to the noise floor.
>
> 7. **Solder the perfboard AFTER the firmware works on breadboard.** `[HYPOTHESIS]`
>    If you solder first and the firmware has a bug, you'll debug wiring when the bug is logic. Breadboard → verify → solder. And perfboard has no ground plane: run a dedicated ground wire next to SDA/SCL or I2C will glitch.
>

## Dependencies that waste your week if hit backwards

- **Simulate in Velxio BEFORE hardware arrives.** Velxio (velxio.dev, self-hosted via Docker, free) emulates ESP32 + I2C peripherals with real CPU execution. Wire the MPU6050 in Velxio, write the register-read firmware, verify WHO_AM_I returns 0x68, confirm the data format. When the real board arrives, you're debugging wiring, not logic. This saves 2–3 days of "is it my code or my soldering?" Velxio does NOT support STM32 — it's for Phase 0–1 (Arduino, ESP32, RP2040) only.
- WHO_AM_I before anything else. If the bus doesn't work, nothing downstream works.
- Wake the device before reading. All-zeros ≠ broken sensor.
- Output format before firmware loop. PlotJuggler parsing is annoying to retrofit.
- Practice solder joints on scrap BEFORE the real board.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 1.2 — Noise, Filtering, and Frequency Domain

> [!info] 📚 Resources — Noise, FFT & Filtering
> **Visual:** 3Blue1Brown *But what is the Fourier Transform?* — mandatory before FFT code.
> **Interactive:** Falstad RC low-pass + square wave (this is what an EMA does in code). Plot your real IMU noise floor with scipy/Audacity FFT.
> **Theory:** Smith *DSP Guide* Ch 8–9 (free, better than Ulaby for this topic).

## Deliverable

EMA filter on raw IMU data, PlotJuggler overlay: raw vs. filtered. Then: FFT of the raw noise, identify dominant peaks, explain what's causing them. Design a targeted fix (notch, rate change, or physical isolation) based on what the FFT shows.

## Pass Condition

### MVM
- [ ] EMA in C on ESP32
- [ ] Raw and filtered visible simultaneously
- [ ] Filtered is visibly smoother
- [ ] Alpha tuned: understand lag vs. noise rejection tradeoff

### Full Pass
- [ ] Can explain α = 0.01 vs. α = 0.99 physically
- [ ] Second filter type attempted, SMA or discrete LPF
- [ ] FFT of raw IMU noise computed in Python, plotted
- [ ] Can identify: is the noise broadband? Periodic? At what frequency?
- [ ] Can explain Nyquist: sampling at Fs means you can only see frequencies below Fs/2. Above that, they alias — appear as false low-frequency content.
- [ ] Can explain: EMA is a first-order IIR lowpass. Its cutoff depends on alpha AND sample rate. Change one without the other → cutoff shifts.
- [ ] If a periodic peak is found: targeted response. Notch filter, sample rate change, or mechanical isolation. Documented.
- [ ] **Analog noise awareness:** Can explain: Johnson noise (thermal, proportional to √(R·T·B)), 1/f noise (dominant at low frequencies), and quantization noise (ADC step size / √12). Can explain: the FFT you just computed shows the COMBINED effect of all these sources plus any periodic interference. The filter you design is digital, but the noise is physical. Knowing the source tells you whether a digital filter is the right fix or whether you need to fix the analog side (shielding, grounding, filtering before the ADC).
- [ ] Can build a sensor error budget: offset, gain, noise, bandwidth, aliasing, quantization, temperature drift; can state what calibration fixes and what remains as uncertainty.

> [!warning] ⚠️ Landmines
> 1. **More filtering = more lag.** `[COMMUNITY]`
>    Can't eliminate noise without delaying the signal. For control, excessive lag reduces stability margins.
>
> 2. **Discrete EMA ≠ continuous RC.** `[COMMUNITY]`
>    Cutoff depends on alpha AND sample rate. Change sample rate without changing alpha → cutoff changes.
>
> 3. **Sensor noise is not always random.** `[HYPOTHESIS]`
>    Motor vibration, PWM switching, quantization. Some is periodic. Look at the raw signal before choosing the filter. An EMA on a 200 Hz vibration peak just attenuates it slightly. A notch at 200 Hz removes it.
>
> 4. **FFT without windowing leaks.** `[COMMUNITY]`
>    A raw FFT of a non-periodic-in-window signal smears energy across bins. Apply a Hanning or Hamming window before FFT. The difference is visible and matters for identifying peaks.
>
> 5. **Aliasing is invisible until it isn't.** `[COMMUNITY]`
>    If your IMU samples at 1 kHz and there's 800 Hz vibration, you see a false 200 Hz signal. No amount of filtering after sampling fixes this. Anti-aliasing happens BEFORE the ADC, or by sampling fast enough. The MPU6050 has an internal DLPF — know what it's set to.
>
> 6. **The FFT is a diagnostic, not a filter.** `[HYPOTHESIS]`
>    The FFT tells you WHAT the noise is. The filter design is a separate step. Don't jump to "add a lowpass" before knowing whether the noise is broadband (lowpass helps) or narrowband (notch is better) or aliased (sample rate is the fix).
>
> 7. **Digital filtering cannot fix an analog problem.** `[HYPOTHESIS]`
>    If the noise is coupling in through a shared ground path, or radiating from a motor cable, or aliasing because there's no anti-aliasing filter before the ADC — no amount of digital filtering fixes the root cause. The FFT tells you the frequency. The fix might be analog: better grounding, shielding, or an RC filter before the ADC.
>

## Dependencies that waste your week if hit backwards

- Observe the raw noise in PlotJuggler BEFORE writing the filter. You need to know what you're filtering: broadband? periodic? spikes?
- Verify α = 1, passthrough, and α → 0, frozen, as sanity checks before tuning the real value.
- Compute the FFT BEFORE designing the second filter. The FFT tells you what filter to design.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 1.3 — H-Bridge, BLDC Commutation + Characterization

> [!info] 📚 Resources — H-Bridge, BLDC & Characterization
> **Visual:** Ben Briny / Informed comment (BLDC commutation, H-bridge, FOC intro).
> **Interactive:** LTspice/Falstad H-bridge — watch flyback & dead-time before wiring. Scope the phase terminals for back-EMF.
> **Theory:** Hughes *Electric Motors & Drives* Ch 1–4; ST/TI gate-driver & current-sense app notes.

## Deliverable

**Stage 0:** Discrete H-bridge driving a brushed DC motor. PWM speed control, direction reversal, flyback protection. **Analog current-sense front end:** shunt resistor → current-sense amplifier → anti-aliasing filter → ADC. Verify the analog waveform on scope before trusting the digital reading.
**Stage 1:** Physical BLDC spinning with sinusoidal commutation (three half-bridges). **Encoder interfacing:** quadrature encoder via timer input capture OR SPI encoder (AS5048/MA730). Position and velocity computed. Encoder calibrated for electrical offset.
**Stage 2:** Back-EMF measured, pole pairs counted, phase resistance measured. Constants documented.

The H-bridge is the brick. A 3-phase BLDC inverter is three H-bridges with sinusoidal commutation. The analog front end is the eye. Without it, the MCU is blind to current. The encoder is the sense of position. Without it, FOC is open-loop. Build all three.

**Physical artifact note:** mount the H-bridge + driver on the 3D-printed test rig base from Milestone 1.7. Nothing dangles. This habit is what makes Phase 3's Puck look professional.

## Pass Condition

### MVM
- [ ] **H-bridge:** brushed DC motor spins forward and reverse via PWM
- [ ] **H-bridge:** flyback diodes present, no voltage spikes on scope when PWM switches off
- [ ] **H-bridge:** no shoot-through (both switches on same leg never on simultaneously)
- [ ] **Analog front end:** shunt resistor in series with motor, voltage across shunt amplified by current-sense amplifier (INA219, INA240, or discrete op-amp), output visible on scope
- [ ] **Analog front end:** anti-aliasing RC filter before ADC input (e.g., 1kΩ + 1nF → ~160 kHz cutoff), verified on scope
- [ ] **BLDC:** motor spins at low speed, video
- [ ] **BLDC:** back-EMF visible on scope when spun by hand
- [ ] **Encoder:** position read, changes when motor turns by hand
- [ ] Phase resistance measured

### Full Pass
- [ ] **H-bridge:** deadtime measured on scope, explained (why it exists, what happens without it)
- [ ] **H-bridge:** braking/coast/freewheel behavior explained: what the FETs/diodes do in each state, and what is safe for the supply/bus
- [ ] **H-bridge:** can explain: PWM duty → average voltage → speed. Flyback diode provides path for inductive current when switch opens. Without it → voltage spike → dead FET.
- [ ] **Analog front end:** Can explain: current-sense amplifier gain (e.g., INA219 gain = 320 V/V, so 100 mV across shunt → 3.2V output). Can explain: CMRR (common-mode rejection ratio) — why the amplifier rejects the high common-mode voltage on the shunt and amplifies only the differential voltage. Can explain: amplifier bandwidth must exceed PWM frequency, otherwise the current reading is attenuated and phase-shifted. Can explain: offset voltage — the amplifier outputs a small voltage even at zero current. Measure it. Subtract it. This is calibration.
- [ ] **Analog front end:** Can explain: the anti-aliasing filter is not optional. Without it, PWM switching noise (tens of MHz) aliases into the current measurement band. A simple RC lowpass with cutoff well below Fs/2 is the minimum. The filter adds phase lag — account for it in the control loop.
- [ ] **Encoder:** Can explain: incremental encoder outputs two square waves (A, B) 90° apart. Quadrature decoding counts both edges of both channels → 4× resolution. A 2000 CPR encoder gives 8000 counts/rev = 0.045° per count. Can explain: absolute encoder (AS5048 via SPI) gives a unique position per revolution, no homing needed. Incremental needs a reference (index pulse or homing switch).
- [ ] **Encoder:** Can explain: encoder calibration for FOC — the encoder's mechanical zero ≠ the motor's electrical zero. The offset must be measured: energize one phase pair, let the rotor settle, read the encoder. That's the electrical offset. Without it, Park transform uses the wrong angle → torque is in the wrong direction → motor vibrates instead of spinning.
- [ ] **BLDC:** pole pairs verified from back-EMF cycle count
- [ ] **BLDC:** Ke estimated from scope measurement
- [ ] LTspice 3-phase inverter simulation
- [ ] Current-sensing topology identified, for FOC
- [ ] All constants documented
- [ ] Can explain: a 3-phase inverter IS three half-bridges. Each phase leg is a half-bridge. The commutation sequence energizes them in sinusoidal order.

> [!warning] ⚠️ Landmines
> 1. **Shoot-through kills FETs instantly.** `[COMMUNITY]`
>    If both switches on the same half-bridge leg conduct simultaneously, you short the supply rail to ground. Deadtime prevents this. Even with software interlocks, hardware deadtime (gate driver or RC) is the safety net. Verify on scope BEFORE connecting the motor.
>
> 2. **Flyback diodes are not optional.** `[COMMUNITY]`
>    A motor is an inductor. When you switch off, the inductor maintains current. Without a flyback path, the voltage spikes to hundreds of volts. The FET's body diode can serve as flyback, but it's slow — external Schottky diodes are faster and safer. If you see voltage spikes > supply on the scope, your flyback path is inadequate.
>
> 3. **PWM frequency matters.** `[COMMUNITY]`
>    Too low (< 1 kHz) → audible whine. Too high (> 50 kHz) → switching losses dominate, FETs heat. 10–20 kHz is the sweet spot for small motors. The gate driver's rise/fall time limits the practical maximum.
>
> 4. **Current-sense amplifier bandwidth is not the same as the ADC sample rate.** `[COMMUNITY — Analog Devices AN-105]`
>    The amplifier has a gain-bandwidth product. At gain = 320, an INA219 has ~14 kHz bandwidth. If your PWM is 20 kHz, the amplifier can't track the current waveform — it outputs an averaged, phase-shifted version. For FOC at 20 kHz PWM, you need an amplifier with > 100 kHz bandwidth at your chosen gain (e.g., INA240: 400 kHz at gain 20). Check the gain-bandwidth product, not just the "bandwidth" spec.
>
> 5. **The shunt resistor value is a trade-off.** `[COMMUNITY]`
>    Larger shunt → larger voltage → better SNR. But larger shunt → more power dissipation (P = I²R) → more heat → more error (resistance changes with temperature). For 2A continuous: 100 mΩ gives 200 mV at 2A, 0.4W dissipation. That's reasonable. For 10A: 10 mΩ gives 100 mV at 10A, 1W dissipation. Use a 4-terminal (Kelvin) shunt for accuracy — the sense taps avoid the voltage drop in the current-carrying leads.
>
> 6. **Anti-aliasing filter phase lag affects the control loop.** `[HYPOTHESIS]`
>    An RC filter at 160 kHz cutoff adds ~0.1 µs of group delay at 1 kHz. Negligible. But a 10 kHz cutoff (for a slow ADC) adds ~16 µs. At a 1 kHz control loop, that's 1.6% of the period. It matters. Know your filter's phase response. Include it in your loop timing budget.
>
> 7. **Back-EMF: measure between two phase terminals, not phase-to-ground.** `[COMMUNITY]`
>    With motor spinning freely, each pair shows a sinusoid. Frequency × 1/pole_pairs = mechanical RPM.
>
> 8. **Pole pairs vs. poles.** `[COMMUNITY]`
>    14 poles = 7 pole pairs. One mechanical revolution = 7 electrical. Count electrical cycles per mechanical turn.
>
> 9. **Encoder resolution is not accuracy.** `[COMMUNITY]`
>    A 2000 CPR encoder gives 0.18° per count (4× decoding: 0.045°). But mechanical runout (shaft eccentricity), mounting misalignment, and electrical noise degrade actual accuracy to maybe 0.5–1°. For FOC, this is usually fine. For precision positioning, it's not. Calibrate, don't trust the datasheet.
>
> 10. **Encoder wiring is noise-sensitive.** `[COMMUNITY]`
>     Quadrature encoder signals are low-voltage digital (5V or 3.3V) at potentially high frequency. Long wires near motor cables pick up noise → false counts → position jumps. Use twisted pair or shielded cable. Keep encoder wires away from motor power wires. If using differential (RS-422) encoder outputs, use a differential receiver.
>
> 11. **Gate driver deadtime is not a software guess.** `[COMMUNITY]`
>     Too little → shoot-through → dead FETs. Too much → torque ripple. Read the gate driver datasheet.
>
> 12. **Start in simulation.** `[HYPOTHESIS]`
>     LTspice H-bridge first, then 3-phase inverter. Verify switching produces expected waveforms before touching hardware. Otherwise you can't tell if the problem is your circuit or your wiring.
>
> 13. **Current limiting during bring-up.** `[HYPOTHESIS]`
>     A commutation bug can cause shoot-through. Always current-limited supply. Set below stall current.
>

## Dependencies that waste your week if hit backwards

- Build and verify the H-bridge with a brushed DC motor BEFORE attempting BLDC. The H-bridge teaches PWM, flyback, shoot-through, and current sensing in the simplest possible context. BLDC adds commutation on top.
- **Wire and verify the analog current-sense front end on scope BEFORE connecting it to the ADC.** If the amplifier output is wrong (offset, clipping, oscillation), the ADC reading will be wrong and you'll debug the wrong thing. Scope first. ADC second.
- **Read the encoder on scope or logic analyzer BEFORE reading it in firmware.** Verify the quadrature waveform is clean (sharp edges, no ringing, correct phase relationship). If the waveform is noisy, fix the wiring before debugging the firmware.
- Simulate the H-bridge in LTspice before wiring hardware. Verify flyback behavior and deadtime in simulation.
- 6-step, trapezoidal, commutation before sinusoidal — simpler, verifies wiring.
- Characterize, back-EMF, resistance, pole pairs, with motor UNPOWERED. You cannot measure back-EMF while the driver is switching.
- **Calibrate the encoder electrical offset BEFORE attempting FOC.** Without it, the Park transform angle is wrong. The motor will vibrate, cog, or spin in the wrong direction. This is Step 0 of FOC, not a tuning step.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 1.4 — Pendulum Dynamics Model + Hardware Validation

> [!info] 📚 Resources — Pendulum Dynamics Model
> **Visual:** 3Blue1Brown differential-equations videos.
> **Interactive:** scipy.integrate.solve_ivp pendulum sim; compare to the real drop.
> **Theory:** Ulaby Ch 4–5, Nise Ch 2 & 7. Derive on paper before coding.

## Deliverable

Python simulation of a 1D simple or physical pendulum, `scipy.integrate.solve_ivp`, physical pendulum **on a designed 3D-printed rig**, IMU mounted, comparison plot with error analysis.

**Physical artifact: the pendulum rig.** Not a stick with tape. Design it:
- Pivot: printed bracket + 3 mm steel dowel pin or 608 bearing. Must swing freely 10+ oscillations.
- Arm: printed beam (PETG preferred), known length and mass — measured with calipers, not taken from CAD.
- IMU pocket at a known, measured distance from the pivot.
- Release hook: holds at known θ₀, releases with zero added velocity.

## Pass Condition

### MVM
- [ ] Python sim runs, plausible trajectory
- [ ] Physical pendulum built, dropped, IMU logged
- [ ] Both curves on same plot
- [ ] **Physical:** rig printed and assembled; pivot low-friction (verified by hand)

### Full Pass
- [ ] Error estimated and documented
- [ ] Dominant mismatch source identified: friction? initial conditions? sensor lag?
- [ ] Phase portrait, θ vs. θ̇, plotted
- [ ] **Physical:** arm moment of inertia taken from CAD mass properties, compared to value implied by the measured period; discrepancy documented

> [!warning] ⚠️ Landmines
> 1. **solve_ivp state vector order must match equations.** `[COMMUNITY]`
>    State [θ, θ̇], return [θ̇, θ̈]. Wrong order → garbage, no error.
>
> 2. **Physical pendulum has friction; sim doesn't.** `[HYPOTHESIS]`
>    Real falls slower. Expected. The interesting question: how much slower?
>
> 3. **IMU drift makes long integration unreliable.** `[COMMUNITY]`
>    Gyro integration accumulates error. Short drop test: acceptable. Longer: need complementary or Kalman filter. This is addressed in Milestone 1.5.
>
> 4. **Initial conditions must match.** `[HYPOTHESIS]`
>    Sim starts at θ = 0, physical drop must too. Mismatched ICs explain most "curves don't match" problems.
>
> 5. **The pivot IS the experiment.** `[HYPOTHESIS]`
>    If the pivot has friction, decay is faster than the sim. If it wobbles, the IMU reads garbage. A printed hole with 0.1 mm clearance on a smooth pin, or a bearing, is the minimum. Test by hand first.
>
> 6. **Weigh the arm. Don't trust CAD mass.** `[HYPOTHESIS]`
>    Print infill varies. Measure mass and length physically (Milestone 0.10 skills), put the measured values in the sim. The sim-vs-real comparison only means something if the inputs are real.
>

## Dependencies that waste your week if hit backwards

- Derive equations of motion on paper BEFORE coding. For a simple pendulum with θ from downward vertical: θ̈ = -(g/L)sin(θ). Predict the trajectory shape. Then code and compare.
- Match initial conditions between sim and hardware before comparing curves.
- Print and verify the rig BEFORE running experiments. Bad pivot = garbage data = wrong conclusions about your model.
- Measure mass/length with calipers BEFORE setting sim parameters.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 1.5 — Phase 1 Integration + Sensor Fusion + Calibration

> [!info] 📚 Resources — Integration, Sensor Fusion & Calibration
> **Visual:** complementary/Madgwick filter explainers.
> **Interactive:** PlotJuggler — fuse gyro+accel, watch drift disappear; calibrate 6 orientations.
> **Theory:** calibration (offset/gain); complementary-filter math.

## Deliverable

Single loop on ESP32: IMU → calibration → complementary filter → motor response. Motor responds to orientation changes in real time. The tilt angle comes from fusing gyro and accelerometer, not from raw gyro integration. The IMU is calibrated: offset removed, scale factor verified.

## Pass Condition

### MVM
- [ ] One loop: read IMU, filter, command motor, repeat
- [ ] Motor visibly responds to tilt
- [ ] No crashes for 60 seconds

### Full Pass
- [ ] **IMU calibrated:** offset measured in 6 static orientations (±X, ±Y, ±Z up). For each axis: offset = mean of readings when that axis is aligned with gravity. Scale factor verified: when +Z is up, az should read +1g (±0.05g after calibration). Can explain: offset is the zero-input output. Gain/scale error is the deviation from ideal sensitivity. Linearity is how well the response follows a straight line across the range. Hysteresis is whether the reading depends on the direction you approached from. Temperature drift is how all of these change with temperature.
- [ ] **Can explain why calibration is not optional:** a 2° offset in the accelerometer means a 2° steady-state error in the complementary filter. The filter can't correct what it doesn't know is wrong. Calibration removes the systematic error. The filter handles the random noise. Both are needed.
- [ ] **Complementary filter implemented:** angle = α × (angle + gyro × dt) + (1-α) × accel_angle. Can explain: gyro is accurate short-term but drifts (integrate → unbounded error). Accelerometer is noisy but bounded (atan2 of gravity components). Complementary filter: high-pass gyro + low-pass accel. α ≈ 0.98 for ~1s time constant.
- [ ] **Can explain why neither sensor alone works:** gyro-only drifts within seconds. Accel-only is garbage during motion (measures all acceleration, not just gravity). Fusion is not optional for any real system.
- [ ] **Filter output vs. raw gyro vs. raw accel plotted on same timeline.** The improvement is visible.
- [ ] Loop timing consistent, verify with GPIO toggle + scope
- [ ] PlotJuggler: fused angle + motor command on same timeline
- [ ] Repeatable demo, video

> [!warning] ⚠️ Landmines
> 1. **Integration reveals timing problems invisible in isolation.** `[HYPOTHESIS]`
>    IMU read might block motor update. UART print might cause jitter. Measure actual loop time.
>
> 2. **The seam is where bugs live.** `[HYPOTHESIS]`
>    Filtered angle, float, what units? → motor command, int? PWM count? Unit mismatches and sign errors at interfaces cause "almost works."
>
> 3. **PlotJuggler at high rate can starve the loop.** `[HYPOTHESIS]`
>    Printing every iteration at 1 kHz → UART overhead dominates. Print every 10th iteration or use non-blocking buffer.
>
> 4. **Complementary filter α is not arbitrary.** `[COMMUNITY]`
>    α = 0.98 means the gyro dominates for ~1 second, then the accel corrects drift. Too high (0.999) → drift correction is too slow. Too low (0.9) → accel noise leaks through. The right value depends on your loop rate and how noisy your accel is. Tune it, don't copy it.
>
> 5. **Accel angle is only valid when stationary or slow.** `[HYPOTHESIS]`
>    atan2(ay, az) gives tilt ONLY when the only acceleration is gravity. During fast motion, the accelerometer measures motion + gravity, and the "angle" is wrong. This is why the complementary filter trusts the gyro during motion and the accel during quasi-static periods. For aggressive motion, you need a Kalman filter (parked in IDEAS.md).
>
> 6. **Calibration before fusion, not after.** `[HYPOTHESIS]`
>    If you fuse uncalibrated sensors, the filter converges to the wrong angle. Calibrate first (static, 6 orientations), then fuse. The calibration removes systematic error. The filter removes random noise. They solve different problems.
>
> 7. **Calibration is not "do it once and forget."** `[COMMUNITY]`
>    Temperature changes offset and gain. Mechanical shock changes offset. If the arm is going from a 20°C lab to a 40°C enclosure, the calibration drifts. For high-accuracy work: temperature-compensated calibration, or periodic re-calibration. For this project: calibrate once at room temperature, document the residual error, and note it as a known limitation.
>

## Dependencies that waste your week if hit backwards

- Verify both subsystems still work independently before integrating, regression check.
- Define the interface explicitly: what type, what units, what range does the filter output? What does the motor driver expect?
- **Calibrate the IMU BEFORE implementing the complementary filter.** If the filter output has a steady-state offset, you need to know: is it the filter, or is it the sensor? Calibrate first. Then any residual error is the filter's, not the sensor's.
- Implement the complementary filter BEFORE connecting the motor. Verify the angle estimate against a known tilt (protractor) first.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 1.6 — Stepper Motor + Microstepping Driver

> [!info] 📚 Resources — Stepper + Microstepping
> **Visual:** stepper-drive / microstepping / chopper-drive explainers.
> **Interactive:** TMC2209 — set current limit, sweep microsteps, listen for resonance.
> **Theory:** TMC2209 datasheet; stepper torque-speed fundamentals.

## Deliverable

NEMA17 stepper driven by a microstepping driver (A4988, DRV8825, or TMC2209). Full-step → half-step → 1/16 microstep. Step accuracy measured. Resonance observed. Torque-speed behavior compared to BLDC.

Steppers are the other half of the actuator world. BLDC for continuous rotation and high speed. Steppers for open-loop positioning, holding torque, and simplicity. Every 3D printer, CNC router, and positioning stage uses them. A mechatronics engineer who's only driven BLDCs is missing half the vocabulary.

## Pass Condition

### MVM
- [ ] Stepper spins: full-step, half-step, 1/16 microstep
- [ ] Direction reversal works
- [ ] Can explain: step pulse + direction pin. Each pulse = one step (or microstep). No feedback needed for open-loop.
- [ ] Current limit set on driver (potentiometer or register), verified with multimeter

### Full Pass
- [ ] **Chopper drive explained:** the driver regulates coil current by rapidly switching the H-bridge (chopping). When current exceeds the set limit, it turns off (or reverses) until current drops. This is why stepper drivers need a supply voltage well above the motor's rated voltage — the chopper uses the excess voltage to force current through the coil inductance quickly.
- [ ] **Decay modes explained:** slow decay (recirculate current through low-side FETs) vs. fast decay (reverse voltage across coil). Slow → smoother but slower current change. Fast → quicker current change but more ripple. Mixed decay → compromise. TMC drivers auto-tune this.
- [ ] **Microstep accuracy measured:** command 200 full steps (one revolution), measure actual angle. Command 3200 microsteps (1/16 × 200), measure actual angle. Microstepping improves smoothness but NOT absolute accuracy — the rotor doesn't land exactly on the microstep position under load.
- [ ] **Resonance observed:** sweep speed slowly. At certain speeds (typically 100–300 RPM for NEMA17), the motor vibrates loudly and may stall. This is the rotor's natural frequency being excited by the step pulses. Microstepping reduces resonance amplitude. TMC drivers with StealthChop nearly eliminate it.
- [ ] **Torque-speed comparison:** steppers have high holding torque at zero speed but torque drops rapidly with speed (back-EMF limits current through coil inductance). BLDC maintains torque to higher speed. Can sketch both curves and explain why.
- [ ] Can explain: open-loop steppers lose steps if torque demand exceeds holding torque. No error is reported. This is why high-reliability systems use closed-loop steppers (encoder feedback) or servos (BLDC + encoder).
- [ ] Can explain when to use closed-loop stepper vs servo: stall detection, encoder feedback, torque margin, and reliability requirements

> [!warning] ⚠️ Landmines
> 1. **Current limit is the first thing to set.** `[COMMUNITY]`
>    Before connecting the motor, set the driver's current limit (potentiometer on A4988/DRV8825, register on TMC2209). Too high → motor and driver overheat. Too low → missed steps. Measure the reference voltage with a multimeter. The formula is in the driver datasheet (e.g., A4988: Vref = I_limit × 8 × R_sense).
>
> 2. **Supply voltage ≠ motor rated voltage.** `[COMMUNITY]`
>    A "12V stepper" does not mean you supply 12V. The motor's rated voltage is the DC voltage that produces rated current through the coil resistance. The chopper driver needs a HIGHER supply (24–48V typical) to force current through the inductance quickly. If you supply only 12V, the current rises slowly → torque drops at speed → poor performance.
>
> 3. **Microstepping is not free precision.** `[COMMUNITY]`
>    1/16 microstep divides each full step into 16 microsteps. This makes motion smoother and quieter. But the rotor's actual position under load lags the commanded microstep. Microstepping improves smoothness and reduces resonance. It does NOT improve absolute positioning accuracy. For that, you need an encoder.
>
> 4. **Resonance can stall the motor.** `[COMMUNITY]`
>    At certain step rates, the step frequency matches the rotor's mechanical natural frequency. The rotor oscillates instead of stepping. It may stall completely. Accelerate THROUGH the resonance zone quickly. Microstepping and StealthChop (TMC) reduce the excitation. Mechanical damping (rubber mounts) helps.
>
> 5. **Wiring order matters but is recoverable.** `[HYPOTHESIS]`
>    If the motor vibrates but doesn't turn, one coil pair is likely swapped. Swap one pair (A+/A- or B+/B-) and retry. Unlike BLDC, there's no commutation sequence to get wrong — just two coil pairs.
>
> 6. **Enable pin is active-low on most drivers.** `[COMMUNITY]`
>    A4988/DRV8825/TMC2209: ENABLE pin must be LOW to enable the driver. Floating or HIGH → driver disabled → motor free-spins. Connect ENABLE to GND or a GPIO. Don't leave it floating.
>

## Dependencies that waste your week if hit backwards

- Set the current limit BEFORE connecting the motor. Power the driver with the motor disconnected. Measure Vref. Adjust. Then connect.
- Full-step BEFORE microstepping. Verify basic motion and direction first. Then increase microstep resolution.
- Observe resonance BEFORE trying to eliminate it. You need to know it exists and what it sounds/feels like. Then microstepping or StealthChop is the fix.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 1.7 — Voice Coil Actuator + Motor Test Rig

> [!info] 📚 Resources — VCA & Motor Characterization
> **Visual:** Ben Briny FOC series (Lorentz force context); any "how a voice coil works" video.
> **Interactive:** wind the coil, measure resistance, plot F vs I in Python.
> **Theory:** Lorentz force F = B·I·L·N; Hooke's law for the flexure; H-bridge drive (from 1.3); Ohm/KVL (from 0.5).
> **Fabrication:** 3D print (PETG for the flexure), hand-wound magnet wire, purchased N42 ring magnet, purchased S-beam load cell. NO metal cutting.

## Deliverable

**Artifact 1 — Hand-Wound Voice Coil Actuator:**
- Coil: 30–50 turns of 28–32 AWG magnet wire on a printed former
- Magnet: N42 neodymium ring magnet
- Flexure: printed leaf spring (PETG), constrains motion to one axis, provides centering force
- Housing: printed frame holding magnet, guiding the coil, mounting to the rig
- Drive: the H-bridge from 1.3, PWM force control

**Artifact 2 — 3D-Printed Motor Test Rig (dynamometer frame):**
- Printed baseplate + risers, motor mount, lever arm
- S-beam load cell (5 kg) + HX711: measures tangential force at a measured radius → torque = F × r
- Speed: hand-spin for back-EMF, or the motor's own encoder
- This rig is REUSED in Phase 3 to characterize the QDD actuator. Build it flat and modular.

## Pass Condition

### MVM
- [ ] Coil wound (30+ turns), resistance measured, no shorted turns
- [ ] Coil moves under current; reverses with polarity
- [ ] Rig assembled; load cell reads zero unloaded and correct under a known mass
- [ ] Lever arm radius measured with calipers (Milestone 0.10 method)

### Full Pass
- [ ] Force vs. current curve: 5+ points, plotted with units
- [ ] Force constant (N/A) from slope, compared to F = BILN prediction; gap explained
- [ ] Flexure spring rate measured: known displacement → restoring force
- [ ] Load cell calibration documented: known mass → counts → Newtons, with uncertainty
- [ ] Torque constant Kt measured for at least one motor on the rig
- [ ] Back-EMF constant Ke measured by hand-spinning and measuring open-circuit voltage
- [ ] Torque-speed curve plotted (5+ points, no-load toward stall)
- [ ] Stall tests kept under 2 seconds, current-limited supply
- [ ] Both artifacts mounted, labeled, photographed; data in `data/processed/`

> [!warning] ⚠️ Landmines
> 1. **Magnet-wire insulation is invisible.** `[COMMUNITY]`
>    Nick the enamel while winding → shorted turn → local hot spot → dead coil. Wind slowly with a cloth between fingers and wire. Measure resistance after; lower than expected = shorted turns.
>
> 2. **Print the flexure in PETG, layers along the length.** `[HYPOTHESIS]`
>    PLA creeps within hours. Layers must run along the spring's length, not across its thickness, or it cracks at 20 cycles. Bench-test the flexure alone for 100 cycles before assembling.
>
> 3. **Neodymium magnets are brittle and pinch.** `[COMMUNITY]`
>    They shatter on impact and snap together with real force. Eye protection near steel tools. Keep away from electronics until mounted.
>
> 4. **An uncalibrated load cell produces confident garbage.** `[HYPOTHESIS]`
>    HX711 outputs raw counts. Calibrate with a mass you weighed on a kitchen scale. Record the calibration in the same file as every measurement it produces.
>
> 5. **Lever-arm uncertainty dominates torque uncertainty.** `[HYPOTHESIS]`
>    τ = F × r. At r = 50 mm, ±1 mm is ±2% torque error. Measure r with calipers, record it with the data.
>
> 6. **Printed motor mounts flex.** `[HYPOTHESIS]`
>    A flexing mount eats torque the load cell never sees. PETG, 4+ walls, high infill. If it visibly flexes by hand, it's too weak.
>
> 7. **Stall heats as I²R.** `[COMMUNITY]`
>    Stall current is 5–10× running current. Two seconds max per reading, current limit on, then release. This is why the torque-speed curve is taken point-by-point, not held.
>

## Dependencies that waste your week if hit backwards

- **Complete 1.3 (H-bridge) FIRST** — the VCA needs bidirectional drive.
- **Complete 0.10 (metrology) FIRST** — the rig's lever arm and calibration inherit it.
- Wind the coil BEFORE designing the housing; the coil OD sets the magnet bore.
- Calibrate the load cell BEFORE any motor measurement.
- Test the flexure alone BEFORE assembling the VCA.

> Log sessions in Daily/ notes using the unified template.

---

# Phase 1 Deload / Synthesis

No new inputs.
- [ ] Re-explain IMU-to-motor signal chain from memory, including the analog front end
- [ ] Re-derive EMA transfer function
- [ ] Explain complementary filter equation from memory: angle = α(angle + gyro·dt) + (1-α)·accel_angle
- [ ] Explain IMU calibration procedure from memory: 6 orientations, offset, scale factor
- [ ] Explain back-EMF, pole pairs, Kv without notes
- [ ] Explain H-bridge flyback and shoot-through from memory
- [ ] Explain current-sense amplifier: gain, bandwidth, CMRR, offset, anti-aliasing filter
- [ ] Explain encoder types: incremental vs absolute, quadrature decoding, electrical offset calibration
- [ ] Explain chopper drive and decay modes from memory
- [ ] Explain what the FFT showed about your IMU noise, from memory
- [ ] Explain the VCA's bond graph from memory: effort, flow, storage, dissipation
- [ ] State the measured VCA force constant and one motor's Kt from memory, with units
- [ ] Clean ESP32 firmware: consistent naming, remove debug prints
- [ ] Commit clean state
- [ ] **Physical:** all Phase 1 artifacts photographed, labeled, stored in `docs/captures/`
- [ ] Run `scripts/cold_tools.sh`

## Phase 1 Retro

Actual time vs. range, 12–20 wk:
Most surprising result from hardware vs. simulation:
What I'd tell someone starting Phase 1:
Missing landmine:
