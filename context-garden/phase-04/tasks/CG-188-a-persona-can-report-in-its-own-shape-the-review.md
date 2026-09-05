---
id: CG-188
title: 'A persona can report in its own shape: the review runner keeps the findings block and adds the
  persona''s sections (vision, features, not now, questions), rendered in the report and fed to the retro'
status: in_review
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: medium
reading:
- src/garden/personas.py
- src/garden/scheduler/persona.py
- src/garden/retro.py
- personas/product-manager.md
- context-garden/phase-03/docs/reviews/product-manager-vision-2026-09-05.md
branch: garden/cg-188-a-persona-can-report-in-its-own-shape-the-review
pr: https://github.com/joshmarcus/context-garden/pull/144
attempts: 1
last_dispatched_at: '2026-09-05T12:25:40+00:00'
created: '2026-09-05T10:22:27+00:00'
updated: '2026-09-05T12:43:26+00:00'
---

## Goal

A persona file can declare the sections its report has, and the review runner asks for them, keeps them, and renders them. The findings block (score, overall, findings with severity) stays for every persona, because the retro and `--file-tasks` read it; the persona's own sections come beside it, in the report file and in the retro's inputs, so a product manager can deliver a vision, a ranked feature list, a not-now list and questions, and a usability expert can deliver a walkthrough transcript, without a run outside the loop.

## Context

On 2026-09-05 the phase-03 retro ran the new product-manager persona (`personas/product-manager.md`, which asks for five sections). The runner's brief (`personas.py`, the `GARDEN_PERSONA` marker) only accepts `{score, overall, findings}`, so the report came back as two high, three medium and one low finding, with no vision and no features. The operator produced the intended report with a one-off `claude -p` run from the persona file and the retro material (`docs/reviews/product-manager-vision-2026-09-05.md`), which the user asked to have as a proper fix. CG-181 (the retro's features section) and CG-187 (every finding becomes a draft) read the findings block; this task gives them the richer sections too.

## Design

- A persona file may carry frontmatter `sections: [vision, where-we-are, features, not-now, questions]` (names are free); the brief lists them and asks for `sections: {<name>: "<markdown>"}` in the marker JSON alongside the findings; `features` entries may also be structured (title, body, difficulty, priority) so CG-181 can file them directly.
- The report file renders the persona's sections first, then the findings by severity, then the score line; the phase page's review list shows the score and, for a persona with a `features` section, the count of features.
- The retro brief includes the sections verbatim as persona input; `features` from a persona are candidates for the retro's own features list, deduplicated there.
- The built-in product-manager persona (CG-181) declares these sections.

## Acceptance criteria

- [ ] A persona with declared sections gets them in its brief and back in its report; a persona without them is unchanged.
- [ ] The product-manager built-in declares vision, where-we-are, features, not-now and questions; a phase review with it produces a report with those sections and the findings block.
- [ ] The retro reads the sections; a persona's structured `features` reach the retro's features list with the persona named as the source.
- [ ] Tests with the fake harness for a persona with sections and one without.

## Log

- 2026-09-05T10:31:16+00:00 approved (web)
- 2026-09-05T12:25:40+00:00 dispatched work run 20260905T122531Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~19339 tokens)
- 2026-09-05T12:39:14+00:00 opened https://github.com/joshmarcus/context-garden/pull/144 (base main): A persona file can declare `sections:` in frontmatter; the review runner lists them in the brief, keeps the findings block, asks for the sections in the marker JSON, and renders them in the report. The product-manager built-in declares its five sections, the phase page shows score and feature count, and the retro lifts a persona's structured features into its own list naming the source. cost=$5.10
- 2026-09-05T12:43:26+00:00 automated review: approve — Persona sections are declared in frontmatter, requested in the brief, kept beside the findings block, rendered in the report, and lifted into the retro's features with the source named. All four acceptance criteria are covered by fake-harness tests; ruff clean and full suite 613 passed / 3 skipped. cost=$0.88
