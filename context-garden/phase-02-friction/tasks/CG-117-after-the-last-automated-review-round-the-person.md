---
id: CG-117
title: After the last automated review round, the person is told the PR is theirs
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/inbox.py
- src/garden/web/templates/inbox.html
branch: garden/cg-117-after-the-last-automated-review-round-the-person
pr: https://github.com/joshmarcus/context-garden/pull/60
attempts: 1
last_dispatched_at: '2026-09-04T22:10:53+00:00'
created: '2026-09-04T21:56:41+00:00'
updated: '2026-09-04T22:26:37+00:00'
---

## Goal

When a PR has used its automated review rounds (`review.max_rounds`), the person is told plainly that the PR is now theirs to review, on the Inbox and the task page; the task does not sit silently in `in_review`.

## Context

Found on the first live run. CG-081 (PR #48) had two automated review rounds, both asking only for description changes; after the third push `_maybe_review` skipped the review because `review_rounds` had reached the cap, and the task sat in `in_review` with no run and no card for fifteen minutes until the person noticed and started a review by hand from the task page (which made round three, above the cap). That behaviour after the cap is right: the automated reviewer has had its say and a person should look. But it has to be said. When the cap stops a review, log it on the task, and show an Inbox card under "Needs a decision": "Automated review rounds used; PR #48 is yours", with the link, the last verdict's summary, and actions: open the PR, run one more automated review (which raises the cap by one for this task), or send back with a note. `garden inbox` and the digest list it too. Coordinate with CG-106's stuck-task audit so this state is not also flagged as "stuck".

## Acceptance criteria

- [ ] reaching the review cap logs a line on the task and makes an Inbox card with the PR link and the actions.
- [ ] "one more review" dispatches a review and raises the cap for that task by one.
- [ ] a test with the fake harness.

## Log

- 2026-09-04T22:10:53+00:00 dispatched work run 20260904T221044Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~5680 tokens)
- 2026-09-04T22:23:15+00:00 opened https://github.com/joshmarcus/context-garden/pull/60 (base main): Reaching the automated-review cap now logs a line on the task and raises an Inbox/task-page attention card (kind review_cap) with PR link, 'One more automated review', and 'Send back with a note' actions; 'One more automated review' (garden review <id> / Scheduler.review_again) rolls the round counter back one, raising the cap by one round, and dispatches immediately. Added a fake-harness test exercising the full two-round cap-then-grant flow. cost=$7.76
- 2026-09-04T22:26:37+00:00 automated review: approve — All three acceptance criteria are met with test evidence; the cap now flags a review_cap needs-human card wired through existing CG-045 machinery, and review_again grants exactly one more round. Correct, in-scope, clean description. cost=$0.70
