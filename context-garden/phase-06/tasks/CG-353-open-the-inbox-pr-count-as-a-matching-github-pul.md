---
id: CG-353
title: Open the Inbox PR count as a matching GitHub pull request list
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 3
difficulty: medium
reading: []
created: '2026-09-06T16:57:55+00:00'
updated: '2026-09-06T16:57:55+00:00'
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
