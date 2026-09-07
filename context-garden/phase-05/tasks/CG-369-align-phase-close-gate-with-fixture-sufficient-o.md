---
id: CG-369
title: Align phase-close gate with fixture-sufficient onboarding requirement
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
created: '2026-09-07T04:12:27+00:00'
updated: '2026-09-07T04:12:57+00:00'
---

## Goal

Apply the owner's2026-09-07 removal of named external-project/maintainer adoption as a phase05 closure requirement. Keep repeatable non-Python onboarding and a useful accepted change, with honest fixture provenance.

## Context

phase-05/specs/stabilization.md and goals.md now allow repeatable fixture evidence. Merged CG341 code in src/garden/stabilization.py still unconditionally rejects independent_project when real_user is false (around147-149). Production narrow5cff609 has not deployed that recorder yet. Align before its rollout; do not report phase closed merely by removing this check.

## Acceptance criteria

- [ ] Phase-close and phase-release evaluation accepts otherwise valid current-build independent_project fixture evidence without a named project, external maintainer or real_user=true. Missing/failed/stale onboarding or accepted-change evidence still blocks.
- [ ] Preserve optional real_user provenance and historical records without relabeling fixtures as adoption. Update CLI/UI messages, documentation and tests that describe real-user evidence as mandatory; no history rewriting.
- [ ] All other gates remain intact: four consecutive productive unattended hours, ten representative completions, recovery and application journeys, resource and intervention accounting, cost/quality targets. Add focused tests showing fixture sufficiency and unrelated gate failures still blocking.
- [ ] Focused local verification serial/bounded and exact-head GitHub CI; self-review and fix findings before completion. No production config edits or automatic phase release.

## Log
## Goal

One or two sentences.

## Context

What the agent needs to know that is not in the reading list.

## Acceptance criteria

- [ ] ...

## Out of scope

- ...
- 2026-09-07T04:12:57+00:00 Owner explicitly removed named external adoption from phase gate; policy updated immediately, this task aligns merged enforcement before deployment.
