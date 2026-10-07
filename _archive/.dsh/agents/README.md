# Agents

Project-scoped subagent briefs for the vault learning system. A brief here is
INERT until quoted: hand the child the agent file plus its task — it starts
with no memory of the asking session.

**The `permissions:` frontmatter in these briefs is a declaration, not an
enforced sandbox.** Nothing in the harness parses these markdown files into a
permission profile — the whole file is inert text until an agent reads it. So
`effect: deny` states the role's expected discipline; it does not stop the
child from shelling out or editing. Do not describe a brief as making an agent
*physically* incapable of something. What actually protects the vault is the
learner's review of the output and the agent honouring its brief.

- `scout.md` — research specialist (read-only posture): candidate sources and
  field scans with provenance. Never shares context with verifier.
- `verifier.md` — adversarial source check: fetches each candidate, per-item
  verdict (verified / unverified / rejected) with evidence.
- `assessor.md` — blind grader for claim gates (MVM / Full Pass) and sampled
  audits. Sees only claim + rubric + question + production.
- `waste-scout.md` — waste auditor, scoped only to reducing waste inside the
  system: duplicated ownership, superseded content, unreferenced files, and
  process that produces no evidence. Read-only, and stages proposals rather
  than deleting; protected material is never a candidate.

**Never review with a forked subagent.** A fork inherits the asking session's
context, which biases the reviewer toward an answer it can already see. Use a
fresh subagent and hand it the context it needs. (Learner standing order,
2026-09-26: "dont use fork or it would bias the agent's context".) This
applies to plan review and implementation review, not only to the roles above.

Skills that spawn them live in `.dsh/skills/`. Retired OpenCode/Codex harness
mirrors were removed after reference cleanup; `.dsh/` is the only live home.
