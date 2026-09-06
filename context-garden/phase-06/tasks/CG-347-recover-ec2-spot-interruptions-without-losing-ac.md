---
id: CG-347
title: Recover EC2 Spot interruptions without losing accepted work or exceeding pool limits
status: draft
product: context-garden
phase: phase-06
depends_on:
- CG-216
- CG-346
priority: 2
difficulty: hard
reading:
- context-garden/phase-06/specs/ec2-workers.md
created: '2026-09-06T16:27:50+00:00'
updated: '2026-09-06T16:27:50+00:00'
---

## Goal and evidence

Add Spot purchase policy and replacement on top of managed EC2 execution. Handle interruption notices and abrupt loss without notice, preserve recoverable work/transcripts, fence stale attempts and respect the configured capacity and spend envelope. On-demand fallback is opt-in and priced explicitly.

Exercise interruption during work, checks and result upload; stale-worker return after reassignment; no available Spot capacity; and repeated controller reconciliation. Prove no duplicate result acceptance or merge, no canonical branch overwrite by stale workers, bounded retries, and separate retry/model-cost accounting. Use a live canary in addition to deterministic simulations; do not claim an exactly-once execution guarantee.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Draft in frozen phase 06; do not approve, dispatch or provision cloud resources until the stabilization gate passes or Josh grants an explicit exception.
