---
id: CG-564
title: 'Every idle claim deep-copies all run history for request-identity lookup before '
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: persona:staff-engineer:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

Extract claim and replay policy into a service with indexed durable request identities, preserve historical rejection semantics, and test that idle claims avoid terminal-record materialization.

## Context

Raised by the staff-engineer persona review (Remote claim architecture). persona:staff-engineer:context-garden/phase-05.
