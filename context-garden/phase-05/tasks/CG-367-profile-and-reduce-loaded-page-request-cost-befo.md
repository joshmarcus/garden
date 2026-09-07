---
id: CG-367
title: Profile and reduce loaded page request cost before increasing concurrency
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading: []
created: '2026-09-07T03:58:50+00:00'
updated: '2026-09-07T03:59:41+00:00'
---

## Goal

Measure where loaded Now/Inbox requests spend time, then remove the largest demonstrated avoidable cost so useful work can run concurrently within the existing resource caps.

## Evidence and scope

Repeated five-slot trials produced 2.5–3.1s pages while memory PSI/high/max/OOM remained zero. One-slot observations were about0.6–1.1s. This correlation does not establish CPU, I/O, memory, locks, template work or history scanning as the cause. Owner now accepts up to4s and requests4slots; do not optimize by silently tightening policy or increasing caps. Installed narrow5cff609 includes history-index and fence repairs; profile current code, not an obsolete missing-index implementation. CG358 owns control-plane recovery, CG365 execution isolation, CG339 evidence policy, CG364 test cost. This task owns measured request-cost reduction.

## Acceptance criteria

- [ ] Reproduce in a disposable served garden with representative current and larger histories, cold/warm/cache-expiry periods, and bounded executing workloads at1 and4slots. Record exact code, dataset sizes, commands and caps. No stress/fault injection against production.
- [ ] Attribute elapsed request time using request-level spans or profiling: request queue/lock wait, task/run/history reads and parses, resource/process observation and template work as applicable. Retain CPU time, cgroup CPU throttling and CPU/I/O/memory PSI deltas alongside observed latency. Separate diagnosis from hypotheses; avoid broad permanent telemetry or logging secrets.
- [ ] Fix the largest evidenced avoidable request cost with a minimal change. Preserve freshness/invalidation, task/control truth and cross-process updates; no stale cache as an apparent speedup. If no avoidable code bottleneck is established, publish evidence and concrete next action instead of inventing a cache.
- [ ] Serial before/after comparison on the same limits/data reports empirical p50/p95/max, sample count, process CPU, peak memory/temp and relevant read counts. Include the owner4s tolerance but do not assert a fabricated universal speedup. Add targeted regression for the diagnosed mechanism; keep real performance probes separate from deterministic correctness tests.
- [ ] Focused local tests only, serial/capped; exact-final-head GitHub CI. Self-review and fix findings before completion. No production configuration/process edits.

## Log
- 2026-09-07T03:59:41+00:00 Owner-requested optimization prioritization: phase05 stabilization improvement, priority1; preserve phase06 feature freeze and current4slot/4second policy.
