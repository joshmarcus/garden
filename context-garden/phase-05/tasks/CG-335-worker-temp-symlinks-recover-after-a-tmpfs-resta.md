---
id: CG-335
title: Worker temp symlinks recover after a tmpfs restart
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
created: '2026-09-06T13:15:20+00:00'
updated: '2026-09-06T13:15:21+00:00'
---

## Goal

Worker temp symlinks recover after a tmpfs restart

## Context

At operator takeover on 2026-09-06 at 13:13Z, /home/joshua/work/tmp pointed to missing /tmp/garden-work after WSL restarted. Seventeen tasks failed to dispatch with Errno 17 File exists; CG-308 checks recorded process never started. The operator recreated the target, retried those tasks, and added a service ExecStartPre mkdir drop-in. Make the product diagnose and safely recover this supported temp-directory configuration without operator intervention. Evidence: the failed CG-332 run records, the 13:09-13:14Z event window, CG-310 temp configuration.

## Acceptance criteria

- [ ] An absent tmpfs target for the configured worker temp symlink can be recovered safely, with a regression test. Invalid or unsafe temp paths produce a useful environment stop rather than failing the entire ready queue.

## Log

- 2026-09-06T13:15:21+00:00 approved (cli)
