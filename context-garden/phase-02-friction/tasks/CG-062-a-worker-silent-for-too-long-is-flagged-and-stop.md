---
id: CG-062
title: A worker silent for too long is flagged and stopped before the timeout
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- docs/worker-protocol.md
created: '2026-09-04T18:16:39+00:00'
updated: '2026-09-04T18:16:39+00:00'
---

## Goal

A worker that has produced no commit, file change or output for a configurable number of minutes is shown as idle on the Inbox and, past a second threshold, stopped and treated as a failed run, well before `timeout_minutes`.

## Context

During the first live run a sonnet revise worker for CG-032 sat for 13 minutes with no file activity in its worktree, no commits and no output, at under 1% CPU, while the cut-over waited for it. The only signal the garden has today is the pid probe and the 95-minute kill. With stream-json output (CG-009) the last output line's time is known; without it, the worktree's newest mtime and the run's stdout size are enough. Add `idle_minutes` (warn) and `idle_kill_minutes` (stop) to config, show "idle N min" on the running card, and stop the process group at the second threshold the way the timeout does.

## Acceptance criteria

- [ ] a running card shows idle time once nothing has changed for `idle_minutes`.
- [ ] past `idle_kill_minutes` the run is stopped and handled like a timeout (retry or fail).
- [ ] tests with a fake worker that stalls.
