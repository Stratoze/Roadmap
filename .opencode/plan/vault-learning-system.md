# Plan: Vault Learning System - Engram Retirement + Phase-2 §5 Amendment

Status: APPROVED 2026-09-11 (user: "go"); implementation in progress. Reviewed
in three rounds by three reviewers (execution, pedagogy, retirement ops; round 3
CLEAN). All vault paths are vault-root-relative.

## 0. Decisions locked (user, 2026-09-11)

1. Engram is retired. Replacement: vault-native learning system in
   `.opencode/skills/`, `.opencode/agents/`, `_system/learning/`, `scripts/`.
2. Salvage from Engram: PREFERENCES ONLY - `_system/engram/learner-model.json` +
   `adaptations.jsonl` (interests, multi-lens strategy weights + ledger line,
   challenge band, meaningful settings, commitment cue verbatim + date with a
   stale marker). Everything else hard-deleted: graphs, FSRS state, due dates,
   misconceptions, receipts, artifacts, experiments.
3. Phase 2: amend the engram-coupled parts (preamble, §0, §4, §5, §7) and
   phase-1 §3; keep the rest (§1-§4/§6/§7 structure, gates, registry, lenses).
4. v1: study loop + mapping drill + resource dossiers + review maintain leg.
   Deferred: daily debrief skill, mermaid roadmap view, git automation,
   simulator builder, maker/viz agents.
5. Verbatim: private companion repo cloned at `_private/`. Public lesson notes
   carry summaries and links only; study productions (predictions, attempts,
   reflections) are private. Approved public-verbatim (prior practice): the goal
   scoping answer, misconception lines, the commitment cue. Daily/Changelog keep
   their existing practice (the learner's own journal; the agent pastes only
   learner-supplied text).
6. Credit: amosblomqvist/learn cited in the vault README and
   `_system/learning/README.md`; transition logged in `Changelog/`.
7. Preferences are mirrored to OpenViking memory (replacing the
   `engram-standing-orders` memory); `_system/learning/learner.md` stays
   canonical.

The per-concept loop is the learner's Loop (How to Learn): orient/scaffold
(zero-schema only) -> Predict -> Attempt -> Compare + feedback -> Integrate ->
Maintain. v1 of this plan said "teach -> struggle -> attempt", which inverted
the Loop; fixed here.

## 1. Verified starting facts (2026-09-11; re-check at build)

- Repo: `github.com/Stratoze/Roadmap`, public. `main` is protected by a server
  ruleset (unsigned pushes refused); commits are signed; `main == origin/main`;
  recent work landed on main directly. Tree clean.
- Engram store: `_system/engram/`, committed 2026-09-08 (`9205e59`; local
  rebuild began 09-05). 13 topics / ~270 nodes, 0 tracked receipts, 7
  misconceptions, 5 local receipt files, 2 artifacts, experiments empty;
  learner model created 2026-08-18. Content is architect-generated, unverified.
- Phase-2 landed: §1 scaffold (`Mechatronics/GOAL.md` confirmed,
  `goals/parked/`, registry skeleton), §3 registry (51 rows), §6 pilot lens
  blocks (10: `Lenses - m0-1` ... `m0-10`). NOT landed: §2 split
  (`Mechatronics/math|physics|lab` absent), §4 gate (`scripts/tests/` absent),
  §5, §7 acceptance.
- Engram global install (Win): `~/.config/opencode/` - `skills/{learn,review,coach}`,
  `skills/_shared/`, `agents/engram-*.md`, `scripts/engram.py`,
  `scripts/fuzz.py` (imports engram), `scripts/install-codex.sh` (runs engram),
  `opencode-engram-clean|smudge`, `.engram-smudge-template`,
  `.engram-version.jsonc`, `docs/` (engram docs), `experiments/` (engram
  designs), plugin entry `"opencode-engram-learning"` in `opencode.json`, and
  `opencode.json.bak.*` backups. No engram git filters are configured on this
  machine. No `ENGRAM_*` shell exports; `ENGRAM_ROOT` is injected by the plugin
  at runtime - verify it is gone after plugin removal + opencode restart.
- Tooling: `python3` 3.13.11 works in git-bash; `gh` is NOT installed - private
  repo creation is a user precondition. Windows Python crashes on non-ASCII
  output under cp932 unless `PYTHONIOENCODING=utf-8`; repo is LF
  (`* text=auto eol=lf`).
- opencode V2 (docs checked 2026-09-11): project skills
  `.opencode/skills/<id>/SKILL.md` (or `.md`) are discovered from the current
  dir to the project root and override global skills by ID; a skill needs a
  `description` to be advertised. Project agents `.opencode/agents/<name>.md`
  with `mode: subagent` need a `description`. Built-in `question` picker tool
  and `subagent` tool exist.
- Amos Blomqvist repo cloned at `%TEMP%\opencode\amos-learn` (read 2026-09-11).
  Port: `skills/teach` (probe -> plan -> teach; scoping + edge bracketing; quiz
  construction rules; LaTeX), `skills/visualize`, `agents/{researcher,mermaid-maker,
  svg-maker}` (render -> LOOK -> iterate), the quiz protocol. Do not port: pi
  extension code, md-log, visual-tools pipeline.
- OpenViking is available: tools `remember`, `write`, `edit`, `forget`, `read`,
  etc. Current memory: `viking://user/default/memories/preferences/user/
  engram-standing-orders.md` (engram-flavored standing orders).

## 2. Binding principles

1. **Admission bar.** Nothing is taught as established unless its source was
   verified. scout finds; verifier independently confirms (fetch it, confirm
   the human author, prefer primary sources, check the date, cross-check the
   claim). Unverified material is labeled provisional and never presented as
   fact.
2. **Orient before questions (zero schema), then Predict -> Attempt -> feedback.**
   A zero-schema topic starts with orientation (video / worked example / demo),
   then the Loop. The 3-tier struggle rule is skipped for zero-schema novices
   (How to Learn: scaffold FIRST, then predict).
3. **Mapping is scoped and provisional.** Scoping question first (what to DO,
   by when). Strands come from the goal plus a scout field scan (so unknown
   unknowns can enter). Edge found by bracketing (floor + ceiling). Self-report
   is never evidence. Mapping never gates teaching.
4. **Timely feedback.** Immediate after every attempt: answer + why + process
   gap. Confidence is collected before feedback. Answer keys for computable
   problems are computed by execution, never by inspection. Blind assessor only
   for claims (MVM / Full Pass) and sampled audits.
5. **Multi-lens.** Every concept gets an intuitive lens and a rigorous lens
   (strategy_weights 0.5/0.5 preserved). Rigorous claims are fact-checked
   against the dossier/verifier and cited; when lenses conflict, the conflict is
   named and the rigorous one wins.
6. **The learner produces.** AI never writes the artifact the learner is
   building (code, derivation, solution). AI Use Zones apply as written in
   `_system/How to Learn.md`: Red-zone work (safety design, final values,
   control gains, load ratings, mains/high-current) needs independent
   verification and is never AI-designed. Code problems: the learner writes, AI
   executes, verifies, and reviews. Tool skills are taught JIT as concepts.
7. **Struggle budget.** 15 minutes of solo attempt with attempts logged before
   any scaffold, except zero-schema. After hint_budget (2) scaffolds, switch
   strategy (worked example / lateral move) instead of adding hints.
8. **Privacy.** Raw productions, attempts, reflections, and confidence numbers
   -> `_private/` only. Public lesson notes carry summaries, links, and process
   notes. Approved public-verbatim: the goal scoping answer, misconception
   lines, the commitment cue. Daily/Changelog keep their existing practice. No
   AI inference is stated as learner fact; either a verbatim quote or a dated
   observation linked to its evidence.
9. **Anti-bloat.** v1 is one loop. Deferred items stay deferred until v1 has
   run at least two weeks.

## 3. v1 spec

### 3.1 Data

- `_system/learning/README.md` - system doc: purpose, design, provenance and
  citation, private-store pointer, commands, deferred list.
- `_system/learning/learner.md` - sections:
  - `## Preferences`: interests; multi-lens weights 0.5/0.5 + its 2026-09-03
    ledger line; challenge band (target_success 0.85, hint_budget 2);
    meaningful settings (default_mode, artifacts, momentum).
  - `## Standing orders`: the engram-free standing orders (global AGENTS.md
    keeps a thin pointer copy).
  - `## Commitment cue`: verbatim + date + `stale (names engram)` marker.
  - `## Mirrors`: OpenViking memory URI; global AGENTS.md pointer.
- `_system/learning/curriculum/<topic>.md` - created from the pinned skeleton
  (Appendix A) by `study` step 0 (new topic) or `map` on first contact.
- Concepts state machine: `unknown -> seen` (first contact/orientation),
  `seen -> review` (taught + first schedule), `review -> solid` (clean recall at
  rung >= 4); `solid -> review` on a miss. No other transitions. Mapping
  estimates live in `## Map` as `provisional (<date>)`, never in `state`.
- `_system/learning/lessons/<topic>/YYYY-MM-DD-<slug>.md` - sections exactly:
  `## Target`, `## Predict` (summary; verbatim in `_private/`), `## Orientation`,
  `## Attempts` (what happened; where the verbatim lives), `## Feedback`
  (the gap), `## Reflection` (summary; verbatim in `_private/`), `## Confidence`
  (recorded privately; note the receipt path, no numbers public), `## Next`
  (concept id + `next_review`). No scores, XP, or streaks.
- `_private/learning/verbatim/<YYYY-MM-DD>-<topic>.md` - raw learner text.
- `_private/learning/receipts/<YYYY-MM-DD>-<topic>.jsonl` - confidence picks,
  grades, assessor outputs.

### 3.2 Skills (`.opencode/skills/`, each with frontmatter `name` + `description`)

- `study/SKILL.md`:
  0. New topic: create the topic file from Appendix A; ask the scoping question
     (goal + by when, verbatim); spawn scout for a goal-bounded field scan
     (provisional concepts, strands, common gotchas); learner prunes; the scan
     seeds `## Map` and inserts the pruned one-claim aims as `unknown` rows in
     `## Concepts` (rows must exist before any `review.py schedule` call).
  1. Load topic file + `learner.md`. Preflight: `[ -d _private/.git ]` else
     pause verbatim capture and tell the learner to clone (public summaries
     continue).
  2. Dossier check; spawn scout + verifier in the background if missing.
  3. Frontier: first `unknown`/`seen` concept whose prereqs are
     `review`/`solid`. Comfort branch ("test me in"): one mid-map probe; hit ->
     walk the unreceipted prereqs; miss -> drop below. If no bracket exists,
     proceed with orientation and bracket as you go. Mapping never blocks.
  4. Per concept: motivate -> predict ("I expect ___ because ___") -> attempt
     (struggle budget; hint count) -> compare (answer key by execution) ->
     immediate feedback (confidence picked before it) -> establish/derive
     (Socratic where reachable, expository otherwise; intuitive lens then
     rigorous lens) -> connect -> check (one compressed verify) -> record
     (state, rung 0 via `review.py schedule`, confidence to private receipts).
     Zero-schema concepts get orientation before predict; no quiz before schema.
     Checks routinely above target_success (0.85) -> escalate difficulty or
     advance; far below -> shrink the chunk or scaffold before proceeding.
  5. Repeated lapses: re-encode differently (analogy, contrast, or an offer to
     build an explorable - deferred in v1 to a plain worked variant).
  6. Reflection: learner writes; summary public, verbatim private.
  7. Close: one next step; offer the stale commitment cue once (verbatim, never
     rewritten); no recap wall.
  Bans: no quiz before schema; no answer before an attempt; no AI-written
  solution or derivation; no unverified claim as established; no AI-generated
  video; no scores or streaks.
- `map/SKILL.md`:
  1. Scoping question (goal + by when) if not already in the topic file.
  2. Scout field scan -> provisional concept/strand list -> learner prunes.
  3. Question rounds, one strand at a time: broad open -> gradable probes ->
     narrow. Quiz where gradable, conversation where not. Cap: 6 gradable
     probes per sitting (continue only if the learner asks).
  4. Bracket each strand: one floor (right) + one ceiling (miss). All-correct ->
     escalate. One miss -> characterize (slip, gap, misconception) with
     adjacent probes before concluding. Self-report is never evidence.
  5. Zero schema -> stop, hand to `study` for orientation.
  6. Write `## Map` provisional notes and only unambiguous `state` changes;
     revise from lesson evidence. Never gates teaching.
- `resources/SKILL.md` - JIT per active topic:
  1. scout: candidates (title, creator, URL, type, claim covered).
  2. verifier: independent fetch + check (human author, primary source, date,
     claim cross-check) -> verdict in the entry.
  3. Pinned entry format (Appendix A); rejected stays listed as rejected.
  4. Re-verify only on trigger: fast-moving field, a lesson contradiction, or
     learner request. Resources are dated snapshots.
- `review/SKILL.md`:
  1. `python3 scripts/review.py due` - cap 12 per sitting.
  2. Backlog over cap: one amnesty line; offer capped set / catch-up / not now.
     No guilt, no streak language.
  3. Per item: free recall cold (no re-exposure first) -> confidence pick ->
     immediate feedback + gap -> on lapse, criterion loop (re-derive,
     interleave, re-ask; max 3 passes, stop at one clean recall).
  4. Outcome -> `review.py next`: hit -> rung +1 (cap 5); hard -> same rung;
     miss -> one rung back + a same-session relearn attempt; still shaky after
     that -> `review.py schedule <topic> <id> 0` (reset). Two+ lapses ->
     re-encode differently.
  5. Claims (MVM / Full Pass) route to the assessor; ordinary reps do not.
  6. Close: counts + next due date. No streaks.

### 3.3 Agents (`.opencode/agents/`, frontmatter `description` + `mode: subagent`)

- `scout.md` - research briefs, resource candidates, field scans. Multi-angle
  search; primary sources first; output = candidates + kept/dropped + gaps,
  each with provenance.
- `verifier.md` - independent adversarial check of scout output. Must fetch and
  read sources; per claim: verified / unverifiable / rejected + evidence line.
  Never shares context with scout.
- `assessor.md` - blind grading for claim gates and sampled audits. Never sees
  the lesson or the dialogue; returns grade, gap, and misconception lines
  verbatim.
- Deferred: makers (mermaid/svg), simulator smith.

### 3.4 Scheduler (transparent, vault-native)

- Ladder `[1, 3, 7, 16, 35, 90]` days; rung 0-5.
- `python3 scripts/review.py due` -> one line per due row
  (`topic | id | state | rung | next_review`), sorted by (topic, id); due =
  `next_review <= today`; empty output, exit 0 when none.
- `python3 scripts/review.py schedule <topic> <id> [rung]` -> writes `rung`
  (argument; else current; else 0), `next_review = today + ladder[rung]`, and
  sets `state = review` when the state is `unknown`/`seen`; prints the row,
  exit 0; unknown row -> stderr, exit 2.
- `python3 scripts/review.py next <topic> <id> <hit|hard|miss>` -> applies the
  rule (hit +1 cap 5; hard same; miss -1 floor 0), writes the new rung,
  `next_review = today + ladder[new rung]`, and state: a clean hit at rung >= 4
  -> `solid`; a miss demotes `solid` -> `review`; prints the row, exit 0;
  unknown -> stderr, exit 2.
- `python3 scripts/review.py selftest` -> in-memory ladder/table fixture checks,
  exit 0/1.
- Row creation: only study step 0 creates rows (the concepts table is the source
  of truth); `schedule` and `next` never upsert.
- Parsing: only rows inside `## Concepts`; skip header and separator; split on
  `|`, trim; malformed rows get a stderr warning carrying only file:line (never
  row content, to avoid cp932 output issues) and are skipped. Dates ISO
  `YYYY-MM-DD`, local date. Writes `encoding='utf-8', newline='\n'`; output
  ASCII; `PYTHONIOENCODING=utf-8` set by the caller where needed. No network.
  Target: under ~150 lines.
- Tradeoff accepted and documented: simpler than FSRS, chosen for transparency
  and clean Mac/Win git merges (markdown, no `-merge` attribute needed).

### 3.5 Private companion repo

- Setup order matters:
  1. Add `_private/` to `.gitignore`; verify `git check-ignore -q _private/`.
  2. Guard `scripts/save.sh`: if `_private` exists and is not ignored, refuse
     (`git check-ignore -q _private/ || { echo "BLOCKED: _private not ignored"; exit 1; }`).
  3. User creates the private repo (`Stratoze/Roadmap-private` or other name)
     and provides the clone URL (no `gh` on this machine).
  4. Clone it at `_private/`; layout `_private/learning/{verbatim,receipts}/`.
  5. Add `_private` to Obsidian excluded files (user setting).
  6. Patch `scripts/diagnose.py`: skip `_private` in `md_files` and add it to
     `ORPHAN_EXCLUDE_DIRS`.
- Study preflight: if `_private/.git` is missing, pause verbatim capture with a
  one-line instruction; public summaries continue.
- `_system/learning/README.md` documents the setup (public-safe).
- Acceptance: `git ls-files _private/` empty; `git check-ignore -q _private/`
  passes on both machines.

### 3.6 Credit and transition log

- `Changelog/2026-09.md` gets a section in the file's existing style, e.g.
  `## 2026-09-11 - Engram retirement` (use the actual build date): reason,
  scope, what was deleted, what replaced it, verification output (the public
  grep result, `rm -rf` + ignore checks, acceptance results), Mac status. Never
  paste output sourced from `_private/`.
- Vault `README.md`: one line crediting Amos Blomqvist's learn system with a
  link to `_system/learning/README.md`.
- `_system/learning/README.md` `## Provenance`: what was borrowed (probe ->
  plan -> teach, scoping-first mapping, quiz construction, researcher pattern,
  makers, LaTeX, unconditional truths) and what was added (verification
  pipeline, struggle rules, multi-lens, review/maintain leg, evidence gates,
  vault-native store, private verbatim).

### 3.7 OpenViking mirror

- Write a new memory `viking://user/default/memories/preferences/user/
  learning-preferences.md` (via the `openviking` write tool; `remember` is also
  acceptable) with the content of `learner.md` `## Preferences` + `## Standing
  orders`, engram-free.
- After the new memory exists and the user confirms: `openviking forget` the old
  `engram-standing-orders.md` (irreversible - confirm first).
- `learner.md` is canonical; the memory is a session-visibility mirror; note the
  URI in learner.md. Verify the old memory no longer appears in session-start
  context.

## 4. Amendment edit set (phase-1, phase-2, AGENT.md, How to Learn)

- phase-2 file: preamble lines 14-19 (runner definition + subcommand list) ->
  replaced by a new-system note; §0 line ~70 cue mention -> updated; §0 lines
  ~77-89 ("Engine facts ...") -> replaced; §4 parenthetical (`ENGRAM_HOME`
  exported per `_system/engram/env.example.sh`) -> replaced wholesale; §5
  section (heading contains an em-dash; match by `## 5.`) -> replaced with
  "Curriculum store" per this plan; §7 cold-start step 0/1 (runner env +
  `due --cap 12`) -> the Appendix B check; any remaining engram mention ->
  explicitly marked historical, never operative. Line numbers are as of
  2026-09-11; re-grep at build (`grep -n engram .opencode/plan/phase-2*`).
- phase-1 file: replace every engram reference (facts ~14/22/26-27/42/55, §3
  loop + fallback ~76-99, non-goals ~133; re-grep at build). No engram
  machinery remains operative.
- `AGENT.md`: engram lines ~16, 22-24, 31-34, 77, 85 replaced; session-start
  block becomes Appendix B; everything else unchanged.
- `_system/How to Learn.md`: the Memory / SRS Strategy section rewritten to the
  new system and MUST keep: Anki = Japanese vocabulary only; the routing rule
  (reconstruct -> spaced review; recognize/produce instantly -> Anki); no
  double-SRS; and remove the "Engram owns..." sentences.

## 5. Engram retirement checklist (ordered; Win first, Mac mirrored after)

1. Salvage preferences into `learner.md` + OpenViking memory (§3.7).
2. Private repo setup in the pinned order (§3.5).
3. Vault cleanup - edit/remove:
   - `AGENT.md`, `_system/How to Learn.md`, `README.md`, `index.md`,
     `DataScience/Index.md`, `Japanese/Index.md`, `Japanese/Resources.md`,
     `Science/Index.md`, `Piano/Resources/Maintenance and Performance.md`,
     `Piano/Resources/Progression.md`, `Piano/Resources/Repertoire and 12-Week
     Goals.md`, `Piano/Resources/Resource List.md`,
     `_templates/mech/stress_inoculation.md`, `_templates/piano/12-Week Goal.md`,
     `_templates/piano/Weekly Review.md`,
     `Mechatronics/milestones/00_foundations.md`.
   - `.gitattributes`: drop the `_system/engram/graphs/*.json -merge` and
     `_system/engram/artifacts/** linguist-generated` lines.
   - `.gitignore`: add `_private/`; do NOT drop the engram receipt ignore lines
     until step 4 completes.
4. Hard delete the store (order matters because ignored verbatim files are on
   disk): `git rm -r _system/engram/` -> `rm -rf _system/engram/` -> remove the
   receipt ignore lines -> verify `git status --ignored _system/engram` is
   empty and `git status --short` is clean.
5. Global cleanup (Win): delete `skills/{learn,review,coach}`, `skills/_shared/`,
   `agents/engram-*`, `scripts/engram.py`, `scripts/fuzz.py`,
   `scripts/install-codex.sh`, `opencode-engram-clean`, `opencode-engram-smudge`,
   `.engram-smudge-template`, `.engram-version.jsonc`, `docs/` (engram docs),
   `experiments/` engram designs; strip the engram block from
   `~/.config/opencode/AGENTS.md` (lines 1-25 as of 2026-09-11) and leave a thin
   pointer to `_system/learning/learner.md`; remove the plugin entry from
   `opencode.json`; delete backups (`opencode.json.bak.*` and
   `_backup_20260904-194135/`) with consent; restart opencode; confirm
   `ENGRAM_ROOT` is unset. Branches: delete `engram/coordination` and
   `engram/vault-scoped-proposal` (local + origin) with consent after the Mac
   confirms abandonment. OpenViking: §3.7. Residual grep
   (`grep -ri engram ~/.config/opencode`) must return nothing outside OpenViking
   session state and any explicitly kept backups; log kept files in the
   Changelog entry.
6. Mac mirror: the same global deletions + plugin entry + env check + `_private`
   clone + verification; record in Changelog (done or dated deferral).
7. Log + credit (§3.6).
8. Acceptance (§7).

## 6. Sequencing

- A - Setup: preferences salvage, learner.md, OpenViking memory, private repo
  setup + guards, `_system/learning/README.md`.
- B - Teach: study/map/resources skills + scout/verifier agents +
  `scripts/review.py` (study depends on its `schedule` command); run ONE real
  topic lesson end-to-end; first review scheduled for the next day.
- C - Maintain: `review/SKILL.md`; run the due review the next day.
- D - Retire: checklist §5 + amendment §4; acceptance §7.
- One commit per step. Pushes only with consent (protected main).

## 7. Acceptance (cold start)

1. Fresh session: the Appendix B block runs with zero engram machinery and
   produces at most one nudge.
2. One real study run produces: topic file from the skeleton; verified dossier
   entries; orient -> predict -> attempt -> feedback sequence; lesson note with
   summaries; private verbatim + confidence; `next_review` set.
3. One due review (the next day): cold recall first, immediate feedback, row
   updated by `review.py`.
4. `grep -ri engram --exclude-dir=.git --exclude-dir=.opencode
   --exclude-dir=_private .` returns only `Changelog/`, `Daily/`, and two
   historical lines in `learner.md` (the stale cue + the old-memory pointer).
   `.opencode/plan/**` is historical and intentionally excluded. No `_private/`
   output is ever pasted into tracked files.
5. `git ls-files _private/` empty; `git check-ignore -q _private/` passes;
   `git status --ignored _system/engram` empty.
6. README credits Amos; `_system/learning/README.md` exists; Changelog entry
   present; OpenViking `learning-preferences` memory present and the old memory
   gone; `~/.config/opencode` grep clean per §5.5; Mac cleanup done or
   explicitly dated.

## 8. Deliberately out (anti-bloat)

Daily debrief skill (existing Daily flow stays, engram refs removed only);
mermaid roadmap view; git automation; simulator builder; FSRS/headless engine;
engram migration beyond preferences; custom quiz plugin; maker/viz agents (until
a lesson needs a visual twice).

## 9. Open questions (non-blocking)

- Private repo name (decide in step A; user creates it).
- Ladder rung lengths after first real use.
- Daily debrief later: own skill or folded into the study close.
- Assessor sampling rate for claim gates.

## Appendix A - curriculum file skeleton (pinned)

```markdown
# <Topic>

## Goal
- Scoping answer (verbatim, <YYYY-MM-DD>): "<learner's words>"
- By when: <YYYY-MM-DD or none>

## Map
- [mermaid graph TD block: few nodes, short labels]
- Provisional (<YYYY-MM-DD>): strand <name> bracketed (floor: <x>, ceiling: <y>);
  strand <name> unbracketed

## Concepts
| id | aim | prereqs | state | rung | next_review | evidence |
|----|-----|---------|-------|------|-------------|----------|
| c1 | <one claim-sized aim> | - | unknown | 0 | - | - |

## Resources
- rigorous | <title> | <creator> | <url> | unverified
- intuitive | <title> | <creator> | <url> | verified <YYYY-MM-DD>
- interactive | <name> | <creator> | <url> | verified <YYYY-MM-DD>

## Misconceptions
- <YYYY-MM-DD> c1 - "<learner's words>" (or: dated observation, evidence: <link>)

## Log
- <YYYY-MM-DD> - <one-liner>
```

## Appendix B - session-start block (replaces the engram runner protocol)

```bash
python3 scripts/review.py due
test -f "Daily/$(date +%F).md" && echo "note: exists" || echo "note: missing"
```

- If the due output is non-empty or the note is missing: ONE message:
  `Due: N (topics: ...) | Today's note: missing/exists.` + optionally one direct
  quote from the last 7 days (file + date) + one question offering action.
- Otherwise: silence.
- Never repeat after a same-day decline; never auto-create the note; no hooks,
  no Telegram, no background jobs.
