---
id: CG-476
title: Complete external manual runs after a verified squash merge
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/human.py
- src/garden/scheduler/poll.py
- src/garden/github.py
- src/garden/gitops.py
- tests/scheduler/test_human.py
branch: garden/cg-476-complete-external-manual-runs-after-a-verified-s
pr: https://github.com/joshmarcus/context-garden/pull/374
attempts: 1
last_dispatched_at: '2026-09-09T13:46:23+00:00'
created: '2026-09-09T12:12:45+00:00'
updated: '2026-09-09T14:14:08+00:00'
---

## Goal

Complete an externally owned manual run when GitHub reports its exact PR merged by squash and the resulting commit is verified on the final base, without requiring the original PR head to be an ancestor of that base.

## Confirmed defect

CG-474 was implemented and reviewed at exact head `5208120b4cc739c4e0dd39bd539321da59205b0f`, then operator squash-merged as PR #370 to commit `739f7b5da823ce976d23281c7b280c1e60482692`. The current `Scheduler._finish_external_manual` rejected completion because it only tests ancestry of the original head. A squash merge intentionally rewrites that head, although fresh GitHub facts, merge-commit ancestry, and stable patch identity all confirmed the exact source reached `main`. The guarded operator reconciliation and both refusal attempts remain preserved in `/home/joshua/work/operator-test-tmp/cg474-manual/completion-receipt.json`.

CG-362 introduced verified external completion and requires already merged PR support, but its ancestry-only implementation omitted squash merges. CG-228 already handles squash identity for stacked-child promotion; reuse consistent source/merge provenance where appropriate rather than weakening the fence.

## Acceptance criteria

- [ ] For a GitHub PR reported `MERGED`, support merge, rebase, and squash methods using immutable PR head, merge commit, base, repository, and final-base facts. A squash result can complete only when the verified merge commit is included in the configured final base and the original PR source is proven equivalent to that result.
- [ ] Reject a coincidental merge commit, wrong repository/base/branch, moved or mismatched head, partial/cherry-picked content, inaccessible metadata, and any failed Git/worktree fence. Do not trust a user-supplied commit alone.
- [ ] Successful completion preserves the original source head and merge commit separately, retains prior refusal attempts and run/result evidence, uses the ordinary task/dependency lifecycle, and records external/operator provenance without counting it as a Garden automatic merge.
- [ ] Focused tests cover ordinary ancestry, a real squash topology, rebase merge, mismatched patch/content, stale head, wrong base/repository, repeated completion, and the CG-474 refusal reproduction.

## Log

- 2026-09-09T12:13:17+00:00 approved (operator: reproduced CG-474 squash-completion defect with verified source and merge facts)
- 2026-09-09T12:13:17+00:00 Filed from preserved CG-474 operator reconciliation; do not reopen or relabel that completed implementation run.
- 2026-09-09T12:34:15+00:00 dispatched work run 20260909T123411Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~18802 tokens)
- 2026-09-09T12:46:00+00:00 preserved uncommitted worktree changes from run 20260909T123411Z-work outside the PR: `git stash apply cd42acf5befbaea5af3c09b3def0bad6944e9f33` in /home/joshua/work/worktrees/CG-476 (garden:CG-476:20260909T123411Z-work:reap)
- 2026-09-09T12:46:00+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:47:21+00:00 opened https://github.com/joshmarcus/context-garden/pull/374 (base main): External manual completion now verifies immutable GitHub source and merge identities while supporting merge, squash, and rebase topologies. Final head fb14c0e72 passed 175 focused tests and repository-wide Ruff lint. cost=$2.62
- 2026-09-09T12:50:00+00:00 automated review requested changes: The rewritten-history verification works, but external PR claims can proceed after an inaccessible metadata lookup, bypassing immutable-head capture. cost=$0.36
- 2026-09-09T13:03:47+00:00 dispatched revise run 20260909T130344Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19879 tokens)
- 2026-09-09T13:09:03+00:00 preserved uncommitted worktree changes from run 20260909T130344Z-revise outside the PR: `git stash apply 66ed7ee67a59864d18dc70140d9cc0933fa20cce` in /home/joshua/work/worktrees/CG-476 (garden:CG-476:20260909T130344Z-revise:reap)
- 2026-09-09T13:09:03+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:10:23+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/374: External PR claims now require accessible, complete provider metadata before task or run state is created, preventing unpinned claims and moved-head bypasses. Commit 593e76d44 passed 68 focused scheduler tests and repository-wide Ruff lint. cost=$1.04
- 2026-09-09T13:20:19+00:00 automated review: approve — Verified external completion securely supports merge, squash, and rebase histories, including the claim-time metadata fix from the previous review. cost=$0.38
- 2026-09-09T13:22:01+00:00 CI failure
- 2026-09-09T13:38:18+00:00 dispatched revise run 20260909T133815Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~21400 tokens)
- 2026-09-09T13:41:56+00:00 preserved uncommitted worktree changes from run 20260909T133815Z-revise outside the PR: `git stash apply 20f519eb2627fe1ab82f62e40c870d3bc7e3136c` in /home/joshua/work/worktrees/CG-476 (garden:CG-476:20260909T133815Z-revise:reap)
- 2026-09-09T13:41:56+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:43:19+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/374: Updated the enterprise-host and stabilization integration fixtures to supply the immutable head, base, merge-commit, and successful fetch facts required by verified external completion. Commit 18add8c78 passed 70 focused tests and repository-wide Ruff lint. cost=$0.70
- 2026-09-09T13:46:10+00:00 automated review requested changes: Rewritten-history support works for the tested merge, squash, and rebase topologies, but a coincidental merge commit can still complete an external run. cost=$0.50
- 2026-09-09T13:46:23+00:00 dispatched revise run 20260909T134619Z-revise-2 via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20627 tokens)
- 2026-09-09T13:50:17+00:00 preserved uncommitted worktree changes from run 20260909T134619Z-revise-2 outside the PR: `git stash apply d6146c2bc539ef5aaff301ad97243210ba7e36ec` in /home/joshua/work/worktrees/CG-476 (garden:CG-476:20260909T134619Z-revise-2:reap)
- 2026-09-09T13:50:17+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:51:45+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/374: External manual completion now binds the immutable source head directly to GitHub's reported merge commit, rejecting coincidental commits even when both are independently present on the final base. Commit 110a91b2a passed all 69 focused scheduler-human tests, repository-wide Ruff lint, and diff validation. cost=$0.68
- 2026-09-09T14:10:36+00:00 automated review: approve — Verified external completion safely supports merge, squash, and rebase histories while rejecting mismatched provenance and preserving lifecycle evidence. cost=$0.35
- 2026-09-09T14:12:20+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T14:14:08+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/374
