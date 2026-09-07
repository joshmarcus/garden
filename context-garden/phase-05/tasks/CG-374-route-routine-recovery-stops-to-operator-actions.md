---
id: CG-374
title: Route routine recovery stops to operator actions instead of owner decisions
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
created: '2026-09-07T09:14:35+00:00'
updated: '2026-09-07T09:14:36+00:00'
---

## Goal

Route routine recovery stops to operator actions instead of owner decisions.

## Context

Owner queue audit found CG253/297/323/339 retry caps with actionable findings, CG329 missing CI, CG358 stale browser stop and CG295 asking to edit live config outside its checkout. Owner requested prevention tickets after resolving the human queue.

## Acceptance criteria

- [ ] Separate actionable technical recovery from decisions requiring owner preferences or authority; expose clear reason and next action.
- [ ] With delegated recovery authority, enqueue one bounded continuation retaining feedback and PR identity; enforce resource admission and stop repeated unchanged failures.
- [ ] Preflight task scope against checkout ownership; split operator-owned config steps and accept verified operator evidence without granting workers production-write access.
- [ ] Regression coverage includes retry caps with feedback, missing CI, stale infrastructure prerequisites and mixed product/live-config deliverables; none produces an unexplained owner card.

## Log

- 2026-09-07T09:14:36+00:00 approved (web)
