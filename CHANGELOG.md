# Project Steward Changelog

All notable changes to Project Steward are documented here.

Project Steward follows Semantic Versioning.

## [Unreleased]

## [0.16.0] - 2026-10-12

States the intent behind the secrets rules: secrets belong in a vault,
so `.env` becomes plain configuration the agent may read and edit.
Details in `docs/skill-improvements/SIP-0009-vault-first-env.md`.

### Changed

- `references/secrets-management.md`: "aim for a vault, not `.env`";
  where `.env` holds no secret the agent reads and edits it and the
  `.env` deny rules are left out; at rung 1 the old rules and
  `set_env.py` still apply, with a nudge toward rung 2.
- `references/claude-code.md`, `templates/AGENTS.md`,
  `workflows/project-inception.md`: same rule; inception aims for rung 2
  or above.

## [0.15.1] - 2026-10-12

### Fixed

- Python bytecode files committed by mistake in 0.15.0 are
  removed, and bytecode is now ignored.

## [0.15.0] - 2026-10-12

The agent can now write non-secret settings into `.env` without reading
it. Details in `docs/skill-improvements/SIP-0008-env-write-without-read.md`.

### Added

- `scripts/set_env.py`: add, replace (`--header` titles new ones) or remove
  (`--unset`, with their comments) `.env` variables by name, print
  names only, `--check` for presence; refuses secret-looking names and
  values; keeps comments, other lines and file permissions. Unit tests
  run in CI.

### Changed

- `references/secrets-management.md`, `references/claude-code.md`,
  `templates/AGENTS.md`: the agent may write non-secret settings to
  `.env` through `set_env.py`; reading `.env` stays forbidden and secret
  values stay the owner's.
- `templates/.claude/settings.json`: allow rule for `set_env.py`. The
  `Read(.env)` deny rules are unchanged.

## [0.14.1] - 2026-10-12

CI templates that fail on first use are fixed. Details in
`docs/skill-improvements/SIP-0007-ci-template-fixes.md`.

### Fixed

- `templates/.github/workflows/python-ci.yml` and `dependency-audit.yml`:
  `astral-sh/setup-uv@v10` does not exist; pinned to `v10.2.0`.
- `templates/.github/workflows/gitleaks.yml`: grant `pull-requests: read`,
  without which the secret scan fails with 403 on every pull request.

### Changed

- `profiles/github-actions.md`: check that every `uses:` reference exists
  before committing a workflow.

## [0.14.0] - 2026-10-12

Start new projects from an idea on solid ground: a short product brief
with numbered requirements, a recorded stack decision, a milestone plan,
a secrets mechanism matched to the stage, documentation rules, and a
Claude Code setup that keeps secret files away from the agent. Details in
`docs/skill-improvements/SIP-0006-inception-secrets-documentation.md`.

### Added

- `workflows/project-inception.md`: idea → questions → `PROJECT.md` brief
  (`FR`/`NFR` with acceptance criteria) → stack ADR → `ROADMAP.md`
  milestones → bootstrap → walking skeleton.
- `references/secrets-management.md`: four rungs (`.env`, password-manager
  injection, sops/age, secret manager such as Vault) by stage; CI secrets
  and OIDC; agent rules; rotation.
- `templates/.claude/settings.json`: deny rules for secret files and cloud
  credentials, read-only allow rules.
- `references/claude-code.md`: "Project setup", including what deny rules
  do not cover.
- `scripts/check_skill.py`: JSON templates must parse.

### Changed

- `references/documentation-standard.md`: "What goes where" table,
  writing rules, ADR immutability, keeping documentation current.
- Stage 1 (`references/scaling-model.md`, `workflows/project-bootstrap.md`,
  `references/bootstrap-checklist.md`) now includes `PROJECT.md`,
  `ROADMAP.md`, `CHANGELOG.md` with a version source, ADRs, a chosen
  secrets mechanism, a CI secret scan and `.claude/settings.json`.
  Stage 2 and 3 gain shared-secret and secret-manager requirements.
- `templates/PROJECT.md` is a product brief; `templates/ROADMAP.md` uses
  milestones; `templates/AGENTS.md` cites requirements and keeps agents
  away from secret files.
- `workflows/new-feature.md`, `references/project-health.md`,
  `references/security-policy.md`: requirement IDs, documentation and
  secrets drift checks.
- `SKILL.md`: router entries and triggers for ideas, PRD, documentation
  and secrets.

## [0.13.0] - 2026-10-12

Skill changes the owner asks for are applied, released and installed in
one pass, and older repositories are offered the autonomy section. Details
in `docs/skill-improvements/SIP-0005-owner-requested-upgrades.md`.

### Added

- `references/skill-evolution-policy.md`: "Owner-requested changes" — an
  explicit request is the approval; limits on scope, security weakening,
  self-granted autonomy and harness refusals. "Source and installed
  copies" — change the source, never the installed copy, then
  fast-forward the installed copy after each release.
- `references/ai-agent-policy.md`: when the autonomy section is missing,
  offer to create it with a recommended single-owner preset.
- `references/project-health.md`: "Agent instructions" checks.

### Changed

- `workflows/improve-skill.md`: approval and version steps cover
  owner-requested changes and the installed copy.
- `SKILL.md`: an explicit owner request counts as the approval for a
  skill change (edited by the owner).
- This repository's `AGENTS.md` gains an "Agent autonomy" section,
  written by the owner.

## [0.12.0] - 2026-10-12

Make the skill work as a delegation target in Claude Code: it triggers on
ordinary coding requests, knows what it may do without asking, and its
repository instructions are actually read. Details in
`docs/skill-improvements/SIP-0004-claude-code-integration.md`.

### Added

- `references/claude-code.md`: path convention, AGENTS.md/CLAUDE.md rule,
  mapping of workflow steps to Claude Code tools (task list,
  `AskUserQuestion`, plan mode, worktrees, `gh`), and how autonomy relates
  to the harness and `.claude/settings.json`.
- `references/ai-agent-policy.md`: "Autonomy" — local actions never asked;
  push, pull request, merge, tag, release and non-production deploy
  governed by the repository's "Agent autonomy" section, default `ask`,
  asked once per task; force-push, production deploys, data deletion and
  recurring costs always asked.
- `templates/CLAUDE.md`: `@AGENTS.md` import. Claude Code ignores
  `AGENTS.md` whenever a `CLAUDE.md` exists.
- `templates/AGENTS.md`: "Agent autonomy" section and a line directing
  agents to use the skill for every code change.
- `scripts/check_skill.py`: trigger text within Claude Code's listing
  limit; `templates/CLAUDE.md` imports `AGENTS.md`.

### Changed

- `SKILL.md`: description triggers on outcome-only coding requests;
  `when_to_use` and `argument-hint` added; path rule and autonomy summary;
  data-protection and dependency sections condensed into pointers.
- Bootstrap (`workflows/project-bootstrap.md`,
  `references/bootstrap-checklist.md`, `references/scaling-model.md`):
  `AGENTS.md` with autonomy choices and `CLAUDE.md` at Stage 1.
- `OPERATING-GUIDE.md`, `README.md`: autonomy and Claude Code usage.
- This repository applies the rule to itself: `CLAUDE.md` imports
  `AGENTS.md`.

## [0.11.0] - 2026-09-20

A merged change is not running anywhere until the environments that track
the branch are rebuilt, and nothing said so. Details and evidence in
`docs/skill-improvements/SIP-0003-refresh-environments-after-integration.md`.

### Added

- `references/git-workflow.md`: an "After integration" section. Every
  environment that tracks the integrated branch runs the new version before
  the task is reported done, preferably through a versioned trigger set up
  the first time it is missing, and verified. Production is excluded from
  the automatic path.
- `references/definition-of-done.md`: checklist item and completion
  criterion for environments tracking the integrated branch.
- `workflows/deploy.md`: a "Refresh after integration" step describing the
  versioned-hooks pattern for local previews and the CI-on-push pattern for
  remote environments, with their safety rules.
- `workflows/new-feature.md`, `workflows/bugfix.md`: completion points to
  the after-integration rule.

## [0.10.0] - 2026-09-20

Publishing an artifact and having contributors are independent, and the
maturity model only measured the second. Details and evidence in
`docs/skill-improvements/SIP-0002-publication-triggers-release-discipline.md`.

### Added

- `references/scaling-model.md`: a publication trigger. When a repository
  publishes an artifact others install or depend on, the release items —
  version source, `CHANGELOG.md` with `[Unreleased]`, annotated tags,
  release notes — apply at whatever stage it is at, instead of arriving
  with Stage 2. A public repository that is only read does not qualify.
- `workflows/project-bootstrap.md`: a release step before the health
  summary, handing off to `workflows/release.md`. The workflow previously
  created files, audited, and stopped — it never mentioned a release, a tag
  or a version, so a repository could be bootstrapped, published and
  installed while its version existed in no tag. The health summary now
  reports the released version.
- `references/bootstrap-checklist.md`: `[Unreleased]` section present, and
  initial release tagged and published.

## [0.9.0] - 2026-09-07

The skill now applies its own rules to itself, plus the first self-audit. Findings and evidence in `docs/audits/2026-09-07-self-audit.md`.

### Security

- Updated every stale pinned version. All were behind upstream, several by multiple majors, and because these live in `templates/` the staleness propagated into every repository bootstrapped from them: `actions/checkout` v4→v7, `actions/setup-python` v5→v7, `actions/setup-node` v4→v7, `astral-sh/setup-uv` v6→v10, `gitleaks/gitleaks-action` v2→v3, `gitleaks` pre-commit v8.28.0→v8.30.1, `ruff-pre-commit` v0.12.11→v0.16.6. The `setup-uv` and `ruff-pre-commit` upgrades were verified against upstream (`enable-cache` input and `ruff-check`/`ruff-format` hook ids still present) rather than assumed compatible.
- `references/self-audit.md`: new obsolescence question covering pinned versions in `templates/`, and why Dependabot is structurally blind to them — it scans a repository's real `.github/workflows/`, not workflow files inside a templates directory.

### Added

- CI for the skill repository itself: `.github/workflows/ci.yml` (structural checks), `.github/workflows/gitleaks.yml` (secret scan, on schedule), `.github/dependabot.yml` (GitHub Actions ecosystem).
- `scripts/check_skill.py`: verifies templates parse as YAML, internal references resolve, `SKILL.md` keeps the frontmatter Claude Code needs for discovery, `VERSION` agrees with `CHANGELOG.md`, and every router entry points at a real file. Validated by deliberately breaking four things and confirming each was caught.
- `AGENTS.md` for the skill repository, recording the constraints that are easy to violate here: SKILL.md stays a router, template pins go stale silently, stage definitions must agree across files.
- `docs/audits/` with the first self-audit report.

### Fixed

- `workflows/project-bootstrap.md` contradicted itself: step 2 classified the repository into Stage 0–3 and warned against imposing Stage 3 controls on a Stage 0 experiment, then step 3 listed a flat fifteen-file baseline ignoring that classification. Following it literally buried every scratch experiment in Stage 2 governance. Step 3 is now stage-aware, with `references/scaling-model.md` as the authority.
- `OPERATING-GUIDE.md` was referenced from nowhere and effectively invisible; it is now listed in `README.md` and covered by the reference check.

### Changed

- `README.md`: documents the repository's own development commands, as the skill requires of every project.

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
