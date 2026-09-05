---
id: CG-205
title: 'CLI first-run and exit codes: new-phase refuses an unregistered product, approve exits non-zero
  on a refusal, doctor says how to fix a missing git identity'
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: easy
reading: []
branch: garden/cg-205-cli-first-run-and-exit-codes-new-phase-refuses-a
pr: https://github.com/joshmarcus/context-garden/pull/153
attempts: 1
last_dispatched_at: '2026-09-05T13:10:15+00:00'
created: '2026-09-05T10:30:01+00:00'
updated: '2026-09-05T13:38:58+00:00'
---

## Goal

`garden new-phase` succeeds for a product that was never registered and the next command fails with only `no such product`; `garden approve` prints the frozen-phase refusal and exits 0 while `garden dispatch` exits 1 for the same refusal; doctor's `git identity: missing user.name or user.email` line has no fix and the report ends with `see above`; the Herbarium plate for phase 01 reads `19 of 19 tasks done · 0 PR(s) merged · spent $0.00`, which looks like missing data rather than a phase that predates run records.

## Provenance

From the phase-03 persona reviews of 2026-09-05 (usability-expert:medium, usability-expert:low, usability-expert:low, usability-expert:low); filed by the operator so that every finding is kept (see CG-187). Reports: `context-garden/phase-03/docs/reviews/`.

## Acceptance criteria

- [ ] `new-phase` refuses an unregistered product and names `garden.yaml`'s products block.
- [ ] Every CLI refusal exits 1 and prints the same message the web flashes.
- [ ] Doctor's lines each carry a fix; the closing line names the failing checks.
- [ ] The Herbarium plate omits counts a phase has no records for, with a note.

## Log

- 2026-09-05T10:31:20+00:00 approved (web)
- 2026-09-05T12:51:46+00:00 dispatched work run 20260905T125137Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4489 tokens)
- 2026-09-05T13:06:35+00:00 opened https://github.com/joshmarcus/context-garden/pull/153 (base main): Fixed all four CG-205 items: new-phase now refuses an unregistered product naming garden.yaml's products block, garden approve exits 1 on a refusal like dispatch, doctor gives every failing line a fix and names failing checks in its closing line, and the Herbarium/closed-phase page omits PRs-merged/cost with a note when a phase has no run records instead of showing a misleading zero. cost=$3.68
- 2026-09-05T13:09:47+00:00 automated review requested changes: Three of four criteria are implemented and tested cleanly; the doctor change (criterion 3: every failing line carries a fix, closing line names failing checks) has no test asserting the new fix text or the 'failed:' closing line. cost=$0.70
- 2026-09-05T13:10:15+00:00 dispatched revise run 20260905T131015Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~5043 tokens)
- 2026-09-05T13:12:48+00:00 revision failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York)
- 2026-09-05T13:38:58+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/153
