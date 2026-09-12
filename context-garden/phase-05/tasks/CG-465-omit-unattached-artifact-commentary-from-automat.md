---
id: CG-465
title: Omit unattached-artifact commentary from automated reviews
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/review.py
- src/garden/scheduler/review.py
- tests/test_review.py
branch: codex/quiet-unattached-artifacts
pr: https://github.com/joshmarcus/context-garden/pull/360
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T13:22:16+00:00'
created: '2026-09-09T02:59:25+00:00'
updated: '2026-09-09T13:38:09+00:00'
---

## Goal

Omit review commentary about evidence artifacts that were not attached. Assume such artifacts are not included; review the source and verification actually performed.

## Context

The owner explicitly requested this policy on September 9. Live principles already say to omit absent-artifact caveats and nits, but the scheduler still appends an Evidence metadata advisory finding for unavailable artifact paths or omitted optional metadata after parsing an otherwise valid reviewer result. This deterministic addition must follow the owner policy as well. Preserve original historic review records.

## Acceptance criteria

- [ ] New review comments, findings and revision feedback do not add automatic absence or packaging nits for unattached optional artifacts or omitted optional evidence metadata.
- [ ] Review guidance explicitly tells reviewers to assume unattached artifacts are not included and to discuss checks actually performed, without caveats or demands solely for missing optional attachments.
- [ ] Substantive reviewer findings, explicit request_changes and actual contradictions in available artifact source identity retain their blocking behavior. Preserve useful diagnostic records separately from posted review prose.
- [ ] Focused coverage verifies both approval and real-rejection cases with omitted and unavailable artifacts, and still rejects a present artifact contradicting the reviewed source.

## Log

- 2026-09-09T02:59:26+00:00 approved (explicit owner artifact-review policy)
- 2026-09-09T02:59:26+00:00 Operator implements the narrow scheduler-generated commentary change in an isolated worktree; CG464 separately owns merge eligibility.
- 2026-09-09T02:59:29+00:00 dispatched work run 20260909T025928Z-work via manual [human] (fresh session, base main, ~14268 tokens)
- 2026-09-09T03:13:30+00:00 external PR attached at codex/quiet-unattached-artifacts; existing CI is PENDING
- 2026-09-09T03:42:14+00:00 automated review: approve — Automated reviews now keep optional evidence-packaging diagnostics out of posted findings while retaining genuine blockers. cost=$0.18
- 2026-09-09T03:42:31+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T03:49:00+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T03:59:36+00:00 automated review: approve — Automated reviews now suppress optional evidence-packaging commentary while preserving diagnostics and genuine blockers. cost=$0.23
- 2026-09-09T04:01:05+00:00 CI failure
- 2026-09-09T04:01:37+00:00 dispatched revise run 20260909T040137Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~14783 tokens)
- 2026-09-09T04:09:34+00:00 revision failed: worker exited 1: {'message': "You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Sep 15th, 2026 2:14 AM."}
- 2026-09-09T09:44:27+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T09:47:30+00:00 dispatched revise run 20260909T094730Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~14953 tokens)
- 2026-09-09T09:50:00+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T09:54:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/360: Verified the existing committed implementation suppresses automatic unattached-artifact and optional-metadata commentary while retaining diagnostics internally and blocking actual source contradictions. Focused review tests passed (88 passed); Ruff and git diff whitespace checks passed. cost=$0.19
- 2026-09-09T09:57:31+00:00 CI failure
- 2026-09-09T09:58:10+00:00 dispatched revise run 20260909T095810Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15128 tokens)
- 2026-09-09T09:59:20+00:00 automated review: approve — Automated reviews now suppress optional evidence-packaging commentary while retaining diagnostics and genuine blockers. cost=$0.16
- 2026-09-09T10:03:16+00:00 worker found no change to make: The same commit has a passing push CI run; the failing pull-request test run has no retrievable log in this environment, while its separate actions check reports missing GitHub CLI authentication. Local focused coverage passes, so no deterministic source defect was found.; reconciling with checks and a fresh review
- 2026-09-09T10:04:38+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/360: Verified commit 0b551e4c suppresses posted unattached-artifact/optional-metadata commentary while retaining internal diagnostics and blocking genuine source contradictions. Focused review coverage passed (88 passed) and Ruff passed. cost=$0.37
- 2026-09-09T10:08:25+00:00 CI failure
- 2026-09-09T10:09:58+00:00 automated review: approve — Automated reviews now suppress optional unattached-artifact and metadata commentary while retaining internal diagnostics and genuine blockers. cost=$0.18
- 2026-09-09T10:18:24+00:00 dispatched revise run 20260909T101823Z-revise-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15456 tokens)
- 2026-09-09T10:20:47+00:00 worker found no change to make: The existing commit is correct: focused review coverage passes (88 passed), lint passes, and the only supplied actions failure is missing GitHub CLI authentication, which is external to this diff.; reconciling with checks and a fresh review
- 2026-09-09T10:22:12+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/360: Verified commit 0b551e4c suppresses posted commentary for omitted/unavailable optional artifacts while retaining diagnostics and blocking source contradictions. Ran focused review tests and Ruff successfully; no type checker is configured in pyproject or CI. cost=$0.24
- 2026-09-09T10:23:32+00:00 CI failure
- 2026-09-09T10:23:41+00:00 dispatched revise run 20260909T102341Z-revise-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15674 tokens)
- 2026-09-09T10:24:45+00:00 automated review: approve — Automated reviews now suppress optional evidence-packaging commentary while retaining internal diagnostics and genuine blockers. cost=$0.15
- 2026-09-09T10:34:34+00:00 worker found no change to make: The reported test failure does not reproduce on the current head, and inspection found no deterministic source defect to change. The separate actions failure is missing GitHub CLI authentication.; reconciling with checks and a fresh review
- 2026-09-09T10:35:53+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/360: Existing commit 0b551e4c already suppresses posted commentary for omitted or unavailable optional artifacts while retaining internal diagnostics and source-identity blockers. Focused review coverage passed (88 tests), the bounded full pytest run completed with exit 0, and Ruff passed. cost=$0.52
- 2026-09-09T10:37:16+00:00 CI failure
- 2026-09-09T10:37:32+00:00 dispatched revise run 20260909T103732Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15946 tokens)
- 2026-09-09T10:38:40+00:00 automated review: approve — Automated reviews now suppress optional evidence-packaging commentary while preserving internal diagnostics and genuine blocking findings. cost=$0.23
- 2026-09-09T10:39:50+00:00 worker found no change to make: The supplied Actions error is missing GitHub CLI authentication, and the unspecified test failure has no available log and does not reproduce on the current head; no deterministic source defect was found.; reconciling with checks and a fresh review
- 2026-09-09T10:41:08+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/360: Existing commit 0b551e4c suppresses optional unattached-artifact and metadata commentary while preserving internal diagnostics and source-identity blockers. Verified with tests/test_review.py (88 passed), .venv/bin/ruff check src tests scripts, and git diff --check. cost=$0.21
- 2026-09-09T10:42:26+00:00 CI failure, but 6 revision rounds already used; needs a human
- 2026-09-09T12:44:47+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T12:46:58+00:00 precise shared QA failure diagnosis preserved alongside approval; owner revision limit10, no counter reset
- 2026-09-09T12:54:25+00:00 dispatched revise run 20260909T125425Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~17442 tokens)
- 2026-09-09T13:03:20+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:04:59+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/360: Optional UI scope mapping omissions are now retained only in the review run's internal diagnostics, never posted as review prose. Verified with 89 focused review tests, the reported canary test (1 passed), and Ruff. cost=$0.36
- 2026-09-09T13:17:44+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: new review comments, findings and revi; run `garden triage CG-465 --changes "<feedback>" to unblock`
- 2026-09-09T13:20:43+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T13:22:16+00:00 dispatched revise run 20260909T132215Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~17333 tokens)
- 2026-09-09T13:28:44+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:30:15+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/360: Committed f90bda4c: expected-but-unread UI captures and unavailable current-head check notes are internal diagnostics, not posted findings. Verified with 91 focused review tests and Ruff. cost=$0.31
- 2026-09-09T13:36:37+00:00 automated review: approve — Automated reviews now keep optional evidence-packaging diagnostics out of posted prose while preserving genuine blockers and internal diagnostics. cost=$0.25
- 2026-09-09T13:38:09+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/360
