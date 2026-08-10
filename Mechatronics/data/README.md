# Data

Use for logs and datasets.

Do not overwrite raw data. Create processed copies instead.

```txt
data/
├── raw/
└── processed/
```

## Naming

```txt
YYYY-MM-DD_source_condition.ext
```

Examples:

```txt
2026-08-02_imu_static_raw.csv
2026-08-03_motor_back_emf_hand_spin.csv
2026-08-04_pid_step_response_processed.csv
```

## Record context

For meaningful datasets, use `templates/experiment_note.md`.

Minimum context:

- firmware/code commit
- sample rate
- units
- calibration
- hardware setup
- what was happening during capture
