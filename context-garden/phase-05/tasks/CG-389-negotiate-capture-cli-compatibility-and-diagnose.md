---
id: CG-389
title: Negotiate capture CLI compatibility and diagnose renderer exit before requesting revisions
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
created: '2026-09-07T17:59:29+00:00'
updated: '2026-09-07T17:59:54+00:00'
---

## Goal
A pinned controller can capture an older supported worktree without wasting implementation revisions on an incompatible invocation.

## Evidence
CG216 six revision rounds ended with UI renderer did not return a result and no PNG captures. Installed v0.2.0rc1 passes a fourth pages argument; branch c82d123 only accepts three argv entries, exiting2 with empty output. Operator compatibility patch accepted both forms; identical controller invocation then captured14pages/56PNGs in69s,691MiB,no swap. Evidence /home/joshua/work/operator-test-tmp/cg216-capture-compat.

## Acceptance criteria
- Negotiate or fall back across supported legacy and page-selecting capture entry points without hiding genuine render failures; exercise new controller against old worktree source.
- Report child exit code, sanitized invocation and empty-output/protocol diagnosis, including quiet exit2; retain stderr and evidence paths.
- Treat a protocol/infrastructure mismatch as operator/check recovery rather than repeated implementation revisions; preserve PR, feedback and counters.
- Recheck the same commit successfully after environment/protocol recovery and enqueue normal automated review once; focused mixed-version regression and disposable actual capture evidence.
