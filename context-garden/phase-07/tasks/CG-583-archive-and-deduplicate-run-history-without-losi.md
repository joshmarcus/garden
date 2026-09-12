---
id: CG-583
title: Archive and deduplicate run history without losing recovery or accounting
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-344
- CG-360
priority: 1
difficulty: hard
reading:
- src/garden/runs.py
- src/garden/scheduler/fence.py
- src/garden/scheduler/state.py
- src/garden/config.py
branch: garden/cg-583-archive-and-deduplicate-run-history-without-losi
pr: https://github.com/joshmarcus/context-garden/pull/454
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T23:48:15+00:00'
created: '2026-09-10T13:11:06+00:00'
updated: '2026-09-11T00:46:13+00:00'
---

## Goal

Reduce disk growth from Garden run history and scheduler state through lossless compression, deduplication and bounded operational state, while preserving the full historical record, exact accounting, auditability and recovery behavior.

## Evidence

The September 10 storage audit found 877 per-run fence_guard/.garden__state.json snapshots totaling 8,760,216,811 logical bytes, approximately 8 GiB. Representative in-memory gzip tests saved 82.09%, 83.24% and 88.45%, with exact byte-count and SHA256 round-trip verification. The largest sample decreased from 113,875,273 to 13,148,002 bytes. These samples demonstrate potential savings; they are not a measured compression result for the entire history.

Other measured areas include roughly 1.3 GiB in the shared fence-guard cache, run outputs and manifests, and a current state.json of about 15 MB. Current fence restoration reads plain JSON snapshots and cached blobs directly. Blindly deleting or gzipping those files would break existing readers and recovery.

## Existing ownership and scope

Build on the existing RunStore archive/restore paths and CG-360's immediate visibility/accounting guarantees. Preserve CG-344's bounded fence bookkeeping and tamper protections. CG-527 owns disposable worktree/home/cache lifecycle cleanup; CG-528 owns the selected 20 GiB physical-disk admission reserve. This task owns retained history storage and reference-aware collection of its redundant blobs, never deletion of logical history or ordinary scratch cleanup; redundant physical representations may be retired only after verified durable reconstruction as specified below. Coordinate with CG-506's complete transcript storage format without blocking preservation of legacy outputs.

## Acceptance criteria

- [ ] Introduce a versioned lossless archive format with compressed, content-addressed immutable blobs and per-run references/checksums. Deduplicate only identical content or another representation whose exact reconstruction is verified. Read mixed legacy and migrated data, and preserve original bytes where manifests or provenance hashes depend on them.
- [ ] Preserve run identity, briefs/prompts, original outputs/transcripts, review findings and disagreements, failures and corrections, source heads/diffs, timestamps, token usage, costs, CI/validation receipts and necessary recovery evidence. Historical costs must not be recalculated from current prices or silently omitted. Archive, restore, UI/history/search/export and cost totals must show the same complete records exactly once.
- [ ] Archive only records proven eligible after finalization and reference checks. Protect running, waiting, blocked, incompletely collected/finalized and recovery-referenced runs, including terminal-looking runs whose task transition or fence check is still pending. Recheck liveness and references at commit time, preserving unrelated holds and manual/external ownership.
- [ ] Migrate existing data transactionally and resumably: write and durably flush the archive, verify reconstruction through the production reader and checksums, commit the index/reference change, and only then retire redundant originals. A crash, ENOSPC, corrupt blob, failed read or concurrent update must retain a usable original or verified archive and an explicit repair state; never invent a successful completion or empty history.
- [ ] Collect shared fence/cache blobs only after a complete reference analysis across live manifests, retained archives, authoritative manifest stores and recovery operations. Missing/corrupt reference data fails closed. An interrupted or concurrent mark/delete cycle must not remove newly referenced data.
- [ ] Keep hot scheduler state bounded by moving bulky completed-task historical payloads into indexed historical storage while retaining compact operational references. Status pages and ticks must not decompress or scan all history; measure state size and representative read/tick behavior as history grows.
- [ ] Provide a bounded preview/apply/report path using the existing archive/maintenance interfaces, with bytes by category, estimated versus actual savings, skipped reasons and idempotent retry. Large migrations must respect real backing-volume headroom and avoid unbounded temporary copies, memory use or scheduler blocking. This task must not shut down WSL, compact its VHD or change resource/spending limits automatically.
- [ ] Verify byte-identical round trips, unchanged accounting/visibility through fresh readers and timestamp collisions, mixed-format compatibility, duplicate references, concurrent reads/claims, active recovery, corruption, deletion failure and crashes at each migration boundary using deterministic fixtures. Include a representative multi-run storage measurement rather than extrapolating the three samples. Use portable APIs/configurable paths on Linux, macOS and Windows through WSL, and explicitly report platforms not tested.

## Out of scope

Dropping historical runs, replacing detailed findings with summaries, rewriting original failures, blindly pruning archived files by age, or weakening fences to save space.

owner_request_key: owner-lossless-run-history-archival-20260910


The owner deferred CG-506 on September10 because transcript storage growth needs redesign, potentially with external object storage. Preserve that hold. Implement lossless archival of the existing accepted formats independently, with a versioned adapter boundary for any later accepted transcript format; never assume the deferred draft format is deployed or discard legacy outputs. Coordinate future format integration after its owner resolves the storage design.

## Log

- 2026-09-10T13:21:20+00:00 approved (delegated operator all-Inbox review)
- 2026-09-10T15:27:46+00:00 dispatched work run 20260910T152742Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~17112 tokens)
- 2026-09-10T15:39:09+00:00 worker blocked: Implemented versioned gzip-compressed content-addressed run artifacts, exact checksum verification, deduplication, mixed legacy/current reads, restoration, bounded preview/apply reporting, timestamp collision protection, and fail-closed interrupted migrations. Focused archive/UI/CLI tests passed (27 passed) and `.venv/bin/ruff check src tests scripts` passed, but the full frozen scope is not complete. cost=$2.03
- 2026-09-10T16:04:00+00:00 PR attached: https://github.com/joshmarcus/context-garden/pull/454 (pr_number none -> 454)
- 2026-09-10T16:04:00+00:00 triage: changes requested by hand: Continue the exact preserved four-commit archive implementation ending43493b1e5bd1fc6a5a042a970bb2fcfff3b3f31b; do not r
- 2026-09-10T17:24:06+00:00 dispatched revise run 20260910T172402Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~18000 tokens)
- 2026-09-10T17:47:17+00:00 discovered work filed: CG-595
- 2026-09-10T17:47:17+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:50:47+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$6.22
- 2026-09-10T18:34:37+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/454: Completed lossless terminal scheduler-state archival with on-demand history reads and operational rehydration, plus reference-aware fence manifest/cache collection with guarded rechecks, integrity validation, bounded reporting, and retry-safe deletion failures. Rebased the preserved four archive commits onto origin/main; 369 affected tests passed with 4 stress tests deselected, a final 125-test rerun passed, and changed-file lint passed on WSL2.
- 2026-09-10T18:34:40+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T18:43:37+00:00 automated review requested changes: The core archive tests pass, but two migration recovery defects can make scheduler history unreadable or prevent an interrupted run archive from being repaired through the documented command. cost=$0.63
- 2026-09-10T18:44:06+00:00 dispatched revise run 20260910T184403Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~18743 tokens)
- 2026-09-10T18:48:24+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:53:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/454: Fixed both archive recovery defects and committed the changes as 6be835f4. Verified the affected state, run-index, and CLI suites (140 passed) and full repository lint; no typecheck command is configured. cost=$1.05
- 2026-09-10T18:56:29+00:00 automated review requested changes: Archive integrity and interrupted-migration recovery are well covered, but large apply operations can block scheduling and proceed without checking available backing-volume space. cost=$0.68
- 2026-09-10T19:33:18+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T19:42:20+00:00 dispatched revise run 20260910T194219Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18946 tokens)
- 2026-09-10T19:50:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:52:07+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/454: Moved run and scheduler-state compression outside the scheduler tick lock, added target-volume headroom admission, and made commit/retirement conditional on fresh eligibility, reference, source-identity, payload, and blob checks. Committed as c608de33; 209 focused tests passed and repository lint passed. cost=$1.87
- 2026-09-10T19:55:46+00:00 automated review requested changes: State-history archival can overwrite a concurrent durable update with the stale prepared payload, violating lossless migration and concurrency guarantees. cost=$0.55
- 2026-09-10T20:05:19+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T20:05:33+00:00 dispatched revise run 20260910T200533Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19394 tokens)
- 2026-09-10T20:10:34+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T20:11:54+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/454: Fixed the independently reproduced stale state-archive race by validating and replacing freshly read durable state under the state.json write lock. Committed as e6e585d2; 144 focused tests passed and full repository lint passed. cost=$0.78
- 2026-09-10T20:15:53+00:00 automated review requested changes: Run archival can clear its recovery marker before the rebuilt history index is durably committed, allowing a crash to silently omit moved runs from history and accounting. cost=$0.54
- 2026-09-10T20:46:36+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T21:07:29+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T21:07:59+00:00 dispatched revise run 20260910T210759Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19889 tokens)
- 2026-09-10T21:11:14+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T21:12:35+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/454: Made each archived-run move independently durable: source/target parents are flushed, the rebuilt index is fsynced and atomically published, and only then is the recovery marker removed and its directory flushed. Deterministic interruption tests preserve transcripts and exact costs through every boundary, including a two-run marker-overwrite scenario; committed as 6ec72e8f. cost=$0.75
- 2026-09-10T21:12:48+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/runs.py); a rebase agent will resolve it
- 2026-09-10T21:27:22+00:00 dispatched rebase run 20260910T212722Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3805 tokens)
- 2026-09-10T21:57:16+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.02
- 2026-09-10T22:20:15+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T22:20:43+00:00 dispatched revise run 20260910T222043Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~19771 tokens)
- 2026-09-10T22:43:37+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T22:50:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/454: Removed the sole obsolete `tmp` binding without changing durable archive-index replacement or recovery ordering. Ruff passed, and all 44 archive-index durability tests passed. cost=$0.37
- 2026-09-10T22:56:27+00:00 automated review requested changes: Archive durability and accounting coverage is strong, but some production history readers bypass the archive adapter, causing archived evidence to disappear from UI/export behavior. cost=$0.89
- 2026-09-10T23:09:56+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T23:10:32+00:00 dispatched revise run 20260910T231031Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20469 tokens)
- 2026-09-10T23:19:58+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T23:24:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/454: Preserved archived check configuration, receipts, investigation reports, and edit-history bodies through production artifact readers. Verified commit 2767bcc0 with 178 web tests plus 48 archive/deep-dive tests passing, repository Ruff clean, and no unresolved conflict markers; no typecheck command is configured. cost=$1.11
- 2026-09-10T23:37:30+00:00 automated review requested changes: Archive reader integration is improved, but interrupted restore can expose one run twice and double its historical cost. cost=$0.95
- 2026-09-10T23:43:45+00:00 triage: changes requested by hand: One bounded correction for the newly demonstrated restore transaction boundary: moving a run live before archive-index p
- 2026-09-10T23:47:45+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T23:48:15+00:00 dispatched revise run 20260910T234815Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~20845 tokens)
- 2026-09-11T00:01:45+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T00:12:12+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/454: Committed a durable restore transaction that prevents stale archive indexes from exposing restored runs twice. Verified the failed-index-publication restart path preserves one run, its evidence, and the exact $3.25 total; 45 focused tests and repository Ruff lint passed on Linux. cost=$0.58
- 2026-09-11T00:24:25+00:00 automated review: approve — The archive, state compaction, fence collection, and interrupted-restore paths satisfy the lossless recovery and exact-accounting requirements. No blocking defects found. cost=$0.82
- 2026-09-11T00:45:07+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/454
- 2026-09-11T00:46:13+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/454
