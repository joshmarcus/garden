---
id: CG-695
title: Repair Git migration and standalone reversal
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-11/goals.md
- src/garden/migration.py
- src/garden/git_coordination.py
- tests/test_migration.py
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:11:17+00:00'
---

## Goal

User value: move an existing garden into or out of multiplayer without losing authority or duplicating work. Why now: released migration still initializes SQLite and export misses other installations' Git obligations. Size: hard. Dependencies: delivered CG-631, CG-632 and CG-634; correct the implementation delivered by CG-639 without duplicating its historical task. Cover resumable commit, preserved ownership/history, Git-backed startup and refusal under unresolved work.

## Context

Proposed at the context-garden/phase-10 retro. The supported recovery boundary must agree with the architecture before users entrust existing work to multiplayer.

## Acceptance criteria

- [ ] Preview, commit and resumable migration initialize the accepted Garden Git authority through supported configuration, preserving owners, installations and task/run history without requiring or creating the obsolete coordinator service.
- [ ] Standalone export checks authoritative Git claims and unresolved effects across installations; uncertain, unavailable or active authority blocks export while confirmed quiescence permits it.
- [ ] Exercise the actual migration/CLI boundary against disposable Git repositories with successful startup/export, interrupted migration recovery and another installation's unresolved permit. Preserve the original failure evidence and supported legacy behavior explicitly.

## Planning boundary

Frozen Phase11 retrospective draft. No implementation approval, production activation, extra worker capacity, spending or deadline extension is implied. Address every intended outcome substantively; alternate evidence and justified criteria amendments are welcome. Retain material failures and avoid cosmetic or mechanical-rebase rejection rounds.
