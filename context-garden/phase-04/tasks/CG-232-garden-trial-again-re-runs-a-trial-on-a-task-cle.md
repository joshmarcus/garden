---
id: CG-232
title: 'garden trial --again re-runs a trial on a task cleanly: closes or archives the previous contender
  PRs, clears the task''s cached PR state, and names branches from the task''s base, not the last winner'
status: done
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
pr: https://github.com/joshmarcus/context-garden/pull/187
attempts: 1
last_dispatched_at: '2026-09-05T20:25:55+00:00'
created: '2026-09-05T19:47:53+00:00'
updated: '2026-09-05T20:36:30+00:00'
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
- 2026-09-05T20:13:29+00:00 opened https://github.com/joshmarcus/context-garden/pull/187 (base main): garden trial --again now resets a task cleanly: it closes (or, with --keep-prs, leaves open) the previous contenders' PRs, deletes their remote branches, drops their worktrees, and clears the task's cached PR/review state before starting new contenders named from the task's default branch rather than the last winner's; the trials and task pages show every past trial for a task with closed contenders marked. cost=$4.72
- 2026-09-05T20:18:01+00:00 automated review requested changes: The --again reset itself is correct (verified live: branches renamed from base, PRs closed, state cleared), but the new trial-history view can display a closed PR as still open because closing a previously-open winner's PR during --again is never reflected back into the append-only trials.jsonl record. cost=$0.55
- 2026-09-05T20:18:21+00:00 dispatched revise run 20260905T201821Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~10700 tokens)
- 2026-09-05T20:25:34+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/187: Addressed the review's blocking finding: --again's PR closes now reflect back into the already-written trials.jsonl record via a new TrialLog.mark_closed, so trial-history views never show a PR as open after --again has closed it. cost=$0.59
- 2026-09-05T20:25:39+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/cli/loop.py); a rebase agent will resolve it
- 2026-09-05T20:25:55+00:00 dispatched rebase run 20260905T202555Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~9795 tokens)
- 2026-09-05T20:30:07+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/187: Rebased onto origin/main; resolved the single conflict in src/garden/cli/loop.py's trial() signature by keeping both sides' new options (--wait/--interval from main's CG-231, --again/--keep-prs from this branch) rather than letting one clobber the other. Rebase completed cleanly, no other files touched. cost=$0.22
- 2026-09-05T20:34:50+00:00 automated review: approve — The --again reset, branch naming, and trial-history backfill are all correctly implemented and verified against a full test run (910 passed) and lint; no correctness, scope, or description issues found. cost=$0.35
- 2026-09-05T20:34:55+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-05T20:36:30+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/187
