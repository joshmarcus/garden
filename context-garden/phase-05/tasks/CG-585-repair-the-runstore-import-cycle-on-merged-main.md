---
id: CG-585
title: Repair the RunStore import cycle on merged main
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-584
kind: bug
priority: 0
difficulty: hard
reading:
- src/garden/runs.py
- src/garden/hosts/__init__.py
- src/garden/runner/base.py
- tests/conftest.py
- context-garden/docs/incidents/main-runstore-import-cycle-2026-09-10.md
branch: garden/cg-585-repair-the-runstore-import-cycle-on-merged-main
pr: https://github.com/joshmarcus/context-garden/pull/449
runner: remote
discovered_from: CG-584
freeze_exception: true
freeze_exception_reason: Accepted main fails before test collection after the completion-race repair;
  restore the integrated source before closure and stable release.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-10T14:59:28+00:00'
created: '2026-09-10T14:58:25+00:00'
updated: '2026-09-10T15:44:20+00:00'
---

## Goal

Restore clean-process imports and the full main-branch test entry point after the accepted CG-584 RunStore change, preserving its process-safe completion guarantees. Repair the dependency cycle once on current main so downstream branches can rebase onto accepted source.

## Context

Main CI 34488489354 passed on 0eb7a66eabfbd7549938c2848eb8a275ecffee53. Main CI 34489071296 failed on CG-584 merge 9565228279b58d754efd026d32be51bd2da368d9, and 34491506154 failed identically on subsequent CG-213 merge c1b0022c0e5ff27318ec5fe75e6ed5c9ef1df9cc. Both fail before test collection, on Python3.12, with runner -> runs -> hosts.locking -> hosts.__init__ -> hosts.drain -> RunStore importing from partially initialized runs. CG-584's exact-head CI and focused review were green; preserve those historical results without treating them as proof the final merged import graph is healthy. CG-501 and rebased CG-518 inherit the same failure; this task owns the shared main-source repair, not their separate functionality.

## Acceptance criteria

- [ ] Reproduce the original failure from accepted main in a fresh Python process using the actual pytest conftest import order, then remove the RunStore/hosts dependency cycle at the appropriate low-level locking or package boundary. Do not mask ImportError, weaken file locking, delete completion metadata protections or depend on a lucky prior import.
- [ ] Fresh processes can import garden.runner, garden.runs and garden.hosts in the relevant independent import orders, and the normal pytest entry point collects successfully. Include a focused subprocess regression that fails on the original source and detects partial-module import cycles without reusing pytest's already populated sys.modules.
- [ ] Preserve CG-584's deterministic cross-process claim/heartbeat/finish versus stale scheduler-save regressions, exact publication/fencing and compatibility behavior. Run the relevant focused suite, full required CI and repository lint on the final integrated source. Preserve all initial failure evidence and report the accepted source identity.
- [ ] Keep the correction narrow and portable across Linux, macOS and Windows through WSL; retain existing supported locking alternatives and report which native platforms were actually tested. No paid live canary, fleet or deployment change is part of this task.

## Ownership

This is the focused post-merge regression follow-up to completed CG-584. CG-537 must wait for this actual merge and report main's red-to-green recovery. Preserve CG-501 diagnostics and CG-518 sandbox source; they may rebase after this repair instead of independently redesigning locking. This task does not authorize a release, a direct set-done action or a runtime hotpatch.

owner_request_key: main-runstore-import-cycle-20260910

## Log

- 2026-09-10T14:58:25+00:00 approved (delegated operator; verified main CI import regression)
- 2026-09-10T14:59:28+00:00 dispatched work run 20260910T145928Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23117 tokens)
- 2026-09-10T15:31:38+00:00 discovered work filed: CG-588, CG-589
- 2026-09-10T15:31:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:33:03+00:00 opened https://github.com/joshmarcus/context-garden/pull/449 (base main): Removed the RunStore/hosts package cycle by moving the unchanged portable file lock to a package-neutral boundary while retaining the hosts compatibility import. Fresh-process imports and focused concurrency/host suites pass at 6ea7dd8c; the full suite now collects and runs, with 2,492 passing and three unrelated failures reported truthfully. cost=$2.57
- 2026-09-10T15:36:38+00:00 automated review: approve — The package-neutral locking boundary repairs fresh-process imports without changing locking or RunStore completion semantics. cost=$0.36
- 2026-09-10T15:44:20+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/449
