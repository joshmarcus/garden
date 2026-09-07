---
id: CG-347
title: Recover EC2 Spot interruptions without losing accepted work or exceeding pool limits
status: ready
product: context-garden
phase: phase-05
depends_on:
- CG-216
- CG-346
priority: 2
order: 6
difficulty: hard
reading:
- context-garden/phase-06/specs/ec2-workers.md
created: '2026-09-06T16:27:50+00:00'
updated: '2026-09-07T12:47:31+00:00'
---

## Goal and evidence

Add Spot purchase policy and replacement on top of managed EC2 execution. Handle interruption notices and abrupt loss without notice, preserve recoverable work/transcripts, fence stale attempts and respect the configured capacity and spend envelope. On-demand fallback is opt-in and priced explicitly.

Exercise interruption during work, checks and result upload; stale-worker return after reassignment; no available Spot capacity; and repeated controller reconciliation. Prove no duplicate result acceptance or merge, no canonical branch overwrite by stale workers, bounded retries, and separate retry/model-cost accounting. Use a live canary in addition to deterministic simulations; do not claim an exactly-once execution guarantee.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Owner explicitly brought this work into phase 05 on 2026-09-07. Implementation is authorized now under ordinary admission; live provisioning follows the spec’s bounded resource/cost plan.

## Pluggability requirement (owner clarification)

Expose generic interruption/drain/replacement events from the EC2 provider, with task checkpoint/retry behavior implemented by the garden consumer. Capability-check Spot requests. Remote-dev profiles default to on-demand and persistent storage; never apply disposable-worker destruction or replacement policies to a person's development workspace. A dev profile may opt into Spot only with an explicit recoverable-workspace policy.

## Log

- 2026-09-07T12:47:31+00:00 moved from context-garden/phase-06 to context-garden/phase-05

## Owner scope update, 2026-09-07

Remote AWS workers are now phase-05 work, without waiting for local stabilization failure. Preserve existing PRs, branches, evidence and dependency order. The reusable host lifecycle must still support non-garden remote development hosts. This supersedes earlier feature-deferral notes; it does not approve an old PR verdict or waive validation.
- 2026-09-07T12:47:31+00:00 approved (owner-phase05-promotion)
