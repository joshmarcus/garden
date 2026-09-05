---
id: CG-146
title: 'A retro page per phase: the reconciled document, the operator retro, persona reports with scores,
  and the tasks the retro generated'
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/web/app.py
- src/garden/web/templates/phase_closed.html
- src/garden/web/templates/herbarium.html
- src/garden/retro.py
- src/garden/model.py
branch: garden/cg-146-a-retro-page-per-phase-the-reconciled-document-t
attempts: 1
last_dispatched_at: '2026-09-05T03:02:23+00:00'
created: '2026-09-05T02:49:08+00:00'
updated: '2026-09-05T03:05:29+00:00'
---

## Goal

Once a phase's retro has run, its results are one page in the web UI, reachable from the closed-phase header, the phase page and the Herbarium: the reconciled retro document, the operator's retro, each persona's report with its score and high findings, the harvested friction with its verdicts, and the list of tasks the retro generated, each linked, so a future phase can see what the retro found and what was done about it.

## Context

Asked at the phase-02 retro on the first live run. Today the pieces exist as files under `<phase>/docs/` (`retro/operator.md`, `retro/README.md`, `reviews/<persona>-<date>.md`, `friction.md`) and the retro document arrives by PR; the closed-phase header (CG-078) lists persona reviews but nothing ties the set together or shows what came of it. Add `/phases/<product>/<phase>/retro`: a header with the phase's numbers (done, cancelled, cost, runs), the reconciled document rendered, the operator retro, a persona table (name, score, high findings, link to the report), the friction table with verdicts from the reconciliation, and "Tasks from this retro". For the last, tasks filed from a retro carry `discovered_from: retro:<phase>` (the retro command and the person's `garden new-task --from-retro <phase>` both set it), so the page lists them with their current status, in this phase or the next. The closed-phase header links to the page; the Herbarium shows the persona scores beside each closed phase. Keep the copy plain and the look the app's herbarium look, not a dashboard.

## Acceptance criteria

- [ ] the retro page renders every artefact above for a phase whose retro has run, and says "no retro yet" otherwise; a test with the demo garden and fake reports.
- [ ] tasks filed with `--from-retro` or by `garden retro` carry the provenance and appear on the page with their status, across phases.
- [ ] the closed-phase header and the Herbarium link to it.

## Log
- 2026-09-05T02:50:00+00:00 deferred by the feature freeze (2026-09-05): phase 03; the phase-02 retro files are under docs/retro, docs/reviews and docs/friction.md meanwhile
- 2026-09-05T03:00:43+00:00 approved (web)
- 2026-09-05T03:02:23+00:00 dispatched work run 20260905T030213Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~5737 tokens)
- 2026-09-05T03:05:29+00:00 back to draft: approved by mistake during the phase 02 freeze; phase 03 work (CG-137 runs alone, first)
