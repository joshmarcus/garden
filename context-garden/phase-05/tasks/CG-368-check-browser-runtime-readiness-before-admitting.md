---
id: CG-368
title: Check browser runtime readiness before admitting capture-dependent work
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading: []
branch: garden/cg-368-check-browser-runtime-readiness-before-admitting
pr: https://github.com/joshmarcus/context-garden/pull/263
attempts: 1
last_dispatched_at: '2026-09-07T05:16:35+00:00'
created: '2026-09-07T03:58:51+00:00'
updated: '2026-09-07T05:37:39+00:00'
---

## Goal

Detect an unusable browser environment once before capture-dependent work consumes review/revision rounds, and recover automatically when the environment becomes ready.

## Evidence and boundaries

CG326 repeatedly produced HTML/text and no PNGs because Chromium lacked libnspr4/libnss3/libnssutil3/libsmime3. Its fallback base probe exited0 with checks=[] and repeatedly asked for human input. The operator extracted official Ubuntu runtime packages without sudo and proved a bounded Chromium launch with actual390px viewport using an explicit LD_LIBRARY_PATH, then activated service configuration. Worker environments remain separately scrubbed. Environment readiness must not be mistaken for a product defect or screenshot proof. CG326 owns actual narrow capture behavior, CG323 owns mechanical check routing, CG362 external completion/state feedback gaps. Coordinate with those rather than duplicating their implementations.

## Acceptance criteria

- [ ] A bounded readiness probe tests the actual configured browser executable/dependencies under the environment used by capture execution, including service versus scrubbed worker differences. Distinguish missing executable, missing shared libraries and sandbox/launch failure with an actionable diagnostic. Do not automatically grant privileges or modify host packages.
- [ ] Only capture-dependent work is held on an infrastructure prerequisite; unrelated work can proceed. Deduplicate repeated readiness failures/probes with a bounded retry/invalidation policy so no model revision or empty base probe is launched merely because the browser cannot start.
- [ ] After repair/config change, readiness is rechecked and preserved work continues exactly once through supported lifecycle actions. Retain original failed-run evidence, branch and task feedback; do not restart implementation or manufacture successful captures.
- [ ] A successful probe is explicitly not application acceptance. Current-head applicable flows still need real PNGs and executed interaction/viewport evidence. Missing images remain a failure with correct infrastructure/product classification.
- [ ] Focused lifecycle tests cover absent libraries, environment mismatch, repeated checks, recovery and unrelated-work admission using isolated fixtures. Document setup/diagnosis including unprivileged environments, without prescribing this operator host path as a universal setting. Local tests serial/capped, full exact-head CI remote; self-review and repair before completion.

## Log
- 2026-09-07T03:59:41+00:00 Owner-requested optimization prioritization: phase05 stabilization improvement, priority1; preserve phase06 feature freeze and current4slot/4second policy.
- 2026-09-07T04:22:52+00:00 Additional root-cause evidence04:20: service-only LD_LIBRARY_PATH was insufficient because launch of python checks itself uses scrubbed_env. Installed allowlist excludes LD_LIBRARY_PATH by default. Added explicit worker_env.pass=[LD_LIBRARY_PATH] to operator garden.yaml, accounted restart preserved4active workers; verified actual service path survives scrubbed_env with current config. Readiness must test the final child environment, not just service or direct browser probe. Earlier activation claim was incomplete.
- 2026-09-07T04:48:46+00:00 04:49 executable-config hold kept effective worker_env.pass empty despite disk config/restart; accepted exact operator allowlist via supported /config/accept-reload. Readiness must inspect effective scheduler/check payload and identify held configuration. Also CG323 baseprobe lint127 missing .venv/bin/ruff despite green exact-main CI shows setup readiness must be distinguished from source failure.
- 2026-09-07T04:58:48+00:00 dispatched work run 20260907T045827Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~9630 tokens)
- 2026-09-07T05:09:41+00:00 preserved uncommitted worktree changes from run 20260907T045827Z-work outside the PR: `git stash apply 96bce5eb0aa9e4c2c3d4b69265ae8621a997af2a` in /home/joshua/work/worktrees/CG-368 (garden:CG-368:20260907T045827Z-work:reap)
- 2026-09-07T05:12:32+00:00 opened https://github.com/joshmarcus/context-garden/pull/263 (base main): Capture-dependent tasks now wait on a bounded Chromium readiness probe executed in the effective scrubbed capture environment, while unrelated work continues. Readiness failures are cached, classified and automatically retried; successful launch remains distinct from required PNG and interaction evidence. cost=$1.71
- 2026-09-07T05:15:57+00:00 automated review requested changes: The bounded admission gate works for its tested happy path, but it conflates a missing Playwright package with a missing browser, incompletely classifies capture infrastructure failures, and does not prove preserved exactly-once lifecycle recovery or interaction evidence. cost=$0.99
- 2026-09-07T05:16:35+00:00 dispatched revise run 20260907T051633Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10752 tokens)
- 2026-09-07T05:27:35+00:00 preserved uncommitted worktree changes from run 20260907T051633Z-revise outside the PR: `git stash apply bb6791e7eb681d6c90673a241e4b800aa1413d44` in /home/joshua/work/worktrees/CG-368 (garden:CG-368:20260907T051633Z-revise:reap)
- 2026-09-07T05:28:56+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/263: Browser readiness now distinguishes missing Playwright from a missing configured browser, and capture checks propagate structured infrastructure failures while requiring separate executed navigation/viewport evidence. Normal scheduler recovery preserves failed-run evidence, branch, and feedback and dispatches the continuation exactly once. cost=$2.14
- 2026-09-07T05:31:46+00:00 automated review: approve — The readiness gate, recovery path, failure classification, and independent capture-evidence enforcement satisfy the task. Focused tests and lint pass locally, exact-head CI is successful, and all 56 listed captures were inspected. cost=$1.05
- 2026-09-07T05:35:28+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-07T05:35:38+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-07T05:37:39+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/263
