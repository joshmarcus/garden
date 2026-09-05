---
id: CG-232
title: 'garden trial --again re-runs a trial on a task cleanly: closes or archives the previous contender
  PRs, clears the task''s cached PR state, and names branches from the task''s base, not the last winner'
status: running
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler/trials.py
- src/garden/cli/reviews.py
- src/garden/scheduler/human.py
- tests/test_trials.py
branch: garden/cg-232-garden-trial-again-re-runs-a-trial-on-a-task-cle
attempts: 1
last_dispatched_at: '2026-09-05T19:48:30+00:00'
created: '2026-09-05T19:47:53+00:00'
updated: '2026-09-05T19:48:30+00:00'
---

## Goal

A trial can be run again on the same task without hand surgery: `garden trial <task> --again -c ...` (and the task page's trial form when a trial already ended) closes the previous contender PRs with a comment (or leaves them with `--keep-prs`), deletes or archives their branches and worktrees, resets the task's cached PR and review state, and starts the new contenders from the task's original base branch. Branch names come from the task's base branch, never from the last trial's winning branch.

## Context

2026-09-05 19:45: to compare claude sonnet 5 with codex on gpt-5.6-terra (the first run had used codex's default gpt-6-astra), the operator had to close two PRs by hand, remove two worktrees and two remote branches, run `set-status ready`, delete the `pr:` line from the task file and clear eleven keys from `state.json` under the lock between ticks, because `start_trial` refuses a task with a PR and reuses existing trial worktrees and branch names. The relaunch also produced the branch `garden/cg-225-...-trial-codex-trial-codex-gpt-5-6-terra`, because the previous winner's branch had become `task.branch` and the new suffix was appended to it.

## Acceptance criteria

- [ ] `garden trial --again` performs the reset above and starts the new trial; without `--again` a task with a finished trial and a PR still refuses with a message naming the flag.
- [ ] Contender branch names derive from the task's default branch; a winner's branch does not change what later trials are named.
- [ ] The trials page and the task page list previous trials with their contenders, scores, costs and PRs (closed ones marked), so a re-run's comparison is visible beside the first.
- [ ] Tests: run a trial, declare a winner, run `--again`, and check the old PRs closed, the state reset, the new branches named from the base.

## Log

- 2026-09-05T19:47:54+00:00 approved (web)
- 2026-09-05T19:48:30+00:00 dispatched work run 20260905T194814Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~9181 tokens)
