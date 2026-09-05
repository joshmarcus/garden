---
id: CG-147
title: A product clone gets a git identity when it is made, and doctor checks every clone
status: running
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 2
difficulty: easy
reading:
- src/garden/gitops.py
- src/garden/cli.py
- src/garden/scheduler.py
branch: garden/cg-147-a-product-clone-gets-a-git-identity-when-it-is-m
attempts: 1
last_dispatched_at: '2026-09-05T04:47:55+00:00'
created: '2026-09-05T02:50:49+00:00'
updated: '2026-09-05T04:47:55+00:00'
---

## Goal

When the garden clones a product repo (including a `self: true` product), it sets the clone's `user.name` and `user.email` from the garden's own configuration, and `garden doctor` checks every clone under `work_dir/repos/` for an identity, so a commit made by the scheduler or a worker never fails with "Author identity unknown".

## Context

Found at the phase-02 retro on the first live run. The first friction of the day (CG-032) was a missing git identity in the WSL profile; it was set repo-locally in the product clone by hand. The self product's clone made at 02:41 for the retro had no identity, so the reconciliation's render was staged in the retro worktree but never committed, no PR appeared, and the retro entry vanished from state without a card. The person set the identity by hand and re-ran the reconciliation. Take the identity from `garden.yaml` (`git.user_name`, `git.user_email`, defaulting to the garden checkout's own config or the `gh` login) and write it into every clone at creation; `doctor` lists clones without one; a commit failure inside a reap becomes a card that names the repo and the error, never a silent return.

## Acceptance criteria

- [ ] a fresh clone (product or self) has a repo-local identity; a test creates one in a temp garden.
- [ ] `garden doctor` reports a clone with no identity and exits 1.
- [ ] a failed commit or push in `reap_retro` raises a card with the error text.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)
- 2026-09-05T02:56:00+00:00 deferred by the feature freeze (2026-09-05): identity set by hand in the garden clone this time
- 2026-09-05T03:02:34+00:00 approved (web)
- 2026-09-05T03:05:55+00:00 back to draft: approved by mistake during the phase 02 freeze; carried into phase 03
- 2026-09-05T03:19:59+00:00 approved (web)
- 2026-09-05T04:47:55+00:00 dispatched work run 20260905T044746Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~6102 tokens)
