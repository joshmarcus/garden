---
id: CG-242
title: Hold untrusted config changes before live reload
status: running
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/config.py
- src/garden/store.py
- src/garden/scheduler/fence.py
- src/garden/scheduler/reap.py
- src/garden/scheduler/__init__.py
- tests/scheduler/test_reap.py
- tests/test_store.py
branch: garden/cg-242-hold-untrusted-config-changes-before-live-reload
pr: https://github.com/joshmarcus/context-garden/pull/199
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: Live reload currently activates a worker's configuration write before the fence
  can reject it, creating a newly introduced privileged execution path.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-06T02:55:45+00:00'
created: '2026-09-05T23:15:09+00:00'
updated: '2026-09-06T02:55:45+00:00'
---

## Goal

Before applying changed garden configuration, compare it with active worker fence manifests and hold mismatches until trusted resolution or reap recovery. Cover executable command fields, harness binaries and worker_env.pass; preserve legitimate operator changes without accepting a worker write early. Emit a visible held-reload event and test a worker shell write followed by a tick before reap.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: Live reload currently activates a worker's configuration write before the fence can reject it, creating a newly introduced privileged execution path.

## Acceptance criteria

- [ ] When garden.yaml (or a layered garden.*.yaml) changes on disk while any worker run is in flight, the per-tick reload compares the executable fields (notify.command, checks, setup.command, harness bin and command, worker_env.pass, retry_command) with the fence manifest each in-flight run was dispatched under; a mismatch holds the reload, emits a `config_reload_held` event naming the keys and the run, and the Inbox shows one notice.
- [ ] A held reload is applied once every in-flight run has been reaped (the fence attributes and reverts a worker write) or once the operator confirms the change (`garden config accept` or the Config page); a legitimate operator edit with no runs in flight applies within a tick as before.
- [ ] Test with the fake harness: a worker's shell write to notify.command followed by a tick before reap does not run the new command; the fence reverts it at reap and the reload resumes; an operator edit with no runs in flight applies at once.
- [ ] The Config page lists the held keys and the runs holding them.

## Log

- 2026-09-05T23:15:09+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:59:06+00:00 approved (cli)
- 2026-09-06T00:00:58+00:00 dispatched work run 20260906T000043Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~17423 tokens)
- 2026-09-06T00:39:34+00:00 opened https://github.com/joshmarcus/context-garden/pull/199 (base main): Implemented a live-reload gate that holds an executable-field garden.yaml change against any in-flight fenced run's config until the run is reaped or an operator confirms it, with CLI/web surfaces and tests proving a worker's notify.command write never runs early. cost=$11.15
- 2026-09-06T00:39:41+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/fence.py, tests/test_fence.py); a rebase agent will resolve it
- 2026-09-06T00:40:12+00:00 dispatched rebase run 20260906T004011Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~12254 tokens)
- 2026-09-06T00:48:07+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/199: Rebased onto origin/main, resolving two textual conflicts in src/garden/scheduler/fence.py (module docstring) and tests/test_fence.py (import block) by combining both sides' content rather than choosing one; no logic changed. Full test suite (985 passed, 3 skipped) and tests/test_fence.py (20 passed) verified green after rebase. cost=$0.26
- 2026-09-06T00:59:10+00:00 automated review requested changes: The hold/accept mechanism, tests, and docs are solid, but the fix is incomplete: garden canary's _drive() loop still calls the unconditional store.invalidate() after every tick, leaving one live route around the new gate that the PR's own docs claim doesn't exist. cost=$1.31
- 2026-09-06T01:01:02+00:00 dispatch failed: [Errno 28] No space left on device: '/tmp/garden-empty-hooks-vbiklx7n'
- 2026-09-06T01:46:22+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T01:51:53+00:00 dispatched revise run 20260906T015152Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~15662 tokens)
- 2026-09-06T01:57:49+00:00 revision failed: no GARDEN_RESULT in worker output (see final.md)
- 2026-09-06T02:04:20+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T02:14:59+00:00 kept 1 local-only commit(s) on `backup/20260906T021458Z-revise` before syncing to origin/garden/cg-242-hold-untrusted-config-changes-before-live-reload's head: 6fada6b Close the canary's own route around the config-reload gate
- 2026-09-06T02:14:59+00:00 dispatched revise run 20260906T021458Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~16965 tokens)
- 2026-09-06T02:28:05+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/199: Closed the canary route that could unconditionally adopt a held executable config reload. The fix is committed as a9db9f9 and all local checks pass. cost=$0.60
- 2026-09-06T02:42:56+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/retro.py, src/garden/store.py); a rebase agent will resolve it
- 2026-09-06T02:43:30+00:00 dispatched rebase run 20260906T024330Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~19382 tokens)
- 2026-09-06T02:51:56+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/199: Rebased onto origin/main and resolved the two marked conflicts while preserving both sides' intent. cost=$0.01
- 2026-09-06T02:54:58+00:00 automated review requested changes: A fresh `garden tick` process loads the worker-modified config before the gate compares it, so it can execute untrusted settings before reap. The focused acceptance tests pass, but only retain the same Scheduler instance. cost=$0.36
- 2026-09-06T02:55:45+00:00 dispatched revise run 20260906T025544Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~13439 tokens)
