# Workflow: Release

## Release preparation

1. Confirm target version.
2. Review `Unreleased` changelog entries.
3. Confirm CI is green.
4. Confirm required security checks pass, including a freshly run dependency vulnerability audit — the last CI run may predate a newly published advisory (`references/vulnerability-management.md`).
5. Confirm install/upgrade instructions.
6. Confirm migration steps.
7. Confirm breaking changes are explicit.
8. Confirm version metadata is consistent.

## Version selection

Use Semantic Versioning:

- PATCH for backward-compatible fixes;
- MINOR for backward-compatible features;
- MAJOR for breaking changes.

## Release artifacts

Where relevant:

- package/binary/container image;
- checksum;
- SBOM;
- signed artifact;
- release notes.

## Tagging

Use:

`vMAJOR.MINOR.PATCH`

Do not move an already-published tag.

## Post-release

- verify published artifacts;
- verify installation or deployment smoke test;
- update documentation links if versioned;
- close milestone/issues;
- create follow-up issues for deferred work.
