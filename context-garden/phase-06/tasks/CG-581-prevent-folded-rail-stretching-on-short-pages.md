---
id: CG-581
title: Prevent folded rail stretching on short pages
status: done
product: context-garden
phase: phase-06
depends_on: []
priority: 4
difficulty: easy
reading:
- src/garden/web/templates/base.html
- src/garden/web/pages/now1.py
branch: garden/cg-581-prevent-folded-rail-stretching-on-short-pages
pr: https://github.com/joshmarcus/context-garden/pull/470
runner: remote
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T17:50:58+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T19:26:36+00:00'
---

## Goal

Check the specific tall-viewport short-page grid behavior reported by CG-308. If it persists, keep the rail at its intended content height without changing normal scrolling or mobile layout. Verify the affected short-page rendering proportionately rather than recapturing every page.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Reproduce the precise folded-rail stretch on a short page in a tall viewport against current accepted source. If present, repair that layout while preserving ordinary scrolling and the mobile layout; inspect only representative affected views. If current source already fixes it, retire with the observed source/page result and no unnecessary rewrite.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:50:58+00:00 dispatched work run 20260910T175057Z-work-2 via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~12610 tokens)
- 2026-09-10T17:55:04+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:58:27+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$0.05
- 2026-09-10T18:34:30+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:32+00:00 opened https://github.com/joshmarcus/context-garden/pull/470 (base main): Prevented the folded responsive rail from stretching to the shell's 100vh height on short pages by adding align-self:start. Added a regression test and verified the full web test module.
- 2026-09-10T18:34:32+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T19:23:41+00:00 automated review: approve — The responsive rail now remains content-height on short folded layouts while desktop sticky sizing and narrow-page width remain unchanged. cost=$0.42
- 2026-09-10T19:25:02+00:00 automated review: approve — The folded rail remains content-height on short pages without changing desktop sticky sizing or introducing horizontal overflow. cost=$0.20
- 2026-09-10T19:26:36+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/470
