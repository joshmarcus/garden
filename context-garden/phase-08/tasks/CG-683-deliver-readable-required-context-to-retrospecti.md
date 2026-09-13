---
id: CG-683
title: Deliver readable required context to retrospective workers
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 2
difficulty: medium
reading:
- context-garden/phase-08/goals.md
- src/garden/personas.py
- src/garden/reference_snapshot.py
- src/garden/scheduler/persona.py
- src/garden/remote_worker.py
discovered_from: retro:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T17:06:27+00:00'
---

## Goal

Include the requested sanitized walkthrough HTML/text and required context references in dispatched readable snapshots, or validate their availability as the actual worker identity before launch. Distinguish missing required input from inlined or controller-owned material using the existing brief machinery. Cover a canonical source readable by the controller but unavailable to the worker, and preserve content provenance and publication boundaries. Browser execution remains optional. Keep this distribution repair distinct from CG-663's missing-verdict rendering defect and CG-402's deferred immutable-evidence policy. File as a frozen Phase 08 draft.

## Context

A follow-up carried into phase-08 by the context-garden/phase-07 retro verdict.

## Acceptance criteria

- [ ] Include required permitted context and requested sanitized walkthrough HTML/text in the immutable readable reference snapshot for dispatched persona/retro workers, or validate equivalent access as that actual worker identity.
- [ ] Use worker-visible paths and explicit available/missing labels; do not point remote workers only at private controller paths. Keep browser use optional and never expand unrelated file/data permissions.
- [ ] Exercise actual brief/snapshot dispatch to an isolated worker identity with accessible and denied references. Preserve truthful limitations, avoid model launch for a deterministically missing required input, and avoid repeat persona calls when existing evidence suffices.

## Planning boundary

Retrospective draft in frozen Phase08; no implementation approval, runtime activation, private-data access, new workers or spending is implied. Address each outcome with meaningful observations; alternate evidence and reasoned criteria amendments are welcome. Preserve substantive findings and avoid process-only author rounds.
