# Context-garden operator handoff

Current handoff, consolidated 2026-09-06 ~17:14 UTC. Replace obsolete state here instead of appending contradictory updates. Verify live state before acting. Historical handoffs are archived in `context-garden/docs/operator-history/`; do not read them as current instructions.

## Start here

Read `.claude/skills/garden-operate/SKILL.md` for supported operator actions, then `context-garden/docs/fast-forward.md` for the active maintenance protocol and action ledger. This file owns current state; the manual supplies procedures. The garden is `/home/joshua/garden`; product worktrees are `/home/joshua/work/worktrees/CG-NNN`. Use the installed `.venv/bin/garden` for state-only actions. Never manually edit task status or race the scheduler's state writer.

## Owner authority and priorities

Josh delegates routine decisions, task approvals, direct fixes, PR merges and filing process gaps. Do not repeatedly ask him to interpret scheduler states. Preserve unfinished work and distinguish actual live processes from labels. No extra model review is required for operator self-reviewed repairs during fast-forward. Keep tests serial and resource-bounded. Do not launch additional agents without explicit authorization.

Phase 05 is stabilization/adoption, governed by `context-garden/phase-05/specs/stabilization.md`: four productive unattended hours, at least ten representative completed tasks, recovery exercises, real application journeys and named-project adoption evidence. Operator repairs are interventions, not unattended progress. Missing evidence is UNPROVEN. Phase 06 remains frozen; new feature requests belong there as drafts. Onboarding stays active. Both Now pages and the main Now CLI repair have merged; do not resurrect their old repair queue.

Workers must internally self-review, fix findings and recheck before completion. They report ordinary acceptance-criterion evidence, not a separate self-review report. This is included in `principles/00-index.md` and verified in generated briefs.

## Normal operation restored, 2026-09-06 17:40 UTC

Josh explicitly ended fast-forward and requested normal operation before the final eligible PR merged. Fast-forward is INACTIVE: its service drop-in was removed, existing garden-serve.service restarted with normal watch, and global dispatch resumed (HTTP 200). Do not re-enter maintenance merely because #223 remains open. The disposable UI fixture services were stopped.

PRs #232/CG-344, #229/CG-254 and #228/CG-296 merged and tasks are done. Josh merged #216/CG-215 at 545c745f6cc38087f4623a7a5726768e17856a02; reconciled done. #223/CG-324 subsequently merged at cf76e6ed1f671b5a9d5a6055ae8f3d1f127a07ae; normal scheduler reconciled it to done. All five eligible PRs are now merged. Frozen #221/#222 remain open and excluded.

The operator heartbeat checks every five minutes until 18:41 UTC after the owner increased concurrency, then returns to ordinary 25-minute duties: status/inbox/digest and live resource checks, act on actionable stalls with owner authority. Continue stabilization work with three worker slots, one review and caps; no unattended stabilization claim follows from supervised repairs. CG-355 tracks automatic update/restart regression; CG-356 tracks onboarding rejected-plan recovery.

## Resource limits and services

Persistent garden service limits: CPUQuota=200%, CPUWeight=20, MemoryHigh=3G, MemoryMax=4G, MemorySwapMax=512M. Josh explicitly increased the live max_parallel override to 3 at 17:41 UTC; review_parallel remains 1. garden.yaml retains its conservative default of 1; the persisted live override governs dispatch. Retain CPU/memory caps and watch actual pressure. Restart only after verifying no active workers or checks; KillMode=process means detached work can survive.

CLI-spawned work bypasses service limits. During maintenance launch manual checks in a separate bounded systemd user service (2 GiB memory, 2 CPUs used for current fixes), with disk temp `/home/joshua/work/operator-test-tmp`. Normal future work should use capped server launch paths. CG-338 owns comprehensive resource admission.

`/tmp` is a 3 GiB tmpfs; `/home/joshua/work/tmp` links to `/tmp/garden-work`. The worker-temp service drop-in recreates that target. Never delete active-run temp. The timed two-minute resource monitor has ENDED; its JSONL is historical, not live monitoring. Inspect current /proc and service cgroup memory/events/load.

The host previously locked up: overlapping test suites, RAM-backed temp and a 102 MiB state file with duplicated manifests were measured contributors, not a proven final OOM cause. Preserve recovery data; do not clear state/manifests or caches blindly.

## Installed build

Installed pin is 14676f50bf6e68fb0c5111c7c8a0c96d66cfc8aa as of 2026-09-06 17:40 UTC (verified main CI). It includes memory/lifecycle/operating UI repairs; onboarding's merge had main CI in progress at install time and is not yet installed. Existing server runs normal watch; /, /now1 and /now2 returned HTTP 200 after restart, and global resume returned 200. Verify current state before future pin movement; only install/restart when workers/checks drain. Retain caps and phase holds. Global resume is POST http://127.0.0.1:8765/resume with matching loopback Origin; CLI resume requires a task id.

Read git log before pushing and commit only intended files. Codex operator spend remains unavailable until CG-336; never substitute Claude spend.

## Active web responsiveness incident, 17:43–17:49 UTC

Owner reported web timeouts. Service alive; static requests fast, dynamic pages repeatedly scan roughly 1,546 run records in concurrent threads (py-spy verified). CG-357 is priority 0, ready, covering bounded read models and safe archival. No history moved/deleted. A process-local Run.load parse cache experiment at /home/joshua/work/operator-test-tmp/web-run-read-mitigation.py was applied to PID 1440205 using Python remote_exec without restart; it did NOT restore reliable access and must not be called a fix. It disappears at restart; record removal/supersession. No scan-method experiment was applied. Keep active work intact and investigate before restarting.
