---
id: CG-138
title: Automerge orders PRs that touch the same file one per cycle instead of letting them rebase against
  each other
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/github.py
created: '2026-09-05T00:47:36+00:00'
updated: '2026-09-05T02:17:27+00:00'
---

## Goal

When several mergeable PRs touch the same file, automerge merges one per poll cycle and holds the others until the next cycle's mergeability check, instead of merging one and sending the rest into simultaneous rebase rounds.

## Context

Measured at the end of the first live run. Fourteen of thirty reviewed PRs went conflicting within a minute of the first merges because they shared `scheduler.py` or `web/app.py`; each then ran a rebase round (one to three dollars, five minutes), several more than once as the next merge landed. GitHub reports the files a PR touches; the poll already knows which PRs are mergeable. Order the automerge candidates so that no two in the same cycle share a file, prefer the one with the fewest shared files, and log "held: shares scheduler.py with #N" on the others. The rebase rounds still exist for real conflicts; this just stops manufacturing them.

## Acceptance criteria

- [ ] two mergeable PRs sharing a file are merged in consecutive cycles, not the same one; the held one's task log says why.
- [ ] PRs with disjoint files merge in the same cycle as before.
- [ ] a test with the fake GitHub covers both.

## Log
- 2026-09-05T00:48:00+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03
- 2026-09-05T02:17:27+00:00 absorbed into the rebase-mode task (merge queue replaces the one-per-cycle hold)
