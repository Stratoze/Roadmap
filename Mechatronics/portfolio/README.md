# Portfolio

This folder is for final delivery artifacts, not daily marketing.

Use it when evidence is ready to compile:

- engineering report drafts
- final report
- video script
- demo notes
- resume bullets
- presentation outline

Most raw material should come from milestone files, decision records, captures, test notes, and retros.

Do not write from scratch. Compile what the project already proved.

## Quick compilation

```bash
# All decision records across the repo
grep -rn "^DECISION:" . --include="*.md"

# All verified landmines, things that actually tripped you
grep -rn "\[VERIFIED" milestones/
```
