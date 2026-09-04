---
id: CG-037
title: Stop the revise template and the review prompt contradicting each other
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/brief.py
- src/garden/review.py
branch: garden/cg-037-stop-the-revise-template-and-the-review-prompt-c
discovered_from: CG-027
last_dispatched_at: '2026-09-04T17:36:39+00:00'
created: '2026-09-04T17:03:10+00:00'
updated: '2026-09-04T18:47:54+00:00'
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
