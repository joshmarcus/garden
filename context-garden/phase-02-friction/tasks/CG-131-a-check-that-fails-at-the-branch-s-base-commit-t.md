---
id: CG-131
title: A check that fails at the branch's base commit triggers a rebase, not a revise round
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/checks.py
- src/garden/gitops.py
branch: garden/cg-131-a-check-that-fails-at-the-branch-s-base-commit-t
pr: https://github.com/joshmarcus/context-garden/pull/92
attempts: 1
last_dispatched_at: '2026-09-05T00:49:59+00:00'
created: '2026-09-05T00:21:13+00:00'
updated: '2026-09-05T01:10:46+00:00'
---

## Goal

When a pre-PR check fails and the same check also fails at the branch's base commit, the loop treats it as a stale base, not as the worker's fault: if the product's base branch has moved, it rebases the branch onto it and re-runs the checks; only if the check still fails after that does a revise round start. A worker's "nothing to change" on such a round leads to the same rebase, never to a repeat of the failing check on the old base.

## Context

Found on the first live run. Main was red for twenty minutes (CG-127) and every rebased branch failed its pre-PR test check on a test it had not touched. Each spent a revise round ($1 to $3) to discover that; several reported "nothing to change" (CG-100's path, which worked), the person accepted, and the accept re-ran the checks on the same stale base, so CG-062 failed again and hit the revision cap. After main went green nothing rebased the branches, because the loop rebases only on conflicts. The person rebased the idle ones by hand. Add a base-commit probe when a check fails: run the failing check at the merge base (in the worktree at a temporary detached checkout, or in the product clone), and if it fails there too, log "fails at base <sha>; not this branch"; then, if the base branch has moved since dispatch, rebase and re-run; else open a card that says main itself is broken and name the failing check, and do not start a revise round. Accepting a "nothing to change" card follows the same path.

## Acceptance criteria

- [ ] a check that fails at both the branch and its base does not start a revise round; the log names the base commit.
- [ ] when the base branch has moved, the branch is rebased and the checks re-run without a worker; a test seeds a red base that turns green.
- [ ] when main itself is red, the Inbox card says so and names the check; the task waits without spending.

## Log

- 2026-09-05T00:49:59+00:00 dispatched work run 20260905T004950Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~7718 tokens)
- 2026-09-05T01:04:20+00:00 opened https://github.com/joshmarcus/context-garden/pull/92 (base main): A failing pre-PR check now probes the branch's base commit: if it fails there too the loop rebases a moved/green base and re-runs without a worker, or parks the task on a 'base broken' card that names the check and commit — never a revise round on a stale/red base. Accepting a no_change card follows the same path. cost=$4.85
- 2026-09-05T01:07:32+00:00 automated review: approve — Base-probe on a failing pre-PR check is correct and well-tested: all three acceptance criteria are met with passing tests, scope is tight, and the description is clean and complete. cost=$0.95
- 2026-09-05T01:10:46+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/92
