---
id: CG-174
title: garden pr and the web attach a new PR by refreshing the cached PR number and state, so the poll
  follows the new PR
status: done
product: context-garden
phase: phase-03
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/cli.py
- src/garden/scheduler/__init__.py
- src/garden/scheduler/poll.py
- src/garden/scheduler/state.py
branch: garden/cg-174-garden-pr-and-the-web-attach-a-new-pr-by-refresh
pr: https://github.com/joshmarcus/context-garden/pull/119
attempts: 1
last_dispatched_at: '2026-09-05T04:57:34+00:00'
created: '2026-09-05T04:39:47+00:00'
updated: '2026-09-05T05:49:52+00:00'
---

## Goal

Attaching a PR to a task by hand (`garden pr <id> <url>`, and any web equivalent) makes the scheduler follow that PR from the next tick: the cached `pr_number`, `pr_state`, `head_sha`, `review_run` and `automerge_blocked` in `state.json` are reset for the task, and its status becomes `in_review`.

## Context

On 2026-09-05 at 04:31 the operator opened PR #110 for CG-161 after GitHub closed its stacked PR #108 (CG-173), then ran `garden pr CG-161 <#110>`. The command set the task's `pr` field and status, but `_pr_number` prefers `state["pr_number"]` (still 108) over the URL, so the next poll looked at #108, saw it closed, and failed the task again; this repeated every tick until the operator edited `state.json` by hand under the lock. A review run for the task was orphaned in the meantime.

## Acceptance criteria

- [ ] `garden pr` (and the web action, if one exists) resets the task's cached PR fields in state and logs the old and new PR numbers.
- [ ] After attaching, the next poll reads the new PR; a test attaches a second PR to a task whose first PR is closed and sees the task stay `in_review`.
- [ ] `_pr_number` (or its successor) prefers the task's `pr` URL when it disagrees with the cached number, and repairs the cache.

## Log

- 2026-09-05T04:40:59+00:00 approved (web)
- 2026-09-05T04:57:34+00:00 dispatched work run 20260905T045725Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~3964 tokens)
- 2026-09-05T05:08:13+00:00 opened https://github.com/joshmarcus/context-garden/pull/119 (base main): `garden pr` now goes through a new Scheduler.attach_pr() that resets the cached pr_number, pr_state, head_sha, review_run and automerge_blocked in state.json and logs the old/new PR numbers, so the next poll follows a newly attached PR instead of a stale one; _pr_number() also now self-heals when the cached number disagrees with the task's pr URL. cost=$1.87
- 2026-09-05T05:13:26+00:00 automated review: approve — attach_pr resets all cached PR state and _pr_number self-heals against a stale cache; all three acceptance criteria are met and directly tested, and the change is tightly scoped with a clean, self-contained description. cost=$0.74
- 2026-09-05T05:28:41+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T05:35:15+00:00 automated review: approve — attach_pr resets all cached PR state (pr_number, pr_state, head_sha, review_run, automerge_blocked) and logs old/new numbers, and _pr_number self-heals against a stale cache; all three acceptance criteria are met and directly tested, tests and lint pass, and the change is tightly scoped with a clean description. cost=$0.83
- 2026-09-05T05:49:52+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/119
