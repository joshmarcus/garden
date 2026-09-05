---
id: CG-136
title: 'PR descriptions stop costing rounds: a body contract in the brief, friction out of the body, reviewer
  rewrites'
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/brief.py
- src/garden/review.py
- src/garden/scheduler.py
- principles/00-index.md
- src/garden/cli.py
branch: garden/cg-136-pr-descriptions-stop-costing-rounds-a-body-contr
pr: https://github.com/joshmarcus/context-garden/pull/93
attempts: 1
last_dispatched_at: '2026-09-05T00:50:17+00:00'
created: '2026-09-05T00:44:27+00:00'
updated: '2026-09-05T01:14:31+00:00'
---

## Goal

A PR description that only needs rewording never costs a worker round. The brief states the description contract once; friction leaves the body for its own channel; a rebase round drops what main already has; and when the automated review finds nothing blocking but the description, it returns the corrected description and the scheduler applies it.

## Context

Asked at the freeze of the first live run, after twelve description-only review requests in an evening, each a revise round of one to four dollars. The reviewer's complaints cluster into three prompt contradictions. First, revise briefs for rebase and pre-PR-check rounds hand the worker `pr_body` as something to rewrite, so it narrates the round ("## Revision round", "## Review responses"): seven of eight quoted findings. CG-037 (#44) fixed this for review responses only. Second, `principles/00-index.md` says to note friction in the PR body under "Friction" while `review.py` forbids process narration; friction is process narration, so every PR that follows the principle fails the review (#86 tonight). Third, after a rebase the body claims work main has since absorbed (#82 described five fixes with two in the diff).

Do four things. (1) In `brief.py`'s result rules, state the contract: `pr_body` is the permanent description for a reader without the task file (what, why, tests, follow-ups); it never mentions rounds, rebases, reviews, checks, prior attempts or this run; those go in `pr_comment`; on a revise round omit `pr_body` unless the description must change, and the current one stays. (2) Move friction to a `friction` field of the result (a list of short items); the scheduler posts them as one marked PR comment and appends them to the phase's friction record; `garden friction` harvests from the record and the marked comments, with the body-section path kept for old PRs; update the principle's wording. (3) The rebase-round brief says: drop from the description anything that is now on main. (4) In `review.py`, when `description_ok` is false and no finding is blocking, the reviewer returns `description_rewrite` (the full corrected body); the scheduler updates the PR body through the GitHub API, logs "description rewritten by the reviewer", and does not start a round. Overlaps CG-109 (easy tier for description rounds), which becomes the fallback when the rewrite is empty.

## Acceptance criteria

- [ ] the brief's result section carries the contract and a test asserts the wording; a revise round that omits `pr_body` leaves the description unchanged.
- [ ] `friction` in a result reaches the phase record and a marked comment, and never the body; `garden friction` harvests it.
- [ ] a review with `description_ok: false` and no blocking finding updates the PR body and starts no run; a test with the fake GitHub checks the body.

## Log

- 2026-09-05T00:50:17+00:00 dispatched work run 20260905T005008Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~8293 tokens)
- 2026-09-05T01:08:26+00:00 opened https://github.com/joshmarcus/context-garden/pull/93 (base main): A body contract in the brief states that pr_body is the permanent description (process narration goes to pr_comment, friction to a new friction field); the scheduler routes worker friction to a marked comment plus the phase record, tells rebase rounds to drop what the base already has, and applies reviewer description_rewrite directly without spending a round. cost=$9.02
- 2026-09-05T01:11:51+00:00 automated review: approve — All three acceptance criteria are met with direct test evidence; full suite (379 passed) and ruff are green, scope is tight, and the PR description cleanly follows the very contract it introduces. cost=$1.06
- 2026-09-05T01:14:31+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/93
