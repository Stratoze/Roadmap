# IMPLEMENTED DESIGN RECORD — Japanese Tutor, JIT Sources, and Lean Learning System

> **Historical context, not operative procedure.** The active contract is
> `AGENTS.md`; active procedures are `.dsh/skills/`, `scripts/`, `Japanese/CURRENT.md`,
> and `Mechatronics/CURRENT.md`. Do not treat the design sections below as a
> second protocol.

**Status:** IMPLEMENTED — changes landed 2026-09-26; validation evidence recorded in `Changelog/2026-09.md`.
**Approval:** user approved the plan before implementation.

## 1. Objective

Implement the learner's accepted learning design while reducing procedural and documentation waste:

1. Add a Japanese daily tutor that coordinates grammar, i+1 conversation, reading, immersion, Anki boundaries, and freshness-aware reuse.
2. Add an explicit technical-session flow: roadmap delivery and dependencies first, learner-selected/read source material, cold conceptual probing, a real break, fresh transfer, implementation/theory testing, Feynman correction when needed, and MVM/Full Pass evidence.
3. Make the raw Mechatronics roadmap answer:
   - what must be delivered;
   - what it depends on;
   - keywords for finding material;
   - the safety/evidence boundary.
4. Remove or stage stale source catalogues, duplicated navigation, retired harness mirrors, and print-only pseudo-tools without deleting learner work, evidence, safety material, or provenance.
5. Treat the current `AGENTS.md` and other existing documents as **migration inputs, not unquestionable authority**. Reconcile contradictions instead of preserving them by default.

## 2. Learner decisions already fixed

These are design inputs, not new questions:

- Japanese ordinary-day budget: 4–5 hours total.
- Immersion: approximately 3 hours.
- Anki: approximately 30 minutes.
- Deliberate Japanese work: sustainable 30–90 minutes; weekends may extend reading/output, not automatically add more grammar.
- Japanese style: Japanese-first explanation where possible, with a clear English bridge; compare neighbouring structures, situations, register, pitfalls, and native-style intuition. Native-style claims beyond the cited source must be labelled as sourced observation, learner report, or hypothesis.
- Conversation: i+1; introduce useful new vocabulary/grammar and use it immediately.
- Reading gate: the learner completes 30 actual novel-reading sessions with an English explanation first; after the 30th session, Japanese attempt comes first, followed by English explanation/correction. Sentence-analysis fallback sessions do not count toward the 30.
- If reading is skipped: one level-appropriate sentence-analysis task, not a rigorous grammar exam.
- Anki owns Japanese vocabulary. The vault owns grammar, output, reading, immersion, and evidence.
- Books/videos are not stockpiled. When an active topic needs a book/source, the learner asks the tutor for it; the tutor uses scout/verifier on demand, records only that active locator, and does not prebuild a source library. A learner-supplied book may be used.
- Old material is used when it fits, not only when formally due. Nothing is forced merely to satisfy a counter.
- Technical tests must not repeat the exact question; the same construct with a fresh context is allowed.
- The technical break is a gate before the post-break transfer. If the break cannot be evidenced, the post-break result is not claimed as complete.

## 3. Current-state findings

Read-only impact and waste scouts found:

- `study`, `map`, `resources`, and `review` exist, but there is no Japanese-session or technical-session orchestrator.
- `scripts/review.py` has a fixed seven-column concept parser and no usage/freshness model. It silently skips malformed rows and invalid dates in some paths.
- There is no inspected Anki bridge. The system can record learner reports of mining, but cannot independently claim complete Anki knowledge.
- Technical curriculum uses both `## Sources` and `## Resources`; active skills expect `## Resources`.
- Source inventories are primarily in milestone files and inactive curriculum files, not the raw roadmap.
- `Mechatronics/ROADMAP.md` also contains live safety, evidence, dependency, MVM/Full Pass, and Skill Spine policy. Reduction must not remove those.
- `topic-tree.md` says “names only” but contains substantial detailed material that overlaps milestones and curriculum.
- Japanese grammar has real evidence and an unfinished potential-form re-encode. “From the ground up” means re-explain dependencies from first principles when needed; it does not erase or reset the map.
- `japanese-immersion.md` says “no quotas” while suggesting one mined item per session. Remove the ambiguity.
- No question-signature persistence, break timer, or technical test runner exists. This pass will use append-only records and procedural timestamps, not build a large runner.
- Current learner standing orders still say books/videos are supplied for each lesson and phase. They must be rewritten to match JIT source acquisition.
- `Mechatronics/Index.md` pointing at the latest Daily for milestone state while `AGENTS.md` says ROADMAP is the only status owner — now resolved: `Mechatronics/Index.md` reads "Current milestone status: Roadmap only".
- The roadmap's milestone order is now resolved and implemented: evidence → flip → commit → signed tag. `scripts/milestone.sh` refuses to tag on an unclean tree and says so.

## 4. Target ownership and protected content

One fact gets one active owner:

```text
AGENTS.md                  short operating contract, boundaries, routing
How to Learn.md            learning method, not topic state
learning/README.md         layout, ownership, and data contracts
learner.md                 learner words, preferences, standing orders
topic-tree.md              short hierarchy and dependency map
Mechatronics/ROADMAP.md    status, deliverables, dependencies, keywords, safety
milestones/*.md             acceptance, project detail, landmines, evidence links
curriculum/<topic>.md      concepts, state, misconceptions, problems, active locator
.dsh/skills/*              procedures
.dsh/agents/*              bounded roles
Anki                       Japanese vocabulary
_private/                  raw learner productions
lessons/evidence           public summaries and technical evidence
Changelog/                 append-only historical decisions
archive/                   historical material, never active procedure
```

Never delete or destructively rewrite:

- `Daily/**`
- `_private/**`
- `_system/learning/lessons/**`
- `Mechatronics/milestones/evidence/**`
- `Mechatronics/docs/captures/**`
- `Mechatronics/data/**`
- hardware/project evidence referenced by milestones
- `Mechatronics/resources/SAFETY_CARD.md`
- `Mechatronics/GOAL.md` learner-confirmed goal content
- learner-authored goals/scoping answers
- signed milestone tags
- Changelog history

The implementation may **append** new lesson evidence, technical-session records, and Changelog entries. It may not remove or rewrite existing evidence. `bash scripts/save.sh` must not be used for broad cleanup because it stages with `git add -A`; cleanup commits require a reviewed path manifest.

Additional boundaries:

- Passive reading/immersion exposure is evidence, not natural-use credit.
- Raw learner productions, including reading attempts, go only to `_private/`.
- Novel screenshots and long passages are transient inputs and are never persisted.
- Anki knowledge claims are learner-reported until a bridge exists.
- Unverified/rejected source decisions move to `_system/learning/archive/source-ledger.md`; they are not silently deleted.
- `_system/learning/archive/**` is protected provenance in this implementation, except for the explicitly approved thin retired OpenCode/Codex harness mirrors, which may be deleted after a reference check.

## 5. Exact file changes

### A. Active contract and method

#### `AGENTS.md` — rewrite, not append

Reduce it to:

- session-start and session-end protocol;
- privacy/evidence boundaries;
- sequencing and handoff;
- JIT source policy;
- one-adaptive-question discipline;
- safety and learner-production rules;
- pointers to method, README, learner state, skills, and review commands.

Remove stale machine facts, duplicated teaching/review procedures, unrelated issue/domain instructions if those workflows are retired, and any wording that makes this a second curriculum.

Use this source rule:

> Raw roadmaps contain deliverables, dependencies, and keywords. A source is resolved only when its topic activates. When the learner needs a book or source, the tutor uses the resource/scout/verifier flow on demand, records the active locator, and does not prebuild a source library. The tutor may faithfully restate or translate a cited source into Japanese without adding new claims; any explanation beyond the source is a documented sourcing blocker. Never substitute an unsourced AI lecture for a missing source.

#### `_system/How to Learn.md`

Keep the method. Add:

- natural-use freshness is separate from review scheduling;
- passive exposure is not use;
- attempted/incorrect use is not clean use;
- the four-step cold verification checklist that currently exists only as a print reminder.

#### `_system/learning/README.md`

Document:

- Japanese and technical session skills;
- canonical `## Resources` schema;
- append-only usage events;
- JIT source acquisition;
- roadmap/source ownership;
- private evidence and Anki boundaries.

#### `_system/learning/learner.md`

Preserve learner evidence and update only accepted current direction:

- 4–5 hour Japanese budget and split;
- on-demand source policy;
- 30-session reading mode;
- Japanese explanation style;
- introduced/practised/mined/independently-produced vocabulary distinction.

Rewrite standing orders 5, 8, and 9 so they say:

- a source is selected/verified for the activated concept, not for every future lesson/phase;
- the learner may supply a book;
- the tutor may faithfully translate/restate a cited source into Japanese;
- unsourced additions are blockers/hypotheses, not established teaching;
- no standing source library is maintained.

Remove stale OpenCode/Engram references only when historical and unnecessary to interpret evidence.

#### `_system/learning/topic-tree.md`

Keep a short hierarchy, dependency map, and links. Move long worked chains, repeated detailed descriptions, and obsolete review notes to a new historical file:

```text
_system/learning/archive/topic-tree-details.md
```

The active tree must not contain source lists or duplicate milestone/curriculum detail.

#### `README.md` and `index.md`

Update only pointers if the new skill names or ownership boundaries make the current entry points misleading. Do not duplicate the operating contract.

### B. Japanese tutor

#### New `.dsh/skills/japanese/SKILL.md`

Compose, do not duplicate, `resources`, `study`, `review`, the four Japanese curriculum files, and Anki as vocabulary owner.

Operational defaults:

- 30-minute deliberate session: short old-use/grammar contrast, conversation, and one reading/analysis task.
- 60-minute session: 15 minutes grammar, 15 minutes conversation, 30 minutes reading.
- 90-minute session: 20 minutes grammar, 20 minutes conversation, 50 minutes reading/analysis.
- The 3-hour immersion and 30-minute Anki blocks are separate protected inputs/maintenance, not extra tutor bookkeeping.
- No mandatory pre-work form. The four-field brief is optional context after work starts.
- Load the current frontier from curriculum/map/log evidence. Do not hardcode a new starting concept or reset an unfinished one.
- “Ground up” means explaining the dependency chain from sentence skeleton/particles again when needed, while preserving evidence.

The skill must:

1. Request/resolve a source JIT when a new grammar concept needs one.
2. Teach one usable contrast from the verified locator.
3. Explain Japanese first where appropriate, then English bridge.
4. Compare neighbouring structures, situations, register, and pitfalls.
5. Practise immediately.
6. Run an i+1 conversation.
7. Reuse old grammar when natural, regardless of due date.
8. Use English-first reading mode for the first 30 actual novel-reading sessions; after the 30th session, Japanese-first mode. Sentence-analysis fallback does not count toward the 30.
9. Use a learner-chosen novel; do not silently substitute a recommended title.
10. If reading is skipped, give one level-appropriate sentence-analysis task.
11. Record four evidence states:

```text
introduced   deliberate teaching/selection, not passive encounter
practised    deliberate attempt, not necessarily correct
mined        learner reports selecting a vocabulary item for Anki
produced     independent correct use
```

`mined` is not a knowledge claim. Without an Anki bridge, Anki state remains learner-reported.

Privacy/evidence:

- raw attempts go to `_private/`;
- public records contain summaries and links only;
- screenshots/passages are not persisted;
- passive exposure does not update usage;
- usage events link to lesson/evidence records.

#### Japanese index/resources/curriculum

- `Japanese/Index.md`: remove hardcoded/stale “start” pointer; route to due review, current frontier, immersion, and the new session modes.
- `Japanese/Resources.md`: retain stable discovery links and Anki boundary; remove duplicated grammar source choices; make learner choice/novel workflow explicit.
- `japanese-grammar.md`: preserve evidence and unfinished potential work; add usage-event semantics and frontier handling.
- `japanese-output.md`: define conversation/output evidence, 30/60/90 shapes, and “use within the next relevant session; within seven days when feasible” rather than a rigid daily quota.
- `japanese-reading.md`: define the 30-session English-first mode, later Japanese-first mode, page context, learner attempt, and fallback.
- `japanese-immersion.md`: optional event logging, no mining quota, no streaks.

### C. Technical session and roadmap

#### New `.dsh/skills/technical/SKILL.md`

Compose `map`, `resources`, `study`, `review`, and `assessor`; do not create a second scheduler.

The exact flow:

1. Select the next eligible topic from roadmap dependencies, due reviews, and curriculum state.
2. Give the learner the deliverable, dependencies, and search keywords.
3. Ask the learner to choose/request a source and read it first.
4. Record the selected locator only after the topic activates.
5. Cold Socratic conceptual check, one adaptive question at a time.
6. Start and end an actual break using system-clock timestamps. Duration is checked. If the break cannot be evidenced, do not claim the post-break stage is complete.
7. Fresh conceptual transfer using the same construct but a different prompt/context.
8. Implementation/theory test; learner writes the artifact.
9. If failure exposes a gap, learner gives a Feynman-style simple explanation, then solves a fresh transfer problem.
10. Blind assessor receives claim, rubric, question, production, and evidence pointers; it does not receive raw private context unless explicitly permitted.
11. Record MVM/Full Pass evidence and stage the next review.

#### New `_templates/learning/technical_session.md`

A post-work record template, not a pre-work gate:

```text
Target / Source locator / Learner-produced attempt
Cold conceptual check
Break start / Break end / elapsed
Fresh transfer prompt
Implementation/theory test
Feynman correction (if triggered)
Assessor brief/result
Question variants / Evidence paths / Next
```

The public template stores summaries and paths only. Raw attempt fields belong in `_private/`.

#### `.dsh/agents/assessor.md`

Add an input contract for the technical session:

- claim and rubric;
- exact question and fresh-variant question;
- learner production or permitted file path;
- execution permission where applicable;
- evidence paths;
- private-data boundary.

Add explicit output fields:

```text
per_criterion: criterion -> pass|partial|fail|probe_gap
gate_requested: mvm|full|none
gate_met: yes|no
gate_earned: mvm|full|none
blockers:
error_class:
```

A `partial` or `lapsed` verdict cannot earn MVM or Full Pass. A gate is earned only when every required criterion for that gate passes. Full Pass additionally requires fresh transfer and implementation evidence when those are part of the claim. Preserve blind assessment and deny unrelated context.

#### `Mechatronics/ROADMAP.md`

Keep only active status, deliverables, dependencies, concise keywords, safety boundaries, and canonical MVM/Full Pass/evidence rules.

Use a canonical milestone schema:

```markdown
| Milestone | Status | Deliverable | Depends on | Search keywords | Safety/evidence boundary |
|---|---|---|---|---|---|
```

The status column is the only active milestone status. Milestone checkboxes become frozen acceptance history, not a second current-status source.

Move detailed Skill Spine policy to `Mechatronics/skills/registry.md` under `## Assessment policy`; keep the assessor role in `.dsh/agents/assessor.md`.

Speed runs are optional recommendations. After completing a phase, ask whether the learner wants to do the next speed run or move on. They are not commitments and are not part of the raw deliverable/dependency table.

#### `Mechatronics/milestones/*.md`

Keep deliverables, acceptance criteria, dependencies, safety, landmines, evidence requirements, retro/history, and evidence links. Stage/remove only inactive learning-source metadata. Never remove videos that are required evidence artifacts.

#### `Mechatronics/Index.md`

Remove the Daily pointer as a current-status source. Make ROADMAP the only active milestone status owner. Keep evidence links pointing to the evidence index.

#### `Mechatronics/IDEAS.md`, `GOAL.md`, `skills/registry.md`

- Keep all three.
- Add Skill Spine assessment policy to `registry.md`.
- Move speed runs to `IDEAS.md` as optional recommendations and ask after each phase whether to run the next one or move on.
- Keep the `GOAL.md` migration checklist as historical content or move it to an archive copy with a link; do not delete it.

#### Technical curriculum files

Normalize `## Sources` to `## Resources` in every active technical curriculum file:

```text
m0-1 through m0-10
math-odes.md
physics-first-principles.md
python.md
```

Every active entry must use the existing dossier format with concept IDs and a verdict. Inactive alternatives move to `_system/learning/archive/source-ledger.md`; rejected/unverified records are not silently deleted.

Fix `_system/learning/curriculum/math-odes.md`'s stale `_system/learning/overview-map.md` link to `_system/learning/maps/overview.md`.

### D. Review usage model

Do **not** add mutable usage columns to the existing concept table. The current seven-column rows already contain evidence, and rewriting them risks losing history.

Add an append-only `## Usage events` section to each curriculum file that has a `## Concepts` table. Event format:

```markdown
## Usage events
| date | event_id | concept/item_ref | event | evidence | public note |
|------|----------|------------------|-------|----------|-------------|
| YYYY-MM-DD | opaque-id | id-or-opaque-ref | introduced | lesson-or-private-path | short summary |
```

Allowed events:

- `introduced`: deliberate teaching/selection, not passive encounter;
- `practised`: deliberate attempt, not necessarily correct;
- `produced`: independent correct use;
- `mined`: vocabulary event only; learner-reported selection for Anki;
- `reading_session`: one actual novel-reading session; fallback analysis never uses it.

`mined` uses an opaque Anki note ID if available, otherwise an opaque event ID. It never creates a vault vocabulary state or stores the source passage.

`review.py` gains:

```text
usage <topic> <id> <event> <evidence-path> [public-note]
usage <topic>                             read-only derived last-used listing
```

`review.py` derives:

- `last_used`: most recent `practised`, `produced`, or `reading_session` event;
- `last_clean_use`: most recent `produced` event;
- `sessions`: count of `reading_session` events for the reading gate;
- no passive-exposure field.

Usage commands append idempotent events and never mutate `state`, `rung`, `next_review`, or existing evidence cells. A usage event must reference a lesson/evidence path; the command rejects a missing path with a non-zero result. The script must preserve the existing concept-table parser and add fixture tests for the new event section.

Public notes are limited to 240 characters and a single table cell; they may contain a short learner-selected term or summary, never raw novel passages or private productions. The exact command is documented in `scripts/README.md`.

This keeps concept state, review schedule, and usage history distinct without a second scheduler or a mutable evidence mega-cell.

### E. Question-signature and technical evidence model

Use the existing public lesson record path:

```text
_system/learning/lessons/<topic>/<YYYY-MM-DD>-<slug>.md
```

Add a `## Question variants` section to technical session records:

```markdown
| stage | prompt | normalized signature | reused? |
|-------|--------|---------------------|---------|
| cold | ... | sha256:... | no |
| fresh transfer | ... | sha256:... | no |
| implementation | ... | sha256:... | no |
```

Normalization is exact-prompt normalization, not semantic deduplication: Unicode NFKC, lowercase, collapse whitespace, and strip Markdown formatting. Store the normalized signature and a short prompt summary, not raw private context. Before assessor dispatch, search prior records for the same topic/claim and reject an exact signature match for the fresh-transfer or implementation stage. Same construct with different wording/context is allowed.

Add a fixture test for signature normalization and exact-prompt non-reuse. Add the new template to `_templates/Index.md`.

### F. Skills and agents

- `.dsh/skills/study/SKILL.md`: route technical work to the new technical skill; keep generic source-first study; remove archived-build-plan dependency where no longer needed.
- `.dsh/skills/resources/SKILL.md`: learner requests source; scout/verifier select and verify on demand; learner-supplied books accepted; no prebuilt catalogue.
- `.dsh/skills/review/SKILL.md`: separate due review, usage events, and natural use; read-only stale-usage selection.
- `.dsh/skills/map/SKILL.md`: keep unless implementation finds a conflict.
- `.dsh/agents/scout.md`, `verifier.md`, `assessor.md`: keep; update only for source-request input, question-variant fields, and technical assessor contract.

### G. Waste staging and removal

Staging candidates, not automatic deletions:

```text
_system/learning/archive/harness-opencode/command/*.md
_system/learning/archive/harness-codex/**
scripts/cold_tools.sh
docs/agents/issue-tracker.md
docs/agents/triage-labels.md
docs/agents/domain.md
```

**Steering decision:** the vault does not need a separate GitHub issue/triage/domain workflow. The three `docs/agents/` documents are deletion candidates. During implementation, remove their live `AGENTS.md` pointers and delete them together after a reference check confirms they are not consumed by an active skill or workflow. They are not learner content and do not need an archive copy.

Archive files are protected provenance in this implementation, except for the explicitly approved thin retired OpenCode/Codex harness mirrors. Delete those mirrors after checking references. Retain the larger historical build plans if they still contain useful migration decisions. The issue/triage/domain documents are the explicit exception above.

Delete `scripts/cold_tools.sh` after moving its four-step reminder into `_system/How to Learn.md` and replacing every reference in `scripts/README.md` and `Mechatronics/milestones/00_foundations.md` through `04_capstone_integration.md`.

Keep safety/dependency/landmine material. Keep actual evidence artifacts. Use a path-scoped deletion manifest and reviewed commits; never use broad `save.sh` staging for cleanup.

## 6. Implementation order

1. Protect and inventory all evidence, private, safety, capture, data, hardware, goal, Changelog, and tag paths.
2. Apply the resolved steering decisions: delete unused issue/triage/domain docs and thin retired harness mirrors; retain useful historical plans; make speed runs optional; use the 30-session reading gate; rewrite JIT standing orders; use flip/commit/tag order.
3. Normalize contracts and source headings; update learner standing orders explicitly.
4. Add Japanese session skill, Japanese event records, and 30/60/90 routing.
5. Add technical skill, technical template, question-signature records, assessor contract, and usage-event commands.
6. Migrate source metadata and reduce technical roadmap duplication while preserving safety/evidence policy.
7. Stage/archive/remove only approved waste candidates; do not delete archive provenance.
8. Validate with fixtures, end-to-end scenarios, link checks, and protected-path diffs.

## 7. Validation before completion

Run:

```text
python3 -m unittest discover -s scripts/tests -p "test_*.py"
python3 scripts/review.py selftest
python3 scripts/review.py due
python3 scripts/diagnose.py
python3 scripts/validate_learning.py
```

Add these executable tests:

```text
scripts/tests/test_review.py
scripts/tests/test_usage_events.py
scripts/tests/test_question_signatures.py
scripts/tests/test_source_schema.py
scripts/tests/test_technical_session.py
```

Add read-only `scripts/validate_learning.py` checks for:

- all 17 active curriculum files use `## Resources`;
- every active source entry has concept IDs and a verdict;
- no removed path remains referenced;
- no protected archive provenance path was deleted except the explicitly approved thin OpenCode/Codex mirrors;
- no Daily/private/evidence/safety/capture/data/hardware/goal path was destructively changed;
- Changelog/evidence changes are append-only;
- source-ledger and technical-template references resolve.

Add an end-to-end fixture proving:

```text
technical read
→ cold Socratic check
→ timestamped 20-minute break
→ fresh conceptual transfer
→ implementation/theory test
→ Feynman correction if triggered
→ assessor result
```

Also verify:

- Japanese 30/60/90 session shapes;
- 4–5-hour budget integration with 3-hour immersion and 30-minute Anki;
- i+1 new-material bound;
- 30-session reading transition and fallback behaviour;
- introduced/practised/mined/produced/reading_session events;
- Anki claims remain learner-reported without a bridge;
- no passive exposure updates `last_used`;
- no raw novel text/screenshots enter tracked files;
- no learner/private/evidence/safety/capture/data/hardware/goal content is removed or rewritten;
- all `cold_tools.sh` references are replaced;
- `diagnose.py` limitations do not substitute for the dedicated validator;
- Changelog and new evidence are append-only;
- no broad cleanup commit is created with `save.sh`.

## 8. Steering questions / contradictions

1. **Resolved steering decision:** delete `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, and `docs/agents/domain.md`; remove their live pointers and verify no active consumer before deletion. This vault does not need a separate issue/triage/domain workflow.
2. **Resolved steering decision:** the reading gate is 30 actual novel-reading sessions; sentence-analysis fallback does not count.
3. **Resolved steering decision:** rewrite standing orders 5, 8, and 9 to the JIT-source policy.
4. **Resolved steering decision:** speed runs are optional recommendations. After each phase, ask whether to do the next speed run or move on.
5. **Resolved steering decision:** use the evidence → flip → commit → signed-tag order. Update `scripts/milestone.sh`, `Mechatronics/ROADMAP.md`, and related documentation so the signed tag points at the clean commit containing the completed checkbox and evidence.
6. **Resolved steering decision:** delete the thin retired OpenCode/Codex harness mirrors after checking references; retain larger historical build plans if they still contain useful decisions.
7. **Resolved steering decision:** delete `scripts/cold_tools.sh` after moving its checklist and replacing all references.

No steering questions remain. Implementation and validation are complete; future changes require a new approved plan.
