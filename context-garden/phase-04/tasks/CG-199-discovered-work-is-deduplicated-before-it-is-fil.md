---
id: CG-199
title: 'Discovered work is deduplicated before it is filed: the same finding from several workers becomes
  one draft'
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: easy
reading: []
created: '2026-09-05T10:30:00+00:00'
updated: '2026-09-05T10:30:00+00:00'
---

## Goal

Six discovered drafts were filed for one red-main fix on 2026-09-05 and cancelled by hand. When a worker reports discovered work, compare its title and body with open tasks in the phase (and the next phase) by normalised title and by the file and symptom named; a near-duplicate becomes a note on the existing task (`also found by CG-xxx`) instead of a new draft, with a `discovered_duplicate` event.

## Provenance

From the phase-03 persona reviews of 2026-09-05 (project-manager:medium); filed by the operator so that every finding is kept (see CG-187). Reports: `context-garden/phase-03/docs/reviews/`.

## Acceptance criteria

- [ ] A discovered item whose normalised title matches an open task, or whose body names the same file and error, is attached to that task and not filed.
- [ ] The existing task's page lists who else found it.
- [ ] A test files the same discovery from three workers and sees one draft.

