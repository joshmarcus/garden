---
id: CG-617
title: Separate writable harness state from protected credential inputs
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-619
kind: bug
priority: 0
difficulty: hard
reading:
- src/garden/runner/base.py
- src/garden/runner/local.py
- tests/test_runners.py
branch: garden/cg-617-separate-writable-harness-state-from-protected-c
pr: https://github.com/joshmarcus/context-garden/pull/480
runner: remote
discovered_from: CG-601
retro_blocking: true
attempts: 2
last_dispatched_at: '2026-09-11T02:56:41+00:00'
created: '2026-09-11T01:06:52+00:00'
updated: '2026-09-11T03:36:31+00:00'
---

## Goal

Allow real local Codex and Claude harness startup while preserving protected credentials, disposable per-run settings and the configured OS isolation boundary. Separate writable harness runtime state from immutable credential inputs; never point an entire state directory at a read-only credential-only root.

## Reproduction and accepted-source context

The first observed local CG601 attempt20260911T004633Z-work on RC19/70ae9179 failed before model execution: stderr reports PATH alias creation Permission denied and in-process app-server initialization Permission denied; structured stdout is0bytes and the checkout remains clean3471e86a. Its CODEX_HOME was /home/joshua/work/worktrees/.garden-home-CG-601-credentials/.codex with mode0500, containing only the copied auth.json. Codex needs its home for local runtime state/logs/caches as well as credentials. runner/base.py private_config_dir_env currently copies credential files0400 then locks the whole destination0500 and scrubbed_env exports that destination as CODEX_HOME or CLAUDE_CONFIG_DIR. This same source remains in candidateRC20/541aa9ac; no source fix is installed.

The old RC19 supervisor also hung on its final FIFO after this already-failed child exited. Root preserved original run/brief/stdout/stderr/command/execution bytes and stopped only the verified childless supervisor. No successful exit, final, usage or cost was invented. The distinct FIFO problem is ALREADY fixed by mergedCG600/PR478; do not redesign or duplicate it. Original evidence is /home/joshua/work/operator-test-tmp/rc19-deploy-20260910/cg601-local-startup-failure.json. Official state-location documentation: https://learn.chatgpt.com/docs/config-file/config-advanced#config-and-state-locations.

## Acceptance criteria

- [ ] Provide writable, private and disposable per-run harness state/cache/settings locations for actual local Codex and Claude startup while immutable credential inputs and the operator's original home/files remain protected. Cover both normal workers and auxiliary reviews, setup/check compatibility, explicit configuration and applicable remote/SSH paths without claiming live coverage not run.
- [ ] Preserve least-privilege credential access, opt-in sandbox behavior and OS mount/read-write boundaries. Do not make an entire credential mount writable, expose the operator's whole config/home, carry hooks/settings from a prior worker into the next, or weaken required isolation. Support necessary private credential refresh semantics without modifying the operator's original credential files or logging tokens.
- [ ] Add deterministic CLI-like startup fakes that actually create runtime directories/files under CODEX_HOME and CLAUDE_CONFIG_DIR as the ordinary non-root user, read only intended credential material and leave operator input bytes unchanged. Cover fresh re-dispatch after worker settings contamination and required read-only credential versus writable runtime mounts. An auth-file-exists assertion alone does not establish startup.
- [ ] Run focused runner/harness/isolation tests and Ruff, then actual exact-head CI and independent review. Use portable paths/capability checks across Linux, macOS and Windows through WSL and label untested platforms. Do not call paid models, run Playwright, change live services, change credentials/fleet resources or hotpatch immutable runtimes merely to test this correction.

## Boundaries

This is the distinct harness state/credential separation defect discovered during RC20 preparation. Root owns publication and activation after accepted source and full gates. Preserve CG601's narrower synthetic validation-fixture task and CG616's Playwright defaults request. Include this incident and actual disposition in the existing CG537 account without another persona/verifier task.


Inspect src/garden/sandbox.py and tests/test_execution_sandbox.py from the actual accepted main checkout as well; those new files are absent from the controller cached reading-list source, but present in accepted3471e86a and candidate541aa9ac. Retain actual current source and sandbox boundary verification.

## Log

- 2026-09-11T01:09:35+00:00 approved (operator: observed local harness startup regression)


Inspect src/garden/sandbox.py and tests/test_execution_sandbox.py from the actual accepted main checkout as well; those new files are absent from the controller cached reading-list source, but present in accepted3471e86a and candidate541aa9ac. Retain actual current source and sandbox boundary verification.
- 2026-09-11T01:10:01+00:00 dispatched work run 20260911T011001Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22228 tokens)
- 2026-09-11T01:54:06+00:00 Operator recovery: the worker daemon lost its endpoint connection and systemd stopped its original source-writing process during final validation. Preserve committed head8e4321c8 and original output, missing final/usage/cost and validation SIGTERM. Route future execution to manual attachment while original source is preserved and independently checked; no automatic duplicate author and no direct set-done.
- 2026-09-11T02:04:53+00:00 attempt 1 failed: worker exited -15: worker produced no output; will retry
- 2026-09-11T02:08:32+00:00 Recovered exact original authored commits are now PR480, with original interrupted validation and absent author final/usage/cost preserved. Restore normal remote review routing; the following manual run only attaches the source and does not claim the original author completed successfully.
- 2026-09-11T02:08:33+00:00 dispatched work run 20260911T020833Z-work via manual [human] (fresh session, base main, ~22480 tokens)
- 2026-09-11T02:08:34+00:00 external PR attached at garden/cg-617-separate-writable-harness-state-from-protected-c; existing CI is FAILURE
- 2026-09-11T02:09:07+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/runner/local.py); a rebase agent will resolve it
- 2026-09-11T02:09:17+00:00 dispatched rebase run 20260911T020916Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1972 tokens)
- 2026-09-11T02:27:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/480: Rebased onto origin/main and resolved the local runner conflict while preserving both sides' intent. cost=$0.01
- 2026-09-11T02:39:18+00:00 automated review: approve — The change correctly separates writable disposable harness state from protected credential inputs without weakening sandbox boundaries. Exact-head CI remains pending and must pass before merge. cost=$0.50
- 2026-09-11T02:55:59+00:00 Core source5f2439b5 independently approved with132 focused passes. CurrentCI34554293842 failed only the same branch-cleanup run-ID prefix case (2784passes), already fixed by root ownerCG619/PR482. Wait for its actual merge, then restack/rebase and resume exact-source CI/review; do not start a duplicate correction to that separately owned CI defect. Original CI failures and current source approval are retained.
- 2026-09-11T02:56:19+00:00 CI failure
- 2026-09-11T02:56:41+00:00 dispatched revise run 20260911T025641Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23180 tokens)
- 2026-09-11T03:02:36+00:00 temporary runner hold by delegated_operator: Wait for actual CG619/PR482 merge, then restack and rerun current source CI. The ordinary revision dispatcher ignored the dependency; the025641 worker correctly returned blocked without changing source. Preserve its actual157+14 tests, cost and original source approval; do not dispatch another diagnosis of the same separately owned CI failure.
- 2026-09-11T03:02:37+00:00 worker blocked: The CG-617 implementation remains clean and its focused suites pass, but exact-head CI cannot pass until the separately owned CG-619/PR 482 fix merges and this branch is restacked. No source changes were made in this revision. cost=$0.95
- 2026-09-11T03:18:18+00:00 temporary runner hold released by delegated_operator: Wait for actual CG619/PR482 merge, then restack and rerun current source CI. The ordinary revision dispatcher ignored the dependency; the025641 worker correctly returned blocked without changing source. Preserve its actual157+14 tests, cost and original source approval; do not dispatch another diagnosis of the same separately owned CI failure.
- 2026-09-11T03:18:18+00:00 triage: marked ready for review (Canonical CI repair619/PR482 actually merged; core617 source remains independently approved. Bring i)
- 2026-09-11T03:18:23+00:00 Canonical CI repair CG619 actually merged; restack the separately approved startup source; rebased onto main mechanically and force-pushed
- 2026-09-11T03:28:05+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-11T03:36:25+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T03:36:31+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/480
