# AGENTS.md - Operating Contract for AI Sessions in This Vault

Active system: **Vault Learning System** (`_system/learning/`). This file is the short operating contract. Read the pointed-to method and skill files for procedure; do not recreate their content here.

## Session start

Before other work, run from the repository root:

```bash
python3 scripts/review.py due
test -f "Daily/$(date +%F).md" && echo "note: exists" || echo "note: missing"
```

If due output is non-empty, send one short message with the count/topics and one question offering action. Do not nag about a missing daily note. Do not auto-create notes, start sessions, reminders, or background jobs.

## Session shape

- Start with the work. No pre-work form or Target/Predict gate.
- Lead sequencing yourself: due reviews, then in-flight maps, then the next eligible topic from the focus queue, ROADMAP, and curriculum state.
- Ask **one adaptive question per message** when probing, mapping, studying, or reviewing. Ask, then wait.
- At close, draft the session log from evidence. The learner owns corrections. No session means no daily note.
- Raw learner productions go only to `_private/learning/`. Public files contain summaries and links.
- The learner produces code, derivations, and solutions. The agent scaffolds, executes, verifies, and reviews.

## Active documents and skills

Read before teaching or reviewing:

- `_system/How to Learn.md` - method, Loop, struggle, AI boundaries.
- `_system/learning/README.md` - layout, ownership, schemas.
- `_system/learning/learner.md` - canonical learner preferences and standing orders.
- `_system/learning/topic-tree.md` - hierarchy and dependency map.
- `_system/learning/maps/overview.md` - provisional cross-strand map.

Active skills in `.dsh/skills/`:

- `study` - source-first concept teaching and checks.
- `map` - one-question knowledge mapping.
- `resources` - JIT source selection and verification.
- `review` - cold spaced review.
- `japanese` - daily Japanese grammar, conversation, reading, immersion, and evidence orchestration.
- `technical` - technical scheduler, source/read handoff, conceptual check, break, transfer, implementation, and assessor flow.

Use plain language (`study X`, `review`, `test me in X`, `Japanese session`, `technical session`). No slash-command infrastructure.

## Source and curriculum policy

Raw roadmaps contain **deliverables, dependencies, search keywords, and safety/evidence boundaries**. They do not maintain a book/video library.

When an active topic needs a source:

1. Identify the exact concept and blocker.
2. Ask the learner for a book or source when needed; the resource skill may scout and verify one on demand.
3. Record only the active locator in the topic dossier.
4. Open the source before teaching or testing.
5. A faithful Japanese translation/restatement of the cited source is allowed. An explanation beyond it requires a documented sourcing blocker; never substitute an unsourced AI lecture.

Stable discovery links may remain in compact index files. Rejected/unverified source decisions move to `_system/learning/archive/source-ledger.md` rather than disappearing.

## Review and evidence

- `python3 scripts/review.py` owns spaced-review state. Never hand-compute schedules.
- Dedicated due review is separate from natural use. Old material remains eligible when it fits a session.
- Usage events are append-only. Passive exposure is not use; an attempted use is not a clean use.
- Anki owns Japanese vocabulary. The vault owns grammar, output, reading, immersion, and evidence. Without a bridge, Anki knowledge claims are learner-reported.
- No exact technical question prompt may be reused for a fresh-transfer or implementation stage. Store signatures in the technical lesson record.
- MVM/Full Pass claims route through the assessor. A partial/lapsed result does not earn a gate.
- Milestone status lives only in `Mechatronics/ROADMAP.md`. Milestone checkboxes are frozen acceptance history. The order is evidence → checkbox flip → commit → signed tag.
- `Mechatronics/resources/SAFETY_CARD.md` and milestone safety/landmine material are protected.
- Use `bash scripts/save.sh` only for reviewed, scoped changes. It stages broadly; never use it for cleanup commits.

## Hard rules

- PLAN-marked files implement only after explicit user approval.
- Scope approval before landing curriculum changes; maps-only landings.
- Never invent activity, evidence, reviews, or session outcomes.
- Never write the learner's artifact. Verify independently.
- Never AI-generate video. Books win when they cover the concept; otherwise use a verified human source.
- Keep learner records, private data, evidence, safety material, signed tags, and useful historical provenance intact.
- Do not delete archive material by default. The approved thin retired harness mirrors and unused issue/triage/domain documents are the only cleanup exceptions; check references first.

## Validation and maintenance

Before toolchain-dependent work, run `bash scripts/versions.sh`. After
structural changes, run `python3 scripts/diagnose.py`. Use
`python3 scripts/validate_learning.py` for the layout/protected-path checks
and `python3 -m unittest discover -s scripts/tests -p "test_*.py"` for the
executable tests. Do not claim completion from prose alone. Keep the plan and
active documents aligned: one fact has one owner.
