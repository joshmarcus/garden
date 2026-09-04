---
id: CG-064
title: Make test_feedback_triggers_revise_round deterministic
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- tests/test_scheduler.py
- tests/conftest.py
- tests/fake_claude.py
created: '2026-09-04T18:24:37+00:00'
updated: '2026-09-04T18:24:37+00:00'
---

## Goal

`tests/test_scheduler.py::test_feedback_triggers_revise_round` passes every time, on GitHub Actions and under local load, and the cause of its intermittent second PR is understood and removed.

## Context

Failed twice on 2026-09-04: once as a pre-PR check while two other workers loaded the machine, once on GitHub Actions for PR #29 (a change to brief wording, nowhere near this path), with `assert len(fake_github.created) == 1` seeing 2. It passed 36 of 36 local runs in three parallel streams and in the eleven other CI runs that day, so it is timing. The likely seam: `wait_for_runs` returns when every active run has an `exit_code`, but the reap of the revise run must find the existing PR through `find_pr(slug, branch)` on the fake; if the run record or the task's branch is read before the fake worker's commit lands, or two ticks overlap on the run directory, `finalize` takes the open-a-new-PR path. Reproduce by adding jitter to the fake harness (sleep before writing stdout and exit_code) and by running the test under `pytest -p xdist`-style load, then fix the real race in `finalize` or the fake, not the assertion.

## Acceptance criteria

- [ ] the cause is named in the PR and covered by a test that fails before the fix under injected delay.
- [ ] 50 consecutive local runs pass under load; CI is green.
