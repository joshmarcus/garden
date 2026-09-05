---
id: CG-181
title: The retro has a Features for the next phase section, fed by the product-manager persona, and each
  feature becomes a draft in the next phase
status: ready
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
created: '2026-09-05T09:52:59+00:00'
updated: '2026-09-05T09:53:46+00:00'
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
