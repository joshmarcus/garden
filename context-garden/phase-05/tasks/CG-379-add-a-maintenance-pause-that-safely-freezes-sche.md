---
id: CG-379
title: Add a maintenance pause that safely freezes scheduling and collection
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
branch: garden/cg-379-add-a-maintenance-pause-that-safely-freezes-sche
pr: https://github.com/joshmarcus/context-garden/pull/288
attempts: 1
last_dispatched_at: '2026-09-07T11:59:54+00:00'
created: '2026-09-07T11:43:56+00:00'
updated: '2026-09-07T15:24:00+00:00'
---

## Goal

Provide a maintenance pause suitable for reinstalling/restarting the scheduler. Finish the current scheduler transaction, then stop all scheduling and result collection. Durably saved uncollected results do not prevent maintenance; the next scheduler collects them after explicit resume.

## Context

Owner requested this after the2026-09-07 rollout was repeatedly delayed: ordinary pause prevented new workers but continued starting checks/reviews, so the queue never reliably drained. A proposed collection-until-empty requirement was unnecessarily strict. Existing processes and saved results must remain intact, without letting scheduling race the installer. This is not fast-forward mode or a request to kill active workers.

## Acceptance criteria

- [ ] Expose explicit maintenance-pause and resume through supported UI/CLI/API. Document its difference from ordinary admission pause. Acknowledgment distinguishes requested from quiesced; quiesced means the current scheduler transaction has completed and no scheduler collection/mutation is in flight.
- [ ] While quiesced, no new worker/review/check/rebase/persona/retro/merge or result-collection action starts, including manual dispatch endpoints and background callbacks. Read-only health/status and explicit maintenance resume remain available. Persist mode across service restarts.
- [ ] Active processes may finish and atomically save durable results; do not delete artifacts, fabricate terminal statuses or require collection before maintenance. Enumerate actual live/preparing processes separately from finished-but-uncollected records.
- [ ] Report reinstall readiness based on transaction quiescence and live processes that depend on the installed runtime. Pending durable results alone do not block readiness. Identify concrete blockers; do not declare arbitrary live workers safe solely from a PID or require an empty backlog.
- [ ] On explicit resume after reinstall/restart, reconcile saved old-version results exactly once through supported state transitions, preserve feedback/PR identity/costs and avoid duplicate dispatch or merge. Define behavior for incompatible result schema and interrupted collection with honest actionable recovery.
- [ ] A disposable integration test pauses during a tick, lets a worker finish while quiesced, replaces/restarts the scheduler, and resumes collection exactly once. Cover denied manual dispatch, no queued review/check starting, restart-persistent pause, atomic result visibility and runtime-dependent live-process blockers. No fault injection on the live garden.

## Log

- 2026-09-07T11:43:57+00:00 approved (web)
- 2026-09-07T11:59:54+00:00 dispatched work run 20260907T115951Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9603 tokens)
- 2026-09-07T12:17:55+00:00 preserved uncommitted worktree changes from run 20260907T115951Z-work outside the PR: `git stash apply f7642c4469659ec9cdece89da36b4cd8c0a39c03` in /home/joshua/work/worktrees/CG-379 (garden:CG-379:20260907T115951Z-work:reap)
- 2026-09-07T12:20:28+00:00 opened https://github.com/joshmarcus/context-garden/pull/288 (base main): Adds a durable maintenance pause that quiesces scheduler transactions, blocks scheduler launch paths, and leaves finished results for explicit post-restart collection. It exposes CLI, web, and read-only API controls plus reinstall-readiness reporting. cost=$1.55
- 2026-09-07T13:01:10+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/288
- 2026-09-07T15:24:00+00:00 automated review could not start: CG-379 is done: #288 was merged at 13:01:10
