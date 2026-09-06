# Context-garden operator handoff

Current handoff, consolidated 2026-09-06 ~17:14 UTC. Replace obsolete state here instead of appending contradictory updates. Verify live state before acting. Historical handoffs are archived in `context-garden/docs/operator-history/`; do not read them as current instructions.

## Start here

Read `.claude/skills/garden-operate/SKILL.md` for supported operator actions, then `context-garden/docs/fast-forward.md` for the active maintenance protocol and action ledger. This file owns current state; the manual supplies procedures. The garden is `/home/joshua/garden`; product worktrees are `/home/joshua/work/worktrees/CG-NNN`. Use the installed `.venv/bin/garden` for state-only actions. Never manually edit task status or race the scheduler's state writer.

## Owner authority and priorities

Josh delegates routine decisions, task approvals, direct fixes, PR merges and filing process gaps. Do not repeatedly ask him to interpret scheduler states. Preserve unfinished work and distinguish actual live processes from labels. No extra model review is required for operator self-reviewed repairs during fast-forward. Keep tests serial and resource-bounded. Do not launch additional agents without explicit authorization.

Phase 05 is stabilization/adoption, governed by `context-garden/phase-05/specs/stabilization.md`: four productive unattended hours, at least ten representative completed tasks, recovery exercises, real application journeys and named-project adoption evidence. Operator repairs are interventions, not unattended progress. Missing evidence is UNPROVEN. Phase 06 remains frozen; new feature requests belong there as drafts. Onboarding stays active. Both Now pages and the main Now CLI repair have merged; do not resurrect their old repair queue.

Workers must internally self-review, fix findings and recheck before completion. They report ordinary acceptance-criterion evidence, not a separate self-review report. This is included in `principles/00-index.md` and verified in generated briefs.

## Active operation: finish the eligible PRs

Fast-forward is ACTIVE. The existing `garden-serve.service` serves the UI with `serve --no-watch`, via `~/.config/systemd/user/garden-serve.service.d/fast-forward.conf`. Dispatch is also paused. Do not tick, dispatch, launch automated reviews, globally resume or start another server while maintenance is active. Ordinary pause alone does not suppress all work in this installed build.

Owner scope: leave frozen #221 (CG-216 remote workers) and #222 (CG-230 model pools) OPEN. Finish the other eligible PRs, reconcile their task states and exit through the fast-forward protocol.

- #232 / CG-344 memory-bounded fence bookkeeping: MERGED at bda4911f5a9854212298294ef957813f5b1c016d; task done. Direct integrity/recovery repair, 182 targeted tests, lint and full CI passed. Installed in d5825a3.
- #229 / CG-254 lifecycle commands: MERGED at d5825a3feb93f2ea1869ae09753eb3cb944ba4a6 after 64 targeted tests, lint and full CI passed. Task reconciled to done; Installed in d5825a3.
- #228 / CG-296 operating controls/Inbox: worktree refreshed with main in 0e00a06. Uncommitted fixes address duplicated taskless questions, feed wording, repeated rail spend and the Costs fallback button. Needs tests, disposable-app journeys/captures, current main after #229, push and CI. Original dirty generated snapshot preserved at `/home/joshua/work/operator-test-tmp/CG296-snapshot-recovery.patch`; base snapshot restored.
- #223 / CG-324 required evidence: still open; inspect latest findings, including failed persona runs stranding review.
- #216 / CG-215 onboarding: still open and explicitly authorized to land; inspect convention derivation and provenance findings. Do not reinstate the old hold.

The existing Codex heartbeat `operate-context-garden` runs every five minutes to continue direct PR resolution. A timer is a reminder, not evidence that work is happening: perform repairs instead of ending after status narration. When these three remaining PRs are handled, follow the safe exit, update this handoff, and restore ordinary 25-minute duties. Notify only meaningful changes.

## Resource limits and services

Persistent garden service limits: CPUQuota=200%, CPUWeight=20, MemoryHigh=3G, MemoryMax=4G, MemorySwapMax=512M. max_parallel=1 and review_parallel=1. Do not restore historical limits of 2, 3 or 5 without new evidence/authority. Restart only after verifying no active workers or checks; KillMode=process means detached work can survive.

CLI-spawned work bypasses service limits. During maintenance launch manual checks in a separate bounded systemd user service (2 GiB memory, 2 CPUs used for current fixes), with disk temp `/home/joshua/work/operator-test-tmp`. Normal future work should use capped server launch paths. CG-338 owns comprehensive resource admission.

`/tmp` is a 3 GiB tmpfs; `/home/joshua/work/tmp` links to `/tmp/garden-work`. The worker-temp service drop-in recreates that target. Never delete active-run temp. The timed two-minute resource monitor has ENDED; its JSONL is historical, not live monitoring. Inspect current /proc and service cgroup memory/events/load.

The host previously locked up: overlapping test suites, RAM-backed temp and a 102 MiB state file with duplicated manifests were measured contributors, not a proven final OOM cause. Preserve recovery data; do not clear state/manifests or caches blindly.

## Installed build and safe exit

Installed pin is d5825a3feb93f2ea1869ae09753eb3cb944ba4a6 as of 2026-09-06 17:16 UTC; Now 1 and Now 2 routes both verified HTTP 200 and Now 1 viewed in browser. Maintenance remains serve --no-watch with caps and pause preserved. Verify before changing the pin. After eligible PRs land and all work drains, install a verified merged build per the manual, preserving the resource settings. Remove only fast-forward.conf, daemon-reload/restart the existing service, verify health and then resume globally with POST http://127.0.0.1:8765/resume and a matching loopback Origin header. `garden resume` requires a task id and is not global resume. Do not exit into a known critical resource/main failure.

Read git log before pushing. Avoid garden-repo commits while Claude/Fable workers are active until the relevant fence fix is installed. Commit only intended files; existing task/log changes may belong to the scheduler. Codex operator spend remains unavailable until CG-336; never substitute Claude spend.
