---
id: CG-346
title: Run work reviews and checks on managed EC2 hosts with shared resource admission
status: ready
product: context-garden
phase: phase-05
depends_on:
- CG-216
- CG-338
- CG-345
priority: 2
order: 5
difficulty: hard
reading:
- context-garden/phase-06/specs/ec2-workers.md
created: '2026-09-06T16:27:50+00:00'
updated: '2026-09-07T12:47:31+00:00'
---

## Goal and evidence

Integrate the managed pool lifecycle with the portable worker protocol, using the lifecycle task as a dependency. All execution modes, including setup and base probes, share measured host admission; use disk-backed temp by default and preserve a memory reserve. Deliver durable transcripts, changes and results without scheduler filesystem assumptions.

Evidence should complete a work/review/check cycle on an independent host, demonstrate that a one-slot pool does not start overlapping unchecked suites, and recover artifacts after instance loss. Show actual host/version/resource attribution and no exposed controller credentials.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Owner explicitly brought this work into phase 05 on 2026-09-07. Implementation is authorized now under ordinary admission; live provisioning follows the spec’s bounded resource/cost plan.

## Pluggability requirement (owner clarification)

Garden is a consumer adapter of the shared host lifecycle. Keep task admission, CG-216 enrollment and results within that adapter; generic provisioning must function without garden scheduling or model credentials. Implement the garden-worker environment profile through the documented profile contract. Do not hard-code worker-only semantics into EC2 host lifecycle or credentials.

## Log

- 2026-09-07T12:47:31+00:00 moved from context-garden/phase-06 to context-garden/phase-05

## Owner scope update, 2026-09-07

Remote AWS workers are now phase-05 work, without waiting for local stabilization failure. Preserve existing PRs, branches, evidence and dependency order. The reusable host lifecycle must still support non-garden remote development hosts. This supersedes earlier feature-deferral notes; it does not approve an old PR verdict or waive validation.
- 2026-09-07T12:47:31+00:00 approved (owner-phase05-promotion)
