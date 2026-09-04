---
id: CG-073
title: Task page shows every run's transcript and final message
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/web/app.py
- src/garden/web/templates/task.html
- src/garden/runs.py
- src/garden/harness.py
branch: garden/cg-073-task-page-shows-every-run-s-transcript-and-final
pr: https://github.com/joshmarcus/context-garden/pull/70
attempts: 1
last_dispatched_at: '2026-09-04T22:34:44+00:00'
created: '2026-09-04T18:49:18+00:00'
updated: '2026-09-04T22:44:51+00:00'
---

## Goal

From a task page a person can open any of the task's runs and read what the worker did: the brief it got, its transcript (tool calls, messages, errors) and its final message with the result line, live while it runs and afterwards.

## Context

Asked during the first live run: clicking through to a task shows only the task's own log, one line per transition, and the person expected the session. Everything needed is already on disk under `.garden/runs/<task>/<run>/`: `brief.md`, `command.txt`, `stdout.json` (one JSON object for `claude-json`, one event per line for stream-json once CG-009 lands), `stderr.log`, `final.md`, `run.json`. Nothing renders it. Add a per-run page (`/runs/<task>/<run>`) with tabs for brief, transcript, final message and stderr, and a "Runs" section on the task page listing each run with mode, model, minutes, cost and a link. The transcript view renders stream-json events as a readable log (assistant text, tool calls with their command or path, tool results collapsed, the final result) and falls back to the final text for `claude-json` output. Live tail comes from CG-009's partial; this task makes the same view work for finished runs and reachable from the task page. Rename the Inbox's "log" link to say which it opens.

## Acceptance criteria

- [ ] the task page lists the task's runs with links; each run page shows brief, transcript, final message and stderr.
- [ ] stream-json transcripts render tool calls and results readably; `claude-json` runs show the final text.
- [ ] a finished run and a running run open the same page; the running one keeps tailing.
- [ ] tests for the route with a recorded stdout fixture of each format.

## Out of scope

- Live output itself (CG-009).

## Log

- 2026-09-04T18:49:18+00:00 approved
- 2026-09-04T22:34:44+00:00 dispatched work run 20260904T223435Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~11189 tokens)
- 2026-09-04T22:43:29+00:00 opened https://github.com/joshmarcus/context-garden/pull/70 (base main): Added a /runs/<task>/<run> page with Transcript/Brief/Final message/stderr tabs, reachable from the task page. Stream-json renders tool calls and results readably; claude-json falls back to the final text. Running runs keep tailing via a per-run stdout partial; finished runs show the same view. Renamed the runs-list 'log' link to 'open run' and the task header to 'Latest run'. cost=$3.66
- 2026-09-04T22:44:51+00:00 automated review: approve — Adds a /runs/<task>/<run> page with transcript/brief/final/stderr tabs reachable from the task page; all four acceptance criteria are met and tested, tests and ruff pass, diff and description are clean. cost=$0.81
