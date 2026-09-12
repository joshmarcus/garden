---
id: CG-631
title: Add shared transactional coordination and fenced mutation operations
status: ready
product: context-garden
phase: phase-10
depends_on:
- id: CG-629
  after: merge
- id: CG-630
  after: merge
priority: 2
difficulty: hard
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- src/garden/store.py
- src/garden/events.py
- src/garden/scheduler/state.py
- src/garden/web/app.py
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
created: '2026-09-11T20:19:13+00:00'
updated: '2026-09-12T16:55:55+00:00'
---

## Goal

Provide one authoritative coordination service for independently running local schedulers, with atomic ownership claims and recoverable shared effects.

## Context and scope

Use one coordinator with its own transactional local database and durable operation journal. Do not synchronize a database through Git or rely on a local file lock across machines. Git remains authored context and the canonical task projection. This task supplies the protocol and service; client adoption and scheduler integration follow.

## Acceptance criteria

- [ ] Implement authenticated, versioned snapshots and compare-and-swap commands that bind garden, actor, task version, accepted owner, assignment generation, installation, operation ID and server-issued lease/fencing generation. Concurrent claims admit at most one valid owner, including two installations for the same member.
- [ ] Journal task transitions and Git projections through a recoverable outbox. A projection failure remains pending with its original identity; stale Markdown cannot overwrite newer authority. Preserve authored conflicts and immutable evidence without treating corrupt state as an empty garden.
- [ ] Provide a serialized shared-effect gateway and ledger for publication and other provider mutations, with narrow delegated credentials and provider preconditions where available. Coordinate admission with reassignment. Unknown external outcomes block conflicts pending reconciliation rather than blind retries or an exactly-once claim.
- [ ] Reserve shared capacity and spending atomically so limits cannot be multiplied by scheduler count. Gate phase/global operations with explicit authority; retain existing host-local caps and resource policy.
- [ ] Validate independent competing clients, stale generations, clock skew, duplicate/lost replies, coordinator restart and pending Git/provider effects. Expose useful waiting/conflict states and protocol compatibility failures.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers)
