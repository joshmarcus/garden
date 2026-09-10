---
id: CG-576
title: Deliver controller-owned CI diagnostics to isolated workers
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

Preserve credential isolation while making the actual failing node, command, source and readable diagnostic excerpt available to the assigned worker. Coordinate CG-396 status policy and CG-506 transport; address the specific repeated inaccessible-log failure, not another CI provider implementation. An authentication error alone must not be presented as a source-test failure.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.
