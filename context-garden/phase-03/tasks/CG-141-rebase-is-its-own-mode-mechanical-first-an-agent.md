---
id: CG-141
title: 'Rebase is its own mode: mechanical first, an agent only for conflicts, no re-review when the diff
  is unchanged, a merge queue'
status: running
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 1
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/gitops.py
- src/garden/runs.py
- src/garden/cli.py
- docs/architecture.md
branch: garden/cg-141-rebase-is-its-own-mode-mechanical-first-an-agent
pr: https://github.com/joshmarcus/context-garden/pull/102
attempts: 2
last_dispatched_at: '2026-09-05T04:15:49+00:00'
created: '2026-09-05T02:17:26+00:00'
updated: '2026-09-05T04:15:49+00:00'
---

## Goal

A PR that falls behind main is brought forward by the cheapest thing that works, tracked as its own kind of run, and never re-reviewed for code the reviewer already approved. Automerge lands PRs through a queue, one at a time, so each PR is rebased once, right before it merges.

## Context

Measured at the end of the first live run. Since 20:00 on 2026-09-04: 52 merges, 24 rebase rounds ($37, $1.56 each), 82 review runs ($64), and thirteen "review cap" cards pressed by hand because each rebase ended in a fresh review of unchanged code. Today a rebase is a `revise` run: a full worker session with a ten- to fifteen-thousand-token brief that runs `git rebase`, and then a full review. Most of tonight's conflicts were two PRs appending to the same `elif` chain or the same test file.

Three parts. (1) `rebase` becomes a run mode with its own counter on the task, its own line in `garden metrics` (rebases per merge, rebase cost) and no effect on `max_revisions` or `review.max_rounds` (this absorbs the rebase half of CG-139). On a conflict the scheduler first tries `git rebase origin/main` in the worktree with no model; if it applies cleanly it pushes with a lease and re-runs the pre-PR checks, and that is the whole round. Only a textual conflict starts an agent, on the easy tier, with a brief that carries the conflicting hunks, the task's goal and the rule "resolve the conflict, change nothing else". (2) After any rebase, compute the diff against the new base and compare it with `last_diff_hash` from the reviewed push; when equal, keep the last verdict, log "rebased; diff unchanged; verdict kept", and dispatch no review. (3) Automerge becomes a queue: candidates are ordered (oldest approved first), and only the head is rebased, checked and merged; the next candidate is taken on the following poll. This replaces CG-138's one-per-cycle hold. Write the three rules into `docs/architecture.md` beside stacking, and make `garden runs` and the Runs page show the mode.

## Acceptance criteria

- [ ] a conflict that git resolves alone produces a `rebase` run record with no harness call, a lease push, and re-run checks; a test seeds a clean-rebase conflict.
- [ ] a textual conflict dispatches an easy-tier agent with only the hunks in its brief; a test seeds a real conflict.
- [ ] a rebase whose diff hash matches the reviewed one dispatches no review and keeps the verdict; the caps do not move.
- [ ] automerge merges the head of the queue only; two approved PRs land on consecutive polls, each rebased once.
- [ ] `garden metrics` prints rebases per merge and rebase cost.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)
- 2026-09-05T02:16:00+00:00 deferred by the feature freeze (2026-09-05): phase 03, after the split (CG-137); absorbs CG-138 and the rebase half of CG-139
- 2026-09-05T03:01:22+00:00 approved (web)
- 2026-09-05T03:02:04+00:00 dispatched work run 20260905T030155Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~12969 tokens)
- 2026-09-05T03:05:28+00:00 back to draft: approved by mistake during the phase 02 freeze; phase 03 work (CG-137 runs alone, first)
- 2026-09-05T03:19:58+00:00 approved (web)
- 2026-09-05T03:37:31+00:00 dispatched work run 20260905T033731Z-work via local [claude model=claude-opus-4-8] (fresh session, base garden/cg-137-split-the-scheduler-by-tick-phase-and-the-web-ac stacked on CG-137, ~10740 tokens)
- 2026-09-05T03:42:07+00:00 parent CG-137 merged; will rebase onto main when the current run finishes
- 2026-09-05T04:05:25+00:00 opened https://github.com/joshmarcus/context-garden/pull/102 (base garden/cg-137-split-the-scheduler-by-tick-phase-and-the-web-ac): Rebase is now its own run mode: mechanical rebase with no model first (a rebase run record, lease push, re-run checks), an easy-tier agent with only the hunks on a real textual conflict, no re-review when the rebased diff matches the reviewed hash, and automerge as a queue that rebases and merges one PR per tick. garden metrics reports rebases per merge and rebase cost. cost=$12.04
- 2026-09-05T04:05:29+00:00 parent CG-137 merged; rebased onto main and retargeted the PR
- 2026-09-05T04:10:01+00:00 automated review requested changes: The rebase mode, verdict-keep, merge queue and metrics are all implemented and covered by tests, but the delivered branch fails to collect its own test suite: test_rebase.py imports the removed wait_for_runs helper (CG-152's in-process runner deleted it), aborting all collection. The PR's '461 passed' claim is false as delivered. cost=$1.49
- 2026-09-05T04:15:49+00:00 dispatched revise run 20260905T041549Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~11848 tokens)
