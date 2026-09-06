---
id: CG-327
title: 'The live-garden fence attributes only the worker''s own writes: the operator''s and the scheduler''s
  commits during a run''s window are never counted against the run'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/fence.py
- src/garden/scheduler/reap.py
- src/garden/runs.py
- tests/test_fence.py
branch: garden/cg-327-the-live-garden-fence-attributes-only-the-worker
last_dispatched_at: '2026-09-06T13:04:44+00:00'
created: '2026-09-06T04:28:19+00:00'
updated: '2026-09-06T13:13:32+00:00'
---

## Goal

A run is fenced only for writes the run made. The live-garden check attributes a change to the worker when the worker's own transcript shows the write (a tool call or a shell command that names a path under the garden root or the product clone), or when the change is to a guarded file the fence snapshotted for that run and no other actor touched it; commits in the garden repo during the run's window by the operator (`garden` CLI, the web UI, a person's git) or by the scheduler's own `garden commit` are never attributed to the run. A false attribution is worse than a missed one here, because it discards a finished run.

## Context

2026-09-06 04:04Z: Fable's Now 1 design revise (run 20260906T033749Z-revise, $9.20, 27 minutes) was marked "fenced: worker wrote outside its worktree; the writes it made were reverted. Touched the live garden: wrote context-garden/phase-05/specs/now-page.md and 10 commit(s)". Every one of those ten commits was the operator editing the Now page spec and the scheduler's task-state commits during the run's window; the worker's transcript shows no write under the garden root. The run's result was thrown away and the task failed. The fence's snapshot for the run listed garden.yaml and state.json only, so the "wrote the spec" claim came from the repo-wide window check, not from evidence.

## Acceptance criteria

- [ ] A garden-repo commit or file change during a run's window is attributed to the run only with evidence from the run's own transcript or from a guarded-file snapshot mismatch; the operator's CLI, the web UI and `garden commit` are recognised actors and never counted; a test replays this incident (spec edited and committed by the operator mid-run) and the run is reaped as done.
- [ ] A real worker write under the garden root (a shell redirect in the transcript) is still fenced, and the log line names the transcript evidence.
- [ ] A fenced run's own worktree writes are kept, not reverted, when the fence fires for a live-garden write; only the out-of-worktree writes are reverted, and the log line says which.

## Log
- 2026-09-06T04:28:20+00:00 approved (cli)
- 2026-09-06T11:04:12+00:00 dispatched work run 20260906T110121Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11491 tokens)
- 2026-09-06T12:13:41+00:00 pre-PR checks failed (test); no PR opened yet; revise run will fix cost=$1.98
- 2026-09-06T12:41:53+00:00 dispatched revise run 20260906T124150Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11892 tokens)
- 2026-09-06T12:52:43+00:00 environment stop (auth): auth limit hit on codex; not counted as an attempt; dispatch paused for codex until a probe succeeds
- 2026-09-06T13:04:44+00:00 dispatched work run 20260906T130442Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11698 tokens)
- 2026-09-06T13:07:04+00:00 attempt 2 failed: no GARDEN_RESULT in worker output (see final.md); giving up
- 2026-09-06T13:13:32+00:00 reset to ready by hand
