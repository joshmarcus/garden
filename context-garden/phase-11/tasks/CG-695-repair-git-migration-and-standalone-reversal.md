---
id: CG-695
title: Repair Git migration and standalone reversal
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 1
difficulty: hard
reading: []
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:06:03+00:00'
---

## Goal

User value: move an existing garden into or out of multiplayer without losing authority or duplicating work. Why now: released migration still initializes SQLite and export misses other installations' Git obligations. Size: hard. Dependencies: delivered CG-631, CG-632 and CG-634; correct the implementation delivered by CG-639 without duplicating its historical task. Cover resumable commit, preserved ownership/history, Git-backed startup and refusal under unresolved work.

## Context

Proposed at the context-garden/phase-10 retro. The supported recovery boundary must agree with the architecture before users entrust existing work to multiplayer.
