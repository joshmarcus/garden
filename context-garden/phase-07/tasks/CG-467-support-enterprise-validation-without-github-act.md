---
id: CG-467
title: Support enterprise validation without GitHub Actions
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: hard
reading:
- scripts/check_ci.py
- src/garden/checks.py
- src/garden/github.py
- src/garden/scheduler/poll.py
- src/garden/config.py
- docs/worker-ci.md
branch: garden/cg-467-support-enterprise-validation-without-github-act
pr: https://github.com/joshmarcus/context-garden/pull/365
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T10:20:58+00:00'
created: '2026-09-09T09:51:17+00:00'
updated: '2026-09-09T10:37:27+00:00'
---

## Goal

Support enterprise repositories where GitHub Actions is disabled, unavailable, or not the organization's CI provider. Garden must not assume that publishing a branch can or should start an Actions workflow.

## Owner request

Feature requested September 9, 2026: "Do not assume GitHub actions are enabled for enterprise use cases."

## Acceptance criteria

- [ ] Make the validation path configurable per repository/product: GitHub Actions when selected, another existing status/check provider or configured validation command when selected, and an explicit documented policy for environments without an external CI service. Do not require Actions merely because the repository is hosted on GitHub or GitHub Enterprise.
- [ ] Worker briefs, setup/check tooling (including scripts/check_ci.py where applicable), review and automatic-merge readiness consistently use the selected policy; an Actions-disabled enterprise configuration must not repeatedly push, poll nonexistent workflows, or ask an author to enable Actions.
- [ ] Preserve exact-source validation and honest pending/failure/unknown states. Missing external results are not silently converted into success; use the configured validation evidence and requirements. Never bypass a real failed required check, explicit reviewer rejection, fresh conflict check, or atomic merge-head guard.
- [ ] Provide actionable diagnostics distinguishing an unavailable/disabled provider, insufficient permission, a pending run, and a real failed validation. Avoid requiring public github.com endpoints or broader credentials for enterprise hosts.
- [ ] Cover an enterprise repository without Actions and one alternate configured validation path with focused tests, plus regression coverage for the existing Actions-enabled path. Document configuration and defaults using concrete examples. Do not require access to a paid enterprise instance for deterministic tests.

## Scope

Prefer extending existing check/status/command configuration over introducing a large provider framework. Preserve default behavior for existing explicitly configured Actions users. This task does not disable validation in the live Garden deployment or change the current RC10 release gate; it is separate product work for the normal Garden loop.

## Log

- 2026-09-09T09:51:17+00:00 approved (owner-requested enterprise Actions independence)
- 2026-09-09T09:55:02+00:00 dispatched work run 20260909T095502Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20083 tokens)
- 2026-09-09T10:08:36+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T10:10:06+00:00 opened https://github.com/joshmarcus/context-garden/pull/365 (base main): Added explicit per-product validation policies for GitHub Actions, provider-neutral status checks, exact-head validation commands, and environments with no external CI. Verified with 209 focused tests and clean Ruff lint; the repository has no configured typecheck command. cost=$2.54
- 2026-09-09T10:20:49+00:00 automated review requested changes: Command validation does not refresh its exact-head receipt after scheduler rebases, preventing automatic merge despite a successful validation of the new head. cost=$0.54
- 2026-09-09T10:20:58+00:00 dispatched revise run 20260909T102058Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20999 tokens)
- 2026-09-09T10:27:09+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T10:28:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/365: Command-policy validation receipts now refresh after every successful scheduler recheck, so mechanically rebased heads can become merge-eligible without weakening exact-source validation. Verified 146 focused tests and clean Ruff lint at commit f8dba344; the repository has no configured typecheck command. cost=$1.14
- 2026-09-09T10:30:56+00:00 automated review: approve — Validation policies are consistently applied without weakening exact-head, review, conflict, or merge guards. The prior command-receipt rebase defect is fixed. cost=$0.35
- 2026-09-09T10:35:54+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T10:37:27+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/365
