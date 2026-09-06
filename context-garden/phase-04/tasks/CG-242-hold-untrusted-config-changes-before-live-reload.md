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
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: Live reload currently activates a worker's configuration write before the fence
  can reject it, creating a newly introduced privileged execution path.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-06T00:00:58+00:00'
created: '2026-09-05T23:15:09+00:00'
updated: '2026-09-06T00:00:58+00:00'
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
