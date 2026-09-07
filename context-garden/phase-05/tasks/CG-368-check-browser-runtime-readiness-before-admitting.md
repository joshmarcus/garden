---
id: CG-368
title: Check browser runtime readiness before admitting capture-dependent work
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading: []
created: '2026-09-07T03:58:51+00:00'
updated: '2026-09-07T04:48:46+00:00'
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
