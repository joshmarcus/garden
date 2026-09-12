---
id: CG-506
title: Return complete worker transcripts for server-side storage and analysis
status: changes_requested
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/remote_worker.py
- src/garden/runner/remote.py
- src/garden/runs.py
- docs/worker-protocol.md
- src/garden/web/pages/runs.py
branch: garden/cg-506-return-complete-worker-transcripts-for-server-si
pr: https://github.com/joshmarcus/context-garden/pull/415
attempts: 1
last_dispatched_at: '2026-09-10T11:08:54+00:00'
created: '2026-09-10T02:40:39+00:00'
updated: '2026-09-10T11:43:01+00:00'
---

## Goal

Return the complete transcript produced by each worker run to the controller, durably store it server-side, and make it available for authorized analysis and retrieval without relying on later access to the worker host.

## Context

Owner request: return full worker transcript for analysis and storage on server side. A final answer, summary or tail of stdout is not the full transcript. Preserve the complete observable harness event stream, including assistant messages, exposed tool requests/results, command output and errors, timestamps and final result where emitted. Do not claim access to private model reasoning or events the harness does not expose. Record genuinely unavailable content explicitly.

Inspect existing result/artifact upload and local run storage first. Coordinate with CG073/CG427 transcript rendering, CG501 disconnect recovery and CG499 worker visibility. This task owns complete reliable collection and controller storage, not another transcript renderer or public evidence-export mechanism. The deferred CG402 external evidence-export policy is separate; this task does not unfreeze it.

## Acceptance criteria

- [ ] Define and implement a complete transcript contract for supported worker harnesses and run modes. Preserve original event order and available structured payloads plus stdout/stderr or equivalent emitted output. Include failed, cancelled and interrupted runs as well as successful runs; distinguish missing, partial, truncated, redacted and complete data truthfully. A summary must never substitute for available full content.
- [ ] Transfer transcripts through the authenticated worker/controller protocol using bounded streaming or chunked/resumable upload suitable for large logs. Survive transient disconnects, worker/controller restarts and repeated completion requests without dropped segments or duplicated events. Use existing lease/generation ownership and fencing; late superseded uploads cannot overwrite another run or its canonical transcript. Preserve useful partial evidence under the correct attempt identity.
- [ ] Persist transcripts durably on the controller with task/run/attempt/worker identity, source revision, harness/schema version, sequence/byte counts, checksums and completion status. Acknowledge durable receipt before worker-side cleanup. Handle disk-full, quotas, corruption, missing chunks and interrupted finalization explicitly; never claim a transcript was fully returned when only the final result was stored.
- [ ] Provide authorized server-side retrieval/export and a documented analysis interface that can consume the complete stored event stream and correlate it with result, timing, cost and diagnostics. Reuse existing run links and rendering surfaces; local and remote runs should expose a consistent storage/retrieval contract. Clearly separate worker execution completion from transcript transfer/storage completion and show pending or failed delivery.
- [ ] Apply existing access controls, safe paths, configurable retention and storage limits. Protect credentials and sensitive configuration through scoped redaction of known secrets rather than dropping broad output sections; record redaction and any unavoidable capture limits explicitly. No public publication or third-party analysis upload is implied. Prevent transcript content from being executed or treated as trusted instructions by analysis tooling.
- [ ] Demonstrate a disposable worker/controller journey with a transcript larger than the previous payload/tail limits, tool outputs and stderr, mid-upload interruption, retry, duplicate/out-of-order chunks, controller restart, worker failure, storage failure and stale-generation delivery. Verify event/content completeness and integrity at the server, with only declared secret redactions, and confirm useful partial transcripts remain available after failure. Keep bounded memory/network/disk behavior and test configurable paths on Linux, macOS and Windows through WSL, reporting untested platforms.

## Scope boundaries

Do not expose hidden model reasoning, fabricate unavailable transcript data, publish private transcripts, modify live fleet credentials or delete useful existing run evidence. Reuse current protocol capabilities where sufficient and identify source changes versus deployed runtime behavior separately.

## Log

- 2026-09-10T03:08:57+00:00 approved (delegated operator reviewed owner-requested draft during Inbox sweep)
- 2026-09-10T04:40:25+00:00 dispatched work run 20260910T044022Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~18042 tokens)
- 2026-09-10T04:52:04+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T04:53:24+00:00 opened https://github.com/joshmarcus/context-garden/pull/415 (base main): Remote harness runs now return ordered, timestamped stdout/stderr events through bounded, resumable, lease-fenced uploads. The controller durably stores attempt-scoped streams with checksums and completion metadata, exposes delivery state and authorized download, and preserves partial evidence; 212 focused tests and repository lint passed at 723dd2bfe297bf67492928a436b7a78e3d3001b6. cost=$2.04
- 2026-09-10T04:57:17+00:00 automated review requested changes: The core upload/storage path works, but the complete transcript contract remains unmet for remote check runs, secret redaction boundaries, and bounded large-log retrieval/processing. cost=$0.58
- 2026-09-10T05:10:01+00:00 dispatched revise run 20260910T050958Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19711 tokens)
- 2026-09-10T05:19:02+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T05:20:16+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/415: Completed the transcript contract gaps at commit a7f0adf7: remote checks now deliver canonical transcripts, cross-boundary and structured secret redaction is safe, and export/digest/analysis paths support bounded incremental processing. The focused remote-worker suite passed 78 tests and repository lint passed. cost=$2.04
- 2026-09-10T05:20:24+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/pages/api.py); a rebase agent will resolve it
- 2026-09-10T05:20:27+00:00 dispatched rebase run 20260910T052026Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2177 tokens)
- 2026-09-10T05:22:39+00:00 pre-PR checks failed (lint, syntax); revise run will fix before the PR is updated cost=$0.01
- 2026-09-10T05:26:13+00:00 dispatched revise run 20260910T052609Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19137 tokens)
- 2026-09-10T05:29:27+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T05:30:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/415: Fixed the rebase-introduced indentation error in the transcript API imports and committed it as 2dca1088. The focused transcript/remote-worker/web suite passed 216 tests, repository lint passed, and syntax/conflict-marker/diff checks were clean. cost=$0.44
- 2026-09-10T05:30:49+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_remote_worker.py); a rebase agent will resolve it
- 2026-09-10T05:33:07+00:00 dispatched rebase run 20260910T053306Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2501 tokens)
- 2026-09-10T05:37:32+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.01
- 2026-09-10T05:51:41+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T06:17:39+00:00 dispatched revise run 20260910T061736Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20033 tokens)
- 2026-09-10T06:20:53+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T06:22:06+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/415: Reordered the remote-worker test imports to resolve the sole current-head CI failure and committed the repair as 665f27ddc0a6032717ed521e845bc3d1f50069fc. The focused transcript/remote-worker/web suite passed 221 tests with 4 policy-deselected stress tests, repository Ruff passed, and diff/conflict checks were clean. cost=$0.52
- 2026-09-10T06:26:46+00:00 automated review requested changes: Transcript upload works in ordinary execution, but restart recovery and superseded-attempt retrieval remain incomplete. cost=$0.44
- 2026-09-10T10:53:58+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T11:08:54+00:00 dispatched revise run 20260910T110849Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20744 tokens)
- 2026-09-10T11:22:02+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:23:17+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/415: Remote workers now durably retain the claim identity, transcript spool, sequence state, and acknowledged upload offset so the same lease generation resumes after worker restart. The controller catalogs every complete or partial attempt and provides authorized attempt-aware listing, download, and incremental analysis; focused suites and repository lint passed. cost=$2.99
- 2026-09-10T11:25:44+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: disposable failure/recovery journey; run `garden triage CG-506 --changes "<feedback>" to unblock`
- 2026-09-10T11:43:01+00:00 re-enabled by hand; revise run will follow
