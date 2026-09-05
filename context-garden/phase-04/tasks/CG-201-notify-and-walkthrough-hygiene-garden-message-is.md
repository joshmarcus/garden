---
id: CG-201
title: 'Notify and walkthrough hygiene: GARDEN_MESSAGE is quoted in the documented Slack example, and
  the walkthrough scrubs stderr and absolute paths before it is committed'
status: ready
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 3
difficulty: easy
reading: []
created: '2026-09-05T10:30:00+00:00'
updated: '2026-09-05T10:31:19+00:00'
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
