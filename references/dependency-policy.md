# Dependency Policy

## Principle

Every dependency becomes part of the maintenance and security surface.

## Before adding a dependency

Check:

- Is it necessary?
- Can an existing dependency do the job?
- Can the standard library do the job cleanly?
- Is the project actively maintained?
- Is the license acceptable?
- Is the package reputable?
- Are there known critical vulnerabilities?
- Is the dependency footprint reasonable?

## Versioning

Prefer reproducible dependency resolution.

Use lockfiles when the ecosystem supports them.

Avoid unconstrained production dependencies.

## Updates

Classify dependency updates as:

- routine patch/minor;
- security update;
- breaking major update.

Major updates require compatibility review and targeted tests.

## Vulnerability monitoring

The questions above are answered once, when the dependency is adopted. They do not stay answered.

Ongoing exposure — scheduled scanning, severity thresholds, triage, suppression rules, and what to
do when no patched version exists — is governed by `references/vulnerability-management.md`. Every
repository with a lockfile runs a dependency vulnerability scan in CI and on a weekly schedule.
