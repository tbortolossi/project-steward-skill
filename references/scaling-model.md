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

## Stage 1 — Personal project

Add:

- LICENSE
- CONTRIBUTING
- SECURITY
- tests
- lint/format
- `.env.example`
- CI
- dependency vulnerability scan in CI, on pull requests and weekly
- dependency alerts enabled
- issue/PR templates

## Stage 2 — Shared project

Add:

- CODEOWNERS
- changelog
- release policy
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

## Stage 3 — Production project

Add:

- threat model where relevant
- release automation
- SBOM where relevant
- container image scanning and documented remediation timeframes per severity
- application security scanning beyond dependencies (SAST, secrets, IaC)
- observability
- backup/recovery
- deployment runbooks
- incident procedures
- compatibility/deprecation policy
- SLO/SLA considerations
- ownership and escalation
