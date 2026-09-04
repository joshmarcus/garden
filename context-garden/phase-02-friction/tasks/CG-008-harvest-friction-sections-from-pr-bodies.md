---
id: CG-008
title: Harvest friction sections from PR bodies
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
estimate: M
difficulty: medium
reading:
- context-garden/phase-02-friction/specs/friction-log.md
- context-garden/phase-01-bootstrap/specs/scheduler.md
branch: garden/cg-008-harvest-friction-sections-from-pr-bodies
pr: https://github.com/joshmarcus/context-garden/pull/9
attempts: 1
last_dispatched_at: '2026-09-04T17:04:23+00:00'
created: '2026-09-04T00:00:00+00:00'
updated: '2026-09-04T17:18:08+00:00'
---

## Goal

Add `garden friction <product>/<phase>` that collects `## Friction` sections from task PR bodies into `<phase>/docs/friction.md`.

## Context

The last work or revise run of a task keeps the PR body it wrote in `run.json` (`result.pr_body`, see `RunStore`); use that first so the command works offline, and fall back to `GitHub.get_pr`, whose `PRInfo.body` already carries the live body. The planner already includes `docs/*.md`, so the file it writes is read on the next `garden plan`.

## Acceptance criteria

- [ ] Command writes a grouped markdown file with task id, title, PR link and the friction text.
- [ ] Running it twice is idempotent.
- [ ] Unit test with a fake GitHub object.
- [ ] Web UI task detail shows the friction section if present.

## Out of scope

- Summarising the friction with a model.

## Log

- 2026-09-04T16:00:55+00:00 status forced to draft
- 2026-09-04T17:03:43+00:00 approved
- 2026-09-04T17:04:23+00:00 dispatched work run 20260904T170423Z-work via local [claude model=sonnet] (fresh session, base main, ~2945 tokens)
- 2026-09-04T17:12:51+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/9 (base main): Added `garden friction <product>/<phase>` CLI command that harvests `## Friction` sections from task PR bodies (run.json first, GitHub fallback) and writes `<phase>/docs/friction.md`. The web UI task detail page now shows a Friction panel when one is present. All acceptance criteria met: grouped markdown output, idempotent, unit tests with fake GitHub, web UI panel. cost=$1.77
- 2026-09-04T17:14:58+00:00 automated review: approve — All four acceptance criteria met; tests pass and lint is clean. One minor description inaccuracy (17 tests in test_friction.py, not 19) and a non-blocking note that the web UI friction panel only reads from run-store data, not the GitHub fallback. cost=$0.31
- 2026-09-04T17:17:26+00:00 triage: marked ready for review
- 2026-09-04T17:18:08+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/9
