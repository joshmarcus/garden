---
id: CG-201
title: 'Notify and walkthrough hygiene: GARDEN_MESSAGE is quoted in the documented Slack example, and
  the walkthrough scrubs stderr and absolute paths before it is committed'
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 3
difficulty: easy
reading: []
branch: garden/cg-201-notify-and-walkthrough-hygiene-garden-message-is
pr: https://github.com/joshmarcus/context-garden/pull/162
attempts: 1
last_dispatched_at: '2026-09-05T15:05:54+00:00'
created: '2026-09-05T10:30:00+00:00'
updated: '2026-09-05T15:26:54+00:00'
---

## Goal

`GARDEN_MESSAGE` carries worker-written text and the Slack example splices it unquoted into JSON; captured walkthrough pages include run stderr, briefs and absolute paths and are committed to the garden repo.

## Provenance

From the phase-03 persona reviews of 2026-09-05 (security:low, security:low); filed by the operator so that every finding is kept (see CG-187). Reports: `context-garden/phase-03/docs/reviews/`.

## Acceptance criteria

- [ ] The notify docs and `examples/` quote the message with `jq -Rs` or equivalent, and doctor warns about an unquoted example.
- [ ] The walkthrough redacts absolute home paths and skips stderr blocks unless `--include-stderr` is given.
- [ ] Tests for both.

## Log

- 2026-09-05T10:31:19+00:00 approved (web)
- 2026-09-05T13:16:34+00:00 dispatched work run 20260905T131626Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4380 tokens)
- 2026-09-05T13:17:48+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:18:09+00:00 dispatched work run 20260905T131809Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4482 tokens)
- 2026-09-05T13:19:15+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:33:49+00:00 reset to ready by hand
- 2026-09-05T14:34:03+00:00 dispatched work run 20260905T143403Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4767 tokens)
- 2026-09-05T14:37:34+00:00 reset to ready by hand
- 2026-09-05T15:05:54+00:00 dispatched work run 20260905T150554Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4863 tokens)
- 2026-09-05T15:11:41+00:00 opened https://github.com/joshmarcus/context-garden/pull/162 (base main): Verified the existing commit on this branch fully implements CG-201: the Slack notify example now quotes GARDEN_MESSAGE via jq, doctor warns on unsafe splicing, and garden walkthrough redacts home paths and omits stderr unless --include-stderr is passed. Full test suite and lint pass with no further changes needed. cost=$0.25
- 2026-09-05T15:15:47+00:00 automated review: approve — Both hygiene fixes are correctly implemented and tested: the Slack example now quotes GARDEN_MESSAGE via jq and doctor warns on unsafe splicing; walkthrough captures redact the home directory and omit stderr unless --include-stderr is passed. cost=$0.40
- 2026-09-05T15:19:44+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T15:23:53+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/162
- 2026-09-05T15:26:54+00:00 automated review could not start: CG-201 is done: #162 was merged at 15:23:53
