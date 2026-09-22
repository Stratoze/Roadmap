---
name: Resources
description: Build or refresh a topic's verified resource dossier - scout finds candidates, verifier checks them independently against the live sources, entries are dated with a verdict. Use when a topic has no dossier or needs re-verification.
---

# Resources - the dossier

JIT per active topic: build when a topic starts; never pre-build the whole
roadmap. Read `_system/learning/learner.md` for sourcing preferences.

**Books are the primary tier.** Finding the right book at the right level is the
hard part; a video for a known topic is cheap to find later. Every concept
should name a book chapter/section where one exists. Videos and interactives are
substitutes, marked as substitutes - a concept covered only by video is a weaker
entry, not an equivalent one.

1. Spawn **scout** with: topic, goal, what the next lessons need (rigorous /
   intuitive / interactive), learner background (zero-schema or not), and the
   instruction to name a book chapter/section per concept with its level. It
   returns candidates with title, creator, locator (book chapter/section, or
   video), URL, level, what each claim covers, plus kept/dropped and gaps -
   including an explicit "no book found" line per uncovered concept.
2. Spawn **verifier** on the scout's output. It independently fetches and
   checks: human authorship (videos), primary vs secondary, date, and a
   cross-check of the central claim. Books additionally need existence +
   edition + chapter title matched against a fetched table of contents; the
   verifier never claims to have read a book's interior, and a TOC that cannot
   be fetched means `unverified`. Verdicts: `verified <YYYY-MM-DD>` /
   `unverified` / `rejected`.
3. Write entries to the topic file `## Resources` in the pinned format:
   `- <rigorous|intuitive|interactive|reference> | <title> | <creator> | <book: ch N "Title" | video | interactive: <name>> | <url> | for <concept ids> | <verdict>`
   Rejected stays listed so it is never re-proposed. `for` lists the concept ids
   the locator serves, so a lesson can find its own source without reading the
   whole dossier. Books first in the list; label level (beginner /
   intermediate / advanced) when it is not obvious from the title.
4. Re-verify only on trigger: fast-moving field, a lesson contradiction, a
   logged `blocker`, or the learner asks. Resources are dated snapshots.

Rules: established human educators first; never AI-generated video; prefer
primary sources; a source that cannot be fetched is `unverified`, never
"verified from memory". If scout and verifier disagree, the verifier wins until
the live source shows otherwise.

## AI fallback

When a lesson hits a `blocker` (the cited source genuinely does not cover it),
append to `## Resources`:

`- blocker <YYYY-MM-DD> <concept id>: "<what the source failed to cover>"`

then either refill the dossier (scout for a better locator) or record
`no source found`. A blocker is evidence the dossier is wrong - never a license
to lecture in place of a source.
