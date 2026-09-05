# Repository Bootstrap Checklist

Use this checklist when creating or professionalizing a repository.

## Repository essentials

- [ ] README
- [ ] LICENSE
- [ ] `.gitignore`
- [ ] `.editorconfig`
- [ ] dependency manifest
- [ ] lockfile if applicable
- [ ] `.env.example` if configuration is needed

## Development

- [ ] documented setup
- [ ] documented run command
- [ ] formatter
- [ ] linter
- [ ] tests
- [ ] type checking if useful
- [ ] local developer commands

## GitHub/project workflow

- [ ] issue templates
- [ ] pull request template
- [ ] CONTRIBUTING
- [ ] SECURITY
- [ ] CODEOWNERS when shared
- [ ] branch protection guidance

## CI

- [ ] install dependencies
- [ ] lint
- [ ] test
- [ ] build/package if relevant
- [ ] security checks where useful

## Documentation

- [ ] architecture overview
- [ ] configuration reference
- [ ] troubleshooting
- [ ] roadmap
- [ ] changelog
- [ ] ADR folder

## GitHub automation

- [ ] CI workflow
- [ ] Dependabot or equivalent dependency automation
- [ ] Gitleaks or equivalent secret scanner
- [ ] native GitHub secret scanning enabled when available
- [ ] push protection enabled when available
- [ ] sensible branch protection for maturity stage

## Security

- [ ] secret handling
- [ ] sensitive-data leak review
- [ ] dangerous artifact/file patterns excluded or reviewed
- [ ] no tracked credentials
- [ ] dependency review
- [ ] least privilege
- [ ] security reporting process

## Release

- [ ] version source defined
- [ ] SemVer policy
- [ ] changelog
- [ ] tag convention
- [ ] release process

## Scaling

Do not enable every possible governance mechanism immediately.

Add controls when project complexity, number of contributors, deployment risk, or user impact justifies them.
