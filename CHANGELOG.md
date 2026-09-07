# Project Steward Changelog

All notable changes to Project Steward are documented here.

Project Steward follows Semantic Versioning.

## [Unreleased]

## [0.8.0] - 2026-09-07

Closes the gap where Project Steward asked about dependency vulnerabilities but never checked for them automatically. See `docs/skill-improvements/SIP-0001-dependency-vulnerability-scanning.md`.

### Added

- `references/vulnerability-management.md`: continuous dependency vulnerability scanning — severity-based response, per-ecosystem tooling, mandatory weekly scheduled scans, triage order, suppression rules (named advisory, stated reason, expiry date), and the explicit limits of dependency scanning.
- `templates/.github/workflows/dependency-audit.yml` (Python/uv + `pip-audit`) and `templates/.github/workflows/dependency-audit-node.yml` (`npm audit`), both triggered on pull request, on push to the default branch, weekly on a schedule, and manually. These are the skill's first scheduled workflow templates.
- `docs/skill-improvements/` for accepted SIPs, starting with SIP-0001.
- Definition of Done item: no new high/critical dependency advisory introduced by the change.
- Concrete audit commands in `profiles/python.md` and `profiles/node-typescript.md`; container image scanning promoted from a Stage 3 suggestion to a baseline expectation in `profiles/docker.md`.
- "Scheduled security jobs" section in `profiles/github-actions.md`, with dependency audit and secret scan added to the baseline pipeline.
- "Dependency alerts" section in `references/github-governance.md` separating Dependabot *version updates* (routine upgrade PRs, configured by `dependabot.yml`) from Dependabot *alerts* (a repository setting that must be enabled explicitly, and which the config file does not provide).

### Changed

- `SKILL.md`: new "Dependency vulnerabilities" section and `references/vulnerability-management.md` wired into the reference list.
- `references/dependency-policy.md`: vulnerability checks are no longer a one-time question asked at adoption; ongoing monitoring is now explicit.
- `references/bootstrap-checklist.md`: vague "security checks where useful" replaced by a secret scan and a scheduled dependency vulnerability scan; Dependabot alerts added as a separate checklist item.
- `references/scaling-model.md`: dependency scanning and alerts moved from Stage 3 "security scanning" down to Stage 1; Stage 3 now covers image scanning, SBOM, and application security scanning.
- `references/project-health.md`: dependency and security review now name the audit command and require reviewing accumulated suppressions.
- `references/security-policy.md`: dependency security extended past adoption; explicit prohibition on muting an audit to make CI green.
- `workflows/release.md`: releases require a freshly run dependency audit, since the last CI run may predate a new advisory.
- `templates/.github/dependabot.yml`: header comment clarifying that the file provides version updates only, not alerts and not a merge gate.

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
