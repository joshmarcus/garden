---
id: CG-243
title: redispatch kills the superseded worker, and pin runs the canary, installs and restarts after a
  tick
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:05:56+00:00'
updated: '2026-09-05T23:05:56+00:00'
---

## Goal

**User value:** the two recurring operator hand sequences become one command each; re-dispatching from codex to fable left two workers in one worktree and cost $4.34 for a run with no PR.

**Why now:** both were done by hand several times this phase and each is a known failure mode.

**Size:** medium. **Depends on:** CG-180, CG-198 (merged).

## Context

Proposed at the context-garden/phase-04 retro. Operator hand steps are the operator-spend goal in another form.
