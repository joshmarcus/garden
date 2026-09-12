---
id: CG-422
title: Isolate nested validation lease environment in runner-spawning tests
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/validation.py
- src/garden/runner/local.py
- src/garden/runner/base.py
- tests/conftest.py
- tests/test_runners.py
- docs/worker-protocol.md
branch: garden/cg-422-isolate-nested-validation-lease-environment-in-r
pr: https://github.com/joshmarcus/context-garden/pull/402
discovered_from: CG-375
attempts: 1
last_dispatched_at: '2026-09-09T21:36:10+00:00'
created: '2026-09-08T11:02:02+00:00'
updated: '2026-09-09T21:52:49+00:00'
file: tests/test_runners.py
error: A wrapped local runner suite can contend with the wrapper's inherited execution identity.
---

## Goal

Allow runner-spawning tests to execute under the supported validation wrapper without inheriting a parent heavy-execution lease that makes a child wait on its own parent lock.

## Acceptance criteria

- [ ] Reproduce nested lease inheritance with a bounded runner-spawning test and identify the inherited environment fields responsible.
- [ ] Isolate test-created runner environments or use an equivalent supported lease handoff, retaining production admission and lock ownership checks.
- [ ] Focused regressions pass directly and inside the validation wrapper, terminate child processes, and prove unrelated concurrent owners cannot bypass a held lease.
- [ ] Document the supported test pattern and reproduction; focused checks and exact-head CI pass. Stress/load experiments remain separately opt-in.

## Provenance

Discovered by CG-375 (Measure unattended stabilization by required human-owner action) during run `20260908T104605Z-revise`.
## Log
- 2026-09-08T11:02:02+00:00 discovered by CG-375
- 2026-09-08T12:28:50+00:00 Owner-requested Inbox audit: completed verified source/test reading list; preserved implementation, PR and feedback. Repaired parsed acceptance checklist.
- 2026-09-08T12:35:50+00:00 approved (delegated-operator-inbox-audit)
- 2026-09-09T21:36:10+00:00 dispatched work run 20260909T213606Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~24956 tokens)
- 2026-09-09T21:40:40+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T21:41:59+00:00 opened https://github.com/joshmarcus/context-garden/pull/402 (base main): Centralized scrubbing of all nested execution-lease fields for synthetic runner/supervisor test environments, added a regression for the inherited fields, and documented the supported bounded/reaped test pattern. Verified 70 focused runner tests directly and under garden.validation before the whitespace-only final adjustment; reran focused tests and lint on commit 36b16d04. cost=$0.49
- 2026-09-09T21:45:30+00:00 automated review: approve — Synthetic runner environments consistently discard inherited lease identity, preventing self-deadlock under validation without weakening production admission or ownership behavior. cost=$0.49
- 2026-09-09T21:52:49+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/402
