---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# Firmware Timing Check — {{date}} — {{title}}

Determinism gate BEFORE HIL sign-off. A loop that usually makes it is a loop that fails on demo day.

## Checks

- [ ] Control-loop jitter measured (GPIO toggle + scope); WCET over 10k cycles with utilization ≤20% at the loop rate (5x headroom — state the rate, the WCET, and the quotient)
- [ ] ADC-to-PWM sync verified: sample point vs switching edge documented; evidence filed in `measurement_capture.md`
- [ ] SPI modes (CPOL/CPHA) and UART divisor proven at bench bring-up (3.2) — re-verified here, not discovered here
- [ ] Interrupt priorities: control > limit/fault > telemetry, stated and set
- [ ] Watchdog + HardFault paths demonstrated, not just enabled

## Verdict

- [ ] PASS to HIL / FAIL with rework list:
