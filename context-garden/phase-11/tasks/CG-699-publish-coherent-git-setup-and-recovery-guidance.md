---
id: CG-699
title: Publish coherent Git setup and recovery guidance
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 2
difficulty: medium
reading:
- context-garden/phase-11/goals.md
- specs/multiplayer.md
- docs/multiplayer.md
- src/garden/migration.py
- src/garden/multiplayer_client.py
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:11:17+00:00'
---

## Goal

User value: administrators can admit users, assign work and resolve blocked handoffs without choosing between contradictory instructions. Why now: the released specification describes a rejected coordinator. Size: medium. Dependencies: accepted Git contracts and the migration repair for executable migration examples; architecture corrections can proceed earlier. Preserve automatic username binding, explicit unassignment and installation-bound authority.

## Context

Proposed at the context-garden/phase-10 retro. Clear operating instructions are necessary to make the delivered simplifications usable.

## Acceptance criteria

- [ ] Make product specification and operator guidance agree with the accepted Git architecture, removing unsupported coordinator-service and claim-timing descriptions without weakening the real trust and handoff boundaries.
- [ ] Document administrative initialization, admitted-user startup, assignment and blocked-handoff recovery while keeping ordinary browser login/enrollment steps hidden and preserving the single ownership intent.
- [ ] Check the documented commands and prerequisites against delivered behavior and clearly label unsupported migration/recovery paths until their implementation lands; documentation-only verification is sufficient for prose corrections.

## Planning boundary

Frozen Phase11 retrospective draft. No implementation approval, production activation, extra worker capacity, spending or deadline extension is implied. Address every intended outcome substantively; alternate evidence and justified criteria amendments are welcome. Retain material failures and avoid cosmetic or mechanical-rebase rejection rounds.
