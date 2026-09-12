---
id: CG-420
title: Repair production remote claims and install the complete Codex runtime
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- context-garden/phase-06/specs/ec2-workers.md
branch: codex/cg420-production-worker-recovery
pr: https://github.com/joshmarcus/context-garden/pull/302
runner: manual
attempts: 1
last_dispatched_at: '2026-09-08T08:54:53+00:00'
created: '2026-09-08T08:20:55+00:00'
updated: '2026-09-08T12:01:48+00:00'
---

## Goal

Make the normal production worker rollout succeed with a configured GitHub repository URL and the complete pinned Codex runtime.

## Context

The first real CG419 EC2 rollout exposed two gaps missed by fixture-only checks. The claim endpoint converted the configured HTTPS repository URL into a local Path and returned HTTP500 before leasing the run. Using the existing controller clone as the supported product repo setting restored claims while preserving saved state and run hashes. The first authenticated Codex turn then returned blocked because the standalone binary lacked codex-code-mode-host. Installing the complete official pinned Codex0.153.4 package enabled a real worker verification: 12 focused tests passed and its report returned through the production claim/heartbeat/finish protocol.

Operator evidence is retained under /home/joshua/work/operator-test-tmp/aws-production-20260908. The controller and worker still run Garden0.3.0rc2; the URL setting and live runtime repair are documented recovery actions, not a final-bootstrap clean-image replay. Direct operator implementation during fast-forward; no additional model agent.

## Acceptance criteria

- [ ] Remote claims resolve URL and relative task repositories through the controller's repository logic before reading branch heads, preserving credential-free claim URLs and lease protection.
- [ ] Production bootstrap installs the complete pinned official Codex package, including the Code Mode host and packaged resources, with verified digest and manifest, safe archive paths, and permissions usable by the unprivileged worker.
- [ ] Meaningful regressions reproduce the production URL failure and missing-runtime-companion failure, and reject corrupt or incomplete packages before installation.
- [ ] Exact-head CI and operator self-review pass; publish and deploy a narrow versioned fix while preserving the active AWS host, returned results, existing resource/budget limits, and scheduler pause.
- [ ] Record actual productive AWS evidence, remaining replay/refresh limitations, and restore URL configuration only after the permanent claim fix is verified.

## Out of scope

Additional hosts, expanded IAM rights, new model agents, unrelated Phase07 features, and claims that phase stabilization or a final clean-image replay has passed.

## Log

- 2026-09-08T08:48:05+00:00 PR attached: https://github.com/joshmarcus/context-garden/pull/302 (pr_number none -> 302)
- 2026-09-08T08:54:53+00:00 dispatched work run 20260908T085453Z-work via manual [human] (fresh session, base main, ~13469 tokens)
- 2026-09-08T12:01:48+00:00 PR302 merged with exact-head CI and self-review; versioned rc3 controller/worker source verified. All four production hosts completed real remote regression/lint checks from restored repository URL; bootstrap secrets retired and absolute14:01:25UTC deadlines verified. Phase stabilization remains unproven.
