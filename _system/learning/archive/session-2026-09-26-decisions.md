# Session 2026-09-26 — decision distillation and residue

**Distilled:** 2026-09-26, from session archive `dsh-session-session-30e2c7b5`
(5250-record transcript, 16 subagent logs). The archive itself was deleted
after this record and the operative landings below were reviewed.

**Why this file exists:** the session produced decisions that were not written
anywhere in the vault. Six were promoted to the operative document that owns
them. This file holds the residue — what was checked and cleared, and the
threads that are still open. Provenance only; never operative.

## Promoted to operative documents

| Decision | Landed in |
|---|---|
| Never review with a forked subagent — the fork biases the reviewer | `.dsh/agents/README.md` |
| Assume from prior answers; ask only where genuinely ambiguous | `AGENTS.md` (Session shape) |
| Do not request sandbox escalation; omit the parameter | `AGENTS.md` (Validation) |
| Delegate execution and verification; lead context is the scarce resource | `AGENTS.md` (Session shape) |
| Cold-start step count is a maintained metric, with the method | `AGENTS.md` (Validation) |
| AnkiConnect is local-only, with rationale | `_system/learning/learner.md` (Preferences) |

The escalation decision and the validation guidance initially contradicted each
other — the validation note read as "escalate to get full access". Resolved in
favour of the standing order: the note now explains the artifact and forbids
escalating around it.

## Checked and already captured — do not re-litigate

The Japanese spine and its sequence decisions, the Anki 20–30 minute block, the
daily slot order, Phase-0 priority as tie-breaker, the no-technical-reset rule,
the 30-actual-reading-session gate, the test-variant non-reuse rule, JIT source
policy, the approval-gated bridge, and the milestone order
(evidence → checkbox → commit → tag) are all already recorded in the operative
documents. The distillation confirmed each against a specific file and line
rather than assuming.

## Open threads

1. **A waste-reduction scout role was requested and never created.** The
   learner asked for a scout scoped *only* to reducing waste in the system
   (transcript L185). It was run ad hoc once. `.dsh/agents/scout.md` remains
   scoped to source research. Decide whether it earns a brief of its own.
2. **Q10's graduated severity only half-landed.** The learner asked for hard
   failure on fresh transfer and implementation, warning on a concept check.
   `.dsh/skills/technical/SKILL.md` states the hard-failure half; the
   concept-check leniency is unstated.
3. **Live Anki card creation has never been exercised.** Known debt, recorded
   in `Daily/2026-09-25.md`. Not a surprise, not a blocker.
4. **Cold-start was re-measured once, then the session ended.** Measured 2026-09-26
   after `b7ebf21`: the fresh-agent answer was aligned and current. The exact
   step count was not captured, because a finished background subagent cannot
   be resumed for the self-audit (`send_message` reaches team members only).
   Treat the number as unmeasured and the alignment as confirmed.

## Method note

The distillation deliberately excluded lesson content, review outcomes, and
everything under `_private/`, which was never opened. The 16 subagent worker
logs were not swept: the two defects they raised are both closed, and a sweep
would surface code mechanics rather than learner decisions.
