---
id: CG-194
title: Workers get no HOME, retry_command comes only from config, and the fence hash-checks garden.yaml
  and state.json
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: medium
reading: []
branch: garden/cg-194-workers-get-no-home-retry-command-comes-only-fro
pr: https://github.com/joshmarcus/context-garden/pull/158
discovered_from: retro:context-garden/phase-03
attempts: 2
last_dispatched_at: '2026-09-05T14:59:37+00:00'
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T15:15:49+00:00'
---

## Goal

**User value:** a worker or a branch's test suite cannot read the operator's gh token, cannot forge an approve verdict into .garden/state.json, and cannot run a shell command through a check's JSON output; the docs say exactly what is and is not isolated.

**Why now:** the security persona verified all three on the phase-03 build and with automerge on they chain into a self-approved merge.

**Size:** medium. **Depends on:** CG-164 and CG-165 (merged) for the shared allowlist. Also hold automerge when a diff touches garden*.yaml, **/tasks/, .github/ or principles/, and require a loopback Host on POSTs.

## Context

Proposed at the context-garden/phase-03 retro. Phase 03 claimed trust at the edges; the verified gaps are small, local fixes that make the claim true.

## Log

- 2026-09-05T10:31:17+00:00 approved (web)
- 2026-09-05T12:42:19+00:00 dispatched work run 20260905T124209Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4384 tokens)
- 2026-09-05T13:14:21+00:00 opened https://github.com/joshmarcus/context-garden/pull/158 (base main): Isolated the worker/check HOME so a branch cannot read the operator's gh token; made retry_command config-only and scrubbed; added a fence hash-check for garden*.yaml and .garden/state.json; held automerge on diffs touching config/tasks/CI/principles; required a loopback Host on POSTs; documented the isolation boundary. 634 tests pass (+10 new), lint clean. cost=$14.82
- 2026-09-05T13:14:28+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/poll.py); a rebase agent will resolve it
- 2026-09-05T13:14:42+00:00 dispatched rebase run 20260905T131442Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~7672 tokens)
- 2026-09-05T13:16:00+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:16:17+00:00 dispatched work run 20260905T131617Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4814 tokens)
- 2026-09-05T13:17:48+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:33:47+00:00 re-enabled by hand; revise run will follow
- 2026-09-05T14:59:37+00:00 dispatched revise run 20260905T145937Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~5281 tokens)
- 2026-09-05T15:07:04+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/158: Rebased the CG-194 branch onto current main (resolving conflicts in poll.py's automerge gate and architecture.md docs by keeping both this branch's and main's additions), since GitHub reported no open review comments or CI checks — the PR's only outstanding blocker was the merge conflict already flagged in the task log. Full suite (714 passed, 3 skipped) and lint are clean afterward. cost=$0.65
- 2026-09-05T15:11:36+00:00 automated review: approve — HOME isolation, config-only scrubbed retry_command, config/state hash-check, guarded-path automerge hold, and the loopback-Host POST guard are all correctly implemented and tested; docs updated accurately; full suite and lint clean. cost=$0.78
- 2026-09-05T15:11:51+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T15:14:20+00:00 rebased; diff unchanged; verdict kept
- 2026-09-05T15:15:49+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/158
