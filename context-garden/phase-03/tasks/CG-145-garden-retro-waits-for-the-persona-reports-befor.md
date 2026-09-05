---
id: CG-145
title: garden retro waits for the persona reports before it dispatches the reconciliation
status: running
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 1
difficulty: easy
reading:
- src/garden/retro.py
- src/garden/cli.py
- src/garden/scheduler.py
branch: garden/cg-145-garden-retro-waits-for-the-persona-reports-befor
attempts: 2
last_dispatched_at: '2026-09-05T03:37:32+00:00'
created: '2026-09-05T02:45:40+00:00'
updated: '2026-09-05T03:42:07+00:00'
---

## Goal

`garden retro` dispatches the reconciliation only when every persona report it asked for is on disk (or `--skip-personas` was given and the reports exist). Until then the retro is "waiting for personas: 3 of 6 done" on the phase page and in `garden status`, and the reconciliation's brief always carries the reports.

## Context

Found on the first use, the phase-02 retro on 2026-09-05. The command dispatched six persona runs one after another (02:40 to 02:44) and the reconciliation at 02:41:33, when no report existed; the reconciliation's brief had an empty "Persona reviews" section, so its document could only reconcile the harvested friction against the task list and had nothing from the personas. The person re-ran the reconciliation with `--skip-personas` after the reports landed. Make the reconciliation a pending step in state (`_retro:<phase>` with the expected persona list); the tick dispatches it when the reports are all present, and the phase page shows the count. `--dry-run` says the same.

## Acceptance criteria

- [ ] with six personas requested, the reconciliation does not start until six reports exist; a test with the fake harness.
- [ ] the reconciliation brief's "Persona reviews" section is never empty when personas were requested.
- [ ] `garden status` and the phase page show "retro: waiting for personas (n of m)" while it waits.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)
- 2026-09-05T02:48:00+00:00 deferred by the feature freeze (2026-09-05): worked around with --skip-personas this time
- 2026-09-05T03:01:37+00:00 approved (web)
- 2026-09-05T03:02:13+00:00 dispatched work run 20260905T030204Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~3093 tokens)
- 2026-09-05T03:05:29+00:00 back to draft: approved by mistake during the phase 02 freeze; phase 03 work (CG-137 runs alone, first)
- 2026-09-05T03:19:58+00:00 approved (web)
- 2026-09-05T03:37:32+00:00 dispatched work run 20260905T033731Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-137-split-the-scheduler-by-tick-phase-and-the-web-ac stacked on CG-137, ~6307 tokens)
- 2026-09-05T03:42:07+00:00 parent CG-137 merged; will rebase onto main when the current run finishes
