# Release and Versioning Policy

## Versioning

Use Semantic Versioning by default:

`MAJOR.MINOR.PATCH`

- MAJOR: incompatible change
- MINOR: backward-compatible feature
- PATCH: backward-compatible fix

Pre-1.0 projects may move faster, but breaking changes must still be documented.

## Changelog

Maintain `CHANGELOG.md`.

Prefer sections:

- Added
- Changed
- Deprecated
- Removed
- Fixed
- Security

Keep an `Unreleased` section.

## Release readiness

Before a release:

- all required CI checks pass;
- version is updated;
- changelog is updated;
- migrations are documented;
- breaking changes are explicit;
- security-relevant fixes are called out appropriately;
- installation and upgrade instructions are current;
- artifacts can be reproduced where practical.

## Tags

Use annotated release tags where practical:

`v1.4.0`

Do not reuse or silently move published release tags.

## Deprecation

For public interfaces:

1. mark deprecated behavior;
2. document replacement;
3. provide migration guidance;
4. remove only in an appropriate breaking release.
