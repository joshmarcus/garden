---
id: CG-356
title: Recover onboarding cleanly when planner output is rejected
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
created: '2026-09-06T17:34:36+00:00'
updated: '2026-09-06T17:35:33+00:00'
---

## Goal

A failed onboarding planner step leaves an understandable, recoverable draft instead of requiring the user to untangle a half-created product before retrying.

## Evidence

Operator inspection of #216 on 2026-09-06: onboard_project writes config, product, conventions and phase before calling the planner. Invalid or ambiguous provenance correctly rejects the plan, but a repeated onboard command then encounters the existing-product protection. The first successful onboarding path is validated; planner-failure recovery needs a separate explicit path.

## Acceptance criteria

- [ ] Reproduce planner failure and unsupported-provenance rejection with a disposable existing garden; preserve its pre-existing configuration and files.
- [ ] Offer a deterministic retry/resume or transactional rollback for generated onboarding drafts. Never remove or overwrite owner edits or an unrelated existing product.
- [ ] Explain which draft files were created, whether anything was imported, and the exact recovery action. Do not misreport a partial run as successful onboarding.
- [ ] Exercise failure then successful retry, changed draft files, and existing-product collision. Do not launch task workers or approve drafts implicitly.

## Scheduling

Phase-05 stabilization follow-up to CG-215. Preserve fast-forward hold until the current PR queue is handled.

## Log

- 2026-09-06T17:35:33+00:00 approved (cli)
