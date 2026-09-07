# Firmware

Firmware lives here once real code begins.

Use one folder per board or target. Keep generated build output out of Git.

Suggested structure:

```txt
firmware/
├── esp32/
│   └── project_name/
└── stm32/
    └── project_name/
```

For each firmware project, copy `../../_templates/mech/module_readme.md` into the project as needed for non-trivial modules. Targets: [[Mechatronics/firmware/esp32/README|esp32/]] · [[Mechatronics/firmware/stm32/README|stm32/]].

## Firmware rules

- Write the interface before the implementation.
- Keep telemetry out of timing-critical paths.
- Commit every known-good state.
- Branch per experiment; bisect when lost; never force-push a known-good tag.
- If it worked yesterday and not today: `git diff`.
