---
id: CG-528
title: Enforce a 20 GiB physical-disk reserve before local work and staging
status: done
product: context-garden
phase: phase-07
depends_on:
- id: CG-593
  after: merge
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/resources.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/checkruns.py
- src/garden/runner/local.py
- src/garden/runner/base.py
- src/garden/config.py
- src/garden/cli/diagnostics.py
branch: garden/cg-528-enforce-a-20-gib-physical-disk-reserve-before-lo
pr: https://github.com/joshmarcus/context-garden/pull/445
runner: remote
attempts: 2
last_dispatched_at: '2026-09-11T00:30:15+00:00'
created: '2026-09-10T12:49:51+00:00'
updated: '2026-09-11T02:09:11+00:00'
---

## Goal

Prevent another full backing disk by enforcing the owner's chosen 20 GiB free-space reserve before new local execution and large staging/materialization operations. Existing jobs must be allowed to finish and their results must remain collectable.

## Context

On September 10 the Windows volume backing WSL reached zero free bytes while the guest filesystem reported hundreds of GiB available. WSL returned I/O errors, the controller became unavailable, and a just-received run had empty saved payload files. A guest-only shutil.disk_usage(work_root) check cannot prevent this failure. The owner explicitly selected a 20 GiB Windows free-space reserve in the disk-cleanup side conversation.

CG-527 owns reclamation/retention of abandoned worktrees and caches; CG-310 is the completed temp/cache cleanup baseline; CG-498 owns branch-cleanup primitives. This task owns admission and the truthful measurement of the constrained storage volume. Reuse those tasks' accounting/probes where appropriate, without making admission dependent on deleting files or waiting for a cleanup implementation.

## Acceptance criteria

- [ ] Resolve and measure all storage volumes required by a local operation. On WSL, discover or explicitly configure the Windows backing volume as well as the guest filesystem; do not assume C:, a default user path, or that guest virtual capacity equals host free space. On native Linux and macOS use supported filesystem measurements. Unavailable or failed required measurements yield a visible blocked state, not a fabricated free-space value.
- [ ] Enforce a configurable reserve whose owner-selected value is 20 GiB (20 * 1024**3 bytes). Evaluate fresh free space before starting local work, revisions, reviews, checks, setup, scratch/probe materialization and large controller/runtime staging operations. Include known required allocation in admission where it is available, so admitting an operation does not intentionally cross the reserve. Existing configured execution/resource caps remain in force.
- [ ] A low-space admission denial leaves the work queued with a precise reason and fresh free/reserve/required-byte measurements. It does not consume a model attempt or revision, mark acceptance checks failed, kill an active process, pause remote execution unnecessarily, or block collection/flush of results and recovery evidence. Preserve independently owned operator and maintenance pauses; recovery of disk space must never clear someone else's pause.
- [ ] Coordinate concurrent admission decisions and recheck immediately before materialization. Account for already admitted reservations where estimates exist, release those reservations on failure/completion, and prevent multiple contenders from each consuming the same headroom. Restore eligibility automatically after a fresh successful space check, with bounded retry/backoff and no polling storm.
- [ ] Surface the actual limiting volume, free bytes, reserve and blocked operation in Now/Config or the existing operational status, plus actionable diagnostics. Preserve privacy in paths/identities. Do not silently resize, compact, shut down WSL, delete user files, or change the fleet budget/deadline as part of admission.
- [ ] Cover WSL guest-ample/host-full, native filesystem limits, alternate backing drives, inaccessible probes, just-below/at/above reserve, concurrent admission, growing disk usage during preparation, retry after recovery, active-job completion/result persistence, and unrelated holds with deterministic filesystem/provider fakes and disposable integration fixtures. Validate Linux, macOS and Windows through WSL where available and explicitly report untested platforms.

## Scope

A scheduler/materialization safety gate and its shared storage probe, separate from CG-527's cleanup implementation. No extra cloud spending, destructive automatic cleanup, or blanket interruption of running work is authorized.

owner_request_key: owner-wsl-physical-disk-reserve-20gib-20260910


## Staging boundary

Identify the actual Garden-owned setup, scratch/probe, checkout and runtime-staging entry points and route them through a shared supported storage-admission API. Document that API for external operator tooling and verify each product entry point covered. Scheduler admission alone must not be described as enforcing arbitrary external scripts; distinguish unintegrated external tooling explicitly.

## Log

- 2026-09-10T13:21:20+00:00 approved (delegated operator all-Inbox review)
- 2026-09-10T13:50:13+00:00 dispatched work run 20260910T135010Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~29205 tokens)
- 2026-09-10T14:10:20+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:11:43+00:00 opened https://github.com/joshmarcus/context-garden/pull/445 (base main): Added a default configurable 20 GiB physical-disk reserve with native and WSL backing-volume measurement, atomic per-run reservations, fresh staging/setup/scratch rechecks, automatic recovery, and operational diagnostics. Focused suites passed (including 223 lifecycle/resource tests and targeted setup/runner checks), lint passed, and the worktree is clean at 06271bb2. cost=$5.03
- 2026-09-10T14:15:35+00:00 automated review requested changes: The core storage probe and queued-work behavior are well tested, but reservation accounting and staging coverage remain incomplete. cost=$0.84
- 2026-09-10T14:27:48+00:00 dispatched revise run 20260910T142745Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~15196 tokens)
- 2026-09-10T14:32:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:33:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Fixed both blocking review findings: admitted review/persona/retro staging now rechecks its existing reservation without adding a second estimate, and base-broken recovery gates missing-checkout creation while preserving its waiting state. Committed as fc7d91e8; 291 focused tests passed, 1 platform-dependent test skipped, and Ruff passed. cost=$1.09
- 2026-09-10T14:36:18+00:00 automated review requested changes: Core probing and initial admission work, but two Garden-owned materialization paths can still cross the reserve. cost=$0.45
- 2026-09-10T14:36:27+00:00 dispatched revise run 20260910T143624Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~15659 tokens)
- 2026-09-10T14:44:00+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:45:24+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Remote-result checkout materialization now waits safely for disk recovery while preserving the collected result and attempt count. Detached setup/runtime checks carry the coordinated aggregate reservation; 269 focused tests passed, one platform-dependent test skipped, and Ruff passed at d0ccaa4f. cost=$1.70
- 2026-09-10T14:48:00+00:00 automated review requested changes: Storage probing and reservation tests pass, but some disk-writing staging still occurs without a fresh reserve check, and surfaced probe errors can disclose configured host paths. cost=$0.44
- 2026-09-10T14:50:55+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T14:58:07+00:00 dispatched revise run 20260910T145803Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16455 tokens)
- 2026-09-10T15:02:53+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:04:14+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Closed the remaining checkout synchronization and remote-result staging admission gaps, and sanitized persisted storage-probe failures. At exact head 3032d885, 212 focused tests passed, one platform-dependent test skipped, and Ruff passed; Linux ran locally while WSL was covered with deterministic fakes, with live WSL/Windows and macOS unavailable. cost=$0.86
- 2026-09-10T15:06:41+00:00 automated review requested changes: Checkout staging and reservation accounting are improved, but runtime/probe scratch and setup still perform or permit writes after the last reserve check. cost=$0.42
- 2026-09-10T15:16:20+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T15:17:24+00:00 dispatched revise run 20260910T151721Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16582 tokens)
- 2026-09-10T15:23:27+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:24:47+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Fresh storage admission now precedes runtime HOME/config copying and probe-directory creation, while setup rechecks storage after acquiring its lock and before launching its command. At c3a9cdf1, 151 focused tests passed, one platform-dependent test skipped, and Ruff passed. cost=$0.80
- 2026-09-10T15:27:32+00:00 automated review requested changes: Core storage probing and focused tests pass, but two local staging paths still bypass the required admission boundary. cost=$0.67
- 2026-09-10T15:34:13+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T16:02:24+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T16:17:38+00:00 dispatched revise run 20260910T161734Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16670 tokens)
- 2026-09-10T16:25:06+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:26:38+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Completed shared storage-admission coverage for phase-persona staging and canonical in-place checkouts at 0398fea8. The affected scheduler, canonical, runner, persona, and remote-worker suites passed with 603 tests passed and 1 platform-dependent skip; Ruff passed. cost=$1.02
- 2026-09-10T16:30:30+00:00 automated review requested changes: Most storage admission behavior is well covered, but the Garden-owned kickoff staging path still bypasses the reserve. cost=$0.74
- 2026-09-10T16:51:46+00:00 triage: changes requested by hand: Preserve the corrected phase-persona and canonical-root admission paths. Apply the SAME shared reservation contract to p
- 2026-09-10T16:53:14+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T17:05:29+00:00 dispatched revise run 20260910T170526Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~17002 tokens)
- 2026-09-10T17:15:10+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:16:27+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Phase kickoff now acquires the shared local reservation before repository cloning/fetching or checkout creation, freshly rechecks before writes, transfers that reservation into auxiliary dispatch, and releases it after preparation failure. The architecture inventory now includes storage.py; 219 focused kickoff/persona/canonical/admission/remote-worker/architecture tests passed with 1 platform-dependent skip, and repository Ruff passed. cost=$1.68
- 2026-09-10T17:16:35+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/runner/local.py); a rebase agent will resolve it
- 2026-09-10T17:16:40+00:00 dispatched rebase run 20260910T171638Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3761 tokens)
- 2026-09-10T17:20:16+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Resolved all rebase conflicts while preserving sandbox, storage-admission, and architecture changes. cost=$0.02
- 2026-09-10T17:23:54+00:00 automated review: approve — The shared physical-storage gate now covers local execution and Garden-owned staging while preserving queued work, active result collection, independent holds, and automatic recovery. cost=$0.52
- 2026-09-10T17:34:19+00:00 triage: changes requested by hand: Preserve the actual independent approval at679a1bc0 and its340 focused passes/1 platform skip. Actual pushCI34507460167
- 2026-09-10T18:46:01+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T19:33:20+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T19:42:19+00:00 dispatched revise run 20260910T194219Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17144 tokens)
- 2026-09-10T19:48:12+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:49:34+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Rebased the independently approved physical-storage reserve implementation onto current main containing accepted CG-593, without duplicating its shared repair. At exact head 87300dd33b600c55edc9a6da4290b5b5ddb835ca, 537 focused tests passed with 1 platform-dependent skip, Ruff passed, diff checks passed, and the worktree is clean; fresh remote exact-head CI remains the controller's post-publication gate. cost=$0.90
- 2026-09-10T19:53:21+00:00 automated review requested changes: Base-probe and scratch-merge preparation can still consume local disk before the shared reserve gate runs. cost=$0.55
- 2026-09-10T19:58:56+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T19:59:37+00:00 dispatched revise run 20260910T195936Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17623 tokens)
- 2026-09-10T20:07:52+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T20:09:14+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Base-probe and scratch-merge staging now reserve and freshly recheck physical storage before any Git materialization, transferring the same reservation into local check execution and releasing it on failure. Committed as 9631b430; affected tests passed (108 passed, 1 platform skip) and repository Ruff passed. cost=$1.47
- 2026-09-10T20:13:16+00:00 automated review: approve — The shared physical-storage gate covers local execution and Garden-owned staging, including the corrected base-probe and scratch-merge paths, while preserving queued work, reservations, result collection, independent holds, and automatic recovery. cost=$0.56
- 2026-09-10T20:46:40+00:00 triage: changes requested by hand: Fix actual CI34524518180 on9631b430:2705passed/1failed tests/test_remote_worker.py::test_daemon_crash_after_gate_release
- 2026-09-10T20:53:13+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T21:07:28+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T21:07:59+00:00 dispatched revise run 20260910T210759Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17727 tokens)
- 2026-09-10T21:12:28+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T21:13:54+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Fixed the flaky remote handoff test without changing the approved storage implementation. The test now proves the destination can exist while empty, releases the copy deterministically, waits for the supervisor exit record, and verifies the complete Unicode payload, daemon exit 73, mode 0600, and durable supervisor identity. cost=$0.54
- 2026-09-10T21:14:01+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/persona.py); a rebase agent will resolve it
- 2026-09-10T21:27:21+00:00 dispatched rebase run 20260910T212721Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~4994 tokens)
- 2026-09-10T21:57:16+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.01
- 2026-09-10T22:20:12+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T22:20:42+00:00 dispatched revise run 20260910T222042Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18191 tokens)
- 2026-09-10T22:43:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T22:50:37+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Removed the sole stale persona harness binding while preserving phase-persona storage reservation and dispatch behavior. Focused persona/storage regressions passed (95 passed, 1 platform-dependent skip), repository Ruff passed, and the committed worktree is clean at d7bc530a. cost=$0.41
- 2026-09-10T22:50:58+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/persona.py); a rebase agent will resolve it
- 2026-09-10T22:51:06+00:00 dispatched rebase run 20260910T225106Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~5346 tokens)
- 2026-09-10T22:59:08+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/445: Rebased onto origin/main and resolved the storage-admission conflicts while preserving both sides' intent. cost=$0.01
- 2026-09-10T23:19:55+00:00 CI failure
- 2026-09-10T23:43:45+00:00 triage: changes requested by hand: One bounded correction for the independently reproduced kickoff admission ordering defect. start_kickoff must obtain the
- 2026-09-10T23:47:43+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T23:48:14+00:00 dispatched revise run 20260910T234813Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18885 tokens)
- 2026-09-11T00:12:04+00:00 revision failed: worker idle 21 min (no output or file change)
- 2026-09-11T00:30:15+00:00 dispatched work run 20260911T003015Z-work via manual [human] (fresh session, base main, ~17883 tokens)
- 2026-09-11T00:30:16+00:00 external PR attached at garden/cg-528-enforce-a-20-gib-physical-disk-reserve-before-lo; existing CI is PENDING
- 2026-09-11T00:34:25+00:00 automated review requested changes: The kickoff ordering correction appears sound, but current-head validation is missing: the checkout is 6d282b9d while the review was admitted for 2566014a, whose CI failed. cost=$0.52
- 2026-09-11T01:34:04+00:00 current review resolved the pending review findings
- 2026-09-11T01:34:04+00:00 automated review: approve — The shared physical-storage gate covers local execution and Garden-owned staging, including kickoff repository resolution, while preserving reservations, queued work, result collection, independent holds, and automatic recovery. cost=$0.64
- 2026-09-11T02:04:43+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T02:09:11+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/445
