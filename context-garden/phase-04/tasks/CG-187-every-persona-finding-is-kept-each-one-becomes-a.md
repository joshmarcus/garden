---
id: CG-187
title: 'Every persona finding is kept: each one becomes a draft with its severity as priority, the retro
  reconciles all of them, and nothing below high is dropped'
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 1
difficulty: easy
reading:
- src/garden/personas.py
- src/garden/scheduler/persona.py
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/cli.py
branch: garden/cg-187-every-persona-finding-is-kept-each-one-becomes-a
pr: https://github.com/joshmarcus/context-garden/pull/136
attempts: 1
last_dispatched_at: '2026-09-05T11:51:00+00:00'
created: '2026-09-05T10:21:05+00:00'
updated: '2026-09-05T12:19:53+00:00'
---

## Goal

A persona review never throws a finding away. Every finding, at every severity, becomes a draft task in the phase the review names (the phase under review, or the next phase when the reviewed phase is frozen or closed), with the severity mapped to priority (high 1, medium 2, low 3), the persona and run in its provenance, and the finding's suggestion as its body. The retro reconciles all findings, not only the high ones, and its `duplicate_of` judgement collapses the same finding from several personas into one task.

## Context

The user on 2026-09-05, reading the product manager's phase-03 review: "We shouldn't arbitrarily only schedule two high items per review and toss away the rest." Today `garden persona-review --file-tasks` files only findings with `severity == "high"`; medium and low findings live in the report under `docs/reviews/` and nowhere else, so the planner sees them only if it reads that directory. The phase-02 retro reconciled 41 items but its persona inputs were the reports as prose, and the phase-03 product-manager review carried three medium and one low finding (live config reload, restart-safe reaps, placeholder acceptance criteria, three UI copy fixes) that no task captured. The reviewer chooses severity to rank, not to filter.

## Acceptance criteria

- [ ] `persona-review --file-tasks` and the retro file a draft for every finding, priority from severity, body from summary and suggestion, provenance `persona:<name>:<run>`; a frozen or closed reviewed phase sends them to the next phase.
- [ ] Findings that say the same thing across personas become one task: the reconciliation's `duplicate_of` (or a title match) merges them and the task body lists the personas that raised it.
- [ ] The retro document lists every finding with the task id it became, grouped by severity.
- [ ] `--file-tasks` gains `--min-severity` for a person who wants fewer drafts, defaulting to low.
- [ ] Tests with the fake harness for a review with one finding at each severity.

## Log

- 2026-09-05T10:31:15+00:00 approved (web)
- 2026-09-05T11:51:00+00:00 dispatched work run 20260905T115052Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-197-split-cli-py-into-a-cli-package-and-fold-the-fou stacked on CG-197, ~18641 tokens)
- 2026-09-05T11:55:55+00:00 parent CG-197 merged; will rebase onto main when the current run finishes
- 2026-09-05T12:10:33+00:00 parent CG-197 merged; rebased onto main and retargeted the PR
- 2026-09-05T12:12:13+00:00 opened https://github.com/joshmarcus/context-garden/pull/136 (base main): Every persona finding (not just high) now files as a draft task with priority from severity and persona:<name>:<run> provenance; a frozen/closed reviewed phase redirects to the next phase. The retro reconciles all findings across every persona that ran, merging same-titled ones into one task and listing every finding with its task id, grouped by severity, in the retro document. Added --min-severity to persona-review --file-tasks. cost=$4.71
- 2026-09-05T12:15:09+00:00 automated review: approve — Every persona finding now files as a draft with severity-priority in both the direct-dispatch and retro paths, cross-persona duplicates merge by title, and the retro doc lists findings grouped by severity; all five acceptance criteria are met with fake-harness tests, and the full suite and lint pass. cost=$0.99
- 2026-09-05T12:15:19+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T12:16:44+00:00 rebased; diff unchanged; verdict kept
- 2026-09-05T12:19:53+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/136
