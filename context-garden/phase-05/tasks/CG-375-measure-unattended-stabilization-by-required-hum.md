---
id: CG-375
title: Measure unattended stabilization by required human-owner action
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
created: '2026-09-07T09:22:34+00:00'
updated: '2026-09-07T09:23:14+00:00'
---

## Goal

Align stabilization recording with the owner clarification: four productive hours without required action from Josh is sufficient; delegated agent-operator interventions are permitted.

## Context

Owner clarified this on2026-09-07. Current stabilization.py categorizes operator_repair/requeue/retry as interventions and resets the candidate window in intervene. This incorrectly rejects owner-unattended operation. Policy is context-garden/phase-05/specs/stabilization.md in the garden; product code must reflect the same semantics.

## Acceptance criteria

- [ ] Record actor provenance distinguishing human owner, delegated operator and automated scheduler; operator actions remain visible for cost/reliability without resetting the no-owner-action window.
- [ ] Required owner unblock/repair actions interrupt the window; status questions and non-operative conversation do not. Unknown historical actor provenance is unproven rather than silently relabeled.
- [ ] Preserve four productive hours, ten representative completions, pinned-build consistency and all other existing gates; update CLI/UI wording to explain no-owner-action semantics.
- [ ] Tests prove multiple operator retries/repairs/merges can coexist with a passing window, a required owner intervention interrupts it, and unknown actor evidence cannot manufacture a pass.

## Log

- 2026-09-07T09:23:14+00:00 approved (web)
