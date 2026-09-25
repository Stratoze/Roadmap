# Python

## Goal
- Scoping answer (verbatim, 2026-09-14): "i want to be able to do data, ai, robotics, basically a lot of stuff with python, it's the prototyping language anyway, for now lets focus on the most commonly used lib as well as core python"
- By when: 2026-10-14 (stated "by say 1 month" on 2026-09-14)
- Mode: project-based - a project only needs to teach at least 1 skill (learner's standing rule); the 2-link arm tip plot is a milestone, not the first project.
- Source: `Daily/2026-09-14.md`, verbatim in `_private/learning/verbatim/2026-09-14-python.md`

## Map
- Provisional (2026-09-14): mapping not started (new topic; priors from mech software work unknown - bracket on first contact)
- Bracket 2026-09-14 (data model strand, open conversation - no code run yet): floor = general reference/mutation reasoning only (mutable default `[]` persists across calls; `b = a` aliases; rebinding vs mutating distinguished). **Correction (learner, same session): "i have never touched python before" - the probes showed transferable reasoning, NOT Python schema; dict/`def`/`print` were read cold, not known.** Ceiling: zero Python experience is the true floor - this is a zero-schema start (orientation before prediction; no quiz before schema).
- Scout scan 2026-09-14: sequence proposed - env → core data model/containers → control/iteration idioms → modules/stdlib/I/O → light OOP/dataclasses → numpy (arrays, broadcasting, views vs copies, radians) → matplotlib (OO fig/ax, equal aspect) → pandas (loc/iloc, CoW, groupby, resample) → scipy (optimize, signal, solve_ivp, Rotation) → one integration loop. Projects proposed (each 1 skill, chained): log summarizer → binary frame decoder (optional) → vectorized arm-tip sweep → arm-tip figure → telemetry clean-and-plot. Cross-cutting gotchas: venv vs global, radians, vectorization vs loops, views vs copies, axis semantics, index alignment, float equality. Prune pending with learner.
- Env check 2026-09-14: python 3.14.7; numpy 2.5.3 present; matplotlib/scipy/pandas NOT installed (scout's 3.14 wheel-lag flag is partly live - verify at install time).

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| py-env | run scripts in a project venv; install/pin a library | - | seen | 0 | - | 2026-09-14 venv+jupyter setup |
| py-first-touch | write and run a first cell; read output; change one value and re-run | py-env | unknown | 0 | - | - |
| py-core-types | types, variables, strings, f-strings, numbers | py-env | unknown | 0 | - | - |
| py-control | conditionals, loops, range, comprehensions | py-core-types | unknown | 0 | - | - |
| py-functions | def, args, returns, scope, modules/imports | py-control | unknown | 0 | - | - |
| py-collections | lists, dicts, sets, tuples, slicing, iteration idioms | py-core-types | unknown | 0 | - | - |
| py-files-errors | files, exceptions, context managers | py-functions | unknown | 0 | - | - |
| py-numpy | arrays, vectorized math, shapes, indexing (radians discipline) | py-collections | unknown | 0 | - | - |
| py-matplotlib | plots, labels, subplots, reading a figure critically | py-numpy | unknown | 0 | - | - |
| py-pandas | DataFrames, load/clean/aggregate, CSV telemetry | py-numpy | unknown | 0 | - | - |
| py-scipy | solve_ivp, root finding, basic signal helpers | py-numpy | unknown | 0 | - | - |
| py-project-loop | take a tiny project end-to-end: script + data + plot + note | py-files-errors, py-matplotlib | unknown | 0 | - | - |

## Resources

Active source selected JIT through the `resources` skill when the concept activates. Historical candidates and verification decisions are in [[_system/learning/archive/source-ledger|source ledger]].

## Usage events
| date | event_id | concept/item_ref | event | evidence | public note |
|------|----------|------------------|-------|----------|-------------|

## Misconceptions
-

## Problems
| id | problem | source | theory | attempts | status |
|----|---------|--------|--------|----------|--------|
| - | - | - | - | - | - |

## Links
- Rests on: (none - foundation track)
- Teaches: feeds DataScience & AI (data wrangling, ML core); mech Python sims (`Mechatronics/simulations/python/`); first arm-tip project = `sw-py-forward-kinematics` in `Mechatronics/skills/registry.md`
- Lessons: -

## Log
- 2026-09-14 - file created from Appendix A; goal stored verbatim (data/AI/robotics prototyping, core Python + common libraries, 1 month, project-based); map opened. Learner correction same day: "i have never touched python before" - zero-schema start, orientation first; project scope cut to a first script that teaches one skill at the smallest size.
