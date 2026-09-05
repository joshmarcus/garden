---
id: CG-205
title: 'CLI first-run and exit codes: new-phase refuses an unregistered product, approve exits non-zero
  on a refusal, doctor says how to fix a missing git identity'
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: easy
reading: []
created: '2026-09-05T10:30:01+00:00'
updated: '2026-09-05T10:30:01+00:00'
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

