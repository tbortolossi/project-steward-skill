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
- [ ] secrets mechanism chosen and documented in the README (`references/secrets-management.md`)

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
- [ ] `AGENTS.md` with an "Agent autonomy" section filled with the owner's choices
- [ ] `CLAUDE.md` importing `@AGENTS.md` when Claude Code is used
- [ ] `.claude/settings.json` denying access to secret files, when Claude Code is used

## CI

- [ ] install dependencies
- [ ] lint
- [ ] test
- [ ] build/package if relevant
- [ ] secret scan
- [ ] dependency vulnerability scan, on pull requests and on a weekly schedule

## Documentation

- [ ] `PROJECT.md`: vision, users, numbered requirements, non-goals, security and privacy
- [ ] `ROADMAP.md`: milestones with requirement IDs and exit criteria
- [ ] first ADR (stack choice) for a project started from an idea
- [ ] architecture overview
- [ ] configuration reference
- [ ] troubleshooting
- [ ] roadmap
- [ ] changelog
- [ ] ADR folder

## GitHub automation

- [ ] CI workflow
- [ ] Dependabot version updates or equivalent dependency automation
- [ ] Dependabot alerts enabled — a separate repository setting; version updates do not provide it
- [ ] scheduled dependency audit workflow
- [ ] Gitleaks or equivalent secret scanner
- [ ] native GitHub secret scanning enabled when available
- [ ] push protection enabled when available
- [ ] sensible branch protection for maturity stage

## Security

- [ ] secret handling
- [ ] sensitive-data leak review
- [ ] dangerous artifact/file patterns excluded or reviewed
- [ ] no tracked credentials
- [ ] dependency review at adoption
- [ ] continuous dependency vulnerability monitoring (`references/vulnerability-management.md`)
- [ ] least privilege
- [ ] security reporting process

## Release

- [ ] version source defined
- [ ] SemVer policy
- [ ] changelog
- [ ] tag convention
- [ ] release process
- [ ] `[Unreleased]` section present in the changelog
- [ ] initial release tagged and published, if the repository publishes an artifact

## Scaling

Do not enable every possible governance mechanism immediately.

Add controls when project complexity, number of contributors, deployment risk, or user impact justifies them.
