---
id: CG-179
title: Results and reviews speak to each acceptance criterion by name, with evidence
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: medium
reading: []
created: '2026-09-05T09:41:59+00:00'
updated: '2026-09-05T09:41:59+00:00'
---

## Goal

A worker's result and a reviewer's verdict both speak to each acceptance criterion by name, with the evidence: the test that proves it, the command and its output, or the page and what it shows. A criterion with no evidence is a finding, not a pass.

## Context

Asked by the user on 2026-09-05 after phase 03: "should we have asked the tasks for verification that they're complete?" Today the criteria are prose checkboxes in the task file that nobody ticks; the result has a free-text summary and the PR body a Verification paragraph; the reviewer reads the criteria against the diff and usually checks them (the split's reviewer counted methods), but the verdict has no per-criterion field, so a skipped bullet depends on the reviewer noticing. First-pass approval in phase 03 was 93%, so this is about the remaining 7% and about making the check visible.

## Acceptance criteria

- [ ] The worker brief asks for `verified` in `GARDEN_RESULT`: one entry per acceptance criterion with `evidence` (test name, command and output, or page and observation) or `not_done` with a reason.
- [ ] The review brief asks for `criteria` in `GARDEN_REVIEW`: one entry per criterion with `met` true/false and a one-line reason; a criterion the worker marked `not_done` without a reason accepted by the reviewer is a blocking finding.
- [ ] The task page shows the criteria with the worker's evidence and the reviewer's verdict beside each; the PR body's Verification section is generated from the same list.
- [ ] `garden metrics` reports criteria met on the first review per tier.
- [ ] Tests with the fake harness for a result that skips a criterion.

