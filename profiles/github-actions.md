# Profile: GitHub Actions

Apply when GitHub Actions is used or a GitHub-hosted CI baseline is needed.

## Baseline pipeline

For application repositories, prefer jobs for:

- dependency installation;
- lint/format check;
- tests;
- type checks where configured;
- build/package verification;
- secret scan;
- dependency vulnerability audit.

## Scheduled security jobs

Checks that depend on external data going stale — dependency audits above all — must also run on a
`schedule:` trigger, weekly at minimum, plus `workflow_dispatch` for on-demand runs.

A pull-request-only trigger silently stops protecting a repository as soon as the repository stops
changing. Templates: `templates/.github/workflows/dependency-audit.yml` and
`dependency-audit-node.yml`. Policy: `references/vulnerability-management.md`.

## Security

- pin actions to stable major versions at minimum; stronger pinning may be appropriate for high-security repositories;
- use least-privilege `permissions`;
- do not print secrets;
- avoid untrusted pull-request code accessing privileged secrets;
- review third-party actions before adoption.

## Efficiency

Use dependency caching when safe and worthwhile.

Avoid duplicated expensive jobs.

## Release automation

Separate release permissions from ordinary CI where practical.
