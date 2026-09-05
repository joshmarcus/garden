---
id: CG-149
title: Briefs inline reading-list snippets from the target checkout and verify every path; the fixed brief
  cost is measured per phase
status: in_review
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 2
difficulty: medium
reading: []
branch: garden/cg-149-briefs-inline-reading-list-snippets-from-the-tar
pr: https://github.com/joshmarcus/context-garden/pull/117
discovered_from: retro:context-garden/phase-02-friction
attempts: 1
last_dispatched_at: '2026-09-05T04:48:04+00:00'
created: '2026-09-05T03:14:36+00:00'
updated: '2026-09-05T05:04:18+00:00'
---

## Goal

Briefs inline reading-list snippets from the target checkout and verify every path; the fixed brief cost is measured per phase.

## Context

From the phase-02 retro's open list (item 1), reconciled against what merged on 2026-09-05: "Briefs inline stale reading-list snippets and mark existing files not found (CG-045, 078, 115, 117, 129)". See `../phase-02-friction/docs/retro.md` for the evidence and the persona reports under `../phase-02-friction/docs/reviews/`. Write the acceptance criteria when the task is planned.

## Acceptance criteria

- [ ] to be written at planning; the retro item above is the requirement.

## Log
- 2026-09-05T03:15:00+00:00 filed from the phase-02 retro (open item 1)
- 2026-09-05T03:19:59+00:00 approved (web)
- 2026-09-05T04:48:04+00:00 dispatched work run 20260905T044755Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~3720 tokens)
- 2026-09-05T05:00:25+00:00 opened https://github.com/joshmarcus/context-garden/pull/117 (base main): Dispatch now prepares the task worktree before building the brief, so reading-list snippets are inlined from the target checkout (a stacked parent's or dependency's files included) instead of a stale base repo, and genuinely-absent paths are correctly flagged. Added brief.phase_fixed_tokens() and used it from the phase page and usage CLI so the fixed brief cost is measured once per phase. cost=$3.06
- 2026-09-05T05:03:06+00:00 automated review: approve — Preparing the task worktree before building the brief makes reading-list snippets resolve against the target checkout (via product_dirs preferring the worktree), and phase_fixed_tokens measures the fixed brief cost once per phase. Both are correctly tested; the dispatch refactor is behavior-preserving. cost=$0.43
- 2026-09-05T05:04:18+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
