---
id: CG-226
title: A TUI answer flow for kickoff question cards
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-224
- CG-225
priority: 3
difficulty: easy
reading:
- src/garden/planner.py
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/scheduler/discovered.py
- src/garden/web/pages/phase.py
- src/garden/cli/planning.py
branch: garden/cg-226-a-tui-answer-flow-for-kickoff-question-cards
pr: https://github.com/joshmarcus/context-garden/pull/180
harness: codex
discovered_from: CG-224
attempts: 1
last_dispatched_at: '2026-09-05T18:57:58+00:00'
created: '2026-09-05T17:39:03+00:00'
updated: '2026-09-05T19:10:53+00:00'
---

## Goal

The TUI currently shows a kickoff question card in the Inbox tab but has no dedicated key/flow to answer or dismiss it (only the web Inbox and `garden decide --answer/--dismiss` do). Add TUI parity.

## Context

See src/garden/tui/app.py's _selected_decision/_resolve_decision and src/garden/scheduler/kickoff.py's answer_kickoff_question/dismiss_kickoff_question.

## Provenance

Discovered by CG-224 (Phase kickoff: before a phase starts, flag topics that need design, goals without a definition of done, questions for the owner, and docs that need attention) during run `20260905T170505Z-work`.

## Log

- 2026-09-05T17:39:03+00:00 discovered by CG-224
- 2026-09-05T17:48:28+00:00 approved (web)
- 2026-09-05T17:48:28+00:00 priority 1 -> 3 (web)
- 2026-09-05T18:57:58+00:00 dispatched work run 20260905T185744Z-work via local [codex] (fresh session, base main, ~21166 tokens)
- 2026-09-05T19:06:14+00:00 opened https://github.com/joshmarcus/context-garden/pull/180 (base main): Added TUI answer and dismiss flows for kickoff question cards, with full question details and stable answer targeting across refreshes.
- 2026-09-05T19:07:49+00:00 automated review: approve — The stated TUI parity goal is implemented with stable answer targeting and scheduler-backed resolution. All 18 focused TUI/kickoff tests and repository lint pass; the task contains no explicit acceptance criteria.
- 2026-09-05T19:09:22+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-05T19:10:53+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/180
