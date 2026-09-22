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
Zero-schema note: docs.python.org's own tutorial states it is "designed for programmers that are new to the Python language, not beginners who are new to programming". The learner has never used Python, so the ladder leads with Sweigart's book and CS50P for first contact; the official docs are the precise reference layer, not the first read.

- rigorous | Automate the Boring Stuff with Python (3rd ed., No Starch 2025, ISBN 9781718503403) | Al Sweigart | book: ch 1 "Python Basics"; ch 2 "if-else and Flow Control"; ch 3 "Loops"; ch 4 "Functions"; ch 6 "Lists"; ch 7 "Dictionaries and Structuring Data"; ch 8 "Strings and Text Editing"; ch 10 "Reading and Writing Files"; ch 18 "CSV, JSON, and XML Files"; App. A "Installing Third-Party Packages" | https://nostarch.com/automate-boring-stuff-python-3rd-edition | for py-first-touch, py-core-types, py-control, py-functions, py-collections, py-files-errors, py-env | verified 2026-09-15
- rigorous | Python Data Science Handbook (online edition) | Jake VanderPlas | book: ch 2 "Introduction to NumPy"; ch 3 "Data Manipulation with Pandas"; ch 4 "Visualization with Matplotlib" | https://jakevdp.github.io/PythonDataScienceHandbook/ | for py-numpy, py-pandas, py-matplotlib | verified 2026-09-15
- reference | The Python Tutorial (v3.14) | Python Software Foundation | docs: Ch. 3 "An Informal Introduction to Python" (3.1.1 Numbers, 3.1.2 Text, 3.1.3 Lists) | https://docs.python.org/3.14/tutorial/introduction.html | for py-first-touch, py-core-types, py-collections | verified 2026-09-15
- reference | The Python Tutorial (v3.14) | Python Software Foundation | docs: Ch. 4 "More Control Flow Tools" (4.1 if, 4.2 for, 4.3 range(), 4.8 Defining Functions, 4.9 More on Defining Functions) | https://docs.python.org/3.14/tutorial/controlflow.html | for py-control, py-functions | verified 2026-09-15
- reference | The Python Tutorial (v3.14) | Python Software Foundation | docs: Ch. 5 "Data Structures" (5.1.3 List Comprehensions, 5.3 Tuples and Sequences, 5.4 Sets, 5.5 Dictionaries, 5.6 Looping Techniques) | https://docs.python.org/3.14/tutorial/datastructures.html | for py-collections, py-control | verified 2026-09-15
- reference | The Python Tutorial (v3.14) | Python Software Foundation | docs: Ch. 6 "Modules" (6.1 More on Modules, 6.4 Packages) | https://docs.python.org/3.14/tutorial/modules.html | for py-functions | verified 2026-09-15
- reference | The Python Tutorial (v3.14) | Python Software Foundation | docs: Ch. 7 "Input and Output" (7.1.1 Formatted String Literals, 7.2 Reading and Writing Files) | https://docs.python.org/3.14/tutorial/inputoutput.html | for py-core-types, py-files-errors | verified 2026-09-15
- reference | The Python Tutorial (v3.14) | Python Software Foundation | docs: Ch. 8 "Errors and Exceptions" (8.3 Handling Exceptions, 8.7 Defining Clean-up Actions) | https://docs.python.org/3.14/tutorial/errors.html | for py-files-errors | verified 2026-09-15
- reference | The Python Tutorial (v3.14) | Python Software Foundation | docs: Ch. 12 "Virtual Environments and Packages" (12.2 Creating, 12.3 Managing Packages with pip) | https://docs.python.org/3.14/tutorial/venv.html | for py-env | verified 2026-09-15
- rigorous | NumPy: the absolute basics for beginners | NumPy developers | docs: array fundamentals, attributes, indexing/slicing, basic operations, broadcasting | https://numpy.org/doc/stable/user/absolute_beginners.html | for py-numpy | verified 2026-09-15
- reference | NumPy quickstart | NumPy developers | docs: indexing/slicing/iterating, shape manipulation, copies and views, broadcasting rules | https://numpy.org/doc/stable/user/quickstart.html | for py-numpy | verified 2026-09-15
- reference | Matplotlib Quick start guide | Matplotlib developers | docs: simple example, Parts of a Figure (Figure/Axes/Axis/Artist), labelling, scales and ticks, multiple Figures and Axes | https://matplotlib.org/stable/users/explain/quick_start.html | for py-matplotlib | verified 2026-09-15
- rigorous | pandas User Guide: "10 minutes to pandas" | pandas developers | docs: object creation, viewing data, selection, missing data, grouping, CSV import/export | https://pandas.pydata.org/docs/user_guide/10min.html | for py-pandas | verified 2026-09-15
- rigorous | SciPy User Guide | SciPy developers | docs: Integration (solve_ivp); Optimization (root finding); Signal Processing (filtering, spectral analysis) | https://docs.scipy.org/doc/scipy/tutorial/integrate.html | for py-scipy | verified 2026-09-15
- interactive | CS50's Introduction to Programming with Python | David J. Malan, Harvard University | course: Week 0 Functions/Variables, Week 1 Conditionals, Week 2 Loops, Week 3 Exceptions, Week 4 Libraries, Week 6 File I/O, Final Project | https://cs50.harvard.edu/python/ | for py-first-touch, py-core-types, py-control, py-functions, py-files-errors, py-env, py-project-loop | verified 2026-09-15
- interactive | Python for Everybody (PY4E) | Dr. Charles Severance, University of Michigan | course: conditionals, functions, loops and iteration, files, lists, dictionaries, tuples, regex + autograded assignments | https://www.py4e.com/ | for py-first-touch, py-core-types, py-control, py-collections, py-functions, py-files-errors, py-project-loop | verified 2026-09-15
- interactive | JupyterLite (browser sandbox, no install) | Project Jupyter | sandbox: lab/index.html | https://jupyter.org/try-jupyter/lab/index.html | for py-first-touch, py-core-types, py-numpy, py-pandas, py-matplotlib | verified 2026-09-15
- intuitive | CS50P Lecture 0 and Lecture 2 | CS50 / David J. Malan | video @ chapters: "hello.py", "functions/args/side effects", "return values/variables", "f-Strings", "defining functions/scope/return" (L0); "loops/while", "for", "lists", "dictionaries" (L2) | https://video.cs50.io/JP7ITIXGpHk | for py-first-touch, py-core-types, py-functions, py-control | verified 2026-09-15
- intuitive | CS50P Lecture 6 "File I/O" | CS50 / David J. Malan | video @ chapters: "open", "with", "CSV", "csv library", "csv.reader/DictReader/Writer" | https://video.cs50.io/KD-Yoel6EVQ | for py-files-errors, py-pandas, py-project-loop | verified 2026-09-15
- intuitive | A Visual Intro to NumPy and Data Representation | Jay Alammar | page: visual-numpy | https://jalammar.github.io/visual-numpy/ | for py-numpy | verified 2026-09-15
- intuitive | A Gentle Visual Intro to Data Analysis in Python Using Pandas | Jay Alammar | page: gentle-visual-intro-to-data-analysis-python-pandas | https://jalammar.github.io/gentle-visual-intro-to-data-analysis-python-pandas/ | for py-pandas | verified 2026-09-15

Version caveats (checked 2026-09-15):
- cp314 macOS wheels exist for numpy 2.5.3, matplotlib 3.11.2, pandas 3.0.5, scipy 1.18.1 - the earlier 3.14 wheel-lag concern looks resolved. Verify at install time, not from this line.
- Live docs now show pandas 3.0.x. pandas 3.0 changes defaults (string dtype, Copy-on-Write) against tutorials written for 2.x; the cited "10 minutes to pandas" and Alammar posts predate 3.0. Pin the learner's pandas and check examples against the pinned version.
- Docs URLs are version-pinned to /3.14/ where possible. matplotlib.org returned 200 on one probe and 000 on another - re-warm before relying on it.
- py-scipy has rigorous docs only; no verified SciPy-specific video. That is a deliberate gap.

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
