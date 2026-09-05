---
id: CG-225
title: Reconcile the kickoff's question-decision cards with CG-189 once it merges
status: ready
product: context-garden
phase: phase-04
depends_on:
- CG-224
priority: 1
difficulty: medium
reading:
- src/garden/planner.py
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/scheduler/discovered.py
- src/garden/web/pages/phase.py
- src/garden/cli/planning.py
branch: garden/cg-225-reconcile-the-kickoff-s-question-decision-cards
discovered_from: CG-224
last_dispatched_at: '2026-09-05T18:11:56+00:00'
created: '2026-09-05T17:39:03+00:00'
updated: '2026-09-05T18:14:44+00:00'
---

## Goal

CG-189 (on its own unmerged branch) builds a fuller retro-question mechanism (Inbox, retro page, CLI answer flow). CG-224 added a smaller, self-contained question-decision-card mechanism for kickoff questions since CG-189 wasn't merged. Once CG-189 lands, reconcile the two so there is one question/decision mechanism shared by the retro and the kickoff, not two.

## Context

See src/garden/scheduler/kickoff.py's answer_kickoff_question/dismiss_kickoff_question and src/garden/web/actions/decisions.py.

## Provenance

Discovered by CG-224 (Phase kickoff: before a phase starts, flag topics that need design, goals without a definition of done, questions for the owner, and docs that need attention) during run `20260905T170505Z-work`.

## Log

- 2026-09-05T17:39:03+00:00 discovered by CG-224
- 2026-09-05T17:48:27+00:00 approved (web)
- 2026-09-05T17:48:46+00:00 dispatched work run 20260905T174831Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-224-phase-kickoff-before-a-phase-starts-flag-topics stacked on CG-224, ~25703 tokens)
- 2026-09-05T17:53:28+00:00 worker blocked: CG-189 has not merged: its branch is not an ancestor of main, origin/main, or this branch, and it forked before the kickoff mechanism (CG-224) existed, so there is no second question/decision implementation in the tree to reconcile the kickoff's cards against yet. Reimplementing or guessing CG-189's design here would be out of scope and likely to conflict with whatever actually lands. cost=$0.51
- 2026-09-05T17:58:01+00:00 parent CG-224 merged; rebased onto main and retargeted the PR
- 2026-09-05T18:11:40+00:00 dispatched trial run 20260905T181127Z-trial via local [claude model=claude-sonnet-5] (fresh session, base main, ~25925 tokens)
- 2026-09-05T18:11:56+00:00 dispatched trial run 20260905T181141Z-trial via local [codex] (fresh session, base main, ~25960 tokens)
- 2026-09-05T18:11:56+00:00 trial started with claude:claude-sonnet-5, codex
- 2026-09-05T18:12:38+00:00 trial: no contender produced a PR
- 2026-09-05T18:14:44+00:00 reset to ready by hand
