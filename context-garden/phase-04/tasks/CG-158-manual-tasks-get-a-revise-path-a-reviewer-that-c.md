---
id: CG-158
title: Manual tasks get a revise path, a reviewer that can see garden state, and a cost field on garden
  finish
status: running
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 3
difficulty: medium
reading: []
branch: garden/cg-158-manual-tasks-get-a-revise-path-a-reviewer-that-c
harness: codex
discovered_from: retro:context-garden/phase-02-friction
attempts: 1
last_dispatched_at: '2026-09-05T15:20:20+00:00'
created: '2026-09-05T03:14:37+00:00'
updated: '2026-09-05T15:20:20+00:00'
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
