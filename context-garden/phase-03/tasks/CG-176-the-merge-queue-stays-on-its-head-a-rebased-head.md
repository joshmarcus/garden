---
id: CG-176
title: 'The merge queue stays on its head: a rebased head whose CI is pending is in flight, not dropped,
  and merges when CI goes green'
status: ready
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
created: '2026-09-05T05:50:08+00:00'
updated: '2026-09-05T05:50:08+00:00'
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
