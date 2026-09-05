---
id: CG-160
title: garden retro --skip-personas can dispatch reconciliation with an empty persona-reviews section
status: ready
product: context-garden
phase: phase-03
depends_on:
- CG-145
priority: 1
difficulty: easy
reading:
- src/garden/retro.py
- src/garden/cli.py
- src/garden/scheduler.py
discovered_from: CG-145
created: '2026-09-05T03:54:03+00:00'
updated: '2026-09-05T03:57:42+00:00'
---

## Goal

`start_retro` forces `missing = []` whenever `skip_personas=True`, regardless of whether the requested personas actually have reports on disk (`persona_reports()` is only used to decide reuse-vs-run when *not* skipping). If an operator runs `garden retro --skip-personas` for personas that have no report at all yet, the reconciliation dispatches immediately with a partially or fully empty Persona reviews section.

## Context

Found while fixing CG-145 (garden retro waits for persona reports before reconciling). Not fixed there because it's a different code path with its own tested semantics (`--skip-personas` means "don't wait, use whatever's there"), and changing it risks breaking the documented use case of reusing already-run reports.

## Provenance

Discovered by CG-145 (garden retro waits for the persona reports before it dispatches the reconciliation) during run `20260905T033731Z-work`.

## Log

- 2026-09-05T03:54:03+00:00 discovered by CG-145
- 2026-09-05T03:57:42+00:00 approved (web)
