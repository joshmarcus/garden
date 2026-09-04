---
id: CG-068
title: 'Automerge: merge a PR when the loop''s own gates pass'
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/github.py
- src/garden/config.py
created: '2026-09-04T18:39:35+00:00'
updated: '2026-09-04T18:41:38+00:00'
---

## Goal

A configuration option, off by default, that lets the scheduler merge a task's PR itself once every gate the loop already has is green, so a phase can run to `done` without a person clicking merge.

## Context

Asked during the first live run as "yolo mode". Today the merge is the one step reserved for a person; with PRs now opened ready for review (`github.draft_pr: false`) and bot reviews counting as feedback, the loop has enough signal to decide on its own for low-risk work. The gates, all of which exist: the automated review's last verdict is `approve`; no feedback is pending and no revise run is in flight; the pre-PR checks passed on the head; the PR's checks rollup is green; GitHub reports it `MERGEABLE`; no human review on the PR requests changes; the phase is under budget. When all hold, call the merge (`gh pr merge --squash --delete-branch`, or the REST merge endpoint), log it with the verdict and run ids, and let the existing poll move the task to `done` and restack children.

Config, under `github:`: `automerge: false` (the switch), `automerge_method: squash`, `automerge_min_review_rounds: 1`, and `automerge_tiers: [easy, medium]` so hard tasks still wait for a person. A task-level `automerge: false` opts a single task out. Per-product override like the other github keys. The Inbox shows "merged by the garden" on the task and the digest counts them, so a person can audit a day's merges after the fact. When a gate fails, nothing changes: the task stays in `in_review` for a person, with the failing gate on the task page.

## Acceptance criteria

- [ ] with `github.automerge: true`, a PR whose gates all pass is merged by the scheduler and the task reaches `done` through the poll.
- [ ] any single failing gate (pending feedback, red CI, `CONFLICTING`, a human's changes-requested review, tier not allowed, over budget) leaves the PR unmerged with the reason on the task page.
- [ ] the switch is off by default; README documents the keys and the gates.
- [ ] tests with the fake GitHub for the merge and for each gate.

## Out of scope

- Merging PRs the garden did not open; PRs opened by hand stay with the person.

## Log

- 2026-09-04T18:41:38+00:00 approved
