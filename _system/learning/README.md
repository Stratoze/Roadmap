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

- Skills: `.dsh/skills/study/`, `map/`, `resources/`, `review/` - invoked by
  either party in plain language ("study X", "review", "test me in X") under
  the ask-first rules in `AGENTS.md`. No slash-command infra.
- Agents: `.dsh/agents/{scout,verifier,assessor}.md` - briefs are inert until
  quoted (hand the child the file plus its task).
- Legacy shims (OpenCode commands/agents, Codex agents, `.agents/skills/`)
  are frozen in `archive/harness-opencode/` and `archive/harness-codex/`.

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
