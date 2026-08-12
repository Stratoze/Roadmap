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
- [Movement](Resources/Movement.md) — the technique library (M1–M12), canonical source
- [Practice Protocols](Resources/Practice%20Protocols.md)
- [Progression](Resources/Progression.md)
- [Roadmap](Resources/Roadmap.md)
- [FAQ](Resources/FAQ.md)

## Practice engine
- [Session Engine](Resources/Practice%20Protocols.md#session-engine)
- [Learning Protocol](Resources/Practice%20Protocols.md#learning-protocol)
- [Tempo Control](Resources/Practice%20Protocols.md#adaptive-tempo-protocol)
- [Speed Work](Resources/Practice%20Protocols.md#speed-work)
- [Variable Practice](Resources/Practice%20Protocols.md#variable-practice)
- [Q-Spots](Resources/Practice%20Protocols.md#q-spots)
- [Plateau Breaking](Resources/Practice%20Protocols.md#plateau-breaking)
- [Technique and Health](Resources/Practice%20Protocols.md#technique-and-health)
- [Movement Principles](Resources/Practice%20Protocols.md#movement-principles)
- [Movement Diagnostics](Resources/Movement.md#movement-diagnostics)
- [Individual Calibration](Resources/Movement.md#individual-calibration)
- [Mental Practice and Consolidation](Resources/Practice%20Protocols.md#mental-practice-and-consolidation)
- [Dual-Task Training](Resources/Practice%20Protocols.md#dual-task-training)
- [Sleep Consolidation Protocol](Resources/Practice%20Protocols.md#sleep-consolidation-protocol)

## Planning and progression
- [Practice Volume and Pacing](Resources/Progression.md#practice-volume-and-pacing)
- [Deload Weeks](Resources/Progression.md#deload-weeks)
- [Implementation Order](Resources/Progression.md#implementation-order)
- [Starting from Zero](Resources/Progression.md#starting-from-zero)
- [Skill Stages](Resources/Progression.md#skill-stages)
- [Technical Progression Ladder](Resources/Progression.md#technical-progression-ladder)
- [Movement Progression Ladder](Resources/Progression.md#movement-progression-ladder)
- [Macrocycle and Cycle Structure](Resources/Progression.md#macrocycle-and-cycle-structure)
- [Liszt Path](Resources/Progression.md#liszt-path)
- [Readiness Stages and Shelving](Resources/Progression.md#readiness-stages-and-shelving)
- [Method Book Protocol](Resources/Progression.md#method-book-protocol)
- [Teacher and Feedback](Resources/Progression.md#teacher-and-feedback-checkpoints)
- [Exam Calibration](Resources/Progression.md#exam-calibration-only)
- [Repertoire and 12-Week Goals](Resources/Repertoire%20and%2012-Week%20Goals.md)
- [Sight-Reading Progression](Resources/Progression.md#sight-reading-progression)
- [Ear and Functional Progression](Resources/Progression.md#ear-and-functional-progression)

## Pieces and logs
- [Pieces README](Pieces/README.md)
- [Global Error Logs](Logs/Error%20Logs.md)

### Piece templates
- [Piece Note](../_templates/piano/Piece%20Note.md)
- [Piece Error Log](../_templates/piano/Piece%20Error%20Log.md)
- [Piece Tempo Log](../_templates/piano/Piece%20Tempo%20Log.md)

## Musicianship
- [Sight Reading](Resources/Musicianship.md#sight-reading)
- [Ear, Theory and Functional Playing](Resources/Musicianship.md#ear-theory-and-functional-playing)
- [Listening Habit](Resources/Musicianship.md#listening-habit)
- [Creative Play](Resources/Creative%20Play.md)
- [Functional and J-pop Track](Resources/Functional%20and%20Jpop%20Track.md)
- [Transcription Protocol](Resources/Musicianship.md#transcription-protocol)
- [Eye-Hand Span Training](Resources/Musicianship.md#eye-hand-span-training)
- [Animenz Pathway](Resources/Functional%20and%20Jpop%20Track.md#the-animenz-pathway)

## Maintenance and performance
- [Maintenance and Anki](Resources/Maintenance%20and%20Performance.md#maintenance-and-anki)
- [Recording and Self-Assessment](Resources/Maintenance%20and%20Performance.md#recording-and-self-assessment)
- [Performance Simulation and Memorization](Resources/Maintenance%20and%20Performance.md#performance-simulation-and-memorization)
- [Pre-Performance Routine](Resources/Maintenance%20and%20Performance.md#pre-performance-routine)

## Resources
- [Resource List](Resources/Resource%20List.md)
- [Editions and Sources](Resources/Editions%20and%20Sources.md)
- **RCM-Syllabus-2022**

## Templates
- [Weekly Review](../_templates/piano/Weekly%20Review.md)
- [12-Week Goal](../_templates/piano/12-Week%20Goal.md)

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
FROM "Pieces"
WHERE type = "piece" AND status != "shelved"
SORT status ASC, composer ASC
```

### Shelved pieces
```dataview
TABLE composer, status, notes
FROM "Pieces"
WHERE type = "piece" AND status = "shelved"
SORT composer ASC
```
```

---

## FILE: `_templates/piano/Piece Note.md` (REWRITTEN)

```markdown
---
type: piece
composer:
title: "{{title}}"
status: active
stage:
learning_piece: false
polishing_piece: false
target_tempo:
current_tempo:
edition:
recordings:
tags:
- piece
---
# {{title}} — {{date}}

## Overview
- Composer:
- Title:
- Stage:
- Status:
- Edition:
- Target tempo:
- Current tempo:

## Purpose
- Technical objective:
- Musical objective:
- Why this piece:

## Logs
- [[{{title}} - Error Log|Error log]]
- [[{{title}} - Tempo Log|Tempo log]]

## Movement map
Name the archetype(s) per passage. Full specs: [Movement](../../Piano/Resources/Movement.md).
Mark the seams (S) — errors live there.

| Bars | Archetype(s) | Seam notes | Concern |
| ---- | ------------ | ---------- | ------- |
|      |              |            |         |

- Hardest seam (first Q-spot):
- Gait transition needed? (slow gait → fast gait): yes / no, at approx tempo:

## Personal calibration (this piece)
Copy relevant deviations from your Personal Calibration Log, or add new ones here.
-

## Current focus
1.
2.
3.

## Q-spots
| Bar(s) | Problem | Archetype | Strategy | Status |
| ------ | ------- | --------- | -------- | ------ |
|        |         |           |          |        |

## Structure and memory
- Form:
- Key areas:
- Major structural start points:
- Hardest sections:

## Listening
| Recording | Artist | Observation |
| --------- | ------ | ----------- |
|           |        |             |

## Daily sessions
Daily work is logged in `Daily/` using the unified template.
Piece-specific progress is tracked in the Error Log and Tempo Log above.

## Readiness
- [ ] Plays through without major breakdown
- [ ] Can start from several structural points
- [ ] Hardest section can be played without preparatory reps
- [ ] Maintains pulse after a minor mistake
- [ ] Intended dynamics, articulation, voicing, pedaling present
- [ ] No pain or excessive tension
- [ ] Movement form holds at target tempo (diagnostic run cold)
- [ ] Passes on at least two separate days