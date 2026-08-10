#!/usr/bin/env python3
"""
Simulation: short_name
Date: YYYY-MM-DD

Question:
    What am I trying to predict?

Prediction before running:
    I expect ___ because ___.

Model assumptions:
    -
    -

Expected artifact:
    docs/captures/YYYY-MM-DD_short_name.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CAPTURES = ROOT / "docs" / "captures"
CAPTURES.mkdir(parents=True, exist_ok=True)


def main() -> None:
    # Replace this with the actual model.
    t = np.linspace(0, 1, 500)
    y = np.zeros_like(t)

    fig, ax = plt.subplots()
    ax.plot(t, y)
    ax.set_xlabel("time [s]")
    ax.set_ylabel("output [unit]")
    ax.set_title("Replace with simulation title")
    ax.grid(True)

    out = CAPTURES / "YYYY-MM-DD_short_name.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()