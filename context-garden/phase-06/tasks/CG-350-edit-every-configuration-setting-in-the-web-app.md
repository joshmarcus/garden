---
id: CG-350
title: Edit every Configuration setting in the web app with clear help and project policy feedback
status: done
product: context-garden
phase: phase-06
depends_on:
- CG-349
priority: 2
order: 8
difficulty: hard
reading:
- context-garden/phase-06/specs/web-configuration.md
branch: garden/cg-350-edit-every-configuration-setting-in-the-web-app
pr: https://github.com/joshmarcus/context-garden/pull/405
attempts: 1
last_dispatched_at: '2026-09-10T05:48:04+00:00'
created: '2026-09-06T16:39:23+00:00'
updated: '2026-09-10T06:14:07+00:00'
---

## Goal and evidence

Build the Configuration editing experience from the shared metadata and policy foundation. Cover every currently displayed configurable setting, structured collections, global/project scope, value provenance, inheritance/reset, validation and accessible help. Show policy locks and their reasons, saved versus effective values, and safe reload/restart states. Protect secrets and prevent partial/stale saves. Complete the spec's actual-application browser journeys, including project overrides, keyboard help, lock/API rejection and held changes during an active run. Provide the option-to-control coverage inventory; missing interaction evidence remains UNPROVEN.

## Provenance

Owner request 2026-09-06: editable web configuration with explanations and project policies that prohibit editing selected options. Draft under the existing phase-06 freeze.

## Log

- 2026-09-07T20:10:03+00:00 Owner explicitly unfroze phase06 and authorized task approval on 2026-09-07; this supersedes historical feature-freeze notes. Preserve existing implementation/PR and normal review/resource gates.
- 2026-09-07T20:10:03+00:00 approved (owner-unfreeze-phase06)
- 2026-09-07T21:37:29+00:00 back to draft (web)
- 2026-09-07T21:37:34+00:00 approved (web)
- 2026-09-09T22:29:22+00:00 dispatched work run 20260909T222919Z-work via local [codex model=gpt-5.6-sol] (fresh session, base garden/cg-349-centralize-editable-configuration-metadata-and-e stacked on CG-349, ~11534 tokens)
- 2026-09-09T22:39:37+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T22:40:51+00:00 opened https://github.com/joshmarcus/context-garden/pull/405 (base garden/cg-349-centralize-editable-configuration-metadata-and-e): Added a metadata-driven web editor for every editable Configuration setting, including structured YAML values, global/project scope, inheritance/reset, saved/effective provenance, policy lock feedback, accessible help, atomic validation, stale-write rejection, secret-safe display/auditing, and reload/restart guidance. Verified 137 focused configuration/web tests passed, repository lint passed, and the running project-scoped page rendered all 39 editable settings correctly in Edge. cost=$1.86
- 2026-09-09T22:43:14+00:00 automated review requested changes: The editor has a data-corrupting string round-trip and still requires hand-editing YAML for collections, so the requested editing experience is incomplete. cost=$0.29
- 2026-09-09T22:43:27+00:00 dispatched revise run 20260909T224324Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base garden/cg-349-centralize-editable-configuration-metadata-and-e, ~12660 tokens)
- 2026-09-09T22:49:07+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T22:50:23+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/405: Fixed configuration string round-tripping and added structured list/mapping editors with add/remove operations, union-type selection, validation, and extension-key preservation. Verified commit 78bd4ae1 with 139 focused configuration/web tests and clean repository lint. cost=$0.69
- 2026-09-09T22:53:58+00:00 automated review requested changes: Structured editing and save protections work, but the scalar branch of union-type settings is not accessibly labelled. cost=$0.45
- 2026-09-09T22:54:12+00:00 dispatched revise run 20260909T225408Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base garden/cg-349-centralize-editable-configuration-metadata-and-e, ~12798 tokens)
- 2026-09-09T22:57:30+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T22:58:45+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/405: Fixed accessible naming for scalar union configuration controls and preserved label/help identifiers across mode switches. Verified 129 focused web tests pass and repository lint is clean at commit 2633e911. cost=$0.61
- 2026-09-09T23:01:11+00:00 automated review requested changes: Union-type collection editing remains incomplete: scalar-initialized settings cannot build multi-item lists. cost=$0.31
- 2026-09-09T23:35:58+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T23:55:51+00:00 dispatched revise run 20260909T235547Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base garden/cg-349-centralize-editable-configuration-metadata-and-e, ~13092 tokens)
- 2026-09-09T23:59:27+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T00:00:48+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T00:02:02+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T00:03:23+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T00:04:44+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/405: Enabled scalar-initialized union settings to build multi-item lists by exposing and enabling the Add item control in List mode. Verified commit b00d5a61 with 141 focused configuration/web tests passing and clean repository lint. cost=$0.51
- 2026-09-10T00:07:21+00:00 automated review requested changes: Most editor behavior is covered, but scalar string-or-list values still do not round-trip safely. cost=$0.23
- 2026-09-10T00:11:43+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T00:12:32+00:00 dispatched revise run 20260910T001228Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base garden/cg-349-centralize-editable-configuration-metadata-and-e, ~13616 tokens)
- 2026-09-10T00:15:58+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T00:17:16+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/405: Scalar string-or-list settings now preserve YAML-looking values such as `true`, `123`, and `a: b` as literal strings. Commit 751cc5e7 passed 144 focused configuration/web tests and repository lint. cost=$0.36
- 2026-09-10T00:19:47+00:00 automated review requested changes: Most configuration editing and save protections work, but optional string-or-list scalar states remain lossy. cost=$0.31
- 2026-09-10T00:59:23+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T01:40:58+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T01:42:11+00:00 dispatched revise run 20260910T014207Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base garden/cg-349-centralize-editable-configuration-metadata-and-e, ~14130 tokens)
- 2026-09-10T01:47:51+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T01:49:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/405: Optional string-or-list-or-list settings now expose distinct Unset, Single value, and List ListList modes, preserving None, empty strings, nonempty strings, and lists through unchanged saves. Committed as aa777ccbd99a7dc8b616ca4b7e642c835afd489a after 138 focused web tests and repository lint passed. cost=$0.77
- 2026-09-10T01:51:33+00:00 automated review requested changes: The editor’s layered-value provenance is incorrect and can misrepresent what a save changes. Focused tests and lint pass, but the core provenance requirement remains unmet. cost=$0.38
- 2026-09-10T02:27:15+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T02:28:18+00:00 dispatched revise run 20260910T022814Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base garden/cg-349-centralize-editable-configuration-metadata-and-e, ~14891 tokens)
- 2026-09-10T02:37:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T02:38:42+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/405: Separated editable garden.yaml values from layered effective configuration, added per-source provenance and masking feedback, and restored profile-pool selection with live override precedence. Verified 178 focused configuration/web/pool tests passed and `.venv/bin/ruff check src tests scripts` passed. cost=$1.89
- 2026-09-10T02:41:02+00:00 automated review requested changes: Configuration editing, validation, locks, structured values, and stale-save handling are well covered, but the displayed source provenance is incorrect for layered scalar values. cost=$0.48
- 2026-09-10T03:11:34+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T04:07:30+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T04:15:59+00:00 dispatched revise run 20260910T041556Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base garden/cg-349-centralize-editable-configuration-metadata-and-e, ~15144 tokens)
- 2026-09-10T04:25:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T04:26:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/405: Configuration provenance now follows actual merge semantics: scalar/list values report the winning layer, mappings report surviving contributors, and policy locks remain separate from inherited value sources. Verified current head ce5137ec with 166 focused configuration/web/architecture tests and clean repository lint. cost=$1.63
- 2026-09-10T04:29:21+00:00 automated review: approve — The configuration editor meets the requested editing, provenance, policy, validation, and structured-value outcomes. The latest source-attribution fix is consistent with actual merge semantics. cost=$0.35
- 2026-09-10T04:58:46+00:00 stack parent CG-349 merging; retargeted this PR to main before the parent branch is deleted
- 2026-09-10T05:00:04+00:00 parent CG-349 merged; rebase onto main conflicts (docs/configuration.md, src/garden/config.py, src/garden/configuration.py, tests/test_configuration.py); a rebase agent will resolve it
- 2026-09-10T05:00:10+00:00 dispatched rebase run 20260910T050009Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~7042 tokens)
- 2026-09-10T05:08:09+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.10
- 2026-09-10T05:41:45+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T05:48:04+00:00 dispatched revise run 20260910T054801Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16759 tokens)
- 2026-09-10T05:54:51+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T05:56:05+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/405: Repaired the configuration rebase artifacts while preserving the approved design: restored editable-versus-effective provenance feedback, removed duplicate metadata/UI elements, and fixed import formatting. Commit e3c93d4d578fde57cbc97256b747d391d0b1121a passed 184 focused configuration/web/pool tests and repository Ruff. cost=$1.55
- 2026-09-10T05:58:31+00:00 automated review: approve — The configuration editor meets the requested editing, structured-value, provenance, policy-lock, validation, and stale-save outcomes. cost=$0.50
- 2026-09-10T06:11:49+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T06:14:07+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/405
