# Coursework: what I've learned

Claude updates this after coursework sessions. Coursework does not count toward the daily floor.

## Python / data science (presentation Thu 2026-10-15 11:00 JST, moved from Mon 10-12 on `Stratoze/python-data-scraping`)
- Slides: Claude drafts. Understanding and speaker notes: learner, in own words.
- Can predict: filtering rows (`&`, `~`), labels kept after filtering, new columns (snapshots, can go stale), `.loc`, `mean` (incl. of True/False = fraction), `groupby().mean()`, `Series.apply` (returns new Series), `df.apply(..., axis=1)` row by row, lambda, `classify_risk` early return.
- Shaky: gives rules instead of concrete outputs; mislabels groups.
- Not earned: "mask" (say "True/False column").
- Repo walk stopped mid `clean_data()` at `dropna`. Next: `dropna` / `reset_index`, then `analyze()`, charts, scrape, export.
- 2026-10-11: learner did not yet understand the pandas/numpy basics. Taught: numpy array (fixed-length, one type, `arr * 2` makes a new array), Series (labelled column, `.values` = numpy array), DataFrame (table of Series), filtering keeps original row labels, `reset_index`. Learner predicted: `classify_risk` on student 3 → high via `failures >= 2` (correct, said "3 fails" first). `dropna` on 395 rows with 2 blank G3 → 393 (correct). `result = df["G3"].values * 2` leaves `df["G3"]` unchanged (correct after one hedge).
- Shaky: hedges with "either/or" on predictions (commit to one output); reads a variable on the right side as if it were assigned.
- Still need from learner: talk length and requirements. Still not done: explain the repo in own words (learner said "I don't even understand the python part" on 2026-10-11).
- 2026-10-12 grill (repo for the talk). Can explain after correction: pipeline `load_data → clean_data (risk computed here, before dropna) → analyze (correlation) → export_results`; `to_numeric(errors="coerce")` ("12","abc","7" → 12, NaN, 7); `.copy()` = separate in-memory table, raw CSV is never written; `pass_fail` is the text "pass"/"fail" (only yes/no columns are 1/0), grades 0-20, pass mark 10; `apply(axis=1)` = once per row; `NaN < 10` is False, so a NaN-G3 row can get "low" but `dropna` removes it before any number is reported; dropping the 38 zero-G3 students moves the pass rate 0.671 → 0.742 (predicted +0.3); don't drop them (would hide fails); correlation = strength and direction of a straight-line link, not cause; G3 can't cause G2 (temporal precedence); confounder = third factor pushing both up.
- Report wording accepted: "Guess: the 38 zeroes, which count as fails, came from students not taking the test." `report.md` still says "check that before reading anything into them": learner to update it.
- Shaky: hedges ("probably"); rounds 0.742 to "0.7"; called a rule an "axiom" (standard term: temporal precedence); first said `.copy()` protects the CSV and `pass_fail` is 1/0.
- Not earned: "confounder" (asked what it is on 10-12; explained once).
- Open: Q22 (how to test the risk cut-offs), absences ≈ 0 correlation, why PISA is not joined. Talk length and format still not given. Speaker notes blank.
