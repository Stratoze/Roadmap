# ReadMe

Use for KiCad projects, schematics, layouts, BOMs, fabrication outputs, and bring-up notes.

## Tool stack

- **EDA:** KiCad 9 (free, open source, macOS/Windows/Linux). <https://www.kicad.org/>
- **Learning:** Phil's Lab (YouTube) for mixed-signal design. DigiKey KiCad series for basics. KiCad forum (forum.kicad.info) for specific errors.
- **Trace width:** use KiCad's built-in PCB Calculator (Tools → PCB Calculator) with IPC-2152 for current capacity. Don't guess.

## Before schematic

- Define current-sensing topology.
- Verify footprints against datasheet land patterns.
- Draw ground return paths as arrows.
- Confirm part availability.

## Suggested structure per board

```txt
pcb/board_name/
├── schematic/
├── layout/
├── fabrication/
├── assembly/
├── bringup/
└── bom/
```

Use `bom_template.csv` (in this folder), [[_templates/mech/schematic_review|schematic_review]], and [[_templates/mech/pcb_bringup|pcb_bringup]].
