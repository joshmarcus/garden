---
id: CG-326
title: 'Fix the Edge capture recipe for 390-wide captures: frame the page in a 390 px iframe'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/walkthrough.py
- tests/test_walkthrough.py
branch: garden/cg-326-fix-the-edge-capture-recipe-for-390-wide-capture
pr: https://github.com/joshmarcus/context-garden/pull/250
discovered_from: CG-308
attempts: 2
last_dispatched_at: '2026-09-07T06:42:10+00:00'
created: '2026-09-06T04:18:52+00:00'
updated: '2026-09-07T15:18:09+00:00'
---

Edge headless on this machine has a window floor of about 496 px, so the product overview's `--window-size=390` recipe lays the page out at 496 and every phone capture looks cut off at the right (measured from the page: clientWidth 496). A local HTML file with a `<iframe src="http://localhost:PORT/page" style="width:390px;height:5400px;border:0">` captured at a 600-wide window gives a true 390 viewport (clientWidth 390, scrollWidth 390). Update the recipe in the product overview and have CG-315's check use the wrapper for its narrow captures.

## Provenance

Discovered by CG-308 (Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where the phase is, and the last period) during run `20260906T034805Z-revise`.

## Log

- 2026-09-06T04:18:52+00:00 discovered by CG-308

## Operator scope clarification, 2026-09-06

The operator is correcting the garden-local product overview separately. Keep worker changes in the product worktree: make the UI capture/check path verify the actual content viewport is 390 CSS pixels. For Edge fallback, a wider outer window with a 390px iframe is an available approach, not a required implementation. Document the verified recipe in product-owned documentation. Do not edit the live garden repository.

## Acceptance criteria

- [ ] Narrow captures verify a 390 CSS pixel content viewport rather than trusting outer window dimensions; preserve light/dark captures and document evidence.
- 2026-09-06T13:20:33+00:00 approved (cli)
- 2026-09-06T20:56:08+00:00 dispatched work run 20260906T205542Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~17341 tokens)
- 2026-09-06T21:05:14+00:00 Incident preemption; worktree/transcript and operator-test-tmp/CG326-recurrence.patch preserved. Escaped tests stopped; not a code failure.
- 2026-09-07T01:22:52+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply 6172db52bbafd37b49c27af81cd61e8f074dc435` in /home/joshua/work/worktrees/CG-326 to recover them (garden:CG-326:20260907T012252Z-work:pre-dispatch, run 20260907T012252Z-work)
- 2026-09-07T01:22:54+00:00 dispatched work run 20260907T012252Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~12694 tokens)
- 2026-09-07T01:33:26+00:00 opened https://github.com/joshmarcus/context-garden/pull/250 (base main): Narrow captures now use and verify a true 390px content viewport via iframe framing, with light/dark documentation preserved. Exact-commit CI passed. cost=$0.07
- 2026-09-07T01:36:40+00:00 automated review requested changes: The browser-dependent acceptance criterion remains unproven because the UI check passes when Chromium cannot launch, and the unit test does not execute the measurement JavaScript. cost=$0.21
- 2026-09-07T01:37:13+00:00 dispatched revise run 20260907T013711Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~13285 tokens)
- 2026-09-07T01:46:15+00:00 preserved uncommitted worktree changes from run 20260907T013711Z-revise outside the PR: `git stash apply acf82f1e38d847a2bca3b279486a2d1b59e4a346` in /home/joshua/work/worktrees/CG-326 (garden:CG-326:20260907T013711Z-revise:reap)
- 2026-09-07T01:49:49+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T01:51:09+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T01:52:50+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T01:54:57+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T01:56:45+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T01:58:20+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T02:00:15+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T02:02:10+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T02:04:03+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T02:06:14+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T02:08:18+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T02:10:12+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T02:13:34+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T02:16:04+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T02:18:33+00:00 check did not run (20260907T014802Z-check): no check result; retry also failed; needs human
- 2026-09-07T02:19:27+00:00 triage: changes requested by hand: Preserve PR250 and its current fixes. Verify browser-backed 390px light/dark captures actually exist and are read; brows
- 2026-09-07T03:00:32+00:00 dispatched revise run 20260907T030029Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~14092 tokens)
- 2026-09-07T03:13:29+00:00 preserved uncommitted worktree changes from run 20260907T030029Z-revise outside the PR: `git stash apply cb7a133ef44df0c46eac34122c230f0fd234f47d` in /home/joshua/work/worktrees/CG-326 (garden:CG-326:20260907T030029Z-revise:reap)
- 2026-09-07T03:29:08+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:30:16+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:31:29+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:32:36+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:33:45+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:34:51+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:35:22+00:00 Operator confirmed host capture blocker: Playwright Chromium lacks libnspr4/libnss3/libnssutil3/libsmime3; latest base probe checks=[] is not a code verdict. Official Ubuntu libnspr4/libnss3 packages extracted to ~/.local/share/garden/browser-runtime. Bounded probe with LD_LIBRARY_PATH=/home/joshua/.local/share/garden/browser-runtime/usr/lib/x86_64-linux-gnu successfully launches Chromium and measures390px (382MiB peak). Not yet configured in service; apply at next safe drained boundary, then supported check recovery and actual capture validation. Do not revise working capture code merely to bypass missing host libraries.
- 2026-09-07T03:35:57+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:37:03+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:38:10+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:39:16+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:40:22+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:41:40+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:42:50+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:44:27+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:46:21+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:47:27+00:00 check did not run (20260907T032801Z-check): no check result; retry also failed; needs human
- 2026-09-07T03:48:12+00:00 triage: changes requested by hand: Host browser libraries are now supplied to service by browser-runtime.conf after accounted restart, all five existing wo
- 2026-09-07T03:59:19+00:00 dispatched revise run 20260907T035917Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~15204 tokens)
- 2026-09-07T04:09:09+00:00 preserved uncommitted worktree changes from run 20260907T035917Z-revise outside the PR: `git stash apply 48501ea3a4d6646793ef9550a15892df7102358d` in /home/joshua/work/worktrees/CG-326 (garden:CG-326:20260907T035917Z-revise:reap)
- 2026-09-07T04:11:54+00:00 check did not run (20260907T041036Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:13:51+00:00 check did not run (20260907T041036Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:15:40+00:00 check did not run (20260907T041036Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:17:10+00:00 check did not run (20260907T041036Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:19:35+00:00 check did not run (20260907T041036Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:21:42+00:00 check did not run (20260907T041036Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:22:15+00:00 triage: changes requested by hand: Host browser readiness correction is now propagated through the actual scrubbed launch environment: worker_env.pass=[LD_
- 2026-09-07T04:37:16+00:00 dispatched revise run 20260907T043714Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~15509 tokens)
- 2026-09-07T04:41:05+00:00 preserved uncommitted worktree changes from run 20260907T043714Z-revise outside the PR: `git stash apply 2ca258ca0742e345ac86a79f2d6e7e54b77c144d` in /home/joshua/work/worktrees/CG-326 (garden:CG-326:20260907T043714Z-revise:reap)
- 2026-09-07T04:43:55+00:00 check did not run (20260907T044244Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:45:47+00:00 check did not run (20260907T044244Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:47:13+00:00 check did not run (20260907T044244Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:48:37+00:00 check did not run (20260907T044244Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:50:48+00:00 check did not run (20260907T044244Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:53:04+00:00 check did not run (20260907T044244Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:55:46+00:00 check did not run (20260907T044244Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:57:36+00:00 check did not run (20260907T044244Z-check): no check result; retry also failed; needs human
- 2026-09-07T04:57:39+00:00 triage: changes requested by hand: Effective config hold is now cleared and accepted signature includes LD_LIBRARY_PATH. Operator executed current PR head1
- 2026-09-07T05:02:50+00:00 dispatched revise run 20260907T050248Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~16038 tokens)
- 2026-09-07T05:14:12+00:00 preserved uncommitted worktree changes from run 20260907T050248Z-revise outside the PR: `git stash apply 1a1bfc730e6b1ffc38ee96104fc9f4c91e6a55d5` in /home/joshua/work/worktrees/CG-326 (garden:CG-326:20260907T050248Z-revise:reap)
- 2026-09-07T05:15:55+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/250: Fixed narrow frame selection and preserved diagnostic captures while retaining strict 390px viewport validation. Exact-commit CI passed. cost=$0.08
- 2026-09-07T05:39:08+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/walkthrough.py); a rebase agent will resolve it
- 2026-09-07T05:54:03+00:00 dispatched rebase run 20260907T055401Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~10065 tokens)
- 2026-09-07T05:57:56+00:00 preserved uncommitted worktree changes from run 20260907T055401Z-rebase outside the PR: `git stash apply 865a17ed5bd9a4e8e75521b721730fceb596be9c` in /home/joshua/work/worktrees/CG-326 (garden:CG-326:20260907T055401Z-rebase:reap)
- 2026-09-07T06:01:06+00:00 pre-PR checks failed (lint, ui) and 3 revision rounds already used; needs a human cost=$0.03
- 2026-09-07T06:15:58+00:00 triage: changes requested by hand: Operator diagnosis: pre-PR check 20260907T055757Z-check failed after rebase with a real SyntaxError in src/garden/walkth
- 2026-09-07T06:16:00+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T06:17:26+00:00 dispatched revise run 20260907T061724Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~17093 tokens)
- 2026-09-07T06:26:47+00:00 preserved uncommitted worktree changes from run 20260907T061724Z-revise outside the PR: `git stash apply d6b3c2d470dfc36aa1b91da07d56c7c4500f36a1` in /home/joshua/work/worktrees/CG-326 (garden:CG-326:20260907T061724Z-revise:reap)
- 2026-09-07T06:29:57+00:00 check did not run (20260907T062830Z-check): no check result; retry also failed; needs human
- 2026-09-07T06:31:19+00:00 check did not run (20260907T062830Z-check): no check result; retry also failed; needs human
- 2026-09-07T06:32:41+00:00 check did not run (20260907T062830Z-check): no check result; retry also failed; needs human
- 2026-09-07T06:34:19+00:00 triage: changes requested by hand: Operator recovery: check20260907T062647Z-check now passes lint and actual Now2 narrow captures; 52/56 executed viewport
- 2026-09-07T06:34:20+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T06:42:10+00:00 dispatched revise run 20260907T064208Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~17390 tokens)
- 2026-09-07T06:51:39+00:00 preserved uncommitted worktree changes from run 20260907T064208Z-revise outside the PR: `git stash apply 8a8e6ee5d5b4719bae9ac8f25cb190dbfbfd9535` in /home/joshua/work/worktrees/CG-326 (garden:CG-326:20260907T064208Z-revise:reap)
- 2026-09-07T06:53:04+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/250: Narrow captures now use a measured 390px iframe viewport with strict overflow validation. Main was integrated and exact-commit CI passed. cost=$0.06
- 2026-09-07T08:39:35+00:00 description rewritten by the reviewer cost=$0.80
- 2026-09-07T08:39:41+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/250
- 2026-09-07T15:18:09+00:00 automated review could not start: CG-326 is done: #250 was merged at 08:39:41
