---
id: CG-207
title: Retros and persona reviews use the hard tier by default (retro.difficulty), so nobody edits garden.yaml
  before a retro
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: easy
reading:
- src/garden/config.py
- src/garden/scheduler/persona.py
- src/garden/scheduler/retro.py
- src/garden/review.py
- garden.yaml
- docs/architecture.md
branch: garden/cg-207-retros-and-persona-reviews-use-the-hard-tier-by
pr: https://github.com/joshmarcus/context-garden/pull/156
attempts: 1
last_dispatched_at: '2026-09-05T13:01:07+00:00'
created: '2026-09-05T10:30:59+00:00'
updated: '2026-09-05T13:38:59+00:00'
---

## Goal

A retro and its persona reviews run on the best tier the garden has without anyone editing config first. A new `retro.difficulty` key (default `hard`) picks the tier for persona reviews and the reconciliation run; `review.difficulty` keeps governing PR reviews only. `garden retro --dry-run` and the retro page name the tier and model they will use.

## Context

The user on 2026-09-05: "always set retros to hard (by default) so we're not manually changing anything." For the phase-02 and phase-03 retros the operator edited `review.difficulty` to `hard`, restarted the server, ran the retro, edited it back to `medium` and restarted again, because personas and the reconciliation share the PR-review tier. Each restart cost a review verdict (see CG-198). The user's earlier note stands: there are better models than the hard tier; the tier map can point `hard` at the best available.

## Acceptance criteria

- [ ] `retro.difficulty` exists with default `hard`, documented beside `review.difficulty`; persona reviews (phase and PR) and the reconciliation resolve their model from it; PR reviews are unchanged.
- [ ] `garden retro --dry-run` prints the tier and model; the retro page shows them on the report.
- [ ] `review.difficulty` in the example configs and the live garden no longer carries a "set to hard for a retro" comment.
- [ ] A test runs a persona review with `review.difficulty: easy` and `retro.difficulty: hard` and sees the hard model in the dispatch.

## Log

- 2026-09-05T10:31:20+00:00 approved (web)
- 2026-09-05T13:01:07+00:00 dispatched work run 20260905T130057Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~20463 tokens)
- 2026-09-05T13:09:49+00:00 opened https://github.com/joshmarcus/context-garden/pull/156 (base main): Added retro.difficulty (default hard) so persona reviews (phase and PR) and the retro reconciliation always run on the best tier without editing review.difficulty first; garden retro --dry-run and the retro document now name the tier and model. cost=$1.96
- 2026-09-05T13:11:27+00:00 automated review: approve — retro.difficulty (default hard) cleanly routes persona reviews and the retro reconciliation off review.difficulty; PR reviews untouched, dry-run and retro doc name the tier/model, and all four acceptance criteria are backed by passing tests. cost=$0.74
- 2026-09-05T13:23:36+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T13:27:45+00:00 automated review produced no verdict (worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_messa) cost=$0.00
- 2026-09-05T13:34:53+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T13:37:32+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-207` for one more round, or review on GitHub
- 2026-09-05T13:38:59+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/156
