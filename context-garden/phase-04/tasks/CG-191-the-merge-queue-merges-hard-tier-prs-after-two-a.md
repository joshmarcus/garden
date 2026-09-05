---
id: CG-191
title: The merge queue merges hard-tier PRs after two approving rounds and its own scratch-merge check
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 1
difficulty: medium
reading: []
branch: garden/cg-191-the-merge-queue-merges-hard-tier-prs-after-two-a
pr: https://github.com/joshmarcus/context-garden/pull/135
discovered_from: retro:context-garden/phase-03
attempts: 1
last_dispatched_at: '2026-09-05T12:20:04+00:00'
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T13:05:19+00:00'
---

## Goal

**User value:** an approved green hard-tier PR merges without a person, so the queue is shown working live on a batch and hand merges fall from twelve to zero.

**Why now:** twelve of thirty phase-03 merges were by hand, eight when the queue rotated and four on hard-tier PRs; the operator already asked for this policy.

**Size:** medium. **Depends on:** CG-176 (merged); a config key such as merge.hard_tier: two_rounds that a team can turn off, default on (the owner decided on 2026-09-05 that the queue may merge hard-tier PRs).

## Context

Proposed at the context-garden/phase-03 retro. The queue exists but half the merges still need a button; this closes the phase-03 promise the personas say is only half kept.

## Log

- 2026-09-05T10:31:16+00:00 approved (web)
- 2026-09-05T11:51:09+00:00 dispatched work run 20260905T115101Z-work via local [claude model=claude-opus-4-8] (fresh session, base garden/cg-197-split-cli-py-into-a-cli-package-and-fold-the-fou stacked on CG-197, ~4516 tokens)
- 2026-09-05T11:55:55+00:00 parent CG-197 merged; will rebase onto main when the current run finishes
- 2026-09-05T12:08:16+00:00 parent CG-197 merged; rebased onto main and retargeted the PR
- 2026-09-05T12:10:35+00:00 opened https://github.com/joshmarcus/context-garden/pull/135 (base main): Added github.automerge_hard_tier (default on): hard-tier PRs now automerge after two approving review rounds and the garden's own scratch-merge check — the pre-PR suite run on the branch rebased onto the base tip in a throwaway worktree, dispatched as a detached scratch_merge check run and recorded keyed to the reviewed diff. Full suite green (608 passed), lint clean, 10 new tests. cost=$6.73
- 2026-09-05T12:12:15+00:00 automated review: approve — Hard-tier automerge behind github.automerge_hard_tier (default on) with two-round and scratch-merge gates; all acceptance criteria met, logic sound, scope clean, tests and lint green. cost=$0.73
- 2026-09-05T12:12:21+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/poll.py); a rebase agent will resolve it
- 2026-09-05T12:12:31+00:00 dispatched rebase run 20260905T121231Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~7515 tokens)
- 2026-09-05T12:16:45+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/135: Resolved the poll.py conflict by keeping CG-191's _maybe_dispatch_scratch_merge call and combining it with main's new _queue_hold(task, reason) helper (from CG-202) in place of the old inline candidate/ready_at pop-and-log. Rebase completed cleanly on origin/main; full test suite (614 passed, 3 skipped) and ruff lint are green. cost=$0.27
- 2026-09-05T12:19:49+00:00 automated review requested changes: Hard-tier automerge is well-structured and criteria are met, but checkruns.py calls a nonexistent method _hold_automerge (renamed to _queue_hold by CG-202 during the rebase), raising AttributeError on both scratch-merge failure paths; the errors are silently swallowed by the tick's try/except and the failure test only passes because _automerge_gate re-derives the block reason next tick. cost=$1.11
- 2026-09-05T12:20:04+00:00 dispatched revise run 20260905T122004Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~5292 tokens)
- 2026-09-05T12:25:14+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/135: Renamed the two stale self._hold_automerge calls in the scratch-merge reap to _queue_hold (the method CG-202 introduced), fixing the AttributeError that was silently swallowed on both scratch-merge failure paths, and strengthened the failure test to assert the merge is held directly with no swallowed tick error. cost=$0.88
- 2026-09-05T12:25:14+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-191` for one more round, or review on GitHub
- 2026-09-05T12:39:17+00:00 automated review: approve — Hard-tier automerge behind github.automerge_hard_tier (default on) with a two-round gate and the garden's own diff-keyed scratch-merge check; all acceptance criteria met and tested, the prior _queue_hold rename bug is fixed on both failure paths, scope is exactly the 7 intended files, tests and lint green. cost=$0.71
- 2026-09-05T13:05:19+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/135
