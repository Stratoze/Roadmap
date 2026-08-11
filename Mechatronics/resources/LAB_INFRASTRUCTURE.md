# Lab Infrastructure

Buy each phase's tools WHEN YOU ENTER THAT PHASE. Not before.
Total is spread over 12–24 months.

## Phase 0 — Hand Tools + Metrology + Printer (~$400–$1,100)

| Item | Why | Budget |
| --- | --- | --- |
| Digital calipers (Mitutoyo 500-196 or decent clone) | Everything gets measured. If you can't measure it, you can't build it. | $30–$130 |
| Dial indicator + magnetic base | Runout, flatness, bearing checks later | $20–$40 |
| FDM 3D printer (Bambu A1 Mini / Prusa MK4 class) | Primary fabrication for Phases 0–3 | $250–$800 |
| PLA + PETG filament (2 kg) | PLA for prototypes, PETG for flexures/structural | $40–$60 |
| Hobby knife, steel ruler, cutting mat | Cardboard mechanisms, templates | $15 |
| Precision screwdriver set | Later electronics assembly | $15 |

**Not bought yet:** soldering iron, oscilloscope, multimeter (unless owned), CNC, resin printer.

## Phase 1 — First Electronics + Soldering (~$200–$450)

| Item | Why | Budget |
| --- | --- | --- |
| Soldering iron (Pinecil or Hakko FX-888D) | First through-hole soldering | $25–$100 |
| Solder, flux, desoldering braid | Consumables | $20 |
| Perfboard (10+ boards) | First soldered circuits | $10 |
| Bench supply 0–30V 0–5A, current-limited | The safety device of Phases 1–2 | $60–$150 |
| Multimeter (Fluke 117 class) | Voltage/current/resistance/continuity | $50–$150 |
| Magnet wire 24/28/32 AWG | Winding the VCA coil | $15 |
| Neodymium ring magnets N42 | VCA magnetic circuit | $15 |
| S-beam load cell (5 kg) + HX711 | Force measurement on the motor test rig | $20 |

**Not bought yet:** oscilloscope (borrow/cheap USB scope acceptable), hot air, SMD.

## Phase 2 — Embedded + Motion Hardware (~$250–$650)

| Item | Why | Budget |
| --- | --- | --- |
| STM32 Nucleo (G4 or F4 class) + probe | Bare-metal target | $25–$50 |
| Oscilloscope (Rigol DS1102Z / Siglent SDS1104X class) | Timing, PWM, encoder waveforms — no longer optional | $300–$450 |
| AS5048A magnetic encoder breakout | Absolute position for haptic knob and FOC | $15–$25 |
| Gimbal BLDC motor (3506 class, low Kv) | Haptic knob rotor | $15–$30 |
| MGN12 linear rail 400 mm + carriage | Inverted pendulum cart | $30–$50 |
| 2020 aluminum extrusion + brackets + T-nuts | Bolt-together frames. No cutting metal. | $30–$60 |
| NEMA17 + TMC2209 | Cart drive | $25 |
| 6800/6801 bearings (a few pairs) | Pivot joints | $10–$20 |

## Phase 3 — CNC Services + PCB + SMD (~$500–$1,500)

| Item | Why | Budget |
| --- | --- | --- |
| CNC service (SendCutSend / Xometry / PCBWay CNC) | QDD housing in 6061-T6. You design CAD; they machine. | $50–$200 per housing |
| JLCPCB/PCBWay 4-layer + stencil | The Puck PCB | $30–$100 per batch |
| Hotplate + thermocouple PID (or cheap reflow oven) | SMD reflow for the Puck | $50–$150 |
| Hot air station + solder paste + tweezers | Rework | $50–$90 |
| Planetary gearbox 9:1 or 10:1 (Neugart-class or quality StepperOnline) | QDD transmission. You do NOT design gears. | $40–$150 |
| Precision bearings (SKF/NSK/NTN, ABEC-3+) | QDD joints. Not random AliExpress. | $20–$40 |
| Precision ground shaft 8 mm | Output shaft | $10–$20 |
| Retaining rings, shims, Kapton, thermal pads | Assembly consumables | $15 |
| Second bench supply or 48V supply | QDD bus | $60–$150 |

**CNC service discipline:** you only order AFTER the 3D-printed prototype fits, the FEA
passes, and the DFM review from Milestone 0.8 is done. A bad STEP file sent early is
wasted money — the exact failure mode you asked to avoid.

## Phase 4 — Integration + Safety (~$200–$700)

| Item | Why | Budget |
| --- | --- | --- |
| DIN rail, contactors (DC-rated!), E-stop button (NC, dual-channel) | Hardwired safety. DC rating matters — AC ratings lie. | $50–$90 |
| Fuses + holders, terminal blocks, ferrules + crimp tool | PDU + harness | $30 |
| Aviation connectors or Molex Micro-Fit, braided sleeve, shielded twisted pair | Harness | $40–$70 |
| Panel material (3 mm acrylic, laser-cut service) | PDU faceplate | $20–$50 |
| Label maker | Every cable, both ends | $15 |
| Servo or small BLDC for gripper | End effector | $20–$40 |
| Pogo pins + dowel pins | Tool changer | $15 |

## Phase 5 — Display (~$100–$250)

| Item | Why | Budget |
| --- | --- | --- |
| Acrylic 3–5 mm, laser-cut service | Exploded-view pedestal | $40–$80 |
| LED strip | Backlight | $15 |
| Tripod + light | Video/photo evidence | $30–$60 |

## Sourcing principles

1. **Buy motor cores and gearboxes; design the integration.** You are not a metallurgist. Wind your own coil (Phase 1, for physics), but buy the QDD stator/rotor and gearbox.
2. **Services replace machine ownership.** SendCutSend/Xometry for aluminum, JLCPCB for boards, laser service for acrylic. You supply correct CAD + tolerances; they supply the machine.
3. **Quality fasteners and bearings.** McMaster or equivalent, grade 8.8+. Bearing quality determines actuator smoothness.
4. **One phase's budget at a time.** Do not buy Phase 3 tools in Phase 0. You won't know how to use them and you'll buy wrong.
