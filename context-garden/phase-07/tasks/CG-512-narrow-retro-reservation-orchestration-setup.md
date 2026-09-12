---
id: CG-512
title: Narrow retro reservation orchestration setup
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler/retro.py
- src/garden/store.py
- tests/test_retro.py
- tests/test_store.py
branch: garden/cg-512-narrow-retro-reservation-orchestration-setup
pr: https://github.com/joshmarcus/context-garden/pull/435
runner: remote
discovered_from: CG-502
attempts: 1
last_dispatched_at: '2026-09-10T12:52:07+00:00'
created: '2026-09-10T10:58:33+00:00'
updated: '2026-09-10T13:12:28+00:00'
file: tests/test_retro.py
error: Reservation bookkeeping tests repeat repository, worktree, commit, and PR setup already covered
  at the Store layer.
---

Retain one scheduler/worktree integration test proving retro draft IDs cannot collide with live task creation. Refactor the abandoned-rerun case to prove owner-batch release and stable ID reuse without executing a second complete retro journey, relying on existing Store tests for restart persistence, release, skip, and prune details. Preserve the outcome rather than asserting a private helper call.

## Provenance

Discovered by CG-502 (Find redundant or low-value expensive tests) during run `20260910T105011Z-work`.
## Log
- 2026-09-10T10:58:33+00:00 discovered by CG-502

## Acceptance criteria

- [ ] Retain one scheduler/worktree integration proving a retro draft reservation cannot collide with concurrent live task creation.
- [ ] Cover abandoned rerun cleanup with a small owner-batch release and stable-ID reuse test rather than a second full repository, worktree, commit and PR journey.
- [ ] Preserve restart persistence, release, skip and prune guarantees in Store-level tests and assert observable outcomes rather than private helper calls.
- [ ] Run focused retro and Store tests plus repository lint, and record the removed setup/runtime without weakening reservation race coverage.
- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T12:52:07+00:00 dispatched work run 20260910T125207Z-work via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~13771 tokens)
- 2026-09-10T12:54:57+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T12:57:59+00:00 opened https://github.com/joshmarcus/context-garden/pull/435 (base main): Refactored retro reservation coverage to retain one scheduler/worktree race integration and move abandoned-rerun release/reuse verification into a small Store test. Focused retro and Store tests passed (46), and repository lint passed. cost=$0.04
- 2026-09-10T13:02:56+00:00 automated review: approve — The refactor preserves reservation race coverage while replacing the redundant full retro rerun with focused public Store behavior coverage. cost=$0.22
- 2026-09-10T13:12:28+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/435
