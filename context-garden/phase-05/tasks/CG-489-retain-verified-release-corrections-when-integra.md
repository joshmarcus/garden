---
id: CG-489
title: Retain verified release corrections when integrating current main
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/review.py
- src/garden/scheduler/review.py
- tests/test_review.py
branch: codex/retain-verified-release-corrections
pr: https://github.com/joshmarcus/context-garden/pull/390
runner: manual
attempts: 1
last_dispatched_at: '2026-09-09T16:05:14+00:00'
created: '2026-09-09T16:05:13+00:00'
updated: '2026-09-10T02:00:28+00:00'
---

## Goal
Preserve verified RC12 behavior missing from current main before building the next controller release. Restore exact reviewed fixes rather than weakening current merge or review guards.

## Acceptance criteria
- [ ] Optional omitted/null review observation lists render safely and quietly.
- [ ] Review recovery recognizes proven approval carried across a mechanically derived unchanged-patch head while preserving authentic same-head rejection and invalid lineage refusal.
- [ ] Preserve other audited prior release corrections; include deterministic existing regressions and proportionate tests.
- [ ] Publish a focused current-source PR and independently review before versioned integration; do not hotpatch live runtimes or fabricate review approval.

## Log

- 2026-09-09T16:05:14+00:00 approved (cli)
- 2026-09-09T16:05:14+00:00 dispatched work run 20260909T160514Z-work via manual [human] (fresh session, base main, ~14405 tokens)
- 2026-09-09T16:52:02+00:00 external PR attached at codex/retain-verified-release-corrections; existing CI is SUCCESS
- 2026-09-09T16:57:53+00:00 automated review: approve — The focused corrections preserve review provenance and merge guards while safely handling null observations and fencing notification recipients. cost=$0.51
- 2026-09-10T02:00:28+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/390
