---
id: CG-454
title: Skip destructive pre-merge rebase when the reviewed remote head is already current
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/scheduler/rebase.py
- src/garden/gitops.py
- tests/test_rebase.py
branch: codex/cg454-premerge-current-guard
pr: https://github.com/joshmarcus/context-garden/pull/348
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T23:19:13+00:00'
created: '2026-09-08T21:19:29+00:00'
updated: '2026-09-09T16:46:26+00:00'
---

## Goal

Prevent the pre-merge queue from rewriting a reviewed branch whose exact remote head is already based on the latest target and still has the reviewed diff.

## Context

At 2026-09-08 21:06 UTC, PR 342 at `68190007153c6655fa69f050217775f8e42ae839` was GitHub CLEAN/MERGEABLE with two passing CI runs and an approving review. `origin/main` at `020eced75890d243e61f2e9a045a7abba9461591` was already an ancestor through merge commit `2a482df12dd2565eb35f07b9a64b0c05f204279c`. `_rebase_and_record(..., skip_if_current=True)` nevertheless called `sync_and_rebase` before its current-head guard, flattened the intentional merge topology and manufactured conflicts in `tests/test_remote_worker.py` and `src/garden/web/actions/api.py`. The canonical branch/worktree remained clean at the reviewed head; operational recovery is separate.

Move the no-op proof before any history rewrite. It is valid only when the reviewed head equals the fetched remote branch head, the latest fetched base is an ancestor of that head, and the current branch diff still matches the reviewed diff. Any stale base, local/remote divergence, changed diff or missing provenance must continue through the normal rebase/conflict path. Never replace the existing lease-protected push rules with an unconditional force push.

## Acceptance criteria

- [ ] With `skip_if_current=True`, a branch whose exact reviewed head equals `origin/<branch>`, already contains the exact latest reviewed `origin/<base>`, and matches the diff captured on that review run returns `current` before `sync_and_rebase`; it creates no rebase run, push, conflict artifact or history rewrite. A stale `state.last_diff_hash` from a manual handoff cannot defeat this proof or authorize it.
- [ ] A merge commit whose second parent is the latest base is preserved byte-for-byte by the early no-op path, with a regression reproducing the PR 342 topology and conflicting-file setup.
- [ ] The guard fails closed when reviewed head provenance is missing or differs from the remote head, when the latest base is not an ancestor, when local and remote heads diverge, or when the diff hash changed; those cases still exercise the existing rebase/conflict and lease-protected push behavior.
- [ ] Focused tests cover the no-op and each divergence gate without contacting GitHub or force-pushing a shared branch.

## Out of scope

- Immediate PR 342 state recovery, deployment, publication and unrelated merge-queue policy.

## Log

- 2026-09-08T21:21:19+00:00 approved (cli)
- 2026-09-08T21:21:29+00:00 dispatched work run 20260908T212129Z-work via manual [human] (fresh session, base main, ~16227 tokens)
- 2026-09-08T22:08:06+00:00 fenced: Cannot verify this run's worktree fence; inspect protected paths before retrying. Restoration is unverified: fence manifest unavailable or invalid: trusted manifest reference missing or belongs to another run — worktree writes kept: src/garden/scheduler/rebase.py, src/garden/scheduler/review.py, tests/test_rebase.py.
- 2026-09-08T22:09:10+00:00 reset to ready by hand
- 2026-09-08T22:09:10+00:00 dispatched work run 20260908T220910Z-work via manual [human] (fresh session, base main, ~16894 tokens)
- 2026-09-08T22:09:11+00:00 external PR attached at codex/cg454-premerge-current-guard; existing CI is FAILURE
- 2026-09-08T22:15:07+00:00 CI failure
- 2026-09-08T22:16:29+00:00 automated review could not start: git worktree add /home/joshua/work/worktrees/CG-454 codex/cg454-premerge-current-guard (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/cg454-premerge-current-guard')
fatal: 'codex/cg454-premerge-current-guard' is already used by worktree at '/home/joshua/work/operator-test-tmp/cg454-rebase-current-sol'
- 2026-09-08T22:16:55+00:00 dispatched revise run 20260908T221655Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~17324 tokens)
- 2026-09-08T22:22:22+00:00 revision failed: could not materialise local worktree: git worktree add /home/joshua/work/worktrees/CG-454 codex/cg454-premerge-current-guard (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/cg454-premerge-current-guard')
fatal: 'codex/cg454-premerge-current-guard' is already used by worktree at '/home/joshua/work/operator-test-tmp/cg454-rebase-current-sol'
- 2026-09-08T22:28:44+00:00 re-enabled by hand; revise run will follow
- 2026-09-08T22:28:44+00:00 dispatched revise run 20260908T222844Z-revise via manual [human] (fresh session, base main, ~17456 tokens)
- 2026-09-08T22:28:45+00:00 external PR attached at codex/cg454-premerge-current-guard; existing CI is FAILURE
- 2026-09-08T22:46:40+00:00 automated review requested changes: The exact-head guard is fail-closed, runs before any destructive synchronization, and preserves reviewed merge topology. Focused tests, lint, and disposable served interaction pass on the reviewed SHA; the PR description rewrite adds phase context. cost=$0.43
- 2026-09-08T22:47:03+00:00 dispatched revise run 20260908T224702Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~17796 tokens)
- 2026-09-08T22:55:47+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/348: The pre-merge guard now proves the exact reviewed remote head is current before any synchronization can rewrite it, preserving reviewed merge topology and retaining lease-protected pushes for every divergent case. The existing committed change was validated with focused rebase and review suites, lint, and a disposable served-app check. cost=$0.54
- 2026-09-08T22:57:33+00:00 CI failure
- 2026-09-08T22:57:55+00:00 dispatched revise run 20260908T225755Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~17825 tokens)
- 2026-09-08T23:02:23+00:00 worker asks: Please provide the failed pytest node/log from Actions (or arrange an authenticated controller-side retry) so I can diagnose and fix the actual CI failure. cost=$0.36
- 2026-09-08T23:19:13+00:00 dispatched resume run 20260908T231913Z-resume via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~18180 tokens)
- 2026-09-08T23:26:45+00:00 automated review produced no verdict (idle 20 min (no output or file change))
- 2026-09-08T23:47:25+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/348: Added real completed review-run provenance to automerge and coordination fixtures so fail-closed exact-head validation permits their intended merge paths. Product source remains unchanged from the existing exact reviewed-head guard. cost=$0.42
- 2026-09-09T00:05:49+00:00 description rewritten by the reviewer cost=$0.56
- 2026-09-09T00:06:19+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T00:10:25+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T00:16:33+00:00 automated review clarification requested for ambiguous unverified observations
- 2026-09-09T00:19:31+00:00 reviewer clarification remained malformed or targeted requirements outside the frozen criteria and declared affected flow; operator review is required and no author revision was queued
- 2026-09-09T00:32:56+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/348
- 2026-09-09T16:46:26+00:00 automatic review recovery retired because task is done
