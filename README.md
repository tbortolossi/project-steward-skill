# Project Steward Skill

A reusable software-project stewardship skill for AI-assisted development.

It provides a lightweight but scalable operating model for repositories that may begin as small ideas and later grow into shared or production-grade projects.

## Included

- `SKILL.md` — skill entry point (YAML frontmatter + operating model router)
- `references/` — reusable engineering policies
- `workflows/` — step-by-step execution checklists per change type
- `profiles/` — technology-specific baselines with automatic detection
- `templates/` — repository bootstrap files

## Installation

### Claude Code

Copy (or clone) this directory to one of:

- `~/.claude/skills/project-steward/` — available in all your projects
- `<repo>/.claude/skills/project-steward/` — available in one project, shareable with the team

Claude Code discovers the skill through the YAML frontmatter in `SKILL.md`; the `description` field determines when it triggers automatically.

### Other agents (Codex, VS Code agents, …)

Point the agent's instruction mechanism at `SKILL.md`, or paste its content into the agent's system context. The `references/`, `workflows/`, and `profiles/` files are loaded on demand from paths relative to `SKILL.md`.

### Per repository

Copy or adapt selected files from `templates/` into each repository.

Recommended repository-level context:

- `AGENTS.md`
- `PROJECT.md`
- `ROADMAP.md`
- `CHANGELOG.md`
- `docs/architecture.md`
- `docs/adr/`

## Philosophy

Start lightweight. Add governance as risk, contributors, users, or operational importance increase.

The skill intentionally separates reusable engineering discipline from repository-specific product context.

## Security automation

The skill includes defense-in-depth guidance and templates for:

- GitHub secret scanning and push protection;
- Gitleaks;
- pre-commit secret checks;
- CI secret scans;
- sensitive-data/artifact review;
- Dependabot;
- branch protection guidance.

Secret scanning is intentionally treated separately from general sensitive-data detection: credentials can often be detected reliably, while PII/customer/internal-data detection is heuristic and still requires review.


## Self-improvement

Project Steward can evolve when reusable gaps are discovered.

It separates repository-local learning from globally reusable guidance and uses a controlled Skill Improvement Proposal process.

Low-risk, backwards-compatible improvements may be applied automatically. Changes to defaults, security posture, destructive behavior, or mandatory workflow require explicit approval.

The skill itself is versioned through `VERSION` and `CHANGELOG.md`.


## Language behavior

Project Steward communicates with the user in the user's language, while repository artifacts are written in English by default.

This applies to documentation, issues, pull requests, commit messages, comments, docstrings, and technical identifiers unless the user explicitly requests another language.
