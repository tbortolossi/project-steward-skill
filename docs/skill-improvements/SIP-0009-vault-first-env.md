# SIP-0009: Vault first, so `.env` is configuration the agent can read

- Status: Accepted (requested by the owner)
- Risk: Medium — changes when the agent may read `.env`
- Proposed version: 0.16.0
- Date: 2026-10-12

## Observed gap

The rules treated every `.env` as secret: never read it, deny rules in every Stage 1 repository.
The owner's intent was different: secrets belong in a vault or password manager, injected at run
time, and `.env` is then configuration. A `.env` holding only a project id, a region, a key-file
path and model names was locked anyway, which cost several round trips (Agent Lab, 2026-10-12).

## Proposed change

- Principle: aim for rung 2 or above; `.env` holds configuration only.
- Where `.env` holds no secret: the agent reads and edits it, the `.env` deny rules are left out.
- Where it still does (rung 1): unchanged rules, `set_env.py` for non-secret values, and a nudge
  toward rung 2.
- Key files, credential stores and vault exports stay unreadable in every case.

## Files affected

- `references/secrets-management.md`, `references/claude-code.md`
- `templates/AGENTS.md`, `workflows/project-inception.md`
- `VERSION`, `CHANGELOG.md`

## Security impact

Reading `.env` is allowed only where it holds no secret; the template keeps the deny rules by
default (a fresh repository is rung 1 until a vault is set up). Key files stay denied.

## Rollback plan

Revert the release commit and fast-forward the installed copy.

## Versioning rationale

MINOR: changes a default rule, backward compatible.
