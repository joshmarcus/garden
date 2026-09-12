---
id: CG-627
title: Publish context-garden to PyPI with verified installable releases
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-384
priority: 2
difficulty: hard
reading:
- pyproject.toml
- README.md
- LICENSE
- src/garden/__init__.py
- .github/workflows/ci.yml
- src/garden/cli/__init__.py
branch: garden/cg-627-publish-context-garden-to-pypi-with-verified-ins
pr: https://github.com/joshmarcus/context-garden/pull/493
runner: remote
discovered_from: 'owner: Task: Publish context-garden as a library to pypi (if that is the standard python
  library publishing locatino)'
attempts: 1
last_dispatched_at: '2026-09-11T14:19:33+00:00'
created: '2026-09-11T13:55:37+00:00'
updated: '2026-09-11T14:52:11+00:00'
---

## Goal

Publish Context Garden as an installable Python distribution on the Python Package Index (PyPI), the standard public index used by pip. Users should be able to install `context-garden`, import the documented library modules under `garden`, and run the existing `garden` CLI without a source checkout. Implement the packaging and release path and carry the first actual publication through verification; a workflow file or a GitHub release alone is not the PyPI outcome.

## Existing work and release identity

Build on completed CG-384 release identity/validation, the existing Hatchling pyproject.toml, src/garden package and garden.cli:app entry point. Stable 0.3.0 is already published on GitHub and deployed from exact1629d8673c039e5fa8ceae5d06fc4ba01efe8297. Its version metadata is0.3.0; the main checkout historically still says0.1.0, so inspect actual source and release history rather than publishing that stale version. Do not rewrite stable tags or change running controller/workers. Use0.3.0 only for artifacts built from its exact existing accepted release source; any required changes must pass normal review/CI and use a consistent subsequent release identity. Phase05 is closed; this is independent Phase07 work and does not wait onCG624 test reduction.

Operator preflight September11 found no existing PyPI task and the public project page returned404. That is not proof of package-name availability or authenticated ownership. Verify the normalized name and correct owner/account before upload; report an actual name/ownership conflict if found, without selecting a misleading substitute. The owner has explicitly requested publication, so no repeat publication-permission question is needed once exact reviewed artifacts and usable publisher authority exist.

## Acceptance criteria

- [ ] Produce valid wheel and source distribution from the exact intended accepted release. Reconcile project/version metadata, supported Python requirement, README/license, project URLs, dependencies/extras and packaged runtime resources. Include the templates/static/data needed by installed operation; exclude private operational state, credentials and unrelated working files. Keep distribution name `context-garden` and import namespace `garden` unless an actual name conflict requires an owner decision.
- [ ] Verify a non-editable installation from the built distributions in clean disposable environments outside the repository, including a meaningful documented library-import/use example, package version, `garden --help`, and access to relevant packaged resources. Document the intended library entry points and CLI installation, without promising all private internals are a permanent public API. Keep code portable for Linux, macOS and Windows through WSL; report platforms actually exercised and any untested ones. Use focused checks proportionate to packaging changes, retaining normal applicable exact-head CI and independent source review.
- [ ] Implement and document a repeatable explicit release publication path using the existing repository CI/release convention. Prefer PyPI Trusted Publishing with GitHub Actions OIDC where the owner account supports it. Bind publication to the intended repository/workflow/release and build artifacts, preserve version/source provenance, and make retries handle an already-published version truthfully. Do not publish every main merge or replace an existing version's files. Existing source-install/rollback workflows remain usable.
- [ ] Complete the first actual production PyPI upload using the correct existing owner account or a configured pending/trusted publisher, then verify the public index metadata/version/artifact hashes and perform a clean `pip install context-garden==<published-version>` from PyPI with import/CLI verification. TestPyPI may be used if useful; a TestPyPI upload is not production completion. Report the actual project URL, published version and exact source. If publisher setup/account authentication is unavailable, finish and review all preparatory work first, return the exact concrete account-side action needed through the native question channel, and keep publication explicitly pending. Do not claim publication from an unexecuted workflow or an authentication failure.

## Execution and operator handoff

Use an existing remote worker for source preparation and ordinary focused checks under unchanged resource/deadline limits. Preserve active CG624 and unrelated holds. Worker-side Git publication remains subject to normal setup.worker_push policy; prepare exact commits and let the controller publish them. Root operator owns credential/account interaction and final authorized external upload when it cannot be done by the normal release workflow. Do not request new API tokens or expose credential contents in task files/logs; reuse suitable existing scoped publisher credentials or Trusted Publishing when available. Never repurpose AWS/Tailscale credentials for this service. Source-owned review/CI gates and the actual operator publication step must be tracked distinctly so an unavailable account action does not cause unchanged source revision loops, while the requested public-PyPI outcome remains outstanding until verified. No new fleet resources, deadline extension, production runtime activation, version-tag rewriting, or Phase05 reopening is authorized by this task.

## Official references

- https://packaging.python.org/en/latest/flow/
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
- https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
- https://docs.pypi.org/trusted-publishers/

## Log

- 2026-09-11T13:56:33+00:00 approved (owner requested PyPI publication; delegated operator approval)
- 2026-09-11T13:57:34+00:00 dispatched work run 20260911T135734Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2610 tokens)
- 2026-09-11T14:04:23+00:00 worker asks: Please configure a PyPI pending Trusted Publisher for project `context-garden`, repository `joshmarcus/context-garden`, workflow `publish-pypi.yml`, environment `pypi`, and create the matching protected GitHub `pypi` environment; can you confirm when both are configured so the reviewed 0.3.1 release can be published and verified? cost=$1.16
- 2026-09-11T14:10:15+00:00 dispatched resume run 20260911T141015Z-resume via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2630 tokens)
- 2026-09-11T14:15:10+00:00 opened https://github.com/joshmarcus/context-garden/pull/493 (base main): Prepared context-garden 0.3.1 packaging, documentation, and a Trusted Publishing workflow, then hardened distribution verification against checkout contamination. Focused packaging tests and repository-wide Ruff lint pass; the production PyPI upload remains an explicit external operator gate. cost=$0.50
- 2026-09-11T14:16:07+00:00 Operator verified final candidate91884bc9: wheel+sdist built, Twine metadata passed, and both corrected clean-install checks passed onPython3.14.4/Linux throughWSL. Artifacts match prior17dd7c4e bytes exactly; hashes and original logs are in pypi-final-source-checks-20260911T1414/build-receipt.json. ActualGitHubpypi environment21735403264 configured14:11:45 with singlev*TAG policy59714091, no branch deployment or extra review-count gate; priorcopilot preserved. PyPI pendingpublisher/account access remains unavailable and no upload occurred. Root found no existingpypirc/TWINE/PYPI variables orrepositorysecret; bothbrowserhelpers failed to initialize beforeaccount access. Owner-facing action will be to add the exactpendingpublisher via thePyPI accountPublishing page; sourcePR493 proceeds through ordinaryreview/CI. This is the root delegatedoperator record, not a fabricated worker test or owner setup confirmation.
- 2026-09-11T14:19:24+00:00 automated review requested changes: The release preparation is correct and independently verified. Production PyPI publication remains an explicit owner-side follow-up, while exact-head CI is pending and independently merge-gated. cost=$0.37
- 2026-09-11T14:19:33+00:00 dispatched revise run 20260911T141932Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2921 tokens)
- 2026-09-11T14:20:44+00:00 worker says nothing to change: The only review finding concerns the first production PyPI upload, which binding owner guidance assigns to the root operator after source review, merge, exact-head CI, and PyPI Trusted Publisher configuration. There is no additional source correction to make in this revision. cost=$0.21
- 2026-09-11T14:33:18+00:00 Delegated operator accepts the source-only no_change assessment. Original raw141528review approves exact91884bc9 with no code findings; both exactCIs nowSUCCESS. Owner confirmed PyPIsetup in chat. Root owns actualpostmergeupload/verification and retains alloriginalreview/decisionpayloads. Merging exact reviewedsource with GitHubmatch-head guard, without anothercount-onlyreview or directset-done.
- 2026-09-11T14:34:34+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/493
- 2026-09-11T14:52:11+00:00 Root publication follow-through COMPLETE: context-garden 0.3.1 is on production PyPI. GitHub release workflow34611078677 attempt2 succeeded14:45:29 using the unchanged reviewed91884bc9 artifacts after the owner corrected publisher setup and requested retry. Public wheel and sdist were downloaded and their SHA256/size verified against the accepted builds. A fresh noneditable installation from https://pypi.org/simple passed library frontmatter example, installed import/metadata provenance, packaged resources and garden --help on Python3.14.4/LinuxWSL. Final evidence: /home/joshua/work/operator-test-tmp/pypi-release-031-20260911/public-index-verification.json. Original failed attempt and review results remain intact. Production controller/workers remain stable0.3.0; no runtime activation.
