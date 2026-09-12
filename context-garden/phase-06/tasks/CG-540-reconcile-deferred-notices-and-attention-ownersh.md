---
id: CG-540
title: Reconcile deferred notices and attention ownership
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-437
  after: merge
- id: CG-480
  after: merge
priority: 2
difficulty: medium
reading:
- src/garden/inbox.py
- src/garden/web/pages/inbox.py
- src/garden/web/pages/task.py
- src/garden/scheduler/human.py
branch: garden/cg-540-reconcile-deferred-notices-and-attention-ownersh
pr: https://github.com/joshmarcus/context-garden/pull/451
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T16:45:23+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T16:58:48+00:00'
---

## Goal

User value: a saved deferral stops demanding a decision while preserving the execution hold. Why now: persona observations disagree across snapshots. Size: medium. Dependencies: CG-437, CG-480 and current shared attention logic; first establish which current states are wrong, then align notices, badges and reconsider actions.

## Context

Proposed at the context-garden/phase-05 retro. Resolve observed ownership inconsistencies with current behavior rather than replaying an older UI assessment.


## Reviewed scope and verification

First reproduce a concrete discrepancy on current accepted source: compare saved deferral, current effective policy/source, badge count, next action and execution hold. Preserve separately owned holds and allow deliberate reconsideration. Consolidate CG-552 effective-rule/source clarity here, coordinating existing CG-514 policy ownership rather than adding another review-count mechanism. Make only demonstrated corrections, or record the finding as already resolved with source-specific evidence.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T15:39:24+00:00 dispatched work run 20260910T153920Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~14475 tokens)
- 2026-09-10T15:46:42+00:00 discovered work filed: CG-591
- 2026-09-10T15:46:42+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:47:57+00:00 opened https://github.com/joshmarcus/context-garden/pull/451 (base main): Saved troubled-work deferrals now appear as non-badge Deferred work notices with an explicit reconsider action that restores the preserved decision without starting execution. Verified lint and compilation on commit 6651a8d76bf23daba4bda83c700237fc8f16c21a; focused pytest could not collect because of an existing circular import outside this change. cost=$0.84
- 2026-09-10T15:49:13+00:00 CI failure
- 2026-09-10T16:16:16+00:00 dispatched revise run 20260910T161613Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~15572 tokens)
- 2026-09-10T16:21:07+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:22:27+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/451: Resolved the test-collection circular import by lazily exporting the run-backed host drain bridge, and ensured a saved troubled-work deferral has reconsideration as its sole task action. Verified focused attention and remote-host behavior, lint, and source compilation on commit eb623aed. cost=$0.54
- 2026-09-10T16:27:59+00:00 automated review: approve — Saved troubled-work deferrals are correctly presented as non-decision notices while retaining their execution hold, and reconsideration restores the preserved troubled-task decision without dispatch. cost=$0.68
- 2026-09-10T16:37:28+00:00 triage: changes requested by hand: Preserve the independently approved troubled-deferral notice and reconsideration behavior. Actual push CI34501543906 fai
- 2026-09-10T16:45:23+00:00 dispatched revise run 20260910T164520Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~15718 tokens)
- 2026-09-10T16:48:53+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:50:09+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/451: Normalized frozen deferred Inbox cards so the shared template always receives a kind, preserving move-only frozen work and reconsideration-only saved troubled deferrals. Focused Inbox regressions, combined move/web/attention tests, lint, and compilation passed. cost=$0.49
- 2026-09-10T16:52:58+00:00 automated review: approve — Saved troubled-work deferrals now appear as non-badge Deferred work notices while preserving the execution hold; reconsideration restores the troubled-task decision without dispatching work. cost=$0.35
- 2026-09-10T16:58:48+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/451
