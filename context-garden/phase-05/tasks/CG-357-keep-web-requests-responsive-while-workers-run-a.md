---
id: CG-357
title: Keep web requests responsive while workers run and run history grows
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading: []
created: '2026-09-06T17:45:27+00:00'
updated: '2026-09-06T17:48:30+00:00'
---

## Goal

Keep the real application responsive as durable run history grows, including while three workers share the configured CPU/memory limits. Separate live status and historical summaries from full archived logs so opening a page does not scan every past run repeatedly.

## Context

Owner reported the web application inaccessible after normal operation resumed on 2026-09-06 around 17:43 UTC. Requests to /now2 and / timed out from both WSL and Windows at 8–20 seconds, while /favicon.svg returned 200 in 0.02 seconds. The server remained alive. Initial VM available memory was about 6.5 GiB; subsequent worker activity increased service memory toward 3 GiB. Do not assume this is only network failure or fix by raising resource caps.

A py-spy dump of server PID 1440205 showed many concurrent web request threads repeatedly in RunStore.all_runs/runs_for/active, Scheduler.spent_for, build_inbox, Site.ctx and Now snapshot next_queues. Scheduler initialization for page reads also invokes fence migration/startup checks. Approximately 1,546 run records exist; history is durable and keeps growing. Now's phase budget calculation rereads all runs per phase, and page chrome repeats these calculations. Timed-out clients leave expensive synchronous work running, and browser partial requests pile up.

Owner explicitly requested a priority fix and asked about moving history to another location. Merely moving files is insufficient if every request still scans them. Introduce bounded live/status and historical aggregate access, plus safe archival of older terminal-run artifacts where appropriate. Keep historical details available on demand and preserve audit/recovery correctness.

An operator runtime experiment cached Run.load parsing by file stat fingerprint (bounded 2048 entries, deep-copy isolation). Mutation isolation, changed-file visibility and corrupt-file rejection passed, but a subsequent /now2 request still timed out at 20 seconds: this is not a verified fix. Do not treat this experiment as the durable solution. No run history was moved or deleted.

Related: CG-344 reduced duplicated fence manifests; state.json is now about 3.3 MiB, so its old 102 MiB size alone does not explain this incident. CG-338 owns resource admission. Retain the current worker/review limits and service resource caps when validating.

## Acceptance criteria

- [ ] Reproduce the live-history request amplification and identify dominant costs using measured request timings and scan/read counts.
- [ ] Now, Inbox and Board initial loads and updates stay responsive under representative history (at least current size and a substantially larger fixture) and concurrent workers within current caps. Target p95 under 2 seconds for ordinary reads; report actual measurements and limits.
- [ ] Ordinary page and status requests do not repeatedly materialize full run history per phase/task/widget. Shared summaries/indexes have explicit freshness and invalidation behavior; concurrent callers do not trigger an unbounded duplicate scan workload.
- [ ] Active-run transitions, task completion, cost corrections and new records appear promptly; read-only page construction does not repeatedly perform scheduler migrations or mutate recovery state.
- [ ] Old terminal-run logs/artifacts can be archived outside the active working set while preserving run identity, costs, links, review evidence and on-demand historical access. Specify the retention/selection policy and archive location clearly; do not move active, unreaped or recovery-referenced data.
- [ ] Archival is safe to retry after interruption, supports verification/recovery, and does not lose or double-count history. The ordinary UI does not scan the archive for every request. Missing archive data is reported honestly.
- [ ] Regression coverage verifies freshness, concurrent access, archival round trips and bounded work as history increases. Walk through the real app with representative data and record timings, not only screenshots or fixture success.
- [ ] Remove or supersede any temporary operator mitigation during safe installation; document deployment and verification without interrupting active work.

## Out of scope

- Deleting history, silently resetting cost totals, raising CPU/memory caps to hide unbounded work, or a general UI redesign.

## Log

- 2026-09-06T17:48:30+00:00 priority 0 -> 0
