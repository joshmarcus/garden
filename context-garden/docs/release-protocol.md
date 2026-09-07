# Release and deployment protocol

Owner adopted versioned GitHub releases on 2026-09-07. This is the operator publication workflow; release creation does not automatically deploy.

## Versions and channels

Use v0.MINOR.PATCH tags while the product evolves. Increment patch for fixes, minor for features or compatibility changes; describe breaking changes explicitly. Never move/reuse a published tag. A candidate uses v0.MINOR.PATCHrcN and matching PEP440 package version 0.MINOR.PATCHrcN. A final release uses matching pyproject.toml version. Existing v0.1.0 is a one-time bootstrap preview naming the installed 0.1.0 package; do not reuse that version for another commit.

Main is merged development, not deployment approval. Use an isolated codex release branch when selecting approved fixes from main. Keep excluded work explicit. Prepare a version bump before final candidate CI; a version-only change still changes the commit, so prior-head CI is insufficient.

## Prepare and validate

1. Select an exact source commit. Verify automated approval lineage for included PRs and inspect any post-review differences. Merged/DONE alone is insufficient.
2. Set the package version and commit release metadata. Obtain passing exact-commit full GitHub CI and the focused checks warranted by deployment changes. No broad local suite.
3. Prepare release notes and a machine-readable manifest: version, tag, exact SHA, CI links, included fixes, known limitations, exclusions, compatibility/data changes, install and rollback instructions. Do not claim unmet stabilization or live cloud evidence.
4. Create a draft/prerelease explicitly at that SHA using gh release create --target SHA --prerelease --notes-file FILE. Attach only verified artifacts. GitHub source archives are sufficient initially; do not imply wheel/PyPI publication.
5. Confirm the published tag resolves to the validated SHA. Preserve tags; publish a new version for corrections. The operator owns this gate under delegated authority; do not route unapproved PRs to Josh.

## Deploy separately

Use the existing incident/deployment protocol to account for active runtime users and durable uncollected results. Install the exact release SHA under bounded resources, restore venv protections, restart safely, and verify source/version plus affected application journeys. A release candidate may be installed for monitored verification without calling it stable.

Record deployed release, exact SHA, deployment time, prior pin and verification independently of latest available release. Only update this record after the installed build is verified. Roll back by installing the previous verified release/pin through the same safe boundary; never rewind scheduler state or delete run evidence. Never auto-upgrade merely because a release exists.

The initial deployed record is v0.1.0 at899b2c0cda5a311f6e498b75929ca6b58a524eab; phase05 remains unproven. The CG373-only branch9db48a7 is an unversioned candidate, not a published release. Give the next deployable candidate a new package version and exact-head CI before publication.
