---
id: CG-251
title: Cost per accepted task and first-pass approval per model, tier and harness in metrics, the Costs
  page and the retro
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
created: '2026-09-05T23:58:09+00:00'
updated: '2026-09-05T23:58:09+00:00'
discovered_from: retro:context-garden/phase-04
---

## Goal

**User value:** the operator can read whether a cheaper model lowers the bill per merged task, which is the finding of this phase (sonnet halved the run price and did not lower the bill).

**Why now:** CG-213 and CG-230 cannot be evaluated without it; CG-233 and CG-214 (merged) supply the per-run cost and the page.

**Size:** medium. **Depends on:** CG-233, CG-214. Accepted means merged to the base branch (CG-228).

## Context

Proposed at the context-garden/phase-04 retro. Every routing decision in phase 05 is a guess until the garden reports this number.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-240 (renumbered by the operator: two reconcile runs drew ids from one counter)
