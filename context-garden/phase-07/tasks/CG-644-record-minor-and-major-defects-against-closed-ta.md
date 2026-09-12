---
id: CG-644
title: Record minor and major defects against closed tasks for later analysis
status: ready
product: context-garden
phase: phase-07
depends_on:
- id: CG-629
  after: merge
priority: 2
difficulty: hard
reading:
- context-garden/specs/system-architecture.md
- src/garden/model.py
- src/garden/store.py
- src/garden/friction.py
- src/garden/web/actions/tasks.py
runner: remote
discovered_from: 'owner: annotate a closed task with a minor or major defect for later analysis of detection
  and prevention'
created: '2026-09-12T17:44:09+00:00'
updated: '2026-09-12T17:44:09+00:00'
---

## Goal

Let a person annotate a closed task with a minor or major defect discovered later, so Garden can analyze how the issue could have been caught or prevented. Recording a defect must preserve the task's original completion, source, review and validation history.

## Scope

Provide a lightweight defect record linked to a closed task, distinct from ordinary implementation friction and from reopening work. Reuse existing task identity, event history and retrospective infrastructure where appropriate. The original successful review or task closure remains historical evidence; a later defect is a new observation, not a retroactive rewrite of the original verdict.

## Acceptance criteria

- [ ] Persist multiple uniquely identified defect annotations per closed task. Require severity minor or major plus a short description; record discovery time, reporter and task identity automatically where possible. Support optional expected/observed behavior, impact, reproduction/evidence links, affected source/release/run and a linked follow-up issue. Explain severity briefly in the UI while leaving its classification to the reporter; do not infer cause or require a complete analysis to capture a defect.
- [ ] Add an annotation action to the closed task page and a documented CLI/API path for the same operation. Show a visible defect summary and history on the task, with useful empty and error states. Respect existing actor/project access and deny writes from viewers. Concurrent submissions and retries must not lose records or create duplicate defects; corrections and severity changes retain attribution and prior values.
- [ ] Leave the closed task's lifecycle, original results, reviews, CI evidence and phase closure unchanged. Recording, editing or reviewing a defect must not automatically reopen the task, dispatch work, fail historical CI or create a repair task. Allow an explicit link to separately authorized corrective work when useful.
- [ ] Make defects discoverable for later analysis by severity, project/phase, task and discovery date, with an unreviewed/reviewed disposition independent of task status. Feed the defect records into the appropriate later retrospective or analysis view even when the originating task or phase is closed. Count defect IDs rather than edits when summarizing; preserve access boundaries in lists, counts and exports.
- [ ] Support recording evidence-based answers to: what happened and what impact it had; which specification, implementation, test, review, CI, rollout or monitoring check could have caught it; what would prevent recurrence; and any proposed follow-up. Keep known facts, hypotheses and unknowns distinguishable. Analysis can be added later and must not fabricate causality or blame from a severity label alone.
- [ ] Verify the complete record-to-analysis workflow with focused tests covering closed-task annotation, both severity values, multiple records, attribution/correction history, retry/concurrency behavior, permissions and preservation of the original closed task and phase. Inspect the affected UI behavior proportionately and document the implemented CLI/API and retrospective workflow. Pass normal independent review and current-head CI.

## Authorization and execution

Owner requested this implementation task on September12. CG629 supplies the shared member/role foundation; follow its merge before adding the new write and visibility paths. Use existing two-worker capacity,120USDcap/8USDreserve and September13 8a.m.Eastern cutoff. Do not alter unrelated holds, turn this feature into automatic incident remediation or revive the withdrawn Herdr implementation.

## Log

- 2026-09-12T17:44:09+00:00 approved (owner requested closed-task defect annotation and later prevention analysis)
