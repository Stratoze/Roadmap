# AGENTS.md - Operating Contract

Active system: **Vault Learning System** (`_system/learning/`). Procedure lives
in the files below — read, don't restate. Tooling: `scripts/README.md`.

## Start

```bash
python3 scripts/session_state.py today
```

Resolves checklist and next action. Order: Japanese →
Anki/due (30-min cap) → technical. Never nag about a missing daily note, or
auto-create notes, sessions, or jobs. Reading and Piano stay opt-in.

## Working

- **Learner owns learn → tutor tests → tutor records** (`_system/learning/loop.md`).
  Schedule keywords, questions-to-answer-yourself, one offline task, and a source
  locator; then test, answer, correct in one sentence, and record. No unprompted
  explanation — defer it into the next brief.
- **No tracking machinery for reading or immersion.** Name the source and level,
  ask how many were read, then get out of the way. Building a player, log, or
  dashboard to count reading is procrastination dressed as rigour — see
  `_system/learning/learner.md` order 1 and the learner's words there. Measurement
  belongs to the conversation ledger, never to the reading itself.
- One adaptive question per message, then wait. Never re-ask what is settled;
  infer and continue.
- Delegate execution and verification; context is the scarce resource.
  Team member if a follow-up is needed.
- The learner works; you scaffold, execute, verify. Never write their artifact
  or invent evidence.
- Raw productions go only to `_private/`; public files hold summaries.
- No sandbox escalation by default; escalate only as fallback.
- Pushed history is immutable. Fix forward; a thin message needs no rewrite.
- PLAN-marked files need approval. Safety material and provenance stay
  protected.

## Evidence

- `review.py` owns review state. Never hand-compute schedules.
- `progress.py` owns progress state (floor, score, ledger). Never hand-compute.
- Milestone status lives only in `Mechatronics/ROADMAP.md`: evidence →
  checkbox → commit → signed tag.
- MVM/Full Pass routes through `.dsh/agents/assessor.md`.

## Read before teaching

`_system/How to Learn.md`; `_system/learning/{loop,README,learner,topic-tree}.md`;
`Japanese/CURRENT.md`; `Mechatronics/CURRENT.md`; `.dsh/skills/`;
`.dsh/agents/`.
