---
id: CG-640
title: Verify the complete multiplayer workflow across independent local users
status: ready
product: context-garden
phase: phase-10
depends_on:
- id: CG-639
  after: merge
priority: 2
difficulty: hard
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- context-garden/specs/system-architecture.md
- src/garden/scheduler/__init__.py
- src/garden/web/app.py
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
created: '2026-09-11T20:19:16+00:00'
updated: '2026-09-12T16:55:55+00:00'
---

## Goal

Prove the integrated two-person local workflow, idle unassigned behavior and public read-only boundary on the final reviewed implementation.

## Context and scope

Use a bounded disposable local setup with separate checkouts and processes plus one coordinator. Reuse component checks and add only the missing integrated behaviors; this task does not require AWS workers, production fault injection, a paid deployment or a prescribed screenshot/receipt format.

## Acceptance criteria

- [ ] Run Alex and Blair from independent local roots against one coordinator with distinct issue/project/phase assignments. Demonstrate disjoint work, retained dependency/hold/review gates, a persisted start phase, and contention from a second installation of the same member without duplicate active ownership.
- [ ] Exercise reassignment during work, a stale result, a lost response, scheduler restart and coordinator disconnect/reconnect. Confirm preserved evidence, blocked unresolved effects, fenced stale operations and safe progress by the current assignee after recovery.
- [ ] Demonstrate personal Inbox and direct action isolation, consistent project focus across affected views and updates, and that changing views never changes execution scope. Verify an unassigned UI/watch startup causes no task/run/PR/CI/phase/resource operations.
- [ ] Run a viewer from only the approved projection and verify direct reads/mutation attempts, unpublished data exclusion and revocation behavior. Report actual observations and meaningful limitations without claiming broader platform or production evidence.
- [ ] Update the multiplayer specification and user documentation to match accepted behavior, record any genuinely deferred outcomes, and run applicable focused and final CI checks under the existing review policy. Keep release, activation and deployment separate from source acceptance.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers)
