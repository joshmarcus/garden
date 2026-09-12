---
id: CG-398
title: Validate a human-gated enterprise profile with bot feedback and private notifications
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-395
- CG-397
priority: 1
difficulty: medium
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-398-validate-a-human-gated-enterprise-profile-with-b
pr: https://github.com/joshmarcus/context-garden/pull/318
runner: local
attempts: 1
last_dispatched_at: '2026-09-08T13:52:46+00:00'
created: '2026-09-07T19:56:16+00:00'
updated: '2026-09-08T17:30:11+00:00'
---

## Goal

Provide a generic example profile using existing trusted-bot, notification, draft PR, base-branch and automerge settings. Add code only for demonstrated configuration gaps.

## Acceptance criteria

- [ ] Human review, approval, merge and deployment remain required; automated approval cannot override the profile. Preserve the configured PR description sections.
- [ ] Trusted synthetic bot findings with priority markers drive actionable feedback; status notices and untrusted bots do not trigger revision loops.
- [ ] Construct notification payloads without executing worker-controlled text; constrain recipients to the configured calling user. Validate escaping, timeout and nonfatal failure using fake delivery; actual diagnostic sends are explicit.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: G7, G9 and existing configuration. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T13:52:46+00:00 dispatched work run 20260908T135246Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~9195 tokens)
- 2026-09-08T14:58:13+00:00 opened https://github.com/joshmarcus/context-garden/pull/318 (base main): Added a generic human-gated enterprise profile, trusted-bot settings, and safely constructed recipient-pinned notification JSON payloads. Focused regression coverage and lint pass at b82380493cdf859aa86421ce198a62d2cad31bae. cost=$4.05
- 2026-09-08T15:33:22+00:00 check did not run (20260908T153320Z-check): idle 39 min (no output or file change); will retry
- 2026-09-08T15:36:13+00:00 automated review produced no verdict (idle 42 min (no output or file change))
- 2026-09-08T16:31:33+00:00 review validation scope expansion: replacement notification interaction replay — The planned scheduler replay failed with exit 126 and produced no manifest, so the exact head was replayed against a disposable HTTP receiver.
- 2026-09-08T16:31:35+00:00 automated review requested changes: The trusted-bot behavior passes, but two security/policy outcomes remain unmet: the complete human gate is not represented or tested, and notification recipients are not protected by the executable-config fence. cost=$0.63
- 2026-09-08T17:30:11+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/318
