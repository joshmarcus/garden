---
id: CG-703
title: Git coordination subprocesses have no timeout, so a stalled remote or credential
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: persona:staff-engineer:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:06:03+00:00'
---

## Goal

Give src/garden/git_coordination.py:_run and _push one bounded subprocess abstraction with noninteractive authentication, descendant cleanup, and a total operation deadline. Treat an interrupted push as ambiguous and resolve its existing operation ID before execution. Add controlled stalled-fetch, stalled-push, and accepted-push/lost-reply tests that assert bounded return and retained obligations.

## Context

Raised by the staff-engineer persona review (Git transport deadlines). persona:staff-engineer:context-garden/phase-10.
