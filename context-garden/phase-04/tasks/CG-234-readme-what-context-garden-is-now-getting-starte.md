---
id: CG-234
title: 'README: what context-garden is now, getting started end to end, operating a running garden, and
  restarting an operator agent session'
status: done
product: context-garden
phase: phase-04
depends_on: []
priority: 0
difficulty: medium
reading:
- README.md
- docs/design.md
- docs/architecture.md
- docs/worker-protocol.md
- .claude/skills/garden-operate/SKILL.md
- .claude/skills/garden-plan/SKILL.md
- examples/garden.work.yaml
- src/garden/cli/__init__.py
branch: garden/cg-234-readme-what-context-garden-is-now-getting-starte
pr: https://github.com/joshmarcus/context-garden/pull/189
harness: claude
model: claude-fable-5-1
attempts: 2
last_dispatched_at: '2026-09-05T21:11:02+00:00'
created: '2026-09-05T20:40:39+00:00'
updated: '2026-09-05T21:36:23+00:00'
---

## Goal

`README.md` is the front door and is true about the product as it is today. It says in a paragraph what context-garden is (a repository of context files driving detached agent workers through a token-free scheduler, with a web UI, a TUI and a CLI), then takes a new person from nothing to a running garden with one phase, then tells an operator how to run and observe it, and tells an operator agent how to pick the garden back up after its own session ends. Written for someone who has never seen the repo; plain copy, no scar tissue, the herbarium's vocabulary where the UI uses it.

## Context

The user on 2026-09-05, high priority. The README predates phases 03 and 04: the scheduler is a package of tick-phase mixins, the web app has pages and an action registry, reviews are automated with a verdict contract, there is a merge queue with mechanical rebases, a freeze and close lifecycle, a retro with a verdict and features, a kickoff, decision cards, a costs page, trials between harnesses and models, a codex harness beside claude, a scrubbed worker environment, and four Claude Code skills that `garden init` ships (`garden-take`, `garden-plan`, `garden-review`, `garden-operate`). None of that is in the README. The operator of this garden is a Claude Code session driven by the `garden-operate` skill; when that session ends (context compaction, a restart of the machine, a new day) the next session needs a documented way back in: where the truth lives (`.garden/`, the task files, the events log), the first look (`garden observe`, or `garden status` and `garden inbox` until it lands), how the server is run as a service and restarted after a tick, the environment the workers need (harness config dirs), and the rule that the loop keeps its own state so nothing is lost by a session ending.

## Sections the README must have

1. **What it is** (one paragraph) and **what it is not** (not a chat bot, not a CI runner; the scheduler never calls a model).
2. **How the loop works** (a short list: context files, planner, tasks, workers in worktrees, checks, PR, automated review, merge queue, retro), with a link to `docs/design.md` and `docs/architecture.md`.
3. **Getting started**: install (`uv` or `pip`, Python 3.11+), `garden doctor`, `garden init`, `garden.yaml` (products, harnesses and tiers, review settings, budgets; point at `examples/garden.work.yaml` for a work setting where dependencies and tests are not Python), a first product and phase, `garden plan`, approve on the Inbox, `garden serve`, the first PR. Every command shown must exist in `garden --help`.
4. **Operating a garden**: the web pages (Inbox, Board, Trellis, task and run pages, Costs, Config, Herbarium), decision cards and what each action does, freeze and close, the retro and kickoff, trials, budgets and the observation profiles.
5. **Running it as a service**: a systemd user unit example with the environment the harnesses need (`CLAUDE_CONFIG_DIR`, `CODEX_HOME`), restart after a tick, logs in the journal; keep-alive notes for WSL.
6. **Restarting an operator agent session**: what an operator session is (a Claude Code session using `garden-operate`), what it should read first when it starts or resumes (the skill, `garden observe` or `garden status` plus `garden inbox`, `git log` of the garden, the phase docs), what it must never do (edit task status by hand, stop the service by killing a process tree), why nothing is lost when it ends, and how to keep its own cost low (compact at phase boundaries, observe on the quiet profile, record spend).
7. **Costs**: how spend is recorded per run and per operator session, tiers and harness routing, and where to look.
8. **Skills and contributing**: the four skills, `garden validate`, tests and lint.

## Acceptance criteria

- [ ] Every command and page named in the README exists (`garden --help` and the web routes), checked by a test that greps the README for `garden <verb>` and asserts each verb is a registered command.
- [ ] A reader can follow "Getting started" on a clean machine to a running garden with one phase; the sequence is the one the CLI actually enforces (init before plan, approve before dispatch).
- [ ] The "Restarting an operator agent session" section matches `.claude/skills/garden-operate/SKILL.md` and names it.
- [ ] No section describes phase-02-era behaviour that later phases changed (single-file scheduler, manual merges, review by hand).
- [ ] The description reads as one document written today: goal and outcome first, no history of how it got here.

## Log

- 2026-09-05T20:40:39+00:00 approved (web)
- 2026-09-05T20:41:32+00:00 dispatched work run 20260905T204117Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~13559 tokens)
- 2026-09-05T20:44:09+00:00 reset to ready by hand
- 2026-09-05T20:44:13+00:00 dispatched work run 20260905T204413Z-work via local [claude model=claude-fable-5-1] (fresh session, base main, ~13609 tokens)
- 2026-09-05T20:50:33+00:00 attempt 1 failed: no GARDEN_RESULT in worker output (see final.md); will retry
- 2026-09-05T20:50:58+00:00 dispatched work run 20260905T205058Z-work via local [claude model=claude-fable-5-1] (fresh session, base main, ~16211 tokens)
- 2026-09-05T20:59:50+00:00 also found by CG-234 (README: what context-garden is now, getting started end to end, operating a running garden, and restarting an operator agent session) during run `20260905T205058Z-work`
- 2026-09-05T21:03:02+00:00 opened https://github.com/joshmarcus/context-garden/pull/189 (base main): README.md rewritten as the front door to the product as it is today: what it is, the loop, getting started in the order the CLI enforces, operating a garden, running it as a systemd user service, restarting an operator agent session against the garden-operate skill, costs and the four skills. A test asserts every garden command, bold page name and relative link in the README exists. cost=$4.08
- 2026-09-05T21:10:40+00:00 automated review requested changes: README rewrite is thorough and well-verified (commands, pages, ordering, skill correspondence all check out), but it misdescribes merging as an automatic default when the shown config (automerge: false) actually requires a human to merge on GitHub, with a backwards inline comment and no getting-started guidance for that step. cost=$1.09
- 2026-09-05T21:11:02+00:00 dispatched revise run 20260905T211102Z-revise via local [claude model=claude-fable-5-1] (fresh session, base main, ~18081 tokens)
- 2026-09-05T21:16:53+00:00 also found by CG-234 (README: what context-garden is now, getting started end to end, operating a running garden, and restarting an operator agent session) during run `20260905T211102Z-revise`
- 2026-09-05T21:19:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/189: Fixed the README's description of merging: by default a person merges an approved PR on GitHub and the poll marks the task done; the merge queue merges only with github.automerge: true. Intro, loop step 7, the config comment, the getting-started walkthrough and the Inbox card list now match the scheduler. cost=$3.07
- 2026-09-05T21:25:38+00:00 automated review: approve — README rewrite is accurate, well-scoped to README.md and tests/test_readme.py, and every checked claim (commands, routes, automerge default, skill correspondence) verifies against the code. cost=$0.78
- 2026-09-05T21:30:17+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T21:33:16+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-05T21:36:23+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/189
