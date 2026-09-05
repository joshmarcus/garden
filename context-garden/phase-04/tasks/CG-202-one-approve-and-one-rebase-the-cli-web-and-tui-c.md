---
id: CG-202
title: 'One approve and one rebase: the CLI, web and TUI call the same approve gate, and the sync-rebase-force-push
  sequence lives in one place'
status: running
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 1
difficulty: medium
reading: []
branch: garden/cg-202-one-approve-and-one-rebase-the-cli-web-and-tui-c
attempts: 1
last_dispatched_at: '2026-09-05T11:51:18+00:00'
created: '2026-09-05T10:30:01+00:00'
updated: '2026-09-05T11:55:55+00:00'
---

## Goal

Approve is written five times across CLI, web and TUI; the TUI copy has no `phase_refusal` check and the web copy differs in what it logs. The sync-rebase-force-push sequence is implemented four times and only `mechanical_rebase` and `_reprobe_base_broken` share the verdict-keep logic. `merge_head`, `automerge_candidate`, `automerge_ready_at` and `automerge_blocked` are written from seven places.

## Provenance

From the phase-03 persona reviews of 2026-09-05 (staff-engineer:high, staff-engineer:high, staff-engineer:medium); filed by the operator so that every finding is kept (see CG-187). Reports: `context-garden/phase-03/docs/reviews/`.

## Acceptance criteria

- [ ] A single `Scheduler.approve(task, by, phase=None)` with the freeze and validation gates, called by all three surfaces; the TUI refuses a frozen phase like the others.
- [ ] A single `gitops.sync_and_rebase(worktree, branch, base)` used by the rebase mixin, the restack, the base probe and the queue.
- [ ] Queue state is written through one helper; a test asserts no other writer.

## Log

- 2026-09-05T10:31:19+00:00 approved (web)
- 2026-09-05T11:51:18+00:00 dispatched work run 20260905T115109Z-work via local [claude model=claude-opus-4-8] (fresh session, base garden/cg-197-split-cli-py-into-a-cli-package-and-fold-the-fou stacked on CG-197, ~4611 tokens)
- 2026-09-05T11:55:55+00:00 parent CG-197 merged; will rebase onto main when the current run finishes
