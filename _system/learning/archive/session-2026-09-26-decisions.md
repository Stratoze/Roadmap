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
   (transcript L185). **Closed 2026-09-26:** `.dsh/agents/waste-scout.md` now
   exists and stages proposals rather than deleting, with protected material
   excluded by name. *Correction, same day:* an earlier version of this line
   called the scout "read-only" on the strength of its `permissions:` block.
   That was wrong — a brief in `.dsh/agents/` is inert text, nothing parses it
   into a profile, so `effect: deny` is a declaration of expected discipline,
   not enforcement.
2. **Q10's graduated severity only half-landed.** **Closed 2026-09-26**, and
   the earlier wording of this line was itself wrong twice over. There is no
   "warning" tier: the decision was *"Same concept/equation: allowed. Same
   exact test item, value set, or lab condition: forbidden for fresh transfer
   and implementation. Full Pass requires a new scenario."* A cold conceptual
   check may re-ask a concept, and the reuse exemption applies only to a pure
   concept check — one recording `-` for both values and context, not a row
   carrying a real test instance. `scripts/validate_learning.py` enforces this
   and `.dsh/skills/technical/SKILL.md` states it.
3. **Anki is read-only, by decision (2026-09-26).** The learner closed this:
   *"anki gets new cards from stuff like mining, not from our chat"*. Anki is
   populated by mining, not by conversation, so the chat does not write. The
   `add-approved` path stays unexercised on purpose — not debt, a non-goal.
   What the bridge is for is *reading* Anki to choose conversation material,
   which is now `anki_bridge.py iplusone`. Note the lesson: an attempt to
   "test" that write gate against the live collection was denied by auto-review
   for exactly this reason. Exercise write gates against a fake client, which
   the test suite already does.
4. **Cold-start measurement.** Measured 2026-09-26 after `b7ebf21`: the
   fresh-agent answer was aligned and current. The step count was not captured,
   because the probe was spawned as a background subagent and `send_message`
   cannot reach one. The method in `AGENTS.md` now records that trap and calls
   for a team member. Re-measure before trusting a number.

## Method note

The distillation deliberately excluded lesson content, review outcomes, and
everything under `_private/`, which was never opened. The 16 subagent worker
logs were not swept: the two defects they raised are both closed, and a sweep
would surface code mechanics rather than learner decisions.
