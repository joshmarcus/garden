---
id: CG-242
title: Hold untrusted config changes before live reload
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: Live reload currently activates a worker's configuration write before the fence
  can reject it, creating a newly introduced privileged execution path.
retro_blocking: true
created: '2026-09-05T23:15:09+00:00'
updated: '2026-09-05T23:15:09+00:00'
---

## Goal

Before applying changed garden configuration, compare it with active worker fence manifests and hold mismatches until trusted resolution or reap recovery. Cover executable command fields, harness binaries and worker_env.pass; preserve legitimate operator changes without accepting a worker write early. Emit a visible held-reload event and test a worker shell write followed by a tick before reap.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: Live reload currently activates a worker's configuration write before the fence can reject it, creating a newly introduced privileged execution path.

## Log

- 2026-09-05T23:15:09+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
