# GitHub Governance

## Goal

GitHub should enforce the project's engineering policy rather than merely host code.

## Repository settings

Recommended for shared or important repositories:

- protect the default branch;
- require pull requests for non-trivial changes;
- require CI checks before merge;
- prevent force pushes to protected branches;
- prevent branch deletion where appropriate;
- enable automatic branch deletion after merge;
- enable Dependabot alerts and Dependabot security updates;
- enable secret scanning where available;
- enable push protection where available.

## Dependency alerts

Dependabot **alerts** and Dependabot **version updates** are different features and are routinely
confused.

- Version updates are configured by `.github/dependabot.yml` and open routine upgrade pull requests.
  They are hygiene, not security, and they do not report vulnerabilities.
- Alerts are a repository setting (Security → Code security). They match the lockfile against the
  advisory database and, with security updates enabled, open targeted fix pull requests.

Enable alerts explicitly. Committing a `dependabot.yml` does not enable them.

Alerts are also not a merge gate: they fire after code lands. Pair them with the dependency audit job
in CI defined by `references/vulnerability-management.md`, which blocks new exposure before merge.

## Secret scanning

Use GitHub native secret scanning and push protection when the repository/account plan supports them.

Push protection is preventative: it can block supported credentials before they are pushed.

Native secret scanning is not a complete sensitive-data/DLP solution. Supplement it with repository checks for files and content that may contain confidential data but are not credentials.

## Sensitive data

Treat the following as potentially sensitive unless explicitly intended for publication:

- production logs;
- packet captures;
- database exports;
- customer datasets;
- support bundles;
- configuration backups;
- cloud metadata dumps;
- authentication traces;
- private API responses;
- personally identifiable information;
- internal hostnames/IP plans when considered confidential;
- architecture exports;
- screenshots containing credentials or customer information.

Before committing such artifacts, ask whether they are necessary and whether they can be sanitized or replaced by synthetic examples.

## Branch protection

For Stage 2/3 projects, recommend:

- pull request required;
- required CI checks;
- conversation resolution;
- no force pushes;
- no bypass by default;
- optional required review depending on contributor count and risk.

Do not make a single-maintainer personal repository unusable by requiring reviews that cannot be satisfied.
