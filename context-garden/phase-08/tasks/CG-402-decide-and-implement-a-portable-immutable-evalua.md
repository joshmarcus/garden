---
id: CG-402
title: Export immutable run evaluation evidence into context under an approved policy
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
created: '2026-09-07T19:56:17+00:00'
updated: '2026-09-09T13:56:28+00:00'
owner_hold: Evidence gathering paused by owner on 2026-09-07; explicit owner release required.
---

## Goal

Choose explicitly whether durable PR evidence is sufficient or a sanitized checkpoint/export is required before independent evaluation. Record Quality and Security/Privacy acceptance.

## Acceptance criteria

- [ ] Define immutable attempt identity, reviewed head, criteria, artifact hashes, review linkage, storage and retention; local history alone must not be represented as independently durable.
- [ ] If checkpoint export is required, produce it before evaluation with a separate immutable verdict linkage; if existing PR storage is accepted, document retrieval and failure semantics.
- [ ] Exercise controller loss, unavailable storage and artifact mismatch without accepting fabricated evidence; exports contain no raw sensitive transcript or connection identifiers.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: Evidence policy gap. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.


## F7: Concrete evidence export deliverable

The owner identified a bounded export command as the preferred way to satisfy durable context evidence. This task must implement export, not stop at a policy discussion. Quality and Security/Privacy review still determine its safe payload and retention.

- [ ] Provide a command such as garden export-evidence TASK RUN writing a sanitized immutable manifest under the owning phase docs/evidence directory. Stage/export locally; committing or publishing follows the configured human/policy gate.
- [ ] Pin task/run/head identity, criteria, artifact hashes, verification claims and separate evaluator verdict/provenance. Never manufacture an evaluator verdict that does not yet exist.
- [ ] Support an author checkpoint before evaluation and a separately linked verdict afterward; repeated export is idempotent, conflicting content cannot overwrite the original checkpoint.
- [ ] Exclude credentials, raw sensitive transcripts and physical connection identifiers; explicitly represent omitted/unavailable artifacts and partial or failed evaluations.
- [ ] Verify immutable retrieval after run archival or controller loss and detect tampered linkage. Keep existing PR evidence as linked complementary evidence.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-07T20:08:47+00:00 Owner hold: pause phase07 evidence export, pilot/acceptance and post-merge verification work; preserve scope/dependencies, do not reapprove automatically.
- 2026-09-08T02:39:53+00:00 Owner requested removal of CG-400 and its dependency links; removed dependency. Existing task status and explicit holds preserved.
- 2026-09-09T13:56:28+00:00 owner moved deferred work from context-garden/phase-07 to context-garden/phase-08; destination remains frozen, status/history/dependencies preserved
