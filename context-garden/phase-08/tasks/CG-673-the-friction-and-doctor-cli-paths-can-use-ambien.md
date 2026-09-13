---
id: CG-673
title: The friction and doctor CLI paths can use ambient gh authentication even when th
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

Route src/garden/cli/planning.py:254 and src/garden/cli/diagnostics.py:491 through the same scoped client construction used by the scheduler, or enforce explicit credential selection centrally in GitHub. The crossed boundary is product-specific authority versus the operator's ambient identity: with a missing or revoked scoped token and an authenticated gh executable, friction collection can still read repository data and doctor can report successful authentication. Fail closed on missing scoped credentials and cover these CLI entry points with ambient gh present.

## Context

Raised by the security persona review (Scoped CLI credentials). persona:security:context-garden/phase-07.
