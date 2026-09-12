---
id: CG-424
title: Make metadata-only review gaps advisory and align worker verification instructions
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/brief.py
- src/garden/review.py
- src/garden/scheduler/review.py
- tests/test_review.py
- docs/worker-protocol.md
branch: codex/cg424-evidence-metadata
pr: https://github.com/joshmarcus/context-garden/pull/306
runner: manual
created: '2026-09-08T11:15:50+00:00'
updated: '2026-09-08T14:06:38+00:00'
---

# Goal
Stop review/revision churn caused solely by missing artifact metadata, and make author/reviewer verification expectations consistent and proportionate.

## Context
Owner instructions 2026-09-08: do not block on missing artifact metadata only; investigate why agents do not know to record it; give implementers leeway in implementation and equivalent verification. CG253/PR265 and CG327/PR251 received passing substantive assessments followed by a mechanical rejection because scheduler review.py required a JSON artifact whose states/events exactly equalled the reviewer paraphrase. The implementation brief exposes per-criterion prose; the detailed interaction schema is in the reviewer instructions and was not a shared author completion contract. Old review records can remain after a PR merges: inspect actual current PR state before intervening.

## Acceptance criteria
- [ ] Missing or differently formatted artifact metadata alone produces an advisory with a concrete correction, while an otherwise passing current-head review can approve; actual test/behavior failures, contradictory source provenance and materially unverified outcomes still block.
- [ ] Author and reviewer briefs explain the same minimal evidence record, where to save/report it, and how to verify it before completion. Reviewers reuse inspectable evidence and do not require identical paraphrases, an arbitrary filename or a redundant rerun solely for packaging.
- [ ] Implementers may choose a different implementation and equivalent meaningful verification when the requested outcome and explicit constraints hold; reviewers identify a concrete defect or unmet outcome for each blocking finding. Explicit phase evidence holds remain intact.
- [ ] Focused regression tests demonstrate advisory-only metadata gaps, approval with substantive evidence, retained genuine blockers and aligned generated briefs. Preserve old review/evidence records and record any operator reconciliation separately.

## Log

- 2026-09-08T11:17:17+00:00 Direct operator owns this bounded repair while normal scheduled work and the AWS rollout continue; do not dispatch a duplicate implementation.
- 2026-09-08T12:07:34+00:00 Operator implementation2f0225d0 in PR306;159review/brief tests and lint pass, including metadata-only approval and retained real blockers. Exact-head fullCI pending; versioned rollout still required.
- 2026-09-08T12:35:50+00:00 PR306 merged0dff3636 after both exact2f0225d0 fullCI runs succeeded and operator self-review. Controller remains0.3rc3; narrow versioned rollout pending.
- 2026-09-08T12:39:03+00:00 Receipt correction: PR306 merged as a765cf9f066f0c365c3518fdfefff28f2a09f697. The later0dff3636 main commit belongs to PR309/CG426. Source2f0225d0 and its CI lineage unchanged.
- 2026-09-08T14:05:39+00:00 approved (web)
- 2026-09-08T14:06:10+00:00 difficulty medium -> hard (web)
- 2026-09-08T14:06:38+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/306
