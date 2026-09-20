# SIP-0002: Publishing an installable artifact triggers release discipline

- Status: Proposed
- Risk: Low
- Proposed version: 0.10.0
- Date: 2026-09-20

## Observed gap

The maturity model has one axis: how many people work on the repository
(Scratch → Personal → Shared → Production). It has no axis for whether the
repository **publishes something other people install**.

Two consequences follow, and both fired on a real bootstrap:

1. `CHANGELOG` appears only at Stage 2 — Shared. A solo maintainer
   publishing an installable artifact is therefore told they do not need
   one, although their users have no other way to learn what changed
   between two versions they can install.
2. `workflows/project-bootstrap.md` never mentions a release, a tag or a
   version. It creates files, audits, and ends at a health summary.
   `references/bootstrap-checklist.md` does carry a `## Release` section
   (version source, changelog, tag convention, release process), but no
   step of the workflow routes the reader to it, and
   `workflows/release.md` is never reached from bootstrap.

## Evidence

Bootstrapping and publishing a Claude Code plugin marketplace (a
documentation-only repository, single maintainer, Stage 1). The bootstrap
produced README, LICENSE, SECURITY, CONTRIBUTING, `.gitignore`, CI and a
changelog, and the repository was pushed public and installed successfully
by the CLI — which reads a `version` field from the plugin manifest.

At that point the repository had: a version in the manifest, a changelog
with no `[Unreleased]` section, **no tag**, **no release**, and two
subsequent fix commits that existed in no version at all. The owner noticed,
not the skill. The gap was the workflow's, not the checklist's.

## Why this belongs in Project Steward

Team size and distribution are independent. A one-person repository that
publishes a plugin, a package, a container image or a GitHub Action has
consumers who need versions, a changelog and tags; a five-person internal
service with no external consumer may legitimately not. Keying release
discipline to contributor count gets both cases wrong, and it will get them
wrong in every repository that publishes.

## Proposed change

Add a publication trigger, independent of stage.

1. `references/scaling-model.md` — a short section: when a repository
   publishes an artifact others install, release discipline applies at
   whatever stage it is at (version source, `CHANGELOG.md` with an
   `[Unreleased]` section, annotated tags, release notes), even at Stage 0
   or 1. Stage still governs everything else.
2. `workflows/project-bootstrap.md` — in step 3, note that a publishing
   repository takes the release items whatever its stage; and a new step
   before the health summary: if the repository publishes, hand off to
   `workflows/release.md` and cut the first release before declaring the
   bootstrap complete. The health summary reports the released version.
3. `references/bootstrap-checklist.md` — add `[Unreleased] section present`
   and `initial release tagged and published` to the `## Release` section.

No existing rule is weakened or removed.

## Files affected

- `references/scaling-model.md`
- `workflows/project-bootstrap.md`
- `references/bootstrap-checklist.md`
- `CHANGELOG.md`
- `VERSION`

## Compatibility impact

Additive. Repositories that publish nothing are unaffected — the trigger
does not fire. Repositories that do publish gain checklist items they were
already expected to satisfy under `references/release-policy.md`, which
this only routes them to.

## Security impact

None directly. Marginally positive: tagged releases make it possible to say
which published version carries a security fix.

## Risks

- Over-triggering: "publishes an artifact others install" could be read to
  cover any public repository. The wording names the case — something
  installed or depended upon by a consumer — and a public repository that
  is only read does not qualify.
- Ceremony on a scratch experiment. Mitigated by keeping the trigger to the
  four release items and leaving every other stage control alone.

## Validation plan

Re-run the bootstrap workflow against a repository that publishes an
installable artifact and confirm the run ends with a tagged, released
version and an `[Unreleased]` section, rather than at the health summary.

## Rollback plan

`git revert` the implementing commit. The change is documentation only; no
repository bootstrapped in the meantime is left in a broken state, since
the items it adds are additive.

## Versioning rationale

MINOR: new mandatory behavior for a class of repositories, no existing rule
changed or removed.
