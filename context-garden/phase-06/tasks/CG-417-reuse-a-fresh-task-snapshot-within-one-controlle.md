---
id: CG-417
title: Reuse a fresh task snapshot within one controller operation
status: done
product: context-garden
phase: phase-06
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/store.py
- src/garden/scheduler/__init__.py
- src/garden/web/app.py
- tests/test_store.py
branch: garden/cg-417-reuse-a-fresh-task-snapshot-within-one-controlle
pr: https://github.com/joshmarcus/context-garden/pull/393
discovered_from: CG-380
attempts: 1
last_dispatched_at: '2026-09-10T04:29:33+00:00'
created: '2026-09-07T23:43:23+00:00'
updated: '2026-09-10T05:02:29+00:00'
file: src/garden/store.py
error: The 1,000-task fixture spends about 0.6 seconds per full task/product scan, with two scans dominating
  each no-dispatch tick and equivalent scans dominating Now, Inbox, and Config request CPU.
---

## Goal

Reuse one fresh task snapshot within a controller request or tick, reducing repeated full task scans without hiding external changes.

## Context

CG-380 measured approximately 0.6 seconds per full scan in the 1,000-task fixture; repeated scans dominated controller CPU. Preserve operation boundaries and existing state-writer synchronization.

## Acceptance criteria

- [ ] Matched 100- and 1,000-task before/after measurements report scan counts, served request latency and no-dispatch tick time using the same fixture and bounded resources.
- [ ] Repeated consumers inside one operation reuse an immutable snapshot; the next operation observes external edits and cross-process state changes.
- [ ] Focused tests prove snapshot reuse, invalidation across operations and no stale status after a supported task mutation.
- [ ] No process-global indefinite cache or extra worker concurrency is introduced; preserve four-second page tolerance and existing resource safeguards.

Profile Store stats and YAML parses, then test a request/tick-local immutable task snapshot that eliminates duplicate full scans while preserving external-edit and cross-process invalidation guarantees. Use matched 100- and 1,000-task before/after served and tick measurements.

## Provenance

Discovered by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T224859Z-revise`.
## Log
- 2026-09-07T23:43:23+00:00 discovered by CG-380
- 2026-09-08T02:29:15+00:00 approved (delegated-operator)
- 2026-09-09T17:20:27+00:00 dispatched work run 20260909T172026Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~17959 tokens)
- 2026-09-09T17:27:16+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T17:28:46+00:00 opened https://github.com/joshmarcus/context-garden/pull/393 (base main): Quiet scheduler ticks reuse their initial task discovery snapshot, while fingerprint detection refreshes it after in-pass writes or external edits. Focused scheduler, web/store tests and lint passed; bounded 100/1,000-task measurements showed reduced latency and scan work. cost=$0.80
- 2026-09-09T17:32:10+00:00 automated review requested changes: The snapshot change is focused and its scheduler regressions pass, but the required matched measurement report is incomplete. cost=$0.30
- 2026-09-09T17:33:02+00:00 dispatched revise run 20260909T173258Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~18901 tokens)
- 2026-09-09T17:38:46+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T17:41:05+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/393: Added a bounded, reproducible matched measurement report for 100- and 1,000-task fixtures. The replay records served scan counts and latency plus no-dispatch tick scan counts and latency; focused snapshot regressions and lint passed. cost=$0.75
- 2026-09-09T17:42:56+00:00 automated review: approve — The focused scheduler change correctly removes the redundant post-reap scan while preserving freshness across ticks and after in-pass task mutations. The revised matched report covers both required fixture sizes, scan counts, served latency, and no-dispatch tick time. cost=$0.37
- 2026-09-10T02:26:29+00:00 moved from context-garden/phase-05 to context-garden/phase-06
- 2026-09-10T02:27:17+00:00 triage: changes requested by hand: Code is reviewed but both CI runs 34384186594 and 34384180459 failed twice BEFORE tests because unrelated Google Chrome
- 2026-09-10T02:50:32+00:00 dispatched revise run 20260910T025028Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~16143 tokens)
- 2026-09-10T02:52:45+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T02:53:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/393: Added the established runner-specific CI workaround that removes the unrelated Google Chrome apt source before Playwright installs Chromium dependencies. Verified commit 922e89c826ec0a992b0f430cd24eb3c74f684b6d with focused scheduler/store tests (46 passed) and Ruff. cost=$0.21
- 2026-09-10T02:56:17+00:00 automated review: approve — The quiet-tick change removes the redundant post-reap task scan while retaining refresh behavior after external and supported in-tick mutations. The bounded report documents matched 100- and 1,000-task served and no-dispatch measurements. cost=$0.45
- 2026-09-10T03:09:38+00:00 triage: changes requested by hand: The apt setup correction succeeded: current CI now reaches tests. Preserve that correction and approved snapshot behavio
- 2026-09-10T03:17:55+00:00 difficulty medium -> hard after 2 substantive revisions; model gpt-5.6-terra -> gpt-5.6-sol
- 2026-09-10T03:17:58+00:00 dispatched revise run 20260910T031755Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16544 tokens)
- 2026-09-10T03:23:48+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T03:25:03+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/393: Fixed the Now partial fanout race by sharing snapshots through an explicit per-refresh identity instead of relying solely on scheduling within a 250 ms TTL. Verified final head 5d8a09b8 with 19 focused snapshot/store/web tests and Ruff; the existing Chrome apt-source correction remains intact. cost=$1.40
- 2026-09-10T03:25:10+00:00 PR conflicts with main; rebased onto main mechanically and force-pushed
- 2026-09-10T03:28:54+00:00 automated review: approve — The snapshot reuse and freshness behavior are correctly implemented and proportionately verified. cost=$0.40
- 2026-09-10T04:07:31+00:00 triage: changes requested by hand: Exact current-head CI runs 34433259053 and 34433255398 both reached the full suite and failed only tests/test_now1.py::t
- 2026-09-10T04:29:33+00:00 dispatched revise run 20260910T042930Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16839 tokens)
- 2026-09-10T04:31:48+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T04:33:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/393: Updated the stale Now stream regression to verify the shared refresh identity is passed through head and period refreshes. Committed as ea67fb0a; 10 focused tests passed and Ruff completed cleanly. cost=$0.59
- 2026-09-10T04:36:40+00:00 automated review: approve — The change reuses the quiet-tick snapshot while preserving refresh after supported mutations and external edits; explicit burst identities keep Now partial fanouts consistent. cost=$0.40
- 2026-09-10T04:59:57+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T05:02:29+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/393
