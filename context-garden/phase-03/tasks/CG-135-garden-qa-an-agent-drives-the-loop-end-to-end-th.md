---
id: CG-135
title: 'garden qa: an agent drives the loop end to end through the web app on a throwaway garden'
status: ready
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 2
difficulty: hard
reading:
- src/garden/web/app.py
- tests/fake_claude.py
- tests/conftest.py
created: '2026-09-05T00:37:32+00:00'
updated: '2026-09-05T03:19:57+00:00'
---

## Goal

`garden qa` starts a throwaway garden with the fake harness (as the tests do), serves the web app, and lets an agent drive the loop end to end through the HTTP surface: add a task, approve, dispatch, answer a worker's question, send back with a note, triage, accept a nothing-to-change card, merge, close a phase. It reports what broke or confused it as friction reports, each with the page it saw, and exits non-zero when a flow cannot be completed.

## Context

Asked at the freeze of the first live run, as the interactive half of the QA walkthrough. The walkthrough (CG-134) shows the pages; this exercises them. The agent gets the walkthrough's index as its script and the fake harness so nothing costs tokens beyond the agent itself. Runs in CI on a schedule or by hand before a phase closes. Findings arrive as friction reports on the phase, with the page HTML attached in the run directory, so the retro can read them.

## Acceptance criteria

- [ ] `garden qa` completes the flows above on a fresh throwaway garden and prints a summary; a broken flow makes it exit non-zero with the failing step named.
- [ ] each finding is a friction report with the page it was seen on.
- [ ] a test runs the command against the demo garden with a scripted fake agent.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)
- 2026-09-05T00:40:00+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03
- 2026-09-05T03:01:13+00:00 approved (web)
- 2026-09-05T03:05:55+00:00 back to draft: approved by mistake during the phase 02 freeze; carried into phase 03
- 2026-09-05T03:19:57+00:00 approved (web)
