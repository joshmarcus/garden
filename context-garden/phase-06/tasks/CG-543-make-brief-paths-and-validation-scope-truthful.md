---
id: CG-543
title: Make brief paths and validation scope truthful
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-293
  after: merge
- id: CG-294
  after: merge
- id: CG-483
  after: merge
priority: 2
difficulty: medium
reading:
- src/garden/brief.py
- src/garden/scheduler/dispatch.py
- src/garden/validation.py
branch: garden/cg-543-make-brief-paths-and-validation-scope-truthful
pr: https://github.com/joshmarcus/context-garden/pull/466
runner: remote
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T17:32:15+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T18:51:54+00:00'
---

## Goal

User value: workers spend time on implementation rather than locating context that is already supplied. Why now: late CG-434/437 reports persist after brief-gate work. Size: medium. Dependencies: CG-293/294/483 and existing scope planning; distinguish inlined, controller-owned and checkout-readable content and refresh scope when behavior changes.

## Context

Proposed at the context-garden/phase-05 retro. Repeated late-phase context errors show that presence checks alone are insufficient.


## Reviewed scope and verification

Make the brief distinguish inlined content, checkout-readable files and controller-owned references, with a usable source/context location for each. Keep a genuinely absent required input actionable and preserve configured validation scope. Verify representative garden and product references, unavailable paths, inlined large files and scope refresh without requesting nonexistent checkout paths or requiring unrelated evidence.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:32:15+00:00 dispatched work run 20260910T173214Z-work-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~11896 tokens)
- 2026-09-10T17:38:05+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:41:31+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$0.69
- 2026-09-10T18:34:19+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:22+00:00 opened https://github.com/joshmarcus/context-garden/pull/466 (base main): Briefs now label oversized garden inputs and run snapshots as controller-owned rather than asking workers to read nonexistent checkout paths, while product-checkout references remain readable. Validation-plan wording now accurately describes dispatch-time scope and its refresh before pre-check/review; focused tests passed (196).
- 2026-09-10T18:34:22+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T18:46:44+00:00 automated review: approve — Briefs now truthfully distinguish inlined, checkout-readable, controller-owned, and missing inputs, while validation wording matches dispatch-time scope refresh. cost=$0.44
- 2026-09-10T18:50:02+00:00 automated review: approve — Briefs now distinguish inlined, checkout-readable, controller-owned, and unresolved inputs, while validation wording accurately reflects dispatch-time scope and later refresh. cost=$0.55
- 2026-09-10T18:51:54+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/466
