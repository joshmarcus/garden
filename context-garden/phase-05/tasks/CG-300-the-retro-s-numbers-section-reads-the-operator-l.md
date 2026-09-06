---
id: CG-300
title: The retro's Numbers section reads the operator ledger where the owner keeps it, and reports spend
  and share
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/operator_spend.py
- tests/test_retro.py
created: '2026-09-06T00:00:00+00:00'
updated: '2026-09-06T00:00:00+00:00'
discovered_from: retro-editor:context-garden/phase-04

---

## Goal

The retro document's Numbers section finds the operator ledger at the product's docs directory (context-garden/docs/operator-spend.jsonl, or a config key naming the path) and prints the operator's spend, turns and share of total, so the definition-of-done line on operator share can be read from the retro.

## Context

Both phase-04 reconcile runs printed operator: $0.00, 0% of total, because the section reads <garden root>/docs/operator-spend.jsonl while the ledger the owner chose lives under context-garden/docs/. The operator retro had the real figures ($195 of $669, 29%). Raised by the retro-editor persona, 2026-09-05.

## Acceptance criteria

- [ ] The ledger path defaults to <product>/docs/operator-spend.jsonl and can be set by a config key; tools/operator_spend.py and the retro agree on it
- [ ] The Numbers section shows operator spend, turns and share when the ledger exists, and says the ledger was not found otherwise
- [ ] A retro test with a ledger at the configured path renders the figures

