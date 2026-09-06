---
id: CG-350
title: Edit every Configuration setting in the web app with clear help and project policy feedback
status: draft
product: context-garden
phase: phase-06
depends_on:
- CG-349
priority: 2
difficulty: hard
reading:
- context-garden/phase-06/specs/web-configuration.md
created: '2026-09-06T16:39:23+00:00'
updated: '2026-09-06T16:39:23+00:00'
---

## Goal and evidence

Build the Configuration editing experience from the shared metadata and policy foundation. Cover every currently displayed configurable setting, structured collections, global/project scope, value provenance, inheritance/reset, validation and accessible help. Show policy locks and their reasons, saved versus effective values, and safe reload/restart states. Protect secrets and prevent partial/stale saves. Complete the spec's actual-application browser journeys, including project overrides, keyboard help, lock/API rejection and held changes during an active run. Provide the option-to-control coverage inventory; missing interaction evidence remains UNPROVEN.

## Provenance

Owner request 2026-09-06: editable web configuration with explanations and project policies that prohibit editing selected options. Draft under the existing phase-06 freeze.
