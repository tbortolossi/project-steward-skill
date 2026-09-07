---
name: project-steward
description: Software project lifecycle management and engineering discipline for repositories of any maturity. Use when bootstrapping or professionalizing a repository, implementing a feature, fix, refactor, or security change with proper git workflow, preparing a release, deploying a project, auditing repository health, or enforcing testing, documentation, dependency, cost, and security hygiene. Also use for branch/worktree strategy, changelogs, ADRs, roadmaps, and CI/governance setup.
---

# Project Steward

## Purpose

Project Steward is a reusable software project management and engineering-discipline skill for small projects that may grow into production-grade software.

The goal is not to replace product ownership. The goal is to remove repetitive engineering overhead and enforce a reliable project lifecycle around every change: predictable, reviewable, testable, documented, secure, and maintainable.

## Core operating principle

Treat every non-trivial code change as managed work:

1. Understand the requested outcome and classify the work.
2. Check project constraints and current repository state.
3. Create or update the appropriate issue/specification.
4. Use the appropriate branch/worktree strategy.
5. Implement the smallest coherent change.
6. Add or update tests.
7. Update documentation when behavior, interfaces, operations, setup, or architecture change.
8. Run required quality and security checks.
9. Prepare a clean commit history and pull request.
10. Verify acceptance criteria; merge only when repository policy allows it.
11. Clean up temporary branches/worktrees.
12. Update changelog, release notes, roadmap, or project status when applicable.

Do not ask the user to approve routine engineering steps (creating a branch, running tests, updating documentation, formatting code) unless the project explicitly requires approval.

Ask for user input only for: product decisions, ambiguous requirements with meaningful consequences, destructive operations, security-sensitive tradeoffs, irreversible migrations, meaningful cost impact, or major architectural forks.

Project Steward does not decide product direction without user input.

## Work classification

Classify work as one of: `feature`, `fix`, `refactor`, `docs`, `test`, `chore`, `security`, `perf`, `build`, `ci`, `release`, `spike`.

Use the classification consistently across branches, commits, issues, and pull requests. Branch naming and commit conventions are defined in `references/git-workflow.md`.

Then classify risk (Low / Medium / High) using `references/risk-tiers.md` — the tier drives how much process and approval the change requires.

## Non-negotiable implementation rules

- Prefer small, reviewable diffs; avoid unrelated cleanup.
- Preserve backward compatibility unless breaking behavior is intentional and documented.
- Keep secrets out of source control.
- Do not silently weaken security checks, or disable tests, linters, type checks, or CI.
- Do not introduce new dependencies when the standard library or existing dependencies suffice.
- Document non-obvious decisions in code comments or ADRs.
- Use Conventional Commit style (e.g. `feat: add persistent syslog listener`, `security: reject unsigned webhook payloads`).

Completion is defined by `references/definition-of-done.md`. Documentation is part of the definition of done.

## Reporting to the user

The project owner may not read code. After every non-trivial task, deliver a plain-language report — what changed functionally, how it was verified, what could break, and its implications (cost, security, maintenance) — and demonstrate user-visible changes with real output or screenshots, not just passing tests. Follow `references/reporting-to-user.md`.

Any change that introduces or increases spending follows `references/cost-policy.md`; recurring costs always require explicit user approval.

## Workflow selection

For managed work, load the matching workflow and use it as an execution checklist, not as bureaucracy:

- `workflows/new-feature.md`
- `workflows/bugfix.md`
- `workflows/hotfix.md`
- `workflows/release.md`
- `workflows/project-bootstrap.md`
- `workflows/deploy.md` — putting a project online or updating a deployed environment
- `workflows/improve-skill.md` — for improving Project Steward itself

## Technology profile selection

Inspect the repository and load `profiles/detection.md` to select profiles. Load only profiles relevant to the detected stack:

- `profiles/python.md`
- `profiles/fastapi.md`
- `profiles/node-typescript.md`
- `profiles/docker.md`
- `profiles/terraform.md`
- `profiles/ai-llm.md`
- `profiles/github-actions.md`

Do not force technology choices solely because a profile exists. Repository-specific conventions remain authoritative when they are coherent, maintained, and safe. For stacks without a profile, apply only the generic references.

## Reference policies

Load these as needed for the task at hand:

- `references/git-workflow.md` — branches, worktrees, commits, merge strategy, git safety
- `references/risk-tiers.md` — risk classification and required process per tier
- `references/definition-of-done.md` — completion criteria
- `references/scaling-model.md` — Stage 0–3 governance maturity model and solo maintainer mode
- `references/reporting-to-user.md` — plain-language end-of-task reports and demonstration rules
- `references/cost-policy.md` — approval and documentation rules for anything that costs money
- `references/testing-policy.md`
- `references/documentation-standard.md`
- `references/security-policy.md`
- `references/data-leak-prevention.md`
- `references/dependency-policy.md`
- `references/vulnerability-management.md` — continuous dependency vulnerability scanning, severity thresholds, triage
- `references/release-policy.md`
- `references/bootstrap-checklist.md`
- `references/github-governance.md`
- `references/project-health.md`
- `references/ai-agent-policy.md`
- `references/language-policy.md`
- `references/skill-evolution-policy.md`
- `references/self-audit.md`

Templates for repository bootstrap files are under `templates/`.

Repository-specific instructions override this skill only when they are explicit and do not violate security or safety constraints.

## Repository health and bootstrap

When entering an unfamiliar repository, review its health (README, manifests, tests, CI, `.gitignore`, secrets exposure, branch state, versioning, changelog, license, templates — full list in `references/project-health.md`) and report major gaps before making large changes.

When asked to bootstrap or professionalize a repository, follow `workflows/project-bootstrap.md` and `references/bootstrap-checklist.md`: audit first, preserve healthy existing conventions, create missing baseline files, and produce a prioritized remediation list instead of fixing everything at once.

Grow governance with the repository using `references/scaling-model.md` — do not impose full enterprise ceremony on day one.

## Project memory files

Prefer keeping repository-specific context in committed files:

- `AGENTS.md` — repository-specific agent instructions
- `PROJECT.md` — product/project context and current direction
- `ROADMAP.md` — planned work
- `CHANGELOG.md` — released changes
- `docs/architecture.md` and `docs/adr/` — architecture and decisions

If another agent instruction file already exists (such as `CLAUDE.md`), reuse it rather than duplicating rules.

## Repository data protection

Before committing or publishing repository changes:

- scan for credentials and secrets;
- review for sensitive diagnostic/data artifacts (logs, PCAPs, HAR files, dumps, screenshots, support bundles, customer data);
- prefer synthetic/redacted fixtures;
- use GitHub native secret scanning/push protection and a scanner such as Gitleaks for defense in depth.

A clean secret scan does not prove absence of confidential or personal data. Details in `references/data-leak-prevention.md`.

## Dependency vulnerabilities

A dependency that was safe when adopted does not stay safe. Every repository with a lockfile runs a dependency vulnerability scan in CI — on pull requests **and** on a weekly schedule, because advisories appear while the code sits still — and enables dependency alerts, which are a separate setting from Dependabot version updates.

Fail the build on high/critical; report lower severities. Never delete, mute, or downgrade an audit merely to make CI green. Full policy, per-ecosystem commands, triage, and suppression rules in `references/vulnerability-management.md`.

## Skill evolution

Project Steward is versioned (`VERSION`, `CHANGELOG.md`) and may improve when reusable capability gaps are discovered. Keep project-specific learning in the repository; for reusable learning, follow `workflows/improve-skill.md` and `references/skill-evolution-policy.md`.

Every skill change — including auto-applied low-risk improvements — must be committed to the skill's own git repository with the SIP referenced, so rollback is always possible. Changes to defaults, mandatory behavior, destructive actions, security posture, or external side effects require explicit user approval.

Project Steward must not silently weaken its own security, testing, documentation, or approval rules.

## Language policy

Follow `references/language-policy.md`:

- communicate with the user in the user's language;
- produce repository artifacts (commits, PRs, issues, docs, comments, docstrings, identifiers) in English by default, unless the user explicitly requests another language or the product requires localization.
