---
id: CG-210
title: 'The pre-merge rebase keeps the verdict when the PR''s own patch is unchanged: compare git patch-ids,
  not diff hashes, so a rebase onto a moved main never forces a re-review'
status: ready
product: context-garden
phase: phase-04
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/scheduler/rebase.py
- src/garden/scheduler/reap.py
- src/garden/gitops.py
- tests/test_rebase.py
created: '2026-09-05T13:02:16+00:00'
updated: '2026-09-05T13:02:16+00:00'
---

## Goal

A mechanical rebase that does not change what the PR itself does keeps the approve verdict. "Unchanged" is judged by `git patch-id --stable` over `git diff <merge-base>..<head>` before and after the rebase (or by comparing the rebased commits' patch ids), not by a hash of the diff text, whose hunk headers and context lines move whenever the base moves.

## Context

Phase 04, 2026-09-05 12:39 to 12:58: with twelve approved, green PRs queued, every head the queue rebased came back `diff_unchanged: false`, `verdict_kept: false`, so the queue asked for another review; after two rounds the review cap put a card on the task. CG-132 went approve (12:39) → rebase CHANGED → cap (12:55); CG-156 went approve (12:52) → rebase CHANGED → cap (12:57). None of those rebases had a conflict or touched the PR's own changes; main had moved by other PRs' merges in the same files, which shifts context lines and `@@` offsets in the diff text. Each merge therefore invalidated every other queued verdict: a review per merge per PR, and a card each, so the queue could not drain without a hand. The operator merged the approved set by hand with a scratch-merge check. CG-141 introduced verdict-keep; CG-176 keeps the head; this fixes the comparison they rely on.

## Acceptance criteria

- [ ] `gitops.patch_id(worktree, base)` returns the stable patch id of the branch's diff against its merge base; the pre-merge rebase (and the stale-base rebase) compares patch ids before and after and keeps the verdict when they match.
- [ ] A test rebases a branch onto a main whose merge added lines next to the branch's hunk and sees `verdict_kept: true`; a test where the rebase changes the branch's own lines sees `verdict_kept: false`.
- [ ] The `rebase` event carries `patch_id_before`, `patch_id_after` and `verdict_kept`.
- [ ] Rebase rounds that keep the verdict do not count toward `review.max_rounds`.

## Log

- 2026-09-05T13:02:16+00:00 approved (web)
