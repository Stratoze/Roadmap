# Pieces README

This folder contains all serious piece work.

## Folder convention

```text
Pieces/Composer/Piece Title/
  Piece Title.md
  Piece Title - Error Log.md
  Piece Title - Tempo Log.md
```

Daily session notes go in `Daily/` using the unified template
(`_system/Daily Template.md`). Put the piece name in the
**Milestone / Piece / Book** field. Do not create a `daily/`
subfolder inside the piece folder.

Piece-specific data lives in the piece's own logs:
- Tempo changes → `Piece Title - Tempo Log.md`
- Recurring errors → `Piece Title - Error Log.md`

Example:

```text
Pieces/Bach/Minuet in G/
  Minuet in G.md
  Minuet in G - Error Log.md
  Minuet in G - Tempo Log.md
```

## Naming rule

Use the same piece title in all file names.

Good:

```text
Minuet in G.md
Minuet in G - Error Log.md
Minuet in G - Tempo Log.md
```

Bad:

```text
bach minuet.md
error log.md
tempo.md
```

## When to create a piece folder

Create one when a piece is:

- a learning piece
- a polishing piece
- expected to stay active for more than 2–3 weeks
- important enough to track tempo and errors over time

Do not create one for:

- tiny method-book exercises
- sight-reading material
- one-off experiments
- casual fun pieces unless you want to

## Workflow

1. Create the piece folder.
2. Create the piece note from [Piece Note](../../_templates/piano/Piece%20Note.md).
3. Create the error log from [Piece Error Log](../../_templates/piano/Piece%20Error%20Log.md).
4. Create the tempo log from [Piece Tempo Log](../../_templates/piano/Piece%20Tempo%20Log.md).
5. Log daily sessions in `Daily/` using the unified template.
   Reference the piece name in the **Milestone / Piece / Book** field.
6. Log tempo changes and recurring errors in the piece's own logs,
   not in the daily note.
