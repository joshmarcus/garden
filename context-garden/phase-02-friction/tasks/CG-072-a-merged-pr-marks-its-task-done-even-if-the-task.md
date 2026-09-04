---
id: CG-072
title: A merged PR marks its task done even if the task had failed
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
created: '2026-09-04T18:47:54+00:00'
updated: '2026-09-04T18:47:54+00:00'
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
