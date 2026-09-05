---
id: CG-137
title: Split the scheduler by tick phase and the web actions into a registry so features stop colliding
status: done
product: context-garden
phase: phase-03
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/scheduler.py
- src/garden/web/app.py
- tests/test_scheduler.py
- tests/fake_claude.py
- docs/architecture.md
branch: garden/cg-137-split-the-scheduler-by-tick-phase-and-the-web-ac
pr: https://github.com/joshmarcus/context-garden/pull/96
attempts: 2
last_dispatched_at: '2026-09-05T03:22:09+00:00'
created: '2026-09-05T00:47:36+00:00'
updated: '2026-09-05T03:42:07+00:00'
---

## Goal

The scheduler is a package split by tick phase and the web's task actions are a registry, so two features in different parts of the loop no longer edit the same class body or the same `elif` chain. Pure movement: no behaviour change, the full suite passes untouched except for imports, and the review can check it mechanically.

## Context

Measured at the end of the first live run. Of 22 conflict events after 20:00, four files caused 20: `src/garden/scheduler.py` (6; one class, 108 methods, 2,359 lines), `src/garden/web/app.py` (6; 35 routes and one `task_action` with 17 `elif action ==` branches), `tests/fake_claude.py` (4) and `tests/test_scheduler.py` (4). Every feature PR edited the same class and the same chain, so thirty reviewed PRs spent the evening rebasing against each other. Cut: `garden/scheduler/` with `__init__.py` holding `Scheduler`, `tick()` and `_transition()`, and modules per phase: `reap.py` (finalize, pre-PR checks, fence), `poll.py` (PR state, feedback, conflicts, restack, automerge), `dispatch.py` (queue, slots, stacking, worktrees, briefs), `human.py` (answer, accept, reject, retry, triage, set-status, priority), `trials.py`, `budget.py`. Web: `garden/web/actions/` with one function per action registered by name (a decorator and a table), `task_action` becomes a lookup; pages grouped in `garden/web/pages/` beside their templates. Tests: `tests/scheduler/test_reap.py` and friends with fixtures in `conftest.py`; `fake_claude.py` gets a table of modes. Run this first in phase 03 with nothing in flight; it conflicts with everything by design. `docs/architecture.md` and `context-garden/product.md`'s module map follow.

## Acceptance criteria

- [ ] no module over 800 lines in `src/garden/scheduler/` or `src/garden/web/`; `task_action` is a registry lookup.
- [ ] the test suite passes with only import changes; `git diff --stat` shows moves, not rewrites (use `git log --follow` friendly moves).
- [ ] the module map in `product.md` and `docs/architecture.md` name the new modules.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)
- 2026-09-05T00:48:00+00:00 deferred by the feature freeze (2026-09-05): first task of phase 03, run alone
- 2026-09-05T03:01:17+00:00 approved (web)
- 2026-09-05T03:01:55+00:00 dispatched work run 20260905T030145Z-work via local [claude model=claude-fable-5-1] (fresh session, base main, ~14688 tokens)
- 2026-09-05T03:05:28+00:00 back to draft: approved by mistake during the phase 02 freeze; phase 03 work (CG-137 runs alone, first)
- 2026-09-05T03:17:38+00:00 priority 1 -> 0
- 2026-09-05T03:19:57+00:00 approved (web)
- 2026-09-05T03:22:09+00:00 dispatched work run 20260905T032209Z-work via local [claude model=claude-fable-5-1] (fresh session, base main, ~8637 tokens)
- 2026-09-05T03:36:08+00:00 discovered work filed: CG-159
- 2026-09-05T03:37:15+00:00 opened https://github.com/joshmarcus/context-garden/pull/96 (base main): Split the scheduler into a package of per-phase mixins, the web app into pages plus an action registry, the scheduler tests by area, and the fake harness into a table of modes. Pure movement: 458 tests pass, no module over 514 lines. cost=$10.17
- 2026-09-05T03:41:01+00:00 automated review: approve — Pure structural split of scheduler.py into per-phase mixins and web app.py into pages + an action registry; 145 methods and 47 scheduler tests preserved exactly, 458 tests pass, ruff clean, no scope creep or scar tissue. cost=$1.22
- 2026-09-05T03:42:07+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/96
