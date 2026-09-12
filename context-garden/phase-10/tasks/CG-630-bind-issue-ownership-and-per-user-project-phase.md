---
id: CG-630
title: Bind issue ownership and per-user project phase assignments to membership
status: ready
product: context-garden
phase: phase-10
depends_on:
- id: CG-629
  after: merge
- id: CG-414
  after: merge
priority: 2
difficulty: hard
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- src/garden/model.py
- src/garden/store.py
- src/garden/graph.py
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
created: '2026-09-11T20:19:13+00:00'
updated: '2026-09-12T16:55:55+00:00'
---

## Goal

Resolve one accountable member per issue and a separate explicit project/phase execution assignment per member.

## Context and scope

Extend CG-414 instead of creating a parallel owner model. The project shown in the UI is the existing product key. A work scope does not implicitly assign every issue in that phase; changing a view does not change a work scope.

## Acceptance criteria

- [ ] Preserve explicit task owner, explicit unassignment, phase default and otherwise-unassigned precedence. Validate effective owners against active project membership; unresolved legacy labels cannot acquire execution authority. No implicit project owner fallback.
- [ ] Persist zero or one active project/current-phase assignment per member with generation, enabled/paused state and optional phase advancement. New members have none. Show explicit assignment and default-owner changes separately, including the affected issues before a bulk operation.
- [ ] Keep dependencies, holds and phase-completion rules in eligibility. Default phase advance to an explicit action; configured advance cannot assign new work or close a phase while another member still has unfinished work. Model phase-operation authority separately from a task default owner.
- [ ] Validate inherited and overridden ownership, disabled/unknown owners, unassigned members, issues outside the current scope, stale assignment edits and a dependency crossing a project boundary. Display only permitted dependency information.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers)
