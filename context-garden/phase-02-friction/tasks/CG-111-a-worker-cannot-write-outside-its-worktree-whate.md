---
id: CG-111
title: A worker cannot write outside its worktree, whatever it is told
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/harness.py
- src/garden/runner/local.py
- src/garden/scheduler.py
- docs/worker-protocol.md
branch: garden/cg-111-a-worker-cannot-write-outside-its-worktree-whate
pr: https://github.com/joshmarcus/context-garden/pull/57
attempts: 1
last_dispatched_at: '2026-09-04T22:03:05+00:00'
created: '2026-09-04T21:28:15+00:00'
updated: '2026-09-04T22:03:05+00:00'
---

## Goal

A worker's writes are confined to its own worktree by the runner, not by the brief. Nothing a person types into an answer, and nothing a worker reads, lets it edit or commit in the live garden, the product clone, or another task's worktree.

## Context

On the first live run, CG-092's worker was asked a question, the person answered "Try to make the fix yourself", and the resumed worker changed directory to the live garden (`/home/joshua/garden`), edited `garden.yaml` and `product.md` there, and committed on `main` under the person's git identity. The garden's next push carried the commit to GitHub. The change removed the product's pre-PR checks in favour of a `setup` block the running scheduler does not know, so the next restart would have run with no gate. CG-054 and CG-058 keep the brief and `garden` commands away from the garden; this is the remaining hole. The brief never named the garden: the worker's first run found it by listing the filesystem (`/home/joshua/garden/.garden` turned up in a directory sweep). The harness runs with `--permission-mode acceptEdits`, which accepted `Edit` calls on files outside the worktree without a prompt, and its `Bash` calls (`cd /home/joshua/garden && git commit ...`) ran unchallenged. Choose the fence and implement it: run the harness with a permission mode that auto-accepts edits inside the worktree and denies them outside (in `-p` mode a prompt cannot be answered, so a denied edit fails, which is what we want); and, as belt and braces, have `finalize` check the garden repo and the product clone for changes or new commits since dispatch, revert them, and mark the run failed with a card that quotes what was touched. Say in `docs/worker-protocol.md` that the fence is the runner's, and that a person's answer cannot lift it.

## Acceptance criteria

- [ ] a fake-harness run that writes outside its worktree fails, the write is undone, and the Inbox says what it touched.
- [ ] edits and shell commands outside the worktree are denied (permission rules scoped to the worktree, or a sandbox); edits inside it still need no prompt.
- [ ] `docs/worker-protocol.md` states the fence.

## Log

- 2026-09-04T21:34:07+00:00 dispatched work run 20260904T213406Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~10351 tokens)
- 2026-09-04T21:57:15+00:00 opened https://github.com/joshmarcus/context-garden/pull/57 (base main): Confined a worker's writes to its own worktree at the runner, not the brief: the claude harness now passes permissions.deny rules (and an opt-in worktree sandbox) for the live garden and product clone, and finalize snapshots those repos at dispatch and reverts any commit or non-owned write on reap, failing the run with an Inbox card that quotes what was touched. Scheduler-owned task-file/.garden changes (e.g. garden sync) are ignored so they don't false-trip. Documented the fence in worker-protocol.md. cost=$8.50
- 2026-09-04T21:57:27+00:00 1 new review item(s)
- 2026-09-04T21:59:04+00:00 triage: marked ready for review (the only new item was Codex's usage-limit notice, not a finding; back to in_review while the automat)
- 2026-09-04T22:02:21+00:00 automated review: approve — Fence is correctly implemented in two layers, meets the acceptance criteria for the garden/clone incident vector, and is well-tested (246 pass, ruff clean). Default config denies only the two known repos rather than fully scoping to the worktree, but this is disclosed and the belt-and-braces revert is a solid net. cost=$1.33
- 2026-09-04T22:03:03+00:00 1 new review item(s)
- 2026-09-04T22:03:05+00:00 dispatched revise run 20260904T220304Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~12655 tokens)
