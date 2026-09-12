---
id: CG-522
title: Use copy-on-write web discovery snapshots
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/store.py
- src/garden/web/app.py
- src/garden/web/common.py
- tests/test_store.py
- tests/test_web.py
branch: garden/cg-522-use-copy-on-write-web-discovery-snapshots
pr: https://github.com/joshmarcus/context-garden/pull/439
runner: remote
discovered_from: CG-503
attempts: 1
last_dispatched_at: '2026-09-10T13:11:06+00:00'
created: '2026-09-10T11:25:39+00:00'
updated: '2026-09-10T13:27:09+00:00'
file: src/garden/store.py
error: Every web request fingerprints and deep-copies the complete mutable discovery tree, including read-only
  GET requests.
---

Avoid deep-copying the entire product/phase/task tree for read-only requests while preserving stable per-request views, concurrent action safety, duplicate-ID quarantine, external edit detection, and fence-gated config reload. Compare the existing 120- and 600-task fixtures before and after under identical limits.

## Provenance

Discovered by CG-503 (Find removable and overengineered code to simplify and optimize) during run `20260910T111342Z-work`.
## Log
- 2026-09-10T11:25:39+00:00 discovered by CG-503

## Acceptance criteria

- [ ] Read-only web requests use a stable versioned or copy-on-write discovery snapshot without fingerprinting and deep-copying the complete mutable tree for every request.
- [ ] Concurrent task/config actions cannot mutate an in-flight request view; duplicate-ID quarantine, external edit detection and fence-gated config reload retain their current fail-closed behavior.
- [ ] Snapshot invalidation is atomic across product, phase and task mutations and does not serve mixed generations after restart or concurrent writes.
- [ ] Compare identical 120- and 600-task web fixtures before and after, exercise concurrent reads plus mutation and external edits, and run focused Store/web tests and lint.
- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T12:52:14+00:00 dispatched work run 20260910T125213Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~19892 tokens)
- 2026-09-10T13:06:06+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:07:40+00:00 opened https://github.com/joshmarcus/context-garden/pull/439 (base main): Implemented copy-on-write web discovery generations with Linux filesystem notification invalidation and isolated action Stores. Verified focused Store/web tests, lint, concurrent reader/action isolation, external-edit refresh, and 120/600-task before/after benchmarks on commit 2e6becfd. cost=$0.88
- 2026-09-10T13:10:44+00:00 automated review requested changes: Copy-on-write isolation works, but partial inotify setup can silently disable external-edit detection. cost=$0.29
- 2026-09-10T13:11:06+00:00 dispatched revise run 20260910T131105Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~20741 tokens)
- 2026-09-10T13:16:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:18:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/439: Fail-closed inotify discovery-watch setup now disables incomplete watchers so external edits use Store signature detection. Added regression coverage and verified focused Store/web tests plus lint on commit 7076c53e. cost=$0.57
- 2026-09-10T13:22:27+00:00 automated review: approve — Copy-on-write web discovery snapshots preserve stable request views and external-edit safety. The previous partial-watcher defect is resolved. cost=$0.36
- 2026-09-10T13:27:09+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/439
