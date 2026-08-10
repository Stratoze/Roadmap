---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# PCB Bring-Up — {{date}} — Board Rev — {{title}}

For the generic pre-power procedure, see `templates/first_power_on.md`.

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
- [ ] Clock/oscillator present if needed
- [ ] GPIO sanity check
- [ ] Driver enable disabled by default
- [ ] Load test with safe dummy load

## Issues

| Issue | Suspect | Evidence | Next |
| --- | --- | --- | --- |
| | | | |

## Result

Pass / fail:

Artifact paths:
