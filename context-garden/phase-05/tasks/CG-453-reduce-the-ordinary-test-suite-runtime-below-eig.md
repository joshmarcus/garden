---
id: CG-453
title: Reduce the ordinary test suite runtime below eight minutes
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- scripts/check_ci.py
- pyproject.toml
- .github/workflows/ci.yml
- docs/test-suites.md
- tests/conftest.py
- tests/test_runners.py
branch: garden/cg-453-reduce-the-ordinary-test-suite-runtime-below-eig
pr: https://github.com/joshmarcus/context-garden/pull/353
runner: remote
attempts: 2
last_dispatched_at: '2026-09-08T23:01:15+00:00'
created: '2026-09-08T20:10:38+00:00'
updated: '2026-09-09T01:11:32+00:00'
---

## Goal

Reduce the context-garden ordinary test suite to a representative runtime below eight minutes while preserving its intended coverage, deterministic failures, and the separate opt-in policy for stress/load experiments.

## Context

The owner explicitly requested this priority-0 task on 2026-09-08 after repeated ordinary-suite runs approached or exceeded the useful feedback window. CG-354 organized focused suites and repaired one fixture descendant leak, and CG-446 bounds individual tests and validation sessions; reuse those foundations without reopening their completed scope. Start from existing CI logs and profiles rather than guessing. The task owns measured runtime reduction in ordinary pytest/CI through targeted fixture reuse, safe caching, and bounded dependency/process setup.

Use one fixed representative Linux/Python environment and exact source for comparisons. Define **cold** as the first ordinary pytest run in a prepared dependency environment with pytest caches and test-created temporary state empty; define **warm** as an immediate second run at the same source and caps with dependencies unchanged. Measure dependency/browser installation separately and exclude it from the under-eight-minute pytest threshold, while still reporting it so CI setup regressions remain visible. Run measurements serially under the configured worker/resource bounds; parallel suites must not masquerade as a speedup.

## Acceptance criteria

- [ ] Profile the current ordinary suite before changing it, starting with the longest nodes and fixture/setup spans visible in existing CI logs. Save exact source, commands, collected/deselected counts, wall time, slowest-node timings, environment/caps, and cold/warm definitions. Distinguish useful test execution from dependency installation, admission waiting, and a stuck process.
- [ ] Reduce both representative cold and warm ordinary pytest runs to less than 480 seconds. Target measured bottlenecks with fixture lifecycle changes, safe cache reuse/invalidation, bounded subprocess/dependency setup, or similarly scoped improvements; explain each material saving with before/after evidence.
- [ ] Preserve the intended ordinary test collection and assertions. Keep stress/load experiments explicitly opt-in under the existing policy; do not reach the target with blanket skips, broad deselection, hidden xfails, reduced assertions, false-pass fallbacks, or by dropping platform/application coverage. Account for any intentional node-count change by name and rationale.
- [ ] Keep caches and shared fixtures isolated, bounded, and invalidated by every input that affects their result. A failed or interrupted setup must not poison later runs, hold pipes/locks, leak descendants, reuse another source revision, or let concurrent tests share mutable state unsafely.
- [ ] Run the final exact-head ordinary suite through the repository CI command and show it passes within the threshold in the representative environment. Also run focused regressions for every changed fixture/cache/process boundary and keep final GitHub CI as the merge gate. Report cold and warm results honestly; do not claim the threshold from a targeted subset.
- [ ] Update the focused-suite guidance and CI diagnostics so future workers can reproduce the fixed environment, find the current longest nodes, and tell a real performance regression from admission time or infrastructure failure.

## Scheduling

Owner-approved priority 0. Use the remote runner under existing global/host/resource limits. Global dispatch may be paused for separate AWS preservation work; approval does not authorize bypassing that pause, launching hosts, raising concurrency, or running uncapped local profiling. Preserve the configured 120-second per-test and 900-second validation limits.

## Log

- 2026-09-08T20:10:39+00:00 approved (owner)
- 2026-09-08T20:41:04+00:00 dispatched work run 20260908T204104Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~22180 tokens)
- 2026-09-08T22:16:34+00:00 attempt 1 failed: worker timed out; will retry
- 2026-09-08T22:16:55+00:00 dispatched work run 20260908T221655Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~22236 tokens)
- 2026-09-08T22:31:45+00:00 Operator preserved both AWS worktrees, restored actual execution age from claimed_at, and cancelled the new duplicate. No functional failure or approval was invented.
- 2026-09-08T22:32:14+00:00 fenced: Cannot verify this run's worktree fence; inspect protected paths before retrying. Restoration is unverified: fence manifest unavailable or invalid: trusted manifest reference missing or belongs to another run


## Operator continuation from preserved partial source 2026-09-08T22:59:04.407144+00:00

Continue the preserved implementation at ef1d0e7ed93b6d91f52be9ac3add863f961d75d2 on this task branch. Do not restart from main or repeat the discarded duplicate. The previous original worker returned an honest blocked partial result: the cold ordinary suite was580.66seconds, warm is unproven, and an upgrade integration test failed with an old-pip local-git requirement. Existing profiling and fixture isolation changes are useful; inspect docs/validation/cg453/report.md and retained durations before targeted next changes. The host runtime was subsequently prepared with Python3.12.14 and modernpip25 at /opt/garden-test-python/bin; verify the actual interpreter/pip chosen by nested fixtures and compare the reported failure against base before altering product behavior. Fix measured remaining bottlenecks, preserve coverage, and run final cold/warm serial suites under480seconds each. A prior controller queue-age timeout launched a duplicate while the original was still live. The operator preserved both source bundles, cancelled only the duplicate, and preserved original usage/result. The original run's final fence rejection is retained because the per-task trusted reference was lost; it is not an author-code verdict or an accepted review. This new revision receives fresh ordinary guards and must independently validate the preserved code. No failed criterion has been waived.
- 2026-09-08T22:59:32+00:00 Preserved exact partial source after controller duplicate/fence bookkeeping failure; continue measured optimization with unmet criteria retained
- 2026-09-08T22:59:32+00:00 re-enabled by hand; revise run will follow
- 2026-09-08T23:01:15+00:00 dispatched revise run 20260908T230115Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23215 tokens)
- 2026-09-09T00:28:55+00:00 opened https://github.com/joshmarcus/context-garden/pull/353 (base main): Reduced the serial ordinary suite below eight minutes by caching and indexing walkthrough CSS selector parsing, reusing isolated Git fixture seeds, and tightening process-boundary fixtures. Final exact-head validation passed in 451.50 seconds at 464a47fad51c2ec9f4db4c5d64e28fe68276cef6. cost=$7.93
- 2026-09-09T00:32:46+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/353
- 2026-09-09T01:11:32+00:00 automated review could not start: CG-453 is done: #353 was merged at 00:32:46
