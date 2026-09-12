---
id: CG-391
title: Recognize CI-helper validation commands during onboarding discovery
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 8
difficulty: medium
reading:
- README.md
- docs/architecture.md
- docs/worker-protocol.md
- docs/roadmap.md
- src/garden/config.py
branch: garden/cg-391-recognize-ci-helper-validation-commands-during-o
pr: https://github.com/joshmarcus/context-garden/pull/357
discovered_from: CG-378
attempts: 1
last_dispatched_at: '2026-09-09T02:20:34+00:00'
created: '2026-09-07T18:43:36+00:00'
updated: '2026-09-09T16:46:25+00:00'
file: src/garden/onboard.py
error: _documented_commands ignores the documented CI helper and discovery falls back to pytest -q.
---

Onboarding's documented-command parser does not recognize python3 scripts/check_ci.py. After removing the obsolete README full-local-suite example, onboarding this repository selects the workflow's pytest -q step instead. Preserve intentional CI-offload workflows during discovery, including the required permission and credential context, rather than silently inferring a local full-suite command.

## Provenance

Discovered by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`.
## Log
- 2026-09-07T18:43:36+00:00 discovered by CG-378
- 2026-09-07T18:44:54+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:46:15+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:47:49+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:49:01+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:50:12+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:51:23+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:52:35+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:53:49+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:55:00+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:56:14+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:57:27+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:58:59+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:00:39+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:03:29+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:05:25+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:07:11+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:08:55+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:10:17+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:11:40+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:12:58+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:14:22+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:15:42+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:17:03+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:18:24+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:19:44+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:21:05+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:22:25+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:23:41+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:24:56+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:26:11+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:27:27+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:28:43+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:30:14+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:31:44+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:33:32+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:35:07+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:36:40+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:38:10+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:39:39+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:40:56+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:42:12+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:43:27+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:44:42+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:46:01+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`


## Acceptance criteria

- [ ] Recognize an explicitly documented CI-helper workflow without silently replacing it with a local full-suite command.
- [ ] Preserve push/auth requirements and require explicit configured authorization before running a helper that publishes a branch.
- [ ] Exercise discovery with a documented helper, ordinary local commands, unavailable credentials and ambiguous documentation; report ambiguity instead of inventing permission.
- 2026-09-07T20:06:51+00:00 approved (operator-owner-delegated)
- 2026-09-09T02:20:34+00:00 dispatched work run 20260909T022028Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~19610 tokens)
- 2026-09-09T02:26:52+00:00 preserved uncommitted worktree changes from run 20260909T022028Z-work outside the PR: `git stash apply a7d572c4f74242668f1ad8413188bceb1c7a4dd7` in /home/joshua/work/worktrees/CG-391 (garden:CG-391:20260909T022028Z-work:reap)
- 2026-09-09T02:26:53+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T02:28:45+00:00 opened https://github.com/joshmarcus/context-garden/pull/357 (base main): Onboarding now recognizes documented python3 scripts/check_ci.py helpers, reports ambiguous CI documentation, and prevents publishing helpers from running until worker push permission is explicitly configured. Verified with focused onboarding/worker-CI tests (60 passed) and clean ruff lint. cost=$1.02
- 2026-09-09T02:32:04+00:00 automated review: approve — The change preserves documented publishing CI helpers while withholding execution until worker push authorization is explicit; no blocking defects found. cost=$0.37
- 2026-09-09T02:37:07+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T02:38:11+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T02:46:21+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/357
- 2026-09-09T02:46:36+00:00 automated review could not start: CG-391 is done: #357 was merged at 02:46:21
- 2026-09-09T16:46:25+00:00 automatic review recovery retired because task is done
