---
id: CG-348
title: Make EC2 pool cost health draining and teardown understandable and verifiable
status: draft
product: context-garden
phase: phase-06
depends_on:
- CG-345
- CG-346
- CG-347
priority: 2
difficulty: medium
reading:
- context-garden/phase-06/specs/ec2-workers.md
created: '2026-09-06T16:27:50+00:00'
updated: '2026-09-06T16:27:50+00:00'
---

## Goal and evidence

Deliver pool status and operator controls from the spec, integrating lifecycle, execution and Spot recovery. Show actual executing work, resource headroom, recovery state, estimated machine spend and model retry spend. Implement bounded launch/runtime policies, safe drain/disable, explicit emergency stop, and orphan-resource reconciliation. Billing delays must not be presented as an instantaneous hard budget guard.

Run an independently repeatable budgeted AWS acceptance exercise covering provisioning, work/check/review, interruption, controller restart and teardown. Record measured cost and inventory all retained resources. Walk through real operator actions and consequence-bearing decision cards; screenshots alone are insufficient. Preserve missing live evidence as UNPROVEN.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Draft in frozen phase 06; do not approve, dispatch or provision cloud resources until the stabilization gate passes or Josh grants an explicit exception.

## Pluggability requirement (owner clarification)

Provide common host inventory, lifecycle and cost controls independently of garden, then garden-specific task views as an integration. Include a standalone remote-dev workflow using the same EC2 provider and lifecycle: create from a dev profile, obtain approved SSH/editor connection information, preserve edits through stop/start, and release with an explicit workspace retention/deletion choice. Respect active sessions and workplace-supplied access policies. Demonstrate no dependency on a garden daemon or model account. Document how a work platform supplies its own identity, network, images and secrets. Real workplace acceptance remains separate from the example canary.
