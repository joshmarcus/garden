# Context-garden operator handoff

Current handoff, consolidated 2026-09-06 19:01 UTC. Replace obsolete state here instead of appending contradictory updates. Verify live state before acting. Historical handoffs are archived in `context-garden/docs/operator-history/`; do not read them as current instructions.

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

Installed pin8842552190ef675dd0af281ea23a82f15cdb1963 (CG-357 PR234) at18:59 UTC after current-head CI and merge. Existing service restarted with no active workers/checks, caps and admission pause preserved. New server PID2315784. This also includes earlier onboarding/evidence/UI repairs. No temporary runtime patches remain. No production history moved or deleted. Verify current state before further pin changes.

Read git log before pushing and commit only intended files. Codex operator spend remains unavailable until CG-336; never substitute Claude spend.

## Web incident: observing recovery from 19:00 UTC

Follow `context-garden/docs/incident-protocol.md`; current record `context-garden/docs/incidents/2026-09-06-web-responsiveness.md`. CG-357 merged and task done. Operator served benchmarks under caps passed (p95 .213s/ .570s at1546/6000 records with three executing local CPU/metadata workers); Windows browser journeys passed. Actual production Inbox, Board, Now1/Now2 all returned200 after installation and Windows browser navigation succeeded at19:00. WSL Now2 was .55s; Windows PowerShell localhost requests took2.5–2.8s (client-path overhead remains to distinguish). This is initial recovery, not incident closure.

Ordinary admission remains paused. One controlled CG-329 revision was dispatched through capped server at19:01 (HTTP303); verify actual PID/output. Observe three successful representative journey checks over at least ten minutes from19:00, including resumed workload, with no renewed pressure. If healthy at/after19:10, resume ordinary operation conservatively up to owner's3 workers/review1. If symptoms recur contain immediately. Do not duplicate CG-357 work or its old dispatches. Keep five-minute monitoring through observation and retrospective.

CG-294 preemption: worktree head f129ed553e6fcc7733be06d87628166ebbe0d454, dirty snapshot/transcript preserved; extra patch /home/joshua/work/operator-test-tmp/CG294-web-outage-recovery.patch. Four escaped tests stopped. Resume its preserved work after recovery. CG-337 needs later normal reconciliation. Frozen phase06 and PR221/222 remain held.

After verified recovery, run the owner-requested retrospective and file/link prevention tasks with counterfactuals and measurable criteria. Record task IDs and retro beside the incident before restoring ordinary25-minute follow-ups. Restoration/merged tasks do not establish unattended phase05 stabilization.
