---
id: CG-442
title: Make onboarding report test consistent with absent GitHub metadata
status: cancelled
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: easy
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
discovered_from: CG-410
created: '2026-09-08T17:03:55+00:00'
updated: '2026-09-08T19:23:55+00:00'
file: tests/test_onboard.py
error: Ordinary fail-fast suite fails at `tests/test_onboard.py::test_onboard_this_repository_uses_documented_setup_and_ci_tests`
  after 903 passing tests.
---

Clarify or correct `test_onboard_this_repository_uses_documented_setup_and_ci_tests`: it mocks `_gh_json` to return `None` but asserts that the onboarding report includes `GitHub repository metadata`. Decide whether absent metadata should still render that heading or adjust the assertion to the intended fallback behavior.

## Provenance

Discovered by CG-410 (Show eligible manual work in Inbox with a safe take action) during run `20260908T163839Z-revise`.
## Log
- 2026-09-08T17:03:55+00:00 discovered by CG-410
- 2026-09-08T19:23:55+00:00 Consolidated into active CG432, which already owns deterministic transport/unavailable-metadata onboarding behavior; reporter evidence retained there.
