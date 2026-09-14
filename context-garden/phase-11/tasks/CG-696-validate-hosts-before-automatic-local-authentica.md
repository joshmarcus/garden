---
id: CG-696
title: Validate hosts before automatic local authentication
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 1
difficulty: medium
reading:
- context-garden/phase-11/goals.md
- src/garden/web/app.py
- src/garden/web/trust.py
- tests/test_web.py
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:11:17+00:00'
---

## Goal

User value: retain effortless local startup while protecting private reads. Why now: the security reproduction and source show ambient identity under unknown Host values. Size: medium. Dependencies: CG-690 and web trust middleware. Use explicitly configured listener names, reject unknown hosts for GET and HEAD, and preserve permitted localhost behavior and mutation checks.

## Context

Proposed at the context-garden/phase-10 retro. This closes a concrete confidentiality gap without adding another login interaction.

## Acceptance criteria

- [ ] Reject unrecognized request hosts before automatic local identity grants private reads, including GET and HEAD, using explicit listener/configuration names rather than request-derived or forwarded allowlists.
- [ ] Permitted local/listener aliases retain automatic server-start identity and normal authorized UI behavior, with existing mutation-origin, worker-ingress and public-view protections preserved.
- [ ] Exercise the production middleware with synthetic private content, unknown hosts, permitted localhost aliases and relevant forwarded-header controls. Describe the verified boundary without claiming browser exploitation that was not demonstrated.

## Planning boundary

Frozen Phase11 retrospective draft. No implementation approval, production activation, extra worker capacity, spending or deadline extension is implied. Address every intended outcome substantively; alternate evidence and justified criteria amendments are welcome. Retain material failures and avoid cosmetic or mechanical-rebase rejection rounds.
