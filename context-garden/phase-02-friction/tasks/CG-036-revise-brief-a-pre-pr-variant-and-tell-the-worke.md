---
id: CG-036
title: 'Revise brief: a pre-PR variant, and tell the worker what is already on the branch'
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/brief.py
- src/garden/scheduler.py
branch: garden/cg-036-revise-brief-a-pre-pr-variant-and-tell-the-worke
pr: https://github.com/joshmarcus/context-garden/pull/13
discovered_from: CG-027
attempts: 1
last_dispatched_at: '2026-09-04T17:24:47+00:00'
created: '2026-09-04T17:03:09+00:00'
updated: '2026-09-04T17:40:31+00:00'
---

## Goal

The "Revision round" section says the truth about the PR, and a fresh work run on a reused worktree is told about commits already on the branch.

## Context

On CG-027 the first revise brief opened with "This branch already has an open pull request: (unknown). Reviewers left feedback" when no PR existed and the feedback was a ruff failure from the pre-PR check. The second work attempt (after attempt 1 hit the turn cap) started on the same worktree with three commits on it, but its brief differed from the first only by two log lines and the dispatch note said "fresh session, base main". Add a pre-PR wording in `brief.py` and, when the worktree has commits ahead of the base at dispatch, list them under a "Already on this branch" heading.

## Acceptance criteria

- [ ] no PR: the revision section names the failed check and says no PR exists yet.
- [ ] commits ahead of the base are listed in the brief with their subjects.
- [ ] tests for both.

## Provenance

Discovered by CG-027 (First live run of the loop on itself) during run `20260904T160635Z-work`.

## Log

- 2026-09-04T17:03:09+00:00 discovered by CG-027
- 2026-09-04T17:23:52+00:00 approved (web)
- 2026-09-04T17:24:47+00:00 dispatched work run 20260904T172446Z-work via local [claude model=haiku] (fresh session, base main, ~4749 tokens)
- 2026-09-04T17:29:49+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/13 (base main): Added pre-PR revision section to brief.py and implemented commits-ahead display. Scheduler now passes existing worktree commits to workers so they understand what's already on their branch before revision attempts. All acceptance criteria met with comprehensive tests. cost=$0.43
- 2026-09-04T17:32:28+00:00 automated review: approve — All three acceptance criteria met with clean tests. Logic for pre-PR detection and commits-ahead display is sound. Implementation correctly integrates with scheduler and brief builder. cost=$0.08
- 2026-09-04T17:40:31+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/13
