---
id: CG-176
title: 'The merge queue stays on its head: a rebased head whose CI is pending is in flight, not dropped,
  and merges when CI goes green'
status: done
product: context-garden
phase: phase-03
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/scheduler/rebase.py
- src/garden/scheduler/poll.py
- tests/test_rebase.py
- tests/test_automerge.py
branch: garden/cg-176-the-merge-queue-stays-on-its-head-a-rebased-head
pr: https://github.com/joshmarcus/context-garden/pull/127
attempts: 1
last_dispatched_at: '2026-09-05T09:35:19+00:00'
created: '2026-09-05T05:50:08+00:00'
updated: '2026-09-05T10:10:48+00:00'
---

## Goal

Once the merge queue picks a head and rebases it, it keeps that head until it merges or is genuinely taken off the queue (a conflict, a failed check, a new review round, a human request for changes). A head whose CI is still running after the pre-merge rebase is "in flight": the queue waits for it and merges the moment the rollup is green, and it never rebases a branch that is already on the base's tip.

## Context

Observed 2026-09-05 05:37 to 05:46 with eight approved, mergeable, green PRs open: `_merge_candidate` rebased the head (`mechanical`, `diff_unchanged`, `verdict_kept`), force-pushed it, and then failed the gate because the rollup was pending after the push; `_hold_automerge` popped `automerge_candidate` and `automerge_ready_at`. The next tick, `_maybe_automerge` re-marked the previous head only when its CI had finished, with a new `ready_at`, so the queue took a different PR as head, rebased that one, and dropped it the same way. Rebases at 05:38 (CG-125), 05:41 (CG-139), 05:43 (CG-150), 05:45 (CG-155); zero merges. Each rebase costs a full pre-PR check run inside the tick, so ticks stretched to a minute. The operator merged the set by hand with a scratch merge and the suite.

## Acceptance criteria

- [ ] After the pre-merge rebase, a pending rollup keeps the task as the queue head (a `merge_head` marker with its `ready_at`); the queue does not pick another head while one is in flight, and merges the head on the first poll where the rollup is green and the gate passes.
- [ ] A branch already on the base's tip is not rebased or pushed before merging.
- [ ] A head leaves the queue only on a conflict, a failed check, a changed diff that needs a review, a closed PR or a human request for changes; the reason is logged and the next-oldest candidate becomes head.
- [ ] `ready_at` is preserved across holds caused by a pending rollup so the queue order is stable.
- [ ] Tests with the fake GitHub: eight approved PRs merge one after another with exactly one rebase each; a pending rollup does not rotate the head.

## Log

- 2026-09-05T05:50:08+00:00 approved (web)
- 2026-09-05T05:51:13+00:00 dispatched work run 20260905T055105Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4176 tokens)
- 2026-09-05T09:32:51+00:00 attempt 1 failed: no GARDEN_RESULT in worker output (see final.md); will retry
- 2026-09-05T09:34:10+00:00 dispatch failed: git merge --ff-only -q origin/main (in /home/joshua/work/worktrees/CG-176): error: Your local changes to the following files would be overwritten by merge:
	src/garden/scheduler/rebase.py
Please commit your changes or stash them before you merge.
Aborting
- 2026-09-05T09:35:00+00:00 reset to ready by hand
- 2026-09-05T09:35:19+00:00 dispatched work run 20260905T093519Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~16172 tokens)
- 2026-09-05T09:57:33+00:00 opened https://github.com/joshmarcus/context-garden/pull/127 (base main): The merge queue now keeps its head: after the pre-merge rebase a head with a still-running rollup goes in flight (a merge_head marker holding its ready_at), the queue never rotates to another PR while one is in flight, a branch already on the base tip is merged without a rebase or push, and each PR is rebased at most once right before it merges. Added tests for eight PRs merging in order (one rebase each) and for a pending rollup holding the head; full suite (587) and lint pass. cost=$8.40
- 2026-09-05T10:01:10+00:00 description rewritten by the reviewer cost=$0.96
- 2026-09-05T10:10:48+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/127
