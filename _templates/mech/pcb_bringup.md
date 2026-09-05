---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# PCB Bring-Up — {{date}} — Board Rev — {{title}}

For the generic pre-power procedure, see `_templates/mech/first_power_on.md`.

This template adds PCB-specific checks on top of it.

## Board

Name:

Revision:

Schematic commit / tag:

Assembly state:

## PCB-specific pre-power

- [ ] Visual inspection under magnification
- [ ] No solder bridges on fine-pitch pins
- [ ] Critical polarized parts oriented correctly

## Rails

| Rail | Expected | Measured | Pass? |
| --- | ---: | ---: | --- |
| | | | |

## Functional checks

- [ ] Programming/debug interface connects
- [ ] Clock/oscillator running at the expected frequency (scope or firmware readout)
- [ ] GPIO sanity check
- [ ] Gate-driver enable held OFF by default (pull-down/hardware default — motor must not drive at power-on)
- [ ] Load test with safe dummy load

## Issues

| Issue | Suspect | Evidence | Next |
| --- | --- | --- | --- |
| | | | |

## Result

Pass / fail:

Artifact paths:
