---
id: CG-064
title: Make test_feedback_triggers_revise_round deterministic
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- tests/test_scheduler.py
- tests/conftest.py
- tests/fake_claude.py
branch: garden/cg-064-make-test-feedback-triggers-revise-round-determi
pr: https://github.com/joshmarcus/context-garden/pull/64
attempts: 1
last_dispatched_at: '2026-09-05T00:19:31+00:00'
created: '2026-09-04T18:24:37+00:00'
updated: '2026-09-05T00:29:06+00:00'
---

## Goal

`tests/test_scheduler.py::test_feedback_triggers_revise_round` passes every time, on GitHub Actions and under local load, and the cause of its intermittent second PR is understood and removed.

## Context

Failed twice on 2026-09-04: once as a pre-PR check while two other workers loaded the machine, once on GitHub Actions for PR #29 (a change to brief wording, nowhere near this path), with `assert len(fake_github.created) == 1` seeing 2. It passed 36 of 36 local runs in three parallel streams and in the eleven other CI runs that day, so it is timing. The likely seam: `wait_for_runs` returns when every active run has an `exit_code`, but the reap of the revise run must find the existing PR through `find_pr(slug, branch)` on the fake; if the run record or the task's branch is read before the fake worker's commit lands, or two ticks overlap on the run directory, `finalize` takes the open-a-new-PR path. Reproduce by adding jitter to the fake harness (sleep before writing stdout and exit_code) and by running the test under `pytest -p xdist`-style load, then fix the real race in `finalize` or the fake, not the assertion.

## Acceptance criteria

- [ ] the cause is named in the PR and covered by a test that fails before the fix under injected delay.
- [ ] 50 consecutive local runs pass under load; CI is green.

## Log

- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T21:44:53+00:00 priority 2 -> 0
- 2026-09-04T22:03:05+00:00 dispatched work run 20260904T220305Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~10054 tokens)
- 2026-09-04T22:31:46+00:00 opened https://github.com/joshmarcus/context-garden/pull/64 (base main): Found the real cause of the flake (a byte-identical commit collision between a stacked child's work run and its parent's revise commit, not a finalize()/find_pr race as hypothesized), fixed it in the fake harness, rescoped the test's assertion to what it actually intends to check, and added a deterministic regression test. cost=$11.12
- 2026-09-04T22:34:29+00:00 automated review: approve — Correctly identifies and fixes a byte-identical-commit collision in the fake harness (independently reproduced) as the real cause of the flake, with a deterministic regression test and a legitimate assertion rescoping. Both acceptance criteria met; 50/50 local runs clean. cost=$0.74
- 2026-09-05T00:02:12+00:00 PR conflicts with main (tests/test_scheduler.py); revise run will rebase and resolve
- 2026-09-05T00:02:27+00:00 dispatched revise run 20260905T000226Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~12723 tokens)
- 2026-09-05T00:07:34+00:00 pre-PR checks failed (test); revise run will fix before the PR is updated cost=$1.68
- 2026-09-05T00:07:56+00:00 dispatched revise run 20260905T000755Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~8802 tokens)
- 2026-09-05T00:12:16+00:00 worker says nothing to change: The failing pre-PR check is an unrelated, pre-existing bug on main (already tracked as CG-127), not caused by or fixable within this diff. Reproduced the identical failure on the exact base commit via a scratch worktree; this branch's own acceptance criteria (deterministic test_feedback_triggers_revise_round, 50/50 local runs, regression test for the real collision cause) are already met from the prior commit. cost=$1.42
- 2026-09-05T00:19:07+00:00 no-change accepted by the person (accepted: the failing check was CG-127's bug on main, fixed by #89; main is green); resuming the round without a new work run
- 2026-09-05T00:19:20+00:00 pre-PR checks failed (test); revise run will fix before the PR is updated
- 2026-09-05T00:19:31+00:00 dispatched revise run 20260905T001931Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~9054 tokens)
- 2026-09-05T00:24:42+00:00 push failed: git push -u origin HEAD:refs/heads/garden/cg-064-make-test-feedback-triggers-revise-round-determi (in /home/joshua/work/worktrees/CG-064): To https://github.com/joshmarcus/context-garden.git
 ! [rejected]        HEAD -> garden/cg-064-make-test-feedback-triggers-revise-round-determi (non-fast-forward)
error: failed to push some refs to 'https://github.com/joshmarcus/context-garden.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details. cost=$1.12
- 2026-09-05T00:26:49+00:00 triage: marked ready for review
- 2026-09-05T00:29:06+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/64
