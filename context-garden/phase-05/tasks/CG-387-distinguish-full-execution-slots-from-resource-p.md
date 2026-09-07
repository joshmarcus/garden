---
id: CG-387
title: Distinguish full execution slots from resource pressure in the status banner
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/resources.py
- src/garden/web/templates/base.html
created: '2026-09-07T15:39:48+00:00'
updated: '2026-09-07T15:39:49+00:00'
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
