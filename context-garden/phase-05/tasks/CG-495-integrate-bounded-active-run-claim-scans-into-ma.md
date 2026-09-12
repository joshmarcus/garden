---
id: CG-495
title: Integrate bounded active-run claim scans into main
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/web/pages/api.py
- src/garden/runs.py
- tests/test_remote_worker.py
branch: garden/cg-495-integrate-bounded-active-run-claim-scans-into-ma
pr: https://github.com/joshmarcus/context-garden/pull/397
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T01:20:49+00:00'
created: '2026-09-09T19:35:18+00:00'
updated: '2026-09-10T01:32:25+00:00'
---

## Goal

Integrate the already implemented and validated RC15 remote-claim performance fix into current main through Garden's normal source review and merge lifecycle.

## Frozen source

Use the exact source delta from commit `fb86636d08a7809f0b0288db218b85019136d265` relative to RC14 base `a057dd8a90e4b1a1107533a274e1519be631ed59`, branch `codex/rc15-claim-active-runs`. Transfer only:

- `src/garden/web/pages/api.py`: authenticated `POST /api/runs/claim` materializes `RunStore.active()` instead of all historical runs.
- `tests/test_remote_worker.py`: the focused authenticated claim, reclaim, stale-generation, six-idle-host, and concurrent Now regression.

Do not reimplement the behavior. Do not copy `pyproject.toml`, `src/garden/__init__.py`, `docs/releases/v0.3.0rc15.md`, release metadata, tags, deployment helpers, or unrelated candidate history.

## Dedupe and boundaries

CG-479 owns broad page-load optimization and is done. CG-417 owns task discovery snapshots. CG-493 owns retention of the RC14 discovery and CI runner-source guards. CG-491 owns transient and lost-response claim retry/idempotency. This task owns only the successful authenticated idle-claim scan cost and its exact existing source integration.

Preserve claim eligibility, host capacity, harness/tier filtering, lease recovery, current-generation authority, stale-generation rejection, heartbeat/finish behavior, and the CG-491 request-identity work.

## Existing validation

The frozen source already passed:

- exact CI run 34393741158 at frozen head
- 64 `tests/test_remote_worker.py` tests and Ruff
- independent source review with no findings
- installed RC13 WorkerClient to frozen RC15 controller TCP claim, heartbeat, generation fencing, reconnect, finish, and RC13 run-record load
- representative copied-state load with 3,889 historical runs, six active runs, six distinct authenticated idle hosts, 24 claims at three-second cadence, concurrent Now requests and one SSE stream: claim median 0.736s to 0.117s, p95 0.984s to 0.132s, and process CPU/wall 0.404 to 0.193

Controller receipts are preserved under `/home/joshua/work/operator-test-tmp/rc15-claim-active`.

## Acceptance criteria

- [ ] Integrate only the exact two-file behavior/test delta from frozen `fb86636d` onto current main, resolving context mechanically without redesigning or expanding scope.
- [ ] Prove authenticated claim admission sees every requested/preparing/running run needed for claim/current/recovery decisions while excluding terminal history; stale and replaced generations remain rejected.
- [ ] Keep the six-host concurrent claim/UI regression deterministic and bounded. Preserve meaningful existing remote-worker tests.
- [ ] The resulting source-only PR passes exact-head CI and independent substantive review with no conflict before Garden merges it.
- [ ] Record the frozen source identity and reuse the existing CI, peer, TCP, and representative load receipts without claiming release metadata is part of the source PR.

## Log

- 2026-09-09T19:36:19+00:00 dispatched work run 20260909T193619Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19090 tokens)
- 2026-09-09T19:41:05+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T19:42:27+00:00 opened https://github.com/joshmarcus/context-garden/pull/397 (base main): Integrated the exact RC15 active-run claim scan delta onto current main and committed it as 47d39b61. The focused remote-worker suite passed 59 tests and Ruff passed. cost=$0.65
- 2026-09-09T19:45:04+00:00 automated review: approve — The exact frozen two-file delta is integrated without scope expansion; no substantive defects found. cost=$0.31
- 2026-09-10T01:14:14+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/pages/api.py); a rebase agent will resolve it
- 2026-09-10T01:14:17+00:00 dispatched rebase run 20260910T011417Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1504 tokens)
- 2026-09-10T01:18:02+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/397: Resolved api.py conflict by preserving CG-491 replay handling over all runs and using active runs for claim admission; rebase onto origin/main completed. cost=$0.02
- 2026-09-10T01:20:39+00:00 automated review requested changes: The composed implementation is correct and focused, but the PR description contradicts the current source by claiming an identical stable patch ID. Update the verification claim to describe the intentional CG-491 replay composition. cost=$0.23
- 2026-09-10T01:20:49+00:00 dispatched revise run 20260910T012049Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20454 tokens)
- 2026-09-10T01:24:32+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T01:25:52+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/397: Corrected the PR description to accurately document the RC15 active-run scan composed with CG-491’s all-history replay lookup. At head fcae6a77, all 61 remote-worker tests and Ruff passed; merge-tree reports no conflict with current origin/main. cost=$0.34
- 2026-09-10T01:28:26+00:00 automated review: approve — The bounded active-run admission scan is correctly composed with CG-491’s all-history replay lookup; no substantive defects found. cost=$0.22
- 2026-09-10T01:30:56+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T01:32:25+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/397
