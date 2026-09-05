---
id: CG-212
title: A usage or spend-limit error from a harness pauses dispatch for that harness and leaves the task
  ready, instead of burning attempts and failing tasks
status: running
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/harness.py
- src/garden/scheduler/reap.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/budget.py
- src/garden/inbox.py
- context-garden/phase-02-friction/tasks/CG-033-an-environment-error-in-a-worker-pauses-dispatch.md
branch: garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus
attempts: 1
last_dispatched_at: '2026-09-05T15:33:56+00:00'
created: '2026-09-05T15:32:11+00:00'
updated: '2026-09-05T15:33:56+00:00'
---

## Goal

When a worker exits because the harness's account is out of quota (Claude: "You've hit your monthly spend limit"; Codex: "You've hit your usage limit. Upgrade to Pro"), the scheduler treats it as an environment stop, not the task's failure: the attempt is not counted, the task returns to `ready`, dispatch is paused for that harness with the reason on the Inbox and in `garden status`, and dispatch resumes by itself when a cheap probe succeeds (or when a person presses resume). A run killed this way leaves its worktree usable: uncommitted edits are stashed under a named stash before the next dispatch (CG-198 covers the stash; this task makes sure the limit path reaches it).

## Context

2026-09-05: between 13:12 and 13:37 the Claude account hit its monthly spend limit; twenty-six worker exits carried the message, every affected task burned both attempts within a minute and twelve tasks went `failed`; the operator retried them by hand at 14:33 and two of the retries then failed on dirty worktrees. At 15:25 the Codex trial on CG-158 hit the ChatGPT usage limit the same way and failed the same way. CG-033 (phase 02) asked for exactly this for login and binary errors and was cancelled; the limit messages are a third, more common case. The harness already parses `is_error` results.

## Acceptance criteria

- [ ] `Harness.parse` (claude and codex) classifies a quota or spend-limit message as `env_error` with `kind: quota`; the message patterns are configurable per harness.
- [ ] On a quota env_error the run is closed without counting an attempt, the task goes back to `ready` with a log line, and `_control.paused_harnesses[<harness>]` is set with the reason; dispatch skips tasks whose resolved harness is paused and the Inbox shows one notice for it.
- [ ] Every few ticks (configurable, default 10 minutes) the scheduler probes the paused harness with a one-line prompt; on success it clears the pause and emits `dispatch_resumed` with the harness name.
- [ ] Before any dispatch, a dirty worktree is stashed with the run id in the stash name and noted on the task (shared with CG-198).
- [ ] Tests with the fake harness for both messages, the pause, the probe and the resume.

## Log

- 2026-09-05T15:32:12+00:00 approved (web)
- 2026-09-05T15:33:56+00:00 dispatched work run 20260905T153346Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~20700 tokens)
