# Phase 2 — Skill Builder (decouple vault + foolproof gates + nodes + lenses)

Status: PLAN — do not implement until user approves this file + reviewer sign-off.
(Win-adapted 2026-09-08 for reviewer blockers: ordering, checkability, tag grammar,
staleness vs landed 13-topic store. Still unapproved — this edit changes no vault content.)
Active-phase rule: AGENT.md §Hard Rules names the active phase; on conflict the active
phase's file governs. Depends on: Phase 1 complete (AGENT.md live, vault caught up,
diagnose at known-baseline).
Incorporates: vault-structure + load/sustainability evaluations (2026-09-07) AND all
plan-review rounds. Where this file contradicts those evaluations, this file governs
and says why. Reference convention: §X item Y (e.g. §4 item 3 = §4's third numbered check).
File:line citations are repo-root-relative paths + current line numbers (re-check: rot fast). Runner for all engram operations: `$ENGRAM_RUNNER` (per-machine env — Mac `python3 ~/engram/scripts/engram.py`, Win `python3 ~/.config/opencode/scripts/engram.py`; see `_system/engram/env.example.sh`. NEVER hardcode either path)
(subcommands `due`, `topics`, `session-start`, `doctor`, `add-topic`,
`edit-node`, `retire`, `rate`, `receipt`, `selftest`). `scripts/*.sh` are NOT +x:
invoke as `bash scripts/<name>.sh`.

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
  the checklist as it rewrites). Coupled files include pattern hits AND semantic-feed lines
  (not pattern matches — labeled as such): `Science/Index.md:14` (Lorentz feed, semantic),
  `DataScience/Index.md:9,13` (telemetry pipeline, semantic), `Mechatronics/resources/LAB_INFRASTRUCTURE.md`,
  `Mechatronics/IDEAS.md`, `Mechatronics/hardware/inventory.md`.
- Foundations are ALREADY goal-instantiated (0.2 FK arm tip, 0.4 arm FBD + holding
  torque, QDD torque-constant reference at 0.10 `:568`, 0.7 arm-link material,
  CONVENTIONS arm frame defaults): §1 parameterization tasks are mandatory,
  not cosmetic (scaffold-first per §1 — mass parameterization deferred to pass 2).
- Engram (LANDED vault store — `_system/engram/`, 13 topics / 270 nodes / 258 `new` /
  0 repo receipts as of 2026-09-08; mark universe wherever counts gate anything):
  reconciled 340 HOLD / 14 PORT (`mech-spine`, Mac) / 0 DROP; resits ~zero (all Win
  receipts pre-divergence, Win nodes adopted in place). ENGINE_PIN green (engine sha
  FULL match both sides, verified 2026-09-08). WIP caps below evaluate against THIS store.
  Win store per mailbox (12 topics / 256 nodes) is a SEPARATE universe and TODAY
  violates the §5 WIP gate — no landings until v4 reconciliation lands + PIN green.
  Known duplicates: `static-equilibrium` ×2, torque pair, Japanese verb clusters.
  `kind` absent on ~37 nodes (absent ⇒ `concept` per architect — caveat: absent +
  `arbitrary:true` ⇒ `fact`; audit content, only true fresh-instance procedures earn
  `procedure` + `practice` frames with engine-native `problem_frame` + `verify` +
  `error_bank`, plus `contrasts_with` edges for discrimination — `discriminates_from`
  appears only in a code comment nothing reads; "execution key" is no field).
  Commitment cue `10am`
  is a clock cue: OFFER an event anchor once at `/learn` close (`/coach` only if a
  renewal is due, cue age ≥ 28d) and store the verbatim answer (never force-rewrite). `artifact` null everywhere — keep it so; vault
  linkage lives in the registry Evidence-tag + `Goal era` columns and session-log
  lines (see the §3 `Requires:` format paragraph and the §5 "Language-project loop"
  paragraph).
- Engine facts this plan respects (NOT negotiable): node kinds are `concept|procedure|fact`
  ONLY (no `kind:transfer` on nodes); capstone = engine-minted `{capstone:true,
  transfer_probe:None}` with receipt `kind:transfer` (metrics never pooled; successful
  transfer MAY strengthen scheduling); `why_chain` = derives-from id path by CONVENTION
  ONLY (engine neither validates nor walks it — say so, never rely on it); cross-topic
  `requires` is unsupported (prerequisites live in ONE canonical topic +
  `analogous_to` links — `analogous_to` itself has ZERO engine hits: vault convention,
  not engine field); pretests diagnose the frontier (never land over an
  undiagnosed frontier); probe↔rubric are one object (3-step self-check per node).
- Foundation rule after this phase: bare minimum every goal needs. Projects: ≥1 skill each.

## 1. GOAL.md — single goal source (scaffold FIRST, parameterize after confirm)

Two passes (sequencing economics — do NOT front-load the ~118-line rewrite ahead of
GOAL-confirm): pass 1 scaffolds (`GOAL.md` draft + `goals/parked/` dir + registry
`Goal era` column); pass 2 (post-confirm) does the mass parameterization below.

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
  `^([a-z0-9]+-)?m[0-9]+\.[0-9]+-(mvm|full)$` (post-swap tags carry the `<goal>-` prefix,
  e.g. `cnc-m3.1-mvm`; `m0.1-fullpass` grandfathered, never rewritten). `Goal era` format:
  `pre-GOAL`, or `<slug> (<YYYY-MM>[–<YYYY-MM>])` with `<slug>` pinned in GOAL.md
  (today `qdd-arm (2026-08–)`). No tag retire rule.
- Parameterization tasks (mandatory): CONVENTIONS arm frame defaults → goal parameters;
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

Target (verbatim bodies via `git mv` + explicit link-migration per moved file — cut map
with VERIFIED line spans of `Mechatronics/milestones/00_foundations.md` (599 lines):
title+Outcome+Pass Condition 1–49; 0.1 → 50–96; 0.2 → 97–133; 0.3 → 134–167;
0.4 → 168–208; 0.5 → 209–246; 0.6 → 247–285; 0.7 → 286–359; 0.8 → 360–424;
0.9 → 425–515; 0.10 → 516–579; Deload 580–599. Output filenames follow the scheme
`<dir>/0.N-<kebab-from-section-heading>.md` (slugs derived at build from the section
headings above — no invented names); each new dir gets a `README.md` index.
`00_foundations.md` itself becomes a redirect index (no checkboxes — evidence backlinks
keep resolving). Pre-move `Mechatronics/firmware/` + `Mechatronics/simulations/` READMEs,
`requirements.txt` (`simulations/python/requirements.txt` — the only one),
`template_*.py` (both under `simulations/python/`) — each gets: merge as dir
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
| `lab/` | 0.10 + Phase-0 Pass/Deload (lines 25–46 and 578–599 of `Mechatronics/milestones/00_foundations.md` at time of writing — 578–599 covers photo, `versions.sh`, Retro) + SAFETY_CARD + CONVENTIONS + inventory refs | metrology + shared discipline |

Structural fixes (all mandatory, in this order):

1. **Primacy:** ROADMAP table is the ONLY ✅. Domain `Index.md` files are links-only
   (≤7 entries, no status, no checkboxes) — includes trimming `Mechatronics/Index.md`
   (14 link targets today) with per-line dispositions in the build commit. Milestone bodies keep checkboxes with header:
   `Status lives in [[Mechatronics/ROADMAP|Roadmap]] — do not duplicate.`
   Rewrite `ROADMAP.md:9-17` Completion & Evidence text (pinned replacement):
   `1. Pass the gate: bash scripts/milestone.sh --dry-run <tag> "<msg>" is green.
   2. Tag: bash scripts/milestone.sh <tag> "<msg>". The tag is the durable evidence.
   3. Mark ✅ in the ROADMAP table only, then bash scripts/save.sh "roadmap: mark <tag>."`
   STAGED: this rewrite lands ONLY after §4 ships `--dry-run` (until then the
   documented command fails — build §4 first, swap text second). Doc==script owner:
   Mac builds §4; the pinned doc text governs, the script implements it.
   Fix `milestone.sh` echo to the same text; add domain commit scopes (`math:`,
   `physics:`, …) to `CONVENTIONS.md` (bare `phaseN:` deprecated for domain work; old tags untouched).
2. **Anchors:** every milestone gets `<a id="m0-N"></a>` (`m0-1`…`m0-10` — resolvers match
   full IDs, never prefixes, since `m0-1` prefixes `m0-10`); ROADMAP + all new notes link
   `#m0-N` only. Migration script rewrites the 37 ROADMAP milestone rows, records old slugs as
   HTML comments `<!-- was: <old> -->` (Daily history immutable — old links rot by design).
   `diagnose.py` extension spec: resolve `<a id="X">` definitions; accept link forms
   `[[File#X]]`, `(file.md#X)`, `#X` (same-file — definition-side lookup, not a skip);
   skip code fences; skill IDs (scanned on `Skills gained` + `Requires:` lines) validated
   against §3 regex + registry membership. Must pass clean. Timing rule: full rescan per
   tag accepted; add incremental mode only if a run exceeds 60s (record timing).
3. **Evidence 2-home rule:** canonical = milestone-body checkboxes + git tag.
   Narrative sources live in the SPLIT files (0.2 body in `math/0.2-*.md`); 0.1's checkbox
   duplication is MERGED into its split body with a redirect header (per §2 redirect format).
   Daily notes reference status, never restate it.
4. **Mechatronics/software/ bounds:** one folder per PROJECT at `Mechatronics/software/<kebab-project>/`
   with `README.md` carrying EXACTLY these 6 headings: `## Question`,
   `## Inputs/Outputs`, `## How to run`, `## Pinned commit`, `## Skills gained`,
   `## Pass` (MVM/Full Pass checkboxes + `Evidence:` lines — §4 item 2 grammar).
   Snippets (non-project, no status, no gates) live ONLY in
   `Mechatronics/software/_snippets/` (cap 20 files TOTAL across languages; overflow
   forces a project or deletion). `Mechatronics/software/simulations/` (the moved home)
   is the only sim home — no other sim dirs. Per-project `.gitignore` for build output. `Mechatronics/software/`
   is created by this task (it does not exist yet).
5. **Ownership table** (both Indexes, ~5 lines): Science wins proofs; `math/`/`physics/`
   win worked procedures; `CONVENTIONS.md` wins frames/units — until §1 parameterizes the
   arm defaults into GOAL.md (tracked task). Reciprocal `[[links]]`.
6. **Keep** `Mechatronics/ROADMAP.md` at its path; `resources/` untouched.

## 3. Skill registry — ≥1 skill per project, machine-checkable, scalable
(ABSENT — `Mechatronics/skills/` does not exist; created by this section.)

- Location: `Mechatronics/skills/registry.md` (mech+software skills; piano/japanese/data
  skills explicitly deferred, not homeless-by-accident).
- Schema: `| Skill ID | Name | Evidence tag | Goal era | Project | Requires |`
  (`Requires` = comma-separated prerequisite skill IDs, empty ONLY for true entry
  points — 0.1-level — with `Requires: — (entry point)` written explicitly; blank = fail.)
- ID regex (gate-enforced): `^(sw|ee|mech|lab)-[a-z0-9-]+$`. Language token applies to
  `sw-` ONLY and is gate-checked against the pinned token list (`c`, `py`, `cpp`, `jl`):
  `sw-c-…`, `sw-py-…`, `sw-cpp-…`, `sw-jl-…` (new `sw-` language token needs
  NO amendment; new PREFIX needs a one-line registry-header amendment). Shard to
  `Mechatronics/skills/<domain>.md` when data rows exceed 100 — `<domain>` ∈
  {`sw`, `ee`, `mech`, `lab`} (one shard per prefix); `registry.md` becomes the index
  (schema + shard list), rows move to shards, IDs never change on sharding.
- `Skills gained` format (gate-parseable, one per line under the heading):
  `- sw-py-csv-plot — CSV→PlotJuggler (tag m1.1-mvm, Goal era qdd-arm (2026-08–))`
  (`Evidence tag` column holds TAGS matching the pinned tag regex; `Evidence:` lines hold
  PATHS — different grammars, both required where specified.)
  `Requires:` line directly below (same heading, gate-parseable):
  `Requires: sw-py-venv, sw-py-uncertainty-mean` (or `Requires: — (entry point)`).
- Foundation milestones declare their bare-minimum skill sets in the same registry
  (evidence = milestone tags). Registry answers "what can I do, proven by what".

### Skill-order audit — the vault must confer skills in a reasonable order (§3, part 2)

The agent checks curriculum sequence (at every landing + quarterly re-run):

1. **Requires closure:** every registry row's `Requires` IDs resolve in the registry
   (no dangling prerequisites, no forward references to unconferred skills).
2. **Date order:** every prerequisite's evidence tag predates (or equals) the
   claimant's tag — compare TAGGER dates with `git log -1 --format=%(taggerdate:iso)
   <tag>` (`%cI` answers committer date, which re-sign preserves by design — wrong
   clock). Lightweight tags have empty taggerdate → gate REFUSES them (require
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
   project. Quarterly audit re-runs the full walk; a new milestone/project with an
   order violation fails the gate even if all other checks pass.

## 4. Machine-gated `milestone.sh` (foolproof — refusal + audit, no silent bypass)

Invocation: `bash scripts/milestone.sh <tag> "<msg>"`; dry run:
`bash scripts/milestone.sh --dry-run <tag> "<msg>"` (flag first, tags nothing).
On success the script MUST write `scripts/tests/receipts/<tag>.json`
(checks run + versions + result — schema PINNED: `{"tag": str, "checks": [{"name": str,
"result": "pass"|"fail", "detail": str}], "versions": {tool: version}, "result": "pass"|"fail"}`)
— the file `audit-tags.sh` consumes (match rule: receipt exists + `result == "pass"`;
exit 0 lists clean, exit 1 prints missing/failing tags, one per line).
Touched files = staged + unstaged working-tree files for `--dry-run`
(`git status --short`); for audits, the tag's commit range.
Tagging REFUSES (non-zero exit + reason) unless ALL pass:

1. Build+lint table (pinned in the script; code extensions mapped, `.md` handled by the
   diagnose check in item 4 — NOT by this table; gate FAILS CLOSED on unlisted CODE extensions):
   `py` → `ruff check` + `ruff format --check`; `c/h` → `clang-tidy`;
   `jl` → `JuliaFormatter` if `.JuliaFormatter.toml` (or `[JuliaFormatter]` in
   `Project.toml`) exists in the project, else syntax-parse:
   `julia -e 'for f in ARGS; Meta.parse(read(f,String)); end' <files>`.
   A 5th language MUST add its row before its first tag.
2. Artifacts: `Evidence:` lines (one per line, repo-relative path, living under the
   README `## Pass` heading or milestone `## Pass Condition`), e.g.
   `Evidence: Mechatronics/docs/captures/2026-09-07_hbridge-loss.png`
   Every listed path exists on disk. Freeform checkboxes are NOT parsed.
3. Skills: `## Skills gained` line present with COUNT ≥ 1, plus a `Requires:` line
   (entry-point form allowed, blank forbidden); every ID matches §3 regex AND resolves
   in the registry; every registry row touched has non-null `Goal era` and its Evidence-tag
   value exists as a minted tag; every prerequisite taggerdate ≤ claimant taggerdate (§3 skill-order audit).
4. Links+lenses: extended `diagnose.py` (§2 item 2 spec) clean on touched files, INCLUDING
   the lens rule — any touched milestone MISSING its lens block, or any `status: proposed`
   lens in one, fails the gate (checked inside `diagnose.py`, not by hand; skill IDs are
   scanned on `Skills gained` + `Requires:` lines; lens blocks parsed on the exact header
   `Lenses — <milestone id>` at per-milestone placement).
5. Attestation: dated blank-page test note, e.g.
   `Mechatronics/math/0.2-attest-2026-09-07.md`
   (`<domain>/0.N-attest-<date>.md`, domain = split dir owning the milestone, `<date>` = YYYY-MM-DD):
   re-solve from memory, gaps red-penned; Full Pass note MUST cite a PRIOR attempt date
   (same-day echo fails — compared via taggerdate where tags exist, note dates otherwise);
   red-pen gaps appended to Landmine Log or linked.
6. Direct-`git-tag` bypass is detectable, not preventable: monthly
   `bash scripts/audit-tags.sh` (new: lists tags lacking gate receipts in
   `scripts/tests/receipts/<tag>.json`) + agent rule — never attest a bypassed tag;
   bypassed tags get `-unaudited` registry note until re-earned.

Gate ships with fixtures at `scripts/tests/fixtures/{refusal-1..7,clean}/` (ABSENT —
created by this section; refusal-N maps to gate item N: 1 lint-fail, 2 missing-artifact-path,
3 bad-skill-ID, 4 broken-link-or-proposed-lens, 5 same-day-attest, 6 forced-tag-without-receipt,
7 skill-order violation with prerequisite taggerdate after claimant), run by
`bash scripts/test-gate.sh` (ABSENT — created here) expecting 8/8. 8/8 or red.

## 5. Engram topics — engine-native WIP, JIT-cut, capstone-only builds

GATE (satisfied 2026-09-08 — proposal landed to main + ENGINE_PIN green, engine sha FULL
match both sides): landings proceed under the WIP caps below, evaluated against the LANDED
13-topic store. Pre-landing backlog burn-down (remediation, NOT a landing — no approval needed):
dedupe via `analogous_to`-convention/`retire` + `doctor` until `new` approaches cap, plus capped
review sittings (`due --cap 12`); whatever remains above cap needs per-batch JIT-override
(logged, user-signed) — no standing overrides. Doctor-gating rule: preconditions run with
`$ENGRAM_RUNNER doctor` on the machine doing the landing, sha recorded alongside results.

Preconditions (before ANY landing):

1. `doctor probe_gaps` clean on touched topics; scope approval covers pretest plan, node
   kinds, `practice` frames, contrast/viz/interactivity needs.
2. Dedupe via `analogous_to`/`retire` + `doctor` (NOT keyword diff): `static-equilibrium`×2,
   torque pair, Japanese verb clusters. Overlap check (exact-id + claim read) joins every
   scope approval.
3. Kind audit: absent ⇒ concept (no blind backfill); true fresh-instance procedures earn
   `procedure` + `practice` frame with engine-native `problem_frame` + `verify` +
   `error_bank` (+ `contrasts_with` edges for discrimination — NEVER `discriminates_from`
   or "execution key", which §0 establishes as non-fields).
   Counts include capstones (say capstone count in reports).

WIP policy (VAULT POLICY, not engine law — the engine permits new work with dues
outstanding; this policy trades speed for habit protection, overrideable):

- Default refuse landing while `due --cap 12` shows `due > 12`, or the `topics`
  command shows global `states.new` summed > 20, or the landing topic's own
  `states.new` > 20 (`12` = engine STANDARD_CAP; `20` = architect 20-node arc max,
  cited; capstones count inside `new` — no exclusion arithmetic).
- Escape hatch (logged, user-signed): JIT-override after reviewing the due list —
  allowed ONLY for scope-approved JIT nodes (§5 landings). Standing override = fail.
- Backlog-clear pre-step (before first landing): capped review sittings
  (`due --cap 12`, amnesty-first as session-start sensibility — `RETURN_ABSENCE_DAYS=7`
  is prose, not a command; cited as sensibility) until `due ≤ 12` or JIT-override signed.
- Soft alarm at 150 active: ARBITRARY, review-or-retire session due by 2026-12.

Landings (scope approval each; pretests/maps land maps-only — builds are the STATED
exception and land ONLY as topic capstones, never as parallel vault structure):

- **Now (JIT, each node tied to a NAMED MVM checkbox — recorded in the scope-approval
  note, NOT in `why_chain`, which stays an id-path):** py CSV→PlotJuggler plot (M1.1),
  FFT+windowing (M1.2), `solve_ivp` pendulum (M1.4); C ring buffer + versioned telemetry
  framing (M1.5/M1.1). Parked until the demanding milestone is ACTIVE: packaging, OOP,
  CMake lore, FK-visualizer rebuild (M0.2 already ✅✅).
- **Atomicity policy (VAULT POLICY, ARBITRARY — dosage, not finding):** one claim per node,
  5–15 min per node. Builds land ONLY as topic capstones
  (engine capstone semantics, receipt `kind:transfer`). Vault linkage = registry
  Evidence-tag + `Goal era` columns and session-log lines — NEVER `transfer_probe` text
  (stays None) or parallel checkboxes. Any node reviewable only by opening a README
  is malformed.
- **Language-project loop (§3 carve-out — applies to EVERY topic with builds, incl.
  future piano/japanese projects):** user writes the code/piece/text; AI reviews errors +
  best practices and NEVER writes the solution (scaffolds only — How-to-Learn Yellow zone).
  Each project carries its own MVM/Full Pass pair (in README `## Pass` for code, in the
  topic's milestone file for piano/japanese) with distinct evidence tags; the AI review
  note is filed as evidence and linked from `## Pass`.
- **Later:** `cpp-foundations`, `julia-viz` (post-stabilization = `due ≤ 12` at two
  consecutive weekly checks — cadence ARBITRARY; first stabilization review 2026-12,
  jointly with the 150-alarm review and quarterly audit), then
  `mech-software/electronics/mechanical` with `analogous_to` cross-links (cross-topic
  `requires` admitted unsupported).

## 6. Video-first lenses (VAULT POLICY, authoritative, veto-gated, generation-first)

Resource-block format per milestone (pilot: Phase-0 files only; per-milestone placement):

```
Lenses — <milestone id>
Rigorous: <title> — <creator> — <url> — <status: proposed|approved|waived>
Intuitive: <title> — <creator> — <url> — <status: proposed|approved|waived>
Interactive: <sim/bench>   Theory: <scoped book ch>   (existing content kept)
```

Rules: agent proposes exactly 2 (1 rigorous + 1 intuitive, Veritasium/3Blue1Brown/
Efficient Engineer caliber; new domains calibrated with the user first). User
approves/replaces per topic. **No approved pair → topic doesn't land**, with ONE explicit
escape: `waived` + logged reason (affordance-none content) — a user-signed decision,
never a default. AI-generated video is NEVER a lens; if proposed, drop it and chat directly.
Protocol per topic (generation-first — predict precedes the first watch turn; watch
NEVER comes before a prediction):
predict/commit → watch segment → self-explain aloud → blank-page reconstruction →
fresh-probe verify (probe → confidence pick → blind assessor → receipt) → project.
Fallback ladder (when prediction fails twice): scaffolded worked example → predict
again → verify; never lecture what derivation practice could reach. Authorship-verify
step: for any lens without an established educator, verify human authorship before
linking (no-established-educator cases logged). Explorable→rigorous rule: interactive explorables
illustrate the RIGOROUS lens (manipulables carry the formalism), never the intuition.
Veto-gate throughput: every JIT batch needs a signed pair-or-waiver — expect approval
clustering; batch approval per milestone is allowed (one user sign covers the pair list).
Fluency guard: "makes sense" is zero evidence (AGENT.md). Congruence: verbal quiz for
verbal claims, execution/build probe for procedures (no incongruent grading).
(Enforcement of this section activates with Phase 2 — Phase-1 cites it as forward
pointer only.)

## 7. Sequencing + acceptance (STOP for user feedback — no further work unapproved)

Order (dependency-sorted — each step's inputs exist when it runs): §1-scaffold (GOAL draft
+ parked dir + `Goal era` column) → §2-item-2 diagnose-extension (anchors + skill-ID checks;
the §4 gate CONSUMES this, so it builds before §4) → §4 gate build (fixtures are
SELF-CONTAINED — fixture registry ships in `fixtures/`, so 8/8 evaluates without the real
§3 fill) → §2 split pilot + Completion-text swap (STAGED on §4) → §3 registry fill →
§1-pass-2a (CONVENTIONS arm defaults → GOAL parameters ONLY — feeds the §2 ownership table;
rest of pass 2 stays deferred) → §6 lens pairs (per-landing approval; the §4 lens-presence
check is STAGED on this grammar — until pairs exist, §4 fails any touched milestone lacking
a lens block, and `status: proposed` fails once blocks exist) → §5 landings.
Phase acceptance (ALL must hold, each mechanically checkable): §1 grep-gate
(exact command: `grep -rEoh 'QDD|2-DOF|2DOF|2 DOF|2-link|Puck|backdrivab|quasi-direct|SendCutSend|gripper|lever-arm' Mechatronics/ Science/ DataScience/ | sort | uniq -c`)
+ GOAL.md checklist file exists + semantic pass recorded in GOAL.md; anchor-aware
`diagnose.py` clean (or only `EXEMPT`-block items — `EXEMPT` = the `EXEMPT:` comment block at
the top of `scripts/diagnose.py`, authoritative for carried failures); gate fixtures 8/8;
skill-order audit (§3 skill-order audit) clean on the current vault (pre-existing inversions
RECORDED in `Changelog/` + the build commit message — "filed as defects" means exactly that,
not waived); cold-start test (fresh session runs the AGENT.md session-start block verbatim
and reaches the same due counts); FRESH reviewer agents on the same three briefs (alignment,
neuroscience, extensibility+onboarding) report zero blocking verdicts, max 2 rounds — leftovers
go to the user for adjudication, the loop terminates.
