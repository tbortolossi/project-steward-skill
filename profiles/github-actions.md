# Profile: GitHub Actions

Apply when GitHub Actions is used or a GitHub-hosted CI baseline is needed.

## Baseline pipeline

For application repositories, prefer jobs for:

- dependency installation;
- lint/format check;
- tests;
- type checks where configured;
- build/package verification.

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
