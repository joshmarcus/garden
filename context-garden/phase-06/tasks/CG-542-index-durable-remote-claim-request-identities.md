---
id: CG-542
title: Index durable remote claim request identities
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-491
  after: merge
- id: CG-495
  after: merge
- id: CG-496
  after: merge
priority: 3
difficulty: hard
reading:
- src/garden/runs.py
- src/garden/remote_worker.py
branch: garden/cg-542-index-durable-remote-claim-request-identities
pr: https://github.com/joshmarcus/context-garden/pull/465
runner: remote
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T20:47:27+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T21:09:04+00:00'
---

## Goal

User value: keep idle polling responsive as history grows. Why now: historical evidence suggests a residual request-identity lookup cost that must be measured on current accepted source. Size: hard. Dependencies: CG-491/495 and current durable lease/replay rules; preserve rejection of stale, expired and replaced generations while avoiding terminal-history materialization.

## Context

Proposed at the context-garden/phase-05 retro. Measure and remove any remaining material historical lookup cost without weakening idempotency or expanding the worker fleet.


## Reviewed scope and verification

CG-495 already removed the unconditional full-history deep copy from active selection. First measure the remaining current-source claim/request-identity and replay lookup, including index refresh boundaries; report the source and which path scales with historical runs. If a material residual cost remains, index the required durable identities and preserve restart, stale/expired/replaced generations, collision handling and exactly-once accepted results. Use a bounded history-growth regression; do not restate the obsolete unconditional-copy finding or weaken fencing. Retire with evidence if current accepted source already satisfies the intended bound.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:42:03+00:00 dispatched work run 20260910T174202Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14069 tokens)
- 2026-09-10T17:47:12+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:50:28+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$0.67
- 2026-09-10T18:34:17+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:19+00:00 opened https://github.com/joshmarcus/context-garden/pull/465 (base main): Indexed durable remote claim request identities and changed claim replay lookup to copy only the matching run rather than all terminal history. Verified remote worker fencing/replay behavior and bounded history lookup at commit 890a5c8d.
- 2026-09-10T18:34:19+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T18:53:06+00:00 automated review requested changes: The indexed lookup avoids deep-copying terminal history, but periodic index refresh still rebuilds and sorts the entire history, so the requested history-independent idle polling bound is unmet. cost=$0.19
- 2026-09-10T18:55:12+00:00 dispatched revise run 20260910T185512Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15140 tokens)
- 2026-09-10T18:59:28+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:01:03+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/465: Indexed durable remote claim identities remain available for replay, and unchanged age-based refreshes now return after cheap freshness checks without traversing or rebuilding terminal history. Verified at commit 8ae487fb with 107 focused run-index and remote-worker tests, repository-wide Ruff lint, and git diff checks. cost=$0.59
- 2026-09-10T19:08:15+00:00 automated review requested changes: The durable identity lookup works and unchanged age-based refreshes are cheap, but changed-bucket refreshes still make claim polling scale with terminal history. cost=$0.26
- 2026-09-10T19:08:46+00:00 dispatched revise run 20260910T190846Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15488 tokens)
- 2026-09-10T19:16:59+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:18:28+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/465: Run-index refreshes now replace only changed task-bucket contributions for durable claim identities, active runs, and totals, avoiding traversal or sorting of unrelated terminal history during idle claim polling. Verified at commit b9807777 with 108 focused tests, repository-wide Ruff lint, and clean diff/worktree checks. cost=$1.84
- 2026-09-10T19:22:23+00:00 automated review: approve — The durable claim-identity index preserves replay and fencing semantics while keeping unchanged and single-bucket refreshes independent of unrelated terminal history. cost=$0.30
- 2026-09-10T20:02:36+00:00 triage: changes requested by hand: Correct actual full-CI34519480295 on b9807777:50failed/2578passed. RunStore.totals() returns an empty dictionary for a f
- 2026-09-10T20:06:51+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T20:08:07+00:00 dispatched revise run 20260910T200807Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15799 tokens)
- 2026-09-10T20:13:11+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T20:14:37+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/465: Initialized the incremental run index with the complete zero-valued totals schema, preserving it for fresh and empty histories without consumer-side fallbacks. Verified the accepted claim/replay/index behavior with 109 focused tests, empty-store CLI/web behavior with 30 focused tests after the final edit, and repository-wide Ruff lint; committed as 77ab0c39. cost=$0.88
- 2026-09-10T20:17:06+00:00 automated review requested changes: Live-bucket claim lookups and empty-history totals work, but an archive-ledger change still makes the next claim poll rebuild the entire archived index. cost=$0.43
- 2026-09-10T20:46:35+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T20:47:27+00:00 dispatched revise run 20260910T204727Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16410 tokens)
- 2026-09-10T20:52:58+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T20:54:16+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/465: Archive-ledger refreshes now identify and reload only changed per-task archive buckets while retaining compatibility with existing version-1 archives. Verified at f61cdd1a with 111 focused run-index and remote-worker tests plus repository-wide Ruff lint. cost=$1.38
- 2026-09-10T20:58:03+00:00 automated review: approve — Durable remote claim identities are indexed with task-bucket-granular live and archive refreshes, preserving replay behavior without materializing unrelated terminal history. cost=$0.92
- 2026-09-10T21:06:37+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T21:09:04+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/465
