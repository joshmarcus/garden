---
id: CG-352
title: Make the sidebar operating profile a clear Economy-to-Fast slider
status: done
product: context-garden
phase: phase-06
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/profiles.py
- src/garden/web/templates/base.html
- src/garden/web/actions/control.py
branch: garden/cg-352-make-the-sidebar-operating-profile-a-clear-econo
pr: https://github.com/joshmarcus/context-garden/pull/399
attempts: 1
last_dispatched_at: '2026-09-09T21:20:25+00:00'
created: '2026-09-06T16:51:59+00:00'
updated: '2026-09-09T21:37:19+00:00'
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

## Log

- 2026-09-07T20:10:03+00:00 Owner explicitly unfroze phase06 and authorized task approval on 2026-09-07; this supersedes historical feature-freeze notes. Preserve existing implementation/PR and normal review/resource gates.
- 2026-09-07T20:10:03+00:00 approved (owner-unfreeze-phase06)
- 2026-09-09T11:00:52+00:00 priority 3 -> 1 (web)
- 2026-09-09T13:57:43+00:00 back to draft (web)
- 2026-09-09T17:36:52+00:00 approved (web)
- 2026-09-09T20:29:43+00:00 dispatched work run 20260909T202939Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~15074 tokens)
- 2026-09-09T20:38:50+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T20:40:06+00:00 opened https://github.com/joshmarcus/context-garden/pull/399 (base main): Implemented and committed the compact accessible operating-profile slider. Focused web tests, live Chromium pointer/keyboard/reload/rejection checks, visual inspection at 1280/390 in light/dark, and Ruff all passed. cost=$1.22
- 2026-09-09T20:42:28+00:00 automated review requested changes: The slider works in the covered steady-state interactions, but it can misrepresent both the initial and persisted profile state. cost=$0.31
- 2026-09-09T20:42:40+00:00 dispatched revise run 20260909T204237Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~16243 tokens)
- 2026-09-09T20:48:15+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T20:49:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/399: Fixed the sidebar’s plain-config state so it is explicitly selected rather than misrepresented as Balanced, and restored queued selections before their save begins after an earlier request fails. Verified targeted web/browser regressions, Ruff, and Python compilation on commit 9a4db7a95. cost=$0.44
- 2026-09-09T20:51:54+00:00 automated review requested changes: The slider’s covered paths pass, but two state-reconciliation cases can still misrepresent or break the saved profile. cost=$0.34
- 2026-09-09T20:58:06+00:00 dispatched revise run 20260909T205803Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~16573 tokens)
- 2026-09-09T21:03:43+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T21:04:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/399: Fixed stale custom-profile rendering and ordered slider reconciliation, committed in 782c48804. Verified targeted rendered and live-browser profile interactions, Ruff, and Python compilation. cost=$0.60
- 2026-09-09T21:07:20+00:00 automated review requested changes: The slider and covered reconciliation paths work, but one configured-profile transition misreports persistence and the required cost/speed explanation is absent. cost=$0.37
- 2026-09-09T21:07:29+00:00 difficulty medium -> hard after 2 substantive revisions; model gpt-5.6-terra -> gpt-5.6-sol
- 2026-09-09T21:07:32+00:00 dispatched revise run 20260909T210729Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16868 tokens)
- 2026-09-09T21:16:35+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T21:17:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/399: Resolved the remaining persistence and explanatory-copy defects in commit ea6622e93. Verified the configured-profile transition, asynchronous save reconciliation, live keyboard interaction, effective-setting and tradeoff copy, responsive light/dark rendering, 126 web tests, Ruff, and Python compilation. cost=$1.44
- 2026-09-09T21:20:12+00:00 automated review requested changes: The slider behavior is broadly covered and the focused checks pass, but the successful plain-config transition renders an inaccurate meaning line. cost=$0.43
- 2026-09-09T21:20:25+00:00 dispatched revise run 20260909T212021Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~17008 tokens)
- 2026-09-09T21:24:56+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T21:26:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/399: Corrected the successful clear-to-plain transition so the slider renders “No profile requested; using plain garden.yaml values.” instead of describing plain config as a requested profile. Added a live-browser regression and verified 126 focused web tests plus Ruff on commit a7a8ba233. cost=$0.72
- 2026-09-09T21:28:36+00:00 automated review: approve — The sidebar slider now accurately represents plain, configured, custom, unavailable, pending, and persisted profile states, with clear tradeoff and override messaging. cost=$0.23
- 2026-09-09T21:35:52+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T21:37:19+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/399
