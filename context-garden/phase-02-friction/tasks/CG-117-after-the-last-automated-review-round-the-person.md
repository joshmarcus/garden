---
id: CG-117
title: After the last automated review round, the person is told the PR is theirs
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/inbox.py
- src/garden/web/templates/inbox.html
created: '2026-09-04T21:56:41+00:00'
updated: '2026-09-04T21:56:41+00:00'
---

## Goal

When a PR has used its automated review rounds (`review.max_rounds`), the person is told plainly that the PR is now theirs to review, on the Inbox and the task page; the task does not sit silently in `in_review`.

## Context

Found on the first live run. CG-081 (PR #48) had two automated review rounds, both asking only for description changes; after the third push `_maybe_review` skipped the review because `review_rounds` had reached the cap, and the task sat in `in_review` with no run and no card for fifteen minutes until the person noticed and started a review by hand from the task page (which made round three, above the cap). That behaviour after the cap is right: the automated reviewer has had its say and a person should look. But it has to be said. When the cap stops a review, log it on the task, and show an Inbox card under "Needs a decision": "Automated review rounds used; PR #48 is yours", with the link, the last verdict's summary, and actions: open the PR, run one more automated review (which raises the cap by one for this task), or send back with a note. `garden inbox` and the digest list it too. Coordinate with CG-106's stuck-task audit so this state is not also flagged as "stuck".

## Acceptance criteria

- [ ] reaching the review cap logs a line on the task and makes an Inbox card with the PR link and the actions.
- [ ] "one more review" dispatches a review and raises the cap for that task by one.
- [ ] a test with the fake harness.
