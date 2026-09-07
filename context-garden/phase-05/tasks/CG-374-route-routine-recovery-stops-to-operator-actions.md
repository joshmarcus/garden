---
id: CG-374
title: Route routine recovery stops to operator actions instead of owner decisions
status: changes_requested
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
branch: garden/cg-374-route-routine-recovery-stops-to-operator-actions
attempts: 1
last_dispatched_at: '2026-09-07T09:36:06+00:00'
created: '2026-09-07T09:14:35+00:00'
updated: '2026-09-07T11:55:09+00:00'
---

## Goal

Route routine recovery stops to operator actions instead of owner decisions.

## Context

Owner queue audit found CG253/297/323/339 retry caps with actionable findings, CG329 missing CI, CG358 stale browser stop and CG295 asking to edit live config outside its checkout. Owner requested prevention tickets after resolving the human queue.

## Acceptance criteria

- [ ] Separate actionable technical recovery from decisions requiring owner preferences or authority; expose clear reason and next action.
- [ ] With delegated recovery authority, enqueue one bounded continuation retaining feedback and PR identity; enforce resource admission and stop repeated unchanged failures.
- [ ] Preflight task scope against checkout ownership; split operator-owned config steps and accept verified operator evidence without granting workers production-write access.
- [ ] Regression coverage includes retry caps with feedback, missing CI, stale infrastructure prerequisites and mixed product/live-config deliverables; none produces an unexplained owner card.

## Log

- 2026-09-07T09:14:36+00:00 approved (web)
- 2026-09-07T09:36:06+00:00 dispatched work run 20260907T093540Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9003 tokens)
- 2026-09-07T10:03:24+00:00 preserved uncommitted worktree changes from run 20260907T093540Z-work outside the PR: `git stash apply a3e1b9c66f3cddbfab8c9babec3fe8107116c5b1` in /home/joshua/work/worktrees/CG-374 (garden:CG-374:20260907T093540Z-work:reap)
- 2026-09-07T10:08:10+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:09:46+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:11:32+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:13:02+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:14:31+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:15:57+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:17:30+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:18:51+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:20:25+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:22:17+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:24:38+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:26:40+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:29:24+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:32:12+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:34:43+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:38:20+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:42:27+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:46:53+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:50:38+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:53:21+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:55:21+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:57:20+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:58:38+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T10:59:51+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:01:11+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:02:31+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:03:47+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:05:00+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:06:15+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:07:34+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:08:47+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:10:07+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:11:26+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:12:39+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:13:53+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:15:21+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:17:06+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:19:04+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:21:01+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:23:00+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:24:59+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:26:34+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:27:47+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:29:00+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:30:13+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:31:29+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:32:42+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:33:56+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:35:09+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:36:29+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:37:42+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:39:01+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:40:12+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:41:31+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:42:42+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:44:08+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:45:21+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:46:13+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:46:15+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:47:27+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:48:39+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:49:50+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human

- 2026-09-07T11:51:02+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:52:14+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:53:26+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
- 2026-09-07T11:54:37+00:00 check did not run (20260907T100635Z-check): no check result; retry also failed; needs human
