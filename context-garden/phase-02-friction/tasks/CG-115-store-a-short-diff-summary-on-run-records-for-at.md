---
id: CG-115
title: Store a short diff summary on run records for attention/triage evidence
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/inbox.py
- src/garden/web/templates/task.html
- src/garden/scheduler.py
discovered_from: CG-045
created: '2026-09-04T21:56:12+00:00'
updated: '2026-09-04T22:03:22+00:00'
---

## Goal

Attention cards and triage rows should be able to show a real diff summary (files changed, +/- line counts, maybe the commit subjects) as evidence.

## Context

CG-045's acceptance criteria list 'the diff summary' among the evidence an attention card shows. Nothing in the garden stores one: computing it at render time would put git calls into `build_inbox`, which must stay cheap and offline. The natural place is the run record — the scheduler already has the worktree and base at finalize time, so it could write e.g. `diff_stat` (from `git diff --stat base...branch`) onto the Run when a work/revise run finishes, and `attention_view` / the triage card could render it for free.

## Provenance

Discovered by CG-045 (Attention cards say what the decision is and what each button will do) during run `20260904T214307Z-work`.

## Log

- 2026-09-04T21:56:12+00:00 discovered by CG-045
- 2026-09-04T22:03:22+00:00 approved
- 2026-09-04T22:03:22+00:00 priority 2 -> 3
