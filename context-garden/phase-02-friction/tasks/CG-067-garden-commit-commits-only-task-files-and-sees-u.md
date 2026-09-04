---
id: CG-067
title: garden commit commits only task files and sees untracked ones
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/gitops.py
- src/garden/cli.py
created: '2026-09-04T18:35:09+00:00'
updated: '2026-09-04T18:35:09+00:00'
---

## Goal

`garden commit` never sweeps unrelated staged changes into its commit, and `garden status` and `garden commit` see task files inside wholly untracked directories.

## Context

Codex review on PR #23 (CG-042), merged before the comments were read. (P1) `commit_task_files` stages the task files and then runs an unqualified `git commit`, so anything the operator already had in the index is committed under the generated message. Commit the task pathspecs explicitly (`git commit -- <paths>` or `--only`), or stash and restore the index. (P2) `uncommitted_task_files` parses plain `git status --porcelain`, which collapses an untracked phase directory to one `?? dir/` entry, so new task files under a new phase are reported clean. Use `--untracked-files=all`.

## Acceptance criteria

- [ ] with an unrelated file staged, `garden commit` commits only task files and leaves the other change staged.
- [ ] a task file under an untracked phase directory is reported and committed.
- [ ] tests for both in `tests/test_commit.py`.
