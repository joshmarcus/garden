---
id: CG-359
title: Preserve unrelated worktree changes without adding them to recovered PRs
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
created: '2026-09-06T19:13:47+00:00'
updated: '2026-09-06T19:13:47+00:00'
---

## Goal

Recover worker results without silently adding unrelated dirty artifacts to the task's PR; preserve those artifacts and provenance separately.

## Context

In CG-357 the worker explicitly left docs/design/snapshot.json uncommitted. Scheduler leftover salvage committed it in7b818c4 and again1b8d31c after an operator cleanup, adding tens of thousands of unrelated runtime-state lines to PR234. Review rejected the diff and operator had to preserve/remove it twice. CG-333 salvages already committed work when a result is missing; coordinate with that task rather than weakening recovery or discarding dirty data. See context-garden/docs/incidents/2026-09-06-web-responsiveness-retro.md.

## Acceptance criteria

- [ ] Track pre-existing dirty changes and provenance at dispatch; recovery does not blindly commit every modified/untracked file or treat a worker's excluded artifact as part of its completed result.
- [ ] Preserve ambiguous/unrelated changes in a documented recovery artifact or equivalent safe location, with task/run references and clear restoration instructions. Never delete them merely to obtain a clean PR.
- [ ] A completed worker with intended commits plus an unrelated dirty snapshot opens/updates a PR containing only intended changes. A second revise/reap cycle cannot reintroduce the preserved snapshot.
- [ ] Missing-result salvage still preserves intended committed work per CG-333. Cover pre-existing edits, intentional new files, interrupted runs and repeated recovery with regression tests; do not use a blanket filename denylist that blocks a legitimate snapshot task.

## Counterfactual

Provenance-aware salvage would have prevented repeated enormous unrelated diffs, review failures and manual cleanup during incident restoration.
