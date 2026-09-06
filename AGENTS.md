# Context-garden operator handoff

Current state consolidated 2026-09-06 22:23 UTC. Replace obsolete claims rather than appending contradictory overrides. Verify live state before acting. Historical handoffs in context-garden/docs/operator-history are evidence, not current instructions.

## Start here

Read .claude/skills/garden-operate/SKILL.md for supported actions and context-garden/docs/incident-protocol.md for interrupted basic operation. The garden is /home/joshua/garden; product worktrees are /home/joshua/work/worktrees/CG-NNN. Use installed .venv/bin/garden for state-only actions. Never hand-edit task status or race the scheduler state writer. Fast-forward is INACTIVE; context-garden/docs/fast-forward.md is the owner-invoked maintenance procedure, not an active queue.

## Owner authority and priorities

Josh delegates routine decisions, task approvals, direct fixes, PR merges and process-gap filing. Do not repeatedly ask him to interpret scheduler states. Preserve work and distinguish process liveness from labels. No extra agents without explicit authorization. Keep tests serial and resource-bounded.

Workers internally self-review, repair their findings and recheck before completion. They report acceptance-criterion evidence, not a separate self-review report. This is in principles/00-index.md and verified in generated briefs. Reviewers directly fixing code remains deferred by the owner.

Phase 05 stabilization remains UNPROVEN: four productive unattended hours, ten representative completions, recovery exercises, real application journeys and named-project adoption. Operator repairs are interventions. Onboarding and both Now pages merged; do not resurrect their old queue. Phase 06 and PR221/222 remain frozen. New features belong there as drafts.

## Active incident and current containment

Web responsiveness incident reopened around 21:04 UTC after Now2 timed out amid overlapping suites and service memory.high pressure. Earlier closure at 19:13 was superseded by recurrence. Incident record: context-garden/docs/incidents/2026-09-06-web-responsiveness.md. Initial retro is complete; recurrence recovery observation and final retro addendum remain due. Follow the incident protocol before closing.

Ordinary admission remains PAUSED. Temporary live worker limit=1, review limit=1; garden.yaml also sets resources.max_parallel=1 across local work/reviews/checks/base probes, min_memory_available_mb=1536 and min_temp_free_mb=1024. These combined limits are now INSTALLED and enabled. Do not restore the owner's earlier three-worker limit without workload evidence. A full shared slot is admission saturation, not evidence of actual memory pressure.

Persistent garden-serve.service caps: CPUQuota=200%, CPUWeight=20, MemoryHigh=3GiB, MemoryMax=4GiB, MemorySwapMax=512MiB. Web and tests still share this resource budget. CLI launches share garden admission now, but OS budget isolation across launch paths is NOT established; prefer capped server POST actions. Manual heavy work uses a bounded systemd user service, disk temp /home/joshua/work/operator-test-tmp, and serial tests. Never start a second garden server.

/tmp is a 3GiB tmpfs; /home/joshua/work/tmp links to /tmp/garden-work, recreated by the worker-temp drop-in. Never delete active temp. The earlier timed two-minute monitor ended; the current five-minute operator heartbeat is active. Inspect actual cgroup/process pressure, not cumulative counters alone.

## Installed build and verification

Installed pin 6dd3ae49f448f088f8aef10aceb331a68620425c (CG-338 shared admission and descendant supervisor), current main CI success verified. Updated around 21:37 UTC after all runs and actual test/harness processes drained and a fresh tick boundary was observed. Stopped the existing service, installed in a bounded unit (152MiB peak), restored read-only venv permissions, started the existing service. PID1840342 at verification. Prior pin8842552 replaced; no runtime hot patches remain. Also includes CG-330/343 and earlier onboarding/Now/evidence fixes.

Effective resource_status initially active0/limit1, available memory5987MiB/temp2208MiB. HTTP /, /now2, /inbox, /config returned200 in .25-.68s. With recovery work active, Now2 .876s and Windows browser Now2 -> Open run -> Board succeeded. Shared gate reported active1/limit1 and zero free slots. Service memory333MiB, swap0, no memory.high/max/OOM events at that observation. This is initial verification, not the required sustained loaded recovery proof or an unattended phase pass.

## Active recovery work and remaining gap

CG-361 priority0: Bound test workloads within each run and reserve web capacity. Approved and dispatched once via capped server at21:40:06, run20260906T214006Z-work, codex/gpt-5.6-sol. HTTP client timed out but work continued: PID1841626 confirmed live, stdout198167bytes with fresh output at21:42. Do not duplicate dispatch. Verify current PID/output before reporting continued activity.

CG-338 caps parent run records and owns descendants; it DOES NOT cap several pytest suites started inside one worker or reserve CPU/memory for the web service. CG-361 is implementing this enforcement gap, including effective cgroup sensing and actual loaded web/control journeys. Run admission lock is garden-scoped, not automatically every garden on the host. Keep ordinary dispatch paused while this controlled repair runs. Workers must not alter production services or run parallel full suites during implementation.

CG-354 focused-test development task is priority1/ready and now includes bounded Git fixture waits/descendant cleanup after the stall below. CG-360 was directly implemented by the operator alongside the sole worker. PR242 merged44b9a312e7f56c73de3b012a67ce2cff65da2d51 at22:16 UTC; task is DONE. Final full CI1201passed/3skipped; focused ext4 tests33passed and tmpfs14passed, all local tests under100MiB. Worktree /home/joshua/work/worktrees/CG-360, branch codex/cg-360-restore-index. Evidence: docs/incidents/CG-360-validation.md. NOT INSTALLED: retain production archive/restore hold until a drained update. No production history moved/deleted. CG-362 priority1/ready covers external/manual task completion overhead. If main check failures recur, inspect actual check evidence; the known ext4 restore failure may be relevant, but do not label all failures or killed probes as the same source defect.

CG-329 PR233 remains DRAFT safety-held; preserve it until shared admission is verified under intended work, and account for the remaining per-run test gap. CG-337 PR235 needs current review reconciliation (correctness reportedly passed, repeated unrelated screenshot/snapshot blockers). CG-358 PR239 recovery controls awaits current review/rebase; CG-323, CG-322 and CG-293/PR240 need evidence-based state reconciliation. Do not retry a task from stale observations: retry can cancel a just-started automatic run. Check live run and PR state immediately before mutation.

CG-326 preempted at21:04: worktree/transcript preserved, extra patch /home/joshua/work/operator-test-tmp/CG326-recurrence.patch, ready to resume later. CG-294 preempted17:51: headf129ed553e6fcc7733be06d87628166ebbe0d454, dirty edits/transcript preserved, patch CG294-web-outage-recovery.patch in the same directory; four escaped tests stopped. CG-338 retry race backup CG338-retry-race-2013.patch remains preserved. Do not blindly reset or discard these artifacts.

## Measured test costs and follow-up

Owner-requested serial same-suite A/B at c1f75cb: tmpfs163s/969MiB peak; ext4 222s/1523MiB peak with I/O stalls .19% versus11.47%. Negligible CPU throttling and no memory pressure in either isolated run. Memory includes cache/kernel/descendants, not just Python heap. One ordered pair does not prove concurrent incident causality; it gives no basis to move live temp to disk for speed or peak memory. Multiple ~1GiB suites against shared3GiB high/4GiB max is a strong capacity warning, not exact additive accounting. All experiment units finished.

Evidence and scripts: context-garden/docs/incidents/test-temp-ab/README.md and adjacent JSON/source. Raw logs/temp preserved under /home/joshua/work/operator-test-tmp/io-ab-20260906. Ext4 archive round-trip failure reproduced separately; CG-360 tracks it.

The existing operate-context-garden heartbeat runs every five minutes. Next: watch actual CG-361 work and resources; do not duplicate launches or raise concurrency. Verify shared admission and descendant accounting during intended workload; obtain three representative journey checks over ten minutes with loaded evidence before declaring incident recovery. Complete recurrence retro/prevention addendum and maintain CG-360 archive hold. Restore ordinary25-minute cadence only after recovery/follow-up, retaining unresolved safety limits as appropriate.

Owner authorizes useful direct implementation in this operator session alongside the sole scheduled worker; keep changes independent and tests serial, without starting another model agent for the direct work. CG-360 is the first completed direct task.

At22:08 pytest1962007 was stalled after its Git push child exited128 but orphan fixture helpers1995748/1995749 retained stderr. Operator verified process identity/start times/cwd/pipes and terminated only those helpers in the disposable test_persona_without_sections_0 fixture. Pytest then finished425passed/1fixtureerror after694.80s. CG-361 agent and commits were preserved; no full-suite pass is established. Process evidence is operator-test-tmp/CG361-orphan-git-helpers.json; task notes and CG-354 record the incident. Diagnose original Git failure before another full retry. Verify fresh CG-361 output/processes; last observed commits included df9b4e7 with QA lease isolation.

CG-360 manual finish bookkeeping initially failed after an operator worktree move. Original path restored; all protected hashes match the dispatch snapshot. Only the resolved block for that exact manual run was archived (operator-test-tmp/CG360-resolved-git-block.txt); the clone is no longer blocked. Actual branch/PR recorded, normal ancestry-checked set-status done succeeded without force. Failed manual run220127 remains honest audit evidence, not successful automated work. CG-362 tracks a supported external completion workflow; avoid moving a worktree after take has snapshotted it.

At22:04 Now2 returned200/1.171s during worker test workload, service memory1.32GiB/swap0 and no memory.high/OOM. This adds recovery observation; recurrence closure and final retro addendum remain outstanding. Installed pin remains6dd3ae49 and ordinary admission stays paused.

Read git log before pushing; commit only intended files. Many scheduler-owned task/spend/friction changes may be dirty. Codex operator spend remains unavailable until CG-336; never substitute Claude spend. Global resume is POST http://127.0.0.1:8765/resume with matching loopback Origin; CLI resume requires a task id. Routine pin updates require accounted drain; incident restarts follow the preservation procedure. No fast-forward drop-in or fixture server is active.
