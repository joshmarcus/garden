---
id: CG-390
title: Require screenshots only for materially changed visual behavior
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading: []
created: '2026-09-07T18:08:12+00:00'
updated: '2026-09-07T18:08:12+00:00'
---

## Goal
Apply the owner policy: PRs do not universally require screenshots or design snapshots. Require visual evidence only for relevant visual changes, and keep functional evidence separate.

## Context
Owner explicitly clarified this after CG216 burned six revisions on captures. Installed review.validation_plan treats any web/app.py or web/common.py edit as shared visual chrome and fans out to every page; page-module paths imply visuals without inspecting the changed behavior. CG216 remote API/auth wiring required14pages/56PNGs despite nonvisual intent. CG377 is merged but its path-based classifier remains too broad. CG389 separately owns mixed-version capture CLI compatibility; do not duplicate it.

## Acceptance criteria
- Backend/API/auth, scheduler, test-only, documentation-only, and nonvisual shared-module edits can pass without screenshots; HTTP/CLI/functional evidence remains proportional to actual claims.
- For a materially visual change, name the changed visible behavior and require only affected pages/states. Shared styling uses representative affected consumers with expansion justified by distinct visual risk, not unconditional full inventory.
- Generated captures/design snapshot artifacts do not trigger new screenshot requirements. Current-head source equivalence can reuse unchanged visual evidence rather than create a self-referential evidence commit loop.
- Worker preflight, pre-PR checks, reviewer brief and mechanical gate consume the same scoped visual decision. Unknown paths require bounded inspection, not blanket screenshots or automatic exemption from functional tests.
- Focused regressions cover nonvisual web/app.py route/auth wiring, API-only, docs/capture artifacts, a single-page layout change, and shared visual styles. Record the chosen scope/reason and a bounded affected-page capture only for the visual example.

## Scope
Keep actual task-specific functional validation and ordinary review/CI. Do not weaken CG385 real reclaim proof. No live fault injection or active-branch edits.
