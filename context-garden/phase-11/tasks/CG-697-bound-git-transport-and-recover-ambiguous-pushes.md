---
id: CG-697
title: Bound Git transport and recover ambiguous pushes
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-11/goals.md
- src/garden/git_coordination.py
- tests/test_git_coordination.py
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:11:17+00:00'
---

## Goal

User value: a slow remote produces a recoverable state instead of a frozen scheduler. Why now: Git subprocesses have no deadlines. Size: hard. Dependencies: CG-631 and CG-632. Apply total operation deadlines, noninteractive authentication and descendant cleanup; reconcile interrupted pushes through their existing operation IDs before permitting effects.

## Context

Proposed at the context-garden/phase-10 retro. The existing recovery protocol cannot help until stalled transport returns control.

## Acceptance criteria

- [ ] Git coordination fetch, push and credential-helper execution return within a configured total operation deadline and use noninteractive authentication with cleanup of owned descendants.
- [ ] A timed-out push retains its operation identity and unresolved obligations until accepted state determines the result; retries cannot authorize duplicate execution or erase an ambiguous publication.
- [ ] Use controlled stalled fetch/push/helper cases, an accepted push with a lost reply, and successful controls to verify bounded return and safe subsequent progress without production-network calls.

## Planning boundary

Frozen Phase11 retrospective draft. No implementation approval, production activation, extra worker capacity, spending or deadline extension is implied. Address every intended outcome substantively; alternate evidence and justified criteria amendments are welcome. Retain material failures and avoid cosmetic or mechanical-rebase rejection rounds.
