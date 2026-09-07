---
id: CG-380
title: Attribute controller, scheduler, and worker performance under load
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading: []
discovered_from: CG-367
created: '2026-09-07T12:03:08+00:00'
updated: '2026-09-07T12:29:53+00:00'
---

## Goal

Explain how much local resource use and page latency comes from the garden controller versus workers, then identify the next measured optimization. Preserve owner-approved four-slot operation and the existing caps.

## Context

Owner requested continued performance investigation on 2026-09-07 because worker versus application cost remains unclear. CG-367 is DONE and its Inbox history-read reduction is deployed in 899b2c0; extend its evidence rather than repeating or reopening its implementation. CG-365 resource isolation is also deployed. This task measures attribution, not another concurrency/configuration feature.

Operator evidence is preserved in context-garden/docs/incidents/performance-attribution-2026-09-07.json in the garden repository. Read-only summary for product-only workers: a 12-second no-operator-probe interval consumed 2.80 server CPU-seconds of 4.08 total service CPU-seconds, with a scheduler state save. Three serial page probes then consumed 1.77 server CPU-seconds of 2.08 total over 1.78 wall seconds; Now1/Inbox/Config returned 200 in .760/.678/.345 seconds. Service memory was 1341MiB, memory high/max/OOM zero, no memory pressure or CPU throttling delta. No-operator-probes does not mean idle: other clients may exist. These short observational intervals cannot establish tick cost or a general proportional split.

## Acceptance criteria

- [ ] On the current product build, reuse CG-367 fixtures/profiling and create a bounded disposable comparison with representative retained history: no workers, model-session/CI-wait activity, setup, and one focused validation workload. Compare one and four admitted slots where applicable. Do not launch extra model agents; replay or use bounded subprocess fixtures and label their representativeness. No production stress, pause, configuration changes, or full local suite.
- [ ] Attribute web request handling and scheduler phases separately: CPU execution, request/lock waiting, filesystem/history reads and parsing, process/resource inspection, and rendering as applicable. Measure worker setup/validation separately from controller work, including short-lived descendants. Record process identity and cgroup membership so parent CPU is not mistaken for total workload CPU. Do not equate summed RSS with actual aggregate memory.
- [ ] Retain exact build, dataset sizes, commands, caps, timestamps, sample counts, CPU seconds, cgroup throttling and CPU/I/O/memory pressure deltas, memory anon/file/shmem and temp headroom. Report empirical page p50/p95/max for repeated samples, cold/warm behavior, and background tick timing. Quantify instrumentation overhead. Label unsupported or unmeasured components honestly.
- [ ] Produce an evidence-backed attribution report separating confirmed bottlenecks from hypotheses and recommending the highest-value next action. If a narrow correction is demonstrated, implement it with a matched before/after comparison; otherwise file a precise follow-up instead of speculative caching or broad telemetry. Preserve data freshness and control correctness. Four-second page tolerance is the owner's operational target, not permission to fabricate passing evidence.
- [ ] Use focused serial bounded local validation and exact-final-head GitHub CI for code changes. Self-review and fix findings before completion; report ordinary acceptance evidence. Avoid unrelated application-wide walkthrough demands and do not claim incident closure or four-hour stabilization from this experiment.

## Boundaries

This is a new independent investigation. Do not regroup, rewrite, or widen in-flight task briefs. Reuse deployed work and its artifacts. Operator owns live monitoring and any eventual production changes.

## Additional operator observation: cache-heavy admission stop

At 2026-09-07T12:29Z, shared limit was five but only CG253 had a recorded running run. Scheduler resource_pressure reported available memory550MiB below1536MiB. Host MemAvailable was5621MiB, service memory.current about2501MiB, earlier breakdown anon251MiB/file2198MiB/shmem58MiB; memory high/max/OOM all zero and memory PSI zero. Now1/Inbox .715/.602s. The current sensor takes the minimum of host and cgroup headroom, so this is not host exhaustion. Inspect the cgroup admission calculation and reclaimable file-cache treatment as a concrete attribution hypothesis. Preserve hard memory caps and pressure safeguards; do not bypass the admission stop or assume all file cache is reclaimable. Report whether conservative soft-limit headroom is intentionally preventing progress and propose a measured safe policy if warranted.
