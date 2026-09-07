---
id: CG-377
title: Scope review validation to affected behavior and acceptance claims
status: ready
product: context-garden
phase: phase-05
depends_on:
- CG-339
priority: 1
difficulty: medium
reading: []
created: '2026-09-07T09:31:44+00:00'
updated: '2026-09-07T09:31:45+00:00'
---

## Goal

Require evidence proportional to affected behavior, rather than making every PR satisfy an application-wide validation checklist. Preserve meaningful UI and lifecycle review.

## Context

Owner requested fixing overly broad validation demands on2026-09-07. CG358 had all incident-control criteria accepted yet a blanket missing-captures finding named14 unrelated pages. CG365 suffered the same. CG339 currently repairs package-wide interaction classification and label-only recovery evidence; depend on and preserve that work rather than duplicate it. CG315's historical always-capture core-page rule and available capture inventory must not become unconditional review requirements. CG376 tracks review-loop friction.

## Acceptance criteria

- [ ] Derive one explicit validation plan from changed behavior, acceptance claims and shared dependencies. Each required page/flow/check records its applicability reason; merely being captured or existing in src/garden is insufficient.
- [ ] Separate available artifacts from required artifacts. Missing pages_seen blocks only required affected pages; pure documentation/parser/formatting changes require focused relevant checks, not screenshots or generic empty/failure journeys.
- [ ] Shared templates/styles/navigation and cross-cutting lifecycle changes expand scope to affected consumers with a stated rationale. Require real served/browser behavior for interaction claims; relevant empty/failure/recovery states remain mandatory when behavior can affect them. Unknown scope prompts bounded inspection rather than blanket exemption or whole-app default.
- [ ] Workers, pre-checks and reviewers consume the same head-bound validation plan. New demands identify the changed claim or discovered risk and are logged as scope expansion; preserve frozen acceptance criteria and existing valid evidence without accepting stale-head evidence.
- [ ] Regression cases cover CG358-style backend control change without rendered-page changes, parser-only change, one-page layout change, shared stylesheet change and real failure/recovery behavior. Reject arbitrary14-page demand and reject under-validation of shared UI or claimed interactions.
- [ ] Preserve broad whole-application walkthroughs at phase/milestone validation where appropriate; record avoided review rounds/capture cost and remaining unknowns in friction, linked to CG376.

## Log

- 2026-09-07T09:31:45+00:00 approved (web)
