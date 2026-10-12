# SIP-0007: CI templates that fail on first use

- Status: Accepted (requested by the owner)
- Risk: Low — template fixes, no change to rules or defaults
- Proposed version: 0.14.1
- Date: 2026-10-12

## Observed gap

Bootstrapping a new Stage 1 repository from the templates produced red CI on the first push and the
first pull request:

1. `python-ci.yml` and `dependency-audit.yml` use `astral-sh/setup-uv@v10`. setup-uv publishes full
   versions only (`v10.0.0` … `v10.3.0`), so the reference does not resolve and every job fails at
   "Set up job".
2. `gitleaks.yml` grants `contents: read` only. On a pull request, gitleaks-action lists the PR
   commits through the API and fails with `403 Resource not accessible by integration`.

## Evidence

New project bootstrap (a FastAPI + React learning tool), first push to `main` and first pull request,
2026-10-12. Both fixes verified green in that repository's CI.

## Why this belongs in Project Steward

The defects are in the shared templates: every repository bootstrapped from them hits the same
failures.

## Proposed change

- Pin `astral-sh/setup-uv@v10.2.0` in both Python workflows, with a comment explaining why.
- Add `pull-requests: read` to `gitleaks.yml`.
- `profiles/github-actions.md`: verify that each `uses:` reference exists before committing.

## Files affected

- `templates/.github/workflows/python-ci.yml`
- `templates/.github/workflows/dependency-audit.yml`
- `templates/.github/workflows/gitleaks.yml`
- `profiles/github-actions.md`
- `VERSION`, `CHANGELOG.md`

## Compatibility impact

None for existing repositories; new bootstraps get working CI.

## Security impact

`pull-requests: read` is a read-only scope, the minimum gitleaks-action needs. Pinning a full version
is stricter than a moving major tag.

## Risks

`v10.2.0` will age; Dependabot's `github-actions` updates (already in the template) keep it current.

## Validation plan

`scripts/check_skill.py`; YAML parses; the same workflows passed in the repository that exposed the
gap.

## Rollback plan

Revert the release commit and fast-forward the installed copy.

## Versioning rationale

PATCH: fixes templates without changing behavior or defaults.
