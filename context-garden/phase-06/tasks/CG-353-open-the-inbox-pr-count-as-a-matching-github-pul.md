---
id: CG-353
title: Open the Inbox PR count as a matching GitHub pull request list
status: done
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/web/pages/inbox.py
- src/garden/github.py
- src/garden/config.py
branch: garden/cg-353-open-the-inbox-pr-count-as-a-matching-github-pul
pr: https://github.com/joshmarcus/context-garden/pull/406
attempts: 1
last_dispatched_at: '2026-09-09T23:19:27+00:00'
created: '2026-09-06T16:57:55+00:00'
updated: '2026-09-09T23:32:50+00:00'
---

## Goal

Clicking the Inbox's "PRs open" count opens the corresponding open pull request list on GitHub.com or the configured GitHub Enterprise host. The destination agrees with the count and current project scope, making the summary actionable.

## Context

Requested by Josh on 2026-09-06. Existing PR URLs and repository host configuration are authoritative. A label or another searchable grouping mechanism may be needed; inspect GitHub search capabilities and current garden PR metadata before choosing. Reuse existing identifiers if they reliably select the same set, rather than adding tags gratuitously.

## Acceptance criteria

- [ ] The count is an accessible link with a descriptive name and normal browser link behavior, targeting the correct configured host and repositories rather than hardcoding github.com.
- [ ] The query selects open PRs represented by the Inbox count, honoring project filters and garden ownership. Unrelated PRs are excluded. Verify the displayed count and destination against a fixture containing garden PRs, unrelated PRs and closed/merged PRs.
- [ ] If durable labels or another marker are necessary, document their meaning, apply them on creation, and safely backfill tracked open PRs without replacing existing labels or requiring excessive permissions. Explain permission failures; do not display a broader list as an exact match.
- [ ] Handle multiple repositories, mixed GitHub hosts and URL/query length limits explicitly. When no single exact list is possible, present clearly scoped destination links; never silently omit part of the count. Escape and encode query components correctly.
- [ ] Walk through the actual application: click the count, inspect the resulting host/query and list, change project scope, and verify zero-count and Enterprise-host behavior. No credentials or tokens appear in URLs. Record any unverified live Enterprise interaction as UNPROVEN rather than claiming it passed from URL unit tests.

## Scheduling

Deferred by the phase-06 feature freeze (2026-09-06). Preserve fast-forward maintenance and stabilization priorities. Coordinate with Inbox vocabulary changes in CG-296.

## Log

- 2026-09-07T20:10:03+00:00 Owner explicitly unfroze phase06 and authorized task approval on 2026-09-07; this supersedes historical feature-freeze notes. Preserve existing implementation/PR and normal review/resource gates.
- 2026-09-07T20:10:03+00:00 approved (owner-unfreeze-phase06)
- 2026-09-09T09:49:04+00:00 priority 3 -> 2 (web)
- 2026-09-09T09:49:13+00:00 back to draft (web)
- 2026-09-09T09:49:16+00:00 approved (web)
- 2026-09-09T23:01:25+00:00 dispatched work run 20260909T230121Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~12552 tokens)
- 2026-09-09T23:08:15+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T23:09:31+00:00 opened https://github.com/joshmarcus/context-garden/pull/406 (base main): Linked the Inbox open-PR count to configured, branch-scoped GitHub pull-request searches and added scoped fallback links for multiple hosts or repositories. Verified with 17 focused Inbox tests passing and clean repository lint; live Enterprise interaction is UNPROVEN. cost=$0.95
- 2026-09-09T23:11:55+00:00 automated review requested changes: The generated search fails once a repository has enough tracked PRs because GitHub limits boolean operators in issue/PR searches. cost=$0.35
- 2026-09-09T23:12:08+00:00 dispatched revise run 20260909T231205Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~13436 tokens)
- 2026-09-09T23:15:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T23:16:46+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/406: Bounded Inbox GitHub search chunks to GitHub's boolean-operator limit and retained exact PR destinations for overlong single filters. Verified on commit dd48c29b with 19 focused Inbox tests passing, clean Ruff lint, and compile checks; live Enterprise interaction is UNPROVEN. cost=$0.41
- 2026-09-09T23:19:12+00:00 automated review requested changes: The generated GitHub destinations are exact and bounded, but the PR count ignores the Inbox’s active owner scope. cost=$0.38
- 2026-09-09T23:19:27+00:00 dispatched revise run 20260909T231923Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~13829 tokens)
- 2026-09-09T23:22:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T23:24:06+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/406: Inbox PR counts and GitHub destinations now use the same effective-owner scope as Inbox cards, including inherited phase ownership. Verified with focused Inbox/web tests and Ruff on commit 4089d164; live Enterprise interaction remains UNPROVEN. cost=$0.35
- 2026-09-09T23:25:21+00:00 automated review: approve — The revision aligns the PR count and destinations with the Inbox’s effective-owner scope while preserving exact, bounded links across repositories and hosts. cost=$0.30
- 2026-09-09T23:32:50+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/406
