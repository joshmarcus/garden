---
id: CG-241
title: 'Complete CG-239: contain reading paths and scheduler git'
status: cancelled
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: hard
reading: []
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: The security review demonstrates both arbitrary local-file disclosure into model
  prompts and worker-triggered code execution with scheduler credentials.
retro_blocking: true
created: '2026-09-05T23:15:09+00:00'
updated: '2026-09-05T23:57:12+00:00'
---

## Goal

Reuse existing draft CG-239; do not create a replacement. Refuse absolute and parent-traversing reading entries and symlink escapes, enforce resolved-root containment and expose violations as brief gaps. Protect shared clone config, hooks, the worktree .git file and worktree metadata before any scheduler git can execute changed configuration; neutralize unsafe hooks and fsmonitor and address credential-helper execution. Hash checks performed only after an unsafe git command are insufficient. Reproduce the supplied shared-config attack and verify it cannot execute in the scheduler.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: The security review demonstrates both arbitrary local-file disclosure into model prompts and worker-triggered code execution with scheduler credentials.

## Log

- 2026-09-05T23:15:09+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:57:12+00:00 cancelled by the joined retro (2026-09-05 23:55Z): duplicate of CG-239, which is already merged or in review
