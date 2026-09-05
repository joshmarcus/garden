---
id: CG-174
title: garden pr and the web attach a new PR by refreshing the cached PR number and state, so the poll
  follows the new PR
status: ready
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
created: '2026-09-05T04:39:47+00:00'
updated: '2026-09-05T04:40:59+00:00'
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
