---
id: CG-037
title: Stop the revise template and the review prompt contradicting each other
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/brief.py
- src/garden/review.py
branch: garden/cg-037-stop-the-revise-template-and-the-review-prompt-c
pr: https://github.com/joshmarcus/context-garden/pull/44
discovered_from: CG-027
attempts: 1
last_dispatched_at: '2026-09-04T21:21:41+00:00'
created: '2026-09-04T17:03:10+00:00'
updated: '2026-09-04T21:24:14+00:00'
---

## Goal

A revised PR does not fail its next review because of something the revise brief told the worker to write.

## Context

`brief.py` (revise section) says: reply to each review point in `pr_body` under a "Review responses" heading. `review.py` says the description must have no scar tissue and no references to earlier review rounds. On CG-027 review round two requested changes for exactly that heading, which cost a revise run and then a false stall. Decide where review responses go (a PR comment is the obvious place, since the scheduler already comments on each push) and make both prompts agree.

## Acceptance criteria

- [ ] the revise brief no longer asks for a section in the PR body that the review prompt forbids.
- [ ] responses to feedback still reach the reviewer (comment or otherwise) and a test shows where.

## Provenance

Discovered by CG-027 (First live run of the loop on itself) during run `20260904T160635Z-work`.

## Log

- 2026-09-04T17:03:10+00:00 discovered by CG-027
- 2026-09-04T17:23:52+00:00 approved (web)
- 2026-09-04T17:24:47+00:00 dispatched work run 20260904T172447Z-work via local [claude model=haiku] (fresh session, base main, ~6176 tokens)
- 2026-09-04T17:29:49+00:00 attempt 1 failed: worker exited 1: worker error: error_max_turns; will retry
- 2026-09-04T17:30:41+00:00 dispatched work run 20260904T173040Z-work via local [claude model=haiku] (fresh session, base main, ~6237 tokens)
- 2026-09-04T17:36:03+00:00 no active run found; back to ready
- 2026-09-04T17:36:39+00:00 dispatched work run 20260904T173639Z-work via local [claude model=sonnet] (fresh session, base main, ~6511 tokens)
- 2026-09-04T17:40:26+00:00 attempt 3 failed: no GARDEN_RESULT in worker output (see final.md); giving up
- 2026-09-04T18:47:54+00:00 reset to ready by hand
- 2026-09-04T20:01:59+00:00 dispatched work run 20260904T200159Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~7485 tokens)
- 2026-09-04T20:09:34+00:00 opened https://github.com/joshmarcus/context-garden/pull/44 (base main): The fix was already committed by a prior attempt that failed only because it omitted the GARDEN_RESULT marker; verified both acceptance criteria are met and the full test suite (114 passed) and lint pass cleanly. cost=$2.78
- 2026-09-04T20:10:39+00:00 automated review: approve — The revise brief and review prompt now agree: review responses go in a pr_comment (posted by the scheduler on revision pushes) instead of the PR body, with a test that asserts the comment is posted. Both acceptance criteria are met; tests and lint pass; scope and description are clean. cost=$0.47
- 2026-09-04T20:12:47+00:00 2 new review item(s)
- 2026-09-04T20:55:50+00:00 dispatched revise run 20260904T205549Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~7561 tokens)
- 2026-09-04T20:57:53+00:00 pre-PR checks failed (tests, lint); revise run will fix before the PR is updated cost=$1.41
- 2026-09-04T20:57:54+00:00 dispatched revise run 20260904T205753Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~7373 tokens)
- 2026-09-04T21:02:12+00:00 discovered work filed: CG-095
- 2026-09-04T21:02:35+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/44: Verified the existing branch already satisfies both acceptance criteria: the revise brief points reviewers' responses to pr_comment instead of pr_body, and a test confirms both that the comment posts and that the next automated review brief includes it. Full suite (114 passed, 3 skipped) and lint pass cleanly in this worktree; no new code changes were needed this round. cost=$1.70
- 2026-09-04T21:02:37+00:00 PR conflicts with main (src/garden/scheduler.py); revise run will rebase and resolve
- 2026-09-04T21:03:40+00:00 dispatched revise run 20260904T210339Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~7564 tokens)
- 2026-09-04T21:06:46+00:00 pre-PR checks failed (tests); revise run will fix before the PR is updated cost=$1.10
- 2026-09-04T21:07:49+00:00 automated review: request_changes — Code and tests correctly resolve the contradiction (pr_comment replaces the forbidden body heading, is posted as a comment, and is threaded into the next review brief; both acceptance criteria met, full suite and lint green). The only blocker is the PR description itself, which carries a '## Review responses' section — the exact scar tissue this change removes. cost=$0.53
- 2026-09-04T21:19:41+00:00 revision counter reset (web)
- 2026-09-04T21:19:42+00:00 triage: changes requested by hand: The tests check failed because of the garden's environment (a sentinel GARDEN_ROOT reached the pytest subprocess); that
- 2026-09-04T21:21:41+00:00 dispatched revise run 20260904T212141Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~8600 tokens)
- 2026-09-04T21:24:14+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/44: No code changes needed this round: the pre-PR test failures were caused by the runner's GARDEN_ROOT sentinel leaking into the pytest subprocess (confirmed by re-running with it unset: 219 passed, 3 skipped), and lint is clean. Fixed the PR description to drop the '## Review responses' heading that the automated review flagged as scar tissue, moving that reply into a pr_comment instead, consistent with the pr_comment mechanism this branch already ships. cost=$0.64
