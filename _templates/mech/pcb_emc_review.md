---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# PCB EMC Review — {{date}} — {{title}}

Layout gate BEFORE Gerber order. The schematic can be perfect and the board still fail.

## Checks

- [ ] ERC + DRC clean (not "only a few warnings")
- [ ] Every IC, every connector, and anything with >2 pins or a thermal pad checked vs datasheet land pattern (pad count, pin 1, courtyard) — "trivial" packages kill boards too
- [ ] One solid ground plane; analog/digital separated by placement, never by splits
- [ ] Switching node short, narrow, plane intact beneath it
- [ ] Buck input cap placed first, < 5 mm; decoupling 100 nF < 3 mm + 10 uF bulk per rail
- [ ] Trace widths sized for stall current per IPC-2221, not nominal
- [ ] Ground return arrows drawn: motor, ADC, MCU returns share no segment before the star point
- [ ] Programming/debug header reachable with the board mounted

## Verdict

- [ ] PASS to fab / FAIL with rework list:
