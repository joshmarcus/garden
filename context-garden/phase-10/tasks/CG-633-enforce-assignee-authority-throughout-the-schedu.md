---
id: CG-633
title: Enforce assignee authority throughout the scheduler lifecycle
status: ready
product: context-garden
phase: phase-10
depends_on:
- id: CG-632
  after: merge
- id: CG-630
  after: merge
priority: 2
difficulty: hard
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- src/garden/scheduler/__init__.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/poll.py
- src/garden/scheduler/human.py
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
created: '2026-09-11T20:19:14+00:00'
updated: '2026-09-12T16:55:55+00:00'
---

## Goal

Make every automatic task transition belong to its assignee and assigned execution scope, across dispatch and all later lifecycle paths.

## Context and scope

Filtering the initial ready queue is insufficient. Inventory the full tick, result adoption, revision/review, human-answer resume, CI reconciliation/reruns, publication, merge and completion paths. Read observations may be shared; mutations must pass the coordinator contract.

## Acceptance criteria

- [ ] Admit work only for an active authenticated member who is the effective owner and has an enabled matching project/current phase, valid claim and all ordinary dependency, hold, resource and quality gates.
- [ ] Route every mutating task lifecycle path through current owner/generation validation and the shared effect gateway. Worker and reviewer claims are delegated under the owner while preserving independent reviews and source-head evidence.
- [ ] Ensure a member with no work assignment performs no task/run/PR/CI/phase/resource mutation when watch starts or ticks. Automatic planning, phase closure, retrospectives, infrastructure cleanup and upgrades require their own explicit scope and cannot escape through an idle scheduler.
- [ ] Exercise two members with mixed ownership and phases across fresh dispatch, completed results, revision, CI and merge eligibility; include two installations of one member. Assert that a non-owner tick does not progress the other member's issue and that existing single-user gates still work.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers)
