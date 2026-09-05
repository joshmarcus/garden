---
id: CG-226
title: A TUI answer flow for kickoff question cards
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/planner.py
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/scheduler/discovered.py
- src/garden/web/pages/phase.py
- src/garden/cli/planning.py
discovered_from: CG-224
created: '2026-09-05T17:39:03+00:00'
updated: '2026-09-05T17:39:03+00:00'
---

## Goal

The TUI currently shows a kickoff question card in the Inbox tab but has no dedicated key/flow to answer or dismiss it (only the web Inbox and `garden decide --answer/--dismiss` do). Add TUI parity.

## Context

See src/garden/tui/app.py's _selected_decision/_resolve_decision and src/garden/scheduler/kickoff.py's answer_kickoff_question/dismiss_kickoff_question.

## Provenance

Discovered by CG-224 (Phase kickoff: before a phase starts, flag topics that need design, goals without a definition of done, questions for the owner, and docs that need attention) during run `20260905T170505Z-work`.

## Log

- 2026-09-05T17:39:03+00:00 discovered by CG-224
