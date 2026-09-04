---
id: CG-108
title: Document (or design a dedicated mode for) the GARDEN_ROOT-sentinel gotcha for self-hosted check
  commands
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/store.py
- src/garden/runner/local.py
- src/garden/brief.py
discovered_from: CG-101
created: '2026-09-04T21:18:21+00:00'
updated: '2026-09-04T21:20:35+00:00'
---

checks.run_check() always forces GARDEN_ROOT to a non-existent sentinel for `command` checks, which is correct for user-authored checks acting on the live garden but is a footgun for this repo's own `tests`/`lint` pre-PR checks, which run this repo's *own* test/lint tooling as that subprocess. CG-101 fixed the immediate breakage (an autouse conftest fixture strips ambient GARDEN_ROOT before each test), but the underlying trap — any self-hosted command check subprocess that itself calls find_root() will inherit the sentinel and must explicitly manage GARDEN_ROOT — isn't documented anywhere workers would see it before hitting it again. Consider a note in docs/architecture.md or checks.py's module docstring, or a `self_hosted: true` check flag that skips the GARDEN_ROOT override for checks running this repo's own tooling.

## Provenance

Discovered by CG-101 (Pre-PR `tests` check environment doesn't match test suite assumptions) during run `20260904T211520Z-work`.

## Log

- 2026-09-04T21:18:21+00:00 discovered by CG-101
- 2026-09-04T21:20:35+00:00 cancelled (web)
