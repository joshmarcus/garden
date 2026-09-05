---
id: CG-126
title: Verify worktree provisioning for stacked tasks actually checks out the parent branch
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/web/app.py
- src/garden/web/templates/base.html
- src/garden/web/templates/phase.html
- src/garden/store.py
- src/garden/model.py
- src/garden/cli.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
discovered_from: CG-121
created: '2026-09-04T23:45:33+00:00'
updated: '2026-09-05T00:04:53+00:00'
---

Twice now (this run and the prior CG-121 attempt) a task whose brief says "based on <parent-task-branch>" was actually checked out at main instead, because the parent PR wasn't merged yet. This time the branch had no commits of its own so a fast-forward fixed it safely, but that won't always be true. Worth checking the runner/worktree setup for stacked tasks so this doesn't recur and doesn't require a worker to reach for git surgery.

## Provenance

Discovered by CG-121 (Planner and friction reports can still create tasks in a closed phase) during run `20260904T233628Z-work`.

## Log

- 2026-09-04T23:45:33+00:00 discovered by CG-121
- 2026-09-05T00:04:53+00:00 approved (web)
- 2026-09-05T00:04:53+00:00 priority 3 -> 1 (web)
