---
id: CG-361
title: Bound test workloads within each run and reserve web capacity
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading: []
branch: garden/cg-361-bound-test-workloads-within-each-run-and-reserve
pr: https://github.com/joshmarcus/context-garden/pull/244
attempts: 2
last_dispatched_at: '2026-09-07T00:50:37+00:00'
created: '2026-09-06T21:38:26+00:00'
updated: '2026-09-07T00:50:37+00:00'
---

## Goal

Keep local tests from exhausting the operator machine or starving the web/control service. Bound expensive test execution even when a single worker starts multiple suites, and reserve capacity for the control service independently of worker consumption.

## Context

Owner asked for the solution to repeated load/memory incidents on 2026-09-06. CG-338 merged at 6dd3ae49 and is installed with resources.max_parallel=1, min_memory_available_mb=1536 and min_temp_free_mb=1024. Its atomic shared admission counts run records across queues, and its subreaper owns descendants. Inspection confirms it does not limit the number or footprint of test suites launched inside a single run. The lock is scoped to this garden, not automatically every garden on a host. Host MemAvailable sensing also misses pressure against a lower service cgroup memory.high limit.

CG-294 previously left four simultaneous pytest processes. At recurrence, the garden shared a two-CPU quota and MemoryHigh=3GiB/MemoryMax=4GiB across web, scheduler, workers and tests. The serial full-suite A/B at c1f75cb measured tmpfs 163s/969MiB peak and ext4 222s/1523MiB peak, with much greater disk I/O stall. This is charged process/cache/kernel memory, not solely Python heap. Multiplication is a capacity warning, not proof of exact concurrent usage or the original OOM mechanism.

Evidence: context-garden/docs/incidents/test-temp-ab/README.md and the 2026-09-06 web incident/retro. Coordinate CG-338 shared run admission, CG-354 focused tests, CG-359 salvage, and CG-360 archive visibility. This task closes a missing enforcement boundary; it must not simply restate CG-338 or add a prompt and claim the problem solved.

## Acceptance criteria

- [ ] Provide a configurable heavy-test budget, initially one full suite at a time, shared by checks, base probes, worker/reviewer-issued validation and operator-supported launch paths. Tests from the same run cannot multiply resource consumption outside the configured execution budget. Queue or reject duplicate overlapping validation explicitly; do not consume branch failure/revision budgets for resource deferral. Document the enforcement boundary and any unsupported paths honestly.
- [ ] Isolate local execution from the web/control service with separately enforced CPU/memory budgets and a documented reserved-capacity profile. Descendants, including detached sessions and CLI launches, remain in the execution budget. Preserve ownership, stop/drain behavior and recovery artifacts. Sensing considers effective cgroup limits/pressure as well as host memory and temp headroom. Missing enforcement support must be visible rather than silently claiming isolation.
- [ ] Demonstrate repeated concurrent attempts from multiple launchers and from inside one worker cannot exceed the configured heavy-test budget. Include cancellation, launcher exit and stale reservation recovery; avoid nested-lock deadlocks when a check or worker already owns a run slot. Use focused deterministic coverage plus one bounded real workload, not repeated full-suite stress loops.
- [ ] On a representative retained-history fixture, perform actual Now/Inbox/control journeys while the allowed test workload runs and extra test requests wait. Record web latency, CPU/memory pressure, temp use and actual live descendants; keep pages and pause usable within the incident recovery latency target (under two seconds locally) without new memory.high thrashing or OOM. If the initial budget does not meet that target, reduce workload and report the evidence rather than raising caps.
- [ ] Explain effective limits and waiting reasons in relevant operator views and documentation. Instructions should require focused tests during iteration and sequential validation, with full CI retained as a merge gate; instructions supplement enforcement. Report acceptance evidence without claiming an unattended stabilization pass.

## Implementation safety

Keep validation serial and resource-bounded while implementing this fix. Do not run parallel full suites to prove the danger again, start uncapped services, raise production concurrency, modify the live host service, or change live temp storage from a worker. Supply deployment guidance for the operator; validate OS isolation against isolated test units/fixtures. Do not archive production history or bundle unrelated UI/history cleanups.

## Log

- 2026-09-06: Priority-0 incident prevention filed with owner authority after measuring test memory and inspecting the newly installed shared run guard. Implementation pending.
- 2026-09-06T21:39:49+00:00 approved (cli)
- 2026-09-06T21:40:23+00:00 dispatched work run 20260906T214006Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~9314 tokens)


## Operator validation intervention, 2026-09-06 22:08 UTC

The full-suite test process1962007 stalled in Git fixture setup after its direct git push child exited128. Orphaned fixture helpers1995748/1995749 kept stderr open; operator verified exact identities and fixture paths and terminated only those helpers, preserving files and evidence in operator-test-tmp/CG361-orphan-git-helpers.json. Pytest then reported425 passed and one fixture error after694.80s. This is partial validation with an operator intervention, not a full-suite pass. CG-354 now includes bounded fixture waits/descendant cleanup. Diagnose the original Git stderr/environment before treating this as a source defect or repeating the full suite.
- 2026-09-06T22:32:14+00:00 attempt 1 failed: worker idle 24 min (no output or file change); will retry
- 2026-09-06T22:44:19+00:00 Operator 22:45 UTC: run 20260906T214006Z-work timed out after idle 24m following preserved fixture-helper stall. Changes remain at df9b4e7 and dirty snapshot; no full pass. CG-363 implements owner-requested CI offload; keep this task ready until that workflow is installed, then use focused local checks plus exact-commit GitHub CI after incorporating current main. Do not rerun full suites locally or discard prior work.

## Operator continuation after CI offload

CG-363 is merged and installed at 58e13b99. Keep the existing resource-isolation implementation
and saved work; incorporate current origin/main (which contains the worker CI helper and
brief permission changes) before validation. The previous full suite stalled on orphan Git
fixture helpers and the model then idled out; it did not establish a full pass. Use focused,
bounded local regressions and the real resource-isolation fixture journey, then commit and
run `python3 scripts/check_ci.py` to validate the full suite on GitHub before finishing.
Do not run another full suite locally or modify the production service. Preserve unrelated
snapshot changes rather than adding them to the PR. Keep the workload/application evidence
honest: GitHub passing the suite alone does not establish local resource isolation.
- 2026-09-06T22:59:27+00:00 2026-09-06T22:59:27+00:00: CI offload deployed; eligible for one controlled recovery continuation under unchanged resource caps.
- 2026-09-06T23:03:31+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply fad1a65f4861637f96afc93356b4f503f1a4bc9f` in /home/joshua/work/worktrees/CG-361 to recover them (garden:CG-361:2026-09-06T23:03:31+00:00)
- 2026-09-06T23:03:33+00:00 dispatched work run 20260906T230331Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10560 tokens)
- 2026-09-06T23:15:58+00:00 opened https://github.com/joshmarcus/context-garden/pull/244 (base main): Local execution now shares a configurable per-user heavy-workload lease and an optional delegated cgroup, keeping descendants within an aggregate CPU/memory boundary while preserving explicit waiting, cancellation, recovery, and operator visibility. Setup commands, checks, probes, workers, reviewers, and supported CLI checks execute inside that boundary; exact-commit GitHub CI passed. cost=$1.56
- 2026-09-06T23:21:07+00:00 automated review requested changes: The lease mechanism is promising, but required workload and journey evidence is absent, isolation can be reported as enforced without any CPU or memory cap, and the focused regression suite fails in a finite-cgroup environment. The PR also includes a large unrelated generated snapshot rewrite. cost=$0.25
- 2026-09-06T23:25:03+00:00 dispatched revise run 20260906T232501Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~12174 tokens)
- 2026-09-06T23:49:00+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/244: Bounded local validation now uses shared execution leases and only reports cgroup isolation after finite CPU/memory controls and process migration are verified. Added real-workload concurrency and retained-history responsiveness evidence, restored the unrelated snapshot, captured every affected operator page, and passed exact-commit CI. cost=$3.28
- 2026-09-06T23:51:22+00:00 automated review requested changes: The cross-run lease and optional cgroup boundary are well documented and tested, but a worker holding one lease can still start multiple heavy suites concurrently. This misses the task’s central within-run enforcement and demonstration requirements. cost=$0.99


## Focused second-review continuation, 2026-09-06 23:55 UTC

The latest review verified the cross-run lease and cgroup work but found the central remaining defect: inherited leases bypass admission for concurrent nested heavy validations within one worker. Implement separate, enforceable admission for supported nested validation launches while preserving parent/child deadlock avoidance. Demonstrate two competing validations from one worker with at most one heavy suite active, using focused bounded workloads. Preserve existing passing behavior and address the actual enforcement gap; do not replace it with a prompt or a claimed guarantee for unsupported arbitrary commands. Keep unrelated snapshots in named recovery stashes and leave them out of the dirty worktree at completion; CG359 fixes the installed scheduler's salvage bug but is not yet deployed. Full suites stay on GitHub, no additional model agents or production service changes.
- 2026-09-06T23:55:31+00:00 dispatched revise run 20260906T235529Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~11882 tokens)
- 2026-09-07T00:07:54+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/244: Supported heavy validations launched within one worker now serialize through an owner-scoped lease while the parent retains its host-wide lease. Nested validations use the existing subreaper lifecycle so cancellation, detached descendants, and lock recovery remain bounded; exact-commit CI passed. cost=$1.38
- 2026-09-07T00:23:45+00:00 automated review requested changes: Within-run supported validations now serialize and focused tests pass, but the claimed per-user heavy-test budget can be exceeded when gardens use different configured limits. The shared host boundary therefore remains incomplete. cost=$1.15
- 2026-09-07T00:23:47+00:00 Latest revision finished atb398cee125859026ff6c7df443688ed9fd5f987a; exact-head branchCI34068412398 and PRCI34068414119 passed. Explicit owner-authorized next review started20260907T002007Z-review/PID2126137 after verifying reviewer slot and task had no active run. Fresh output/PID verified; do not redispatch the worker while review is active.


## Current continuation: preserve useful agent concurrency

Operator 2026-09-07 00:50 UTC: CG359 is now installed at fc658809, with current-main CI passed. Incorporate current main and address the actual latest review finding: gardens sharing one per-user heavy-validation semaphore need one authoritative capacity with visible conflict handling; add the limit-1/limit-2 shared-runtime regression. CG365 already records this issue; do not create another duplicate or leave the blocking guarantee deferred.

The owner's approved worker concurrency is FOUR while the heavy-validation budget is initially ONE. Code inspection found the existing outer supervisor holds the heavy lease for the entire model session, including thinking and remote CI waits (docs/codex.md describes only one local run executing at once). That would silently serialize useful agent work. Apply the heavy budget to supported expensive local setup/validation/check/probe execution, while allowing multiple model sessions and remote CI waits within the separate aggregate execution cgroup/run limits. Do not solve this by allowing concurrent unbounded local suites. Preserve honest unsupported-command boundaries, descendant ownership, cancellation, resource deferral semantics and nested-lock deadlock avoidance. Add focused evidence that two model sessions may proceed while two heavy validations contend and never exceed the authoritative budget.

Keep local checks serial/bounded, complete full tests on exact-head GitHub CI, preserve recovery artifacts, and do not change production service configuration or launch extra model agents. Existing passing evidence may be reused only for unchanged behavior; refresh affected concurrency and journey evidence.
- 2026-09-07T00:50:07+00:00 Operator continuation after verified CG359 deployment: repair authoritative host validation capacity and avoid holding a heavy-validation lease during the whole model/remote-CI session.
- 2026-09-07T00:50:37+00:00 dispatched revise run 20260907T005035Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~12639 tokens)
