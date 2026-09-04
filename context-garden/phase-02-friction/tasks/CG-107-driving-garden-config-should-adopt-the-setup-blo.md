---
id: CG-107
title: Driving garden config should adopt the setup block for context-garden
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/runner/local.py
- src/garden/runner/ssh.py
- src/garden/brief.py
- src/garden/config.py
- examples/garden.work.yaml
discovered_from: CG-081
created: '2026-09-04T21:17:52+00:00'
updated: '2026-09-04T21:26:18+00:00'
---

The joshmarcus/garden config still gates context-garden with an explicit `checks.pre_pr` running `$GARDEN_EXEC_ROOT/.venv/bin/python -m pytest` / `ruff`. With CG-081 merged, that product could instead define a `setup` block (test/lint/env) and leave `checks.pre_pr` empty so the tool's new default runs the same commands in the worktree. This is a config change in the separate garden repo, not the tool repo.

## Provenance

Discovered by CG-081 (Environment setup is per-product configuration, not a venv assumption) during run `20260904T210100Z-revise`.

## Log

- 2026-09-04T21:17:52+00:00 discovered by CG-081
- 2026-09-04T21:19:59+00:00 approved (web)
- 2026-09-04T21:26:18+00:00 duplicate of CG-092 (same change to the garden repo's config), which is running with the person's answer
