# ReadMe

Use for KiCad projects, schematics, layouts, BOMs, fabrication outputs, and bring-up notes.

## Tool stack

- **EDA:** KiCad 9 (free, open source, macOS/Windows/Linux). <https://www.kicad.org/>
- **Learning:** Phil's Lab (YouTube) for mixed-signal design. DigiKey KiCad series for basics. KiCad forum (forum.kicad.info) for specific errors.
- **Trace width:** use KiCad's built-in PCB Calculator (Tools → PCB Calculator) with IPC-2221. Don't guess.

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

Use bom_template.csv, [schematic_review_template.md](schematic_review_template.md), and templates/pcb_bringup.md.
