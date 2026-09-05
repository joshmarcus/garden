---
id: CG-150
title: garden friction keeps hand-written sections and the retro reads the Reported section and comment
  friction
status: done
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 2
difficulty: easy
reading: []
branch: garden/cg-150-garden-friction-keeps-hand-written-sections-and
pr: https://github.com/joshmarcus/context-garden/pull/116
discovered_from: retro:context-garden/phase-02-friction
attempts: 1
last_dispatched_at: '2026-09-05T04:48:14+00:00'
created: '2026-09-05T03:14:36+00:00'
updated: '2026-09-05T05:48:39+00:00'
---

## Goal

garden friction keeps hand-written sections and the retro reads the Reported section and comment friction.

## Context

From the phase-02 retro's open list (item 2), reconciled against what merged on 2026-09-05: "garden friction drops the hand-written First live run section; the retro reconciliation reads neither the Reported section nor comment friction". See `../phase-02-friction/docs/retro.md` for the evidence and the persona reports under `../phase-02-friction/docs/reviews/`. Write the acceptance criteria when the task is planned.

## Acceptance criteria

- [ ] to be written at planning; the retro item above is the requirement.

## Log
- 2026-09-05T03:15:00+00:00 filed from the phase-02 retro (open item 2)
- 2026-09-05T03:19:59+00:00 approved (web)
- 2026-09-05T04:48:14+00:00 dispatched work run 20260905T044804Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~3719 tokens)
- 2026-09-05T04:57:04+00:00 opened https://github.com/joshmarcus/context-garden/pull/116 (base main): garden friction now preserves any hand-written section (not just ## Reported) on rewrite, and garden retro's reconciliation now reads the phase's ## Reported friction log and unreconciled PR-comment friction alongside the harvested PR-body friction. cost=$1.67
- 2026-09-05T05:00:28+00:00 automated review: approve — Focused, well-tested change: garden friction now preserves any hand-written section and the retro reconciliation reads the Reported log and marked PR comments. Tests pass and lint is clean. cost=$0.83
- 2026-09-05T05:21:02+00:00 automated review: approve — garden friction now preserves any hand-written section on rewrite, and the retro reconciliation reads the phase's ## Reported log and marked-but-unreconciled PR-comment friction alongside PR-body friction. Well-tested (including a read-only assertion), full suite passes, lint clean. cost=$0.66
- 2026-09-05T05:30:55+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T05:31:50+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-150` for one more round, or review on GitHub
- 2026-09-05T05:37:32+00:00 automated review: approve — garden friction now preserves any hand-written section on rewrite, and the retro reconciliation reads the phase's ## Reported log and marked-but-unreconciled PR-comment friction alongside PR-body friction. Well-tested (including a read-only assertion), targeted tests pass, lint clean. cost=$0.66
- 2026-09-05T05:43:11+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T05:44:05+00:00 rebased; diff unchanged; verdict kept
- 2026-09-05T05:48:39+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/116
