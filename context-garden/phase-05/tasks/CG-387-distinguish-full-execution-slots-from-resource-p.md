---
id: CG-387
title: Distinguish full execution slots from resource pressure in the status banner
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/resources.py
- src/garden/web/templates/base.html
branch: garden/cg-387-distinguish-full-execution-slots-from-resource-p
pr: https://github.com/joshmarcus/context-garden/pull/298
attempts: 1
last_dispatched_at: '2026-09-08T09:50:58+00:00'
created: '2026-09-07T15:39:48+00:00'
updated: '2026-09-08T10:50:59+00:00'
---

## Goal

Show normal full concurrency as busy capacity, with a precise explanation when actual memory/temp/pressure gates prevent admission.

## Evidence

Owner reported the Inbox said the loop was stuck after normal operation resumed. At2026-09-07T15:38Z all five shared slots had live processes, but the banner said Resource pressure: local execution limit reached (5/5). Active work is draining; pause dispatch or wait for headroom, then retry. Ordinary dispatch was enabled; memory PSI and high/max/OOM counters were zero. No drain was requested. The wording falsely implies an incident and asks for unnecessary operator action. Effective controller headroom was1550MiB near the1536MiB reserve, so actual memory gates must remain independently visible if they engage.

## Acceptance criteria

- [ ] Full shared slots alone render neutral busy/at-capacity wording with live occupancy and explain that eligible work waits for a slot; do not claim resource pressure, draining, pause required or manual retry required solely from normal occupancy.
- [ ] Actual memory/temp/pressure/isolation failures remain accurately identified, including concurrent limiting conditions. Do not alter admission decisions, lower reserves or hide real pressure merely because slots are also full.
- [ ] Exercise rendered Inbox/Config status with full-but-healthy, available-slot, real low-headroom and mixed conditions; verify automatic admission remains enabled for normal full capacity. Record actual affected-page evidence with proportional focused checks and exact-head CI.

## Scope

Keep this presentation/classification fix separate from CG385's active bounded cache-reclaim implementation. One initial Inbox response was6.053s during new activity; subsequent Inbox/Now/Inbox measurements were2.235/2.103/2.125s, within the owner four-second tolerance. Do not claim a sustained latency incident from that isolated response.

## Log

- 2026-09-07T18:39:00+00:00 dispatched work run 20260907T183858Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~10499 tokens)
- 2026-09-07T19:03:32+00:00 preserved uncommitted worktree changes from run 20260907T183858Z-work outside the PR: `git stash apply a36d9aef0fb36f6bffb7c5318c0110faa48b4467` in /home/joshua/work/worktrees/CG-387 (garden:CG-387:20260907T183858Z-work:reap)
- 2026-09-07T19:51:34+00:00 opened https://github.com/joshmarcus/context-garden/pull/298 (base main): Normal full local execution capacity now renders as neutral busy occupancy, while memory, temporary-storage, and cgroup pressure remain distinct alerts. Added rendered-state coverage and Inbox/Config light/dark desktop/narrow captures. cost=$2.06
- 2026-09-07T20:00:46+00:00 automated review requested changes: The classification change is correct and tested, but criterion 3 lacks the required served affected-state interaction and scalability evidence. The exact-head replay exercises unrelated task lifecycle actions and records no capacity/pressure journey or load measurements. cost=$0.55
- 2026-09-08T09:50:58+00:00 dispatched revise run 20260908T095056Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11632 tokens)
- 2026-09-08T10:01:29+00:00 preserved uncommitted worktree changes from run 20260908T095056Z-revise outside the PR: `git stash apply a3165baf428a7334cfe9b085de42119f43840ac5` in /home/joshua/work/worktrees/CG-387 (garden:CG-387:20260908T095056Z-revise:reap)
- 2026-09-08T10:02:44+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/298: Recorded a disposable served-app replay that explicitly covers healthy availability, neutral full capacity, low headroom, mixed capacity plus pressure, recovery, and the requested scalability measurements. Exact-head CI passed for a2475001e0ef9649804ded8b616ad95cfad9e780. cost=$0.64
- 2026-09-08T10:12:21+00:00 stalled: review finding repeated after a revise round: acceptance criterion lacks a passing, evidenced assessment: exercise rendered in; run `garden triage CG-387 --changes "<feedback>" to unblock`
- 2026-09-08T10:50:59+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/298
