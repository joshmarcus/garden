---
id: CG-200
title: 'Trust policy round two: the origin check resists DNS rebinding, bot trust is opt-in, and self-product
  PRs need a person or a second round'
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: medium
reading: []
created: '2026-09-05T10:30:00+00:00'
updated: '2026-09-05T10:30:00+00:00'
---

## Goal

Origin is compared with Host, so a rebound page whose name appears in both passes; every `[bot]` login is trusted, so an app relaying untrusted comment text can steer a worker; an easy or medium PR against the self or tool product merges on the LLM review alone and such a PR can change the loop that merges it.

## Provenance

From the phase-03 persona reviews of 2026-09-05 (security:medium, security:medium, security:medium); filed by the operator so that every finding is kept (see CG-187). Reports: `context-garden/phase-03/docs/reviews/`.

## Acceptance criteria

- [ ] The origin check compares against the configured bind host and `web.trusted_origins` only.
- [ ] Bots are trusted only when listed in `github.trusted_bots`; the default is empty.
- [ ] PRs against a product with `self: true` or `provides_tool: true` require `automerge_min_review_rounds: 2` by default or a person; the setting is documented.
- [ ] Tests for each.

