---
id: CG-426
title: Keep stress and load tests out of the default test suite
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: easy
reading:
- pyproject.toml
- tests/conftest.py
- tests/test_web.py
- docs/test-suites.md
- .github/workflows/ci.yml
branch: codex/cg426-opt-in-stress
pr: https://github.com/joshmarcus/context-garden/pull/309
runner: manual
created: '2026-09-08T12:28:50+00:00'
updated: '2026-09-08T12:40:09+00:00'
---

## Goal

Ordinary test runs and CI must not run stress/load experiments. The owner reported workers hitting these workloads in pytest on 2026-09-08.

## Acceptance criteria

- [ ] Mark retained-history latency, generated CPU/memory workload, and concurrent served overload experiments as stress; normal pytest/CI deselect them before fixtures execute.
- [ ] Require deliberate opt-in including explicit stress node/marker selection; keep lightweight functional concurrency regressions in the normal suite.
- [ ] Document the separate bounded stress command and worker policy; verify selection without stressing production.
- [ ] Focused functional validation, lint and exact-head CI pass before merge.

## Log

- 2026-09-08T12:28:50+00:00 Owner requested stress tests excluded. Direct operator implementation reserved; do not dispatch another implementation.
- 2026-09-08T12:35:50+00:00 Direct operator patch887dbf76 in PR309. Default collection1598/1602; all4stress cases deselected even explicit node/marker selection. Opt-in collection selects4;2functional tests/lint pass. Full CI pending.
- 2026-09-08T12:39:41+00:00 approved (web)
- 2026-09-08T12:40:09+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/309
