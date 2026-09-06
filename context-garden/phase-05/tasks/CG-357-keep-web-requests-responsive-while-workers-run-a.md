---
id: CG-357
title: Keep web requests responsive while workers run and run history grows
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading: []
branch: garden/cg-357-keep-web-requests-responsive-while-workers-run-a
pr: https://github.com/joshmarcus/context-garden/pull/234
attempts: 1
last_dispatched_at: '2026-09-06T18:30:57+00:00'
created: '2026-09-06T17:45:27+00:00'
updated: '2026-09-06T18:59:04+00:00'
---

## Goal

Keep the real application responsive as durable run history grows, including while three workers share the configured CPU/memory limits. Separate live status and historical summaries from full archived logs so opening a page does not scan every past run repeatedly.

## Context

Owner reported the web application inaccessible after normal operation resumed on 2026-09-06 around 17:43 UTC. Requests to /now2 and / timed out from both WSL and Windows at 8–20 seconds, while /favicon.svg returned 200 in 0.02 seconds. The server remained alive. Initial VM available memory was about 6.5 GiB; subsequent worker activity increased service memory toward 3 GiB. Do not assume this is only network failure or fix by raising resource caps.

A py-spy dump of server PID 1440205 showed many concurrent web request threads repeatedly in RunStore.all_runs/runs_for/active, Scheduler.spent_for, build_inbox, Site.ctx and Now snapshot next_queues. Scheduler initialization for page reads also invokes fence migration/startup checks. Approximately 1,546 run records exist; history is durable and keeps growing. Now's phase budget calculation rereads all runs per phase, and page chrome repeats these calculations. Timed-out clients leave expensive synchronous work running, and browser partial requests pile up.

Owner explicitly requested a priority fix and asked about moving history to another location. Merely moving files is insufficient if every request still scans them. Introduce bounded live/status and historical aggregate access, plus safe archival of older terminal-run artifacts where appropriate. Keep historical details available on demand and preserve audit/recovery correctness.

An operator runtime experiment cached Run.load parsing by file stat fingerprint (bounded 2048 entries, deep-copy isolation). Mutation isolation, changed-file visibility and corrupt-file rejection passed, but a subsequent /now2 request still timed out at 20 seconds: this is not a verified fix. Do not treat this experiment as the durable solution. No run history was moved or deleted.

Related: CG-344 reduced duplicated fence manifests; state.json is now about 3.3 MiB, so its old 102 MiB size alone does not explain this incident. CG-338 owns resource admission. Retain the current worker/review limits and service resource caps when validating.

## Acceptance criteria

- [ ] Reproduce the live-history request amplification and identify dominant costs using measured request timings and scan/read counts.
- [ ] Now, Inbox and Board initial loads and updates stay responsive under representative history (at least current size and a substantially larger fixture) and concurrent workers within current caps. Target p95 under 2 seconds for ordinary reads; report actual measurements and limits.
- [ ] Ordinary page and status requests do not repeatedly materialize full run history per phase/task/widget. Shared summaries/indexes have explicit freshness and invalidation behavior; concurrent callers do not trigger an unbounded duplicate scan workload.
- [ ] Active-run transitions, task completion, cost corrections and new records appear promptly; read-only page construction does not repeatedly perform scheduler migrations or mutate recovery state.
- [ ] Old terminal-run logs/artifacts can be archived outside the active working set while preserving run identity, costs, links, review evidence and on-demand historical access. Specify the retention/selection policy and archive location clearly; do not move active, unreaped or recovery-referenced data.
- [ ] Archival is safe to retry after interruption, supports verification/recovery, and does not lose or double-count history. The ordinary UI does not scan the archive for every request. Missing archive data is reported honestly.
- [ ] Regression coverage verifies freshness, concurrent access, archival round trips and bounded work as history increases. Walk through the real app with representative data and record timings, not only screenshots or fixture success.
- [ ] Remove or supersede any temporary operator mitigation during safe installation; document deployment and verification without interrupting active work.

## Out of scope

- Deleting history, silently resetting cost totals, raising CPU/memory caps to hide unbounded work, or a general UI redesign.

## Log

- 2026-09-06T17:48:30+00:00 priority 0 -> 0
- 2026-09-06T17:58:24+00:00 Owner requested server restart; interrupted pre-worker setup superseded, orphaned setup stopped, worktree preserved. Retry startup through capped server.
- 2026-09-06T17:59:34+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply dfeceb430fa1861454701877b65bfd3297b2a691` in /home/joshua/work/worktrees/CG-357 to recover them (garden:CG-357:2026-09-06T17:59:33+00:00)
- 2026-09-06T18:01:06+00:00 dispatched work run 20260906T175931Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~9362 tokens)
- 2026-09-06T18:24:57+00:00 opened https://github.com/joshmarcus/context-garden/pull/234 (base main): Kept web history reads bounded with a shared, freshness-controlled run index; added one-pass phase cost summaries and read-only scheduler construction for pages. Added conservative retry-safe run archival with compact metadata, on-demand historical access, restoration, corruption reporting, and documented deployment. cost=$3.43
- 2026-09-06T18:29:12+00:00 automated review requested changes: The shared index still rebuilds and materializes all active and archived metadata every second, while archived corruption and cost corrections can produce incomplete or stale totals. The performance evidence lacks real concurrent capped workers, and the PR contains extensive unrelated history. cost=$0.34

## Operator revision guidance, 18:30 UTC

Priority is restoring the unavailable application; fix material review findings and validate recovery, not a broad rewrite. Operator preserved the unrelated snapshot at /home/joshua/work/operator-test-tmp/CG357-snapshot-salvage.json and removed its PR diff in a7bab24; do not restore it. Review's claim of 89 unrelated commits is stale-base analysis: after fetching origin/main, only four original CG-357 commits plus this cleanup differ. Do not cherry-pick/rewrite unrelated history on that premise.

Address real issues: repeated full index rebuild/materialization, honest archive corruption/missing-index behavior, and archived cost-backfill invalidation. Use a measured pre/post responsiveness comparison with sufficient samples across cache expiry and realistic capped concurrent process load; report empirical percentiles that cannot exceed observed maximum. Three fixture run records are not actual worker load. Keep experiments resource-bounded and serial. Restore basic service promptly; if safe archival expansion prevents a small verifiable recovery, propose splitting it into linked follow-up work rather than delaying the outage fix. No archive operations on live history during development.
- 2026-09-06T18:30:57+00:00 dispatched revise run 20260906T183056Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~11022 tokens)
- 2026-09-06T18:42:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/234: Run-history cache expiry now reparses only changed task buckets, archived metadata reloads only when its manifest changes, and corrupt archive state returns an honest 503 instead of partial totals. Archived cost corrections atomically refresh the archive index; measured fixture p95 remained 0.044s at 1,549 records and 0.190s at 6,003 records across 60 requests and multiple expiry intervals. cost=$1.22
- 2026-09-06T18:46:56+00:00 stalled: review finding repeated after a revise round: ui captures not read for: board, board-list, config, events, herbarium, inbox, n; run `garden triage CG-357 --changes "<feedback>" to unblock`
- 2026-09-06T18:59:04+00:00 PR234 merged8842552 after current-head CI, operator snapshot cleanup and served/browser workload evidence. Production recovery observation pending.
