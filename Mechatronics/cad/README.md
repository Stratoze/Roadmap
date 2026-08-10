# CAD

Use for mechanical parts, assemblies, exported STEP/STL files, drawings, and release notes.
Before opening CAD, write requirements. If payload/reach/material/manufacturing method are blank, design has not started.

## Tool stack

- **Primary CAD:** Solid Edge Community Edition (Windows, free, no student ID). Download: <https://resources.sw.siemens.com/en-US/download-solid-edge-community-edition/>
- **FEA:** PrePoMax (Windows, portable, free). Import STEP from Solid Edge. <https://prepomax.fs.um.si/>
- **macOS STEP viewer:** FreeCAD (free, native macOS). For quick viewing, measurement, light edits. Not the primary design tool.
- **Exchange format:** STEP (`.step` / `.stp`) for everything. Solid Edge CE cannot open others' native files. Always export STEP.

## Suggested structure

```txt
cad/
├── requirements/
├── parts/
├── assemblies/
├── drawings/
└── exports/          ← STEP files live here
```

Use templates/cad_release.md before calling anything release-ready.

## Checklists
- [Assembly Template](assembly_template.md) — copy for each new assembly
- [Part Template](part_template.md) — copy for each new part
