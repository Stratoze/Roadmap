---
title: Piano
aliases:
- Piano Home
- Piano MOC
tags:
- piano
- moc
---
# Piano Index

## Start here
- [[_system/Daily Template|Daily Template]] — unified daily note (all domains)
- [[Piano/Resources/Movement|Movement]] — the technique library (M1–M12), canonical source
- [[Piano/Resources/Practice Protocols|Practice Protocols]]
- [[Piano/Resources/Progression|Progression]]
- [[Piano/Resources/Roadmap|Roadmap]]
- [[Piano/Resources/FAQ|FAQ]]

## Practice engine
- [[Piano/Resources/Practice Protocols|Practice Protocols]] — session engine, learning protocol, tempo, Q-spots
- [[Piano/Resources/Movement|Movement]] — technique library (M1–M12), diagnostics, calibration

## Planning and progression
- [[Piano/Resources/Progression|Progression]] — volume, stages, ladders, cycles
- [[Piano/Resources/Roadmap|Roadmap]] — stage map
- [[Piano/Resources/Repertoire and 12-Week Goals|Repertoire and 12-Week Goals]]
- [[Piano/Resources/FAQ|FAQ]]

## Pieces and logs
- [Pieces README](Pieces/README.md)

### Piece templates
- [[_templates/piano/Piece Note|Piece Note]]
- [[_templates/piano/Piece Error Log|Piece Error Log]]
- [[_templates/piano/Piece Tempo Log|Piece Tempo Log]]

## Musicianship
- [[Piano/Resources/Musicianship|Musicianship]] — sight-reading, ear/theory, listening
- [[Piano/Resources/Creative Play|Creative Play]]
- [[Piano/Resources/Functional and Jpop Track|Functional and J-pop Track]]

## Maintenance and performance
- [Maintenance rotation](Resources/Maintenance%20and%20Performance.md#maintenance-rotation-engram)

## Resources
- [Resource List](Resources/Resource%20List.md)
- [Editions and Sources](Resources/Editions%20and%20Sources.md)

## Templates
- [[_templates/piano/Weekly Review|Weekly Review]]
- [[_templates/piano/12-Week Goal|12-Week Goal]]

---

## Dashboards
These require the Dataview plugin. If you do not use Dataview, ignore this section.

### Recent daily notes
```dataview
LIST
FROM "Daily"
SORT file.name DESC
LIMIT 20
```

### Active pieces
```dataview
TABLE composer, status, current_tempo, target_tempo
FROM "Piano/Pieces"
WHERE type = "piece" AND status != "shelved"
SORT status ASC, composer ASC
```

### Shelved pieces
```dataview
TABLE composer, status, notes
FROM "Piano/Pieces"
WHERE type = "piece" AND status = "shelved"
SORT composer ASC
```
```
