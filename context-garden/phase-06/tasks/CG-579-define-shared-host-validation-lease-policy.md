---
id: CG-579
title: Define shared-host validation lease policy
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-365
  after: merge
priority: 3
difficulty: hard
reading:
- src/garden/validation.py
- src/garden/config.py
- src/garden/scheduler/resources.py
branch: garden/cg-579-define-shared-host-validation-lease-policy
pr: https://github.com/joshmarcus/context-garden/pull/468
runner: remote
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T17:49:21+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T20:00:49+00:00'
---

## Goal

Specify one authoritative capacity policy for gardens sharing a user and lock namespace, including clear mismatch handling and a safe migration path. Preserve current process ownership and resource limits; do not raise capacity as part of the change.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Define the supported shared namespace identity, authority for capacity, behavior for conflicting configurations, owner-visible diagnosis and migration/recovery rules before changing enforcement. Preserve active leases and current aggregate caps across multiple gardens. Do not silently increase capacity or reinterpret another garden's lock. Test the agreed contract with isolated competing clients.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:49:21+00:00 dispatched work run 20260910T174921Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15089 tokens)
- 2026-09-10T17:56:39+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:59:52+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$1.12
- 2026-09-10T18:34:25+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:27+00:00 opened https://github.com/joshmarcus/context-garden/pull/468 (base main): Defined and implemented the per-user/runtime-directory validation lease policy, including atomic slot claims, visible mismatch behavior, and an idle-only capacity migration command. Verified commit 5362265416a50d2e870beca461273bcac6824d2d with 76 runner tests, three focused exact-head policy/CLI tests, and clean changed-file lint.
- 2026-09-10T18:34:27+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T19:09:52+00:00 automated review: approve — The change defines a coherent shared namespace and safely serializes capacity migration against new and active lease claims without increasing capacity implicitly. cost=$0.27
- 2026-09-10T19:19:52+00:00 automated review: approve — The shared-host capacity policy and idle-only migration path are correctly implemented without silently increasing capacity or reinterpreting active leases. cost=$0.31
- 2026-09-10T20:00:49+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/468
