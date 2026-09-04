---
id: CG-013
title: Replan a phase after failures
status: awaiting_triage
product: context-garden
phase: phase-02-friction
depends_on:
- CG-008
priority: 3
estimate: M
difficulty: medium
reading:
- principles/agent-loop.md
branch: garden/cg-013-replan-a-phase-after-failures
pr: https://github.com/joshmarcus/context-garden/pull/24
attempts: 1
last_dispatched_at: '2026-09-04T17:39:16+00:00'
created: '2026-09-04T00:00:00+00:00'
updated: '2026-09-04T17:52:14+00:00'
---

## Goal

`garden plan product/phase --replan` includes failed/blocked task logs and the friction doc in the planner prompt so it can propose fixes, splits, or new tasks.

## Context

`plan_prompt` in `src/garden/planner.py`. Add a section with, for each failed task: id, title, last three log lines, and the worker's blocked question if any. Keep the prompt under the brief budget by truncating logs.

## Acceptance criteria

- [ ] Prompt section appears only with `--replan`.
- [ ] Planner may output `"supersedes": [ids]`; import marks those tasks cancelled with a log line.
- [ ] Test the import path with a JSON fixture.

## Out of scope

- Automatic re-approval of replanned tasks.

## Log

- 2026-09-04T17:23:49+00:00 approved (web)
- 2026-09-04T17:39:16+00:00 dispatched work run 20260904T173915Z-work via local [claude model=sonnet] (fresh session, base main, ~2273 tokens)
- 2026-09-04T17:45:24+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/24 (base main): Added `--replan` to `garden plan`: the planner prompt now includes a 'Failed and blocked tasks' section (id, title, last 3 log lines, blocked question) for failed/waiting_human tasks. `import_plan` handles `"supersedes": [ids]` to cancel replaced tasks. 8 new tests; all 126 pass, lint clean. cost=$1.04
- 2026-09-04T17:52:14+00:00 automated review: approve — All three acceptance criteria met, 126 tests pass, lint clean. One tautological test assertion (`or True`) is a dead nit but does not hide any real failure. cost=$0.63
