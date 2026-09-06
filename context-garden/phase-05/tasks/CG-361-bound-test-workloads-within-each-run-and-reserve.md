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
attempts: 1
last_dispatched_at: '2026-09-06T21:40:23+00:00'
created: '2026-09-06T21:38:26+00:00'
updated: '2026-09-06T21:40:23+00:00'
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
