---
id: CG-706
title: Automatic local authentication grants private read access under arbitrary Host h
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: persona:security:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:06:03+00:00'
---

## Goal

In src/garden/web/app.py and src/garden/web/trust.py, validate the request Host against explicitly configured listener names before granting the automatic local principal, covering GET and HEAD as well as mutations. An attacker-controlled page could rebind its hostname to the local listener and read member-visible tasks or logs where browser network protections permit; the existing POST Origin check does not protect these reads. An in-memory reproduction using the production OriginCheck returned 200 and the synthetic local principal for an unrecognized Host without credentials, while the cross-origin POST returned 403. Add a focused regression proving unknown hosts are rejected and permitted localhost names retain automatic startup; do not derive the allowlist from request or forwarded headers.

## Context

Raised by the security persona review (Automatic local session / HTTP Host validation). persona:security:context-garden/phase-10.
