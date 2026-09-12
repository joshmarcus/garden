---
id: CG-445
title: Make onboarding discovery ignore transient pytest cache
status: cancelled
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/scheduler/review.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/aux.py
- src/garden/runs.py
- src/garden/inbox.py
- tests/test_review.py
- tests/test_runners.py
discovered_from: CG-438
created: '2026-09-08T17:49:27+00:00'
updated: '2026-09-08T19:23:55+00:00'
file: src/garden/onboard.py
error: 'Full suite failure: expected `GitHub repository metadata` in onboarding report after earlier tests
  created `.pytest_cache`.'
---

The repository onboarding regression changes its report when `.pytest_cache` exists in the source checkout, causing `test_onboard_this_repository_uses_documented_setup_and_ci_tests` to miss its expected GitHub metadata note. Exclude transient test caches from project discovery so full-suite execution does not alter onboarding results.

## Provenance

Discovered by CG-438 (Preserve review requests through unclaimed timeout and admission recovery) during run `20260908T170122Z-work`.
## Log
- 2026-09-08T17:49:27+00:00 discovered by CG-438
- 2026-09-08T19:23:55+00:00 Consolidated into active CG432, which already owns deterministic transport/unavailable-metadata onboarding behavior; reporter evidence retained there.
