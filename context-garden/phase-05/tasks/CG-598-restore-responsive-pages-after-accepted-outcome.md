---
id: CG-598
title: Restore responsive pages after accepted-outcome accounting
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-536
- CG-593
kind: bug
priority: 0
difficulty: hard
reading:
- src/garden/events.py
- src/garden/outcomes.py
- src/garden/web/common.py
- src/garden/web/pages/now1.py
- tests/test_costs.py
- tests/test_now1_design.py
branch: garden/cg-598-restore-responsive-pages-after-accepted-outcome
pr: https://github.com/joshmarcus/context-garden/pull/476
runner: remote
discovered_from: CG-537
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-10T19:49:46+00:00'
created: '2026-09-10T19:49:15+00:00'
updated: '2026-09-10T20:35:51+00:00'
---

## Goal

Restore responsive Now, Inbox and shared page rendering at the current installation scale while preserving the corrected accepted-task, priced/unpriced and operator-accounting contract.

## Observed regression

Published RC18 source7c3f88a83f828a69ae57e693b1fbfdfe1cd1d77e directly follows accepted main dc84676ee573fbceda33ddc7bf3e1a256e65bdb4. Full exact-head CI34516229153,66focused tests and RC16-client protocol passed, but the guarded live controller activation timed out on its first full-page probe. The controller was automatically rolled back with all source/results/config/caps verified; all six worker daemons remained RC16. Both root rollout pauses were resumed19:41:30. Do not deploy or hotpatch any runtime in this task.

An isolated read-only server running the exact RC18 package against current data, outside the deployment tick lock and bounded to one CPU, measured Now19.003s, a repeated Now18.248s, Inbox34.394s, and task API0.402s. This is persistent page work, not a startup-only miss, a network failure or proof of a lock deadlock. Source-specific receipts are retained by the root operator in rc18-deploy-20260910. The root owns repeat comparison against the real data after your repair.

Direct build_inbox profiling on the same source took2.753s with596 tasks and4899 run records; that alone does not explain the full page times. Shared Site.ctx invokes metrics over full history, and Inbox computes its own reporting too. Inspect events.metrics and outcomes.acceptance_cohort: repeated history sorting, timestamp parsing and per-task full-history scans across breakdown groups are a concrete candidate. Establish the dominant path rather than treating this hypothesis as a proved root cause.

## Acceptance criteria

- [ ] Reproduce the dominant scaling regression with a disposable realistic history/task population or a meaningful operation-count test. Preserve the reported live failure and identify the actual expensive path. Avoid private controller data, remote host fan-out, network calls or a fresh whole-system load exercise.
- [ ] Remove avoidable repeated history work, using an indexed/prepared view or another proportionate approach. Prefer reusing one calculation across a request and aggregation groups to stale cross-request caches. If caching is used, task phase/difficulty membership changes, event edits/appends, pricing updates and time/filter boundaries must invalidate correctly.
- [ ] Preserve exact accounting results: proven base acceptance only, stable chronological/tied-event behavior, half-open completion windows, all historical runs through acceptance, task/model/harness filters, first-review denominators, explicit known/unknown prices and attributed/unattributed operator coverage. Do not hide rows, sample history, treat unknown cost as zero or weaken correctness to improve latency.
- [ ] Prove output equivalence on representative edge cases and guard the eliminated multiplicative work without a fragile timing-only test. Verify affected page/metrics tests and actual exact-head CI; root will run the repaired source against the preserved real-scale comparison before release activation.
- [ ] Keep code portable across Linux, macOS and Windows through WSL, and report untested platforms. Do not change resource limits, review/merge policies, phase targets, live configuration, installed packages, published RC18 history or CG537's manual reservation.

## Delivery

Use the existing normal task branch and review/CI workflow. This is the canonical Phase05 blocking correction for the failed RC18 activation; do not duplicate it as generic performance cleanup. Root owns a fresh immutable release version and controller/all-six activation after accepted repair. Existing source, failures, receipts and staged RC18 runtimes remain preserved.

owner_request_key: rc18-rendering-regression-accepted-outcomes-20260910

## Log

- 2026-09-10T19:49:15+00:00 approved (delegated operator verified failed RC18 activation and real rendering regression)
- 2026-09-10T19:49:46+00:00 dispatched work run 20260910T194946Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15953 tokens)

## Confirmed operator profile, 2026-09-10T19:48Z

Actual cProfile of events.metrics over30,597 events and596 tasks identifies21 calls to outcomes.acceptance_cohort consuming62.135 of63.155 profiled CPU seconds (98.4%). The operation performed239,848,621 dictionary get calls and3,177,529 timestamp conversions. This confirms repeated cohort/history work as the dominant source, not build_inbox itself. Preserve the full aggregation contract while eliminating repeated per-task scans and repeated reconstruction across dimension filters. Root retains candidate-metrics-profile.pstats/.txt and will compare repaired output and actual pages against a fixed input snapshot. The profiled wall/CPU cost includes profiling overhead; unprofiled page measurements remain19/18/34seconds, not63seconds.
- 2026-09-10T20:13:11+00:00 worker blocked: Prepared and indexed acceptance history now replaces repeated timestamp parsing, sorting, per-task full-history scans, and per-breakdown cohort rebuilding. Focused accounting/page tests pass at commit 210f2e7c8cf50f2a3dc90bd74987356d218c6fae, but the exact-head full ordinary suite timed out at 88% after emitting one unidentified failure marker, so a clean merge-gate result remains outstanding. cost=$3.09
- 2026-09-10T20:29:50+00:00 triage: marked ready for review (Original worker210f2 source recovered unchanged. Exact CI34525481078 and34525487155 now BOTH SUCCESS)
- 2026-09-10T20:33:27+00:00 automated review: approve — The change removes the dominant multiplicative accepted-outcome work without introducing cross-request caching or weakening accounting correctness. cost=$0.63
- 2026-09-10T20:35:51+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/476
