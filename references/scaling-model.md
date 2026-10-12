# Small Idea to Large Project Scaling Model

Governance should grow with the repository. Evolve the stage when risk, contributors, users, or operational importance increase — do not impose full enterprise ceremony on day one, and do not leave a production project at scratch-level hygiene.

## Stage 0 — Scratch

Use only for disposable experiments.

Minimum:

- README
- `.gitignore`
- dependency manifest
- basic run instructions

Do not pretend scratch code is production-ready.

A project the owner starts from an idea and means to keep is not Stage 0: start it with
`workflows/project-inception.md`, which sets it up at Stage 1.

## Stage 1 — Personal project

Add:

- LICENSE
- CONTRIBUTING
- SECURITY
- `PROJECT.md` (product brief with numbered requirements) and `ROADMAP.md` (milestones), kept short
- `CHANGELOG.md` with an `[Unreleased]` section, and a version source starting at `0.1.0`
- an ADR for each decision that is expensive to reverse — the stack choice is the first
- tests
- lint/format
- `.env.example`, and a secrets mechanism chosen and documented (`references/secrets-management.md`, rung 1 or 2)
- CI
- secret scan in CI (Gitleaks or equivalent)
- dependency vulnerability scan in CI, on pull requests and weekly
- dependency alerts enabled
- issue/PR templates
- agent instructions: `AGENTS.md` with an "Agent autonomy" section, imported by `CLAUDE.md` when Claude Code is used, and `.claude/settings.json` from `templates/.claude/settings.json` (`references/claude-code.md`, "Project setup")

## Stage 2 — Shared project

Add:

- CODEOWNERS
- release policy
- secrets shared between people or machines through encrypted files or a secret manager (rung 3 or 4), never sent by chat or email
- ADRs
- branch protection
- dependency automation
- architecture documentation
- operational/troubleshooting guide

## Solo maintainer mode

At any stage, when the repository has a single maintainer and no human code reviewers:

- Pull requests remain useful as checkpoints, but their purpose shifts: the agent summarizes and self-verifies the change instead of waiting for human code review.
- Human review is replaced by the plain-language report and demonstration defined in `references/reporting-to-user.md` — the owner validates behavior, not code.
- Skip team-only ceremony (CODEOWNERS, review-approval gates) until a second contributor exists.
- Everything else still applies: tests, documentation, security checks, and approval rules for high-risk changes do not relax in solo mode.

## Publishing changes the requirement, at any stage

Stage measures how many people build the repository. It says nothing about
whether anyone *installs* what it produces. These are independent, and a
one-person Stage 1 repository that publishes a plugin, a package, a
container image or an action has consumers who need to know which version
they have and what changed in it.

When a repository publishes an artifact others install or depend on, the
release items apply whatever its stage:

- a defined version source, and SemVer;
- `CHANGELOG.md` with an `[Unreleased]` section, even at Stage 0;
- annotated tags on released versions;
- release notes where the platform has them.

A public repository that is only read does not qualify. Stage still governs
everything else: publishing does not pull a scratch experiment into Stage 2
ceremony.

## Stage 3 — Production project

Add:

- threat model where relevant
- release automation
- SBOM where relevant
- container image scanning and documented remediation timeframes per severity
- application security scanning beyond dependencies (SAST, secrets, IaC)
- secrets in a secret manager (rung 4) with documented rotation, and OIDC federation instead of long-lived CI keys
- observability
- backup/recovery
- deployment runbooks
- incident procedures
- compatibility/deprecation policy
- SLO/SLA considerations
- ownership and escalation
