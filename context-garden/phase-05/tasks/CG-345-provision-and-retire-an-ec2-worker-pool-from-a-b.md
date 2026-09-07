---
id: CG-345
title: Provision and retire an EC2 worker pool from a bounded declarative configuration
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
order: 3
difficulty: hard
reading:
- context-garden/phase-06/specs/ec2-workers.md
created: '2026-09-06T16:27:49+00:00'
updated: '2026-09-07T12:47:31+00:00'
---

## Goal and evidence

Implement the on-demand lifecycle and bootstrap portion of specs/ec2-workers.md. Provide a plan/enable boundary, idempotent reconciliation with ownership tags, scoped credential delivery, reachable HTTPS enrollment, pinned versions and explicit failure states. Default to zero idle instances and a one-instance maximum.

Evidence should cover duplicate provisioning requests, delayed AWS responses, controller restart, bootstrap failure and cleanup without touching unrelated resources. A separately enabled bounded AWS canary must register a real worker and retire it with an inventory of any retained billed resources. Fake-provider tests alone do not establish live readiness.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Owner explicitly brought this work into phase 05 on 2026-09-07. Implementation is authorized now under ordinary admission; live provisioning follows the spec’s bounded resource/cost plan.

## Pluggability requirement (owner clarification)

Implement an independently usable host lifecycle with versioned provider and environment-profile contracts. EC2 is an adapter, not the core data model. Expose plan/provision/reconcile/inspect/stop/start/destroy capabilities and lifecycle events without garden task IDs or scheduler imports. Support injected workplace policy/credential resolution and validated namespaced provider options. Supply a fake provider and a minimal extension example proving a second provider can be added without modifying core or garden scheduling. The same lifecycle must support both disposable worker hosts and persistent development hosts; do not assume every termination deletes workspace storage.

## Log

- 2026-09-07T12:47:30+00:00 moved from context-garden/phase-06 to context-garden/phase-05

## Owner scope update, 2026-09-07

Remote AWS workers are now phase-05 work, without waiting for local stabilization failure. Preserve existing PRs, branches, evidence and dependency order. The reusable host lifecycle must still support non-garden remote development hosts. This supersedes earlier feature-deferral notes; it does not approve an old PR verdict or waive validation.
- 2026-09-07T12:47:31+00:00 approved (owner-phase05-promotion)
