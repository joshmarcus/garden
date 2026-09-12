---
id: CG-525
title: Repair manual PR refresh fake mutation regression
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-515
  after: merge
priority: 1
difficulty: easy
reading:
- src/garden/github.py
- src/garden/config.py
- src/garden/checks.py
- src/garden/scheduler/poll.py
- docs/architecture.md
- tests/scheduler/test_poll.py
branch: garden/cg-525-repair-manual-pr-refresh-fake-mutation-regressio
pr: https://github.com/joshmarcus/context-garden/pull/460
runner: remote
discovered_from: CG-515
attempts: 1
last_dispatched_at: '2026-09-10T17:32:12+00:00'
created: '2026-09-10T11:49:21+00:00'
updated: '2026-09-10T18:43:41+00:00'
file: tests/scheduler/test_poll.py
error: Expected `head_sha == new-head`; retained the original commit SHA after refresh.
---

`tests/scheduler/test_poll.py::test_manual_pr_refresh_records_current_head_conflict_without_action` fails on the stacked parent because the test mutates a previously returned fake PR object that repository refresh subsequently replaces. Reconcile the fake identity/update behavior with the repository observation cache.

## Provenance

Discovered by CG-515 (Support provider-neutral source control with scoped certificate and proxy policy) during run `20260910T113703Z-work-3`.
## Log
- 2026-09-10T11:49:21+00:00 discovered by CG-515


## Reviewed scope

After CG-515 lands, reproduce the named regression against accepted source and establish whether the production refresh or only the mutable test fake violates the repository-observation contract. A refreshed manual/linked PR must record its current identity and conflict state without relying on mutation of an obsolete returned object. Correct the actual defect and use focused deterministic refresh regressions; preserve the original failure and distinguish a fake-only correction from a production fix. This follows CG-475 polling ownership rather than reimplementing polling.
- 2026-09-10T13:21:20+00:00 approved (delegated operator all-Inbox review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:32:12+00:00 dispatched work run 20260910T173212Z-work via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~18568 tokens)
- 2026-09-10T17:37:56+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:41:19+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$0.07
- 2026-09-10T18:34:04+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:06+00:00 opened https://github.com/joshmarcus/context-garden/pull/460 (base main): Aligned both fake providers with fresh PR observation semantics and added identity regression coverage. Focused scheduler/fake tests pass: 52 passed.
- 2026-09-10T18:34:06+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T18:37:49+00:00 automated review: approve — The fake-only snapshot correction matches production provider semantics and repairs manual PR refresh without changing scheduler behavior. cost=$0.32
- 2026-09-10T18:40:36+00:00 automated review: approve — The fake providers now return distinct PR objects, matching production refresh semantics and repairing manual PR identity/conflict refresh behavior. cost=$0.30
- 2026-09-10T18:43:41+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/460
