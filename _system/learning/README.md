# Vault Learning System

The learning system for this vault. Replaced the previous FSRS-based engine
(retired 2026-09-11; see the Changelog). Design: verified sources,
teach-first on new material, struggle in the material, timely feedback, spaced
review - everything visible, versioned, and hand-editable in the vault.

## Layout

- [[learner]] - canonical preferences and standing orders (OpenViking mirror
  retired 2026-09-15; `learner.md` is canonical).
- [[topic-tree]] - the curriculum map: subjects -> chunk-sized topics, the
  theory spine, and the theory-to-practice link map.
- `curriculum/<domain>-<slug>.md` - per-topic file: goal, map, concepts, resources,
  problems, misconceptions, links, log. Naming: `<domain>-<slug>` in kebab-case
  (e.g. `math-odes`); rows are created only by `study` step 0 / intake, never by
  `review.py`. Skeleton: `archive/vault-learning-system.md` Appendix A.
- `lessons/<topic>/YYYY-MM-DD-<slug>.md` - lesson notes: target, predict,
  orientation, attempts, feedback, reflection, links, next. Summaries only; raw
  text lives in the private store.
- Review schedule: every concept row carries `rung` and `next_review`; the
  ladder is 1, 3, 7, 16, 35, 90 days. `python3 scripts/review.py due` lists
  today's items; `next` and `schedule` update them.
- Pre-system knowledge (completed milestones, migrated tracks) enters through
  **intake**: one compressed cold verify per concept - clean -> scheduled at
  rung 2, effortful -> rung 1, miss -> taught first. No re-teaching of passing
  verifies.
- [[quiz-protocol]] - how graded probes/quizzes are constructed (bare claims,
  mutated distractors) and graded (keys by execution; confidence first).
- `maps/overview.md` - roadmap-level edge map (in-flight scoping; strand queue +
  provisional brackets by unit). Provisional by design; never canonical status.

## Active session skills

- `.dsh/skills/japanese/SKILL.md` coordinates the daily Japanese grammar,
  conversation, reading, immersion, Anki boundary, and usage evidence.
- `.dsh/skills/technical/SKILL.md` coordinates technical source selection,
  learner reading, cold conceptual checks, breaks, fresh transfer,
  implementation, Feynman correction, and assessor handoff.
- `Japanese/CURRENT.md` is the mutable next-session handoff. The Japanese
  skill reads it before branching and rewrites it at every close.
- `scripts/session_state.py` reads/updates the daily checklist; `anki_bridge.py`
  is an optional local AnkiConnect reader with approval-gated writes.

These compose the existing `study`, `map`, `resources`, and `review` skills;
they do not create a second curriculum or vocabulary database.

## Schemas and ownership

- `## Resources` is the canonical active source-dossier heading. Raw roadmaps
  contain deliverables, dependencies, keywords, and safety/evidence boundaries,
  not source libraries.
- `## Usage events` is append-only. Events are `introduced`, `practised`,
  `produced`, learner-reported `mined`, or `reading_session`; passive exposure
  is not use.
- Anki owns Japanese vocabulary. Public notes contain summaries and links;
  raw learner productions stay in `_private/`.
- Technical lesson records are written under
  `_system/learning/lessons/<topic>/`; technical sessions use the
  `_templates/learning/technical_session.md` shape with the timestamped break
  and prompt/variant signature table. Generic concept lessons keep the
  Target/Predict/Attempts/Feedback/Reflection schema. Use
  `scripts/question_signatures.py check` before a fresh prompt.

## The link web

Everything links: topics, theory, problems, lessons, evidence - and links run
both ways. If a lesson uses a theory, the lesson links to the theory and the
theory links back to the lesson ("Applied in"). Obsidian backlinks are a safety
net, not the plan; write the explicit link.

- Curriculum file sections that carry links: `Rests on:` (theory this practice
  depends on), `Teaches:` (what it gives back), `Problems:` (table), `Lessons:`.
- `Problems` table: `| id | problem | source | theory | attempts | status |`;
  source = milestone section, authored, or generated; status = open / attempted
  / solved / revisit.
- Lesson notes carry `## Links`: Topic, Theory, Problems (ids), Previous
  lesson.
- A problem is not done until its row points at a lesson note and the lesson
  points back.
- An edge must name its mechanism (one sentence: why does this follow?).
  Conventions (sign rules, right-hand rules, unit standards) are labeled as
  conventions; no decorative links.

## Private store

Raw productions, attempts, reflections, and confidence records live in
`_private/learning/` - a separate private repo, gitignored by this one. If
`_private/` is not cloned, the system pauses verbatim capture and says so;
public summaries continue.

## Skills and agents

Project-scoped; no global plugin needed. Single live home: `.dsh/`.

- Skills: `.dsh/skills/study/`, `map/`, `resources/`, `review/`, `japanese/`,
  `technical/` - invoked by either party in plain language under the ask-first
  rules in `AGENTS.md`. No slash-command infra.
- Agents: `.dsh/agents/{scout,verifier,assessor}.md` - briefs are inert until
  quoted (hand the child the file plus its task).
- Retired OpenCode/Codex harness mirrors are historical provenance only; they
  are not active procedure.

## Provenance

Inspired by Amos Blomqvist's learn system (github.com/amosblomqvist/learn):
probe -> plan -> teach; scoping-first mapping; quiz construction rules;
researcher/verification pattern; mermaid/SVG makers; LaTeX-first; unconditional
truths and "how could I have discovered this". Added for this vault: the
scout + verifier sourcing pipeline, the multi-lens rule, the struggle budget,
the review/maintain leg with a transparent ladder, evidence gates for
milestones, and the private verbatim store.

Plan of record: `archive/vault-learning-system.md` (historical build plan;
operative docs are `AGENTS.md`, `_system/How to Learn.md`, and this file).
