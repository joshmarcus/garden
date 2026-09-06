---
id: CG-245
title: Isolate planner execution from operator state
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: A stated phase trust goal remains unshipped, and model-written documents currently
  drive an edit-capable process in the live garden with operator credentials.
retro_blocking: true
created: '2026-09-05T23:15:10+00:00'
updated: '2026-09-05T23:59:48+00:00'
---

## Goal

Route synchronous planning through the worker environment and a scratch directory with only the capabilities needed to read approved context and return a plan. Do not inherit operator HOME or unrestricted tokens, and enforce the common brief gate on generated work. Cover planner and synchronous kickoff paths with malicious document input and assertions about environment, filesystem and allowed operations.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: A stated phase trust goal remains unshipped, and model-written documents currently drive an edit-capable process in the live garden with operator credentials.

## Log

- 2026-09-05T23:15:10+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:58:00+00:00 moved from context-garden/phase-04 to context-garden/phase-05
- 2026-09-05T23:59:48+00:00 approved by the retro reopen verdict
