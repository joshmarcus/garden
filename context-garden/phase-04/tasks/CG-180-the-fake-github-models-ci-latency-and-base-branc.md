---
id: CG-180
title: The fake GitHub models CI latency and base-branch deletion, and a canary run checks a new pin before
  it is trusted
status: ready
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: medium
reading: []
created: '2026-09-05T09:42:00+00:00'
updated: '2026-09-05T10:31:14+00:00'
---

## Goal

The fake GitHub behaves like the real one in the two ways that broke the loop on 2026-09-05, and a canary run drives the throwaway garden with a freshly pinned build before that build is trusted with real PRs.

## Context

Three bugs merged in phase 03 with green tests and failed in the live loop within the hour: the merge queue rotated heads because a force-push puts the real rollup into `pending` (CG-176); deleting a merged parent's branch made real GitHub close the stacked child's PR (CG-173); a server restart lost a review verdict the old process had reaped in its last tick. The fake GitHub reports checks as instantly green, never closes a PR on base deletion, and the tests never restart a scheduler mid-flight. `garden qa --scripted` (CG-135, CG-169) already drives the web flows on a throwaway garden and is most of a canary.

## Acceptance criteria

- [ ] The fake GitHub has a configurable check latency: after any push the rollup is `PENDING` for N polls before it turns green or red, and tests for the merge queue and automerge use N >= 1.
- [ ] Deleting a branch in the fake GitHub closes every open PR whose base is that branch, with a `base_ref_deleted` timeline entry; the stacking tests exercise it.
- [ ] A scheduler test stops one `Scheduler` after reaping a review and starts another on the same garden; the verdict survives.
- [ ] `garden canary` (or `garden qa --scripted --pin <sha>`) installs the given build into a throwaway venv, runs the scripted QA flows plus one stacked-PR and one merge-queue scenario against the fake GitHub, and exits non-zero on any failure; the operator skill says to run it before moving the pin.

## Log

- 2026-09-05T10:31:14+00:00 approved (web)
