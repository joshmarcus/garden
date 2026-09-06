---
id: CG-338
title: Keep the operator machine responsive under concurrent workers and test suites
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 3
difficulty: hard
reading: []
branch: garden/cg-338-keep-the-operator-machine-responsive-under-concu
attempts: 1
last_dispatched_at: '2026-09-06T19:14:37+00:00'
created: '2026-09-06T13:27:34+00:00'
updated: '2026-09-06T19:14:37+00:00'
---

## Goal

The scheduler keeps the owner machine responsive and avoids exhausting temporary storage while workers, reviews and checks overlap. Resource pressure is handled as an environment condition, not a wave of task failures.

## Context

Josh reported high load on 2026-09-06 at 13:26Z. The 7.7GiB WSL instance had five workers, two reported reviews, multiple concurrent full pytest suites, load 5.69 and 2.2GiB used on a 3GiB tmpfs. The operator paused new dispatch, reduced max_parallel from five to two, and applied a runtime systemd CPUQuota=200% / CPUWeight=20 without killing workers. CG-329 addresses slot counting; CG-310/335 address worker temp paths. Coordinate rather than duplicate those fixes. Harness-launched full suites also consume resources beyond the scheduler check records.

## Acceptance criteria

- [ ] Admission or configurable resource limits account for overlapping workers, reviews and checks; an overloaded host can drain without restarting the service or discarding work.
- [ ] Low temp headroom prevents a cascade of dispatch/check failures; cleanup proves a run is inactive before removing its directories.
- [ ] The UI and operator feed identify resource pressure and the effective limits with a clear recovery action. Retries distinguish environment exhaustion or throttling from branch defects.
- [ ] Provide focused regression evidence and a documented local operating profile that keeps the owner machine responsive.

## Log

- 2026-09-06T13:27:36+00:00 approved (cli)
- 2026-09-06T13:46:58+00:00 priority 1 -> 0

## Memory incident evidence, 2026-09-06 15:00Z

The owner rebooted after host lockup. The prior garden cgroup peaked at 6.5GiB with no memory cap. Full pytest suites overlapped in workers and reviews; /tmp is a 3GiB tmpfs. After reboot the runtime CPU cap was lost. Persistent service limits now CPUQuota=200%, CPUWeight=20, MemoryHigh=3GiB, MemoryMax=4GiB, MemorySwapMax=512MiB; worker and review concurrency are one each. A lightweight guard samples every 15 seconds for an hour, recording cgroup anon/file/shmem, swap, VM available memory, temp space and top process RSS, and pauses dispatch on pressure. Logs: /home/joshua/.local/state/garden-operator/resource-watch.jsonl (operator-owned, do not edit). Distinguish anonymous memory, reclaimable file cache and shmem: memory.current is not process RSS, and summing RSS double-counts shared pages. The 102MiB scheduler state amplification is separately tracked in CG-344. No retained kernel OOM event proves the exact lockup cause.

Critical coverage finding at 15:12Z: manual `garden dispatch` and `garden review` CLI launches inherit /init.scope, escaping garden-serve.service cgroup caps and service-only RSS enumeration. CG-344 worker PID62303 and its descendants were moved under the service cgroup by the operator. Enforce limits and report resource use across every launch path, including CLI, without changing intended dispatch authorization. Prefer server POST actions for operator launches until fixed. Add coverage demonstrating CLI-dispatched work cannot bypass configured limits.

Recovery measurement 2026-09-06 16:15:56Z: ordinary dispatch paused and max_parallel=review_parallel=1, yet three pytest processes ran concurrently (CG-342 pre-PR plus CG-215 and CG-344 base probes following main movement). Cgroup memory 3,213,402,112 bytes, shmem 841,412,608, load 2.21, no OOM. Admission must include automatic base probes, not only work/review dispatch; pause alone is not a global execution bound. Evidence: operator resource-watch.jsonl.
- 2026-09-06T19:14:37+00:00 dispatched work run 20260906T191420Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~9054 tokens)

## Web-incident retro extension, 2026-09-06

CG-294 had four simultaneous pytest processes that survived stopping its harness/process group; each was verified in its worktree and terminated manually. Add acceptance coverage for per-run descendant ownership across detached sessions, duplicate overlapping full-suite admission and stop/drain verification. Preserve recovery artifacts, respect caps across all launch paths and distinguish environment interruption from code failure. Counterfactual: bounded per-run tests and complete descendant cleanup would have reduced contention and freed recovery capacity promptly. Provenance: docs/incidents/2026-09-06-web-responsiveness-retro.md.
