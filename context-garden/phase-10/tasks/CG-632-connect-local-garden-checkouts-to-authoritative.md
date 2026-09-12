---
id: CG-632
title: Connect local garden checkouts to authoritative multiplayer state
status: ready
product: context-garden
phase: phase-10
depends_on:
- id: CG-631
  after: merge
priority: 2
difficulty: hard
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- src/garden/config.py
- src/garden/store.py
- src/garden/scheduler/__init__.py
- src/garden/web/common.py
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
created: '2026-09-11T20:19:13+00:00'
updated: '2026-09-12T16:55:55+00:00'
---

## Goal

Let each person run a local UI and scheduler against the same coordinator while keeping their workspace and execution setup local.

## Context and scope

The coordinator is shared control infrastructure, not a centralized UI or a replacement for local scheduling. Build a reusable client boundary before changing tick behavior. Local task files are cached projections and authored proposal sources, not independent lifecycle authorities.

## Acceptance criteria

- [ ] Configure a local installation with garden identity, coordinator endpoint and authenticated member credentials stored outside shared context. Keep local harness configuration and execution credentials local; do not give workers unrestricted shared publication credentials.
- [ ] Read versioned authoritative snapshots and submit validated commands through one client abstraction usable by scheduler and UI. Reject garden/version mismatches and prevent code paths from silently falling back to writable standalone state.
- [ ] Synchronize accepted authored context and task projections into independent checkouts without force-resetting unrelated edits. Surface content conflicts and projection lag; require the canonical revision needed for the requested operation.
- [ ] On disconnect retain authorized read views with a stale-state indicator and stop mutations. Refresh assignments, roles, claims and source state before reconnecting work; reject unchecked offline command replay. Check this using two separate local roots.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers)
