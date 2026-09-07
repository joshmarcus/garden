---
id: CG-365
title: Complete resource isolation enforcement and evidence after CG-361
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading: []
branch: garden/cg-365-complete-resource-isolation-enforcement-and-evid
discovered_from: CG-361
attempts: 1
last_dispatched_at: '2026-09-07T01:12:31+00:00'
created: '2026-09-06T23:47:10+00:00'
updated: '2026-09-07T01:21:04+00:00'
---

## Goal

Close the concrete remaining resource-isolation defects found in CG361's final review, so the operator can deploy a bounded execution profile and verify recovery without serializing useful agent work.

## Context

Reuse the existing discovered host-policy follow-up instead of opening a duplicate. CG361/PR244 merged at2d5e87459cd665f64cee334b6e5a3bdf335ef8ad at01:06:18 UTC on2026-09-07, before review20260907T010546Z-review finished at01:09:01. GitHub merged_by is joshmarcus; do not claim the reviewer approved it. Review of exact head7878424 found four actionable gaps. CG341/PR247 subsequently merged907ed1ed0dc05d3d0eb084cc3f121562c4a6ab66. Start from current main; never reopen the merged task as a revision or lose prior fixes.

Operator confirmed source: ResourceMixin.resource_status measures /proc/self/cgroup rather than configured resources.execution_cgroup; heavy_limit comes from requested config instead of authoritative metadata; _authoritative_limit and slot/owner locks open predictable files under XDG_RUNTIME_DIR or /tmp with ordinary following open calls. Reviewer also found the claimed workload journey only runs a short sleeping pytest without configured isolation or retained measurements. Earlier reviews had accepted that evidence; use actual configured enforcement and durable artifacts now.

CG361's useful existing behavior must remain: multiple model sessions and remote-CI waits can proceed within aggregate run/cgroup limits while supported heavy validation budget defaults1; shared authoritative host capacity and within-worker validations serialize with descendant/cancellation ownership. Do not regress to holding a heavy lease throughout every agent session. Full local suites remain prohibited; focused checks serial/bounded and exact-head full tests on GitHub CI.

## Acceptance criteria

- [ ] When resources.execution_cgroup is configured, admission reads its effective memory headroom and pressure/events as well as host/controller constraints. A regression with different controller/execution limits proves execution pressure prevents admission and reports the actual constrained boundary; missing or unreadable configured enforcement is visible rather than falsely healthy.
- [ ] Operator resource status, rail, observe and config distinguish requested and authoritative effective heavy capacity and expose conflicts. A limit1/limit2 fixture shows all views agree with enforced capacity, including before/after active validation changes.
- [ ] All shared capacity metadata and host/owner slot locks use a verified user-owned private0700 runtime directory, reject symlinks/untrusted ownership/nonregular files, and avoid following hostile path substitutions. Cover the no-XDG_RUNTIME_DIR fallback and hostile precreated files with focused tests. Preserve legitimate restart/limit-conflict behavior and document migration without deleting active locks or another user's files.
- [ ] Produce a durable reviewable artifact from one bounded real validation workload and a waiting validation under an isolated, finite execution cgroup separate from the fixture web/controller. Exercise retained-history Now, Inbox, task control and pause; record timestamped commands, limits, latency, CPU/memory pressure, memory.events, temp and live descendants. Meet local<2second journey targets without new high/OOM events. A sleeping test or ambient uncapped measurements do not demonstrate reserved capacity. Never use production fault injection or parallel full suites.
- [ ] Preserve two concurrent useful model sessions with at most one supported heavy validation, cancellation/descendant cleanup, authoritative capacity, and honest unsupported-command boundaries. Self-review/fix internally; report ordinary acceptance evidence, passing focused checks/lint and exact-final-commit GitHub CI. Do not claim unattended stabilization or real adoption.

## Implementation safety

Do not modify production services, increase OS caps/concurrency, move live temp/history or launch additional model agents. Prepare isolated test units and operator deployment guidance, including safe provisioning of the separate execution cgroup under existing total host budgets. Coordinate current main before final CI; preserve unrelated artifacts using installed CG359's named salvage mechanism. Actual deployment and three loaded recovery journeys over ten minutes remain operator responsibilities after merge.

## Provenance

Discovered originally byCG361 during run20260906T232501Z-revise; expanded from its final current-head review completed after merge. This is priority0 continuation of the existing incident, not a new feature.

## Log

- 2026-09-07T01:11:52+00:00 Operator01:12 UTC expanded existing draft with four verified remaining CG361 review findings after its merge; keep production pinnedfc658809 until repaired deployment is ready.
- 2026-09-07T01:11:53+00:00 approved (cli)
- 2026-09-07T01:12:31+00:00 dispatched work run 20260907T011212Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9886 tokens)
- 2026-09-07T01:21:04+00:00 Operator01:21 UTC inspected active work atd1f1c23/faadd08 without changing the worker tree. Enforcement fixes and new artifact exist, but tests/test_web.py::test_retained_history_journey_stays_responsive_with_running_and_waiting_pytest still generates only time.sleep(0.75). report.json labels supervisor PIDs as live_supervisor_descendants and omits execution cgroup CPU/memory PSI and aggregate CPU usage; memory sample12MiB and supervisor ticks do not establish representative running pytest load. The isolated finite cgroup is a useful improvement, but criterion4 remains UNPROVEN until a bounded nontrivial workload is synchronized as actually running and its real descendants/aggregate pressure are recorded. Reuse this finding in the next review/continuation, not a duplicate task. No local full suite, production changes, or extra agent needed.
