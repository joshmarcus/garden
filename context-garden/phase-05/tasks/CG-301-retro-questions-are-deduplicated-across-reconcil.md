---
id: CG-301
title: Retro questions are deduplicated across reconcile runs, and a second judge can run with task filing
  off
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/operator_spend.py
- tests/test_retro.py
created: '2026-09-06T00:00:00+00:00'
updated: '2026-09-06T00:00:00+00:00'
discovered_from: retro-editor:context-garden/phase-04

---

## Goal

Two reconcile runs of the same phase do not ask the owner the same question twice or file the same follow-ups twice: questions are matched by normalised text before decision cards are created, and garden retro takes --no-file (or a judge-only mode) so a comparison judge writes its document without filing drafts or blocking tasks.

## Context

The phase-04 retro ran twice (fable, then astra with --skip-personas). Each asked the same six questions in different words, so the owner answered each twice and phase-05/goals.md carries every decision twice; each also filed the same 31 persona findings and its own blocking set from one live id counter (CG-244 covers the ids). Raised by the retro-editor persona, 2026-09-05.

## Acceptance criteria

- [ ] A second reconcile run on the same phase files no question card whose normalised text matches an open or answered card from the first run; the answer is copied onto the retro record instead
- [ ] garden retro --no-file writes retro.md and the goals draft and opens the PR without filing features, follow-ups, blocking tasks or persona-finding drafts, and says so in the document header
- [ ] Tests: two runs with paraphrased questions yield one card each; --no-file leaves the task tree untouched

