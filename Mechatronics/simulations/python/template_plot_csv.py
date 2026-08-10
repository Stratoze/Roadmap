#!/usr/bin/env python3
"""
Plot a CSV log and save the figure to docs/captures.

Usage example:
    python3 template_plot_csv.py ../../data/raw/YYYY-MM-DD_log.csv time_s value
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
CAPTURES = ROOT / "docs" / "captures"
CAPTURES.mkdir(parents=True, exist_ok=True)


def read_columns(path: Path, x_name: str, y_name: str) -> tuple[list[float], list[float]]:
    xs: list[float] = []
    ys: list[float] = []
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            xs.append(float(row[x_name]))
            ys.append(float(row[y_name]))
    return xs, ys


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: template_plot_csv.py path.csv x_column y_column")
        return 2

    path = Path(sys.argv[1])
    x_name = sys.argv[2]
    y_name = sys.argv[3]

    xs, ys = read_columns(path, x_name, y_name)

    fig, ax = plt.subplots()
    ax.plot(xs, ys)
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.set_title(path.stem)
    ax.grid(True)

    out = CAPTURES / f"{path.stem}_{y_name}.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

