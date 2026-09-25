# Agents

Project-scoped subagent briefs for the vault learning system. A brief here is
INERT until quoted: hand the child the agent file plus its task — it starts
with no memory of the asking session.

- `scout.md` — research specialist (read-only posture): candidate sources and
  field scans with provenance. Never shares context with verifier.
- `verifier.md` — adversarial source check: fetches each candidate, per-item
  verdict (verified / unverified / rejected) with evidence.
- `assessor.md` — blind grader for claim gates (MVM / Full Pass) and sampled
  audits. Sees only claim + rubric + question + production.

Skills that spawn them live in `.dsh/skills/`. Retired OpenCode/Codex harness
mirrors were removed after reference cleanup; `.dsh/` is the only live home.
