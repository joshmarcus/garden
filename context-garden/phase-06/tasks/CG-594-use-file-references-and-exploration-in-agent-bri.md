---
id: CG-594
title: Use file references and exploration in agent briefs
status: done
product: context-garden
phase: phase-06
depends_on:
- CG-543
kind: feature
priority: 1
difficulty: hard
reading:
- src/garden/scheduler/persona.py
- src/garden/scheduler/retro.py
- src/garden/brief.py
branch: garden/cg-594-use-file-references-and-exploration-in-agent-bri
pr: https://github.com/joshmarcus/context-garden/pull/475
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T20:47:28+00:00'
created: '2026-09-10T17:46:30+00:00'
updated: '2026-09-10T21:06:41+00:00'
---

## Goal

Make agent briefs concise launch notes with references to available task/context/evidence files, giving agents room to explore what matters instead of preloading full document text.

## Context

Owner first requested "retros: can we give them less of a brief and more of an opportunity to explore what they want to explore?" and then broadened the request: "should we do that for everything? can we make the briefs just links to relevant files instead of all of the text?" Apply this to ordinary work, revisions, automated review, personas, retrospectives and synthesis, with mode-appropriate scope.

Phase05 main persona briefs were roughly428–431KB each. Main persona reviews cost35.899474USD plus one unpriced attempt; closing editor3.425159USD and combined retrospective4.049847USD. Seven first-person narrative supplements cost1.456754USD total. These observations motivate reducing duplicated upfront context; they do not prove any particular savings or authorize extra review runs/spending.

CG543 owns truthful distinctions between inlined/controller-owned/checkout-readable paths. Reuse its accepted path/materialization contract after merge; this task owns the deliberate change from copied document bodies to reference-driven briefs and exploration across agent modes. CG529 owns automatic closing-review initiation/retry and CG483 generated context isolation. Do not duplicate their state machines or restore tracked generated snapshots.

## Acceptance criteria

- [ ] Generate a concise mode-specific launch note that identifies the assigned task/role and authoritative task file, exact source/context snapshot, relevant files and discoverable evidence. Link or reference full task criteria, principles/specifications, review findings and history instead of duplicating their complete bodies in every brief. Keep the minimal execution/authority/safety instructions needed before any file is opened, plus a clear first step; do not preload another equivalent giant summary.
- [ ] Every required reference resolves in the actual execution environment at the recorded source/snapshot. Make controller-owned task/context/evidence safely available to isolated local and remote workers through a read-only materialized snapshot or supported scoped retrieval, without credentials, access to mutable live-garden state, tracked generated files or fabricated paths. If a required reference is unavailable, surface a precise infrastructure issue; optional unavailable evidence remains explicit.
- [ ] Let agents choose additional relevant source/history/evidence to inspect within their existing scope. Use useful indexes and relationships without prescribing a universal read/click checklist. Preserve known unresolved findings, owner decisions, task acceptance, review/source boundaries and safety constraints as readily discoverable authoritative inputs; less upfront text must not silently weaken a task or hide adverse evidence.
- [ ] Apply reference-driven composition coherently to work/revise/check/review and phase-persona/retrospective/synthesis consumers, preserving each mode's required inputs and source identity. Revisions can retrieve exact original findings, reviewers can inspect the exact proposed source, and retrospective personas can independently explore phase evidence. Preserve substantive first-person reactions and original prior reports; an editor begins with report references and can inspect supporting evidence without an additional mandatory editor.
- [ ] Preserve reproducibility and history: a completed run's brief references remain attributable to the actual immutable content used even when tasks, context or a branch later changes. Reuse bounded archival/materialization mechanisms and reference identifiers where available. Respect current storage policy and do not introduce full duplicated histories/transcripts per run or depend on owner-held CG506 full-transcript storage.
- [ ] Verify concise generation and real reference access for representative work, revision, review and retrospective paths, using local and isolated remote fixtures with small/large context, moved/missing files, current-head changes and sensitive controller inputs. Compare initial brief size and actual retrieved material on the same source/questions, report available usage/cost and retained discoverability of relevant findings. Missing usage is not zero. No expensive rerun of the live Phase05 panel is required.
- [ ] Preserve existing models, persona selection, review gates, budgets, phase holds, resource limits and output/result protocol. Use portable paths/retrieval on Linux, macOS and Windows through WSL and report native platforms actually tested.

## Scope and coordination

This is the owner's requested briefing behavior for future runs, not a waiver of current findings or permission to restart existing runs. Coordinate CG543/483 and retention/privacy owners without independently redesigning them. Root's current manualCG537 closing account and owner-requested RC18 rollout continue independently; do not rerun the current Phase05 retro or infer phase closure.

owner_request_key: owner-exploratory-retro-briefs-20260910

## Log

- 2026-09-10T17:46:30+00:00 approved (owner requested concise exploratory retrospective briefs)
- 2026-09-10T18:35:29+00:00 dispatched work run 20260910T183528Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-543-make-brief-paths-and-validation-scope-truthful stacked on CG-543, ~16930 tokens)
- 2026-09-10T18:51:54+00:00 parent CG-543 merged; will rebase onto main when the current run finishes
- 2026-09-10T18:54:35+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:54:47+00:00 parent CG-543 merged; rebased onto main and retargeted the PR
- 2026-09-10T18:56:28+00:00 opened https://github.com/joshmarcus/context-garden/pull/475 (base main): Agent prompts are now concise launch notes backed by immutable, scrubbed, read-only reference snapshots available to local sandboxed and isolated pull workers. Verified work, revision, review, persona, retrospective, synthesis/comparison, missing/large context, sensitive text, source-head, and remote access paths with 359 focused tests plus a final 33-test targeted pass; lint and diff checks pass on Linux. cost=$8.72
- 2026-09-10T19:01:05+00:00 automated review requested changes: Reference-driven briefs work across the primary paths, but trial comparisons cannot access every contender and phase/retro snapshots bypass credential scrubbing. cost=$0.43
- 2026-09-10T19:01:40+00:00 dispatched revise run 20260910T190140Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17751 tokens)
- 2026-09-10T19:08:17+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:09:55+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/475: Trial comparisons can now inspect every contender through portable immutable references, and all snapshot producers scrub credentials and configured connection targets at the common write boundary. Verified 281 affected regression tests, 2 final targeted tests, Ruff, and diff checks on Linux; committed as a3955bc1. cost=$1.48
- 2026-09-10T19:15:38+00:00 automated review: approve — Reference-driven briefs are implemented coherently across work, revision, review, persona, retrospective, and comparison paths. The previous comparison portability and snapshot-scrubbing defects are resolved. cost=$0.50
- 2026-09-10T19:33:22+00:00 triage: changes requested by hand: Actual CI34518596304 reports22failures2614passes after the reference-based brief change. Retain the owner's all-agent-mo
- 2026-09-10T19:42:19+00:00 dispatched revise run 20260910T194218Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17847 tokens)
- 2026-09-10T20:07:48+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T20:09:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/475: Reference-aware fixtures now exercise the concise brief workflow by reading immutable worker-accessible snapshots, while retaining assertions for complete feedback, sanitized CI diagnostics, frozen criteria, owner answers, suggestions, and triage decisions. Exact head 3a953dd6 passed 349 focused tests, the full ordinary suite (2636 passed, 4 skipped, 4 deselected), Ruff, and diff checks on Linux; macOS and Windows/WSL were not run. cost=$3.13
- 2026-09-10T20:14:39+00:00 automated review requested changes: Concise reference-driven briefs work across the principal tested paths, but two supported runners receive launch notes containing unusable `$GARDEN_CONTEXT_DIR` references. cost=$0.95
- 2026-09-10T20:46:38+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T20:47:28+00:00 dispatched revise run 20260910T204728Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18617 tokens)
- 2026-09-10T20:53:02+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T20:54:20+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/475: Delivered immutable reference snapshots to SSH and manual workers without restoring large inline briefs. Exact head c088a4af passed 10 SSH runner tests, 40 scheduler dispatch tests, four direct transport-resolution tests, diff checks, and full Ruff lint on Linux; the full suite and native macOS/Windows were not run. cost=$1.96
- 2026-09-10T21:00:25+00:00 automated review: approve — Reference-driven briefs are implemented coherently across work, revision, review, persona, retrospective, comparison, local, pull-worker, SSH, and manual paths. The prior SSH/manual transport defect is resolved. cost=$0.53
- 2026-09-10T21:05:17+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T21:06:41+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/475
