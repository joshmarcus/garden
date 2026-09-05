---
id: CG-229
title: Trial contender worktrees get the product setup like any work run, and a contender that reports
  a blocked environment is a harness failure, not a model loss
status: ready
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler/trials.py
- src/garden/scheduler/dispatch.py
- src/garden/runner/local.py
- src/garden/trials.py
- tests/test_trials.py
created: '2026-09-05T18:50:57+00:00'
updated: '2026-09-05T18:50:58+00:00'
---

## Goal

A model trial compares models, not environments. Every contender's worktree is prepared exactly like a work run's: the product's `setup.command` runs there (with `setup.log` in the run directory), the harness's config dir and the scrubbed environment apply, and the contender's harness has the same freedoms as the incumbent's (commit, push is the scheduler's, network per the product's setup). A contender whose run ends with an environment complaint (cannot commit, no dependencies, no network, not logged in) is recorded as a harness failure on the trial, shown as such on the task page and the trials page, and excluded from the comparison so the other contender does not win by default.

## Context

2026-09-05, the first two trials (CG-030 easy, CG-225 medium; claude sonnet 5 against codex): neither trial worktree got a `.venv` (no `setup.log` in any trial run directory, while work runs have one), so codex's contender on CG-030 stopped with "resume with writable Git metadata, prepared dependencies, asset network access" and claude improvised a test run; codex's sandbox (`full-auto`, workspace-write) also blocked `.git` writes and network, so it could not have committed at all until the operator switched the codex harness to bypass mode. The trial then declared claude the winner with both scores empty, which is a harness comparison, not a model one. CG-225's first trial had both contenders refuse a false premise (CG-189's code was not on main); that was correct behaviour and became a re-scope, not a loss.

## Acceptance criteria

- [ ] `start_trial` prepares each contender worktree through the same path as `dispatch` for a work run (setup command, env, config dirs); trial run directories carry `setup.log`.
- [ ] A contender result whose final message or exit reports an environment problem (the same classifier CG-212 and CG-217 add: quota, login, sandbox denial, missing setup) is marked `env_failed` on the trial with the message, and the comparison runs only over contenders that produced a PR; a trial with fewer than two PRs is `inconclusive`, not won.
- [ ] The trials page and the task page show contender states, costs and the failure kind; `garden trial` prints the same at the end.
- [ ] Tests: a trial where one contender's setup fails is inconclusive; a trial where both open PRs runs the comparison.

## Log

- 2026-09-05T18:50:58+00:00 approved (web)
