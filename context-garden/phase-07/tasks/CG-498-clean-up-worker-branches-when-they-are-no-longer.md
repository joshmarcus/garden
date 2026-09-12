---
id: CG-498
title: Clean up worker branches when they are no longer needed
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: hard
reading:
- src/garden/gitops.py
- src/garden/scheduler/poll.py
- src/garden/runs.py
branch: garden/cg-498-clean-up-worker-branches-when-they-are-no-longer
pr: https://github.com/joshmarcus/context-garden/pull/412
attempts: 1
last_dispatched_at: '2026-09-10T03:41:07+00:00'
created: '2026-09-10T01:22:55+00:00'
updated: '2026-09-10T04:15:54+00:00'
---

## Goal

Stop accumulating abandoned worker branches. Automatically remove Garden-owned local and remote branches once their work is complete and no task, PR, stack, active run, or recovery operation still needs them.

## Context

Owner request: "We are generating worker branches and abandoning them — we should drop them when we no longer need them."

Cover branches left by completed work, superseded attempts, and abandoned worker sessions, including existing backlog as well as future lifecycle cleanup. A cancelled task or an old branch name alone is not proof that its commits can be discarded. Reuse existing repository/provider routing, run ownership, stack references, and cleanup mechanisms. Coordinate with CG-232 trial cleanup and CG-310 temporary-file cleanup without expanding this into general artifact deletion.

## Acceptance criteria

- [ ] Identify Garden-owned branches from recorded provenance, and classify each as needed, safely removable, or uncertain with a concrete reason. Support configured remotes and enterprise hosts without assuming origin or GitHub.com.
- [ ] Preserve branches needed by active or queued runs, open PRs, dependent stacks, worktrees, manual/external ownership, or recovery. Preserve unmerged unique work unless its durable preservation or explicit discard is established; uncertain cases remain visible rather than being silently deleted.
- [ ] Clean up eligible local and remote worker branches after their lifecycle ends, and provide a bounded, repeatable sweep for branches already abandoned. Expose a preview of candidates and skipped reasons.
- [ ] Recheck references and branch identity immediately before deletion; a concurrent push, new claim, changed PR, or new dependent prevents unsafe deletion. Remote deletion uses an expected-head guard where supported and fails safely otherwise.
- [ ] Record which repository, branch, and head were removed or retained and why. Missing branches, partial local/remote failures, interrupted sweeps, and retries are handled idempotently without erasing task/run/PR history.
- [ ] Exercise merged and superseded branches, cancelled work with unique commits, active work, open and stacked PRs, foreign/protected branches, concurrent changes, and partial failures in meaningful tests. Use portable Git/process APIs and configurable paths; validate Linux, macOS, and Windows through WSL, explicitly reporting any untested platform.

## Out of scope

- Deleting unrelated user branches, protected/default branches, run evidence, or worktrees merely because they are old.
- Changing branch ownership, merge policy, or retention of useful unmerged work to make cleanup easier.

## Log

- 2026-09-10T02:33:40+00:00 approved (owner requested draft review and readiness; operator verified brief)
- 2026-09-10T03:01:15+00:00 dispatched work run 20260910T030114Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~13061 tokens)
- 2026-09-10T03:16:15+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T03:17:37+00:00 opened https://github.com/joshmarcus/context-garden/pull/412 (base main): Added conservative provenance-based worker branch cleanup with bounded automatic sweeps, CLI preview/apply, expected-head deletion guards, retention reasons, and durable audit events. Verified 174 focused lifecycle/CLI/Git tests plus 7 final cleanup tests and clean Ruff lint on Linux under Windows WSL2; native macOS was unavailable. cost=$2.78
- 2026-09-10T03:21:27+00:00 automated review requested changes: Branch cleanup is generally conservative and lease-guarded, but it can delete a branch newly claimed by an open PR because the required delete-time PR recheck is incomplete. cost=$0.46
- 2026-09-10T03:29:07+00:00 dispatched revise run 20260910T032904Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~14383 tokens)
- 2026-09-10T03:34:47+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T03:36:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/412: Branch deletion now performs fresh, author-independent provider checks for open PRs using the candidate as either head or base, and retains the branch if checks fail. Committed as 688a102c; 130 affected tests plus 8 focused cleanup tests passed and Ruff is clean. cost=$0.88
- 2026-09-10T03:40:56+00:00 automated review requested changes: The PR-race revision is sound, but completed tasks can cause unique commits on superseded branches to be deleted without proof of preservation or explicit discard. cost=$0.33
- 2026-09-10T03:41:07+00:00 dispatched revise run 20260910T034104Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~14411 tokens)
- 2026-09-10T03:55:01+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T03:56:15+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/412: Branch cleanup now requires head-specific preservation proof even after a task completes, preventing deletion of unique superseded work. Verified at commit e6efe9ee6347a8703f550ed66d274b55f85d8790 with 10 focused branch-cleanup tests and clean Ruff lint on Linux under WSL; native macOS was unavailable. cost=$0.98
- 2026-09-10T03:58:45+00:00 automated review: approve — The cleanup is conservative, bounded, provenance-based, and guarded against stale heads and newly claimed PR/stack references. The prior unique-superseded-work defect is resolved. cost=$0.46
- 2026-09-10T04:14:32+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T04:15:54+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/412
