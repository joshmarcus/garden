---
id: CG-158
title: Manual tasks get a revise path, a reviewer that can see garden state, and a cost field on garden
  finish
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 3
difficulty: medium
reading: []
branch: garden/cg-158-manual-tasks-get-a-revise-path-a-reviewer-that-c
pr: https://github.com/joshmarcus/context-garden/pull/167
discovered_from: retro:context-garden/phase-02-friction
attempts: 1
last_dispatched_at: '2026-09-05T15:35:23+00:00'
created: '2026-09-05T03:14:37+00:00'
updated: '2026-09-05T16:35:50+00:00'
---

## Goal

Manual tasks get a revise path, a reviewer that can see garden state, and a cost field on garden finish.

## Context

From the phase-02 retro's open list (item 13), reconciled against what merged on 2026-09-05: "Manual tasks get no revise path and their reviewer cannot see garden state; garden finish has no cost field (CG-027)". See `../phase-02-friction/docs/retro.md` for the evidence and the persona reports under `../phase-02-friction/docs/reviews/`. Write the acceptance criteria when the task is planned.

## Acceptance criteria

- [ ] to be written at planning; the retro item above is the requirement.

## Log

- 2026-09-05T03:25:00+00:00 moved to phase-04: user-facing work, not structure
- 2026-09-05T03:15:00+00:00 filed from the phase-02 retro (open item 13)
- 2026-09-05T10:31:13+00:00 approved (web)
- 2026-09-05T13:07:16+00:00 dispatched work run 20260905T130707Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4380 tokens)
- 2026-09-05T13:12:47+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:14:44+00:00 dispatched work run 20260905T131444Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4481 tokens)
- 2026-09-05T13:16:00+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:33:45+00:00 reset to ready by hand
- 2026-09-05T14:34:00+00:00 dispatch failed: git merge --ff-only -q origin/main (in /home/joshua/work/worktrees/CG-158): error: Your local changes to the following files would be overwritten by merge:
	src/garden/scheduler/review.py
Please commit your changes or stash them before you merge.
Aborting
- 2026-09-05T15:10:26+00:00 reset to ready by hand
- 2026-09-05T15:20:20+00:00 dispatched work run 20260905T152020Z-work via local [codex] (fresh session, base main, ~4854 tokens)
- 2026-09-05T15:25:05+00:00 attempt 1 failed: worker exited 1: {'message': "You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 3:35 PM."}; will retry
- 2026-09-05T15:25:21+00:00 dispatch failed: git merge --ff-only -q origin/main (in /home/joshua/work/worktrees/CG-158): error: Your local changes to the following files would be overwritten by merge:
	src/garden/cli/loop.py
	tests/test_cli.py
Please commit your changes or stash them before you merge.
Aborting
- 2026-09-05T15:31:55+00:00 reset to ready by hand
- 2026-09-05T15:35:23+00:00 dispatched work run 20260905T153522Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~5044 tokens)
- 2026-09-05T15:59:23+00:00 opened https://github.com/joshmarcus/context-garden/pull/167 (base main): Manual tasks now get a revise path (the stuck-task audit flags a manual task waiting for a revise round instead of silently assuming the queue will pick it up, and dispatch clears the flag once taken), the automated reviewer now runs on a manual finish that has no local worktree (the common `garden take` flow), and `garden finish --cost` now records a manual round's cost through the same `run.cost_usd` field an automated worker populates. cost=$4.44
- 2026-09-05T16:00:57+00:00 automated review produced no verdict (worker error: success Not logged in · Please run /login) cost=$0.00
- 2026-09-05T16:31:18+00:00 automated review: approve — Diff matches the task exactly (8 files), all three gaps from the retro item are addressed and covered by new tests, full suite and lint pass, and the PR description is clean and reader-ready. cost=$0.53
- 2026-09-05T16:31:26+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T16:34:10+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-05T16:35:50+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/167
