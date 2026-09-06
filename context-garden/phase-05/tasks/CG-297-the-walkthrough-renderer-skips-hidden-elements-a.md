---
id: CG-297
title: The walkthrough renderer skips hidden elements and attributes, and check runs retry once on a signal
  exit
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:19+00:00'
updated: '2026-09-06T00:55:56+00:00'
---

## Goal

Render the text capture with an HTML parser that drops hidden panels and never prints attribute values (a '->' in a title showed as 'tasks">Plan phase'). Separately, a pre-PR check that exits on SIGTERM under machine contention is rerun once before it counts as a failure, and the failure card carries the stack trace.

## Context

Carried into phase-05 from the phase-04 retro verdict.

## Acceptance criteria

- [ ] The walkthrough renderer parses captured HTML and drops elements hidden via `display:none`, `hidden`, or `aria-hidden`, so hidden panels never appear in the rendered text.
- [ ] The renderer outputs only element text content, never attribute values — a title attribute containing '->' must not leak into the rendered output.
- [ ] A renderer test exercises a page with a hidden panel and a title attribute containing '->', asserting neither appears in the rendered walkthrough.
- [ ] A pre-PR check process that exits on a signal (e.g. SIGTERM) is automatically retried once before it is recorded as a failure.
- [ ] If the retried check also fails, the resulting failure card includes the check's full stack trace.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-286 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:55:37+00:00 integrated 1 suggestion(s) (run 20260906T005027Z-edit) cost=$0.13
- 2026-09-06T00:55:56+00:00 approved (cli)
