# Context-garden operator handoff

Current handoff, consolidated 2026-09-06 19:14 UTC. Replace obsolete state here instead of appending contradictory updates. Verify live state before acting. Historical handoffs are archived in `context-garden/docs/operator-history/`; do not read them as current instructions.

## Start here

Read `.claude/skills/garden-operate/SKILL.md` for supported operator actions, then `context-garden/docs/incident-protocol.md` when basic operation is interrupted. `context-garden/docs/fast-forward.md` documents owner-invoked PR maintenance; it is currently inactive. This file owns current state; the manual supplies procedures. The garden is `/home/joshua/garden`; product worktrees are `/home/joshua/work/worktrees/CG-NNN`. Use the installed `.venv/bin/garden` for state-only actions. Never manually edit task status or race the scheduler's state writer.

## Owner authority and priorities

Josh delegates routine decisions, task approvals, direct fixes, PR merges and filing process gaps. Do not repeatedly ask him to interpret scheduler states. Preserve unfinished work and distinguish actual live processes from labels. No extra model review is required for operator self-reviewed repairs during fast-forward. Keep tests serial and resource-bounded. Do not launch additional agents without explicit authorization.

Phase 05 is stabilization/adoption, governed by `context-garden/phase-05/specs/stabilization.md`: four productive unattended hours, at least ten representative completed tasks, recovery exercises, real application journeys and named-project adoption evidence. Operator repairs are interventions, not unattended progress. Missing evidence is UNPROVEN. Phase 06 remains frozen; new feature requests belong there as drafts. Onboarding stays active. Both Now pages and the main Now CLI repair have merged; do not resurrect their old repair queue.

Workers must internally self-review, fix findings and recheck before completion. They report ordinary acceptance-criterion evidence, not a separate self-review report. This is included in `principles/00-index.md` and verified in generated briefs.

## Normal operation restored, 2026-09-06 17:40 UTC

Josh explicitly ended fast-forward and requested normal operation before the final eligible PR merged. Fast-forward is INACTIVE: its service drop-in was removed, existing garden-serve.service restarted with normal watch, and global dispatch resumed (HTTP 200). Do not re-enter maintenance merely because #223 remains open. The disposable UI fixture services were stopped.

PRs #232/CG-344, #229/CG-254 and #228/CG-296 merged and tasks are done. Josh merged #216/CG-215 at 545c745f6cc38087f4623a7a5726768e17856a02; reconciled done. #223/CG-324 subsequently merged at cf76e6ed1f671b5a9d5a6055ae8f3d1f127a07ae; normal scheduler reconciled it to done. All five eligible PRs are now merged. Frozen #221/#222 remain open and excluded.

The operator heartbeat returns to ordinary25-minute duties after incident closure and completed retrospective at19:14 UTC. Check status/inbox/digest and live resources, resolve actionable stalls with owner authority. Phase05 unattended stabilization remains unproven. CG-355 owns safe automatic updates; CG-356 owns rejected-onboarding recovery.

## Resource limits and services

Persistent garden service limits: CPUQuota=200%, CPUWeight=20, MemoryHigh=3G, MemoryMax=4G, MemorySwapMax=512M. Josh explicitly increased the live max_parallel override to 3 at 17:41 UTC; review_parallel remains 1. garden.yaml retains its conservative default of 1; the persisted live override governs dispatch. Retain CPU/memory caps and watch actual pressure. For routine restarts, verify no active workers or checks. During an incident use the deliberate preservation/restart procedure in `context-garden/docs/incident-protocol.md`; KillMode=process means detached work can survive.

CLI-spawned work bypasses service limits. During maintenance launch manual checks in a separate bounded systemd user service (2 GiB memory, 2 CPUs used for current fixes), with disk temp `/home/joshua/work/operator-test-tmp`. Normal future work should use capped server launch paths. CG-338 owns comprehensive resource admission.

`/tmp` is a 3 GiB tmpfs; `/home/joshua/work/tmp` links to `/tmp/garden-work`. The worker-temp service drop-in recreates that target. Never delete active-run temp. The timed two-minute resource monitor has ENDED; its JSONL is historical, not live monitoring. Inspect current /proc and service cgroup memory/events/load.

The host previously locked up: overlapping test suites, RAM-backed temp and a 102 MiB state file with duplicated manifests were measured contributors, not a proven final OOM cause. Preserve recovery data; do not clear state/manifests or caches blindly.

## Installed build

Installed pin8842552190ef675dd0af281ea23a82f15cdb1963 (CG-357 PR234) at18:59 UTC after current-head CI and merge. Existing service restarted with no active workers/checks, caps and admission pause preserved. New server PID2315784. This also includes earlier onboarding/evidence/UI repairs. No temporary runtime patches remain. No production history moved or deleted. Verify current state before further pin changes.

Read git log before pushing and commit only intended files. Codex operator spend remains unavailable until CG-336; never substitute Claude spend.

## Normal operation after web incident

Incident CLOSED at19:13 UTC after successful production checks at19:00,19:07,19:13, including genuine controlled revision/check work. Windows browser navigation succeeded; final dynamic pages were .46–.63s WSL and Now2 .645s WindowsIPv4. No new memory pressure or swap after recovery restart. Global resume returned200, owner3 worker slots/review1 and persistent caps retained. CG-357 is merged/installed/done; do not redispatch it. Monitor recurrence and use incident protocol if basic operation fails again.

Incident evidence: `context-garden/docs/incidents/2026-09-06-web-responsiveness.md`. Owner-required retrospective COMPLETE: `context-garden/docs/incidents/2026-09-06-web-responsiveness-retro.md`. New prevention tasks CG-358 (responsive retry-safe recovery controls, priority0) and CG-359 (provenance-safe dirty-file salvage, priority1); existing CG-338/339 strengthened, CG-331 clarified and CG-333 linked. Task creation does not establish implemented prevention. No production history moved/deleted; no temporary runtime experiment remains.

CG-294 preemption recovery remains: worktree head f129ed553e6fcc7733be06d87628166ebbe0d454, dirty snapshot/transcript preserved; extra patch /home/joshua/work/operator-test-tmp/CG294-web-outage-recovery.patch. It is ready to resume preserved work in normal priority order. Four escaped tests were stopped. CG-337 and CG-329 need normal current-state reconciliation; inspect their latest checks/reviews/PRs. Frozen phase06 and PR221/222 remain held.

19:43 operator check: web Now2 healthy1.13s with3 workers+1 review; VM available~5GiB, tmp29%, service near3GiB/high throttling but no OOM. CG-329/330 snapshot-only review blockers removed in8874a88/31b2db9 with backups under operator-test-tmp; both resumed in_review, new-head CI pending. CG-330 alleged broken main was exit127 missing .venv/bin/python on base probe, not executed failing tests; recorded environmental classification/coverage. CG-337, CG-358, CG-338 and CG-343 were active—verify fresh state.

20:13 operator update: CG-330 PR236 mergedc2df40a, task done, not yet installed while workers/checks active. CG-337 snapshot deletion repaired8e2afdb; resumed in_review with new CI. CG-329 is DRAFT safety-held until CG-338 admission/descendant ownership is verified; removing check/edit gates first would increase uncontrolled test concurrency. Preserve PR233. Operator retry raced automatic CG-338 revision201038 and cancelled it; PID20418 verified absent, ready restored, dirty edits backed up at /home/joshua/work/operator-test-tmp/CG338-retry-race-2013.patch. Preserve/reuse these edits; check live run before any further action, no duplicate dispatch. This is an operator intervention, not unattended progress. Web remained healthy .83s, no OOM.
