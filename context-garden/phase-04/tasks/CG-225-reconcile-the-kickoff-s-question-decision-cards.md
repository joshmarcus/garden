---
id: CG-225
title: Reconcile the kickoff's question-decision cards with CG-189 once it merges
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: medium
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

CG-189 (on its own unmerged branch) builds a fuller retro-question mechanism (Inbox, retro page, CLI answer flow). CG-224 added a smaller, self-contained question-decision-card mechanism for kickoff questions since CG-189 wasn't merged. Once CG-189 lands, reconcile the two so there is one question/decision mechanism shared by the retro and the kickoff, not two.

## Context

See src/garden/scheduler/kickoff.py's answer_kickoff_question/dismiss_kickoff_question and src/garden/web/actions/decisions.py.

## Provenance

Discovered by CG-224 (Phase kickoff: before a phase starts, flag topics that need design, goals without a definition of done, questions for the owner, and docs that need attention) during run `20260905T170505Z-work`.

## Log

- 2026-09-05T17:39:03+00:00 discovered by CG-224
