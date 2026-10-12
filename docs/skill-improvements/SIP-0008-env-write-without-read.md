# SIP-0008: Write non-secret settings to `.env` without reading it

- Status: Accepted (requested by the owner)
- Risk: Medium — changes the agent's secrets rules (narrowly, toward writing only)
- Proposed version: 0.15.0
- Date: 2026-10-12

## Observed gap

The agent could not touch `.env` at all: the `Read(.env)` deny rule also blocks edits, and
`AGENTS.md` forbids reading it. Setting a Vertex project id, region, key-file path and model pins
required the owner to paste lines by hand, after a round of guessing which names were set.

## Evidence

Agent Lab, 2026-10-12: the owner's `.env` used another project's variable names; several
exchanges were needed to get the right non-secret variables in place.

## Why this belongs in Project Steward

Every project with a `.env` has non-secret settings next to secrets. The rule "never read `.env`"
is right; "never write to it" was collateral.

## Proposed change

- `scripts/set_env.py` (stdlib only): `KEY=VALUE` adds or replaces by name and prints names only;
  `--unset KEY` removes a variable and the comments above it; `--header` titles appended ones;
  `--check KEY` prints `set` / `-`. Refuses names with API_KEY / KEY / TOKEN / SECRET / PASSWORD /
  AUTH... (unless they end with `_FILE`, `_PATH`, `_DIR`) and values that look like secrets
  (provider prefixes, JWT, PEM, JSON, 40+ character tokens). Atomic write, permissions kept, new
  files `0600`.
- Policy: the agent may write non-secret settings with this script; reading `.env` and setting
  secret values stay forbidden.
- Template `.claude/settings.json`: allow `python3 ~/.claude/skills/project-steward/scripts/set_env.py *`.

## Files affected

- `scripts/set_env.py`, `scripts/test_set_env.py`, `.github/workflows/ci.yml`
- `references/secrets-management.md`, `references/claude-code.md`
- `templates/AGENTS.md`, `templates/.claude/settings.json`
- `VERSION`, `CHANGELOG.md`

## Compatibility impact

Existing repositories keep their rules until they adopt the new template lines.

## Security impact

No secret value enters the agent's context: the script never prints the file, and refuses to
write anything that looks like a secret. Residual risk: a secret that does not look like one (a
short password under a neutral name) could be written by the agent if the owner dictates it;
the policy still says secret values are set by the owner. The `Read(.env)` deny rules are kept.

## Risks

- Heuristics can refuse a legitimate long non-secret value; the owner then sets it by hand.
- The allow rule matches the literal path `~/.claude/skills/project-steward/scripts/set_env.py`.

## Validation plan

Unit tests (10) in CI; `scripts/check_skill.py`; used in Agent Lab to set the Vertex settings.

## Rollback plan

Revert the release commit and fast-forward the installed copy.

## Versioning rationale

MINOR: a new capability and a changed default rule, backward compatible.
