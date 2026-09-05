---
id: CG-129
title: Automerge merges only into the product's base branch, never into a parent's branch
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/scheduler.py
- tests/test_automerge.py
- docs/architecture.md
branch: garden/cg-129-automerge-merges-only-into-the-product-s-base-br
attempts: 1
last_dispatched_at: '2026-09-05T00:45:27+00:00'
created: '2026-09-05T00:07:15+00:00'
updated: '2026-09-05T00:45:27+00:00'
---

## Goal

Automerge (CG-068) merges a PR only when its base is the product's base branch. A stacked child waits until its parent has merged and the child has been restacked onto main; it is never merged into the parent's branch.

## Context

Found in the first minutes of automerge on the first live run. #78 and #87 were stacked on CG-086's branch and #68 on CG-064's; all three passed every gate and automerge merged them into their parents' branches while both parents were in rebase rounds. A rebase round force-pushes the parent branch from the worker's worktree, which does not have those merge commits, so the children's work would have vanished from the branch while GitHub shows their PRs as merged. The person fast-forwarded CG-086's idle worktree by hand to keep them; CG-064's rebase was already running. Add the gate: `pr.base == product base branch`, with the reason "stacked on <parent>; waits for the restack" on the task page. Also make the restack path pull the remote parent branch before a rebase round when it has moved (someone merged into it), so a rebase never discards commits that only exist on the remote; if they conflict, the round resolves them like any conflict. Write both rules in `docs/architecture.md` next to stacking.

## Acceptance criteria

- [ ] a stacked PR with every other gate green is not automerged; the reason names the parent.
- [ ] after the parent merges and the child is restacked onto main, the child automerges on the next poll.
- [ ] a rebase round on a branch whose remote has extra commits keeps them; a test seeds a remote-only commit.

## Log

- 2026-09-05T00:45:27+00:00 dispatched work run 20260905T004518Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~8248 tokens)
