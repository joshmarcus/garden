---
id: CG-418
title: Measure safe reclaimable-cache treatment for admission
status: cancelled
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: CG-380
created: '2026-09-07T23:43:24+00:00'
updated: '2026-09-08T02:29:15+00:00'
file: src/garden/scheduler/resources.py
error: The current conservative sensor can stop admission when cgroup file cache consumes soft-limit headroom
  even though host memory and pressure counters are healthy; existing observations do not establish how
  much cache is safely reclaimable.
---

Under the existing hard cgroup cap, populate disposable file cache, record inactive-file working set and PSI/events, issue bounded memory.reclaim, and measure reclaimed bytes plus a one-slot launch high-water mark. Only then consider a guarded reclaimable-cache allowance while preserving the hard cap, OOM/pressure safeguards, 1,536 MiB reserve, and four-slot limit.

## Provenance

Discovered by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T224859Z-revise`.
## Log
- 2026-09-07T23:43:24+00:00 discovered by CG-380
- 2026-09-08T02:29:15+00:00 Delegated operator: stale admission-policy proposal overlaps CG383/CG385 and conflicts with owner disabling memory-headroom admission (min_memory_available_mb=0). Preserve CG380 measurements; do not reintroduce a 1536 MiB reserve or production reclaim controller.
