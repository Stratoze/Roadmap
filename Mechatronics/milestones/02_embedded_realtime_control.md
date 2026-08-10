# Phase 2 — Embedded Architecture & Real-Time Control

## Outcome

Move from "code that runs" to deterministic embedded control.
By the end: bring up STM32 at register level with GPIO, timers, SPI, UART, and hardware encoder decoding; create a deterministic timer-driven loop; simulate PID; attempt FOC from understanding; use FreeRTOS without destroying timing guarantees; model the coupled dynamics of the 2-DOF arm with state-space tools; implement a homing sequence with limit switches; and design state machines as a general firmware pattern.

This phase is about control over time, hardware, and failure.



### Real-Time Determinism: Hard vs. Soft
A critical distinction for this phase and everything after:

**Hard real-time:** missing a deadline is a system failure. The control loop must execute
within its period, every time, or the plant becomes unstable. Motor control at 1 kHz,
safety interlocks, encoder counting — these are hard real-time. A late correct answer is
worse than an early wrong one.

**Soft real-time:** missing a deadline degrades performance but doesn't cause failure.
Telemetry logging, parameter updates, display updates — these are soft real-time.

In this phase, the motor control timer ISR is hard real-time. Telemetry is soft. The
FreeRTOS milestone (2.4) is where this distinction becomes concrete: if a soft-real-time
task (UART printing) blocks the hard-real-time task (motor control), the motor oscillates
or crashes. The architecture must enforce this separation.

**Worst-Case Execution Time (WCET):** For hard-real-time tasks, you must know not just
the average execution time but the WORST case. If your control ISR takes 50 µs typically
but 200 µs when a cache miss and interrupt nesting align, and your period is 1 ms, you
have 800 µs of margin. But if the worst case is 1.1 ms, you have a deadline miss that
will happen rarely, unpredictably, and always at the worst moment. WCET analysis (static
or measurement-based) is how you prove your timing guarantees. For this phase: measure
your ISR execution time with a debug GPIO toggle + scope. Record the worst case over
10,000+ cycles. That number is your WCET estimate. If it exceeds 80% of the period, you
have a timing problem.

---

## Phase Pass Condition

### MVM

- [ ] Bare-metal STM32 blink without HAL
- [ ] 1 kHz timer interrupt verified on scope
- [ ] SPI device read at register level (encoder or ADC)
- [ ] UART telemetry with interrupt-driven RX
- [ ] Quadrature encoder read via timer encoder mode
- [ ] PID simulation: step response plots
- [ ] FOC attempted up to current sensing + transform logging
- [ ] FreeRTOS: 3 tasks without blocking control loop
- [ ] 2-DOF arm equations of motion derived and simulated
- [ ] Homing sequence: limit switch → debounce → state machine → zero
- [ ] Firmware has explicit modes/fault state: IDLE, RUN, FAULT, with watchdog and timeout behavior

### Full Pass

- [ ] Register-level project builds from command line
- [ ] Linker script and startup flow understood at "Applied" level
- [ ] 1 kHz jitter measured and documented
- [ ] Can explain SPI CPOL/CPHA modes and why mismatch gives garbage
- [ ] Can explain UART framing, baud rate, and why mismatch gives garbage
- [ ] Can explain timer encoder mode: hardware quadrature decoding, 4× resolution, overflow handling
- [ ] PID tuning guide from own experiments
- [ ] FOC current loop tracks Iq/Id on hardware
- [ ] Priority inversion created, captured, fixed
- [ ] Watchdog tested
- [ ] State-space model of 2-DOF arm: A, B, C, D matrices, simulated
- [ ] Natural frequencies of the arm identified from the model
- [ ] Homing: NC switch fails safe (wire break → trigger), debounce verified on scope
- [ ] State machine design: can draw state diagram, explain transitions, guards, entry/exit actions
- [ ] Can explain cascade control: current/torque → velocity → position, and why inner loop bandwidth must exceed outer loop bandwidth
- [ ] Can explain feedforward vs feedback: model-based torque/position feedforward reduces tracking error, feedback handles residual
- [ ] Can explain telemetry/parameter/calibration storage as firmware architecture: non-blocking telemetry, versioned config, calibration persistence
- [ ] Phase synthesis from memory

---

# Milestone 2.1 — Bare-Metal STM32 Foundation

> [!info] 📚 Resources — Bare-Metal STM32
> **Visual:** Controllers Tech / Quantum Leaps (STM32 from registers).
> **Interactive:** arm-none-eabi-gcc + CMake + OpenOCD + GDB; blink, then 1 kHz timer on a scope.
> **Theory:** STM32 Reference Manual + Datasheet. RCC → GPIO → TIM order.


## Deliverable

LED blinking via direct register writes, no HAL, compiled from command line, flashed via OpenOCD, with a 1 kHz timer interrupt verified on scope. SPI device read. UART telemetry. Quadrature encoder via timer encoder mode.

## Pass Condition

### MVM

- [ ] LED blinks via RCC + GPIO register writes
- [ ] Compiled and flashed from command line
- [ ] Can explain why RCC enable comes before GPIO config

### Full Pass

- [ ] Custom linker script works
- [ ] CMakeLists.txt builds from scratch
- [ ] OpenOCD flashes, GDB connects, breakpoint hits
- [ ] 1 kHz timer ISR toggles debug pin
- [ ] Scope confirms timing, jitter recorded
- [ ] Can explain: reset → main → ISR
- [ ] **SPI:** Read an SPI device (AS5048 encoder, MCP3008 ADC, or similar) at register level. Configure SPI peripheral: CPOL, CPHA, baud prescaler, chip select GPIO. Can explain: SPI Mode 0 (CPOL=0, CPHA=0) vs. Mode 3 (CPOL=1, CPHA=1). Clock idles low vs. high. Data sampled on rising vs. falling edge. Mismatch → every reading is garbage, no error flag.
- [ ] **SPI:** Can explain: SPI is full-duplex (MISO + MOSI simultaneous), master generates clock, each slave has a chip select. Faster than I2C (no address phase, no ACK), but more pins (SCK, MOSI, MISO, CS per slave). Daisy-chain possible but rare.
- [ ] **UART:** Interrupt-driven RX for telemetry. Configure baud rate, 8N1. Can explain: UART is asynchronous — no clock line. Both sides must agree on baud rate. Start bit → 8 data bits → optional parity → stop bit. Framing error = stop bit not high = baud mismatch or noise.
- [ ] **UART:** Can explain: baud rate mismatch gives consistent garbage (every byte wrong). Noise gives intermittent garbage. If you see 0x00 or 0xFF repeatedly, check baud rate first, then wiring, then ground.
- [ ] **Encoder via timer:** Configure a timer in encoder mode (STM32 TIMx_SMCR.SMS = encoder mode). Connect encoder A and B to timer CH1 and CH2. Read TIMx_CNT for position. Can explain: the timer hardware counts both edges of both channels → 4× resolution. No software interrupt needed for counting. The CPU only reads the count when it needs position. Can explain: 16-bit timer overflows at 65535 counts. For a 2000 CPR encoder (8000 counts/rev), that's ~8 revolutions before overflow. Handle overflow in software (track direction, add/subtract 65536) or use a 32-bit timer.
- [ ] **Encoder via timer:** Can explain: velocity = Δcount / Δt. Read the count at a fixed rate (e.g., every 1 ms in the control ISR). Divide by the time step and counts-per-revolution to get rad/s. Low-speed resolution is limited by the count granularity. High-speed is limited by the timer clock. Know both limits.

> [!warning] ⚠️ Landmines
> 1. **Datasheet ≠ reference manual.** `[COMMUNITY]`
>    Datasheet: pinout, electrical specs, memory sizes. Reference manual: peripheral registers. Timer behavior is in the reference manual, not the datasheet.
>
> 2. **Clock tree assumptions break timing.** `[COMMUNITY]`
>    Timer frequency ≠ the number on the board. PLL, prescalers, APB multipliers, default reset clock all matter. If 1 kHz is wrong, check the clock tree before touching code.
>
> 3. **Enable peripheral clock BEFORE configuring.** `[COMMUNITY]`
>    Write to RCC_AHBxENR before GPIO registers. Forget → GPIO writes go nowhere, LED stays dark. #1 "my STM32 does nothing" cause. Same for SPI (RCC_APB2ENR) and UART (RCC_APB1ENR or APB2 depending on instance). Same for timers (RCC_APB1ENR or APB2).
>
> 4. **Volatile matters.** `[COMMUNITY]`
>    Memory-mapped registers need volatile-qualified access. Otherwise the compiler optimizes away reality.
>
> 5. **The toolchain IS the milestone, not the LED.** `[HYPOTHESIS]`
>    arm-none-eabi-gcc + CMake + linker script + OpenOCD + GDB working together for the first time is where the 1–3 weeks goes.
>
> 6. **SPI mode mismatch is silent.** `[COMMUNITY]`
>    If CPOL/CPHA doesn't match the slave device, every reading is wrong. No error flag. No hard fault. Just garbage. Check the device datasheet's "SPI timing diagram" — it shows clock idle state and sampling edge. Match those exactly.
>
> 7. **UART baud rate is set by a divisor, not a direct number.** `[COMMUNITY]`
>    The baud rate register value depends on the peripheral clock frequency (APB1 or APB2). If the clock tree is wrong, the baud rate is wrong, and you get garbage. Verify the actual peripheral clock before computing the divisor.
>
> 8. **Chip select is a GPIO, not an SPI peripheral function.** `[HYPOTHESIS]`
>    In register-level SPI, YOU toggle the CS pin. Pull it low before the transfer, high after. If you forget, the slave never listens. If you leave it low, the bus is contested. Add a pull-up on CS for safety.
>
> 9. **Timer encoder mode uses specific pins.** `[COMMUNITY — STM32 Reference Manual]`
>    Not every timer pin supports encoder mode. Check the alternate function mapping in the datasheet. TIM2 CH1+CH2, TIM3 CH1+CH2, TIM4 CH1+CH2 are common. If you pick the wrong pins, the timer won't count. Also: encoder mode uses the timer's input capture hardware — you can't simultaneously use the same timer for PWM output.
>
> 10. **Encoder input needs filtering.** `[COMMUNITY]`
>     The STM32 timer has a digital input filter (TIMx_CCMR1.IC1F). Set it to filter out glitches shorter than a few timer clocks. Without it, electrical noise on the encoder lines causes false counts. The filter adds a few clocks of latency — negligible for position, but know it's there.
>

## Dependencies that waste your week if hit backwards

- Read the memory map, flash base, RAM base, peripheral bases, from the datasheet BEFORE writing the linker script. Wrong addresses → silent failure, no error.
- Get the blink working before the timer. Verify the toolchain end-to-end with the simplest possible program first.
- OpenOCD config must match BOTH your debug probe AND your chip. These are separate `.cfg` files.
- Get GPIO + timer working BEFORE adding SPI/UART/encoder. Each peripheral adds clock tree complexity. Verify one at a time.
- For SPI: read the slave device's timing diagram BEFORE configuring the SPI peripheral. CPOL/CPHA must match.
- For encoder: verify the encoder waveform on scope BEFORE configuring the timer. If the waveform is noisy or the wrong voltage level, the timer will miscount and you'll debug firmware instead of wiring.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 2.2 — PID Theory + Tuning in Simulation

> [!info] 📚 Resources — PID Theory & Tuning
> **Visual:** Brian Douglas / MATLAB Tech Talks PID series — the gold standard (P/I/D roles, windup).
> **Interactive:** Python PID sim — step response, Bode, tune Kp→Ki→Kd.
> **Theory:** Nise Ch 8–10; Åström & Murray for depth.


## Deliverable

Python PID simulation with step response plots, Bode plots, and a tuning guide in your own words.

## Pass Condition

### MVM

- [ ] Simulates a first-order or second-order plant
- [ ] P, PI, PID responses plotted separately
- [ ] Can explain P, I, D effects physically

### Full Pass

- [ ] Overshoot created and reduced intentionally
- [ ] Integral windup demonstrated and fixed
- [ ] Derivative noise amplification observed
- [ ] Bode plot: gain margin, phase margin identified
- [ ] Tuning guide written
- [ ] Cascade control simulated or explained: current/torque, velocity, position loops with bandwidth hierarchy
- [ ] Feedforward demonstrated: adding model-based feedforward reduces tracking error versus PID alone
- [ ] Trajectory shaping introduced: step command vs trapezoidal/S-curve command, with acceleration/jerk limits
- [ ] System identification attempted: estimate plant parameters from step/frequency response; document model uncertainty and the frequency range where the model is trusted.

> [!warning] ⚠️ Landmines
> 1. **PID is not magic gain seasoning.** `[COMMUNITY]`
>    P: reacts to present error. I: reacts to accumulated error. D: reacts to predicted future error. Each has a physical role.
>
> 2. **Integral windup is not a corner case.** `[COMMUNITY]`
>    Any actuator limit causes it. If the sim behaves well only with infinite authority, the sim is lying.
>
> 3. **Derivative on noisy measurement makes things worse.** `[COMMUNITY]`
>    D needs filtering or careful implementation. Differentiate the process variable, not the error, avoids derivative kick on steps.
>
> 4. **Discrete PID ≠ continuous PID pasted into code.** `[COMMUNITY]`
>    Sampling time matters. Implementation must match loop period.
>
> 5. **Cascade loops need bandwidth separation.** `[HYPOTHESIS]`
> The inner current/torque loop must be faster than the velocity loop, which must be faster than the position loop. If outer loops are faster than inner loops, they command what the inner loop cannot deliver, and the system oscillates or saturates.
>

## Dependencies that waste your week if hit backwards

- Understand the plant BEFORE tuning. Input = torque, output = angle. Even a crude model beats random gains.
- Add P first, then I, then D. Observe each effect in isolation before combining.
- Simulate the inner loop BEFORE the outer loop. If current/torque tracking is bad, velocity and position tuning will hide the problem.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 2.3 — FOC Closed-Loop on Hardware

> [!info] 📚 Resources — FOC Closed-Loop
> **Visual:** Ben Briny FOC series; SimpleFOC overview.
> **Interactive:** SimpleFOC as reference; scope the current loop.
> **Theory:** ST AN1086, TI SLUA171 (Clarke/Park, ADC-to-PWM sync, encoder offset).


## Deliverable

Field Oriented Control on real hardware, built in stages: open-loop spin → current sensing → Clarke/Park logging → Iq loop → Id loop.

The goal is not to "copy FOC." The goal is to understand what each transformation and timing constraint does.

## Pass Condition

### MVM

- [ ] Open-loop sinusoidal spin works
- [ ] Current sensing topology identified
- [ ] ADC samples at intentional PWM timing point
- [ ] Clarke/Park outputs logged
- [ ] Iq responds in expected direction
- [ ] Motor holds torque 10 sec against light hand load

### Full Pass

- [ ] Iq step: no sustained oscillation
- [ ] Id bounded near zero
- [ ] Cold start first attempt
- [ ] 5-min run, no drift or thermal shutdown
- [ ] Encoder alignment documented
- [ ] Analog front-end verified under switching: offset, noise, bandwidth, and ADC-to-PWM sync checked before blaming PID
- [ ] Current-loop bandwidth and phase margin measured or estimated; disturbance rejection tested by applying a load/current disturbance and observing recovery.
- [ ] Landmines updated from real experience

> [!warning] ⚠️ Landmines
> 0. **Current-sensing topology determines firmware architecture.** `[COMMUNITY — ST AN1086, TI SLUA171]`
>    Three-shunt, dual-shunt, single-shunt: each needs different ADC timing. Find it in your eval board schematic BEFORE writing firmware. Cap PWM duty at ~90%; ADC samples when PWM is low.
>
> 1. **Encoder electrical-angle offset must be calibrated.** `[COMMUNITY]`
>    Mechanical zero ≠ electrical zero. Park output oscillates at 2× electrical freq → rotor zero ≠ encoder zero. Alignment is Step 0. This was introduced in Milestone 1.3. If you skipped it, do it now. Everything downstream is garbage without it.
>
> 2. **ADC-to-PWM sync is not optional.** `[COMMUNITY — TI SLUA171]`
>    Sample at counter bottom, center-aligned. Wrong instant → noise that looks like bad tuning. Days wasted on a PID that's fine.
>
> 3. **Convention consistency.** `[COMMUNITY — ST AN1086]`
>    One Clarke/Park sign convention across ALL transforms. Mixed conventions "almost work" — worse than failing clearly.
>
> 4. **Deadtime is a hardware safety issue.** `[COMMUNITY]`
>    Too little → shoot-through → dead FETs. Verify on scope before motor.
>
> 5. **FOC can fail silently.** `[HYPOTHESIS]`
>    Bad current readings, wrong angle, sign mistakes → "weak torque" rather than obvious failure.
>
> 6. **The analog front end from 1.3 is now in the critical path.** `[HYPOTHESIS]`
>    If the current-sense amplifier has offset, the FOC loop sees a phantom current. If the anti-aliasing filter adds too much phase lag, the current loop bandwidth is reduced. If the amplifier bandwidth is too low, the current reading is attenuated at the PWM frequency. All of these look like "bad PID tuning" but are analog problems. Check the analog stage before tuning the digital loop.
>

## Dependencies that waste your week if hit backwards

- Identify sensing topology and set PWM duty limit BEFORE writing FOC code.
- Encoder alignment BEFORE closing any loop. Everything downstream is garbage without it.
- Log Clarke/Park outputs, no actuation, BEFORE closing the Iq loop. Verify signs and angle behavior manually.
- Close Iq BEFORE Id. Torque control first, flux decoupling second.
- **Verify the analog current-sense front end (from 1.3) is still working correctly BEFORE starting FOC.** Inject a known current (resistor + supply), verify the ADC reading matches. If it doesn't, fix the analog stage first.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 2.4 — FreeRTOS Multi-Task Firmware

> [!info] 📚 Resources — FreeRTOS Multi-Task
> **Visual:** Quantum Leaps RTOS course; FreeRTOS explainers.
> **Interactive:** FreeRTOS on your STM32 — 3 tasks, priority-inversion demo, watchdog.
> **Theory:** FreeRTOS manual; WCET measurement; hard vs soft real-time.


## Deliverable

FreeRTOS with separate tasks for motor control, sensor polling, and telemetry, preserving deterministic control timing.

## Pass Condition

### MVM

- [ ] FreeRTOS builds and runs on STM32
- [ ] 3 tasks: motor/control, sensor, telemetry
- [ ] Motor timing not blocked by UART printing
- [ ] Basic queue or mutex used correctly

### Full Pass

- [ ] Priority inversion intentionally created and captured
- [ ] Fixed with priority inheritance or design change
- [ ] Watchdog configured and tested
- [ ] Stack overflow detection tested
- [ ] HardFault path documented
- [ ] Mode/fault manager exists: IDLE, CAL, RUN, FAULT, with explicit transitions and recovery path
- [ ] Telemetry is buffered/low-priority and cannot block the control loop
- [ ] Calibration/parameters stored in non-volatile memory with versioning, or the plan for it is documented
- [ ] **WCET measurement:** control ISR worst-case execution time measured over 10,000+ cycles via debug GPIO + scope. Value documented. Compared to loop period. If WCET > 80% of period, documented why and what the mitigation is.
- [ ] Can explain: hard real-time vs. soft real-time. Which tasks in this firmware are
      hard? Which are soft? What happens if a soft task blocks a hard task?

> [!warning] ⚠️ Landmines
> 1. **RTOS does not make real-time automatic.** `[COMMUNITY]`
>    It gives scheduling tools. It does not protect bad architecture.
>
> 2. **Printing from a high-priority task destroys timing.** `[COMMUNITY]`
>    Telemetry belongs in a low-priority task or buffered queue.
>
> 3. **Mutexes can create priority inversion.** `[COMMUNITY]`
>    Low-priority task holding a resource blocks high-priority control.
>
> 4. **Stack sizes fail non-obviously.** `[COMMUNITY]`
>    Stack overflow appears as random HardFaults.
>
> 5. **Control loops belong in timer ISR or highest-priority context.** `[HYPOTHESIS]`
>    Don't let task scheduling introduce unacceptable jitter.
>
> 6. **No fault manager means random hangs.** `[HYPOTHESIS]`
> If tasks can enter undefined states, the system needs a mode/fault manager with timeouts, safe outputs, and recovery. Watchdog resets are not a design; they are the last resort.
>
> 7. **Average execution time lies.** `[HYPOTHESIS]`
>    Your control ISR takes 50 µs on average. But once every 5,000 cycles, a flash wait state + interrupt nesting + cache miss pushes it to 300 µs. If your period is 500 µs, you have 200 µs of margin that vanishes without warning. Measure the WORST case over thousands of cycles, not the average over ten. The scope doesn't lie. `printf` timing does.
>

## Dependencies that waste your week if hit backwards

- Start from the known-good bare-metal timer project. Don't rebuild the timer setup under RTOS from scratch.
- Get the heartbeat LED task working before adding motor control. Verify the scheduler works with the simplest task first.
- Move non-critical printing OUT of the control path before testing timing. Otherwise you'll debug UART latency instead of control.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 2.5 — Multi-DOF Dynamics + State-Space Control

> [!info] 📚 Resources — Multi-DOF Dynamics & State-Space
> **Visual:** 3Blue1Brown linear algebra; Brian Douglas state-space videos.
> **Interactive:** sympy for the 2-link Lagrangian, scipy to simulate, eigenvalues for natural freqs.
> **Theory:** Craig *Intro to Robotics* Ch 6–7; Lynch & Park for state-space.


## Deliverable

Derive the coupled equations of motion for the 2-DOF planar arm using Lagrangian mechanics. Simulate in Python. Build the state-space representation. Identify natural frequencies. Show why independent PID per joint is insufficient for coordinated motion.

This milestone connects Phase 0 statics and Phase 1 pendulum dynamics to the actual capstone mechanism. Without it, Phase 4 motion integration is "move joints to angles." With it, the arm moves like a robot.

## Pass Condition

### MVM

- [ ] Lagrangian derived for 2-link planar arm: T, V, L = T - V
- [ ] Equations of motion: M(q)q̈ + C(q, q̇)q̇ + g(q) = τ, written out
- [ ] Can explain: M is the inertia matrix, C is Coriolis/centripetal, g is gravity. Each has a physical meaning.
- [ ] Python simulation: arm responds to applied torques, trajectory plausible
- [ ] Can explain WHY joint 1 torque depends on joint 2 position: the inertia matrix is configuration-dependent

### Full Pass

- [ ] State-space form: ẋ = Ax + Bu, y = Cx + Du. A, B, C, D matrices written for linearized case
- [ ] Natural frequencies computed from eigenvalues of A. Can explain: these are the frequencies at which the arm wants to oscillate
- [ ] Can explain: if motor excitation hits a natural frequency → resonance → large oscillations → bad
- [ ] Controllability checked: can the inputs reach all states? (rank of controllability matrix)
- [ ] Simple LQR or pole-placement controller simulated: compare to independent PID. Show the difference in coordinated motion.
- [ ] Can explain: PID treats each joint independently. The arm is coupled. State-space sees the coupling.
- [ ] Feedforward torque computed from the dynamics model: τ_ff = M(q)q̈_desired + C(q, q̇)q̇ + g(q). Show that PID + feedforward tracks better than PID alone.

> [!warning] ⚠️ Landmines
> 1. **The Lagrangian is not "just energy."** `[HYPOTHESIS]`
>    T and V are straightforward. The Euler-Lagrange equation d/dt(∂L/∂q̇) - ∂L/∂q = τ is where the algebra gets dense. The Coriolis terms (C matrix) are the part most people get wrong. Derive slowly. Check dimensions at every step.
>
> 2. **The inertia matrix M(q) is NOT constant.** `[COMMUNITY]`
>    For a single rigid body, I is constant. For a multi-link arm, M depends on joint angles. This is why the dynamics are nonlinear and why "just tune the PID" breaks down for fast or coordinated motion.
>
> 3. **Linearization is valid only near an operating point.** `[HYPOTHESIS]`
>    State-space A, B, C, D are for the LINEARIZED system around a specific configuration. The arm at full extension has different dynamics than at 90° elbow. If you design a controller at one point, it may not work at another. This is why computed torque / feedback linearization exists.
>
> 4. **Natural frequencies are not academic.** `[COMMUNITY]`
>    If your control loop bandwidth approaches a structural natural frequency, you get resonance. The arm shakes. This is not a simulation artifact — it happens on real hardware. Know your frequencies BEFORE tuning high-bandwidth controllers.
>
> 5. **LQR weights are not magic either.** `[HYPOTHESIS]`
>    Q and R matrices encode "how much do I care about state error vs. control effort?" There's no formula. Start with Q = I, R = I, observe, adjust. The physical meaning: high Q on position error → aggressive tracking. High R → gentle, energy-efficient, slow.
>
> 6. **Don't skip the pendulum connection.** `[HYPOTHESIS]`
>    Milestone 1.4 was a single pendulum. This is two coupled pendulums on a moving base. The math is harder but the physics is the same: gravity restores, inertia resists, coupling transfers energy between modes. If the 2-DOF derivation feels alien, re-derive the single pendulum with Lagrangian first.
>

## Dependencies that waste your week if hit backwards

- Re-derive the single pendulum with Lagrangian mechanics BEFORE attempting the 2-link arm. If you can't do one link cleanly, two links will be impossible.
- Write out T and V completely BEFORE applying Euler-Lagrange. Most errors come from wrong kinetic energy (forgetting that link 2's velocity includes link 1's motion).
- Verify the Python sim against the Phase 1 pendulum data. Single-link case should match. If it doesn't, the derivation is wrong.
- Compute natural frequencies BEFORE designing the state-space controller. You need to know what you're controlling.

> Log sessions in Daily/ notes using the unified template.

---

# Milestone 2.6 — Limit Switches, Homing, and State Machine Design

> [!info] 📚 Resources — Limit Switches, Homing & State Machines
> **Visual:** CNC homing / debounce / state-machine videos.
> **Interactive:** wire an NC limit switch, scope the bounce, debounce in HW+SW.
> **Theory:** state-machine patterns (states/transitions/guards); NC-fails-safe reasoning.


## Deliverable

Homing sequence for one axis: NC limit switch → GPIO interrupt → hardware + software debounce → state machine (fast approach → slow approach → back off → zero). Hall effect sensor verified for BLDC commutation. State machine design practiced as a general firmware pattern.

Every CNC, 3D printer, and robot arm needs homing. Without it, the system doesn't know where it is. Without debounce, every interrupt fires six times. Without NC wiring, a broken wire means the limit switch never triggers and the axis crashes into the end of travel. This is not a polish task. It's a core embedded skill.

The homing sequence is also your first real state machine. The pattern — states, transitions, guards, actions — applies to everything: safety mode management, communication protocols, startup sequences, error recovery. Learn it here. Use it everywhere.

## Pass Condition

### MVM

- [ ] Limit switch triggers GPIO interrupt on falling edge
- [ ] Debounce: switch press produces exactly ONE interrupt, verified on scope
- [ ] Homing state machine: motor moves toward switch, stops on trigger
- [ ] Can explain: NC (normally closed) vs. NO (normally open). NC is safer: wire break → circuit opens → switch triggers → system stops. NO fails silently: wire break → circuit opens → switch never triggers → axis crashes.

### Full Pass

- [ ] **Full homing sequence:** fast approach → switch triggers → back off → slow approach → switch triggers → back off small distance → set position zero. Can explain why two passes: the first pass is fast (saves time), the second is slow (precision). The back-off distance ensures the switch is released before the slow approach.
- [ ] **Debounce verified on scope:** mechanical switch shows 5–50 µs of bouncing. Hardware RC filter (10kΩ + 100nF → ~1ms) cleans the edge. Software timer (ignore edges for 5–10ms after first trigger) catches the rest. Both together. Can explain: hardware debounce protects the interrupt from noise. Software debounce protects the state machine from multiple triggers.
- [ ] **Hall effect sensor:** verified for BLDC commutation (if using hall-sensored motor). Can explain: hall sensors give 6 states per electrical revolution, ~60° resolution. Enough for trapezoidal commutation. Not enough for FOC (need encoder or observer). Can explain: hall sensors are digital (open-drain or push-pull), need pull-ups, and are sensitive to magnetic orientation.
- [ ] **Interrupt priority:** limit switch interrupt is higher priority than telemetry but lower than motor control timer ISR. Can explain: if the limit switch ISR preempts the control loop, the loop jitters. If telemetry preempts the limit switch, the switch response is delayed. Priority order matters.
- [ ] **Failsafe test:** disconnect the limit switch wire during motion. NC → system stops (safe). NO → system does NOT stop (unsafe). Document which type you used and why.
- [ ] Every homing state has a timeout; timeout transitions to FAULT with a documented recovery path
- [ ] **State machine design as a general pattern:**
  - Can draw the homing state diagram: states as circles (IDLE, FAST_APPROACH, BACKOFF_1, SLOW_APPROACH, BACKOFF_2, DONE, FAULT), transitions as arrows, guards as labels on arrows ("switch triggered," "backoff distance reached"), entry actions as labels inside circles ("set speed = 100 RPM," "set speed = 10 RPM," "zero the encoder").
  - Can explain: a state machine is better than nested if/else because: (1) you can't enter an invalid state, (2) transitions are explicit and reviewable, (3) adding a new state doesn't require rewriting all the conditions, (4) the state diagram IS the documentation.
  - Can explain: entry actions (do something when entering a state), exit actions (do something when leaving), guards (conditions that must be true for a transition to fire). These three concepts cover 90% of firmware state management.
  - Can identify 3 other places in the firmware where a state machine applies: safety mode management (IDLE → ARMED → RUNNING → E_STOP → FAULT), communication protocol (LISTENING → RECEIVING → PROCESSING → RESPONDING), startup sequence (POWER_ON → SELF_TEST → CALIBRATE → READY).

> [!warning] ⚠️ Landmines
> 1. **NO switches fail silently. Use NC for safety.** `[COMMUNITY]`
>    A normally-open switch closes when pressed. If the wire breaks, the circuit is open — same as "not pressed." The system never knows the switch is disconnected. A normally-closed switch opens when pressed. If the wire breaks, the circuit is open — same as "pressed." The system stops. This is why every safety-critical limit (E-stop, end-of-travel) uses NC. The failure mode is safe.
>
> 2. **Mechanical switches bounce. Every time.** `[COMMUNITY]`
>    A "clean" switch press produces 5–50 µs of contact bouncing. The GPIO sees multiple edges. Without debounce, your homing state machine triggers 3–10 times per press. Hardware RC + software timer. Both. Not one.
>
> 3. **Interrupt latency is not zero.** `[HYPOTHESIS]`
>    From switch edge to ISR entry: GPIO clock sync (2–3 cycles), NVIC priority check, context save. At 168 MHz, this is ~100–200 ns. Negligible for homing. But if you're counting encoder pulses at high speed in an interrupt, it matters. Know your latency budget.
>
> 4. **Homing speed is a trade-off.** `[HYPOTHESIS]`
>    Fast approach saves time but overshoots the switch (the motor doesn't stop instantly). Slow approach is precise but takes forever. The two-pass homing sequence (fast → back off → slow) is the standard solution. The back-off distance must exceed the overshoot at fast speed.
>
> 5. **Pull-ups/pull-downs are not optional.** `[COMMUNITY]`
>    A floating GPIO input reads random values. Configure the internal pull-up (or external) on the limit switch input. Open-drain hall sensors REQUIRE an external pull-up (typically 4.7kΩ to 3.3V). Check the datasheet.
>
> 6. **Don't poll in the ISR.** `[HYPOTHESIS]`
>    The ISR should set a flag and return. The state machine runs in the main loop or a task. If the ISR does motor control, communication, or delays, it blocks everything else. Keep ISRs short: set flag, clear interrupt, return.
>
> 7. **State machines need a FAULT state.** `[HYPOTHESIS]`
>    If the homing sequence times out (switch never triggers), or the motor stalls, or the encoder stops counting — the state machine must transition to FAULT, not hang in FAST_APPROACH forever. Every state machine needs: a timeout on every state, a FAULT state, and a defined recovery path (reset, retry, or escalate to E-stop).
>

## Dependencies that waste your week if hit backwards

- Wire the switch and verify the GPIO interrupt BEFORE writing the homing state machine. If the interrupt doesn't fire, the state machine has nothing to respond to.
- Verify debounce on scope BEFORE trusting the state machine. If you see multiple triggers on the scope, the state machine will misbehave and you'll debug the wrong thing.
- Test the failsafe (wire disconnect) BEFORE relying on the limit switch for safety. If you wired NO instead of NC, you need to know NOW, not after the axis crashes.
- **Draw the state diagram on paper BEFORE coding.** If you can't draw it, you can't code it. The diagram is the design. The code is the implementation. Get the design right first.

> Log sessions in Daily/ notes using the unified template.

---

# Phase 2 Deload / Synthesis

No new inputs. Do not start CAD/PCB yet.

- [ ] Re-draw STM32 startup flow from memory
- [ ] Re-draw timer ISR timing
- [ ] Explain SPI CPOL/CPHA modes from memory
- [ ] Explain UART framing and baud rate from memory
- [ ] Explain timer encoder mode: how hardware quadrature decoding works, 4× resolution, overflow
- [ ] Explain PID terms aloud without notes
- [ ] Draw FOC signal chain: ADC → Clarke → Park → PI → inv Park → PWM
- [ ] List all FOC landmines from memory
- [ ] Write the 2-DOF equations of motion from memory: M(q)q̈ + C(q, q̇)q̇ + g(q) = τ
- [ ] Explain what the natural frequencies mean for controller design
- [ ] Draw the homing state machine from memory, with guards and entry actions
- [ ] Explain NC vs NO failsafe reasoning
- [ ] Name 3 other firmware state machines and sketch one
- [ ] Run largest integrated firmware cold
- [ ] Run `scripts/versions.sh` and `scripts/cold_tools.sh`
- [ ] Clean code naming, commit phase state

## Phase 2 Retro

Actual time vs. range, 11–24 wk:

What was easier than expected:

What was harder than expected:

Most valuable landmine:

Missing landmine:

What Phase 3 needs from Phase 2:
