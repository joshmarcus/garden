---
id: CG-524
title: Consolidate historical interaction capture harnesses
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/walkthrough.py
- src/garden/web/app.py
- tests/test_web.py
- docs/architecture.md
branch: garden/cg-524-consolidate-historical-interaction-capture-harne
pr: https://github.com/joshmarcus/context-garden/pull/440
runner: remote
discovered_from: CG-503
attempts: 1
last_dispatched_at: '2026-09-10T12:56:45+00:00'
created: '2026-09-10T11:25:40+00:00'
updated: '2026-09-10T13:19:52+00:00'
file: scripts/replay_cg381_inbox.py
error: Several root-level task-specific capture scripts repeat harness setup and are consumed only by
  historical evidence receipts.
---

Map each task-specific capture receipt to reproducible behavior, extract only common disposable garden/server setup into maintained tooling, and move or replace historical scripts without losing source-head and environment provenance.

## Provenance

Discovered by CG-503 (Find removable and overengineered code to simplify and optimize) during run `20260910T111342Z-work`.
## Log
- 2026-09-10T11:25:40+00:00 discovered by CG-503

## Acceptance criteria

- [ ] Inventory each task-specific capture script, its preserved receipt and the behavior it still reproduces before moving, replacing or deleting it.
- [ ] Extract only shared disposable Garden/server setup into maintained tooling; keep task-specific assertions with historical evidence or replace them with focused maintained tests.
- [ ] Preserve source-head, environment, viewport and result provenance so historical captures remain attributable and current behavior can be reproduced without private live state.
- [ ] Exercise the consolidated helper and representative CG-381/CG-410 behaviors, verify no maintained workflow references removed paths, and run focused interaction/web tests plus lint.
- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T12:56:45+00:00 dispatched work run 20260910T125644Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~14572 tokens)
- 2026-09-10T13:07:41+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:09:19+00:00 opened https://github.com/joshmarcus/context-garden/pull/440 (base main): Retired CG-381, CG-410, and CG-455 task-specific capture scripts, documented each receipt's provenance and maintained coverage, and added served HTTP regressions for CG-381/CG-410 using the shared disposable QA server. Verified current-head focused interaction tests and lint; the broader web selection passed at 9579af5d and no application source changed afterward. cost=$0.83
- 2026-09-10T13:13:42+00:00 automated review: approve — The consolidation preserves attributable historical receipts while moving reusable served-app setup into the QA sandbox and retaining focused CG-381/CG-410 regressions. cost=$0.33
- 2026-09-10T13:19:52+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/440
