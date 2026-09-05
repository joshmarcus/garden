---
id: CG-287
title: Persona runs are recorded per phase and the retro validates the run id it reads
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 4
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:05:56+00:00'
updated: '2026-09-05T23:05:56+00:00'
---

## Goal

dispatch_aux keys persona runs by phase rather than the shared _persona id; the retro validates the footer id against a safe character class and requires the resolved path under runs.dir. Also give discovered items structured file and error fields so dedup compares fields, not regexes.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.
