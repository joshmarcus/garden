---
id: CG-479
title: Optimize Garden page load times
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: hard
reading:
- src/garden/web/app.py
- src/garden/web/common.py
- src/garden/web/pages/now1.py
- src/garden/web/pages/inbox.py
- src/garden/store.py
branch: garden/cg-479-optimize-garden-page-load-times
pr: https://github.com/joshmarcus/context-garden/pull/382
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T15:41:03+00:00'
created: '2026-09-09T12:57:17+00:00'
updated: '2026-09-09T16:01:47+00:00'
---

## Goal

Measure and improve Garden page load times so navigation and common operator workflows feel responsive, including when the task, run and event history is large or workers are active.

## Owner request

Add a phase05 task to optimize page load times.

## Acceptance criteria

- [ ] Establish reproducible before/after timings for representative Now, Inbox, board, task detail, run detail and Config loads. Separate server response time from browser rendering and distinguish cold/warm loads and local/public access where relevant. Use actual measurements to choose priorities rather than assume the bottleneck.
- [ ] Profile the slow paths and implement focused improvements to the largest measured costs, including repeated state/file scans, expensive per-item computation, blocking external calls or unnecessarily large rendered payloads when evidence identifies them. Record which costs were reduced and remaining bottlenecks.
- [ ] Preserve accurate current task/check/review status, configuration behavior, navigation and live updates. Any caching must have appropriate invalidation and concurrency handling; do not make pages appear fast by silently serving stale operational state or hiding failures.
- [ ] Verify improvements with comparable before/after measurements using a representative large-history fixture and normal active-worker conditions where practical. Keep performance checks bounded and separate optional stress testing from the ordinary suite. Add only targeted regression coverage warranted by the actual change.

## Scope

Optimize existing page/data paths and reuse current streaming/lazy-loading mechanisms. This is not a visual redesign or a new dashboard. Preserve existing worker/resource limits and avoid interrupting production work for benchmarks. Report concrete measured changes; do not claim a speedup without comparable results.

## Log

- 2026-09-09T12:57:17+00:00 approved (owner-requested phase05 page-load optimization, guided by measured bottlenecks)
- 2026-09-09T13:49:16+00:00 dispatched work run 20260909T134916Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22603 tokens)
- 2026-09-09T14:49:07+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T14:54:36+00:00 opened https://github.com/joshmarcus/context-garden/pull/382 (base main): Profiled representative large-history page loads and removed repeated cross-request YAML parsing with an isolated, metadata-invalidated discovery snapshot. Comparable localhost server/browser measurements show substantially lower response times across Now, Inbox, board, task detail, run detail, and Config; 155 focused tests and Ruff pass at the final source. cost=$2.83
- 2026-09-09T15:12:12+00:00 automated review requested changes: The cache materially improves measured warm loads, but its scan/fingerprint race can indefinitely serve stale task state, and the required cold/warm comparison is incomplete. cost=$0.28
- 2026-09-09T15:13:42+00:00 dispatched revise run 20260909T151342Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23851 tokens)
- 2026-09-09T15:39:02+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:40:41+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/382: Made cached discovery race-safe and replaced ambiguous timing evidence with reproducible cold/warm server and browser measurements. On the 600-task, 1,200-run, 5,000-event active-worker fixture, warm server medians improved 46–78% across all six routes; 117 focused tests and Ruff pass at commit 728a02e2b4fc13fa7542a63a976be893db362fe7. cost=$2.20
- 2026-09-09T15:40:58+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_web.py); a rebase agent will resolve it
- 2026-09-09T15:41:03+00:00 dispatched rebase run 20260909T154102Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1542 tokens)
- 2026-09-09T15:46:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/382: Resolved the tests/test_web.py rebase conflict by preserving both test additions; rebase completed successfully and focused tests passed. cost=$0.01
- 2026-09-09T15:50:25+00:00 automated review: approve — The race-safe discovery snapshot materially improves warm page loads while preserving request isolation and filesystem-driven freshness. cost=$0.35
- 2026-09-09T15:58:55+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T16:01:47+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/382
