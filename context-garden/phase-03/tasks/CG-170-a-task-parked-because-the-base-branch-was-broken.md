---
id: CG-170
title: A task parked because the base branch was broken re-probes the base every tick and continues by
  itself when it goes green
status: ready
product: context-garden
phase: phase-03
depends_on:
- CG-141
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/reap.py
- src/garden/scheduler/poll.py
- src/garden/scheduler/human.py
- src/garden/scheduler/rebase.py
- src/garden/inbox.py
created: '2026-09-05T04:20:21+00:00'
updated: '2026-09-05T04:20:21+00:00'
---

## Goal

A task that the pre-PR path parked with the `base_broken` stop ("base branch `main` is itself broken ... waiting for the base to go green") continues on its own once the base is green: each tick the scheduler checks whether the base tip moved; when it has, it rebases the branch mechanically (the rebase mode from CG-141), re-runs the failed checks, and opens or updates the PR, all without a worker run and without a person.

## Context

On 2026-09-05 at 04:08 main went red (two PRs each green alone merged a minute apart). CG-148 and CG-154 probed while main was still red and parked correctly, with no revise round spent. Main was fixed at 04:12. Nothing un-parked them: `retry` starts a revise run (an agent, at the task's tier; fable for CG-154) and `resume` returns the task to review with the stale red CI still on the PR. The operator rebased both branches onto main by hand, pushed, and pressed `resume`. CG-160, which probed a minute after the fix, took the moved-base path and recovered by itself; the parked tasks should take the same path on a later tick.

The same applies to the CI path: a PR whose CI failed on the merge commit because main was red carries a red rollup until something pushes to the branch; the re-probe should push the rebased branch so CI runs again.

## Acceptance criteria

- [ ] Each tick, every task with a `base_broken` stop has its base tip compared with the probed commit; when it moved, the branch is rebased mechanically, the failed checks re-run, and on green the stop is cleared and the PR opened or updated, with a log line and a `rebased_stale_base` event; no worker run is dispatched.
- [ ] When the rebase does not apply cleanly, or the checks still fail after it, the task takes the existing revise path, and only then.
- [ ] The Inbox card for `base_broken` says the task will continue by itself and what it is waiting for.
- [ ] A test parks a task on a broken base, fixes the base, ticks, and sees the PR open with no run dispatched.

## Log

- 2026-09-05T04:20:21+00:00 approved (web)
