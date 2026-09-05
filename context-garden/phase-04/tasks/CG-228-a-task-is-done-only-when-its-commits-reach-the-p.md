---
id: CG-228
title: 'A task is done only when its commits reach the product''s base branch: a stacked child merged
  into its parent''s branch stays open until the parent merges'
status: ready
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler/poll.py
- src/garden/scheduler/rebase.py
- src/garden/graph.py
- tests/scheduler/test_poll.py
created: '2026-09-05T18:14:53+00:00'
updated: '2026-09-05T18:14:53+00:00'
---

## Goal

`done` means the work is on the base branch. When a stacked child's PR is merged into its parent's branch (by a person on GitHub, or by any path that still allows it), the child moves to a `merged_into_parent` state that the Board and the graph treat as not yet done: dependents do not become ready, the retro does not count it merged, and the task page says which parent it is waiting on. It becomes `done` when the parent merges to the base branch and the poll sees the child's commits there. Automerge never merges into a non-base branch (CG-129 already); the web merge action and the CLI say the same.

## Context

2026-09-05: CG-189 (retro question cards) was stacked on CG-178; its PR #150 was merged into CG-178's branch at 13:38 and the poll marked CG-189 `done`. Five hours later CG-178 was still in review, so main had none of CG-189's code, and CG-225 (approved because its dependency CG-189 was "done") ran twice against a main without the mechanism it had to reconcile: its first worker reported "CG-189 has not merged: its branch is not an ancestor of main", and its trial had to be stopped. The graph's ready set trusts `done`; the poll's `PR merged` transition does not check the merge target.

## Acceptance criteria

- [ ] The poll's merged transition checks the PR's base: merged into the base branch gives `done`; merged into another branch gives `merged_into_parent` with the parent named in the log and on the task page.
- [ ] `graph.ready()` treats `merged_into_parent` as not terminal for dependents; the Board shows it in the review column with a badge; `garden status` counts it separately.
- [ ] When the parent's PR merges to the base branch, the poll promotes every `merged_into_parent` child whose commits are ancestors of the new base tip to `done`, with a log line.
- [ ] A test stacks a child, merges it into the parent's branch, checks the dependent stays blocked, merges the parent, and sees both done.

## Log

- 2026-09-05T18:14:53+00:00 approved (web)
