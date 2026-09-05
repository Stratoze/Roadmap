---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# Firmware Timing Check — {{date}} — {{title}}

Determinism gate BEFORE HIL sign-off. A loop that usually makes it is a loop that fails on demo day.

## Checks

- [ ] Control-loop jitter measured (GPIO toggle + scope); WCET over 10k cycles with 80% headroom rule
- [ ] ADC-to-PWM sync verified: sample point vs switching edge documented
- [ ] SPI modes (CPOL/CPHA) and UART divisor proven on hardware, not assumed from examples
- [ ] Interrupt priorities: control > limit/fault > telemetry, stated and set
- [ ] SIL-vs-HIL divergence triaged: >2x tracking gap means the model is wrong — update the model, not the gains
- [ ] Watchdog + HardFault paths demonstrated, not just enabled

## Verdict

- [ ] PASS to HIL / FAIL with rework list:
