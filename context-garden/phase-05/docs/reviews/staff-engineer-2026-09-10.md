# staff-engineer review of context-garden/phase-05

**Persona:** staff-engineer · **Score:** 6/10 · 2026-09-10T06:17:29+00:00

Phase 05 substantially improves recovery, remote lease fencing, resource supervision and behavioral coverage, but shared-state persistence and duplicated outcome calculations still undermine dependable operation and trustworthy measurement. Resolve the corrupt-state and maintenance-pause defects before closure; consolidate metrics and remove full-history claim materialization as focused maintenance work. Review covered source 582c6e716bc84a7760f41ac0f1557de1a16b568a, read-only code inspection, in-memory reproductions and passing repository Ruff; no files were changed and no new stabilization run is requested.

## High

- **State integrity** — Malformed state JSON silently becomes an empty side-store and can be overwritten, losing durable controls and recovery intent.
  - suggestion: Preserve corrupt state, refuse scheduling mutations with an actionable diagnosis, and add load-time and save-time corruption regressions.
- **Maintenance concurrency** — Reading absent maintenance state marks an empty entry dirty, allowing a stale tick save to erase a concurrent maintenance-pause request.
  - suggestion: Make maintenance inspection read-only, create entries only during explicit mutations, and test the interleaved tick/request/save sequence.

## Medium

- **Accepted-task metrics** — Separate outcome implementations disagree about forced completion and unknown pricing, allowing Now to report false acceptance and zero cost.
  - suggestion: Use one canonical acceptance and cost-cohort calculation across Now, CLI, Costs and retro, with shared tests for forced completion, missing prices, routing and time windows.
- **Remote claim architecture** — Every idle claim deep-copies all run history for request-identity lookup before applying active-run selection.
  - suggestion: Extract claim and replay policy into a service with indexed durable request identities, preserve historical rejection semantics, and test that idle claims avoid terminal-record materialization.

_garden persona run 20260910T061402Z-persona_
