---
id: CG-290
title: The planner and synchronous kickoff run in the worker environment
status: cancelled
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:18+00:00'
updated: '2026-09-06T00:20:03+00:00'
---

## Goal

Route run_planner through scrubbed_env in a throwaway directory with only Read, Glob and Grep, or dispatch it as a run like start_kickoff. Add a test asserting HOME is not the operator's. Goal 3 item left unshipped by CG-194.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-279 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:20:03+00:00 pruned at approval (kickoff q2): owned by CG-245, running
