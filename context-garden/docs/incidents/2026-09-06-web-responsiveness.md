# Web responsiveness incident — 2026-09-06

Status: ACTIVE. Lead: current garden operator. Impact began around 17:43 UTC: dynamic pages unavailable or timing out for the owner and browser-dependent work. Static/clock success does not establish recovery.

## Current containment and recovery

Ordinary admission paused; max_parallel override 3, reviews 1, persistent CPU 200%, MemoryHigh 3 GiB / Max 4 GiB / SwapMax 512 MiB retained. Phase 06 frozen. CG-357 implementation run finished and entered check 20260906T182127Z-check (PID 2114402) at 18:21 UTC. Worker reports 1172 tests passed / 3 skipped, lint passed, and a 3003-record FastAPI benchmark; this is not yet live Windows browser recovery evidence. CG-329 received requested changes about edit admission; keep unrelated revision work subordinate to incident recovery. Recheck live state before acting.

CG-294 was preempted and returned ready; branch/head f129ed553e6fcc7733be06d87628166ebbe0d454 and dirty edits/transcript preserved. Extra patch: /home/joshua/work/operator-test-tmp/CG294-web-outage-recovery.patch. Four escaped pytest processes verified in its worktree were terminated. Resume preserved work after recovery.

## Evidence and interventions

- Windows and WSL dynamic requests exceeded 8–20 seconds; static favicon responded in about 0.02 seconds. Server remained alive.
- py-spy showed concurrent requests repeatedly scanning roughly 1,550 run records through RunStore, phase spending, Inbox/Now and scheduler construction. Full causal/performance verification remains CG-357's responsibility.
- Bounded file-stat-invalidated Run.load parse cache was tried in the running process; tests covered fresh writes, isolation and corrupt data, but full page still timed out. Ineffective; removed by restart. No history moved/deleted.
- Owner authorized restart around 17:57. Existing service restarted, CG-337/329 survived. Clock endpoint recovered; full Now still exceeded 20 seconds. CG-357 pre-worker startup was superseded and one replacement dispatched; replacement subsequently verified live. Do not duplicate it.
- 18:10 resource sample: service memory about 2.69 GiB, swap 23 MiB, VM available about 5.3 GiB, tmpfs 14% used; cumulative memory.high events increased, no max/OOM kills. Pressure has occurred; retain caps.

## Next action and exit evidence

Follow actual CG-357 progress, validate the smallest effective recovery and deploy safely. Separate longer-term archival work if it delays restoration. Do not wait for unrelated feature work or perform browser acceptance against an unavailable application. Verify Inbox, Board and Now from Windows with representative history, latency and resource measurements, then observe a controlled resumed workload per incident protocol. Current installed pin last verified 14676f5; verify before changing. No successful full recovery or exit observation is recorded yet.

After recovery: reconcile preempted work, remove temporary controls deliberately, update handoff/automation, and record root cause and prevention. This is supervised recovery, not evidence that phase 05 stabilization passed.

## Review issues identified at 18:21 UTC

The scheduler salvage commit 7b818c4 included the unrelated docs/design/snapshot.json that the worker deliberately left uncommitted. Preserve it externally/in existing commit history and remove it from the PR diff after the in-flight check drains; do not alter a checked worktree underneath its test. Inspect whether an existing salvage task covers this recurring pollution, otherwise file a scoped follow-up. Worker benchmark reports p95 0.420s above max 0.388s (likely quantile extrapolation); clarify actual measured distribution. Fixture active-run records are not three real resource-saturated workers, and do not satisfy live browser recovery. No repair has yet been installed.

18:21 resources: service memory about 1.23 GiB, swap109 MiB, VM available6.45 GiB, tmp3%; no max/OOM kills. Admission remains paused.

## Post-recovery obligation

Owner explicitly requested a retrospective and prevention tasks after recovery. Pending: write retrospective beside this record, analyze confirmed causes and detection/review/recovery gaps, and file/link concrete prioritized tasks with counterfactuals and measurable criteria. Candidate evidence to investigate includes repeated history scans, unrealistic performance fixtures, automatic commit of unrelated snapshots, duplicate/escaped tests, slow control-plane dispatch and interrupted startup recovery. These are topics for evidence-based assessment, not predeclared conclusions. Record completion and task IDs here before clearing the incident follow-up reminder.
