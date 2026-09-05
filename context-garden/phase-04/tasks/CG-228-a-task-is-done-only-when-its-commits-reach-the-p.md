---
id: CG-228
title: 'A task is done only when its commits reach the product''s base branch: a stacked child merged
  into its parent''s branch stays open until the parent merges'
status: running
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
branch: garden/cg-228-a-task-is-done-only-when-its-commits-reach-the-p
pr: https://github.com/joshmarcus/context-garden/pull/178
attempts: 1
last_dispatched_at: '2026-09-05T18:47:53+00:00'
created: '2026-09-05T18:14:53+00:00'
updated: '2026-09-05T18:47:53+00:00'
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
- 2026-09-05T18:16:06+00:00 dispatched work run 20260905T181552Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~16648 tokens)
- 2026-09-05T18:41:58+00:00 opened https://github.com/joshmarcus/context-garden/pull/178 (base main): Added a merged_into_parent task status: the poll now checks a merged PR's base against the product's base branch, holds a stacked child there (with the parent named in state/log/task page) instead of marking it done, and promotes it to done via an ancestor check once the parent itself reaches the base. Wired the new status into the Board (in_review column, badge), garden status, graph/TUI/CLI colour maps, and the stuck-task audit, plus a full-loop test. cost=$7.32
- 2026-09-05T18:47:36+00:00 automated review requested changes: The merged_into_parent status, gating, and surfaces are correctly wired, but the promotion-to-done check uses git ancestry, which cannot succeed once the parent's own merge to the base is a squash merge — the garden's own default automerge method — so affected children get stuck forever with no retry path; the new test only exercises fast-forward merges and misses this. cost=$0.82
- 2026-09-05T18:47:53+00:00 dispatched revise run 20260905T184753Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~17313 tokens)
