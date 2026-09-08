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
File:line citations are repo-root-relative paths + current line numbers (re-check: rot fast). Runner for all engram operations: `$ENGRAM_RUNNER` (per-machine env — Mac `python3 ~/engram/scripts/engram.py`, Win `python3 ~/.config/opencode/scripts/engram.py`; see `_system/engram/env.example.sh`. NEVER hardcode either path)
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
  the pattern misses): `Science/Index.md:14` (Puck + QDD Lorentz feed),
  `DataScience/Index.md:9,13` (QDD telemetry pipeline), `Mechatronics/resources/LAB_INFRASTRUCTURE.md`,
  `Mechatronics/IDEAS.md`, `Mechatronics/hardware/inventory.md`.
- Foundations are ALREADY goal-instantiated (0.2 FK arm tip, 0.4 arm FBD + holding
  torque, QDD torque-constant reference at 0.10 `:568`, 0.7 arm-link material,
  CONVENTIONS arm frame defaults (`Mechatronics/resources/CONVENTIONS.md:46-55`): §1 parameterization tasks are mandatory,
  not cosmetic (scaffold-first per §1 — mass parameterization deferred to pass 2).
- Engram (LANDED vault store — `_system/engram/`, 13 topics / 270 nodes / 258 `new` /
  0 repo receipts as of 2026-09-08; mark universe wherever counts gate anything):
  reconciled 340 HOLD / 14 PORT (`mech-spine`, Mac) / 0 DROP; resits ~zero (all Win
  receipts pre-divergence, Win nodes adopted in place). ENGINE_PIN green (engine sha
  FULL match both sides, verified 2026-09-08). WIP caps below evaluate against THIS store
  and THIS store only (no separate-universe gating — the pre-landing split is over).
  Pre-landing state: the 12-topic Win source had 244 `new` and TODAY violates the §5 WIP
  gate — no landings until the backlog burn-down (above) brings the
  landing topic ≤20 or a per-batch JIT-override is signed.
  Dedupe targets (claim-overlap, verified): `fbd-statics`/`static-equilibrium`/`fbd-draw`
  (statics equilibrium phrasing across mech topics — ONE `static-equilibrium` node exists,
  no literal ×2) + Japanese verb cluster (7 nodes: `jp-verb-groups`, `jp-masu-polite`,
  `jp-plain-past`, `jp-te-form`, `jp-te-progressive`, `jp-te-requests`, `jp-te-linking`).
  `kind` absent on 34 nodes (absent ⇒ `concept` per architect — caveat: absent +
  `arbitrary:true` ⇒ `fact`; audit content, only true fresh-instance procedures earn
  `procedure` + `practice` frames with engine-native `problem_frame` + `verify` +
  `error_bank`, plus `contrasts_with` edges for discrimination — `discriminates_from`
  appears only in a code comment nothing reads; "execution key" is no field).
  Commitment cue (per `learner-model.json`: cue "lunch or the afternoon tomorrow",
  action "clear the engram reviews"): OFFER an event anchor once at `/learn` close
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
- Parked goals: `Mechatronics/goals/parked/<kebab-goal-slug>.md`, verbatim + superseded date.
- Goal change = replace GOAL.md + park old + re-derive Phase 3–5 artifacts AND flagged
  upstream goal-flavored examples (`Mechatronics/milestones/01_signals_actuators_dynamics.md:518`
  rig reuse, `Mechatronics/milestones/02_embedded_realtime_control.md:60,77,356-368` 2-DOF model,
  `Mechatronics/milestones/05_portfolio_delivery.md:13` QDD pedestal, ROADMAP Feeds-into claims).
- Skills persist: registry rows keep `Evidence tag` + `Goal era` column (§3); pre-swap rows
  BACKFILLED (acceptance: zero null `Goal era`); tags minted pre-swap stay valid history.
  Tag grammar (PINNED — one dialect everywhere): evidence tags match
  `^([a-z0-9]+(-[a-z0-9]+)*-)?m[0-9]+\.[0-9]+-(mvm|full)$` (post-swap tags carry the `<goal>-` prefix,
  e.g. `cnc-m3.1-mvm`, `qdd-arm-m3.1-mvm`; `m0.1-fullpass` grandfathered, never rewritten). `Goal era` format
  (gate-checked): `pre-GOAL`, or `<slug> (<YYYY-MM>[–<YYYY-MM>])` with `<slug>` pinned in GOAL.md
  (today `qdd-arm (2026-08–)`); the dash may be hyphen-minus or en-dash U+2013 (gate normalizes
  U+2013 → `-` first — Win keyboards type hyphen). No tag retire rule.
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
0.9 → 425–515; 0.10 → 516–577 (body ends 577, `---` at 578); Deload 578–599. Output filenames follow the scheme
`<dir>/0.N-<kebab-from-section-heading>.md` (slugs derived at build from the section
headings above — no invented names); each new dir gets a `README.md` index.
`00_foundations.md` itself becomes a redirect index (no checkboxes — evidence backlinks
keep resolving). Pre-move READMEs (exact list — `Mechatronics/firmware/README.md`,
`firmware/esp32/README.md`, `firmware/stm32/README.md`,
`Mechatronics/simulations/python/README.md`, `Mechatronics/simulations/ltspice/README.md`;
NO top-level `Mechatronics/simulations/README.md` exists),
`requirements.txt` (`Mechatronics/simulations/python/requirements.txt` — the only one),
`template_*.py` (`Mechatronics/simulations/python/template_plot_csv.py`,
`template_simulation.py`) — each gets: merge as dir
index / move with redirect header / delete-with-log-line, per-file choice listed in the
build commit. Redirect header format (PINNED): `# Moved → [[<target>]] (<date>, <reason>)`.
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

Structural fixes (all mandatory, in this order):

1. **Primacy:** ROADMAP table is the ONLY ✅. Domain `Index.md` files are links-only
   (≤7 link-target entries — VAULT POLICY cap — no status, no checkboxes). "Domain" = the three
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
   Mac builds §4 (preconditions: `ruff`, `clang-tidy`, `julia` present on the build machine
   + SSH signing key for `git tag -s` — verify before starting); the pinned doc text governs,
   the script implements it.
   Fix `scripts/milestone.sh` echo to the same text; add domain commit scopes (`math:`,
   `physics:`, …) to `Mechatronics/resources/CONVENTIONS.md` (bare `phaseN:` deprecated for domain work; old tags untouched).
   Pinned scope vocabulary: `math:`, `physics:`, `mechanical:`, `electronics:`, `software:`, `lab:`
   for domain work, `vault:` for cross-cutting changes (no other scopes without amendment).
2. **Anchors:** every milestone gets `<a id="m0-N"></a>` (`m0-1`…`m0-10` — resolvers match
   full IDs, never prefixes, since `m0-1` prefixes `m0-10`); ROADMAP + all new notes link
   `#m0-N` only. Migration script rewrites the 37 ROADMAP milestone rows, records old slugs as
   HTML comments `<!-- was: <old> -->` (Daily history immutable — old links rot by design).
   `diagnose.py` extension spec: resolve `<a id="X">` definitions; accept link forms
   `[[File#X]]`, `(file.md#X)`, `#X` (same-file — definition-side lookup, not a skip);
   skip code fences; skill IDs (scanned on `Skills gained` lines — exact heading spelling,
   case-sensitive — plus `Requires:` lines, which must be the immediately-next non-blank
   line) validated against §3 regex immediately, PLUS registry membership once §3 is filled
   (membership check staged — pre-fill runs skip it with a warning, never fail); redirect headers matching the
   pinned format. Must pass clean. Timing rule: the builder's own `diagnose.py` run is the
   check — full rescan per tag accepted; add incremental mode only if a run exceeds 60s
   (ARBITRARY threshold) and record timing.
3. **Evidence 2-home rule:** canonical = milestone-body checkboxes + git tag.
   Narrative sources live in the SPLIT files (0.2 body in `math/0.2-*.md`); 0.1's checkbox
   duplication is MERGED into its split body with a redirect header (per §2 redirect format).
   Daily notes reference status, never restate it.
4. **Mechatronics/software/ bounds:** one folder per PROJECT at `Mechatronics/software/<kebab-project>/`
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
6. **Keep** `Mechatronics/ROADMAP.md` at its path; `resources/` untouched.

## 3. Skill registry — ≥1 skill per project, machine-checkable, scalable
(ABSENT — `Mechatronics/skills/` does not exist; created by this section.)

- Location: `Mechatronics/skills/registry.md` (mech+software skills; piano/japanese/data
  skills explicitly deferred, not homeless-by-accident).
- Schema: `| Skill ID | Name | Evidence tag | Goal era | Project | Requires |`
  (`Requires` = comma-separated prerequisite skill IDs, empty ONLY for true entry
  points — 0.1-level — with `Requires: — (entry point)` written explicitly; blank = fail.)
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
  one skill per line under the heading):
  `- sw-py-csv-plot — CSV→PlotJuggler (tag m1.1-mvm, Goal era qdd-arm (2026-08–))`
  (`Evidence tag` column holds TAGS matching the pinned tag regex; `Evidence:` lines hold
  PATHS — different grammars, both required where specified.)
  `Requires:` line (ONE per `Skills gained` block, immediately-next non-blank line after the
  block's LAST skill line — per-block, not per-skill) directly below (same heading, gate-parseable):
  `Requires: sw-py-venv, sw-py-uncertainty-mean` (or `Requires: — (entry point)`).
- Foundation milestones declare their bare-minimum skill sets in the same registry
  (evidence = milestone tags). Registry answers "what can I do, proven by what".

### Skill-order audit — the vault must confer skills in a reasonable order (§3, part 2)

The agent checks curriculum sequence (at every landing + quarterly re-run):

1. **Requires closure:** every registry row's `Requires` IDs resolve in the registry
   (no dangling prerequisites, no forward references to unconferred skills).
2. **Date order:** every prerequisite's evidence tag predates (or equals) the
   claimant's tag — compare TAGGER dates with `git for-each-ref
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
   project. Quarterly audit re-runs the full walk (exit rule: exit 0 = zero UNRECORDED
   inversions — every finding has a `Changelog/` + build-commit defect entry; unrecorded
   finding = fail); a new milestone/project with an order violation fails the gate even if all other checks pass.

## 4. Machine-gated `milestone.sh` (foolproof — refusal + audit, no silent bypass)

Invocation: `bash scripts/milestone.sh <tag> "<msg>"`; dry run:
`bash scripts/milestone.sh --dry-run <tag> "<msg>"` (flag first, tags nothing).
On success the script MUST write `scripts/tests/receipts/<tag>.json`
(checks run + versions + result — schema PINNED: `{"tag": str, "checks": [{"name": str,
"result": "pass"|"fail", "detail": str}], "versions": {tool: version}, "result": "pass"|"fail"}`)
— the file `audit-tags.sh` consumes (match rule: receipt exists + `result == "pass"`;
exit 0 lists clean, exit 1 prints missing/failing tags, one per line).
Touched files = staged + unstaged working-tree files for `--dry-run`
(`git status --short`); for audits, the tag's commit range = commits reachable from the tag
excluding those reachable from the previous taggerdate-ordered tag. Pinned procedure
(the check runs BEFORE the tag is minted, so the range ends at HEAD): list
`git for-each-ref --sort=-taggerdate --format='%(refname:short)' refs/tags` (newest first),
take the line AFTER `<tag>`'s would-be position — i.e. the newest tag older than HEAD —
then `git log <prev>..HEAD --oneline` is the range (no previous tag =
range is HEAD's full history); after green, mint the tag, then re-run the range command
with `<tag>` for the audit record.
Tagging REFUSES (non-zero exit + reason) unless ALL pass:

0. Tag format: `<tag>` matches the pinned tag regex `^([a-z0-9]+(-[a-z0-9]+)*-)?m[0-9]+\.[0-9]+-(mvm|full)$`
   OR `^p[0-9]-complete$` (phase gates, e.g. `p0-complete`), OR is on the pinned grandfather list
   (`m0.1-fullpass` — the only entry; never extended without a registry-header-style amendment).

1. Build+lint table (pinned in the script; CODE extensions = `py|c|h|cpp|hpp|jl|sh` with rows:
   `py` → `ruff check` + `ruff format --check`; `c/h/cpp/hpp` → `clang-tidy`; `sh` → `bash -n`;
   `jl` → JuliaFormatter-or-parse (rule below);
   `.md` handled by the diagnose check in item 4 — NOT by this table; data/binary formats
   (`json|csv|png|svg|step|toml|txt|…`) get existence-checks only; anything else
   (incl. `js|ts`) MUST add its row before its first tag — gate FAILS CLOSED on unlisted extensions):
   `jl` → `JuliaFormatter` if `.JuliaFormatter.toml` (or `[JuliaFormatter]` in
   `Project.toml`) exists in the project, else syntax-parse:
   `julia -e 'for f in ARGS; Meta.parse(read(f,String)); end' <files>`.
   A 5th language MUST add its row before its first tag.
2. Artifacts: `Evidence:` lines (dash form `- Evidence: <path>`, one per line, repo-relative path, living under the
   README `## Pass` heading or milestone `## Pass Condition`, scope ending at the next
   `##` heading or EOF), e.g.
   `Evidence: Mechatronics/docs/captures/2026-09-07_hbridge-loss.png`
   Every listed path exists on disk. Freeform checkboxes are NOT parsed.
3. Skills: `## Skills gained` line present with COUNT ≥ 1, plus a `Requires:` line
   (entry-point form allowed, blank forbidden); every ID matches §3 regex AND resolves
   in the registry; every registry row touched has non-null `Goal era` matching the era
   format (`pre-GOAL` or the pinned `<slug> (<range>)` — format-checked, not just non-null)
   and its Evidence-tag value exists as a minted tag; every prerequisite taggerdate ≤ claimant taggerdate (§3 skill-order audit).
4. Links+lenses: extended `diagnose.py` (§2 item 2 spec) clean on touched files, INCLUDING
   the lens rule — any touched milestone MISSING its lens block, or any `status: proposed`
   lens in one, fails the gate (checked inside `diagnose.py`, not by hand; skill IDs are
   scanned on `Skills gained` + `Requires:` lines; lens blocks parsed on the exact header
   `Lenses — m0-N`); verbatim MOVES (content unchanged) are EXEMPT from lens-presence
   (new/edited content is not).
5. Attestation: dated blank-page test note, e.g.
   `Mechatronics/math/0.2-attest-2026-09-07.md`
   (`<domain>/0.N-attest-<date>.md`, domain = split dir owning the milestone (Phase 0);
   for unsplit Phases 1–3: `Mechatronics/milestones/<file-stem>-attest-<date>.md`, e.g.
   `01_signals_actuators_dynamics-attest-2026-09-07.md`; `<date>` = YYYY-MM-DD):
   re-solve from memory with NO reread/rewatch before solving (cold-recall-first);
   gaps red-penned; Full Pass note MUST cite a PRIOR attempt date (VAULT POLICY: same-day
   echo fails the gate — enforces spacing; compared via taggerdate where tags exist,
   note dates otherwise — dates compared as YYYY-MM-DD strings); red-pen gaps appended to
   `_system/Landmine Log.md`, or linked from the attest note to an existing vault file
   (endpoint pinned: Landmine Log or vault-file link — no bare text).
6. Direct-`git-tag` bypass is detectable, not preventable: monthly (VAULT POLICY cadence)
   `bash scripts/audit-tags.sh` (ABSENT — created here: lists tags lacking gate receipts in
   `scripts/tests/receipts/<tag>.json`, exit 1 printing one per line, exit 0 when clean)
   + agent rule — never attest a bypassed tag;
   bypassed tags get `-unaudited` registry note until re-earned.

Gate ships with fixtures at `scripts/tests/fixtures/{refusal-0..7,clean}/` (ABSENT —
created by this section; refusal-N maps to gate item N for N=0..5 (direct refusals:
0 tag-format, 1 lint, 2 artifacts, 3 skills, 4 links+lenses, 5 attest); refusal-6 exercises
the DETECTIVE control `audit-tags.sh` (harness creates an annotated fixture tag in a temp
worktree, runs the audit, expects exit 1 listing it); refusal-7 = skill-order violation
(item-3 sub-check) with prerequisite taggerdate after claimant, backdated via
`GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE` env), run by
`bash scripts/test-gate.sh` (ABSENT — created here) expecting 9/9. 9/9 or red. Fixture layout:
each `refusal-N/` holds input files + `expected-exit` + `expected-stderr-fragment`; `clean/`
holds passing inputs + a fixture `registry.md` so skill checks evaluate self-contained.

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
   `error_bank` (+ `contrasts_with` edges for discrimination — NEVER `discriminates_from`
   or "execution key", which §0 establishes as non-fields).
   Counts include capstones (say capstone count in reports).

WIP policy (VAULT POLICY, not engine law — the engine permits new work with dues
outstanding; this policy trades speed for habit protection, overrideable):

- Default refuse landing while `due --cap 12` shows `due > 12`, or the landing topic's own
  `states.new` > 20 (`12` = engine STANDARD_CAP; `20` = VAULT POLICY, ARBITRARY cap per landing
  topic; capstones count inside `new` — no exclusion arithmetic). No global-`new` gate (the
  258-`new` backlog burns down via the pre-step below, not via landing refusal).
- Escape hatch (logged in the scope note's `Override:` field + user-sign line, per batch —
  no standing overrides): JIT-override after reviewing the due list —
  allowed ONLY for scope-approved JIT nodes (§5 landings). Standing override = fail.
- Backlog-clear pre-step (before first landing): capped review sittings
  (`due --cap 12`, cold free recall first — never rewatch/reread before the probe;
  amnesty-first as session-start sensibility — `RETURN_ABSENCE_DAYS=7`
  is prose, not a command; cited as sensibility) until `due ≤ 12` or JIT-override signed.
  Burn-down for `new`: dedupe via `analogous_to`-convention/`retire` + `doctor`
  (remediation step, counts toward the landing-topic ≤20 cap above) — 258 `new` across
  13 topics as of 2026-09-08, tracked per-topic in the build note.
- Soft alarm at 150 active (`active` = `topics` states review+learning+`new` summed, all topics):
  ARBITRARY, review-or-retire session due by 2026-12.

Landings (scope approval each; pretests/maps land maps-only — builds are the STATED
exception and land ONLY as topic capstones, never as parallel vault structure):

- **Now (JIT, each node tied to a NAMED MVM checkbox — recorded in the scope-approval
  note `.opencode/plan/scope-<topic>-<date>.md` (`<date>` = YYYY-MM-DD; pinned path/format:
  topic, node list with target checkboxes, pretest plan, WIP counts — `due --cap 12` n +
  per-topic `new` from `topics` — at approval; `Override:` field + user-sign line when used), NOT in `why_chain`, which stays
  an id-path; per-item kind: procedures land as NODES, builds land as CAPSTONES):** py CSV→PlotJuggler plot (M1.1, nodes),
  FFT+windowing (M1.2), `solve_ivp` pendulum (M1.4); C ring buffer + versioned telemetry
  framing (M1.5/M1.1, capstones). Parked until the demanding milestone is ACTIVE (ACTIVE =
  the milestone named by the AGENT.md next-step rule / current Daily Focus; ✅✅ = MVM tag +
  Full tag both minted): packaging, OOP,
  CMake lore, FK-visualizer rebuild (M0.2 already ✅✅).
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
- Later:** `cpp-foundations`, `julia-viz` (post-stabilization = `due ≤ 12` at two
  consecutive weekly checks — weekly cadence AND the count of two are both ARBITRARY; first stabilization review 2026-12,
  jointly with the 150-alarm review and quarterly audit), then
  `mech-software/electronics/mechanical` with `analogous_to` cross-links (cross-topic
  `requires` admitted unsupported).

## 6. Video-first lenses (VAULT POLICY, authoritative, veto-gated, generation-first)

Resource-block format per milestone (pilot: Phase-0 files only; plain-text lines directly
under the per-milestone Resources callout — NOT a separate callout; `<milestone id>` dialect
PINNED to the anchor scheme `m0-N`, first line `Lenses — m0-2`):

```
Lenses — <milestone id>
Rigorous: <title> — <creator> — <url> — <status: proposed|approved|waived>
Intuitive: <title> — <creator> — <url> — <status: proposed|approved|waived>
Interactive: <sim/bench>   Theory: <scoped book ch>   (existing content kept)
```

Rules: agent proposes exactly 2 (VAULT POLICY dosage: 1 rigorous + 1 intuitive, Veritasium/3Blue1Brown/
Efficient Engineer caliber; new domains calibrated with the user first — titles/creators/URLs
are USER inputs at approval time, the agent drafts candidates). User
approves/replaces per topic. **No approved pair → topic doesn't land**, with ONE explicit
escape: `waived` + reason logged in the lens block + `Changelog/` (affordance-none content) — a user-signed decision,
never a default. AI-generated video is NEVER a lens; if proposed, drop it and chat directly.
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
Fluency guard: "makes sense" counts as zero evidence (VAULT POLICY counting rule — we score it zero; no claim about mechanism). Congruence: verbal quiz for
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
§3 registry fill → §6 lens pairs (per-landing approval) → §5 landings.
Phase acceptance (ALL must hold, each mechanically checkable): §1 grep-gate
(exact commands — counts: `grep -rEoh 'QDD|2-DOF|2DOF|2 DOF|2-link|Puck|backdrivab|quasi-direct|SendCutSend|gripper|lever-arm' Mechatronics/ Science/ DataScience/ | sort | uniq -c`;
files: `grep -rEl 'QDD|2-DOF|2DOF|2 DOF|2-link|Puck|backdrivab|quasi-direct|SendCutSend|gripper|lever-arm' Mechatronics/ Science/ DataScience/ | sort`
— the ONLY-files claim is checked against the filename output, never the `-h` counts) + GOAL.md `## Checklist` section
(exact heading spelling) exists and is filled — the section IS the record, no separate file — + semantic pass
recorded as per-item dispositions in that section; anchor-aware
`diagnose.py` clean (or only `EXEMPT`-block items — `EXEMPT` = the `EXEMPT:` comment block at
the top of `scripts/diagnose.py`, authoritative for carried failures); gate fixtures 9/9;
skill-order audit (§3 skill-order audit) clean on the current vault (pre-existing inversions
RECORDED in `Changelog/` + the build commit message — "filed as defects" means exactly that,
not waived); cold-start test (step 0: export `ENGRAM_RUNNER` + `ENGRAM_HOME` per
`_system/engram/env.example.sh`; step 1: fresh session runs the AGENT.md session-start block
verbatim with zero errors AND `due --cap 12` returns the same `n` as the pre-test run the same
day — time-varying quantities compared same-day only; both invocations logged in the test note
`.opencode/plan/cold-start-<date>.md`, pinned path); FRESH reviewer agents on the same three briefs (alignment,
neuroscience, extensibility+onboarding) report zero blocking verdicts, max 2 rounds (VAULT POLICY
bound) — leftovers go to the user for adjudication, the loop terminates. Reviewer briefs = the three names above
(alignment, neuroscience, extensibility+onboarding); verdicts recorded in `Changelog/` + the
build commit message.
