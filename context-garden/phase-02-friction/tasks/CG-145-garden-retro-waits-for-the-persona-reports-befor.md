---
id: CG-145
title: garden retro waits for the persona reports before it dispatches the reconciliation
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/retro.py
- src/garden/cli.py
- src/garden/scheduler.py
created: '2026-09-05T02:45:40+00:00'
updated: '2026-09-05T02:45:40+00:00'
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
- 2026-09-05T02:48:00+00:00 deferred by the feature freeze (2026-09-05): worked around with --skip-personas this time
