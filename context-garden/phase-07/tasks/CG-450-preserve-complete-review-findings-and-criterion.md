---
id: CG-450
title: Preserve complete review findings and criterion reasons through revision handoffs
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 1
order: -101
difficulty: medium
reading:
- src/garden/review.py
- src/garden/brief.py
- src/garden/scheduler/human.py
- tests/test_review.py
branch: garden/cg-450-preserve-complete-review-findings-and-criterion
pr: https://github.com/joshmarcus/context-garden/pull/340
runner: remote
discovered_from: Owner criteria/enterprise review audit2026-09-08
attempts: 1
last_dispatched_at: '2026-09-09T00:48:32+00:00'
created: '2026-09-08T19:24:45+00:00'
updated: '2026-09-09T01:11:34+00:00'
---

## Goal

Deliver the full actionable review context to the next author without operator triage notes replacing it.

Audit of8briefs found all31frozen criteria present. Four operator recoveries CG328/332/375/381 instead supplied345/430/438/384-character summaries that omitted full prior fixes. The ordinary feedback_from_review function forwards findings and description/improvements but omits criterion reasons/evidence. Preserve operator context as an addition, with explicit resolved/superseded annotations rather than silent loss.

## Acceptance criteria

- [ ] The revision brief retains complete actionable finding summary/fix/location and failed-criterion reason/evidence from the applicable review, including source/run references.
- [ ] Operator triage/recovery notes supplement that review; resolved/superseded findings are distinguished without losing provenance or repeatedly demanding already-fixed work.
- [ ] Focused tests cover long feedback, criterion-only rejection and operator triage/recovery; no substantive field is silently truncated or replaced.

## Log

- 2026-09-08T19:24:45+00:00 approved (owner-delegated-hourly-audit)
- 2026-09-08T19:26:12+00:00 dispatched work run 20260908T192611Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~10451 tokens)
- 2026-09-08T19:34:09+00:00 opened https://github.com/joshmarcus/context-garden/pull/340 (base main): Revision briefs now retain complete review findings, failed-criterion reason/evidence, and review run/head provenance. Operator triage and recovery notes are explicit supplements or superseding handoffs rather than replacements. cost=$0.73
- 2026-09-08T20:56:13+00:00 automated review requested changes: Operator handoffs preserve review text, but triage incorrectly supersedes every prior finding and provenance can cite a head the review never examined. Focused tests and lint pass; the supplied exact-head interaction replay does not exercise the changed handoff behavior. cost=$0.44
- 2026-09-08T21:06:35+00:00 stuck: manual task has a revise round waiting; take it with `garden take`; take it (`garden take CG-450`) or send it back (`garden triage CG-450 --changes "..."`)
- 2026-09-08T21:43:53+00:00 dispatched revise run 20260908T214352Z-revise-3 via manual [human] (fresh session, base main, ~11421 tokens)
- 2026-09-08T22:05:23+00:00 fenced: Cannot verify this run's worktree fence; inspect protected paths before retrying. Restoration is unverified: fence manifest unavailable or invalid: trusted manifest reference missing or belongs to another run — worktree writes kept: docs/test-suites.md, docs/worker-protocol.md, pyproject.toml, src/garden/cli/loop.py, src/garden/config.py, src/garden/remote_worker.py, src/garden/review.py,
- 2026-09-08T22:07:08+00:00 re-enabled by hand; revise run will follow
- 2026-09-08T22:07:08+00:00 dispatched revise run 20260908T220708Z-revise via manual [human] (fresh session, base main, ~11140 tokens)
- 2026-09-08T22:07:09+00:00 external PR attached at garden/cg-450-preserve-complete-review-findings-and-criterion; existing CI is PENDING
- 2026-09-08T22:20:53+00:00 stalled: review finding repeated after a revise round: acceptance criterion lacks a passing, evidenced assessment: operator triage/reco; run `garden triage CG-450 --changes "<feedback>" to unblock`
- 2026-09-08T22:41:17+00:00 re-enabled by hand; revise run will follow
- 2026-09-08T22:41:17+00:00 dispatched revise run 20260908T224117Z-revise via manual [human] (fresh session, base main, ~11980 tokens)
- 2026-09-08T22:41:19+00:00 external PR attached at garden/cg-450-preserve-complete-review-findings-and-criterion; existing CI is PENDING
- 2026-09-08T22:57:31+00:00 stalled: review finding repeated after a revise round: acceptance criterion lacks a passing, evidenced assessment: operator triage/reco; run `garden triage CG-450 --changes "<feedback>" to unblock`
- 2026-09-08T23:43:26+00:00 dispatched revise run 20260908T234325Z-revise via manual [human] (fresh session, base main, ~11227 tokens)
- 2026-09-08T23:43:40+00:00 external PR attached at garden/cg-450-preserve-complete-review-findings-and-criterion; existing CI is SUCCESS
- 2026-09-09T00:34:44+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/review.py); a rebase agent will resolve it
- 2026-09-09T00:34:46+00:00 dispatched rebase run 20260909T003446Z-rebase-2 via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1563 tokens)
- 2026-09-09T00:37:38+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/340: Rebased onto origin/main and resolved the review.py conflict while preserving both sides' logic cost=$0.01
- 2026-09-09T00:40:57+00:00 feedback from an untrusted author ignored: Copilot: > @copilot resolve the merge conflicts in this pull request

Resolved and pushed. I merged `origin/main` into this branch, resolved the conflict in `src/garden/scheduler/review.py`, then merged the cu
- 2026-09-09T00:43:58+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_review.py); a rebase agent will resolve it
- 2026-09-09T00:44:04+00:00 dispatched rebase run 20260909T004404Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1762 tokens)
- 2026-09-09T00:48:12+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/340: Rebased onto origin/main and resolved review handoff conflicts, preserving complete provenance and applicability behavior. cost=$0.03
- 2026-09-09T00:48:29+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/human.py, tests/test_review.py); a rebase agent will resolve it
- 2026-09-09T00:48:32+00:00 dispatched rebase run 20260909T004832Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2040 tokens)
- 2026-09-09T00:52:42+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/340: Resolved the rebase conflicts while preserving actor validation, review provenance backfilling, and exact provenance test assertions. cost=$0.01
- 2026-09-09T01:08:48+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/340
- 2026-09-09T01:11:34+00:00 automated review could not start: CG-450 is done: #340 was merged at 01:08:48
