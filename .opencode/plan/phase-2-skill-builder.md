# Phase 2 — Skill Builder (decouple vault + foolproof gates + nodes + lenses)

Status: PLAN — do not implement until user approves this file + reviewer sign-off.
(Win-adapted 2026-09-08 for reviewer blockers: ordering, checkability, tag grammar,
staleness vs landed 13-topic store. Still unapproved — this edit changes no vault content.)
Active-phase rule: AGENT.md §Hard Rules names the active phase; on conflict the active
phase's file governs. Depends on: Phase 1 complete (AGENT.md live, vault caught up,
diagnose at known-baseline).
Incorporates: vault-structure + load/sustainability evaluations (2026-09-07) AND all
plan-review rounds. Where this file contradicts those evaluations, this file governs
and says why. Reference convention: §X item N = the check numbered N (gate items are
0-based: §4 item 0 is the first check, tag format).
File:line citations are repo-root-relative paths + current line numbers (re-check: rot fast). Runner for all engram operations: `$ENGRAM_RUNNER` (per-machine env — Mac `python3 $HOME/engram/scripts/engram.py`, Win `python3 $HOME/.config/opencode/scripts/engram.py` — `$HOME` form, NEVER `~` (tilde never expands after parameter expansion or inside quotes — verified crash); see `_system/engram/env.example.sh`. NEVER hardcode either path)
(subcommands `due`, `topics`, `session-start`, `doctor`, `add-topic`,
`edit-node`, `retire`, `rate`, `receipt`, `selftest`). Invoke scripts as
`bash scripts/<name>.sh` (works regardless of the +x bit). Windows runners MUST export
`PYTHONIOENCODING=utf-8` first (engine emits UTF-8 the Win codepage cannot encode —
verified crash without it; see `_system/engram/env.example.sh`).

## 0. Verified starting facts (2026-09-07, re-check at build time — counts rot fast)

- `Mechatronics/milestones/00_foundations.md`: 599 lines, milestones 0.1–0.10 (0.1 is
  `##`, 0.2–0.10 are `#` — say exactly that). ROADMAP carries NO `#fragment` links
  today — the gap is absence, not mismatch (verified: grep `(.*#.*)` empty).
  `scripts/diagnose.py` does NOT validate `#anchors` (extended in §2 item 2).
- Goal coupling ≈ 60+ hits repo-wide. CANONICAL PATTERN (used by §0 inventory AND §1
  acceptance — single source, no drift):
  `QDD|2-DOF|2DOF|2 DOF|2-link|Puck|backdrivab|quasi-direct|SendCutSend|gripper|lever-arm`
  plus human semantic pass for generic `arm|actuator` in goal-flavored contexts
  (checklist lives in GOAL.md once created — circularity resolved: the §1 task CREATES
  the checklist as it rewrites). Coupled files (pattern-confirmed hits — every line below
  matches the canonical pattern; the semantic pass covers generic `arm|actuator` contexts
  the pattern misses): `Science/Index.md:14` (Puck PCB thermal + QDD gear hits; Lorentz on that
  line attaches to the voice-coil rig, not to Puck/QDD — attributed exactly),
  `DataScience/Index.md:9,13` (QDD telemetry pipeline), `Mechatronics/resources/LAB_INFRASTRUCTURE.md`
  (`:51-53,55-56,59,74,87-88` SendCutSend/Puck/QDD/gripper/hotplate/bench-supply lines), `Mechatronics/IDEAS.md`
  (`:17-18,28,33,36` Puck/2-DOF/Gripper/backdrivab/QDD/SendCutSend lines),
  `Mechatronics/hardware/inventory.md` (`:12` BLDC/QDD line).
- Foundations are ALREADY goal-instantiated (0.2 FK arm tip, 0.4 arm FBD + holding
  torque, QDD torque-constant reference at 0.10 `:568`, 0.7 arm-link material,
  CONVENTIONS arm frame defaults (`Mechatronics/resources/CONVENTIONS.md:46-55`): §1 parameterization tasks are mandatory,
  not cosmetic (scaffold-first per §1 — mass parameterization deferred to pass 2).
- Engram (LANDED vault store — `_system/engram/`, 13 topics / 270 nodes / 258 `new` /
  0 repo receipts as of 2026-09-08 — counts re-verified at build, never trusted from here;
  reconciled 340 HOLD / 14 PORT (`mech-spine`, Mac) / 0 DROP; re-sits ~zero (all Win
  receipts pre-divergence, Win nodes adopted in place — "re-sit" = re-answer a moved node). ENGINE_PIN green (engine sha
  FULL match both sides, verified 2026-09-08). WIP caps below evaluate against THIS store
  and THIS store only (no separate-universe gating — the pre-landing split is over).
  Pre-landing state: the 12-topic Win source had 244 `new` and TODAY violates the §5 WIP
  gate — no landings until the backlog burn-down (below) brings the
  landing topic ≤20 (the VAULT POLICY per-topic cap) or a per-batch JIT-override is signed.
  Dedupe targets (claim-overlap, verified): `fbd-statics`/`static-equilibrium`/`fbd-draw`
  (statics equilibrium phrasing across mech topics — ONE `static-equilibrium` node exists,
  no literal ×2) + Japanese verb cluster (7 nodes: `jp-verb-groups`, `jp-masu-polite`,
  `jp-plain-past`, `jp-te-form`, `jp-te-progressive`, `jp-te-requests`, `jp-te-linking`).
  `kind` absent on 34 nodes (recounted 2026-09-08: 13 per-topic `capstone`s with null kind +
  21 others — recount method PINNED: count of nodes where the `kind` key is missing or null;
  re-count at build, never trust this number; absent ⇒ `concept` per architect — caveat: absent +
  `arbitrary:true` ⇒ `fact`; audit content, only true fresh-instance procedures earn
  `procedure` + `practice` frames with engine-native `problem_frame` + `verify` +
  `error_bank` (+ `discriminates_from`, which IS engine-documented/preserved/due-carried
  but only individually unvalidated — sole presence-check is `problem_frame`; prefer
  `contrasts_with` edges for confusable pairs, which carry hygiene filtering).
  Commitment cue (per `learner-model.json`: cue "lunch or the afternoon tomorrow",
  action "clear the engram reviews"): OFFER an event anchor once (VAULT POLICY frequency — exactly
  one offer per close, never repeated unasked) at `/learn` close
  (`/coach` only if a renewal is due — interval ARBITRARY) and store the verbatim answer
  (never force-rewrite). `artifact` null except the two landed explorables — keep it so; vault
  linkage lives in the registry Evidence-tag + `Goal era` columns and session-log
  lines (see the §3 `Requires:` format paragraph and the §5 "Language-project loop"
  paragraph).
- Engine facts this plan respects (NOT negotiable): node kinds are `concept|procedure|fact`
  ONLY (no `kind:transfer` on nodes); capstone = engine-minted `{capstone:true,
  transfer_probe:None}` with receipt `kind:transfer` (metrics never pooled; successful
  transfer MAY strengthen scheduling); `why_chain` = derives-from id path by CONVENTION
  ONLY (engine neither validates nor walks it — say so, never rely on it; no step-count
  or shape claims about it); cross-topic
  `requires` is unsupported (prerequisites live in ONE canonical topic +
  `analogous_to` links — `analogous_to` itself has ZERO engine hits: vault convention,
  not engine field); pretests diagnose the frontier (never land over an
  undiagnosed frontier); probe↔rubric are one object (co-located claim + check — no structural
  claims beyond co-location).
- Foundation rule after this phase: bare minimum every goal needs. Projects: ≥1 skill each
  (VAULT POLICY coverage rule — every project confers at least one registry skill).

## 1. GOAL.md — single goal source (scaffold FIRST, parameterize after confirm)
(ABSENT — `Mechatronics/GOAL.md` + `Mechatronics/goals/parked/` do not exist; created here.)

Two passes (sequencing economics — do NOT front-load the ~118-line rewrite ahead of
GOAL-confirm): pass 1 scaffolds (`GOAL.md` draft + `goals/parked/` dir + registry
SKELETON — `Mechatronics/skills/registry.md` with schema header + `Goal era` column, zero
rows — owned by THIS task, so §3 fills an existing file); pass 2 (post-confirm) does the mass parameterization below.

- Create `Mechatronics/GOAL.md` (ABSENT — created here): active goal ONLY — name, actuator type, DOF, work
  envelope, success criteria, parked-history pointer, AND the semantic-pass checklist
  (seed = the canonical pattern list in §0 plus generic `arm|actuator` review; the §1
  task finalizes it as it rewrites). Today: QDD 2-DOF arm.
- Parked goals: `Mechatronics/goals/parked/<kebab-goal-slug>.md` (ABSENT — created here):
  file = old `GOAL.md` content verbatim + frontmatter `superseded: <YYYY-MM-DD>`; the date
  lives in frontmatter (body untouched).
- Goal change = replace GOAL.md + park old + re-derive Phase 3–5 artifacts AND flagged
  upstream goal-flavored examples (`Mechatronics/milestones/01_signals_actuators_dynamics.md:518`
  rig reuse, `Mechatronics/milestones/02_embedded_realtime_control.md:60,77,356-368` 2-DOF model,
  `Mechatronics/milestones/05_portfolio_delivery.md:13` QDD pedestal, ROADMAP Feeds-into claims).
- Skills persist: registry rows keep `Evidence tag` + `Goal era` column (§3); pre-swap rows
  BACKFILLED (acceptance audit: `awk -F'|' 'NR>4 && $5 ~ /^[[:space:]]*$/ {c++} END {print c+0}' Mechatronics/skills/registry.md` (NR>4 skips title/header/separator/blank — header itself matches the empty-cell pattern)
  returns 0 empty cells — NR>2 skips header+separator, `$5` is the `Goal era` column; zero null `Goal era`); tags minted pre-swap stay valid history.
  Tag grammar (PINNED — one dialect everywhere): evidence tags match
  `^([a-z0-9]+(-[a-z0-9]+)*-)?m[0-9]+\.[0-9]+-(mvm|full)$` (post-swap tags carry the `<goal>-` prefix,
  e.g. `cnc-m3.1-mvm`, `qdd-arm-m3.1-mvm`; `m0.1-fullpass` grandfathered, never rewritten). `Goal era` format
  (gate-checked against the pinned era regex
  `^(pre-GOAL|[a-z0-9]+(-[a-z0-9]+)* \([0-9]{4}-[0-9]{2}(-[0-9]{4}-[0-9]{2}|-)?\))$` — HYPHEN form only,
  post-normalization (gate normalizes U+2013 → `-` FIRST, then matches; the regex itself never
  contains en-dashes): `pre-GOAL`, or `<slug> (<YYYY-MM>[-<YYYY-MM>]?[-]?)` — trailing-dash open ranges
  (`qdd-arm (2026-08-)`, Win-keyboard form) are legal; with `<slug>` pinned in GOAL.md
  (today `qdd-arm (2026-08-)`); typists use hyphen-minus, never en-dash U+2013.
  Conformance examples (gate must accept: `pre-GOAL`, `qdd-arm (2026-08)`, `qdd-arm (2026-08-)`,
  `qdd-arm (2026-08-2026-12)`; must reject: `QDD (2026-08)`). No tag retire rule.
- Parameterization tasks (mandatory): `Mechatronics/resources/CONVENTIONS.md` arm frame defaults → goal parameters;
  0.2/0.4/0.7 arm-flavored procedures reworded goal-neutral OR GOAL.md-listed appendices;
  `Science/` + `DataScience/` arm assumptions → `See [[Mechatronics/GOAL]]` pointers;
  `LAB_INFRASTRUCTURE.md` + `IDEAS.md` + `hardware/inventory.md` goal mentions get per-file
  disposition (parameterize / move to parked-goal appendix / delete with log line).
- Goal-era vocabulary: `pre-GOAL` (before GOAL.md existed) or `<goal-slug> (<date range>)`
  per the pinned grammar above (slug + range pinned in GOAL.md itself).
- Acceptance: canonical pattern over `Mechatronics/ Science/ DataScience/` returns ONLY
  `GOAL.md`, `Mechatronics/goals/parked/*`, Phase 3–5 milestone files, and GOAL.md-listed appendices —
  PLUS the semantic pass completed per the GOAL.md checklist.

## 2. Foundation split — Phase-0 pilot ONLY (phases 1–3 stay unsplit)

Target (split the file — `git mv` moves whole files, so: copy each span to its new path
with `git add`, keep bodies verbatim — plus explicit link-migration per moved file — cut map
with VERIFIED line spans of `Mechatronics/milestones/00_foundations.md` (599 lines):
title+Outcome+Pass Condition 1–49 EXCEPT lines 25–46 (owned by `lab/`, pointer left behind);
0.1 → 50–96; 0.2 → 97–133; 0.3 → 134–167;
0.4 → 168–208; 0.5 → 209–246; 0.6 → 247–285; 0.7 → 286–359; 0.8 → 360–424;
0.9 → 425–515; 0.10 → 516–577 (content ends 575, blanks 576–577; separator 578, header at 580); Deload 578–599.
Split rule: builder runs `grep -nE "^#+ (Phase 0|Milestone 0)"` and diffs FULL output against
this pinned expectation (13 lines — title + 10 milestones + Deload + Retro; Retro moves with
lab per the cut map, nothing stays put except the redirect index):
`2:# Phase 0 — Foundations & Vocabulary`, `50:## Milestone 0.1 — Problem-Solving Framework + Toolchain`,
`97:# Milestone 0.2 — Vectors, Trig, Frames of Reference`, `134:# Milestone 0.3 — Calculus Intuition`,
`168:# Milestone 0.4 — Statics + Free Body Diagrams`, `209:# Milestone 0.5 — Circuits Basics`,
`247:# Milestone 0.6 — Power, Efficiency, Thermal`, `286:# Milestone 0.7 — Materials, Failure, and Selection`,
`360:# Milestone 0.8 — Manufacturing Processes + DFMA`, `425:# Milestone 0.9 — Mechanisms & Kinematic Elements + Physical Testbed`,
`516:# Milestone 0.10 — Metrology + Measurement Uncertainty`, `580:# Phase 0 Deload / Synthesis`,
`594:## Phase 0 Retro`. Rationale pinned: bare `^# ` yields 11 (misses 0.1's `##`);
bare `^#+ ` yields 62 (all subheads) — both wrong, hence expected-output diff (spans re-verified
at build, never trusted from this map). Output filenames follow the scheme
`<dir>/0.N-<kebab-from-section-heading>.md` (slugs derived at build from the section
headings above by PINNED algorithm — FIRST strip everything through the first ` — `
(em-dash), i.e. drop the `Milestone 0.N` prefix; THEN lowercase, `[^a-z0-9]+` → single
hyphen, strip leading/trailing hyphens; e.g. `# Milestone 0.2 — Vectors, Trig, Frames of
Reference` → `vectors-trig-frames-of-reference` — no invented names, two executors emit
identical paths; emitted paths must match `^[a-z0-9-]+$` per path segment (builder asserts,
aborts otherwise); each new dir gets a `README.md` index.
`00_foundations.md` itself becomes a redirect index (no checkboxes — evidence backlinks
keep resolving; retains lines 1–24 + 47–49 plus pointers to every split file; lab owns 25–46
and 578–599 INCLUDING Retro :594–599 — Retro moves with the Deload block, nothing stays put
except the redirect index). Pre-move READMEs (exact list — `Mechatronics/firmware/README.md`,
`Mechatronics/firmware/esp32/README.md`, `Mechatronics/firmware/stm32/README.md`,
`Mechatronics/simulations/python/README.md`, `Mechatronics/simulations/ltspice/README.md`;
NO top-level `Mechatronics/simulations/README.md` exists),
`requirements.txt` (`Mechatronics/simulations/python/requirements.txt` — the only one),
`template_*.py` (`Mechatronics/simulations/python/template_plot_csv.py`,
`Mechatronics/simulations/python/template_simulation.py`) — each gets: merge as dir
index / move with redirect header / delete-with-log-line, per-file choice listed in the
build commit. Redirect header format (PINNED): `# Moved -> [[<target>]] (<date>, <reason>)` (ASCII hyphens-minus only — never U+2192).
Log destination for every deletion/move: `Changelog/` entry + build commit message.
Single exception: Daily history links rot by design (immutable Daily files, no redirects).
Dir column is relative to `Mechatronics/` (e.g. `software/` = `Mechatronics/software/`).
File-wide: all vault paths in this file are repo-root-relative unless the sentence says
otherwise (table Dir column = relative to `Mechatronics/`):

| Dir | Milestones | Owns |
|---|---|---|
| `math/` | 0.2, 0.3 | applied math + FK hand-calcs |
| `physics/` | 0.4 WHOLE (no bisection — hand-calc→FEA chain stays atomic) | statics + FBD + FEM intuition |
| `mechanical/` | 0.7, 0.8, 0.9 (+ pointer to 0.4 FEM, not a copy) | materials, DFMA, mechanisms+testbed |
| `electronics/` | 0.5, 0.6 | circuits, power/thermal |
| `software/` | 0.1 (+ `Mechatronics/firmware/` → `Mechatronics/software/firmware/<board>/<project>/`,
  `Mechatronics/simulations/` → `Mechatronics/software/simulations/<backend>/`) | toolchain + executable surface |
  Firmware-parent rule (decided — the two schemes above collide otherwise): board-specific code
  lives at `software/firmware/<board>/<project>/`; board-agnostic projects live directly at
  `software/<kebab-project>/`. One rule, no per-board top-level dirs.
| `lab/` | 0.10 (516–577) + Phase-0 Pass/Deload (lines 25–46 and 578–599 of `Mechatronics/milestones/00_foundations.md` at time of writing — 578–599 covers photo, `versions.sh`, Retro) + SAFETY_CARD + CONVENTIONS + inventory refs | metrology + shared discipline |

Structural fixes (all mandatory; numbered for reference — execution follows §7):

1. **Primacy:** ROADMAP table is the ONLY ✅. Domain `Index.md` files are links-only
   (≤7 link-target entries — VAULT POLICY cap, tables included (an ownership table's links count) — no status, no checkboxes). "Domain" = the three
   hub Indexes carrying navigation (`Mechatronics/Index.md`, `Science/Index.md`,
   `DataScience/Index.md`); counting unit = `[[link targets]]`. Includes trimming `Mechatronics/Index.md`
   (19 link targets today) with per-line dispositions in the build commit. Milestone bodies keep checkboxes with header:
   `Status lives in [[Mechatronics/ROADMAP|Roadmap]] — do not duplicate.`
   Rewrite `Mechatronics/ROADMAP.md:9-17` Completion & Evidence text (pinned replacement):
   `1. Pass the gate: bash scripts/milestone.sh --dry-run <tag> "<msg>" is green.
   2. Tag: bash scripts/milestone.sh <tag> "<msg>". The tag is the durable evidence.
   3. Mark ✅ in the ROADMAP table only, then bash scripts/save.sh "roadmap: mark <tag>."`
   STAGED: this rewrite lands ONLY after §4 ships `--dry-run` (until then the
   documented command fails — build §4 first, swap text second). Doc==script owner:
   the §4 BUILDER (default whoever implements — reassigned from Mac-only by the Win
   authority transfer; preconditions: `ruff`, `clang-tidy`, `julia` present on the build machine
   + SSH signing key for `git tag -s` — verify before starting); the pinned doc text governs,
   the script implements it.
   Fix `scripts/milestone.sh` echo to the same text; add domain commit scopes (`math:`,
   `physics:`, …) to `Mechatronics/resources/CONVENTIONS.md` (bare `phaseN:` deprecated for domain work; old tags untouched).
   Pinned scope vocabulary: `math:`, `physics:`, `mechanical:`, `electronics:`, `software:`, `lab:`
   for domain work, `vault:` for cross-cutting changes (no other scopes without amendment).
2. **Anchors:** every milestone gets `<a id="m0-N"></a>` (`m0-1`…`m0-10` — resolvers match
   full IDs, never prefixes, since `m0-1` prefixes `m0-10`; scope = Phase-0 pilot milestones only); ROADMAP + all new notes link
   `#m0-N` only. Numbered for reference only — execution follows §7, NOT this item order.
   EXEMPT entries (format PINNED: `# EXEMPT <check>: <target> - <reason> - expires <YYYY-MM-DD>`
   — HYPHEN form (split rule: split on ` - expires ` last for the date, then on the first `: `
   after `# EXEMPT ` for check vs rest); pre-existing em-dash entries grandfathered until expiry,
   then rewritten in hyphen form; the builder creates entries with expiry (never open-ended;
   the gate FAILS on expired EXEMPT entries — expiry is enforcement, not decoration)
   and verifies with `grep -nE '^# EXEMPT [a-z]+:' scripts/diagnose.py` (`-E` REQUIRED — BRE `+`
   is literal; lowercase-check-name + colon anchor matches entries like `# EXEMPT broken: …`
   and skips the prose header `# EXEMPT carried failures (…)` — verified live: entry matches,
   header doesn't; negative pinned: header must NOT match).
   Migration script rewrites the 37 ROADMAP milestone rows, records old targets as
   HTML comments `<!-- was: <old-link-target> -->` (whole-file sources are fine — today
   rows carry no `#fragment`, so `<old-link-target>` = the previous link target string;
   the 37-row count is re-verified pre-migration, never trusted from here;
   Daily history immutable — old links rot by design).
   `diagnose.py` extension spec: resolve `<a id="X">` definitions; accept link forms
   `[[File#X]]`, `(file.md#X)`, `#X` (same-file — definition-side lookup, not a skip);
   skip code fences AND HTML comments (migration `<!-- was: -->` old-links must not trip
   the checker); skill IDs (scanned on `Skills gained` lines — exact heading spelling,
   case-sensitive — plus `Requires:` lines, which must be the immediately-next non-blank
   line) validated against §3 regex immediately, PLUS registry membership once §3 is filled
   (membership check staged — pre-fill runs skip it with a warning, never fail); redirect headers matching the
   pinned format. Must pass clean. Checks covered by this extension (no item lands unverified):
   anchors, skill IDs + Requires adjacency, membership (staged), redirect format, Index link-cap
   (≤7 targets on the three hub Indexes), project README 6-heading shape, snippet-only-home
   (no sim dirs outside `software/simulations/`). Timing rule: the builder's own `diagnose.py` run is the
   check — full rescan per tag accepted; add incremental mode only if a run exceeds 60s
   (ARBITRARY threshold) and record timing.
3. **Evidence 2-home rule:** canonical = milestone-body checkboxes + git tag.
   Narrative sources live in the SPLIT files (0.2 body in `math/0.2-*.md`); 0.1's checkbox
   duplication is MERGED into its split body with a redirect header (per §2 redirect format).
   Daily notes reference status, never restate it.
4. **Mechatronics/software/ bounds:** one folder per PROJECT (VAULT POLICY cardinality — exactly one
   dir per project, no splits, no merges) at `Mechatronics/software/<kebab-project>/`
   (a PROJECT = work with its own README carrying the 6 headings + its own MVM/Full Pass pair;
   anything smaller is a snippet, no exceptions)
   with `README.md` carrying EXACTLY these 6 headings (VAULT POLICY fixed shape): `## Question`,
   `## Inputs/Outputs`, `## How to run`, `## Pinned commit`, `## Skills gained`,
   `## Pass` (MVM/Full Pass checkboxes + `Evidence:` lines — §4 item 2 grammar).
   Snippets (non-project, no status, no gates) live ONLY in
   `Mechatronics/software/_snippets/` (cap 20 files TOTAL across languages — VAULT POLICY cap;
   overflow forces a project or deletion). `Mechatronics/software/simulations/` (the moved home)
   is the only sim home — no other sim dirs. Per-project `.gitignore` for build output
   (pinned patterns: `__pycache__/`, `*.pyc`, `target/`, `node_modules/`, `*.o`, `*.class`,
   plus language-standard ignores — extend by amendment, never ad hoc). `Mechatronics/software/`
   is created by this task (it does not exist yet).
5. **Ownership table** (in `Science/Index.md` AND `DataScience/Index.md` — identical table,
   reciprocal links — ~5 lines): Science wins proofs; `math/`/`physics/`
   win worked procedures; `Mechatronics/resources/CONVENTIONS.md` wins frames/units — until §1 parameterizes the
   arm defaults into GOAL.md (tracked task). Reciprocal `[[links]]`.
6. **Keep** `Mechatronics/ROADMAP.md` at its path; `resources/` untouched EXCEPT
   `CONVENTIONS.md` (explicit tasks above — scopes + parameterization).

## 3. Skill registry — ≥1 skill per project, machine-checkable, scalable
(ABSENT — `Mechatronics/skills/` does not exist; created by this section.)

- Location: `Mechatronics/skills/registry.md` (mech+software skills; piano/japanese/data
  skills explicitly deferred — conferred via their domains' milestone files (MVM/Full pairs
  there), never the registry, until those domains onboard; item 3 resolves registry IDs only,
  milestone-file skill lines get format-checks only). Phase rows may carry `pN-complete`
  tags in `Evidence tag` (phase rows are EXEMPT from skill-ID/era checks — they aggregate milestones, confer nothing; the column accepts EITHER tag form — existence check tries both
   regexes; project rows list BOTH tags comma-separated `mvm-tag, full-tag`, each checked)
  regexes); milestone/project rows carry m-form tags. Deferred-domain (piano/japanese/data) milestone skill lines get format-checks ONLY until those domains onboard (resolution-against-registry deferred with the domains — never a mint-blocker for mech/software).
- Schema: `| Skill ID | Name | Evidence tag | Goal era | Project | Requires |`
  (registry CELLS: comma-separated prerequisite skill IDs, or EMPTY for true entry
  points — 0.1-level — only; a missing file-level `Requires:` line = blank = fail. The explicit
  literal `Requires: — (entry point)` lives in milestone/project FILES (gate normalizes
  em-dash U+2014 → `-` first, same typing rule — `Requires: - (entry point)` also passes),
  never in registry cells.)
- ID regex (gate-enforced): `^(sw|ee|mech|lab)-[a-z0-9-]+$`, PLUS the `sw-` language token
  is MANDATORY and gate-checked against the pinned token list (`c`, `py`, `cpp`, `jl`):
  every `sw-` ID matches `^sw-(c|py|cpp|jl)-[a-z0-9-]+$` (so `sw-foo` FAILS; language-agnostic
  skills take the closest token or propose a new token — new `sw-` language token needs
  NO amendment; new PREFIX needs a one-line registry-header amendment).
  `sw-c-…`, `sw-py-…`, `sw-cpp-…`, `sw-jl-…` (new `sw-` language token needs
  NO amendment; new PREFIX needs a one-line registry-header amendment). Shard to
  `Mechatronics/skills/<domain>.md` when data rows exceed 100 (VAULT POLICY scale rule) — `<domain>` ∈
  {`sw`, `ee`, `mech`, `lab`} (one shard per prefix); `registry.md` becomes the index
  (schema + shard list), rows move to shards, IDs never change on sharding.
- `Skills gained` format (gate-parseable — exact heading `## Skills gained`, case-sensitive —
  skill lines in dash form `- <id> - <name> (tag <tag>, Goal era <era>)` (ASCII hyphens —
  legacy `—`/`→` lines are normalized (em-dash U+2014 → `-`, `→` → `->`) then matched, never
  rejected for dashes alone; then matches extraction regex
  `^- ([a-z0-9]+(-[a-z0-9]+)*) - .*\(tag ([^,]+), Goal era (.+)\)$` — one skill per line
  under the heading (VAULT POLICY cardinality)):
  `- sw-py-csv-plot - CSV to PlotJuggler (tag m1.1-mvm, Goal era qdd-arm (2026-08-))`
  (`Evidence tag` column holds TAGS matching the pinned tag regex; `Evidence:` lines hold
  PATHS — different grammars, both required where specified.)
  File-level rule (registry CELLS are separate: comma-separated IDs, or empty for entry points only):
  `Requires:` line (ONE per `Skills gained` block — VAULT POLICY cardinality — immediately-next non-blank line after the
  block's LAST skill line — per-block, not per-skill) directly below (same heading, gate-parseable):
  `Requires: sw-py-venv, sw-py-uncertainty-mean` (or `Requires: — (entry point)`).
- Foundation milestones declare their bare-minimum skill sets in the same registry
  (evidence = milestone tags). Registry answers "what can I do, proven by what".

### Skill-order audit — the vault must confer skills in a reasonable order (§3, part 2)

The agent checks curriculum sequence (at every landing + quarterly re-run — VAULT POLICY cadence):

1. **Requires closure:** every registry row's `Requires` IDs resolve in the registry
   (no dangling prerequisites, no forward references to unconferred skills).
2. **Date order:** every prerequisite's evidence tag predates (or equals) the
   claimant's evidence date — pre-mint, the claimant's date is its attest-note date (the tag
   doesn't exist yet); post-mint, `audit-tags.sh` re-verifies against taggerdates.
   Compare TAGGER dates with `git for-each-ref
   --format='%(taggerdate:iso)' refs/tags/<tag>` (`git log --format=%cI` answers committer
   date, which re-sign preserves by design — wrong clock; `%(taggerdate:…)` is a
   for-each-ref field, NOT a `git log` pretty-format — the literal never varies, so a
   `git log` spelling can never trigger refusal). Lightweight tags have empty taggerdate → gate REFUSES them (require
   annotated+signed). `m0.1-fullpass` naming drift grandfathered, never rewritten.
   Pre-gate tags (`m0.1-fullpass`, `m0.2-mvm`, `m0.2-full`) carry `-unaudited`
   registry notes until re-earned under the gate (they will flag on day one with
   zero gate receipts — expected, not a defect). Machine-checked in §4 item 3.
3. **Use-before-conferred scan:** walk the learner path Phase 0→1→2→3; for each
   milestone MVM checkbox that *uses* a skill (e.g. M1.2 "FFT computed in Python"),
   the conferring milestone/project must come earlier in the walk. Flag inversions
   (e.g. a Phase-1 checkbox needing a Phase-2 skill) as blocking defects.
4. **Foundation-first rule:** no project may require a skill conferred only by a LATER
   phase; cross-phase requirements must be satisfied by foundation (§2) or an earlier
   project. Quarterly audit (VAULT POLICY cadence) re-runs the full walk with cold free recall first
   (never rewatch/reread before the probe — same rule as dues); exit rule: exit 0 = zero UNRECORDED
   inversions — every finding has a `Changelog/` + build-commit defect entry; unrecorded
   finding = fail; a new milestone/project with an order violation fails the gate even if all other checks pass.

## 4. Machine-gated `milestone.sh` (foolproof — refusal + audit, no silent bypass)

Invocation: `bash scripts/milestone.sh <tag> "<msg>"`; dry run:
`bash scripts/milestone.sh --dry-run <tag> "<msg>"` (flag first, tags nothing).
On success the script MUST write `scripts/tests/receipts/<tag>.json`
(checks run + versions + result — schema PINNED: `{"tag": str, "checks": [{"name": str,
"result": "pass"|"fail", "detail": str}], "versions": {tool: version}, "result": "pass"|"fail"}`)
— the file `audit-tags.sh` consumes (match rule: receipt exists + `result == "pass"`;
exit 0 lists clean, exit 1 prints missing/failing tags, one per line).
Touched files = staged + unstaged + untracked working-tree files for `--dry-run`
(`git status --short --untracked-files=all` — `??` lines count as touched); the mint run checks the SAME set (working tree as it stands pre-tag).
For audits, the tag's commit range = commits reachable from the tag
excluding those reachable from the previous taggerdate-ordered tag. Pinned procedure
(the check runs BEFORE the tag is minted, so the range ends at HEAD): list
`git for-each-ref --sort=-taggerdate --format='%(refname:short)' refs/tags` (newest first),
keep ONLY tags with `git merge-base --is-ancestor <tag> HEAD` true (topology guard — tags from
other lineages never enter the range) AND non-empty taggerdate (lightweight tags excluded —
empty dates sort undefined, never silently become `<prev>`), take the FIRST such tag (newest HEAD-ancestor by taggerdate)
as `<prev>`; then `git log <prev>..HEAD --oneline` is the range (no previous tag =
range is HEAD's full history). Post-mint audit form (tags exist by then, pinned separately):
`git log <prev-tag>..<tag> --oneline` with both tags resolved via `for-each-ref`. After green,
mint the tag, then record the post-mint form for the audit record.
Tagging REFUSES (non-zero exit + reason) unless ALL pass (items 0–5 refuse AT MINT time;
item 6 is the monthly detective audit, not a mint gate — it runs on schedule regardless):

0. Tag format: `<tag>` matches the pinned tag regex `^([a-z0-9]+(-[a-z0-9]+)*-)?m[0-9]+\.[0-9]+-(mvm|full)$`
   OR `^p[0-9]+-complete$` (phase gates, e.g. `p0-complete`; multi-digit phases covered), OR is on the pinned grandfather list
   (`m0.1-fullpass` — the only entry; never extended without a registry-header-style amendment).
   Order: mint annotated+signed FIRST (`git tag -s -a`), THEN `git tag -v <tag>` must verify
   (lightweight tags fail here too) — on verify-fail, delete the tag and refuse the receipt
   (mint-then-verify; pre-mint `tag -v` is impossible since the tag doesn't exist yet; on ANY item 0-5 failure post-mint, delete the tag and refuse the receipt — no stray tags ever).

1. Build+lint table (pinned in the script; CODE extensions = `py|c|h|cpp|hpp|jl|sh` with rows:
   `py` → `ruff check` + `ruff format --check`; `c/h/cpp/hpp` → `clang-tidy`; `sh` → `bash -n`;
   `jl` → JuliaFormatter-or-parse (rule below);
   `.md` handled by the diagnose check in item 4 — NOT by this table; data/binary formats
   (`json|csv|png|svg|step|toml|txt|…`) get existence-checks only; extensionless files and
   dotfiles (`.gitignore`, `.JuliaFormatter.toml`) get existence-checks only, same class; anything else
   (incl. `js|ts`) MUST add its row before its first tag — gate FAILS CLOSED on unlisted extensions):
   `jl` → `JuliaFormatter` if `.JuliaFormatter.toml` (or `[JuliaFormatter]` in
   `Project.toml`) exists in the project root (the touched file's `software/<project>/`
   dir, else repo root), else FULL-FILE syntax parse (requirement: every expression must parse;
   `Meta.parse`-first-expression-only is a KNOWN false-green, never the gate; the implementer
   pins whatever passes (candidate one-liner `julia -e 'for f in ARGS; Meta.parseall(read(f,String)); end' <files>` — implementer proves multi-expression behavior on a fixture file with a trailing syntax error at build).
   A 5th language MUST add its row before its first tag.
2. Artifacts: `Evidence:` lines (dash form `- Evidence: <path>` — migration rewrites the
   legacy `> Evidence: [[wikilink]]` form to dash form; worked example (dash form, copy-pasteable):
   `- Evidence: Mechatronics/docs/captures/2026-09-07_hbridge-loss.png`;
   scope ends at the next `##` heading or EOF (`###` subsections do NOT terminate — they belong
   to their parent `## Pass` section); zero `Evidence:` lines under a Pass
   heading = FAIL (vacuous never passes); one per line, repo-relative path, living under the
   README `## Pass` heading or milestone `## Pass Condition`), e.g.
   `- Evidence: Mechatronics/docs/captures/2026-09-07_hbridge-loss.png`
   Every listed path exists on disk. Freeform checkboxes are NOT parsed.
3. Skills: every tagged file carries a `## Skills gained` line with COUNT ≥ 1 (VAULT POLICY coverage gate — same
   rule as §1, enforced here — per-FILE scope: each file under tag must contain ≥1 skill line), plus a `Requires:` line
   (entry-point form allowed, blank forbidden); every ID matches §3 regex AND resolves
   in the registry; every registry row touched has non-null `Goal era` matching the era
   format (`pre-GOAL` or the pinned `<slug> (<range>)` — format-checked, not just non-null)
   and its Evidence-tag value exists as a minted tag, OR equals the tag being minted
   (first-mint carve-out — a row's Evidence tag may be the tag under mint; post-mint,
   the monthly audit re-verifies existence via receipts AND re-runs the §3 taggerdate comparison
   with `git for-each-ref` (dates exist by then); item 3 invokes the §3 rule by reference
   rather than restating); every prerequisite taggerdate ≤ claimant taggerdate (§3 skill-order audit).
4. Links+lenses: extended `diagnose.py` (§2 item 2 spec) clean on touched files, INCLUDING
   the lens rule — any touched milestone MISSING its lens block, or any `status: proposed`
   lens in one, fails the gate (checked inside `diagnose.py`, not by hand; skill IDs are
   scanned on `Skills gained` + `Requires:` lines; lens blocks parsed on the exact header
   `Lenses - m0-N` — N = the milestone number of the enclosing section (matches its `<a id>` anchor);
   lens blocks THEMSELVES are exempt from lens-presence (they ARE the lens — no bootstrap paradox);
   verbatim MOVES (content unchanged — verified mechanically: builder diffs
   each moved file against its source span IGNORING redirect-header lines,
   `diff <(sed '/^# Moved -> /d' newfile) <(sed -n '<start>,<end>p' oldfile)` must be empty (spans from the cut map above))
   are EXEMPT from lens-presence
   (new/edited content is not).
5. Attestation: dated blank-page test note, e.g.
   `Mechatronics/math/0.2-attest-2026-09-07.md`
   (`<domain>/0.N-attest-<date>.md`, domain = split dir owning the milestone (Phase 0);
   for unsplit Phases 1–3: `Mechatronics/milestones/<file-stem>-attest-<date>.md`, e.g.
   `01_signals_actuators_dynamics-attest-2026-09-07.md`; for software projects:
   `<project>/attest-<date>.md`; `<date>` = YYYY-MM-DD):
   re-solve from memory with NO reread/rewatch before solving (cold-recall-first);
   gaps red-penned; Full Pass note MUST carry the pinned line `Prior attempt: <YYYY-MM-DD|tag>`
   (VAULT POLICY: same-day echo fails the gate — enforces spacing; the gate parses exactly this
   line; compared via taggerdate where tags exist,
   note dates otherwise — all dates compared as YYYY-MM-DD strings (taggerdates truncated
   to first 10 chars); red-pen gaps appended to
   `_system/Landmine Log.md`, or linked from the attest note to an existing vault file
   (endpoint pinned: Landmine Log or vault-file link — no bare text).
6. Direct-`git-tag` bypass is detectable, not preventable: monthly (VAULT POLICY cadence)
   `bash scripts/audit-tags.sh` (ABSENT — created here: lists tags lacking gate receipts in
   `scripts/tests/receipts/<tag>.json`, exit 1 printing one per line, exit 0 when clean;
   gate-ship date (pinned at §4 landing in `Changelog/` as `Gate shipped: <YYYY-MM-DD>`) divides
   pre-gate tags (expected `-unaudited`, not defects) from post-gate tags (must have receipts);
   on each run it ALSO re-runs the §3 taggerdate comparison for all registry rows)
   + agent rule — never attest a bypassed tag;
   bypassed tags get `-unaudited` registry note until re-earned.

Gate ships with fixtures at `scripts/tests/fixtures/refusal-{0..7}/` + `scripts/tests/fixtures/clean/`
(brace form PINNED — `{refusal-0..7,clean}` expands wrong; ABSENT — created by this section).
Mapping (explicit table — 8 refusals + clean = 9/9): refusal-0 → item 0 (tag-format);
refusal-1 → item 1 (lint); refusal-2 → item 2 (artifacts); refusal-3 → item 3 (skills);
refusal-4 → item 4 (links+lenses); refusal-5 → item 5 (attest); refusal-6 → item 6 DETECTIVE
control `audit-tags.sh` (harness creates an annotated fixture tag named `fixture/bypass-N`
in a temp CLONE — never a shared worktree — runs the audit, expects exit 1 listing it,
then deletes the clone); refusal-7 → item-3 sub-check, skill-order violation with prerequisite
taggerdate after claimant, backdated via `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` env in a temp
CLONE (same isolation — shared worktrees share refs; fixture tags named `fixture/order-a` +
`fixture/order-b` with fixed dates `2026-01-02`/`2026-01-03`), run by
`bash scripts/test-gate.sh` (ABSENT — created here) expecting 9/9 (exit 0 on 9/9, else 1). 9/9 or red. Fixture layout:
each `refusal-N/` holds input files + `expected-exit` (single int) + `expected-stdout-fragment`
+ `expected-stderr-fragment` (both substring matches); `clean/`
holds passing inputs. Skill-checking fixtures share one `fixtures/registry.md` (single shared fixture registry, no per-fixture copies); the harness selects registries via env `SKILL_REGISTRY=<path>` (default: the real registry). Harness isolation (pinned pseudo-code — implementer writes the trap): make temp dir, `git clone` the vault `file://` URL into it, run the gate there, delete the dir even on failure.

## 5. Engram topics — engine-native WIP, JIT-cut, capstone-only builds

GATE (satisfied 2026-09-08 — proposal landed to main + ENGINE_PIN green, engine sha FULL
match both sides): landings proceed under the WIP caps below, evaluated against the LANDED
13-topic store. Pre-landing backlog burn-down (remediation, NOT a landing — no approval needed):
dedupe via `analogous_to`-convention/`retire` + `doctor` until `new` approaches cap, plus capped
review sittings (`due --cap 12`); whatever remains above cap needs per-batch JIT-override
(logged, user-signed) — no standing overrides. Doctor-gating rule: preconditions run with
`$ENGRAM_RUNNER doctor` on the machine doing the landing, sha recorded alongside results.

Preconditions (before ANY landing):

1. `doctor` JSON `probe_gaps` field empty on touched topics (`doctor` takes no subcommand —
   read the field from its JSON output); scope approval covers pretest plan, node
   kinds, `practice` frames, contrast/viz/interactivity needs.
2. Dedupe via `analogous_to`-convention/`retire` + `doctor` (NOT keyword diff): the §0
   statics trio + Japanese verb cluster (IDs pinned in §0). Overlap check (exact-id + claim read) joins every
   scope approval.
3. Kind audit: absent ⇒ concept (no blind backfill); true fresh-instance procedures earn
   `procedure` + `practice` frame with engine-native `problem_frame` + `verify` +
   `error_bank` (+ `discriminates_from` allowed — engine-documented and due-carried, only
   individually unvalidated; `contrasts_with` preferred for confusable pairs; gate WARNS
   on missing discrimination info, never fails — "execution key" is no field, never require it).
   Counts include capstones (this VAULT POLICY coverage rule counts capstones inside `new` —
   say capstone count in reports).

WIP policy (VAULT POLICY, not engine law — the engine permits new work with dues
outstanding; this policy trades speed for habit protection, overrideable):

- Default refuse landing while `due --cap 12` returns a full page (`n` = 12 means "12 or
  more" — the capped query cannot distinguish; proceed only on `n` < 12, strictly fewer),
  or the landing topic's own `states.new` > 20 (`12` = engine STANDARD_CAP
  (`engram.py:1241` — source-cited engine constant, not vault dosage); `20` = VAULT POLICY,
  ARBITRARY cap per landing topic; capstones count inside `new` — no exclusion arithmetic). No global-`new` gate (the
  258-`new` backlog burns down via the pre-step below, not via landing refusal).
- Escape hatch (logged in the scope note's `Override:` field + user-sign line, per batch —
  no standing overrides): JIT-override after reviewing the due list —
  allowed ONLY for scope-approved JIT nodes (§5 landings). Standing override = fail.
- Backlog-clear pre-step (before first landing): capped review sittings
  (`due --cap 12`, cold free recall first — never rewatch/reread before the probe;
  amnesty-first as session-start sensibility — `RETURN_ABSENCE_DAYS=7`
  is engine prose, not a command; the plan treats the `7` as ARBITRARY) until `due --cap 12`
  returns `n` < 12 (strictly fewer — same rule as the landing gate) or JIT-override signed.
  Burn-down for `new`: dedupe via `analogous_to`-convention/`retire` + `doctor`
  (remediation step — every retire logged in `Changelog/` + commit; counts toward the landing-topic ≤20 cap above) — 258 `new` across
  13 topics as of 2026-09-08, tracked per-topic in the build note. Burn-down EXITS (all required
  for first landing): landing topic ≤20 AND `due --cap 12` returns `n` < 12, OR a per-batch
  JIT-override is signed (same override form as landings).
- Soft alarm at 150 active (`active` = `topics` states review+learning+`new` summed, all topics):
  ARBITRARY, review-or-retire session due by 2026-12.

Landings (scope approval each; pretests/maps land maps-only — builds are the STATED
exception and land ONLY as topic capstones, never as parallel vault structure):

- **Now (JIT, each node tied to a NAMED MVM checkbox — recorded in the scope-approval
  note `.opencode/plan/scope-<topic>-<date>.md` (`<date>` = YYYY-MM-DD; pinned path/format:
  topic, node list with target checkboxes, pretest plan, WIP counts — `due --cap 12` n +
  per-topic `new` from `topics` — at approval; `Override:` field + user-sign line when used), NOT in `why_chain`, which stays
  an id-path; per-item kind: procedures land as NODES, builds land as CAPSTONES):** py CSV→PlotJuggler plot (M1.1, nodes),
  FFT+windowing (M1.2, nodes), `solve_ivp` pendulum (M1.4, nodes); C ring buffer + versioned telemetry
  framing (M1.5/M1.1, capstones). Parked until the demanding milestone is ACTIVE (ACTIVE =
  the milestone named in the latest Daily note's `- **Target:**` line (exact field spelling —
  singular `Target`, not the template's plural `Targets:`; newest Daily FILE by date, never
  `Daily/Index.md`; value names the milestone by id or title),
  fallback = earliest ⬜ in the ROADMAP table; ✅✅ = MVM tag + Full tag both minted): packaging, OOP,
  CMake lore, FK-visualizer rebuild (M0.2 tags minted; the rebuild itself is parked work, NOT done —
  no shipped-build claim: no file, Daily, or tag evidences a visualizer artifact).
- **Atomicity policy (VAULT POLICY, ARBITRARY — dosage, not finding):** one claim per node,
  5–15 min per node. Builds land ONLY as topic capstones
  (engine capstone semantics, receipt `kind:transfer`). Vault linkage = registry
  Evidence-tag + `Goal era` columns and session-log lines — NEVER `transfer_probe` text
  (stays None) or parallel checkboxes. Any node reviewable only by opening a README
  is malformed.
- **Language-project loop (§3 carve-out — VAULT POLICY: generation-first practice; applies to EVERY topic with builds, incl.
  future piano/japanese projects):** user writes the code/piece/text; AI reviews errors +
  best practices and NEVER writes the solution (scaffolds only — How-to-Learn Yellow zone).
  Each project carries its own MVM/Full Pass pair (in README `## Pass` for code, in the
  topic's milestone file for piano/japanese) with distinct evidence tags; the AI review
  note is filed as evidence and linked from `## Pass`.
- Later:** `cpp-foundations`, `julia-viz` (post-stabilization = `due --cap 12` returning `n` < 12 at two
  consecutive weekly checks — weekly cadence AND the count of two are both ARBITRARY;
  stabilization reviews run cold free recall first, same rule as dues; first stabilization review 2026-12,
  jointly with the 150-alarm review and quarterly audit — VAULT POLICY cadences), then
  `mech-software/electronics/mechanical` with `analogous_to` cross-links (cross-topic
  `requires` admitted unsupported).

## 6. Video-first lenses (VAULT POLICY section — every MUST/NEVER below is a vault sourcing
rule, not an empirical claim; authoritative, veto-gated, generation-first)

Resource-block format per milestone (pilot: Phase-0 files only; plain-text lines directly
under the per-milestone Resources callout — NOT a separate callout; `<milestone id>` dialect
PINNED to the anchor scheme `m0-N`, canonical first line `Lenses - m0-2` (HYPHEN form —
gate normalizes em-dash U+2014 → `-` first, then matches; typists use hyphen, never em-dash):

```
Lenses - <milestone id>
Rigorous: <title> | <creator> | <url> | <status: proposed|approved|waived>
Intuitive: <title> | <creator> | <url> | <status: proposed|approved|waived>
Interactive: <sim/bench>   Theory: <scoped book ch>   (existing content kept)
```
(copy-paste SAFE — hyphen-minus and pipes only, no em/en-dashes anywhere in this block;
fields split on ` | ` — titles containing pipes are forbidden, use ` - ` inside titles).

Rules: agent proposes exactly 2 (VAULT POLICY dosage: 1 rigorous + 1 intuitive, Veritasium/3Blue1Brown/
Efficient Engineer caliber; new domains calibrated with the user first — titles/creators/URLs
are USER inputs at approval time, the agent drafts candidates). Lens lifecycle (no deadlock):
propose (`proposed`) → user approves/replaces per topic (`approved`) or `waived` + reason →
ONLY then may a tag minting that topic's work pass the gate. User
approves/replaces per topic. **No approved pair → topic doesn't land**, with ONE explicit
escape: `waived` + reason logged in the lens block + `Changelog/` (affordance-none content — the
sole escape path, exactly ONE (VAULT POLICY count — no second waiver form exists)) — a user-signed decision,
never a default. AI-generated video is NEVER a lens (VAULT POLICY sourcing rule — no AI-channel
lenses, period); if proposed, drop it and chat directly.
Protocol per topic (generation-first — predict precedes the first watch turn; watch
NEVER comes before a prediction):
predict/commit → watch segment → self-explain aloud → blank-page reconstruction →
fresh-probe verify (probe → confidence pick → blind assessor → receipt) → project.
Fallback ladder (VAULT POLICY: when prediction fails twice — count ARBITRARY): scaffolded worked example → predict
again → verify; never lecture what derivation practice could reach. Authorship-verify
step: for any lens without an established educator, verify human authorship before
linking (no-established-educator cases logged). Explorable→rigorous rule: interactive explorables
illustrate the RIGOROUS lens (manipulables carry the formalism), never the intuition.
Veto-gate throughput: every JIT batch needs a signed pair-or-waiver — expect approval
clustering; batch approval per milestone is allowed (one user sign covers the pair list).
Fluency guard: "makes sense" counts as zero evidence (VAULT POLICY counting rule — we score it zero; no claim about mechanism). Congruence (VAULT POLICY grading rule — match probe modality to claim modality): verbal quiz for
verbal claims, execution/build probe for procedures (no incongruent grading).
(Enforcement of this section activates with Phase 2 — Phase-1 cites it as forward
pointer only.)

## 7. Sequencing + acceptance (STOP for user feedback — no further work unapproved)

Order (dependency-sorted — each step's inputs exist when it runs): §1-scaffold (GOAL draft
+ parked dir + registry SKELETON — `Mechatronics/skills/registry.md` with schema header,
zero rows — plus `Goal era` column, so later steps have a file to fill) → §1-pass-2a
(CONVENTIONS arm defaults → GOAL parameters ONLY — feeds the §2 ownership table; rest of
pass 2 stays deferred until after the split, operating on split paths) → §2-item-2
diagnose-extension (anchors + skill-ID regex checks; registry-MEMBERSHIP check staged on
§3 fill) → §4 gate build (fixtures are SELF-CONTAINED — fixture registry ships in
`fixtures/`, so 9/9 evaluates without the real §3 fill) → §2 split pilot +
Completion-text swap (STAGED on §4; verbatim moves are EXEMPT from the lens-presence check —
content unchanged — new/edited content requires lens blocks once §6 grammar exists) →
§3 registry fill → §1-pass-2 remainder (Science/DataScience pointers, LAB/IDEAS/inventory
dispositions, 0.2/0.4/0.7 reword — full mass parameterization, on split paths) →
§6 lens pairs (per-landing approval) → §5 landings. Item coverage: §2 items 1 (Primacy caps),
3 (evidence 2-home), 4 (software bounds), 5 (ownership table) all land inside the split pilot
(the pilot IS items 1–6); diagnose spec covers link caps + 6-heading shape + snippet-only-home
alongside anchors/IDs (extend §2 item 2 — no unverified landings).
Phase acceptance (ALL must hold, each mechanically checkable — shell pinned: git-bash/POSIX
for all greps below, PowerShell never): §1 grep-gate
(exact commands — counts: `grep -rEoh 'QDD|2-DOF|2DOF|2 DOF|2-link|Puck|backdrivab|quasi-direct|SendCutSend|gripper|lever-arm' Mechatronics/ Science/ DataScience/ | sort | uniq -c`;
files: `grep -rEl 'QDD|2-DOF|2DOF|2 DOF|2-link|Puck|backdrivab|quasi-direct|SendCutSend|gripper|lever-arm' Mechatronics/ Science/ DataScience/ | sort`
— the ONLY-files claim is checked against the filename output, never the `-h` counts;
  closure rule: any other hitting file not listed above gets a disposition task added to §1
  pass 2 before acceptance (no hitting file left homeless)) + GOAL.md `## Checklist` section
(exact heading spelling) exists and is filled — the section IS the record, no separate file — + semantic pass
recorded as per-item dispositions in that section (schema PINNED: `- [ ] <coupling> -> <disposition>`
(ASCII `->` accepted equally with `→` U+2192 — gate normalizes `→` to `->` first, same typing rule)
where disposition = `keep:<location>` | `parameterize` | `park:<slug>` | `delete+log`); anchor-aware
`diagnose.py` clean (or only `# EXEMPT`-block items — single authority: the plan format above
governs, the code block mirrors it; on ANY drift the code is updated same-commit, never the reverse;
pinned at
the top of `scripts/diagnose.py`, authoritative for carried failures); gate fixtures 9/9;
skill-order audit (§3 skill-order audit) clean on the current vault (pre-existing inversions
RECORDED in `Changelog/` + the build commit message — "filed as defects" means exactly that:
defect entries carry IDs `F-<nnn>` as `### F-<nnn> <title>` + a `Status:` line (open/fixed),
never bare prose — the audit matches findings to IDs, not waived); cold-start test (step 0: export `ENGRAM_RUNNER` + `ENGRAM_HOME` +
`PYTHONIOENCODING=utf-8` per `_system/engram/env.example.sh`; step 1: fresh session runs the AGENT.md session-start block
verbatim with zero errors AND `due --cap 12` returns the same `n` as the pre-test run the same
day — time-varying quantities compared same-day only (same-day window = ARBITRARY); both invocations logged in the test note
`.opencode/plan/cold-start-<date>.md`, pinned path); FRESH reviewer agents on the same three briefs (alignment,
neuroscience, extensibility+onboarding) report zero blocking verdicts, max 2 rounds (VAULT POLICY
bound) — leftovers go to the user for adjudication, the loop terminates. User adjudication = waiver RECORDED
in `Changelog/` as `Waiver: <finding-ID> — <reason> — <date>`; a waived finding satisfies its
gate item (waiver semantics pinned — adjudication is a verdict, not an open loop).
Reviewer briefs = the three names above
(alignment, neuroscience, extensibility+onboarding); verdicts recorded in `Changelog/` + the
build commit message.
