---
id: CG-173
title: Merging a stack parent retargets its children before the branch is deleted, and a child never opens
  a PR against a deleted branch
status: running
product: context-garden
phase: phase-03
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/poll.py
- src/garden/scheduler/reap.py
- src/garden/scheduler/dispatch.py
- src/garden/github.py
- tests/scheduler/test_poll.py
branch: garden/cg-173-merging-a-stack-parent-retargets-its-children-be
attempts: 1
last_dispatched_at: '2026-09-05T04:33:29+00:00'
created: '2026-09-05T04:31:41+00:00'
updated: '2026-09-05T04:33:29+00:00'
---

## Goal

When a stack parent merges, every stacked child keeps an open PR: the children are retargeted to the final base before the parent's branch is deleted, and a child whose parent is already merged opens its PR against the final base, never against the parent's branch.

## Context

On 2026-09-05 at 04:29 automerge merged CG-148 (#99) with `--delete-branch`. CG-161's PR #108 targeted that branch; GitHub closes a PR the instant its base branch is deleted, so #108 was closed before `_on_merged` reached `_restack`, and the poll then marked CG-161 `failed` ("PR closed without merging"). The operator restored the branch, reopened #108 onto main and deleted the branch again by hand.

In the same minute CG-141 (#102) merged the same way while CG-170, stacked on it, was still running with `restack_pending` set; its `pr_base` still named the deleted branch, so `_open_or_update_pr` at the end of its run would have failed. The operator restored that branch too.

`merge_pr(..., delete_branch=True)` is the default in `poll.py`'s automerge; `_on_merged` runs after the merge; `_restack` calls `update_pr(base=...)` on a PR that is already closed.

## Acceptance criteria

- [ ] Before merging a parent (automerge, and the CLI merge path if any), every non-terminal stacked child with an open PR is retargeted to the final base; only then is the parent's branch deleted. When retargeting fails, the branch is kept and the failure logged.
- [ ] A child whose `stack_parent` is terminal when its run finishes opens its PR against the final base and rebases onto it, using the mechanical rebase from CG-141; `pr_base` is corrected at that point.
- [ ] A PR closed because its base was deleted is recognised in the poll (the timeline event `base_ref_deleted`, or the base branch missing) and reopened onto the final base instead of failing the task; if GitHub refuses to reopen, a new PR is opened from the same branch.
- [ ] Tests cover the three cases with the fake GitHub.

## Log

- 2026-09-05T04:31:41+00:00 approved (web)
- 2026-09-05T04:33:29+00:00 dispatched work run 20260905T043320Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~8335 tokens)
