# Coursework: what I've learned

Claude updates this after coursework sessions. Coursework does not count toward the daily floor.

## Python / data science (presentation Mon 2026-10-12 on `Stratoze/python-data-scraping`)
- Slides: Claude drafts. Understanding and speaker notes: learner, in own words.
- Can predict: filtering rows (`&`, `~`), labels kept after filtering, new columns (snapshots, can go stale), `.loc`, `mean` (incl. of True/False = fraction), `groupby().mean()`, `Series.apply` (returns new Series), `df.apply(..., axis=1)` row by row, lambda, `classify_risk` early return.
- Shaky: gives rules instead of concrete outputs; mislabels groups.
- Not earned: "mask" (say "True/False column").
- Repo walk stopped mid `clean_data()` at `dropna`. Next: `dropna` / `reset_index`, then `analyze()`, charts, scrape, export.
- 2026-10-11: learner did not yet understand the pandas/numpy basics. Taught: numpy array (fixed-length, one type, `arr * 2` makes a new array), Series (labelled column, `.values` = numpy array), DataFrame (table of Series), filtering keeps original row labels, `reset_index`. Learner predicted: `classify_risk` on student 3 → high via `failures >= 2` (correct, said "3 fails" first). `dropna` on 395 rows with 2 blank G3 → 393 (correct). `result = df["G3"].values * 2` leaves `df["G3"]` unchanged (correct after one hedge).
- Shaky: hedges with "either/or" on predictions (commit to one output); reads a variable on the right side as if it were assigned.
- Still need from learner: talk length and requirements. Still not done: explain the repo in own words (learner said "I don't even understand the python part" on 2026-10-11).
