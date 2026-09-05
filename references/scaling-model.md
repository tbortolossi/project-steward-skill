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

## Stage 3 — Production project

Add:

- threat model where relevant
- release automation
- SBOM where relevant
- security scanning
- observability
- backup/recovery
- deployment runbooks
- incident procedures
- compatibility/deprecation policy
- SLO/SLA considerations
- ownership and escalation
