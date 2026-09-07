---
id: CG-348
title: Make EC2 pool cost health draining and teardown understandable and verifiable
status: ready
product: context-garden
phase: phase-05
depends_on:
- CG-345
- CG-346
- CG-347
priority: 2
order: 7
difficulty: medium
reading:
- context-garden/phase-06/specs/ec2-workers.md
created: '2026-09-06T16:27:50+00:00'
updated: '2026-09-07T12:47:31+00:00'
---

## Goal and evidence

Deliver pool status and operator controls from the spec, integrating lifecycle, execution and Spot recovery. Show actual executing work, resource headroom, recovery state, estimated machine spend and model retry spend. Implement bounded launch/runtime policies, safe drain/disable, explicit emergency stop, and orphan-resource reconciliation. Billing delays must not be presented as an instantaneous hard budget guard.

Run an independently repeatable budgeted AWS acceptance exercise covering provisioning, work/check/review, interruption, controller restart and teardown. Record measured cost and inventory all retained resources. Walk through real operator actions and consequence-bearing decision cards; screenshots alone are insufficient. Preserve missing live evidence as UNPROVEN.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Owner explicitly brought this work into phase 05 on 2026-09-07. Implementation is authorized now under ordinary admission; live provisioning follows the spec’s bounded resource/cost plan.

## Pluggability requirement (owner clarification)

Provide common host inventory, lifecycle and cost controls independently of garden, then garden-specific task views as an integration. Include a standalone remote-dev workflow using the same EC2 provider and lifecycle: create from a dev profile, obtain approved SSH/editor connection information, preserve edits through stop/start, and release with an explicit workspace retention/deletion choice. Respect active sessions and workplace-supplied access policies. Demonstrate no dependency on a garden daemon or model account. Document how a work platform supplies its own identity, network, images and secrets. Real workplace acceptance remains separate from the example canary.

## Log

- 2026-09-07T12:47:31+00:00 moved from context-garden/phase-06 to context-garden/phase-05

## Owner scope update, 2026-09-07

Remote AWS workers are now phase-05 work, without waiting for local stabilization failure. Preserve existing PRs, branches, evidence and dependency order. The reusable host lifecycle must still support non-garden remote development hosts. This supersedes earlier feature-deferral notes; it does not approve an old PR verdict or waive validation.
- 2026-09-07T12:47:31+00:00 approved (owner-phase05-promotion)
