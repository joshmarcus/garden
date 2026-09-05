---
id: CG-181
title: The retro has a Features for the next phase section, fed by the product-manager persona, and each
  feature becomes a draft in the next phase
status: done
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/personas.py
- personas/product-manager.md
branch: garden/cg-181-the-retro-has-a-features-for-the-next-phase-sect
pr: https://github.com/joshmarcus/context-garden/pull/128
attempts: 1
last_dispatched_at: '2026-09-05T09:54:46+00:00'
created: '2026-09-05T09:52:59+00:00'
updated: '2026-09-05T10:10:49+00:00'
---

## Goal

The reconciled retro document carries a `## Features for the next phase` section: five to eight ranked items, each with user value, why now, size and dependencies, drawn from the product-manager persona's report and the other personas, and each is filed as a draft task in the next phase with provenance `retro:<phase>` so the planner and the human start from them. The product-manager persona ships with the product.

## Context

Asked by the user on 2026-09-05 at the phase-03 wrap-up: "before ending this phase, can we add to the retro what features we should add to the next phase?" and "do we have a product manager review, who is thinking about the product as a whole and the vision forward? I'd especially like them to put items in the next phase." A `personas/product-manager.md` was written in the garden that day (vision, where we are, features for the next phase, not now, questions for the human); the built-in set (designer, project-manager, security, staff-engineer, usability-expert, user) has no product voice. The reconciliation result today has `summary`, `personas`, `still_open` and `next_goals`; features only reach the next phase through the goals draft, unranked and unfiled. Companion: CG-178 (the retro's close / follow-ups / reopen verdict) files fix-type follow-ups; this task files the feature-type ones.

## Acceptance criteria

- [ ] `personas/product-manager.md` (the garden's version, or an equivalent) is a built-in persona, included by default in `garden persona-review` and `garden retro`.
- [ ] The reconciliation brief asks for `features` (title, body, difficulty, priority, rationale) and the retro document renders them as `## Features for the next phase`, ranked; the next-goals draft references them by title.
- [ ] On reap, each feature is filed as a draft in the next phase with `discovered_from: retro:<phase>` and the rationale in its body; duplicates of existing tasks (same title or the retro says so) are skipped with a log line.
- [ ] The retro page (CG-146) lists the features with their task ids and status.
- [ ] A test with the fake harness files two features and skips one duplicate.

## Log

- 2026-09-05T09:53:46+00:00 approved (web)
- 2026-09-05T09:54:46+00:00 dispatched work run 20260905T095437Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~6749 tokens)
- 2026-09-05T10:06:02+00:00 opened https://github.com/joshmarcus/context-garden/pull/128 (base main): Added the product-manager persona as a built-in default, extended the retro reconciliation brief/verdict with a ranked `features` list, rendered a "Features for the next phase" section in the retro doc and next-goals draft, and filed each feature as a draft task in the next phase's worktree (discovered_from: retro:<phase>), skipping title/flagged duplicates with a log line. cost=$2.41
- 2026-09-05T10:09:34+00:00 automated review: approve — Adds the product-manager persona, extends the retro to rank features and file them as provenance-tagged draft tasks in the next phase (dupes skipped with a log line), and renders them in the retro doc and next-goals draft. All acceptance criteria met; full suite (592 passed) and ruff pass locally. cost=$0.85
- 2026-09-05T10:09:38+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T10:09:38+00:00 rebased; diff unchanged; verdict kept
- 2026-09-05T10:10:49+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/128
