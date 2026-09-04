---
id: CG-038
title: Stall detection judges a description-only round by the description
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/review.py
branch: garden/cg-038-stall-detection-judges-a-description-only-round
pr: https://github.com/joshmarcus/context-garden/pull/21
discovered_from: CG-027
attempts: 1
last_dispatched_at: '2026-09-04T17:24:48+00:00'
created: '2026-09-04T17:03:10+00:00'
updated: '2026-09-04T17:42:30+00:00'
---

## Goal

A revise run whose feedback was only about the PR description is not stalled for leaving the diff unchanged.

## Context

On CG-027 the review asked only for a section to be removed from the PR body. The revise run did that and changed no code; `finalize` compared diff hashes, found no change, and moved the task to `changes_requested` with `needs_human` ("garden retry to resume"), although the PR was clean, mergeable and green. `garden retry` would start a fresh work run, not resume. When `pending_feedback` had no code findings (description feedback, or triage notes that mention only the body), compare the PR body instead, or skip the stall check for that round.


A second case, seen on CG-027's own PR: a revise round whose pre-PR check failed (a flaky test under load) still saved its diff hash. The next round pushed the same commits, which had never reached the PR, and was stalled for "no change to the diff". The hash should only be recorded for rounds that reached the PR, or the comparison should be against the PR head on GitHub.

## Acceptance criteria

- [ ] a description-only round that changes the body is not a stall.
- [ ] a round that changes neither diff nor body still is.
- [ ] a round after a failed pre-PR check is compared with what the PR has, not with the failed round.
- [ ] the stall note names what to do that actually resumes the task.

## Provenance

Discovered by CG-027 (First live run of the loop on itself) during run `20260904T160635Z-work`.

## Log

- 2026-09-04T17:03:10+00:00 discovered by CG-027
- 2026-09-04T17:23:53+00:00 approved (web)
- 2026-09-04T17:24:48+00:00 dispatched work run 20260904T172447Z-work via local [claude model=sonnet] (fresh session, base main, ~3766 tokens)
- 2026-09-04T17:38:41+00:00 discovered work filed: CG-052
- 2026-09-04T17:39:03+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/21 (base main): Fixed stall detection in _after_push to compare both diff and PR body hashes; only save hashes after checks pass; updated stall note to name the correct unblocking command. All 114 tests pass. cost=$2.39
- 2026-09-04T17:42:30+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/21
