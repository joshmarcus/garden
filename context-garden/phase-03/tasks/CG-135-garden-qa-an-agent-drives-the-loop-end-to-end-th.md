---
id: CG-135
title: 'garden qa: an agent drives the loop end to end through the web app on a throwaway garden'
status: in_review
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
branch: garden/cg-135-garden-qa-an-agent-drives-the-loop-end-to-end-th
pr: https://github.com/joshmarcus/context-garden/pull/107
attempts: 1
last_dispatched_at: '2026-09-05T04:20:04+00:00'
created: '2026-09-05T00:37:32+00:00'
updated: '2026-09-05T04:31:21+00:00'
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
- 2026-09-05T03:57:33+00:00 dispatched work run 20260905T035723Z-work via local [claude model=claude-fable-5-1] (fresh session, base main, ~7673 tokens)
- 2026-09-05T04:17:48+00:00 discovered work filed: CG-169
- 2026-09-05T04:18:59+00:00 opened https://github.com/joshmarcus/context-garden/pull/107 (base main): garden qa builds and serves a throwaway garden with fake workers and a pretend GitHub, has a scripted or harness-driven agent complete nine flows through the web app, files findings as friction reports with the page HTML, and exits non-zero naming a failed step. Adds a close-phase route and a stand-in GitHub hook on the web hub. cost=$10.34
- 2026-09-05T04:19:48+00:00 PR conflicts with main (tests/fake_claude.py); revise run will rebase and resolve
- 2026-09-05T04:20:04+00:00 dispatched revise run 20260905T042003Z-revise via local [claude model=claude-fable-5-1] (fresh session, base main, ~12797 tokens)
- 2026-09-05T04:26:48+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/107: Rebased onto origin/main, resolved the tests/fake_claude.py conflict keeping CG-152's in-process shape plus the qa mode, and restored the real local runner for the garden qa tests since the in-process runner has no fake for the QA sandbox's own worker. Full suite and lint pass. cost=$2.05
- 2026-09-05T04:31:21+00:00 automated review: approve — garden qa builds a throwaway garden, serves the web app against a pretend GitHub, and drives nine end-to-end flows; all three acceptance criteria are met with a scripted and a harness-driven test, the full suite and lint pass, and the description is clean. cost=$1.55
