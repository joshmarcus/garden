---
id: CG-273
title: CG-217 merged with a criterion marked 'no evidence given' and CG-158 with a plac
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
harness: codex
discovered_from: persona:project-manager:context-garden/phase-04
created: '2026-09-05T23:58:14+00:00'
updated: '2026-09-06T03:51:39+00:00'
---

## Goal

Turn a reviewer met:false or missing evidence on any criterion into a mechanical changes_requested, or restate the goal as advisory.

## Context

Raised by the project-manager persona review (acceptance criteria). persona:project-manager:context-garden/phase-04. 50Z).

## Acceptance criteria

- [ ] A review where any criterion has `met: false` produces a `changes_requested` verdict, even when other criteria pass.
- [ ] A review where a criterion is missing an `evidence` field is treated the same as `met: false` and forces `changes_requested`.
- [ ] The mechanical rule is documented where reviewers/consumers read verdict logic, so the behavior isn't left to interpretation.
- [ ] A test exercises a review with one unmet or evidence-less criterion and asserts the verdict is `changes_requested`.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.
- [x] A criterion marked met without evidence the reviewer can point to (a test name, a page, a command and its output) is a mechanical request_changes naming the criterion (owner, 2026-09-06 03:50Z).

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-262 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:51:50+00:00 integrated 1 suggestion(s) (run 20260906T005020Z-edit) cost=$0.07
- 2026-09-06T00:52:22+00:00 approved (cli)
- 2026-09-06T03:51:39+00:00 integrated 1 suggestion(s) (run 20260906T035012Z-edit) cost=$0.03
