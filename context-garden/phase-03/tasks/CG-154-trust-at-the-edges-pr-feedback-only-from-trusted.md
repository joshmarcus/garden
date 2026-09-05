---
id: CG-154
title: 'Trust at the edges: PR feedback only from trusted authors, a scrubbed worker environment, sanitised
  HTML and an origin check on POSTs'
status: done
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 1
difficulty: hard
reading: []
branch: garden/cg-154-trust-at-the-edges-pr-feedback-only-from-trusted
pr: https://github.com/joshmarcus/context-garden/pull/101
discovered_from: retro:context-garden/phase-02-friction
attempts: 1
last_dispatched_at: '2026-09-05T04:42:50+00:00'
created: '2026-09-05T03:14:37+00:00'
updated: '2026-09-05T04:52:54+00:00'
---

## Goal

Trust at the edges: PR feedback only from trusted authors, a scrubbed worker environment, sanitised HTML and an origin check on POSTs.

## Context

From the phase-02 retro's open list (item 7), reconciled against what merged on 2026-09-05: "Feedback from any PR commenter becomes a worker prompt; workers inherit full credentials; raw HTML rendering and no origin check on POSTs". See `../phase-02-friction/docs/retro.md` for the evidence and the persona reports under `../phase-02-friction/docs/reviews/`. Write the acceptance criteria when the task is planned.

## Acceptance criteria

- [ ] to be written at planning; the retro item above is the requirement.

## Log
- 2026-09-05T03:15:00+00:00 filed from the phase-02 retro (open item 7)
- 2026-09-05T03:20:00+00:00 approved (web)
- 2026-09-05T03:47:37+00:00 dispatched work run 20260905T034729Z-work via local [claude model=claude-fable-5-1] (fresh session, base main, ~3732 tokens)
- 2026-09-05T04:01:03+00:00 discovered work filed: CG-164, CG-165
- 2026-09-05T04:02:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/101 (base main): PR feedback becomes a worker prompt only from trusted authors; workers and their setup command run in an allowlisted environment; the web UI sanitises every rendered markdown block and refuses cross-origin POSTs. Three commits, 469 tests green, ruff clean. cost=$8.53
- 2026-09-05T04:02:11+00:00 PR conflicts with main (src/garden/runner/local.py); revise run will rebase and resolve
- 2026-09-05T04:05:30+00:00 automated review: approve — All three trust items (trusted-author feedback, scrubbed worker env, sanitised HTML + origin check) are implemented, well-tested, and cleanly scoped; targeted tests and ruff pass. Description meets the standard. cost=$0.96
- 2026-09-05T04:05:35+00:00 dispatched revise run 20260905T040535Z-revise via local [claude model=claude-fable-5-1] (fresh session, base main, ~4315 tokens)
- 2026-09-05T04:10:01+00:00 discovered work filed: CG-167
- 2026-09-05T04:10:55+00:00 base branch `main` is itself broken — pre-PR check(s) test, lint fail at its own commit 55a935290123, not because of this branch; waiting for the base to go green, no revise round cost=$1.94
- 2026-09-05T04:20:19+00:00 nothing to fix; resumed to in review by hand
- 2026-09-05T04:34:33+00:00 PR conflicts with main (src/garden/web/app.py); revise run will rebase and resolve
- 2026-09-05T04:42:50+00:00 dispatched revise run 20260905T044250Z-revise via local [claude model=claude-fable-5-1] (fresh session, base main, ~4489 tokens)
- 2026-09-05T04:46:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/101: Rebased the branch onto origin/main and resolved the one conflict in src/garden/web/app.py by keeping both the origin-check middleware and main's github stand-in plus app.state.hub. 507 tests pass and ruff is clean; nothing on main overlaps with this branch, so the PR description is unchanged. cost=$0.61
- 2026-09-05T04:50:30+00:00 description rewritten by the reviewer cost=$0.93
- 2026-09-05T04:52:54+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/101
