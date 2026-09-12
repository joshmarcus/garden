---
id: CG-472
title: Add an open pull requests tab to the board
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/web/pages/board.py
- src/garden/web/templates/board.html
- src/garden/web/templates/_board.html
- src/garden/web/templates/base.html
- src/garden/github.py
- src/garden/config.py
branch: garden/cg-472-add-an-open-pull-requests-tab-to-the-board
pr: https://github.com/joshmarcus/context-garden/pull/367
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T11:13:37+00:00'
created: '2026-09-09T11:13:01+00:00'
updated: '2026-09-09T11:32:05+00:00'
---

## Goal

Add a **PRs** tab to the existing board so people can see the open pull requests for the board's selected product and repository, including open PRs that are not linked to a Garden task.

## Owner request

Feature requested September 9, 2026: “Can we add a "PRs" tab to the board where all open PRs are listed?” Refined default: list open PRs, including unlinked open PRs, while excluding PRs associated with closed Garden tasks. Closed PR history is outside the default view.

## Acceptance criteria

- [ ] Add a `PRs` tab through the board's existing navigation and selected-product/repository conventions. Keep this within the current board rather than creating another dashboard.
- [ ] By default, show every open PR in the selected repository, including PRs with no Garden task. Exclude a PR when its associated Garden task is closed. Do not add closed PR history unless an existing board filter convention already supports it naturally.
- [ ] For each row, show the PR number, title, safe link, available review state, and available CI/check state. Show the associated Garden task when one is known; represent an unlinked PR clearly without inventing a task association.
- [ ] Derive task associations safely and scope GitHub data to the selected product/repository. Handle unavailable or partial review/check information honestly, and do not assume GitHub Actions is enabled; follow the repository's configured validation/status policy from CG-467.
- [ ] Provide clear loading, empty, and fetch-error states using existing board patterns. A GitHub permission, authentication, enterprise-host, or network failure must not break the rest of the board or silently look like an empty repository.
- [ ] Preserve current board navigation, filters, responsive behavior, and accessibility. Add focused tests for linked and unlinked open PRs, exclusion for a PR tied to a closed task, product/repository scoping, partial statuses, and empty/error behavior. Use proportionate direct UI verification for the new tab.

## Scope

Extend the existing board data and templates with the smallest repository-scoped PR listing. Reuse the current GitHub abstraction, validation policy, navigation, and rendering conventions. Avoid a new dashboard, an Actions-specific status pipeline, broad PR-management actions, or closed-history UI.

## Log

- 2026-09-09T11:13:01+00:00 approved (owner-requested board PR listing; default open PRs only, excluding PRs associated with closed tasks)
- 2026-09-09T11:13:37+00:00 dispatched work run 20260909T111337Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15448 tokens)
- 2026-09-09T11:21:51+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T11:23:24+00:00 opened https://github.com/joshmarcus/context-garden/pull/367 (base main): Added the Board PRs tab and committed it as 5db495e9. Exact-head focused tests (13 passed) and ruff passed; the supervised full relevant web/fake-GitHub selection also completed successfully before commit. cost=$1.14
- 2026-09-09T11:26:16+00:00 automated review: approve — The PRs tab meets the requested repository-scoped listing behavior, including linked/unlinked rows, terminal-task exclusion, safe links, status fallbacks, and explicit empty/error states. cost=$0.35
- 2026-09-09T11:32:05+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/367
