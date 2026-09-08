# Skill registry

| Skill ID | Name | Evidence tag | Goal era | Project | Requires |
|---|---|---|---|---|---|
| lab-toolchain-verify | Toolchain verify + first commit | qdd-arm-m0.1-mvm | qdd-arm (2026-08-) | 0.1 Toolchain |  |
| lab-functional-decomp | Functional decomposition + binary-search debug + Fermi | qdd-arm-m0.1-mvm | qdd-arm (2026-08-) | 0.1 Toolchain |  |
| lab-bench-discipline | DMM/scope awareness + bench commit habit | qdd-arm-m0.1-mvm | qdd-arm (2026-08-) | 0.1 Toolchain |  |
| mech-planar-fk | 2-link planar forward kinematics + frames + vector diagram | qdd-arm-m0.2-mvm | qdd-arm (2026-08-) | 0.2 Vectors + Trig | lab-functional-decomp |
| sw-py-forward-kinematics | 2-link arm tip plot in Python (radians, atan2 discipline) | qdd-arm-m0.2-mvm | qdd-arm (2026-08-) | 0.2 Vectors + Trig | lab-toolchain-verify |
| sw-py-calculus-integrate | Polynomial differentiate/integrate + pos-vel-acc chain + power-to-energy | qdd-arm-m0.3-mvm | qdd-arm (2026-08-) | 0.3 Calculus Intuition | sw-py-forward-kinematics |
| mech-statics-fbd | FBD + equilibrium + shoulder holding torque with units | qdd-arm-m0.4-mvm | qdd-arm (2026-08-) | 0.4 Statics + FBDs | mech-planar-fk |
| mech-fem-intuition | FEM pipeline intuition (mesh/BCs, hand-calc-validates-FEA) | qdd-arm-m0.4-mvm | qdd-arm (2026-08-) | 0.4 Statics + FBDs | mech-statics-fbd |
| ee-circuits-kvl-ohm | LED resistor sizing via KVL + Ohm, sim matches calc, hardware-verified | qdd-arm-m0.5-mvm | qdd-arm (2026-08-) | 0.5 Circuits Basics | lab-bench-discipline |
| ee-datasheet-measure-discipline | KCL/KVL loops + datasheet Vf/If + DMM/scope measurement discipline | qdd-arm-m0.5-mvm | qdd-arm (2026-08-) | 0.5 Circuits Basics | ee-circuits-kvl-ohm |
| ee-power-budget | P=VI + I2R loss + efficiency + thermal resistance + system power budget | qdd-arm-m0.6-mvm | qdd-arm (2026-08-) | 0.6 Power + Thermal | ee-circuits-kvl-ohm |
| mech-material-select | Allowable stress/FoS + Ashby link selection + fatigue/cyclic reasoning | qdd-arm-m0.7-mvm | qdd-arm (2026-08-) | 0.7 Materials + Failure | mech-statics-fbd |
| mech-dfma-rules | Mfg families + CNC/sheet-metal constraints + bracket redesigns + DFM/DFA rules | qdd-arm-m0.8-mvm | qdd-arm (2026-08-) | 0.8 Manufacturing + DFMA | mech-material-select |
| mech-mechanisms-gruebler | Gruebler DOF + kinematic diagrams + Grashof/type + mechanism vocabulary | qdd-arm-m0.9-mvm | qdd-arm (2026-08-) | 0.9 Mechanisms + Testbed | mech-planar-fk |
| mech-testbed-build | Parametric testbed build + tolerance calibration cube + module swap by hand | qdd-arm-m0.9-mvm | qdd-arm (2026-08-) | 0.9 Mechanisms + Testbed | mech-mechanisms-gruebler, mech-dfma-rules |
| lab-metrology-caliper | Caliper read/zero + resolution vs accuracy vs precision | qdd-arm-m0.10-mvm | qdd-arm (2026-08-) | 0.10 Metrology + Uncertainty | mech-testbed-build |
| lab-uncertainty-rss | Type A/B + RSS + k=2 statement + systematic vs random | qdd-arm-m0.10-mvm | qdd-arm (2026-08-) | 0.10 Metrology + Uncertainty | lab-metrology-caliper |
| sw-c-i2c-register | Raw register I2C reads (START/addr/ACK/STOP, WHO_AM_I, wake, scaling) | qdd-arm-m1.1-mvm | qdd-arm (2026-08-) | 1.1 I2C Sensor + Telemetry | lab-toolchain-verify |
| sw-c-telemetry-plotjuggler | Versioned telemetry format + live PlotJuggler stream | qdd-arm-m1.1-mvm | qdd-arm (2026-08-) | 1.1 I2C Sensor + Telemetry | sw-c-i2c-register |
| ee-perfboard-solder | Through-hole soldered perfboard module, inspected + labeled | qdd-arm-m1.1-mvm | qdd-arm (2026-08-) | 1.1 I2C Sensor + Telemetry | lab-bench-discipline |
| ee-adc-sampling | ADC resolution vs ENOB + Nyquist + input-impedance discipline | qdd-arm-m1.1-mvm | qdd-arm (2026-08-) | 1.1 I2C Sensor + Telemetry | sw-c-i2c-register |
| sw-c-ema-filter | EMA in C on-target + alpha lag-vs-rejection tuning | qdd-arm-m1.2-mvm | qdd-arm (2026-08-) | 1.2 Noise + Filtering | sw-c-telemetry-plotjuggler |
| sw-py-noise-fft | Windowed FFT noise diagnosis + Nyquist/aliasing + targeted fix + error budget | qdd-arm-m1.2-mvm | qdd-arm (2026-08-) | 1.2 Noise + Filtering | sw-c-ema-filter |
| ee-hbridge-pwm | Discrete H-bridge PWM/dir + flyback + shoot-through/deadtime + LTspice-verified | qdd-arm-m1.3-mvm | qdd-arm (2026-08-) | 1.3 H-Bridge + BLDC | ee-power-budget |
| ee-current-sense-afe | Shunt-amp-AA-filter ADC front end, scope-verified (gain/CMRR/BW/offset) | qdd-arm-m1.3-mvm | qdd-arm (2026-08-) | 1.3 H-Bridge + BLDC | ee-hbridge-pwm, ee-adc-sampling |
| ee-bldc-characterize | Sinusoidal spin + back-EMF/pole-pairs/phase-R/Ke + encoder electrical-offset cal | qdd-arm-m1.3-mvm | qdd-arm (2026-08-) | 1.3 H-Bridge + BLDC | ee-current-sense-afe |
| sw-py-pendulum-sim | Paper EOM + solve_ivp pendulum sim + phase portrait | qdd-arm-m1.4-mvm | qdd-arm (2026-08-) | 1.4 Pendulum Dynamics | sw-py-calculus-integrate |
| lab-model-validate | Rig drop logged + sim-vs-real overlay with attributed error + inertia-from-period | qdd-arm-m1.4-mvm | qdd-arm (2026-08-) | 1.4 Pendulum Dynamics | sw-py-pendulum-sim, lab-uncertainty-rss |
| sw-c-complementary-filter | 6-orientation IMU cal + complementary filter with stated alpha/dt | qdd-arm-m1.5-mvm | qdd-arm (2026-08-) | 1.5 Fusion + Calibration | sw-c-ema-filter |
| sw-c-control-loop-integrate | IMU-filter-motor single loop + interface units + GPIO/scope timing proof | qdd-arm-m1.5-mvm | qdd-arm (2026-08-) | 1.5 Fusion + Calibration | sw-c-complementary-filter, ee-hbridge-pwm |
| ee-stepper-microstep | Current-limited microstepping drive + chopper/decay + resonance + torque-speed vs BLDC | qdd-arm-m1.6-mvm | qdd-arm (2026-08-) | 1.6 Stepper + Microstepping | ee-hbridge-pwm |
| ee-vca-wind-drive | Hand-wound coil + F=BILN + flexure + force-vs-current + N/A vs prediction | qdd-arm-m1.7-mvm | qdd-arm (2026-08-) | 1.7 VCA + Motor Rig | ee-bldc-characterize, lab-uncertainty-rss |
| lab-motor-rig-characterize | Load-cell cal + lever-arm metrology + Kt/Ke + torque-speed curve (stall <2 s) | qdd-arm-m1.7-mvm | qdd-arm (2026-08-) | 1.7 VCA + Motor Rig | ee-vca-wind-drive, lab-uncertainty-rss |
| sw-c-stm32-baremetal | Register-level blink + linker script + CMake + OpenOCD/GDB, no HAL | qdd-arm-m2.1-mvm | qdd-arm (2026-08-) | 2.1 Bare-Metal STM32 | sw-c-i2c-register |
| sw-c-stm32-timer-isr | 1 kHz ISR scope-verified + clock-tree + jitter record | qdd-arm-m2.1-mvm | qdd-arm (2026-08-) | 2.1 Bare-Metal STM32 | sw-c-stm32-baremetal |
| sw-c-spi-register | Register-level SPI (CPOL/CPHA match, CS discipline) + device read | qdd-arm-m2.1-mvm | qdd-arm (2026-08-) | 2.1 Bare-Metal STM32 | sw-c-stm32-baremetal |
| sw-c-uart-telemetry | Interrupt-driven UART RX + framing/baud + clock-derived divisor | qdd-arm-m2.1-mvm | qdd-arm (2026-08-) | 2.1 Bare-Metal STM32 | sw-c-stm32-baremetal |
| sw-c-timer-encoder | Timer encoder mode (4x, overflow, velocity, input filter) | qdd-arm-m2.1-mvm | qdd-arm (2026-08-) | 2.1 Bare-Metal STM32 | sw-c-stm32-timer-isr, ee-bldc-characterize |
| sw-py-pid-tune | Plant sim + P/PI/PID plots + windup fix + D-noise + Bode margins + tuning guide | qdd-arm-m2.2-mvm | qdd-arm (2026-08-) | 2.2 PID Theory + Tuning | sw-py-pendulum-sim |
| sw-py-cascade-feedforward | Cascade bandwidth hierarchy + model feedforward + trajectory shaping + sys-id | qdd-arm-m2.2-mvm | qdd-arm (2026-08-) | 2.2 PID Theory + Tuning | sw-py-pid-tune |
| sw-c-foc-current-loop | Open-loop to Iq/Id loops + Clarke/Park logging + ADC-PWM sync + BW/PM + disturbance test | qdd-arm-m2.3-mvm | qdd-arm (2026-08-) | 2.3 FOC Closed-Loop | ee-bldc-characterize, sw-c-timer-encoder, ee-current-sense-afe |
| sw-c-freertos-tasks | 3-task firmware + non-blocking telemetry + IDLE/CAL/RUN/FAULT manager + NVM plan | qdd-arm-m2.4-mvm | qdd-arm (2026-08-) | 2.4 FreeRTOS Firmware | sw-c-stm32-timer-isr, sw-c-control-loop-integrate |
| sw-c-realtime-prove | Priority-inversion demo+fix + watchdog/stack/HardFault + 10k-cycle WCET vs 80pct + hard-vs-soft | qdd-arm-m2.4-mvm | qdd-arm (2026-08-) | 2.4 FreeRTOS Firmware | sw-c-freertos-tasks |
| sw-py-lagrangian-2dof | 2-link Lagrangian EOM (M/C/g) + sim + configuration-dependent inertia | qdd-arm-m2.5-mvm | qdd-arm (2026-08-) | 2.5 Multi-DOF Dynamics | sw-py-pendulum-sim, mech-planar-fk |
| sw-py-statespace-lqr | Linearized A/B/C/D + eigenvalues/natural-freqs + controllability + LQR-vs-PID + tau-ff | qdd-arm-m2.5-mvm | qdd-arm (2026-08-) | 2.5 Multi-DOF Dynamics | sw-py-lagrangian-2dof, sw-py-pid-tune |
| sw-c-homing-sequence | NC-switch homing (2-pass, HW+SW debounce scoped, timeouts to FAULT, wire-break test, ISR priorities, Hall check) | qdd-arm-m2.6-mvm | qdd-arm (2026-08-) | 2.6 Homing + State Machines | sw-c-stm32-baremetal, ee-stepper-microstep |
| sw-c-state-machine-design | Diagram-first state design (guards/entry-exit/FAULT) + 3 further firmware applications | qdd-arm-m2.6-mvm | qdd-arm (2026-08-) | 2.6 Homing + State Machines | sw-c-homing-sequence, sw-c-freertos-tasks |
| sw-c-impedance-control | FOC + impedance outer loop (detent/spring/damper) + nested-loop BW separation + 1 kHz proof | qdd-arm-m2.7-mvm | qdd-arm (2026-08-) | 2.7 Haptic Knob | sw-c-foc-current-loop, sw-c-spi-register |
| mech-knob-integration | Printed housing + bearing press + shaft/set-screw + secured wiring + zero-play feel | qdd-arm-m2.7-mvm | qdd-arm (2026-08-) | 2.7 Haptic Knob | sw-c-impedance-control, mech-testbed-build |
| sw-c-lqr-balance | Sim LQR to 500 Hz-1 kHz hardware + Q/R physical meaning + model-vs-reality gap | qdd-arm-m2.8-mvm | qdd-arm (2026-08-) | 2.8 Inverted Pendulum Cart | sw-py-statespace-lqr, ee-stepper-microstep |
| mech-cart-integration | Rail/extrusion assembly + hand-smooth check + cable routing + homing reuse + NC stops + push-recovery demo | qdd-arm-m2.8-mvm | qdd-arm (2026-08-) | 2.8 Inverted Pendulum Cart | sw-c-lqr-balance, sw-c-homing-sequence |
