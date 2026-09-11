# Vault Learning System

The learning system for this vault. Replaces Engram (retirement in progress,
step D of `.opencode/plan/vault-learning-system.md`). Design: verified sources,
teach-first on new material, struggle in the material, timely feedback, spaced
review - everything visible, versioned, and hand-editable in the vault.

## Layout

- [[learner]] - canonical preferences and standing orders (OpenViking mirror;
  see the Mirrors note there).
- `curriculum/<topic>.md` - per-topic goal, map, concepts table, resource
  dossier, misconceptions, log. Skeleton: plan Appendix A.
- `lessons/<topic>/YYYY-MM-DD-<slug>.md` - lesson notes: target, predict,
  orientation, attempts, feedback, reflection, next. Summaries only; raw text
  lives in the private store.
- Review schedule: every concept row carries `rung` and `next_review`; the
  ladder is 1, 3, 7, 16, 35, 90 days. `python3 scripts/review.py due` lists
  today's items; `next` and `schedule` update them.

## Private store

Raw productions, attempts, reflections, and confidence records live in
`_private/learning/` - a separate private repo, gitignored by this one. If
`_private/` is not cloned, the system pauses verbatim capture and says so;
public summaries continue.

## Skills and agents (built in steps B-C)

- `.opencode/skills/study/`, `map/`, `resources/`, `review/`
- `.opencode/agents/scout.md`, `verifier.md`, `assessor.md`

## Provenance

Inspired by Amos Blomqvist's learn system (github.com/amosblomqvist/learn):
probe -> plan -> teach; scoping-first mapping; quiz construction rules;
researcher/verification pattern; mermaid/SVG makers; LaTeX-first; unconditional
truths and "how could I have discovered this". Added for this vault: the
scout + verifier sourcing pipeline, the multi-lens rule, the struggle budget,
the review/maintain leg with a transparent ladder, evidence gates for
milestones, and the private verbatim store.

Plan of record: `.opencode/plan/vault-learning-system.md`.
