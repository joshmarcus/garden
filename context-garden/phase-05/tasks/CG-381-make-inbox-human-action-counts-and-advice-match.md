---
id: CG-381
title: Make Inbox human-action counts and advice match actual ownership
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: CG-337
created: '2026-09-07T12:54:17+00:00'
updated: '2026-09-07T12:59:56+00:00'
---

## Goal

Make Inbox ownership and recommended actions match actual scheduler state. Queued automated reviews and deliberately deferred work must not be presented as unresolved human decisions.

## Evidence

Owner-requested Inbox audit on 2026-09-07 found 24 "need you" items: 13 PRs already had pending_reviews, 10 were intentionally frozen phase06 drafts, and CG294 was an operator-owned deployment prerequisite. The CLI labeled queued reviews "no review yet" despite prior request_changes verdicts and recommended garden set-status TASK done. This is not approval or a safe merge procedure. CG337 has shipped; CG374 and CG362 are in flight. This follow-up owns these specific presentation/action defects and must not expand their frozen briefs.

## Acceptance criteria

- [ ] Derive owner-action count from actual unresolved decisions. Queued/running automatic review shows its queue or resource wait and prior verdict separately, without demanding owner action or recommending set-status done.
- [ ] Explicitly frozen/deferred drafts appear as deferred with the policy reason; owner-action count excludes them. Preserve a deliberate way to change the decision without approving or cancelling to clear a badge.
- [ ] An operator-owned deployment/recovery prerequisite has a concrete reason and next action and is not described as an unanswered owner question. Do not hide genuinely required authority or product choices.
- [ ] CLI and web agree on representative queued-review, prior-request-changes, deferred-draft, and deployment-wait fixtures. Focused tests verify displayed count, wording and actions; actual small Inbox journey verifies rendering. No broad unrelated page checklist, fabricated approval, state rewrite, or auto-merge bypass.
- [ ] Self-review and fix findings; focused bounded validation and exact-head CI for implementation.

## Owner clarification: PR actions require automated approval

Do not ask the human to act on a PR until an automated reviewer has approved its current head. Pending/queued reviews, missing verdicts, and request_changes are automated workflow states, not owner PR-action cards. Prior-head approval is stale after substantive code changes. Approved PRs still require normal exact-head CI/mergeability checks; approval does not itself authorize unsafe completion. Preserve technical recovery visibility as operator-owned and distinguish independent product questions from PR action requests. Cover pending, request_changes, approved-current-head and stale-approved-head cases in CLI/web count and action tests.
