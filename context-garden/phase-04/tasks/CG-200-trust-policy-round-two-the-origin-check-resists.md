---
id: CG-200
title: 'Trust policy round two: the origin check resists DNS rebinding, bot trust is opt-in, and self-product
  PRs need a person or a second round'
status: in_review
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: medium
reading: []
branch: garden/cg-200-trust-policy-round-two-the-origin-check-resists
pr: https://github.com/joshmarcus/context-garden/pull/155
attempts: 2
last_dispatched_at: '2026-09-05T15:21:22+00:00'
created: '2026-09-05T10:30:00+00:00'
updated: '2026-09-05T15:50:13+00:00'
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

## Log

- 2026-09-05T10:31:18+00:00 approved (web)
- 2026-09-05T12:50:05+00:00 dispatched work run 20260905T124956Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4432 tokens)
- 2026-09-05T13:09:46+00:00 opened https://github.com/joshmarcus/context-garden/pull/155 (base main): The web origin check now validates against the bound address plus web.trusted_origins (never the request Host, so DNS rebinding is refused); [bot] PR comments are trusted only when github.trusted_bots names them (default empty); and PRs against self/provides_tool products need two review rounds before automerge (per-product override wins, stricter global still applies). Tests and docs added for each. cost=$6.98
- 2026-09-05T13:09:59+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/poll.py); a rebase agent will resolve it
- 2026-09-05T13:10:14+00:00 dispatched rebase run 20260905T131014Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~7594 tokens)
- 2026-09-05T13:12:48+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:13:12+00:00 dispatched work run 20260905T131312Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4842 tokens)
- 2026-09-05T13:14:23+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:33:48+00:00 re-enabled by hand; revise run will follow
- 2026-09-05T14:59:37+00:00 dispatched revise run 20260905T145937Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~5309 tokens)
- 2026-09-05T15:10:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/155: Rebased the PR onto main (resolving conflicts in web/app.py and cli/diagnostics.py from the interim CG-185/serve-logging changes) and fixed a gap the rebase exposed: github.trusted_bots wasn't in config.RESTART_KEYS even though it's baked into the GitHub client at construction like its siblings, so the Config page would have wrongly called it live-reloadable. cost=$1.02
- 2026-09-05T15:15:46+00:00 automated review: approve — Origin check, bot-trust opt-in, and self/tool two-round gate are all correctly implemented and thoroughly tested; verified tests (711 passed) and lint pass locally. cost=$0.46
- 2026-09-05T15:17:08+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/trust.py, tests/test_web.py); a rebase agent will resolve it
- 2026-09-05T15:21:22+00:00 dispatched rebase run 20260905T152122Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~17355 tokens)
- 2026-09-05T15:30:41+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/155: Resolved rebase conflicts in src/garden/web/trust.py and tests/test_web.py (main had independently landed a weaker DNS-rebinding guard via CG-194's loopback-Host check, fff3c9a; kept this branch's stronger bind-address/server_origins design from 22f018c instead), plus doc conflicts in README.md and docs/architecture.md describing the same setting. Also fixed two tests whose Origin/Referer fixtures silently auto-merged to the wrong (main-side) values, and removed a now-superseded test of the discarded loopback-Host mechanism. All 720 tests pass, ruff clean, rebase complete with no remaining conflicts. cost=$1.36
- 2026-09-05T15:30:41+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-200` for one more round, or review on GitHub
- 2026-09-05T15:34:59+00:00 automated review: approve — All three acceptance criteria are correctly implemented and tested; origin check, bot-trust opt-in, and self/tool two-round gate all verified against the diff, and the full suite (720 passed, 3 skipped) and ruff pass locally. cost=$0.35
- 2026-09-05T15:37:52+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T15:40:07+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-200` for one more round, or review on GitHub
- 2026-09-05T15:47:44+00:00 automated review: approve — All three trust-hardening changes are correctly implemented and tested; origin check ignores Host entirely, bot trust is opt-in via trusted_bots, and self/tool products correctly require two review rounds with proper override semantics. cost=$0.48
- 2026-09-05T15:47:50+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T15:50:13+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-200` for one more round, or review on GitHub
