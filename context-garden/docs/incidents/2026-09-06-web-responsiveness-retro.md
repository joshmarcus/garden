# Web responsiveness retrospective — 2026-09-06

Service recovery verified at19:13 UTC after three successful checks spanning13 minutes, including one real revision/check workload. Normal admission resumed then; persistent resource caps and phase06 holds remain. This is a supervised incident recovery, not phase05's unattended stabilization/adoption gate.

## Impact and timeline

- Around17:43 the owner could not use dynamic pages; requests from Windows and WSL exceeded8–20 seconds. Static assets remained fast. Effective worker limit had just increased to3, sharing a2-CPU cap with the server.
- Stack samples showed many simultaneous request threads repeatedly scanning roughly1550 run records through phase costs, Inbox/Now rendering and scheduler construction. A read-parser cache experiment did not restore service.
- 17:51–17:59: ordinary admission paused, CG-294 preempted with work preserved; four escaped tests stopped. Recovery dispatch itself was slow. Owner-authorized restart preserved two workers but interrupted CG-357 preparation, requiring exactly-once recovery of that startup. Full pages remained slow after restart.
- CG-357 implemented shared/incremental indexes and non-mutating page readers. Review caught archive correctness gaps and insufficient performance evidence. Scheduler salvage repeatedly added an unrelated runtime snapshot despite worker exclusions; operator preserved and removed it.
- 18:54 operator served-app tests with three executing local CPU/metadata workers under shared caps passed: p95 .213s at1546 history and .570s at6000, sixty HTTP samples each. Windows browser followed live Now updates, run details, Board and Inbox. These were controlled workloads, not three production model sessions.
- 18:59 PR234 merged after current-head CI; deployed8842552 at a drained boundary. At19:00 production pages and Windows navigation worked. One controlled CG-329 revision/check ran during observation.
- 19:07 and19:13: Inbox, Board and both Now pages returned200, around .46–.69 seconds from WSL. Windows IPv4 Now2 measured .754/.645s. No memory.high/max/OOM events or swap after the recovery restart. At19:13 normal admission resumed.

Approximate dynamic-service disruption:17:43–19:00,77 minutes; recovery observation extended to19:13. No evidence establishes data loss or an OOM kill. These times describe observed availability, not continuous instrumentation.

## Cause and contributing conditions

Confirmed mechanism: application reads repeatedly parsed/materialized durable history; concurrent page requests amplified this work. The repaired read architecture and measured before/after outcome support that diagnosis. History growth was a normal operating condition, not data that should have been deleted.

Contributors: UI and worker/test work shared a2-CPU budget; overlapping escaped suites added contention. The incident accumulated memory.high throttling and swap, but began with substantial VM memory headroom. Neither the worker-limit increase nor memory exhaustion alone explains it; do not claim a proven final OOM cause. The earlier102MiB state issue had already been reduced and did not by itself explain this outage.

Windows PowerShell localhost checks initially added roughly2 seconds beyond WSL/explicitIPv4; address-selection/client overhead is an inference, not fully isolated. Actual browser navigation and IPv4 timings establish recovery without treating that overhead as the original timeout.

## Why prevention and recovery failed

Functional tests and screenshot-oriented review did not demonstrate interactive responsiveness with accumulated history and concurrent executing work. Inert run records represented occupancy but not resource contention. Tiny samples and extrapolated percentiles overstated evidence. A stale review base also generated an incorrect unrelated-commit finding; the real unrelated snapshot diff was separately valid.

Recovery priority existed in the queue before it had a real slot. The control action shared an overloaded request path; client timeout concealed continuing server work. Restart alone could not fix the read algorithm and interrupted startup. Operator time went into monitoring ambiguous states, trying an ineffective cache and repeatedly cleaning snapshots. The incident protocol now makes containment, real recovery capacity, deliberate restarts and measured exit explicit; documentation is not automatic enforcement.

Including archival in the emergency implementation introduced extra correctness surface and review cycles. It is useful requested work, but future recovery should separate longer-term expansion when it delays the smallest safe restoration.

## Prevention work filed or strengthened

| Task | Concrete prevention | Counterfactual |
|---|---|---|
| CG-357, merged | Incremental/coalesced history reads; honest archive behavior | Avoids the measured per-request history amplification. |
| CG-358, new priority0 | Responsive recovery controls, durable operation IDs and retry-safe startup | A timed-out page would not also block or duplicate urgent recovery. |
| CG-359, new priority1 | Preserve unrelated dirty artifacts without committing them into recovered PRs | Prevents repeated snapshot pollution and wasted review/cleanup cycles. |
| CG-338, expanded | Account for detached descendants and overlapping test suites; verify stop/drain | Bounds contention and releases capacity when a worker is preempted. |
| CG-339, expanded | Served performance evidence at realistic scale/load, empirical distributions and refreshed review base | Exposes application-level regression before rollout and prevents overclaimed verification. |
| CG-331, clarified | Keep lock-order regression separate from real availability performance | Does not dismiss true latency failures as merely slow test machinery. |
| CG-333, linked | Coordinate committed-work salvage with CG-359 provenance | Recovery preserves useful work without indiscriminate dirty-file commits. |
| CG-355, existing | Verified deployment, served version and safe update lifecycle | Reduces stale installed builds and manual deployment ambiguity; updater root cause remains unproven. |
| CG-354, existing owner draft | Focused test suites with full final CI | Reduces repeated expensive suites during iteration; not substituted for resource admission. |

New tasks carry measurable acceptance criteria and provenance. Existing tasks were extended instead of duplicated. No claim is made that their prevention is implemented merely because tasks exist. The full four-hour stabilization, representative completion count and named external adoption remain unproven.

## Follow-through

Continue capped normal operation and monitor recurrence. Resume CG-294 from its preserved worktree/transcript and patch; do not erase it. Keep production history intact. Verify prevention tasks using disposable fault/scale workloads and actual application outcomes, preserve evidence on the tested head, and record any recurrence as a new incident or reopening of this one.
