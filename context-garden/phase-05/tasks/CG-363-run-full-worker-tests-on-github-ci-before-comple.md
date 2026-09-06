---
id: CG-363
title: Run full worker tests on GitHub CI before completion
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading: []
branch: codex/cg-363-worker-ci
pr: https://github.com/joshmarcus/context-garden/pull/243
runner: manual
attempts: 1
last_dispatched_at: '2026-09-06T22:36:08+00:00'
created: '2026-09-06T22:34:20+00:00'
updated: '2026-09-06T22:59:27+00:00'
---

## Goal

Move this product's full worker test suite to GitHub Actions so a worker can fix failures in its current session without putting another large suite on the WSL host.

## Context

Owner requested 2026-09-06 during the memory/web incident. Existing CI only runs after PR publication or a main push; worker briefs prohibit pushing and pre-PR checks repeat the full suite locally. Direct operator implementation is authorized, with ordinary admission paused and no extra model agent. Preserve focused local checks and the existing PR merge gate.

## Acceptance criteria

- [ ] A clean committed worker branch can start full GitHub CI before a PR exists, wait in the foreground, and obtain a result tied to exactly that commit.
- [ ] Stale, missing, failed or unfinished CI cannot be reported as a pass; rechecking unchanged commits reuses the existing run and failures expose useful logs.
- [ ] Push authorization is explicit per product; workers push only their assigned branch without force and the scheduler retains PR creation and merge ownership.
- [ ] The live product configuration asks for focused local checks plus remote full-suite validation and avoids repeating the full suite locally; authenticates in the worker's isolated environment.
- [ ] Focused regressions and an actual GitHub branch run verify the path; existing full PR CI remains required.

## Log

- 2026-09-06T22:36:07+00:00 Owner authorized direct operator implementation for CI offload; worktree outside scheduler-managed task path, branch codex/cg-363-worker-ci.
- 2026-09-06T22:36:08+00:00 approved (cli)
- 2026-09-06T22:36:08+00:00 dispatched work run 20260906T223608Z-work via manual [human] (fresh session, base main, ~8545 tokens)
- 2026-09-06T22:56:30+00:00 Direct operator repair self-reviewed under owner authority. Normal manual completion with review disabled only for this call prevents an unsolicited model agent; no automated verdict is fabricated. PR243 merged58e13b99, final branch and PR CI passed1224/3skipped; main CI34065153856 also passed. Live rollout follows while existing service is stopped at drain.
- 2026-09-06T22:56:30+00:00 finished (work): Implemented and merged worker GitHub CI offload; live rollout is the remaining operator step.
- 2026-09-06T22:57:07+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/243
- 2026-09-06T22:59:27+00:00 2026-09-06T22:59:27+00:00: Live rollout complete. Installed CI-verified merged58e13b99; explicit context-garden worker_push/remote test/GH_CONFIG_DIR enabled, isolated HOME retained, pre-PR lint scoped to context-garden and existing docs-product behavior preserved. Installed CG361 brief and actual check commands validated. Normal scheduler reconciled merged task to done. HTTP /,Now2,Inbox,Config200; Now2 .563s WSL/2.044s Windows, service142MiB and no high/OOM/swap. All acceptance criteria now fulfilled; earlier manual result correctly recorded rollout as pending at code completion.
