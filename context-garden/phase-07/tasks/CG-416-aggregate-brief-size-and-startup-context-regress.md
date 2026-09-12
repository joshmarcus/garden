---
id: CG-416
title: Aggregate brief size and startup-context regressions in metrics
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: medium
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-416-aggregate-brief-size-and-startup-context-regress
pr: https://github.com/joshmarcus/context-garden/pull/331
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T19:09:22+00:00'
created: '2026-09-07T20:05:53+00:00'
updated: '2026-09-09T03:42:32+00:00'
---

## Goal

Aggregate brief size and startup-context regressions in metrics. Recheck current implementation before choosing the smallest compatible change.

## Acceptance criteria

- [ ] Aggregate existing brief-size fields by product, phase, mode and model/tier with run count, mean and useful percentile/max measures; distinguish estimated tokens from measured usage.
- [ ] Show trends or comparable windows so increased activity is distinguishable from increased per-run context. Include a clear baseline and minimum-sample policy for regression flags.
- [ ] Treat missing historical values as unknown, not zero; avoid double-counting archived/restored runs or continuations and do not rescan full transcripts per request.
- [ ] Test known-size mixed runs and archive transitions; reuse CG-012/066/149 measurements and current metrics rather than a second token estimator.

## Provenance and scope

Owner-provided additional gap F9, 2026-09-07. Generic requirements only. This task remains a phase-07 draft and does not authorize new access, deployment or external notifications. Refer to the shared spec, not the private environment survey.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T18:01:16+00:00 dispatched work run 20260908T180115Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~9214 tokens)


## Owner deployment checkpoint 2026-09-08T18:43:07.672930+00:00

Owner-requested deployment interruption after shared test hangs; exact source and streamed outputs checkpointed at /home/joshua/work/operator-test-tmp/rc6-deploy-20260908T1818/checkpoint-CG-416
Source c4a575cf012755d4d3738e7001127e47b94567ec is preserved in source.bundle; this interruption is not a code-failure verdict. Resume this implementation with focused tests and bounded validation; do not repeat unchanged full-suite failures.
- 2026-09-08T18:43:07+00:00 Operator-owned deployment recovery; preserved implementation, no author failure verdict.
- 2026-09-08T18:44:00+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-416`) or send it back (`garden triage CG-416 --changes "..."`)
- 2026-09-08T19:09:22+00:00 dispatched revise run 20260908T190922Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~11017 tokens)
- 2026-09-08T19:14:14+00:00 opened https://github.com/joshmarcus/context-garden/pull/331 (base main): Adds indexed brief/startup-context aggregates with comparable regression windows and displays measured cache-read usage alongside estimated and measured input tokens. cost=$0.33
- 2026-09-09T00:45:32+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/331
- 2026-09-09T03:42:32+00:00 automated review could not start: CG-416 is done: #331 was merged at 00:45:32
