---
id: CG-109
title: A description-only revise round runs on the easy tier
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/review.py
- src/garden/harness.py
branch: garden/cg-109-a-description-only-revise-round-runs-on-the-easy
pr: https://github.com/joshmarcus/context-garden/pull/80
attempts: 1
last_dispatched_at: '2026-09-05T01:16:55+00:00'
created: '2026-09-04T21:23:07+00:00'
updated: '2026-09-05T01:16:55+00:00'
---

## Goal

When a review's only finding is the PR description, the revise round runs on the easy tier, whatever the task's difficulty.

## Context

Found on the first live run. CG-081's review (PR #48) said the code was correct and well tested and asked only for the description to change (`description_ok: false`, no code findings); the revise round went out on the medium tier (opus 4.8) with a 13k-token brief, which is what a rewrite of a paragraph costs at that tier several times over. The review result already distinguishes description findings from code findings (CG-038 uses the same distinction for the stall check). At dispatch of a revise round, if `pending_feedback` has no code findings, pick the easy tier's model and say so in the dispatch note ("description only; easy tier"). A round with any code finding keeps the task's tier. Trials and persona reviews are unaffected.

## Acceptance criteria

- [ ] a description-only round dispatches on the easy tier's model and the note says why.
- [ ] a round with a code finding keeps the task's tier.
- [ ] a test with the fake harness for both.

## Log

- 2026-09-04T23:10:00+00:00 dispatched work run 20260904T230951Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~6850 tokens)
- 2026-09-04T23:17:38+00:00 opened https://github.com/joshmarcus/context-garden/pull/80 (base main): Revise rounds triggered by a description-only automated review (no blocking findings) now dispatch on the harness's easy tier with a note explaining why; any blocking finding still keeps the task's own tier. Added fake-harness tests for both paths. cost=$4.33
- 2026-09-04T23:19:43+00:00 automated review: approve — Meets all three acceptance criteria with tests for both paths; the description-only easy-tier routing is correct and the pending_feedback_easy flag is cleared at every site that sets or empties pending_feedback, so it can't leak. Description and diff are clean. cost=$0.65
- 2026-09-04T23:59:52+00:00 PR conflicts with main (tests/fake_claude.py); revise run will rebase and resolve
- 2026-09-04T23:59:56+00:00 dispatched revise run 20260904T235956Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~7517 tokens)
- 2026-09-05T00:03:58+00:00 pre-PR checks failed (test); revise run will fix before the PR is updated cost=$1.40
- 2026-09-05T00:20:46+00:00 revision counter reset (web)
- 2026-09-05T00:20:46+00:00 triage: marked ready for review
- 2026-09-05T01:11:57+00:00 PR conflicts with main (src/garden/scheduler.py); revise run will rebase and resolve
- 2026-09-05T01:12:08+00:00 dispatched revise run 20260905T011207Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~8067 tokens)
- 2026-09-05T01:16:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/80: Rebased the branch onto origin/main, resolving the conflict in src/garden/scheduler.py by keeping main's refactored _handle_failed_checks/_start_check_revise split and adding the pending_feedback_easy reset to the new single call site. Tests (380 passed, 3 skipped) and ruff both pass. cost=$1.16
- 2026-09-05T01:16:49+00:00 PR conflicts with main (tests/fake_claude.py, tests/test_review.py); revise run will rebase and resolve
- 2026-09-05T01:16:55+00:00 dispatched revise run 20260905T011654Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~8514 tokens)
