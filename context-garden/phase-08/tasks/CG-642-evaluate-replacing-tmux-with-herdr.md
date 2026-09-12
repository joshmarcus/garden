---
id: CG-642
title: Evaluate replacing tmux with Herdr
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 3
difficulty: medium
reading:
- context-garden/specs/system-architecture.md
- src/garden/runner/ssh.py
- docs/worker-protocol.md
discovered_from: 'owner: Add a backlog item to evaluate swapping mix for herdr'
created: '2026-09-12T17:39:36+00:00'
updated: '2026-09-12T17:39:36+00:00'
---

## Goal

Evaluate whether Herdr would be a worthwhile replacement for the tmux layer used by Garden's durable SSH execution. Produce a recommendation before any implementation commitment.

## Context and scope

Owner requested a backlog item to evaluate swapping "mix" for Herdr; interpreted as tmux in the current worker-session context. The current SSH implementation uses durable tmux sessions and retained completion evidence. The previous broad Herdr direction was withdrawn and removed from active discovery. This is a new, bounded evaluation of replacing the session layer, not approval to restore the old implementation plan or change a running worker.

## Acceptance criteria

- [ ] Compare the current tmux-based SSH session contract with Herdr's supported capabilities using current primary documentation and source. Cover detached execution, reconnect and lost acknowledgements, cancellation, result/log retention, credential isolation and platform requirements. Distinguish documented capabilities from observations and assumptions.
- [ ] Assess whether Garden can retain ownership of scheduling, claims, workspaces, source publication, review and completion while substituting Herdr for tmux. Identify integration complexity, operational dependencies, failure modes, migration/reversal costs and any concrete benefit over keeping tmux.
- [ ] Recommend keeping tmux, conducting a narrowly scoped prototype, or pursuing a replacement, with clear reasons and unresolved questions. A no-change recommendation is a valid outcome. If a prototype is warranted, describe its smallest useful scope and success criteria without launching it or creating implementation tasks automatically.

## Backlog disposition

Keep this item DRAFT in frozen Phase08. The owner asked to add an evaluation item, not run the evaluation now. Do not automatically approve or dispatch it under routine operator authority. Do not reopen Phase09 or restore withdrawn CG602-CG615. Existing multiplayer implementation, worker deadlines, budgets and unrelated holds remain in effect. Evaluation approval would not itself authorize production changes, new resources or a Herdr rollout.
