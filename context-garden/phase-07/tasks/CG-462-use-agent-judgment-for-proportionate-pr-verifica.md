---
id: CG-462
title: Use agent judgment for proportionate PR verification
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/review.py
- src/garden/preflight.py
- src/garden/brief.py
- src/garden/scheduler/review.py
- src/garden/scheduler/checkruns.py
- src/garden/scheduler/poll.py
- tests/test_review.py
branch: codex/cg462-reviewer-judgment
pr: https://github.com/joshmarcus/context-garden/pull/355
runner: manual
attempts: 1
last_dispatched_at: '2026-09-09T01:44:49+00:00'
created: '2026-09-09T00:41:56+00:00'
updated: '2026-09-09T16:46:26+00:00'
---

The owner explicitly says that many current requirements are inappropriate for all PRs, names Running-app evidence incomplete as an example, requests thoroughly relaxing PR requirements, and says to let reviewers supply appropriate evidence or attest to testing and let agents judge for themselves. Implement that discretion throughout review admission, briefing, verdict handling, and merge eligibility, using the current principles policy as the contract. Preserve existing results and actual correctness failures; do not force unchanged source revisions just to fill evidence templates.

## Acceptance criteria

- [ ] A worker or reviewer can choose proportionate checks or provide a clear honest attestation of what was tested or inspected. A useful non-UI, parser/configuration, CLI, build, test, or refactor PR does not require a running HTTP app, screenshots, a generic replay, empty/failure/recovery matrices, load measurements, prescribed artifact fields, or cosmetic PR-description changes merely because a broad path or keyword matched.
- [ ] Review admission, prompts, result parsing, reaping, and merge gates consistently treat optional evidence forms and checklist/style omissions as advisory. Reviewer-selected relevant evidence remains usable; explicit real defects, failed applicable checks, contradictory source/result claims, and unmet functional outcomes remain actionable. Preserve existing actual results and safely account for old queued/terminal evidence-only continuations rather than inventing approvals or reopening merged work.
- [ ] Bounded meaningful regressions demonstrate agent-approved attestation/test-only PR progression, applicable UI verification chosen by the reviewer, optional missing fields/captures/style without a forced revision, and retention of real bug/check failures. Reviewers choose the verification method; this task itself does not require a prescribed running-app manifest. Keep exact-head CI and versioned deployment gates intact.

## Log

- 2026-09-09T00:41:56+00:00 approved (explicit owner instruction to relax PR requirements and trust agent judgment)
- 2026-09-09T01:44:49+00:00 dispatched work run 20260909T014449Z-work via manual [human] (fresh session, base main, ~13128 tokens)
- 2026-09-09T01:44:50+00:00 external PR attached at codex/cg462-reviewer-judgment; existing CI is FAILURE
- 2026-09-09T01:45:36+00:00 PR conflicts with main; rebase onto main conflicts (git worktree add /home/joshua/work/worktrees/CG-462 codex/cg462-reviewer-judgment (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/cg462-reviewer-judgment')
fatal: 'codex/cg462-reviewer-judgment' is already used by worktree at '/home/joshua/work/manual/CG-462'); a rebase agent will resolve it
- 2026-09-09T02:12:24+00:00 automated review could not start: git worktree add /home/joshua/work/worktrees/CG-462 codex/cg462-reviewer-judgment (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/cg462-reviewer-judgment')
fatal: 'codex/cg462-reviewer-judgment' is already used by worktree at '/home/joshua/work/manual/CG-462'
- 2026-09-09T02:12:24+00:00 automatic review recovery 1/2 queued for the current head: startup failed: git worktree add /home/joshua/work/worktrees/CG-462 codex/cg462-reviewer-judgment (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/cg462-reviewer-judgment')
fatal: 'codex/cg462-reviewer-judgment' is already used by worktree at '/home/joshua/work/manual/CG-462'
- 2026-09-09T02:32:35+00:00 automated review could not start: git worktree add /home/joshua/work/worktrees/CG-462 codex/cg462-reviewer-judgment (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/cg462-reviewer-judgment')
fatal: 'codex/cg462-reviewer-judgment' is already used by worktree at '/home/joshua/work/manual/CG-462'
- 2026-09-09T02:32:35+00:00 automatic review recovery 2/2 queued for the current head: startup failed: git worktree add /home/joshua/work/worktrees/CG-462 codex/cg462-reviewer-judgment (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/cg462-reviewer-judgment')
fatal: 'codex/cg462-reviewer-judgment' is already used by worktree at '/home/joshua/work/manual/CG-462'
- 2026-09-09T02:41:08+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/355
- 2026-09-09T02:53:19+00:00 automated review could not start: CG-462 is done: #355 was merged at 02:41:08
- 2026-09-09T16:46:26+00:00 automatic review recovery retired because task is done
