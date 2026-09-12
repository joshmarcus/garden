---
id: CG-458
title: Pass option-like replay nonces as argument values
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/scheduler/review.py
- src/garden/interaction_replay.py
- tests/test_review.py
- tests/test_interaction_replay.py
branch: garden/cg-458-pass-option-like-replay-nonces-as-argument-value
pr: https://github.com/joshmarcus/context-garden/pull/351
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T23:05:38+00:00'
created: '2026-09-08T23:05:03+00:00'
updated: '2026-09-09T01:11:32+00:00'
---

## Goal

Generated replay nonces must reach argparse unchanged even when token_urlsafe begins with a hyphen. CG456 current a8d8783 replay225111 failed exit2 because the generated command passed --nonce followed by a value beginning with -, so argparse reported that --nonce expected an argument. This is command construction, not worker environment or implementation failure.

## Acceptance criteria

- [ ] Construct nonce argv so option-like values are always values (for example --nonce=VALUE); preserve nonce/head identity and existing replay attestations.
- [ ] Focused regressions cover leading hyphen, double-hyphen and ordinary urlsafe values through the actual parser/command path, without probabilistic retries or disabling checks.
- [ ] Demonstrate one corrected disposable replay with a previously failing option-like nonce; preserve actual exit/result evidence and use bounded focused validation plus exact-head CI.
- [ ] Keep this fix separate from collected-check parking idempotency, already owned by CG386; link the CG456 incident there rather than duplicate it.

## Evidence

Operator preserves the original result/specs in input-sweep-20260908T2125/cg456-nonce-failure-preserved.json and records corrected continuation in cg456-nonce-recovery.json. Do not read or mutate live production state from implementation/test runs.

## Log

- 2026-09-08T23:05:03+00:00 approved (delegated_operator)
- 2026-09-08T23:05:38+00:00 dispatched work run 20260908T230537Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~13519 tokens)
- 2026-09-08T23:39:55+00:00 opened https://github.com/joshmarcus/context-garden/pull/351 (base main): Replay nonce values are now emitted as attached argparse options, preserving option-like nonces. Added parser-path regressions and completed a disposable replay using -replay225111. cost=$0.44
- 2026-09-09T00:42:28+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/351
- 2026-09-09T01:11:32+00:00 automated review could not start: CG-458 is done: #351 was merged at 00:42:28
