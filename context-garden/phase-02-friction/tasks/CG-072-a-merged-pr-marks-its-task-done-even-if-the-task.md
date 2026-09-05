---
id: CG-072
title: A merged PR marks its task done even if the task had failed
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
branch: garden/cg-072-a-merged-pr-marks-its-task-done-even-if-the-task
pr: https://github.com/joshmarcus/context-garden/pull/67
attempts: 1
last_dispatched_at: '2026-09-04T22:33:28+00:00'
created: '2026-09-04T18:47:54+00:00'
updated: '2026-09-04T23:59:42+00:00'
---

## Goal

The poll covers every task that has a PR, whatever its status, so a PR merged or closed on GitHub always moves the task to `done` or `failed` accordingly.

## Context

During the first live run CG-046 and CG-039 failed (a revise round and a second attempt died on the old turn cap) while their PRs #11 and #14 were open; the person then merged both on GitHub. The tick only polls tasks in the review states, so the merges were never seen: both tasks sat on the Inbox's "Needs a decision" card as failed, with Retry and Cancel as the only buttons, although their work was on main. They were set to `done` by hand. Poll any task with `pr` set and an unfinished status (`failed`, `changes_requested`, `waiting_human`, `ready` after a retry), at least for the merged and closed checks, and let `failed` become `done` on merge.

## Acceptance criteria

- [ ] a `failed` task whose PR is merged becomes `done` on the next tick, with the worktree cleaned up and children restacked.
- [ ] a `failed` task whose PR is closed unmerged stays `failed` with the close noted.
- [ ] a test for both with the fake GitHub.

## Log

- 2026-09-04T18:47:54+00:00 approved
- 2026-09-04T22:33:28+00:00 dispatched work run 20260904T223319Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~2302 tokens)
- 2026-09-04T22:39:08+00:00 opened https://github.com/joshmarcus/context-garden/pull/67 (base main): Added Status.pr_pending (pr_open plus failed/waiting_human/ready) so the tick loop polls any task with a PR set in an unfinished status, not just the active review states; poll() now checks merged/closed for those extra statuses but skips the review-flow-only logic (triage, CI, feedback) unless the task is actually in an active review state. Added two tests with the fake GitHub covering merge-while-failed (-> done, worktree cleaned, children restacked) and close-while-failed (stays failed, close noted). cost=$2.76
- 2026-09-04T22:41:32+00:00 automated review: approve — Poll now covers any task with a PR in a non-terminal status via Status.pr_pending, resolving merges/closes for failed/waiting_human/ready tasks while skipping review-flow side effects; both acceptance cases are tested and pass. cost=$0.43
- 2026-09-04T23:59:42+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/67
