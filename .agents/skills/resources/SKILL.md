---
name: Resources
description: Build or refresh a topic's verified resource dossier - scout finds candidates, verifier checks them independently against the live sources, entries are dated with a verdict. Use when a topic has no dossier or needs re-verification.
slash: false
---

# Resources - the dossier

JIT per active topic: build when a topic starts; never pre-build the whole
roadmap. Read `_system/learning/learner.md` for sourcing preferences.

1. Spawn **scout** with: topic, goal, what the next lessons need (rigorous /
   intuitive / interactive), learner preferences. It returns candidates with
   title, creator, URL, type, what claim each covers, plus kept/dropped and
   gaps.
2. Spawn **verifier** on the scout's output. It independently fetches and
   checks: human authorship (videos), primary vs secondary, date, and a
   cross-check of the central claim. Verdicts: `verified <YYYY-MM-DD>` /
   `unverified` / `rejected`.
3. Write entries to the topic file `## Resources` in the pinned format:
   `- <rigorous|intuitive|interactive|reference> | <title> | <creator> | <url> | <verdict>`
   Rejected stays listed so it is never re-proposed.
4. Re-verify only on trigger: fast-moving field, a lesson contradiction, or
   the learner asks. Resources are dated snapshots.

Rules: established human educators first; never AI-generated video; prefer
primary sources; a source that cannot be fetched is `unverified`, never
"verified from memory". If scout and verifier disagree, the verifier wins until
the live source shows otherwise.
