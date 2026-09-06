# Web responsiveness incident — 2026-09-06

Status: REOPENED around21:04 UTC after recurrent timeout under resource contention. Original19:13 recovery and retrospective remain historical evidence, not proof of current stability. Lead: current garden operator. Impact began around 17:43 UTC: dynamic pages unavailable or timing out for the owner and browser-dependent work. Static/clock success does not establish recovery.

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

18:30 UTC: CG-357 PR #234 received changes requested for repeated full-history rebuilds, archive integrity/cost correction handling and insufficient realistic performance evidence. Operator removed the unrelated snapshot diff in a7bab24, preserving /home/joshua/work/operator-test-tmp/CG357-snapshot-salvage.json. Reviewer's 89-commit claim was disproven by refreshed origin/main comparison (four scoped original commits); recorded correction in brief. Sent one capped server revision dispatch, HTTP303. Latest run 20260906T183056Z-revise; PID 2178766. Keep incident active and admission paused; repair is not installed.

18:54 UTC operator validation: PR#234 code findings resolved; removed reintroduced unrelated snapshot again and added actual served workload evidence in a804c04. Three independent local CPU/metadata worker processes plus uvicorn shared CPU200%, MemoryHigh3G/Max4G/Swap512M. 60 HTTP requests each:1546 history p95 .213s/max .320s (1576 reads/10 refreshes);6000 p95 .570s/max .695s (6054 reads/19 refreshes). Windows browser verified live Now updates, Open run, Board and Inbox with workers executing. These are controlled workload processes, not model harness sessions. Production still unverified. Current-head CI pending; merge/install after it passes and live work drains, then perform recovery observation and owner-required retro. Evidence in PR docs/design/cg357-validation.

18:59 UTC: PR234 merged8842552190ef675dd0af281ea23a82f15cdb1963 after current-head CI passed and GitHub CLEAN. CG-357 reconciled done. Confirmed no active run records or live worker/test processes; installed that merged build in bounded service (138MiB peak). Restart requested with admission still paused and caps retained. Live verification and10-minute observation are next; incident not closed.

19:00 initial production verification: Windows HTTP Inbox/Board/Now1/Now2 all200 (2.825/2.510/2.637/2.599s including Windows client path); WSL Now2 .547s. Windows browser opened live Now2 and navigated Board→Inbox→Now1 successfully. Server PID2315784; caps retained. Observation begins19:00, needs two further samples through at least19:10 including controlled workload. At19:01 one CG-329 revision dispatched through server,303; ordinary admission remains paused. Verify worker PID/progress and page/resource health on next checks.

19:07 recovery sample2: actual Inbox/Board/Now1/Now2 all200 in .688/.506/.641/.626s from WSL. Windows127.0.0.1 Now2 200 in .754s, supporting localhost client-resolution/fallback overhead as the earlier extra ~2s (inference, not fully isolated). CG-329 controlled revision has advanced to live check20260906T190657Z-check PID2441933. Service memory538MiB, zero swap and no memory.high/max/OOM events since restart. Observation not yet ten minutes; keep admission pause until next successful sample at/after19:10.

19:13 recovery sample3: Inbox/Board/Now1/Now2 all200 in .626/.456/.548/.581s WSL; WindowsIPv4 Now2 .645s. Three successful samples span13 minutes and included a genuine CG-329 revision/check workload. Memory357MiB, zero swap/high/max/OOM events after restart. Normal global resume returned200; concurrency remains3 workers/1 review with caps. Incident closed. Retrospective completed in 2026-09-06-web-responsiveness-retro.md. Filed CG-358/359; expanded CG-338/339, clarified CG-331 and linked CG-333. Existing CG-354/355 retained without duplicate tasks. Return operator reminder to25 minutes; preserve recurrence monitoring and CG-294 recovery.

Recurrence around21:04 UTC: owner asked status; Now2 timed out6s while clock responded .18s. Three workers active, service memory3.03GiB, VM swap~514MiB and tmp58%; cumulative high events3.59million, no OOM. Multiple pytest processes overlapped. Operator paused admission, reduced temporary worker limit to1 retaining all caps, preempted CG-326 through Run.stop and preserved worktree/transcript plus /home/joshua/work/operator-test-tmp/CG326-recurrence.patch. CG-358/323 allowed to drain/continue bounded work. Subsequent Now2 returned200 in1.12s and service memory2.51GiB. This is initial relief only; incident reopened with5-minute monitoring. Recovery review must address real test/harness concurrency: prior controlled workload evidence did not establish safety under overlapping full suites. Add recurrence to retro after recovery.
