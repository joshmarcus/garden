---
id: CG-355
title: Restore automatic installation and safe restart after tool updates
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading: []
created: '2026-09-06T17:29:22+00:00'
updated: '2026-09-06T17:29:57+00:00'
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
