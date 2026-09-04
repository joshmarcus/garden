---
id: CG-047
title: Pick up the person's own PR comments as feedback
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/github.py
- src/garden/scheduler.py
branch: garden/cg-047-pick-up-the-person-s-own-pr-comments-as-feedback
pr: https://github.com/joshmarcus/context-garden/pull/12
attempts: 1
last_dispatched_at: '2026-09-04T17:27:02+00:00'
created: '2026-09-04T17:27:01+00:00'
updated: '2026-09-04T17:32:35+00:00'
---

## Goal

A review comment, line comment or review the person leaves on a task's PR becomes feedback for a revise round, even though the person and the garden share one GitHub login.

## Context

Asked during the first live run: a line comment on PR #11 ("Can you please add a screenshot to this PR?") was never picked up. `GitHub.feedback_since` excludes the garden's own login so the scheduler's review verdicts and "Pushed a revision round" comments do not feed back into a revise loop; with `gh` logged in as the person, that login is the person's, so their comments are the one kind the poll cannot see.

Tell the garden's comments apart by content, not by author: `GitHub.comment` appends an invisible marker (an HTML comment such as `<!-- context-garden -->`) to everything it posts, and `feedback_since` drops bodies carrying the marker instead of dropping the login. Keep `exclude_logins` (config) and the `[bot]` rule. Existing footers (`_garden run …_`, `_garden review run …_`, `_garden persona run …_`) stay for people to read. A `CHANGES_REQUESTED` review from the person is feedback as before.

## Acceptance criteria

- [ ] a comment from the same login as `gh` without the marker is returned by `feedback_since`; one with the marker is not.
- [ ] every comment the scheduler posts carries the marker (one place: `GitHub.comment`).
- [ ] the scheduler's own review and revision comments still do not start a revise round (existing tests).
- [ ] a unit test for `feedback_since` with a stubbed `_gh`.

## Out of scope

- Posting under a separate identity (CG-041).

## Log

- 2026-09-04T17:27:02+00:00 approved
- 2026-09-04T17:27:02+00:00 dispatched work run 20260904T172702Z-work via manual [human] (fresh session, base main, ~6044 tokens)
- 2026-09-04T17:28:49+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/12 (base main): The garden's own PR comments are recognised by an invisible marker instead of by login, so comments from the person who shares the gh login now become feedback for a revise round.
- 2026-09-04T17:30:34+00:00 automated review: approve — Correctly implements marker-based filtering to distinguish the garden's own comments from the person's, even when both share the same login. All acceptance criteria are met; existing tests (119 passed) verify scheduler comments don't trigger revise rounds. cost=$0.07
- 2026-09-04T17:32:35+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/12
