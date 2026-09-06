# Web responsiveness incident — 2026-09-06

Status: ACTIVE. Lead: current garden operator. Impact began around 17:43 UTC: dynamic pages unavailable or timing out for the owner and browser-dependent work. Static/clock success does not establish recovery.

## Current containment and recovery

Ordinary admission paused; max_parallel override 3, reviews 1, persistent CPU 200%, MemoryHigh 3 GiB / Max 4 GiB / SwapMax 512 MiB retained. Phase 06 frozen. CG-357 is priority 0 and replacement run 20260906T175931Z-work was confirmed live; at 18:10 it was editing bounded history/index, web and archival code. CG-337/329 had moved from workers to checks. Recheck live state before acting.

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
