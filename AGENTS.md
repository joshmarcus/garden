# Context-garden operator handoff

Current handoff, consolidated 2026-09-06 ~17:14 UTC. Replace obsolete state here instead of appending contradictory updates. Verify live state before acting. Historical handoffs are archived in `context-garden/docs/operator-history/`; do not read them as current instructions.

## Start here

Read `.claude/skills/garden-operate/SKILL.md` for supported operator actions, then `context-garden/docs/incident-protocol.md` when basic operation is interrupted. `context-garden/docs/fast-forward.md` documents owner-invoked PR maintenance; it is currently inactive. This file owns current state; the manual supplies procedures. The garden is `/home/joshua/garden`; product worktrees are `/home/joshua/work/worktrees/CG-NNN`. Use the installed `.venv/bin/garden` for state-only actions. Never manually edit task status or race the scheduler's state writer.

## Owner authority and priorities

Josh delegates routine decisions, task approvals, direct fixes, PR merges and filing process gaps. Do not repeatedly ask him to interpret scheduler states. Preserve unfinished work and distinguish actual live processes from labels. No extra model review is required for operator self-reviewed repairs during fast-forward. Keep tests serial and resource-bounded. Do not launch additional agents without explicit authorization.

Phase 05 is stabilization/adoption, governed by `context-garden/phase-05/specs/stabilization.md`: four productive unattended hours, at least ten representative completed tasks, recovery exercises, real application journeys and named-project adoption evidence. Operator repairs are interventions, not unattended progress. Missing evidence is UNPROVEN. Phase 06 remains frozen; new feature requests belong there as drafts. Onboarding stays active. Both Now pages and the main Now CLI repair have merged; do not resurrect their old repair queue.

Workers must internally self-review, fix findings and recheck before completion. They report ordinary acceptance-criterion evidence, not a separate self-review report. This is included in `principles/00-index.md` and verified in generated briefs.

## Normal operation restored, 2026-09-06 17:40 UTC

Josh explicitly ended fast-forward and requested normal operation before the final eligible PR merged. Fast-forward is INACTIVE: its service drop-in was removed, existing garden-serve.service restarted with normal watch, and global dispatch resumed (HTTP 200). Do not re-enter maintenance merely because #223 remains open. The disposable UI fixture services were stopped.

PRs #232/CG-344, #229/CG-254 and #228/CG-296 merged and tasks are done. Josh merged #216/CG-215 at 545c745f6cc38087f4623a7a5726768e17856a02; reconciled done. #223/CG-324 subsequently merged at cf76e6ed1f671b5a9d5a6055ae8f3d1f127a07ae; normal scheduler reconciled it to done. All five eligible PRs are now merged. Frozen #221/#222 remain open and excluded.

The operator heartbeat checks every five minutes until 18:41 UTC after the owner increased concurrency, then returns to ordinary 25-minute duties: status/inbox/digest and live resource checks, act on actionable stalls with owner authority. Continue stabilization work with three worker slots, one review and caps; no unattended stabilization claim follows from supervised repairs. CG-355 tracks automatic update/restart regression; CG-356 tracks onboarding rejected-plan recovery.

## Resource limits and services

Persistent garden service limits: CPUQuota=200%, CPUWeight=20, MemoryHigh=3G, MemoryMax=4G, MemorySwapMax=512M. Josh explicitly increased the live max_parallel override to 3 at 17:41 UTC; review_parallel remains 1. garden.yaml retains its conservative default of 1; the persisted live override governs dispatch. Retain CPU/memory caps and watch actual pressure. For routine restarts, verify no active workers or checks. During an incident use the deliberate preservation/restart procedure in `context-garden/docs/incident-protocol.md`; KillMode=process means detached work can survive.

CLI-spawned work bypasses service limits. During maintenance launch manual checks in a separate bounded systemd user service (2 GiB memory, 2 CPUs used for current fixes), with disk temp `/home/joshua/work/operator-test-tmp`. Normal future work should use capped server launch paths. CG-338 owns comprehensive resource admission.

`/tmp` is a 3 GiB tmpfs; `/home/joshua/work/tmp` links to `/tmp/garden-work`. The worker-temp service drop-in recreates that target. Never delete active-run temp. The timed two-minute resource monitor has ENDED; its JSONL is historical, not live monitoring. Inspect current /proc and service cgroup memory/events/load.

The host previously locked up: overlapping test suites, RAM-backed temp and a 102 MiB state file with duplicated manifests were measured contributors, not a proven final OOM cause. Preserve recovery data; do not clear state/manifests or caches blindly.

## Installed build

Installed pin is 14676f50bf6e68fb0c5111c7c8a0c96d66cfc8aa as of 2026-09-06 17:40 UTC (verified main CI). It includes memory/lifecycle/operating UI repairs; onboarding's merge had main CI in progress at install time and is not yet installed. Existing server runs normal watch; /, /now1 and /now2 returned HTTP 200 after restart, and global resume returned 200. Verify current state before future pin movement; prefer drained installation/restart; incident exceptions require the preservation and verification procedure. Retain caps and phase holds. Global resume is POST http://127.0.0.1:8765/resume with matching loopback Origin; CLI resume requires a task id.

Read git log before pushing and commit only intended files. Codex operator spend remains unavailable until CG-336; never substitute Claude spend.

## Active web responsiveness incident

Incident protocol is ACTIVE. Current incident record: `context-garden/docs/incidents/2026-09-06-web-responsiveness.md`. Recovery is not verified; preserve admission pause.

Last verified process/resource details at 18:04 UTC

At 18:21 UTC CG-357 worker finished and check 20260906T182127Z-check (PID2114402) is active. No duplicate worker dispatch needed. Worker reports1172 tests/3 skips and fixture performance improvements; installed/live recovery remains unverified. Scheduler salvage commit7b818c4 accidentally included unrelated snapshot.json; remove its diff after check drains, preserving it, before merging. See incident record for review/evidence details. CG-329 review requested changes; keep it subordinate to recovery. Keep admission paused; full web recovery is not established.

Root-cause evidence: py-spy showed repeated full-history scans in concurrent dynamic request threads (RunStore, phase spending, Inbox, Now snapshots and scheduler construction); roughly 1,550 durable run records. CG-357 covers bounded read models and safe archival; no history moved/deleted. Process-local Run.load cache experiment did not fix access and disappeared at the owner-authorized restart around 17:57 UTC. Current server PID 1690856; do not reapply the experiment. Windows/WSL clock endpoint returned 200 after restart, but full Now requests still fail.

CG-294 was preempted via Run.stop and task returned ready through CLI. Its branch head f129ed553e6fcc7733be06d87628166ebbe0d454, dirty snapshot and transcript remain preserved; extra patch /home/joshua/work/operator-test-tmp/CG294-web-outage-recovery.patch. Four escaped pytest processes verified in its worktree were terminated. Resume preserved work after urgent repair. CG-357 original startup 20260906T175413Z-work was interrupted before worker launch and superseded; replacement above is live.

18:04 resource sample: service memory 2.66 GiB, swap 380 MiB; memory.high throttling has occurred (11830 cumulative events), no max/OOM kills. VM available 4.8 GiB, /tmp 41% used. Do not increase concurrency; inspect trends and actual tests, preserve active work. This is supervised recovery, not unattended stabilization.

## Required follow-up after this incident

Josh explicitly requests a retrospective after verified recovery and filed tasks that would have prevented the incident. Follow the required retro section in the incident protocol, link existing related work instead of duplicating it, and keep the reminder active until the retrospective and concrete prevention tasks are recorded.
