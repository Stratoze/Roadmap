# Phase 2 — Skill Builder (decouple vault + foolproof gates + nodes + lenses)

Status: PLAN — do not implement until user approves this file + reviewer sign-off.
Active-phase rule: AGENT.md §Hard Rules names the active phase; on conflict the active
phase's file governs. Depends on: Phase 1 complete (AGENT.md live, vault caught up,
diagnose at known-baseline).
Incorporates: vault-structure + load/sustainability evaluations (2026-09-07) AND all
plan-review rounds. Where this file contradicts those evaluations, this file governs
and says why. Reference convention: §X.Y means §X item Y (sections are numbered lists).
File:line citations are repo-root-relative paths + current line numbers (re-check: rot fast). Runner for all engram operations: `python3 ~/engram/scripts/engram.py`
(verified 2026-09-07; subcommands `due`, `topics`, `session-start`, `doctor`, `add-topic`,
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
  the checklist as it rewrites). Coupled files include `Science/Index.md:14`,
  `DataScience/Index.md:9,13`, `Mechatronics/resources/LAB_INFRASTRUCTURE.md`,
  `Mechatronics/IDEAS.md`, `Mechatronics/hardware/inventory.md`.
- Foundations are ALREADY goal-instantiated (0.2 FK arm tip, 0.4 arm FBD + holding
  torque, QDD torque-constant reference at 0.10 `:568`, 0.7 arm-link material,
  CONVENTIONS arm frame defaults): §1 parameterization tasks are mandatory,
  not cosmetic (scaffold-first per §1 — mass parameterization deferred to pass 2).
- Engram (MAC-SIDE-ONLY universe — mark universe wherever counts gate anything):
  6 topics / 103 nodes, ~100 `new`, 3 receipts, `desired_retention 0.9`.
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

- Create `Mechatronics/GOAL.md`: active goal ONLY — name, actuator type, DOF, work
  envelope, success criteria, parked-history pointer, AND the semantic-pass checklist
  (seed = the canonical pattern list in §0 plus generic `arm|actuator` review; the §1
  task finalizes it as it rewrites). Today: QDD 2-DOF arm.
- Parked goals: `Mechatronics/goals/parked/<kebab-goal-slug>.md`, verbatim + superseded date.
- Goal change = replace GOAL.md + park old + re-derive Phase 3–5 artifacts AND flagged
  upstream goal-flavored examples (`Mechatronics/milestones/01_signals_actuators_dynamics.md:521`
  rig reuse, `Mechatronics/milestones/02_embedded_realtime_control.md:60,77,365` 2-DOF model,
  `Mechatronics/milestones/05_portfolio_delivery.md:13` QDD pedestal, ROADMAP Feeds-into claims).
- Skills persist: registry rows keep `Evidence tag` + `Goal era` column (§3); pre-swap rows
  BACKFILLED (acceptance: zero null `Goal era`); tags minted pre-swap stay valid history;
  post-swap tags get `<goal>-` prefix (e.g. `cnc-m3.1-mvm`). No tag retire rule.
- Parameterization tasks (mandatory): CONVENTIONS arm frame defaults → goal parameters;
  0.2/0.4/0.7 arm-flavored procedures reworded goal-neutral OR GOAL.md-listed appendices;
  `Science/` + `DataScience/` arm assumptions → `See [[Mechatronics/GOAL]]` pointers;
  `LAB_INFRASTRUCTURE.md` + `IDEAS.md` + `hardware/inventory.md` goal mentions get per-file
  disposition (parameterize / move to parked-goal appendix / delete with log line).
- Goal-era vocabulary: `pre-GOAL` (before GOAL.md existed) or `<goal-slug> (<date range>)`.
- Acceptance: canonical pattern over `Mechatronics/ Science/ DataScience/` returns ONLY
  `GOAL.md`, `Mechatronics/goals/parked/*`, Phase 3–5 milestone files, and GOAL.md-listed appendices —
  PLUS the semantic pass completed per the GOAL.md checklist.

## 2. Foundation split — Phase-0 pilot ONLY (phases 1–3 stay unsplit)

Target (verbatim bodies via `git mv` + explicit link-migration per moved file, incl.
pre-move `Mechatronics/firmware/` + `Mechatronics/simulations/` READMEs, `requirements.txt`, `template_*.py` — each gets: merge as dir
index / move with redirect header / delete-with-log-line, listed in the build commit).
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
| `lab/` | 0.10 + Phase-0 Pass/Deload (lines 25–46 and 578–599 of `Mechatronics/milestones/00_foundations.md` at time of writing — 578–599 covers photo, `versions.sh`, Retro) + SAFETY_CARD + CONVENTIONS + inventory refs | metrology + shared discipline |

Structural fixes (all mandatory, in this order):

1. **Primacy:** ROADMAP table is the ONLY ✅. Domain `Index.md` files are links-only
   (≤7 entries, no status, no checkboxes). Milestone bodies keep checkboxes with header:
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
2. **Anchors:** every milestone gets `<a id="m0-N"></a>`; ROADMAP + all new notes link
   `#m0-N` only. Migration script rewrites the ~40 ROADMAP rows, records old slugs as
   HTML comments (Daily history immutable — old links rot by design).
   `diagnose.py` extension spec: resolve `<a id="X">` definitions; accept link forms
   `[[File#X]]`, `(file.md#X)`, `#X` (same-file); skip code fences; skill IDs validated
   against §3 regex + registry membership. Must pass clean. Timing rule: full rescan per
   tag accepted; add incremental mode only if a run exceeds 60s (record timing).
3. **Evidence 2-home rule:** canonical = milestone-body checkboxes + git tag.
   `milestones/Phase 0/0.2.md` keeps narrative, drops nothing; `0.1.md` checkbox
   duplication is MERGED into the body with a redirect header (per-file action listed
   in the build commit). Daily notes reference status, never restate it.
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

- Location: `Mechatronics/skills/registry.md` (mech+software skills; piano/japanese/data
  skills explicitly deferred, not homeless-by-accident).
- Schema: `| Skill ID | Name | Evidence tag | Goal era | Project | Requires |`
  (`Requires` = comma-separated prerequisite skill IDs, empty ONLY for true entry
  points — 0.1-level — with `Requires: — (entry point)` written explicitly; blank = fail.)
- ID regex (gate-enforced): `^(sw|ee|mech|lab)-[a-z0-9-]+$`. Language token applies to
  `sw-` ONLY: `sw-c-…`, `sw-py-…`, `sw-cpp-…`, `sw-jl-…` (new `sw-` language token needs
  NO amendment; new PREFIX needs a one-line registry-header amendment). Shard to
  `Mechatronics/skills/<domain>.md` when data rows exceed 100.
- `Skills gained` format (gate-parseable, one per line under the heading):
  `- sw-py-csv-plot — CSV→PlotJuggler (tag m1.1-mvm, Goal era qdd-arm (2026-08–))`
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
(checks run + versions + result) — the file `audit-tags.sh` consumes.
Touched files = staged + unstaged working-tree files for `--dry-run`
(`git status --short`); for audits, the tag's commit range.
Tagging REFUSES (non-zero exit + reason) unless ALL pass:

1. Build+lint table (pinned in the script; gate FAILS CLOSED on unlisted extensions):
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
   in the registry; every registry row touched has non-null `Goal era` and its tag
   exists; every prerequisite taggerdate ≤ claimant taggerdate (§3 skill-order audit).
4. Links+lenses: extended `diagnose.py` (§2 item 2 spec) clean on touched files, INCLUDING
   the lens rule — any `status: proposed` lens in a touched milestone fails the gate
   (checked inside `diagnose.py`, not by hand).
5. Attestation: dated blank-page test note, e.g.
   `Mechatronics/milestones/Phase 0/0.2-attest-2026-09-07.md`
   (`<m>` = milestone number as in domain filename, `<date>` = YYYY-MM-DD):
   re-solve from memory, gaps red-penned; Full Pass note MUST cite a PRIOR attempt date
   (same-day echo fails); red-pen gaps appended to Landmine Log or linked.
6. Direct-`git-tag` bypass is detectable, not preventable: monthly
   `bash scripts/audit-tags.sh` (new: lists tags lacking gate receipts in
   `scripts/tests/receipts/<tag>.json`) + agent rule — never attest a bypassed tag;
   bypassed tags get `-unaudited` registry note until re-earned.

Gate ships with fixtures at `scripts/tests/fixtures/{refusal-1..7,clean}/` (the 7th =
skill-order violation: prerequisite dated after claimant), run by
`bash scripts/test-gate.sh` expecting 8/8. 8/8 or red.

## 5. Engram topics — engine-native WIP, JIT-cut, capstone-only builds

GATE: nothing in this section lands until v4 reconciliation (vault-scope proposal
landed + ENGINE_PIN green on the merge machine). Until then engram work stays
read-only or tmp-only (`ENGRAM_HOME=<tmpdir>`). Doctor-gating rule: preconditions
run on the merge machine with `python3 ~/engram/scripts/engram.py doctor`, and the
engine sha256 is recorded alongside results — uncompared shas gate nothing.

Preconditions (before ANY landing):

1. `doctor probe_gaps` clean on touched topics; scope approval covers pretest plan, node
   kinds, `practice` frames, contrast/viz/interactivity needs.
2. Dedupe via `analogous_to`/`retire` + `doctor` (NOT keyword diff): `static-equilibrium`×2,
   torque pair, Japanese verb clusters. Overlap check (exact-id + claim read) joins every
   scope approval.
3. Kind audit: absent ⇒ concept (no blind backfill); true fresh-instance procedures earn
   `procedure` + `practice` frame + `discriminates_from` + execution key + error bank.
   Counts include capstones (6 of today's 100 `new` are capstones — say so in reports).

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

Landings (scope approval each, maps-only, pretests included for frontier diagnosis):

- **Now (JIT, each node tied to a NAMED MVM checkbox — recorded in the scope-approval
  note, NOT in `why_chain`, which stays an id-path):** py CSV→PlotJuggler plot (M1.1),
  FFT+windowing (M1.2), `solve_ivp` pendulum (M1.4); C ring buffer + versioned telemetry
  framing (M1.5/M1.1). Parked until the demanding milestone is ACTIVE: packaging, OOP,
  CMake lore, FK-visualizer rebuild (M0.2 already ✅✅).
- **Atomicity law:** one claim per node, 5–15 min. Builds land ONLY as topic capstones
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

Order: §1-scaffold (GOAL draft + parked dir + `Goal era` column) → §4 gate build →
§2 split pilot + Completion-text swap (STAGED on §4) → §3 registry fill →
§5 landings (GATED on v4 reconciliation + PIN green) → §6 lenses.
Phase acceptance (ALL must hold): §1 grep-gate + semantic pass clean; anchor-aware
`diagnose.py` clean (or only `EXEMPT`-block items); gate fixtures 8/8; skill-order
audit (§3 skill-order audit) clean on the current vault (pre-existing inversions filed as defects, not
waived); cold-start test
(Phase-1 §5) still passes; FRESH reviewer agents on the same three briefs (alignment,
neuroscience, extensibility+onboarding) report zero blocking verdicts.
Re-verify loop: any failure → fix → re-run the failing brief(s) until clean.
