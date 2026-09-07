---
id: CG-386
title: Prevent stale collected checks from reopening terminal tasks
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/scheduler/checkruns.py
- src/garden/scheduler/human.py
- src/garden/scheduler/poll.py
- src/garden/scheduler/reap.py
- tests/scheduler/test_human.py
created: '2026-09-07T15:29:52+00:00'
updated: '2026-09-07T15:31:25+00:00'
---

## Goal

A completed or cancelled task stays terminal when an old detached check is collected or its continuation is retried. Parked empty checks do not emit the same owner stop every tick.

## Incident evidence

After verified PR284 merge40373fe99397c5d86f888bafa8dd99e333690db4 and deployment of0.2.0rc1, CG377 was repeatedly changed from done to in_review by already-collected base_probe run20260907T141044Z-check (specs=[], no check results). The loop repeated the needs-human transition from15:16 through15:30. _collect_check_run retains collected continuations for admission recovery; _retry_or_park_check parks the failure but leaves that continuation replayable. Terminal transition clears needs_human/feedback, but not this obsolete check continuation.

Operator verified GitHub merge, preserved full state at /home/joshua/work/operator-test-tmp/cg377-stale-check-20260907T1530.json, marked done through Scheduler.mark_done and retired only the stale continuation through the locked State API. Original run/result/cost/feedback history remains. This is state recovery, not an automated approval or a rerun. CG142 and CG198 are related completed protections; this is a newly observed uncovered path. Copy the synthetic lifecycle facts into a disposable regression; workers must not read or mutate the live garden.

## Acceptance criteria

- [ ] Terminal transitions or check collection retire obsolete continuations so done/cancelled/wont_do tasks cannot return to an active status or emit new owner demands from an older check. Preserve run evidence and costs; verify actual active children before retiring runtime work.
- [ ] Parking a collected check with no results or no retryable specs is idempotent: one explicit actionable stop while the task is active, without repeated logs/events each tick. Missing checks are not fabricated as passed.
- [ ] Preserve legitimate durable continuation behavior for nonterminal tasks after restart or resource admission deferral. A completion that awaits a new check still resumes once, without duplicate dispatch or lost results.
- [ ] Focused lifecycle regressions reproduce the CG377 merged-task case, cancellation, repeated empty-check parking and a restart/resource-deferred valid continuation through multiple ticks. Exact-head CI and self-review precede normal automated review; no broad unrelated validation demands.

## Prevention

This guard would have kept the verified merged/deployed task done and avoided a misleading owner card and repeated operator repair. CG362 covers external claim/reconciliation defects; do not expand an active worker's scope to absorb this independent check lifecycle fix.
