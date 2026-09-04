---
id: CG-115
title: Store a short diff summary on run records for attention/triage evidence
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/inbox.py
- src/garden/web/templates/task.html
- src/garden/scheduler.py
branch: garden/cg-115-store-a-short-diff-summary-on-run-records-for-at
pr: https://github.com/joshmarcus/context-garden/pull/84
discovered_from: CG-045
attempts: 1
last_dispatched_at: '2026-09-04T23:20:30+00:00'
created: '2026-09-04T21:56:12+00:00'
updated: '2026-09-04T23:30:35+00:00'
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
- 2026-09-04T23:20:30+00:00 dispatched work run 20260904T232021Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~7681 tokens)
- 2026-09-04T23:28:24+00:00 opened https://github.com/joshmarcus/context-garden/pull/84 (base main): Run records now store a `diff_stat` (git diff --stat base...branch) computed once at finalize time in _after_push, and attention-card evidence lines plus triage-row 'why' text surface a compact diff summary reusing the existing (previously unused) gitops.diff_stat helper. cost=$4.37
- 2026-09-04T23:30:35+00:00 automated review: approve — Adds Run.diff_stat computed once at finalize in _after_push and surfaces it in attention-card evidence and triage rows, reusing the existing gitops.diff_stat helper; keeps build_inbox git-free. All acceptance criteria met and tested (3 new tests pass, ruff clean). cost=$0.48
