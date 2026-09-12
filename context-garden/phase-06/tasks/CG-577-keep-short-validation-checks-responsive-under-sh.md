---
id: CG-577
title: Keep short validation checks responsive under shared admission
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-361
  after: merge
- id: CG-365
  after: merge
- id: CG-593
  after: merge
priority: 3
difficulty: medium
reading:
- src/garden/validation.py
- src/garden/scheduler/resources.py
- src/garden/scheduler/checkruns.py
- src/garden/runner/local.py
branch: garden/cg-577-keep-short-validation-checks-responsive-under-sh
pr: https://github.com/joshmarcus/context-garden/pull/459
runner: remote
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T18:47:16+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T19:02:49+00:00'
---

## Goal

Measure and distinguish queue wait from execution time for short lint and focused checks. Reuse existing resource controls and investigate bounded admission or lease scoping so waiting for external CI does not monopolize local capacity. Preserve all host caps and avoid stress workloads in ordinary tests.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Measure a reproducible admission delay for a short lint/focused check and identify the exact lease/admission owner. Separate local queue, execution and external CI waits. Make the smallest scheduling or lease-scope correction justified by the measurement, preserving aggregate capacities, fairness, process ownership and deadlines. Use bounded deterministic contention fixtures, not stress runs in the ordinary suite.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:47:33+00:00 dispatched work run 20260910T174733Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~17708 tokens)
- 2026-09-10T17:54:53+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:56:29+00:00 opened https://github.com/joshmarcus/context-garden/pull/459 (base main): Nested local check validations inherit their check run's shared lease, so focused pytest can execute while another admitted check waits externally without acquiring a second slot. Verified with deterministic two-check contention regression, focused runner tests, isolation tests, and Ruff. cost=$0.87
- 2026-09-10T17:59:51+00:00 automated review: approve — Nested local validations correctly inherit their detached check run's lease, preventing self-contention while preserving host admission limits. cost=$0.45
- 2026-09-10T18:12:46+00:00 triage: changes requested by hand: Conditional CG593 shared-main repair hold. Actual pushCI34511114353 reports2622passed and three inherited failures: arch
- 2026-09-10T18:46:03+00:00 troubled task continued with 1 bounded revision(s) at medium
- 2026-09-10T18:47:16+00:00 dispatched revise run 20260910T184716Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~18798 tokens)
- 2026-09-10T18:50:03+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:51:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/459: Rebased the detached-check inherited-lease change onto origin/main (including CG593) at fd272e19. Verified the focused runner suite exits successfully under supervised validation and Ruff is clean; no type-check tool is configured. cost=$0.36
- 2026-09-10T18:56:23+00:00 automated review: approve — Detached local checks correctly pass their owner-scoped lease to nested validation, keeping focused checks responsive without increasing host capacity. cost=$0.30
- 2026-09-10T19:02:49+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/459
