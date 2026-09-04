---
id: CG-050
title: The running garden picks up merged changes to itself
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/cli.py
- docs/architecture.md
created: '2026-09-04T17:35:07+00:00'
updated: '2026-09-04T17:35:07+00:00'
---

## Goal

When a PR merges into a product whose repo is the garden itself (`repo: .`), the garden's checkout is brought up to date and the person is told to restart `garden serve` (or it restarts its loop itself), so a merged fix is the code that runs.

## Context

During the first live run, CG-047 (PR #12) changed how the poll tells the garden's own comments from a person's. It merged, the poll saw the merge and marked the task done, and the running scheduler kept using the old code, because `garden serve` runs from this checkout and nothing pulls main after a merge. A comment the person had left on PR #11 stayed invisible for another ten minutes until the checkout was pulled and the server restarted by hand. The same applies to every fix this phase files: each one changes the garden that is running it.

On `_on_merged` for a product with `repo: .`: fast-forward the checkout's base branch to `origin/<base>` if the working tree is clean apart from files under `tasks/` and `.garden/` (those are the garden's own edits), record an event, and show a "restart to load" line on the Inbox and in `garden status` until the process is restarted. `garden serve` could also watch its own package's mtime and re-exec itself when the loop is idle. Merged worker branches are already fetched, so this is the same fetch plus a fast-forward.

## Acceptance criteria

- [ ] after a merge into `repo: .`, `git log` in the garden checkout shows the merge commit without a manual pull.
- [ ] a dirty tree outside `tasks/` and `.garden/` is left alone with a warning on the Inbox.
- [ ] the Inbox and `garden status` say when the running server is older than the checkout.
- [ ] a test with the fake origin.

## Out of scope

- Products in other repos; their code is not the running garden.
