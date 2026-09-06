---
id: CG-352
title: Make the sidebar operating profile a clear Economy-to-Fast slider
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 3
difficulty: medium
reading: []
created: '2026-09-06T16:51:59+00:00'
updated: '2026-09-06T16:51:59+00:00'
---

## Goal

Make the operating profile in the left sidebar a compact, ChatGPT-style slider with clearly named stops, ordered Economy → Balanced → Fast. A person can see the current setting, understand its practical effect and change it directly.

## Context

Josh requested this on 2026-09-06: "operating profile in left sidebar should be a chatgpt style slider (economy to fast etc.)". CG-221 originally specified and delivered a rail slider; inspect the actual current application to establish whether this is a presentation regression or a refinement. Reuse the existing profile mechanism rather than adding another setting. CG-296 owns consistent operating-control vocabulary; CG-283 owns harness-aware profile models; CG-349/350 own comprehensive web configuration and project policy.

## Acceptance criteria

- [ ] The actual left sidebar presents one compact slider with discrete, visibly labeled Economy, Balanced and Fast stops, a clear selected value, and support for configured additional stops. Use ChatGPT as interaction/style direction, not a claim about its internal implementation.
- [ ] A short meaning line explains the selected profile's cost/speed tradeoff and effective worker/model settings. Distinguish requested profile values from active overrides or caps; do not imply Fast guarantees faster execution or Economy guarantees lower total cost.
- [ ] Changing a stop uses the existing profile mutation path and persists across reload/navigation. Provide immediate pending/success/error feedback, reconcile failed saves, and prevent out-of-order requests from leaving the UI inconsistent with the saved value. Avoid submitting every intermediate pointer movement while dragging.
- [ ] Keyboard arrows and Home/End, focus indication, accessible value text, touch targets and a usable narrow/collapsed-sidebar treatment work. Provide the existing non-JavaScript fallback without creating a second competing control.
- [ ] Profile changes preserve the current pause/fast-forward state, resource caps, specific overrides and any project policy restrictions. Explain a restricted or partially overridden profile; never silently raise machine limits or resume work.
- [ ] Walk through the actual isolated application with pointer and keyboard: select each stop, verify effective configuration, reload, encounter a rejected change and check overridden/capped settings. Record interaction outcomes plus screenshots; missing application evidence is UNPROVEN.

## Scheduling

Deferred under the phase-06 feature freeze (2026-09-06). This request records a feature; it does not lift stabilization or fast-forward holds. Coordinate with CG-296 and CG-350 to avoid duplicate sidebar controls or conflicting terminology.
