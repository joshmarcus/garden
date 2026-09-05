---
id: CG-169
title: 'garden qa: run on a schedule in CI with the scripted agent'
status: in_review
product: context-garden
phase: phase-03
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/app.py
- tests/fake_claude.py
- tests/conftest.py
branch: garden/cg-169-garden-qa-run-on-a-schedule-in-ci-with-the-scrip
pr: https://github.com/joshmarcus/context-garden/pull/122
discovered_from: CG-135
attempts: 1
last_dispatched_at: '2026-09-05T05:09:33+00:00'
created: '2026-09-05T04:17:48+00:00'
updated: '2026-09-05T05:27:29+00:00'
---

## Goal

Add a scheduled CI job (and a manual trigger) that runs `garden qa --scripted` and fails on a non-zero exit, so a page regression is caught between phases.

## Context

`garden qa --scripted` (CG-135) drives the nine flows in a few seconds with no tokens. The task said it runs in CI on a schedule; the workflow file is not part of that change.

## Provenance

Discovered by CG-135 (garden qa: an agent drives the loop end to end through the web app on a throwaway garden) during run `20260905T035723Z-work`.

## Log

- 2026-09-05T04:17:48+00:00 discovered by CG-135
- 2026-09-05T05:05:27+00:00 approved (web)
- 2026-09-05T05:09:33+00:00 dispatched work run 20260905T050924Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~7404 tokens)
- 2026-09-05T05:13:25+00:00 opened https://github.com/joshmarcus/context-garden/pull/122 (base main): Added .github/workflows/qa.yml with a daily schedule and workflow_dispatch trigger running `garden qa --scripted`, which fails CI on any broken flow; added one line to docs/architecture.md noting it alongside ci.yml. cost=$0.40
- 2026-09-05T05:27:29+00:00 automated review: approve — Adds a daily-scheduled + workflow_dispatch CI job running `garden qa --scripted`, matching ci.yml's environment and conventions; the command runs end to end (9/9 flows, exit 0) and fails the job on any broken flow. Minimal, correct, clean description. cost=$0.57
