---
id: CG-345
title: Provision and retire an EC2 worker pool from a bounded declarative configuration
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: hard
reading:
- context-garden/phase-06/specs/ec2-workers.md
created: '2026-09-06T16:27:49+00:00'
updated: '2026-09-06T16:27:49+00:00'
---

## Goal and evidence

Implement the on-demand lifecycle and bootstrap portion of specs/ec2-workers.md. Provide a plan/enable boundary, idempotent reconciliation with ownership tags, scoped credential delivery, reachable HTTPS enrollment, pinned versions and explicit failure states. Default to zero idle instances and a one-instance maximum.

Evidence should cover duplicate provisioning requests, delayed AWS responses, controller restart, bootstrap failure and cleanup without touching unrelated resources. A separately enabled bounded AWS canary must register a real worker and retire it with an inventory of any retained billed resources. Fake-provider tests alone do not establish live readiness.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Draft in frozen phase 06; do not approve, dispatch or provision cloud resources until the stabilization gate passes or Josh grants an explicit exception.
