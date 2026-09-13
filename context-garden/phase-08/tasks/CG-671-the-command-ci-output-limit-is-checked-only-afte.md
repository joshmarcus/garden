---
id: CG-671
title: The command-CI output limit is checked only after subprocess.run has buffered al
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: persona:staff-engineer:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T16:57:41+00:00'
---

## Goal

Replace capture_output buffering in src/garden/ci_status.py:271 with bounded stream consumption for both channels, terminating owned processes when the limit is exceeded and returning an unavailable or malformed result. Reuse the process-supervision primitive where appropriate. Add bounded producer tests for excess stdout and stderr; the existing oversized-JSON test proves rejection after allocation rather than a resource limit.

## Context

Raised by the staff-engineer persona review (CI adapter resource bounds). persona:staff-engineer:context-garden/phase-07.
