---
id: CG-169
title: 'garden qa: run on a schedule in CI with the scripted agent'
status: ready
product: context-garden
phase: phase-03
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/app.py
- tests/fake_claude.py
- tests/conftest.py
discovered_from: CG-135
created: '2026-09-05T04:17:48+00:00'
updated: '2026-09-05T05:05:27+00:00'
---

## Goal

Add a scheduled CI job (and a manual trigger) that runs `garden qa --scripted` and fails on a non-zero exit, so a page regression is caught between phases.

## Context

`garden qa --scripted` (CG-135) drives the nine flows in a few seconds with no tokens. The task said it runs in CI on a schedule; the workflow file is not part of that change.

## Provenance

Discovered by CG-135 (garden qa: an agent drives the loop end to end through the web app on a throwaway garden) during run `20260905T035723Z-work`.

## Log

- 2026-09-05T04:17:48+00:00 discovered by CG-135
- 2026-09-05T05:05:27+00:00 approved (web)
