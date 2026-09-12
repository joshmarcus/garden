---
id: CG-468
title: Avoid nested validation admission deadlock during supervised full suites
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: medium
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-468-avoid-nested-validation-admission-deadlock-durin
pr: https://github.com/joshmarcus/context-garden/pull/369
discovered_from: CG-411
attempts: 1
last_dispatched_at: '2026-09-09T11:30:44+00:00'
created: '2026-09-09T10:03:17+00:00'
updated: '2026-09-09T11:46:22+00:00'
file: src/garden/validation.py
error: The supervised full suite timed out while `test_model_sessions_overlap...` launched nested validation
  work behind the outer suite's one-slot lease.
---

Allow tests and worker subprocesses that invoke the validation wrapper to complete when the enclosing full suite already holds the host validation lease.

## Provenance

Discovered by CG-411 (Adopt an existing PR with its verified branch and revision identity) during run `20260909T094734Z-revise`.
## Log
- 2026-09-09T10:03:17+00:00 discovered by CG-411
- 2026-09-09T10:59:01+00:00 approved (web)
- 2026-09-09T11:30:44+00:00 dispatched work run 20260909T113040Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11997 tokens)
- 2026-09-09T11:35:52+00:00 preserved uncommitted worktree changes from run 20260909T113040Z-work outside the PR: `git stash apply d694146987967460fdc9e938120740aabb0b2df0` in /home/joshua/work/worktrees/CG-468 (garden:CG-468:20260909T113040Z-work:reap)
- 2026-09-09T11:35:52+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T11:37:11+00:00 opened https://github.com/joshmarcus/context-garden/pull/369 (base main): Committed d450db228 to let nested validation wrappers inherit an enclosing full-suite admission lease, avoiding self-deadlock while retaining supervision and timeout behavior. Verified with the focused runner suite (67 passed), repository lint, and diff checks. cost=$0.60
- 2026-09-09T11:39:41+00:00 automated review: approve — Nested validation correctly inherits the enclosing supervisor lease while retaining supervision, timeout handling, and status reporting. cost=$0.26
- 2026-09-09T11:46:22+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/369
