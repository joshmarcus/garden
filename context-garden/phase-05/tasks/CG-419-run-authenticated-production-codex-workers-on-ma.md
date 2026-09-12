---
id: CG-419
title: Run authenticated production Codex workers on managed EC2
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-346
priority: 0
difficulty: hard
reading:
- context-garden/phase-06/specs/ec2-workers.md
branch: codex/aws-production-worker-20260908
pr: https://github.com/joshmarcus/context-garden/pull/301
runner: manual
created: '2026-09-08T04:04:53+00:00'
updated: '2026-09-08T08:55:08+00:00'
---

## Goal

Run an actual authenticated Codex worker on one managed EC2 host and prove useful remote execution with durable results. Complete the production bootstrap on top of the merged and deployed managed-worker foundation.

## Context

Owner repeatedly prioritizes AWS because the operator machine lacks sufficient resources. The prior completed canary used deterministic model/GitHub fixtures. CG346 corrected setup and transport, but its bootstrap installs only the fake canary harness and Git endpoint. The operator owns this direct fast-forward task; no additional model agent is dispatched for implementation.

## Acceptance criteria

- [ ] Production profile verifies and installs a pinned official Codex runtime, installs dedicated model and repository credentials without logging them, and supports unattended credential refresh. No operator credentials go to the worker.
- [ ] A fresh EC2 host joins the existing restricted worker identity, runs unprivileged under measured host admission and an exclusive lock, uses disk temp, blocks metadata access, and has independently enforced bounded runtime.
- [ ] Actual authenticated model work completes over the production controller's worker protocol; setup, result/artifact collection and host attribution are verified. Preserve evidence if a host fails.
- [ ] Provision through the scoped profile, stay within the owner's $80 aggregate allocation, and record runtime/cost commitments and observed cleanup/retention honestly.
- [ ] Focused meaningful tests, exact-head full CI, operator self-review and a versioned bootstrap/source deployment are completed; do not label a controller-only install as a running production worker.

## Scope

First production host and necessary bootstrap/authentication repair. Preserve old canary evidence and never reuse its consumed enrollment. Spot policy, expanded pool controls and unrelated Phase07/05 work follow actual production operation. Credentials and private operational identifiers stay outside public code artifacts.

## Log

- 2026-09-08T04:09:14+00:00 approved (cli)
- 2026-09-08T04:22:13+00:00 PR attached: https://github.com/joshmarcus/context-garden/pull/301 (pr_number none -> 301)
- 2026-09-08T08:55:08+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/301
