# Project Steward Changelog

All notable changes to Project Steward are documented here.

Project Steward follows Semantic Versioning.

## [Unreleased]

## [0.6.0] - 2026-09-05

### Added

- YAML frontmatter (`name`, `description`) in `SKILL.md` for Agent Skills auto-discovery in Claude Code.
- `references/definition-of-done.md`, `references/risk-tiers.md`, `references/scaling-model.md` extracted from `SKILL.md`.
- Detection fallback guidance for stacks without a profile (Node/TypeScript, Go, Rust, others).
- Concrete installation instructions in `README.md`.
- Requirement that every skill change, including auto-applied low-risk improvements, is committed to the skill's own git repository.

### Changed

- Rewrote `SKILL.md` as a compact router (~165 lines instead of ~530): detailed policies now live in `references/`, removing duplication with `workflows/`.
- Consolidated the authoritative branch-prefix list in `references/git-workflow.md`, aligned with the 12 work-classification categories.
- Fixed structural Markdown issues in `SKILL.md` (orphaned reference list, malformed `---` separators, missing `workflows/improve-skill.md` in workflow selection).

### Fixed

- The skill repository is now itself a git repository, making the rollback guarantee of the skill-evolution policy actually enforceable.

## [0.5.0] - 2026-08-31

### Added

- Language policy separating conversational language from repository artifact language.
- English-by-default policy for documentation, issues, pull requests, commits, code comments, docstrings, and identifiers.

## [0.4.0] - 2026-08-31

### Added

- Controlled skill self-improvement policy.
- Skill Improvement Proposal workflow and template.
- Low/medium/high risk classification for skill evolution.
- Local-versus-global learning rules.
- Skill versioning and rollback expectations.

## [0.3.0] - 2026-08-31

### Added

- GitHub governance guidance.
- Secret scanning and sensitive-data leak prevention.
- Gitleaks CI/pre-commit baseline.
- Python `uv` baseline.
- Project health review.

## [0.2.0] - 2026-08-31

### Added

- Reusable workflows.
- Technology profiles.
- Automatic stack/profile detection.

## [0.1.0] - 2026-08-31

### Added

- Initial Project Steward lifecycle.
- Git, testing, documentation, security, release, and bootstrap guidance.
