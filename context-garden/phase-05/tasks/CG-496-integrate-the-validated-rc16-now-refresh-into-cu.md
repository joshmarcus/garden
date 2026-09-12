---
id: CG-496
title: Integrate the validated RC16 Now refresh into current main
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/now1.py
- src/garden/web/pages/now1.py
- tests/test_web.py
branch: garden/cg-496-integrate-the-validated-rc16-now-refresh-into-cu
pr: https://github.com/joshmarcus/context-garden/pull/408
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T20:09:30+00:00'
created: '2026-09-09T20:08:32+00:00'
updated: '2026-09-10T01:58:03+00:00'
---

## Goal

Integrate the validated RC16 Now-page refresh implementation into current main as a normal native Garden change. The frozen source is release head `6716338` relative to RC15 `fb866`; carry only the source changes in `src/garden/now1.py`, `src/garden/web/pages/now1.py`, and `tests/test_web.py`. Exclude release notes, version metadata, deployment helpers, and generated evidence.

## Required behavior

- Preserve the shared left navigation and current Now information while making initial rendering fast and letting independently available regions refresh without rebuilding the whole page.
- Keep the summary, period detail, owner-attention state, profile/config/capacity state, and automerge/event data consistent as their source facts change.
- Preserve populated, sparse, paused, failure/recovery, desktop/mobile, and light/dark behavior.
- Reconcile against current main and related native work before editing. CG-417 is an older task snapshot, CG-479 owns broader page performance, and CG-495 owns claim-path scan integration; do not duplicate or overwrite them.

## Acceptance criteria

- [ ] Integrate only the three frozen RC16 source files or an equivalent minimal current-main patch, with no release/version/deployment artifacts.
- [ ] Initial document generation avoids waiting for independent slow regions and partial refreshes update the intended region atomically.
- [ ] Focused Now/web tests and Ruff pass at the final source head.
- [ ] A served HTTP/browser journey covers populated, sparse, paused, failure/recovery, 1280px/390px, and light/dark states and verifies the shared navigation remains usable.
- [ ] Preserve current-main changes and document any semantic conflict resolution.

## Existing validation

The frozen RC16 source passed 47 focused tests, Ruff, exact-source review with no findings, and a real Windows/browser partial-refresh fanout. Treat this as source provenance for integration, then verify the reconciled final head independently.

## Log

- 2026-09-09T20:08:32+00:00 approved native integration of validated frozen RC16 source; dispatch waits for future remote capacity
- 2026-09-09T20:09:30+00:00 dispatched work run 20260909T200930Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15869 tokens)
- 2026-09-09T23:51:06+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T23:52:33+00:00 opened https://github.com/joshmarcus/context-garden/pull/408 (base main): Integrated the validated RC16 Now refresh into current main at f2fe6bed, changing only src/garden/now1.py, src/garden/web/pages/now1.py, and tests/test_web.py. Focused tests, Ruff, and the served browser lifecycle/viewport replay passed at the committed head. cost=$1.03
- 2026-09-09T23:56:53+00:00 automated review: approve — The bounded Now refresh integration is minimal, preserves current-main behavior, and has no blocking defects. cost=$0.24
- 2026-09-10T01:58:03+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/408
