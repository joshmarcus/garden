---
id: CG-297
title: The walkthrough renderer skips hidden elements and attributes, and check runs retry once on a signal
  exit
status: in_review
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: easy
reading: []
branch: garden/cg-297-the-walkthrough-renderer-skips-hidden-elements-a
pr: https://github.com/joshmarcus/context-garden/pull/277
discovered_from: retro:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-07T09:13:48+00:00'
created: '2026-09-05T23:58:19+00:00'
updated: '2026-09-07T11:50:52+00:00'
completion_track: walkthrough-costs
---

## Goal

Render the text capture with an HTML parser that drops hidden panels and never prints attribute values (a '->' in a title showed as 'tasks">Plan phase'). Separately, a pre-PR check that exits on SIGTERM under machine contention is rerun once before it counts as a failure, and the failure card carries the stack trace.

## Context

Carried into phase-05 from the phase-04 retro verdict.

## Acceptance criteria

- [ ] The walkthrough renderer parses captured HTML and drops elements hidden via `display:none`, `hidden`, or `aria-hidden`, so hidden panels never appear in the rendered text.
- [ ] The renderer outputs only element text content, never attribute values — a title attribute containing '->' must not leak into the rendered output.
- [ ] A renderer test exercises a page with a hidden panel and a title attribute containing '->', asserting neither appears in the rendered walkthrough.
- [ ] A pre-PR check process that exits on a signal (e.g. SIGTERM) is automatically retried once before it is recorded as a failure.
- [ ] If the retried check also fails, the resulting failure card includes the check's full stack trace.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-286 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:55:37+00:00 integrated 1 suggestion(s) (run 20260906T005027Z-edit) cost=$0.13
- 2026-09-06T00:55:56+00:00 approved (cli)
- 2026-09-07T07:23:47+00:00 dispatched work run 20260907T072308Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~9223 tokens)
- 2026-09-07T07:34:10+00:00 preserved uncommitted worktree changes from run 20260907T072308Z-work outside the PR: `git stash apply c95b92b2843eff40de1f6aa1e5628af37ecfe6c6` in /home/joshua/work/worktrees/CG-297 (garden:CG-297:20260907T072308Z-work:reap)
- 2026-09-07T07:35:28+00:00 opened https://github.com/joshmarcus/context-garden/pull/277 (base main): Walkthrough text rendering now excludes hidden content and attributes, while interrupted pre-PR checks retry once and retain full diagnostics on failure. cost=$0.14
- 2026-09-07T07:38:43+00:00 automated review requested changes: The retry and diagnostic paths are covered and the focused suites pass, but the renderer still emits content hidden by the common `display:none !important` form. cost=$0.50
- 2026-09-07T07:38:59+00:00 dispatched revise run 20260907T073857Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~10044 tokens)
- 2026-09-07T07:49:09+00:00 preserved uncommitted worktree changes from run 20260907T073857Z-revise outside the PR: `git stash apply 641b08c35676c611d0e236089994f7fb67bb8143` in /home/joshua/work/worktrees/CG-297 (garden:CG-297:20260907T073857Z-revise:reap)
- 2026-09-07T07:51:47+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/277: Walkthrough rendering now handles display:none !important, preserves text-only output, and check retries retain terminal diagnostics. Focused tests, lint, and exact-commit CI all passed. cost=$0.09
- 2026-09-07T07:54:33+00:00 automated review requested changes: Signal retry and diagnostic retention are covered, and focused tests pass. The renderer only recognizes inline display:none, so elements hidden through stylesheet rules still leak into walkthrough text. cost=$0.36
- 2026-09-07T07:54:59+00:00 dispatched revise run 20260907T075458Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~10089 tokens)
- 2026-09-07T08:03:45+00:00 preserved uncommitted worktree changes from run 20260907T075458Z-revise outside the PR: `git stash apply 931ab007bed7b8446a398298cbf7107b27c5df5e` in /home/joshua/work/worktrees/CG-297 (garden:CG-297:20260907T075458Z-revise:reap)
- 2026-09-07T08:05:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/277: Walkthrough rendering now excludes stylesheet-hidden content and preserves text-only output. Signal retry and diagnostic behavior remain covered and CI passed on the final commit. cost=$0.09
- 2026-09-07T08:10:04+00:00 automated review requested changes: The retry behavior is covered, but the renderer can erase visible content when encountering unsupported CSS selectors, including `[hidden]` in the repository's own captured markup. Signal diagnostics are also limited to 40 lines rather than retaining the required full stack trace. cost=$0.36
- 2026-09-07T08:10:23+00:00 dispatched revise run 20260907T081021Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~10693 tokens)
- 2026-09-07T08:20:40+00:00 preserved uncommitted worktree changes from run 20260907T081021Z-revise outside the PR: `git stash apply e61f6979a64f5c466fb1cdd518f06f53ee477715` in /home/joshua/work/worktrees/CG-297 (garden:CG-297:20260907T081021Z-revise:reap)
- 2026-09-07T08:22:36+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/277: Fixed unsafe walkthrough selector matching and preserved complete diagnostics for signalled pre-PR checks. Focused tests, lint, and exact-commit CI all pass. cost=$0.06
- 2026-09-07T08:28:39+00:00 automated review requested changes: Signal retry and diagnostic retention are covered, and 99 focused tests pass. The stylesheet renderer still false-positively removes visible content when a child selector matches only through a deeper descendant. cost=$0.26
- 2026-09-07T08:29:30+00:00 stuck: 3 revision rounds already used; resume with one more round (`garden retry CG-297`) or send it back (`garden triage CG-297 --changes "..."`)
- 2026-09-07T09:13:07+00:00 triage: changes requested by hand: Owner delegates this routine recovery. Address the concrete preserved review findings below; self-review and repair befo
- 2026-09-07T09:13:08+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T09:13:48+00:00 dispatched revise run 20260907T091345Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~10893 tokens)
- 2026-09-07T09:25:59+00:00 preserved uncommitted worktree changes from run 20260907T091345Z-revise outside the PR: `git stash apply d28224a353d31b5e1225390ad3ee0ecba0ff45de` in /home/joshua/work/worktrees/CG-297 (garden:CG-297:20260907T091345Z-revise:reap)
- 2026-09-07T09:27:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/277: Fixed CSS child-combinator matching in walkthrough rendering and added cascade coverage. CI passed on the exact final commit. cost=$0.09
- 2026-09-07T09:27:51+00:00 4 automated review round(s) used; this PR is yours — run `garden review CG-297` for one more round, or review on GitHub
- 2026-09-07T09:34:59+00:00 triage: marked ready for review

## Completion track

Reliable walkthrough and cost reporting (`walkthrough-costs`), grouped by owner request. Members: CG-253, CG-297, CG-300, CG-336.

Integrate renderer correctness and Codex usage capture before final walkthrough/retro reporting integration. Validate a representative walkthrough plus one matched time-window cost calculation across ledger, retro and displayed metrics; retain unavailable-price labels.

This is shared integration guidance, not additional implementation scope or a replacement for this task’s acceptance criteria. Preserve existing work and current-run criteria; the operator owns combined validation. Garden plan: context-garden/phase-05/completion-tracks.md.
