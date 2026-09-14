---
id: CG-696
title: Validate hosts before automatic local authentication
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:06:03+00:00'
---

## Goal

User value: retain effortless local startup while protecting private reads. Why now: the security reproduction and source show ambient identity under unknown Host values. Size: medium. Dependencies: CG-690 and web trust middleware. Use explicitly configured listener names, reject unknown hosts for GET and HEAD, and preserve permitted localhost behavior and mutation checks.

## Context

Proposed at the context-garden/phase-10 retro. This closes a concrete confidentiality gap without adding another login interaction.
