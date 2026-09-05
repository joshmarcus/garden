---
id: CG-157
title: The Inbox friction form's product and phase selects cannot produce a 404
status: done
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 3
difficulty: easy
reading: []
branch: garden/cg-157-the-inbox-friction-form-s-product-and-phase-sele
pr: https://github.com/joshmarcus/context-garden/pull/121
discovered_from: retro:context-garden/phase-02-friction
attempts: 1
last_dispatched_at: '2026-09-05T05:02:02+00:00'
created: '2026-09-05T03:14:37+00:00'
updated: '2026-09-05T05:37:37+00:00'
---

## Goal

The Inbox friction form's product and phase selects cannot produce a 404.

## Context

From the phase-02 retro's open list (item 11), reconciled against what merged on 2026-09-05: "Inbox friction form independent selects return a bare 404 (CG-044)". See `../phase-02-friction/docs/retro.md` for the evidence and the persona reports under `../phase-02-friction/docs/reviews/`. Write the acceptance criteria when the task is planned.

## Acceptance criteria

- [ ] to be written at planning; the retro item above is the requirement.

## Log
- 2026-09-05T03:15:00+00:00 filed from the phase-02 retro (open item 11)
- 2026-09-05T03:20:00+00:00 approved (web)
- 2026-09-05T05:02:02+00:00 dispatched work run 20260905T050153Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~3684 tokens)
- 2026-09-05T05:12:29+00:00 opened https://github.com/joshmarcus/context-garden/pull/121 (base main): Fixed the Inbox friction form so its phase select is built client-side from a per-product map, making it structurally impossible to submit a product/phase pair from different products (which previously hit a bare 404). Added a regression test with two products; full test suite and lint pass. cost=$1.09
- 2026-09-05T05:17:48+00:00 automated review: approve — The phase select is now built client-side from a per-product data-phases map, making a cross-product (product, phase) pair structurally impossible, which was the source of the bare 404; covered by a regression test, with web tests and ruff passing. cost=$0.58
- 2026-09-05T05:23:32+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T05:24:29+00:00 rebased; diff unchanged; verdict kept
- 2026-09-05T05:35:27+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T05:36:21+00:00 rebased; diff unchanged; verdict kept
- 2026-09-05T05:37:37+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/121
