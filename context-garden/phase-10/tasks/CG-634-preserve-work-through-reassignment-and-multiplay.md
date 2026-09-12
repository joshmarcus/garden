---
id: CG-634
title: Preserve work through reassignment and multiplayer lease recovery
status: ready
product: context-garden
phase: phase-10
depends_on:
- id: CG-633
  after: merge
priority: 2
difficulty: hard
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- src/garden/runs.py
- src/garden/scheduler/poll.py
- src/garden/scheduler/state.py
- src/garden/config.py
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
created: '2026-09-11T20:19:14+00:00'
updated: '2026-09-12T16:55:55+00:00'
---

## Goal

Transfer an active issue between people without duplicate authors, stale publication or lost evidence.

## Context and scope

Apply the shared fencing protocol to reassignment, unassignment, changed work scope, revocation, crashed schedulers and network partitions. Existing commits and original run/review evidence remain immutable history.

## Acceptance criteria

- [ ] Fence the previous generation and stop new effects before acknowledging ownership or scope changes. Request safe local cancellation of active workers and expose an explicit handoff/reconciliation state instead of presenting two live owners.
- [ ] Retain late results as stale evidence without adopting status or publishing source. Reconcile pending provider operations under their original IDs; a handoff cannot finish while an old external outcome remains unknown.
- [ ] Allow the new assignee or authorized recovery operator to resume only after prior claims/effects are resolved. Preserve the original source, outputs, checks and review findings, and use normal review/source gates for the resumed attempt.
- [ ] Exercise reassignment during execution and publication, unassignment, revocation, lost heartbeat, crash/restart and delayed results. Confirm that stale installation and worker claims cannot advance the issue after a newer generation exists.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers)
