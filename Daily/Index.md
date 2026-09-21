# Daily notes

Current Focus (next step per domain) lives in the latest note below.
Breaks are Focus status with a return date, not prose banners — when the latest
note has no Focus block, inherit from the newest note that has one.

```dataview
LIST
FROM "Daily"
WHERE file.name != "Index"
SORT file.name DESC
LIMIT 5
```
(Gaps hide below LIMIT — scan the folder date sequence weekly; a missing date is a missing note.)
