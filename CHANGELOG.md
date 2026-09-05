# Project Steward Changelog

All notable changes to Project Steward are documented here.

Project Steward follows Semantic Versioning.

## [Unreleased]

## [0.7.0] - 2026-09-05

### Added

- `references/reporting-to-user.md`: mandatory plain-language end-of-task reports and "show, don't tell" demonstration of user-visible changes, designed for owners who do not read code.
- `references/cost-policy.md`: approval, estimation, documentation, and cleanup rules for anything that costs money; recurring costs always require explicit user approval.
- `workflows/deploy.md`: deployment workflow covering environments, production secrets, post-deploy verification, rollback, and minimum operations.
- `profiles/node-typescript.md` with detection in `profiles/detection.md`.
- Solo maintainer mode in `references/scaling-model.md`: agent self-verification plus owner behavior validation replaces human code review in single-maintainer repositories.
- `templates/LICENSE-MIT` and `templates/CODEOWNERS`, closing the gap between the Stage 1/2 requirements and the available templates.
- MIT `LICENSE` for the skill repository itself.

### Changed

- `SKILL.md`: new "Reporting to the user" section; wired the new workflow, profile, and references; frontmatter description now covers deployment and cost hygiene.

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
