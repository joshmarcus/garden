---
id: CG-297
title: The walkthrough renderer skips hidden elements and attributes, and check runs retry once on a signal
  exit
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:19+00:00'
updated: '2026-09-06T00:50:26+00:00'
---

## Goal

Render the text capture with an HTML parser that drops hidden panels and never prints attribute values (a '->' in a title showed as 'tasks">Plan phase'). Separately, a pre-PR check that exits on SIGTERM under machine contention is rerun once before it counts as a failure, and the failure card carries the stack trace.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Suggestions

- [ ] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-286 (renumbered by the operator: two reconcile runs drew ids from one counter)
