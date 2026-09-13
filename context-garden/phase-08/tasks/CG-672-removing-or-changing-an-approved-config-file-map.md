---
id: CG-672
title: Removing or changing an approved config-file mapping leaves the previously insta
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: persona:security:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T16:57:41+00:00'
---

## Goal

In src/garden/runner/base.py:276 and the equivalent SSH installation path, track previously managed destinations and safely remove obsolete copies before launching another run, including when the mapping becomes empty. The crossed boundary is current operator authorization versus retained worker capability: a later worker or branch test can read a still-valid credential after its mapping was removed. Preserve unrelated caches and add regression coverage for mapping deletion, destination changes, and an empty allowlist across supported transports.

## Context

Raised by the security persona review (Tool configuration revocation). persona:security:context-garden/phase-07.
