---
id: CG-355
title: Restore automatic installation and safe restart after tool updates
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading: []
branch: garden/cg-355-restore-automatic-installation-and-safe-restart
pr: https://github.com/joshmarcus/context-garden/pull/259
attempts: 1
last_dispatched_at: '2026-09-07T05:27:52+00:00'
created: '2026-09-06T17:29:22+00:00'
updated: '2026-09-07T05:59:42+00:00'
---

## Goal

Restore the expected automatic update path: when the tool repository advances and automatic updates are enabled, the running garden detects the new verified build, installs it at a safe point, restarts its existing controller, and visibly reports the version actually serving requests.

## Evidence

Owner report on 2026-09-06: "automatic restart when git is updated no longer works." The Now pages merged earlier in the day, but the installed server remained on b72dbcc. At 17:15 UTC both /now1 and /now2 returned HTTP 404. A manual bounded install of merged d5825a3 followed by restarting the existing service made both routes return 200 at 17:16. The recent fast-forward window deliberately ran serve --no-watch with dispatch paused; that hold must be preserved and is not itself proof of an updater defect. Diagnose the ordinary operating path, effective upgrade configuration, update detection, safe-idle eligibility, install and restart callback before attributing a root cause. CG-254/#229 adds explicit pinning but does not establish that automatic updating works end to end.

## Acceptance criteria

- [ ] Reproduce or explain the gap using the installed build, effective configuration and service logs: distinguish new commits fetched, merge-detected available updates, pending installation and completed restart. Define which upstream changes trigger automatic updating; do not assume every git fetch is authorization to install an arbitrary branch.
- [ ] With automatic updates enabled, advancing the configured tool base to a verified commit eventually updates the existing running controller and the served build identity. Prove this through a disposable real service lifecycle, including a request that only the new build can answer; a mocked restart callback alone is insufficient.
- [ ] Active workers/checks drain before install/restart, ongoing work survives, and a continuously replenished queue cannot starve an authorized update indefinitely. Preserve pause, maintenance/no-watch, phase freezes, authentication, temp setup and persistent resource caps. An explicit hold explains why an available update is waiting.
- [ ] Failed validation/install/restart produces an actionable diagnosis and retains or recovers a usable prior build. Do not announce a successful upgrade merely because a commit merged or pip returned success; verify the restarted process serves the expected version.
- [ ] The UI/operator status distinguishes available, held, installing, restart pending, failed and active versions with meaningful reasons. Record normal-path, active-check, held-maintenance and failed-update recovery evidence.

## Scheduling

Stabilization regression, owner-requested. Preserve active fast-forward maintenance; queue implementation after eligible PR resolution unless this is needed for safe exit. Coordinate with CG-338 resource admission and CG-295 operational documentation.

## Log

- 2026-09-06T17:29:57+00:00 approved (cli)
- 2026-09-07T04:08:07+00:00 dispatched work run 20260907T040742Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~9399 tokens)
- 2026-09-07T04:23:58+00:00 preserved uncommitted worktree changes from run 20260907T040742Z-work outside the PR: `git stash apply b8707dc632df21bc7ffd24841b99ab783f3c18d1` in /home/joshua/work/worktrees/CG-355 (garden:CG-355:20260907T040742Z-work:reap)
- 2026-09-07T04:27:05+00:00 opened https://github.com/joshmarcus/context-garden/pull/259 (base main): Restored automatic tool-base detection, starvation-free draining, safe installation and restart confirmation, rollback on failure, and visible active/update lifecycle status. Exact-commit GitHub CI passed. cost=$5.39
- 2026-09-07T04:32:56+00:00 automated review requested changes: The unit-level implementation is promising, but the acceptance contract explicitly requires disposable real-controller lifecycle and recovery evidence. Current tests use fake installation/restart objects, while the captures show only the available state. cost=$0.38
- 2026-09-07T04:42:54+00:00 dispatched revise run 20260907T044253Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10493 tokens)
- 2026-09-07T05:07:56+00:00 preserved uncommitted worktree changes from run 20260907T044253Z-revise outside the PR: `git stash apply 3602ec7e4b65a82232f0826c0cd7b26795e1d502` in /home/joshua/work/worktrees/CG-355 (garden:CG-355:20260907T044253Z-revise:reap)
- 2026-09-07T05:09:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/259: Added a real disposable-controller integration test proving automatic installation, process re-exec, build confirmation, and new-route availability. Added complete Inbox lifecycle captures, scoped build status to Inbox to avoid unrelated page churn, and recorded installation events. cost=$5.01
- 2026-09-07T05:12:30+00:00 automated review requested changes: Automatic detection, draining, real-process restart, build confirmation, and lifecycle reporting are well covered. Recovery is incomplete because failed installs and rollbacks are not verified to leave a usable prior build. cost=$1.25
- 2026-09-07T05:13:11+00:00 dispatched revise run 20260907T051310Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10519 tokens)
- 2026-09-07T05:22:36+00:00 preserved uncommitted worktree changes from run 20260907T051310Z-revise outside the PR: `git stash apply 53fe3e7117b17762ee8f9eca9c562712a236843e` in /home/joshua/work/worktrees/CG-355 (garden:CG-355:20260907T051310Z-revise:reap)
- 2026-09-07T05:24:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/259: Failed target installs now always attempt rollback, and recovery is reported only after the prior commit is observed and doctor passes. Exact-commit GitHub CI passed. cost=$0.75
- 2026-09-07T05:27:35+00:00 automated review requested changes: Automatic detection, draining, real-process restart, confirmation, and lifecycle reporting are well covered. Installer exceptions can bypass rollback and leave the update permanently reported as installing, so failure recovery is not yet complete. cost=$1.18
- 2026-09-07T05:27:52+00:00 dispatched revise run 20260907T052750Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10771 tokens)
- 2026-09-07T05:35:27+00:00 preserved uncommitted worktree changes from run 20260907T052750Z-revise outside the PR: `git stash apply 819e7570244a988aed81a5176cd92b6c84dbe4c5` in /home/joshua/work/worktrees/CG-355 (garden:CG-355:20260907T052750Z-revise:reap)
- 2026-09-07T05:37:27+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/259: Installer exceptions can no longer strand the controller in the installing state: target failures invoke rollback, and rollback exceptions persist an actionable unrecovered failure. Focused tests, lint, and exact-commit GitHub CI pass. cost=$0.75
- 2026-09-07T05:40:23+00:00 automated review: approve — Automatic configured-base detection, starvation-free draining, verified installation, real-process restart confirmation, rollback handling, and lifecycle reporting are implemented and tested. The focused upgrade suite passes 22 tests, and all 56 listed captures are visually sound. cost=$0.98
- 2026-09-07T05:50:30+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-07T05:52:31+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T05:53:32+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-07T05:59:42+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/259
