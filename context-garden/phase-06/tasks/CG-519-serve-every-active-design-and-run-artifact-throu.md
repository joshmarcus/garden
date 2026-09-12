---
id: CG-519
title: Serve every active design and run artifact through an inert preview boundary
status: done
product: context-garden
phase: phase-06
depends_on:
- CG-318
- CG-427
priority: 0
difficulty: medium
reading:
- src/garden/web/app.py
- src/garden/web/pages/design.py
- src/garden/web/pages/runs.py
- src/garden/web/trust.py
- tests/test_web.py
- context-garden/phase-06/specs/context-garden-stripe-environment.md
branch: garden/cg-519-serve-every-active-design-and-run-artifact-throu
pr: https://github.com/joshmarcus/context-garden/pull/426
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T11:37:03+00:00'
created: '2026-09-10T11:18:52+00:00'
updated: '2026-09-10T12:00:16+00:00'
---

## Goal

Treat generated design files and run artifacts as untrusted data. Apply one preview policy to HTML, SVG and every other active format so opening an artifact cannot execute with the operator application's authority.

## Context

CG-318 added design and capture serving and CG-427 renders event streams. Their useful one-click surfaces need a format-complete sandbox and response-header contract, including unmerged worktree files.

## Acceptance criteria

- [ ] Centralize raw artifact classification and response policy for design, task and run links, including worktree refs and archived attempts.
- [ ] Render supported active formats in a sandboxed separate-origin or equivalent inert boundary with restrictive CSP and nosniff headers. Unsupported or ambiguous formats download as attachments.
- [ ] Keep markdown sanitization, safe paths, product/ref identity and content-type handling intact. Filenames, metadata and payloads cannot inject headers, navigation or executable markup into the operator origin.
- [ ] Cover scripted SVG, active HTML, polyglot/incorrect MIME files, nested links, missing files, range/download behavior and benign images/documents through disposable HTTP tests.
- [ ] Preserve usable design and capture navigation and record the security boundary in operator documentation without exposing private artifact content.

enterprise_capability_key: enterprise-safe-active-artifact-preview

## Log

- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T11:37:03+00:00 dispatched work run 20260910T113703Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~19059 tokens)
- 2026-09-10T11:46:45+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:48:09+00:00 opened https://github.com/joshmarcus/context-garden/pull/426 (base main): Centralized inert artifact responses for design and run capture routes, including active worktree and archived captures. Verified focused web tests, lint, and source compilation. cost=$0.98
- 2026-09-10T11:52:15+00:00 automated review: approve — The centralized artifact boundary consistently protects design, worktree, live-run, and archived-run responses while retaining sanitized Markdown and path/product/ref checks. cost=$0.31
- 2026-09-10T12:00:16+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/426
