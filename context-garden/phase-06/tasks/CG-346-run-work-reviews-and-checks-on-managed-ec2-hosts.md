---
id: CG-346
title: Run work reviews and checks on managed EC2 hosts with shared resource admission
status: draft
product: context-garden
phase: phase-06
depends_on:
- CG-216
- CG-338
- CG-345
priority: 2
difficulty: hard
reading:
- context-garden/phase-06/specs/ec2-workers.md
created: '2026-09-06T16:27:50+00:00'
updated: '2026-09-06T16:27:50+00:00'
---

## Goal and evidence

Integrate the managed pool lifecycle with the portable worker protocol, using the lifecycle task as a dependency. All execution modes, including setup and base probes, share measured host admission; use disk-backed temp by default and preserve a memory reserve. Deliver durable transcripts, changes and results without scheduler filesystem assumptions.

Evidence should complete a work/review/check cycle on an independent host, demonstrate that a one-slot pool does not start overlapping unchecked suites, and recover artifacts after instance loss. Show actual host/version/resource attribution and no exposed controller credentials.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Draft in frozen phase 06; do not approve, dispatch or provision cloud resources until the stabilization gate passes or Josh grants an explicit exception.

## Pluggability requirement (owner clarification)

Garden is a consumer adapter of the shared host lifecycle. Keep task admission, CG-216 enrollment and results within that adapter; generic provisioning must function without garden scheduling or model credentials. Implement the garden-worker environment profile through the documented profile contract. Do not hard-code worker-only semantics into EC2 host lifecycle or credentials.
