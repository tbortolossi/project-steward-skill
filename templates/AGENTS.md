# Repository Agent Instructions

This repository uses the Project Steward workflow. Agents should use the Project Steward skill for
every code change, including small ones described only by their outcome.

## Before editing

- Read `PROJECT.md` (requirements) and `ROADMAP.md` (current milestone).
- Read relevant architecture documentation.
- Inspect Git status.
- Preserve unexplained user changes.
- Identify acceptance criteria.

## Working rules

- Use focused branches for non-trivial changes.
- Prefer a worktree for parallel or risky work.
- Add or update tests for behavior changes.
- Update documentation in the same change, including the matching requirement in `PROJECT.md`.
- Cite requirement IDs (`FR-n`) in pull requests when there is one.
- Do not commit secrets. Do not read `.env` or credential files, or ask for secret values: work
  from the names in `.env.example`.
- Do not disable quality/security checks to make CI pass.
- Use Conventional Commits.

## Agent autonomy

What the agent may do without asking. `yes` = do it when the task calls for it; `ask` = ask once
per task. Force-push, production deploys and data deletion always require asking and cannot be
granted here.

- push-topic-branches: ask
- open-pull-requests: ask
- merge-to-default-branch: ask
- tag-and-release: ask
- deploy-non-production: ask

## Definition of Done

A task is not complete until required tests, documentation, and verification are complete.

## Repository-specific rules

Add project-specific instructions below this line.
