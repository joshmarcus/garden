---
id: CG-460
title: Stabilize onboarding metadata fixture on worker checkouts
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
created: '2026-09-09T00:30:28+00:00'
updated: '2026-09-09T01:05:18+00:00'
file: tests/test_onboard.py
error: Expected `GitHub repository metadata` was absent from onboarding.md; reproduced in the exact focused
  rerun and the path is unchanged from origin/main.
---

The ordinary suite consistently fails `test_onboard_this_repository_uses_documented_setup_and_ci_tests` because the generated report omits the expected GitHub repository metadata section when `_gh_json` is mocked unavailable. Diagnose and make the fixture expectation independent of checkout metadata.

## Provenance

Discovered by CG-438 (Preserve review requests through unclaimed timeout and admission recovery) during run `20260908T235138Z-revise-2`.
## Log
- 2026-09-09T00:30:28+00:00 discovered by CG-438
- 2026-09-09T01:05:18+00:00 Consolidated into CG432; same onboarding metadata fixture scope, original discovery retained in both task histories.
