---
id: CG-382
title: Profile and reduce repeated Store scans per web request
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/store.py
discovered_from: CG-380
created: '2026-09-07T13:02:16+00:00'
updated: '2026-09-07T13:19:06+00:00'
file: src/garden/store.py
error: Task/product scanning averaged about 52ms on Now and Inbox, roughly 40% of request CPU, and was
  the largest named controller span.
---

Instrument Store scanning on the retained-history fixture to count filesystem stats and YAML parses per page request. If repeated work is confirmed, reuse one immutable request-local snapshot while preserving cross-process freshness and compare matched page latency before and after.

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

- [ ] Preserve exact build, fixture size, commands, sample counts and matched before/after evidence for the proposed mechanism. Distinguish measured savings from hypotheses.
- [ ] Retain data freshness and existing hard caps/pressure safeguards. All load experiments use disposable bounded environments; no production cache deletion, pressure injection, or cap relaxation.
- [ ] Report a narrow justified fix or explicit evidence-backed disposition; focused regression tests and exact-head CI for code changes. Self-review and repair findings before completion.
- 2026-09-07T13:19:06+00:00 approved (operator-incident-followup)
