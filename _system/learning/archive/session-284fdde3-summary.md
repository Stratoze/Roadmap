# Session 2026-09-26 (session-284fdde3) — summary

Reconstructed from the session transcript, not from the changelog. The
learner's messages are the authoritative record of what was decided; agent
narration is not. Range: 22 commits after `f3e8952`, 31 files, +1528/−136.

## What this session was for

A previous session died mid-task. The stated goal, set by the learner partway
in, was *"dont stop until you're sure i would be satisfied with the result"* —
a quality bar, not a task list. The working goal was cutting the number of
steps a cold agent needs to answer "what's next?", and verifying the result
rather than assuming it.

## The spine of the session was five learner interventions

This is the part a changelog-based summary misses, and it is the most useful
thing in the transcript.

1. **"for questions use grilling"** — set the mode for every decision after
   that point.
2. **"have you tested on a fresh agent to see if it would work?"** — the
   pivotal question. The gate had passing unit tests and had never been
   exercised end to end. A fresh agent found two defects: `anki_bridge.py` was
   the only script in the repo without a UTF-8 stdout guard, so the stuck
   words came back as replacement characters; and the gate was reachable only
   by reading the Japanese skill, so an agent that had not opened it would have
   opened with a new word on a `patch` lane. Neither was a coding error. Both
   were wiring errors — the exact class the session's own metric exists to
   catch.
3. **"is not something you would put in agents.md which needs to be lean, less
   than 200 words"** — the learner caught `AGENTS.md` bloating to 1370 words
   while its own first line says procedure lives elsewhere. Now 197. Followed
   by "you can cut out stuff into other doc files and reference them in agents",
   which is the shape of the fix.
4. **"what have you done since the goal was set? whats left? whats taking so
   long? are you sure you aren't over complicating stuff for diminishing
   return?"** — the learner correctly diagnosed a drift the agent had not
   noticed. The preceding rounds had produced a template sentence, a CLI flag,
   and a test expectation: minutes of work each on an already-green system.
5. **"ok, review agents?"** — prompted an independent review that found nine
   defects, five of them in claims the changelog had already recorded.

The pattern: the learner's interventions found more than the agent's own
verification did.

## Substantive changes

**Cold-start cost.** `session_state.py today` inlines each handoff's status and
next action, so a cold agent need not open two `CURRENT.md` files to learn
where to start. `AGENTS.md` 1370 → 197 words, with the cut material moved to
`scripts/README.md` and a source rule dropped outright because `learner.md`
standing orders 4/8/9 already own it.

**Review and teaching split.** `review.py due` had been offering concept `c5`
while withholding `c4` — its own prerequisite — despite both carrying real
evidence from the 2026-09-22 lesson. Neither possible rule was implemented.
`due` now lists by own evidence and ignores prerequisites; the new
`review.py frontier` reports what is ready to teach, showing only the roots of
the unlearned forest (22 lines, not 150). A real bug surfaced underneath: the
prerequisite state map was built per topic file, but prerequisites cross file
boundaries, so those ids resolved to `None` and would have hidden a dependent
concept permanently.

**i+1 lane gate.** `anki_bridge.py iplusone` (read-only) picks the lane for the
next Japanese conversation — `stretch`, `patch`, or `hold`. A stuck word is
`reps>=10` and `interval<7d`. On live data: 9 unlearned, 1000 stuck, lane
`patch`. The lane is now printed by `session_state.py today` and fails closed
when Anki is unreachable.

**Six decisions recovered** from the deleted transcript of the previous session,
each promoted to the document that owns it: never review with a forked
subagent, assume from prior answers, escalate only as fallback, delegate
execution and verification, cold-start cost is a maintained metric, AnkiConnect
is local-only. Eleven further decisions were confirmed already captured —
checked against a specific file and line, not assumed.

**Also:** a waste-reduction scout created and run; Piano's false claims
corrected; `Mechatronics/GOAL.md` archived with its goal statement moved into
ROADMAP's *Confirmed goal*.

## Learner decisions that redirected the work

- **Anki is read-only.** *"anki gets new cards from stuff like mining, not from
  our chat."* The `add-approved` write path stays unexercised by design.
- **Only introduce a new word when none is unlearned**, and let significantly
  overdue words count as i+1. This became the `patch` lane. The agent pushed
  back that an overdue word is consolidation rather than acquisition, and the
  learner accepted the labelling requirement: the tutor must say which lane it
  is on.
- **Escalate only as fallback.** Stated twice, the second time to correct the
  agent's over-broad reading: the default is no escalation; escalate only when
  the current mode genuinely cannot do the job.
- **Piano is outside the learning plan.** This killed the waste scout's largest
  proposal — 618 lines of piano process material — as the wrong question. Only
  files wrongly claiming otherwise were fixed.
- **GOAL.md judged as a Full Pass**: it never started, so it was not a status
  file.

## Errors made and corrected

**Four false claims**, every one the same shape: a subagent's summary reported
as fact without checking the transcript or the code.

1. That `review.py` commands were gated by sandbox permissions. False — a
   brief in `.dsh/agents/` is inert text; nothing parses it into a profile, so
   `effect: deny` is a declaration of discipline, not enforcement.
2. A report of pending "safe-harbor / grace landing / gap severity" decisions.
   They exist in neither transcript nor vault. The learner was told to rule on
   decisions that did not exist.
3. That an append-only violation had been "undone rather than left in history".
   It had not: only a later commit was undone, while the violating commit
   `7231d4f` remained in the range.
4. A "warning for a concept check" severity tier, which was never approved.

**The append-only violation and its root cause.** A commit edited an existing
changelog bullet instead of appending. It was not caught because the check
compared removed against added lines across the *whole* range, so a mid-range
rewrite netted to zero removed lines and passed. It now checks each commit
individually and names the offender. Two further traps: the check only runs
when a base is supplied, and the learner was told to work around a protected
path the first time the agent tried to correct a changelog entry in place.

**Nine defects from the independent review**, five in claims the changelog had
recorded. The reuse rule turned out to be encoded in **five** places that
disagreed, not four — a stale sentence sat 57 lines above its own correction.
The cold exemption was broader than advertised: the code exempted any cold row,
including one carrying a real value set, which is a test instance and may not
repeat. The archived session-decisions record still asserted two claims
retracted earlier the same day.

## State at the end

165 tests pass, 2 skipped. `validate_learning.py` ok, both plain and with
`--base`. `diagnose.py` 0 broken links, 0 orphans. `review.py selftest` ok.
Working tree clean. `origin/main` is at `80f0f6a`, so **15 of the 22 commits are
committed but unpushed**.

## Open

- **The cold-start step count was never cleanly captured.** The last probe was
  spawned as a background subagent, and `send_message` cannot reach one, so the
  self-audit half of the method is unobtainable. The method now calls for a
  team member, but no clean post-fix number exists.
- **One boundary case, undecided:** an implementation prompt re-used as a cold
  check still passes, because the decision scopes the ban to fresh transfer and
  implementation as the *reusing* stages. Whether to tighten it is the
  learner's call.
- **The summary agent was interrupted** after roughly 20 minutes; a second
  attempt with a bounded brief succeeded. The recurring cause was oversized
  briefs, not the agent.

## A note on the harness

Three separate times in this session, a *correct* safety check fired on the
agent: the live Anki write path was denied during a "test" that would have been
refused anyway; a changelog edit that would have rewritten protected history was
denied; and a `Remove-Item` on an unestablished temp path was denied. In each
case the agent had been told a narrower permission and over-read it. The
standing lesson: prefer omitting a permission over requesting one, and never
exercise a write or delete path against real data to "check" that it is
guarded.
