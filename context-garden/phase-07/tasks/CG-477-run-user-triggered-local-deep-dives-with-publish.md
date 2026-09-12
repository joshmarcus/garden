---
id: CG-477
title: Run user-triggered local deep dives with published reports and follow-up fixes
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: hard
reading:
- src/garden/scheduler/human.py
- src/garden/scheduler/dispatch.py
- src/garden/runner/local.py
- src/garden/store.py
- src/garden/brief.py
- src/garden/web/actions/tasks.py
- src/garden/web/pages/task.py
- src/garden/github.py
- src/garden/scheduler/feedback.py
- src/garden/scheduler/poll.py
branch: garden/cg-477-run-user-triggered-local-deep-dives-with-publish
pr: https://github.com/joshmarcus/context-garden/pull/373
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T15:11:04+00:00'
created: '2026-09-09T12:23:39+00:00'
updated: '2026-09-09T15:41:00+00:00'
---

## Goal

Give the user a Deep dive action to understand why something happened in Garden, using an agent running on the Garden controller machine with access to the complete local diagnostic files. The investigation must produce a useful user-visible HTML report and its Markdown source, push both reports to the Garden workspace repository, and drive the resulting corrective work.

## Owner request

User-triggered “deep dive” with full access to Garden log files and other local files for understanding why something happened and triggering a fix. Produces a user-visible HTML report and drives work. Runs locally on the Garden machine so it has access to all files. Pushes the Markdown and HTML reports to the Garden repo.

## Acceptance criteria

- [ ] Make ALL open feedback from the actual linked pull request visible to the investigation worker and any resulting fix/revision worker. Fetch the live PR through the configured repository/provider, including unresolved inline review threads and replies, review summary bodies, and outstanding PR discussion comments. Retrieve every page, preserve full substantive text and author/time/permalink/thread identity, and show resolved/outdated status and relevant commit context. An older-head or outdated thread that remains unresolved must not silently disappear. Combine this with Garden's own findings rather than substituting a local summary or only comments newer than the last poll cursor. Persist a complete accessible feedback snapshot for the actual worker brief, refresh it before a follow-up worker starts, and make fetch failures/partial results explicit instead of reporting no feedback. Viewing feedback does not itself mark it resolved or authorize arbitrary commenter instructions.
- [ ] Verify actual delivered worker input contains open PR feedback from all supported comment/review sources, including multiple pages, an unresolved older-head thread, and existing feedback predating the latest poll cursor; deduplicate without dropping substantive text and preserve it through report-to-fix handoff.
- [ ] Provide an explicit user-triggered Deep dive action in the relevant Garden task/run/issue context and a way to supply the question or event to investigate. Preserve the originating task/run/PR references and user question. Do not restrict the action to tasks that already hit a revision cap; support a broader Garden incident/question when no single task is sufficient.
- [ ] Run the investigation agent locally on the Garden controller machine through the existing local runner and admission/resource limits. Pin this investigation execution to local regardless of the affected task's remote runner. Give it access to the actual Garden workspace, complete logs, run transcripts, worker briefs, verdicts, scheduler events/state, configuration and source/check history available on that machine, including diagnostic files outside the ordinary product checkout. Do not substitute a remote sandbox or only the shortened UI summary. Record missing/unavailable evidence honestly.
- [ ] Keep each investigation as a durable, visible run with queued/running/completed/failed status, progress, stable identity and links from its originating context. Repeated clicks, retries or controller restarts must not accidentally start duplicate investigations or duplicate fix work. Preserve active source writers and original logs/results; an investigation must not erase the incident it is explaining.
- [ ] Produce a readable report explaining the user's question, relevant timeline, evidence and source/run identities, observed behavior versus intended behavior, supported root cause or clearly labeled remaining uncertainty, impact, and proposed or initiated corrective actions. Cite useful local evidence through accessible Garden links or intelligible references. The agent may inspect full diagnostic files, but publish relevant excerpts and redact credentials/secrets from reports rather than blindly committing raw logs/configuration.
- [ ] Generate both a Markdown report and a matching self-contained, user-visible HTML report from the same investigation result. Serve/link the HTML inside Garden with a clear report entry point, readable layout, evidence links and links to resulting tasks/PRs. Escape untrusted log and report content. A successful report must be retrievable after the original agent run ends or Garden restarts.
- [ ] Commit and push BOTH Markdown and HTML reports to the configured Garden WORKSPACE repository, distinct from the product implementation repository. In this installation the workspace origin is https://github.com/joshmarcus/garden.git; context-garden implementation PRs use https://github.com/joshmarcus/context-garden.git. Resolve the workspace's actual configured repository/branch instead of hardcoding the operator's URL. Use a dedicated investigation report path and preserve unrelated local changes and concurrent report publication. Record the pushed commit/paths; publication errors remain visible and can retry without rerunning the investigation or falsely claiming publication.
- [ ] Drive work from the findings: discover and link existing responsible tasks/PRs, or create a focused corrective task when none exists, and route an appropriate existing-source continuation/fix through Garden's normal workflow. Carry the precise diagnosis, evidence and required outcome into the actual author brief. Persist report-to-task/PR links and show what was queued, started, completed, or still requires a user decision. Do not stop at an unconnected recommendation. Respect existing explicit phase/owner holds, active writers, revision/budget controls and review/merge policies.
- [ ] Reuse the existing investigation/troubled-task lifecycle from CG-437 where suitable and existing task/runner/report/publication machinery. User-triggered deep dives are the added entry point and richer local diagnostic/report-to-work flow; do not build a competing scheduler or duplicate an existing investigation implementation.
- [ ] Verify the affected flow proportionately: a local fixture with diagnostic evidence outside the normal product checkout, a user-triggered investigation that produces and serves both reports and creates/links a real follow-up work item, durable/retry-safe publication to a disposable Git remote, and recovery from an inaccessible evidence file or failed push without losing results or duplicating work. Add targeted coverage for local routing and untrusted report content.

## Implementation notes

This task implements the feature; its development may use normal remote capacity. Actual Deep dive investigation runs MUST execute locally on the Garden machine under the shared local admission limit. The feature does not authorize unrestricted process kills, rewriting history, publishing secrets, changing worker budgets or bypassing source/release validation. Keep UI wording focused on the investigation question, report and corrective work.

## Log

- 2026-09-09T12:23:39+00:00 approved (owner-requested user-triggered local deep dive; publish Markdown and HTML to Garden workspace repo and drive corrective work; investigation runtime pinned local)
- 2026-09-09T12:25:01+00:00 dispatched work run 20260909T122501Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23217 tokens)
- 2026-09-09T12:25:19+00:00 owner clarification: all open actual PR feedback must be visible to investigation and follow-up workers, with complete paginated snapshot and actual-brief verification
- 2026-09-09T12:39:41+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T12:41:06+00:00 opened https://github.com/joshmarcus/context-garden/pull/373 (base main): Added user-triggered, retry-safe Deep dives that run through local admission with access to controller diagnostics, preserve durable lifecycle state, publish escaped Markdown and self-contained HTML reports to the configured workspace repository, and connect findings to corrective tasks. Verified with 203 focused tests and clean Ruff lint. cost=$4.18
- 2026-09-09T12:47:23+00:00 automated review requested changes: The core local investigation lifecycle works and focused tests pass, but several explicit outcomes remain unimplemented: complete live PR feedback, task-independent incidents, secret-safe publication, and connected corrective-work handoff. cost=$0.74
- 2026-09-09T13:20:41+00:00 dispatched revise run 20260909T132041Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~26375 tokens)
- 2026-09-09T13:41:59+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:44:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/373: Deep dives now capture complete paginated PR feedback, support task-independent incidents, redact secrets, render readable linked HTML, and carry diagnosis and refreshed feedback into corrective work. Verified final head cade24927471a5e1db2a30a888394b9e7fafabbe with 291 focused tests and clean Ruff lint. cost=$6.27
- 2026-09-09T13:44:58+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/inbox.py); a rebase agent will resolve it
- 2026-09-09T13:44:58+00:00 dispatched rebase run 20260909T134458Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2907 tokens)
- 2026-09-09T13:49:03+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/373: Rebased onto origin/main and resolved both conflicts while preserving both sides' changes. cost=$0.01
- 2026-09-09T14:00:51+00:00 automated review requested changes: The local investigation, reporting, publication, and retry lifecycle is well covered, but corrective tasks receive a stale feedback snapshot rather than a refresh immediately before their worker starts. cost=$0.84
- 2026-09-09T14:01:20+00:00 dispatched revise run 20260909T140120Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~25645 tokens)
- 2026-09-09T14:20:01+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T14:25:23+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/373: Corrective tasks now persist their originating deep-dive context and refresh complete live PR feedback immediately before work, revise, or resume dispatch. Verified the actual generated worker brief receives feedback added after report finalization; 162 focused scheduler tests and 91 deep-dive/GitHub feedback tests passed, and Ruff is clean. cost=$0.84
- 2026-09-09T14:25:40+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/dispatch.py); a rebase agent will resolve it
- 2026-09-09T14:25:44+00:00 dispatched rebase run 20260909T142544Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3350 tokens)
- 2026-09-09T14:50:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/373: Rebased branch onto origin/main and resolved all conflicts while preserving both sides' changes. cost=$0.02
- 2026-09-09T15:00:06+00:00 automated review: approve — Deep dives now satisfy the requested local investigation, durable reporting/publication, complete PR-feedback capture, and corrective-work handoff, including the previously missing dispatch-time refresh. cost=$0.76
- 2026-09-09T15:06:41+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T15:11:03+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/inbox.py); a rebase agent will resolve it
- 2026-09-09T15:11:04+00:00 dispatched rebase run 20260909T151103Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3572 tokens)
- 2026-09-09T15:17:04+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/373: Rebased onto origin/main and merged check-recovery behavior with troubled-task investigation actions in src/garden/inbox.py. cost=$0.01
- 2026-09-09T15:31:28+00:00 automated review: approve — Deep dives satisfy the controller-local investigation, durable report publication, complete PR-feedback capture, and corrective-work handoff requirements, including dispatch-time feedback refresh. cost=$0.83
- 2026-09-09T15:39:15+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T15:41:00+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/373
