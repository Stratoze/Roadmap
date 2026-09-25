---
name: Resources
description: Select and verify a source on demand for the active concept. Use when a lesson or technical session needs a book, video, interactive, or other locator; never prebuild a roadmap source library.
---

# Resources - JIT source dossier

Read `_system/learning/learner.md` and the active topic/concept first. This
skill runs when the concept needs a source, not as a roadmap prebuild.

## Request flow

1. Name the exact concept, claim, learner level, and source gap.
2. Ask the learner for a book or source when needed. If the learner supplies
   one, use the relevant edition/chapter/pages after checking it fits.
3. Otherwise spawn **scout** for a small candidate set: title, creator, exact
   locator, level, what it covers, and gaps. Books are preferred where they
   cover the concept; videos/interactives are verified substitutes or
   supplements.
4. Spawn **verifier** on the candidates. Check human authorship, primary vs
   secondary status, date where relevant, and the central claim. For books,
   verify existence, edition, and chapter title against a fetched table of
   contents; never claim to have read an interior section that was not
   accessed. Unfetchable sources are `unverified`, not verified from memory.
5. Write only the selected active locator to the topic's `## Resources`:

```text
- <rigorous|intuitive|interactive|reference> | <title> | <creator> | <book: ch N "Title" | video | interactive: <name>> | <url> | for <concept ids> | <verdict>
```

6. Re-verify only on a logged blocker, contradiction, fast-moving source, or
   learner request. Keep rejected/unverified decisions in the historical source
   ledger rather than repeatedly proposing them.

## Source-first boundary

The lesson opens at the active locator. A faithful Japanese translation or
restatement of that source is allowed without adding claims. An explanation
beyond it requires a `blocker` entry; an unsourced AI lecture is not a
substitute for a source.

## Failure handling

If no source is available, record:

```text
- blocker <YYYY-MM-DD> <concept id>: "<what the source failed to cover>"
- no source found <YYYY-MM-DD> <concept id>
```

Then narrow the concept, request a learner source, or explicitly mark the
lesson blocked. Never quietly replace the source with memory.

## Rules

- One active locator per concept; no standing catalogue.
- Stable discovery links belong in compact index files, not every curriculum.
- Never AI-generated video.
- Raw learner text and private work stay in `_private/`.
- The scout/verifier roles remain separate and bounded.
