---
id: CG-523
title: Make web benchmark size controls internally consistent
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/app.py
- tests/test_web.py
branch: garden/cg-523-make-web-benchmark-size-controls-internally-cons
pr: https://github.com/joshmarcus/context-garden/pull/438
runner: remote
discovered_from: CG-503
attempts: 1
last_dispatched_at: '2026-09-10T12:55:27+00:00'
created: '2026-09-10T11:25:39+00:00'
updated: '2026-09-10T13:15:27+00:00'
file: scripts/benchmark_web_pages.py
error: Using --runs 0 fails with a 404 because the fixed route list still requests seed-0001.
---

Define and test zero/one/default task and run fixture behavior. Derive benchmark routes from generated identities or reject unsupported minima explicitly, while preserving the JSON output contract.

## Provenance

Discovered by CG-503 (Find removable and overengineered code to simplify and optimize) during run `20260910T111342Z-work`.
## Log
- 2026-09-10T11:25:39+00:00 discovered by CG-503

## Acceptance criteria

- [ ] Define zero, one and default task/run fixture minima explicitly; either generate only routes backed by created identities or reject an unsupported zero value before serving requests.
- [ ] Every benchmark route exists for the generated fixture, including boundary values, so input validation never degrades into an unrelated HTTP 404.
- [ ] Preserve the existing machine-readable JSON fields and timing semantics for supported inputs, with an actionable nonzero CLI error for rejected inputs.
- [ ] Add focused zero/one/default and mixed task/run tests, run a small disposable benchmark, and keep repository lint clean.
- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T12:55:27+00:00 dispatched work run 20260910T125527Z-work via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~14510 tokens)
- 2026-09-10T13:03:01+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:04:33+00:00 opened https://github.com/joshmarcus/context-garden/pull/438 (base main): Fixed benchmark size controls so supported fixtures only serve routes backed by generated identities, while unsupported zero task/run sizes fail clearly. Focused tests and Ruff lint passed on commit 968a8c10. cost=$0.04
- 2026-09-10T13:07:41+00:00 automated review: approve — The size validation and generated route identities are internally consistent with fixture creation, including mixed task/run counts. Supported inputs preserve the benchmark output contract, while unsupported minima fail clearly. cost=$0.16
- 2026-09-10T13:15:27+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/438
