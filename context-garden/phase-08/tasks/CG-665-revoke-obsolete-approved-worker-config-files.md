---
id: CG-665
title: Revoke obsolete approved worker config files
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 1
difficulty: medium
reading:
- context-garden/phase-08/goals.md
- src/garden/runner/base.py
- src/garden/runner/ssh.py
discovered_from: retro:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T17:05:13+00:00'
---

## Goal

User value: removing an approved mapping actually removes Garden's retained credential copy before another run. Why now: current installers only process mappings that remain configured. Size: medium. Dependencies: CG-401 mapping validation and local/SSH installation paths. Reconcile previously managed destinations for mapping deletion, destination changes and an empty allowlist while preserving unrelated files and symlink protections.

## Context

Proposed at the context-garden/phase-07 retro. Current operator authorization must determine the capabilities available to the next worker.

## Acceptance criteria

- [ ] Track Garden-managed approved-file destinations and remove obsolete copies before the next run when a mapping is removed, changes destination, or the allowlist becomes empty.
- [ ] Apply equivalent revocation behavior across supported local/SSH/remote installation paths, preserving unrelated files and caches, restrictive permissions and symlink/path boundaries.
- [ ] Cover mapping deletion, moved destination and empty allowlist with meaningful lifecycle tests. Report removal of managed copies honestly; do not claim this revokes a credential copied independently outside Garden.

## Planning boundary

Retrospective draft in frozen Phase08; no implementation approval, runtime activation, private-data access, new workers or spending is implied. Address each outcome with meaningful observations; alternate evidence and reasoned criteria amendments are welcome. Preserve substantive findings and avoid process-only author rounds.
