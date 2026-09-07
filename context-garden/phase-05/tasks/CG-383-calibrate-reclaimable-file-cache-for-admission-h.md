---
id: CG-383
title: Calibrate reclaimable file cache for admission headroom
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/config.py
discovered_from: CG-380
created: '2026-09-07T13:02:16+00:00'
updated: '2026-09-07T13:19:25+00:00'
file: src/garden/scheduler/resources.py
error: The admission sensor counts all memory.current against memory.high; the operator sample had about
  2,198MiB file cache, 5,621MiB host MemAvailable and zero pressure/events but reported only 550MiB cgroup
  headroom.
---

In a disposable cgroup with the existing hard memory cap and reserve, populate file cache, record memory.stat working-set fields and PSI/events, issue bounded memory.reclaim, and measure reclaimed bytes plus a one-slot launch high-water mark. Use the result to decide whether a guarded reclaimable-cache allowance is safe without weakening hard caps, pressure/OOM safeguards, or the owner-configured shared-slot cap.

## Provenance

Discovered by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`.
## Log
- 2026-09-07T13:02:16+00:00 discovered by CG-380
- 2026-09-07T13:03:31+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:04:53+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:06:07+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:07:21+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:08:35+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:09:48+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:11:03+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:11:29+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:11:39+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:12:55+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:14:13+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:15:32+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:16:55+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`
- 2026-09-07T13:18:20+00:00 also found by CG-380 (Attribute controller, scheduler, and worker performance under load) during run `20260907T123241Z-work`

## Acceptance criteria

- [ ] Measure the proposed mechanism on a disposable bounded fixture with exact build, commands and resource deltas.
- [ ] Preserve hard caps, pressure safeguards and data freshness; no production cache deletion or fault injection.
- [ ] Report justified fix or evidence-backed disposition, with focused regression checks and exact-head CI for code changes. Self-review and fix findings.
- 2026-09-07T13:19:25+00:00 approved (operator-incident-followup)
