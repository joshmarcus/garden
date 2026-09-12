---
id: CG-395
title: Support explicit GitHub Enterprise hosts across all repository operations
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: medium
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-395-support-explicit-github-enterprise-hosts-across
pr: https://github.com/joshmarcus/context-garden/pull/307
runner: local
attempts: 1
last_dispatched_at: '2026-09-08T16:32:31+00:00'
created: '2026-09-07T19:56:15+00:00'
updated: '2026-09-08T19:11:54+00:00'
---

## Goal

Configure host and API base at the appropriate product boundary, retaining github.com defaults. Audit both CLI and REST paths, URL construction and diagnostics.

## Acceptance criteria

- [ ] Parse HTTPS and SSH remotes for a configured enterprise host; reject ambiguous or mismatched host identities.
- [ ] PRs, reviews, comments, timelines, branches, links and authentication checks target the configured host explicitly, independent of ambient gh defaults.
- [ ] Exercise two products on different hosts, non-default base branches, CLI and REST fallback; no credential or request crosses hosts. Use synthetic hosts in fixtures.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: G1. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.

## Suggestions

- [ ] 2026-09-08 web: The scp-form patterns hardcode git@, so a remote rfom a host using per-org service accounts (acct-1234@host:owner/repo.git) matches none of the three and yields no slug -- the case this PR exists to support. Git's rule is [user@]host:path; the username is arbitrary. Same root cause is config.py:350.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T12:02:32+00:00 Owner four-host rollout verified; route this eligible Phase07 P0 task to the authenticated AWS pool while retaining two local resource slots.
- 2026-09-08T12:03:24+00:00 dispatched work run 20260908T120323Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~8314 tokens)
- 2026-09-08T12:22:41+00:00 opened https://github.com/joshmarcus/context-garden/pull/307 (base main): Added product-scoped GitHub host, API base, and token routing with explicit CLI and REST targeting. Enterprise remote parsing, scoped authentication, diagnostics, and cross-host regression coverage are included. cost=$1.90
- 2026-09-08T12:51:04+00:00 check did not run (20260908T125036Z-check): idle 30 min (no output or file change); will retry
- 2026-09-08T13:55:52+00:00 automated review requested changes: Enterprise routing is incomplete: manual PR adoption rejects enterprise URLs, while configurable API bases and slug-only routing can send credentials or requests to the wrong host. The required interaction replay was inaccessible. cost=$0.30
- 2026-09-08T14:00:24+00:00 triage: changes requested by hand: - **automated review** blocking (`src/garden/cli/loop.py`:357): Manual adoption of an enterprise PR URL always validates
- 2026-09-08T14:29:35+00:00 dispatched revise run 20260908T142935Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~10715 tokens)
- 2026-09-08T15:22:48+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/307: Host-scoped GitHub routes now preserve host identity through scheduler operations and manual PR adoption, while rejecting API bases that could redirect scoped tokens. Arbitrary SSH/SCP service-account usernames are accepted across repository resolution paths. cost=$1.14
- 2026-09-08T15:40:33+00:00 automated review produced no verdict (idle 21 min (no output or file change))
- 2026-09-08T16:23:56+00:00 stalled: review finding repeated after a revise round: running-app evidence incomplete: affected interaction is missing or failed; empt; run `garden triage CG-395 --changes "<feedback>" to unblock`


## Owner-requested direct operator conclusion, 2026-09-08T16:32:30.008959+00:00

Owner asked this operator to get CG395 unstuck or drive it to conclusion. Preserve197a43d and all existing fixes. Operator owns the existing worktree for the case-normalization regression and a relevant served verification journey, followed by exact-source validation and actual review. No duplicate author run, metadata-only rewrite or production deployment.
- 2026-09-08T16:32:31+00:00 dispatched revise run 20260908T163230Z-revise via manual [human] (fresh session, base main, ~10273 tokens)
- 2026-09-08T19:11:54+00:00 Verified PR307 externally merged at 2026-09-08T18:20:52Z as 020eced75890d243e61f2e9a045a7abba9461591. Current669f519a full GitHub CI passed twice; scheduler-owned affected replay passed13HTTP/6syntheticAPI requests. AWS one nested-pip fixture failure remains recorded, not relabeled.
