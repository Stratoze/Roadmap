---
date: "{{date:YYYY-MM-DD}}"
title: "{{title}}"
---

# Stress Inoculation — Timed Debugging Exercise — {{date}} — {{title}}
## Purpose
Practice debugging under time pressure to build state-dependent recall.
Engineering judgment is needed when the board is smoking and you have 5 minutes,
not when you have a quiet afternoon. This exercise simulates that state.

## Setup
- [ ] Choose a system you've already built and understand
- [ ] Have a peer, friend, or AI introduce a fault you don't know about
  (or use a random fault from the list below)
- [ ] Set a timer: **10 minutes** for diagnosis, **5 minutes** for fix
- [ ] Have your scope, meter, and tools ready but NOT pre-configured
- [ ] No notes open. No milestone files open. Just you and the hardware.

## Fault Menu (pick one, or have someone else pick)
| Fault | How to introduce |
| --- | --- |
| Encoder dropout | Disconnect encoder cable mid-motion |
| Wrong SPI mode | Change CPOL/CPHA in firmware, reflash |
| Ground loop | Connect two grounds through a long wire |
| Power sag | Add a resistive load to the supply rail |
| Swapped motor phases | Swap two of three BLDC phase wires |
| I2C address conflict | Connect a second device at the same address |
| Floating enable pin | Disconnect the ENABLE pin on the motor driver |
| Corrupted calibration | Change the IMU offset by 10° in firmware |
| Timing jitter | Add a blocking delay in the control ISR |
| Wrong units | Change radians to degrees in one interface |

## Prediction (before starting)
I expect the symptom to be:
My first diagnostic step will be:

## Timed Execution
### Diagnosis phase (10 min)
What I observed:
What I checked first:
What I checked second:
Did my default strategy work? yes / no
What did I switch to?

### Fix phase (5 min)
Did I fix it in time? yes / no
What was the root cause?

## Reflection (after, no timer)
- What debugging strategy did I default to under pressure?
- Was it the right strategy? If not, what would have been faster?
- What knowledge did I reach for that I couldn't recall?
- What did I know cold (didn't have to think about)?
- What did I have to look up or guess?
- How did my decision quality compare to a calm debugging session?

## Integration
- [ ] Add any new landmines discovered to the relevant milestone file
- [ ] If a knowledge gap was revealed, add an Anki card or re-derive the concept
- [ ] Update the relevant FMEA if the fault wasn't predicted
