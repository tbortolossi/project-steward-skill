# SIP-0006: Project inception, secrets management, documentation practice, Claude Code project setup

- Status: Accepted (requested by the owner)
- Risk: Medium — changes Stage 1 defaults for new projects
- Proposed version: 0.14.0
- Date: 2026-10-12

## Observed gap

1. **No path from an idea to a project.** `workflows/project-bootstrap.md` starts by detecting the
   stack from manifests, which an empty repository does not have. Nothing turned "I have an idea"
   into a brief, requirements, a stack decision and a plan. `templates/PROJECT.md` existed but held
   no requirements and appeared only at Stage 2.
2. **Secrets stopped at `.env`.** The policy said what never to commit and to ship `.env.example`,
   but not where secrets should live instead: password managers, sops, Vault or cloud secret
   managers, CI secrets and OIDC, rotation, or how this grows with the stage.
3. **Documentation guidance listed files, not practice.** No rule on which fact lives where, how to
   write for an audience, or how requirements stay in step with the code.
4. **Claude Code setup stopped at `CLAUDE.md`.** No project `.claude/settings.json` keeping secret
   files out of the agent's reach.
5. **Version history started late.** `CHANGELOG.md` arrived at Stage 2 unless the project
   published, so a personal project had no record of its first releases.

## Evidence

Owner request of 2026-10-12: "Est-ce que ce skill aide aussi à faire la doc du projet, à gérer les
points de sécurité (genre pas env mais vault), aider à set un bon environnement pour le projet avec
Claude, PRD, FR, PLAN etc ? … on va partir de zéro en disant j'ai une idée", followed by "Oui go,
mets les bonnes pratiques pour faire la doc et faire en sorte que ce project-steward m'aide à faire
des bons projets, bien documentés, qui partent sur des bonnes bases, secure, et bien gérés dans le
code / version".

## Why this belongs in Project Steward

Every new project goes through inception, secrets and documentation; none of it is specific to one
product.

## Proposed change

- `workflows/project-inception.md` (new): idea → focused questions → `PROJECT.md` brief with `FR`/
  `NFR` IDs and acceptance criteria → stack proposal and ADR-0001 → `ROADMAP.md` milestones starting
  with a walking skeleton → bootstrap → walking skeleton → report. A throwaway experiment exits after
  step 1 to a Stage 0 bootstrap.
- `references/secrets-management.md` (new): principles; four rungs (`.env`, password-manager
  injection, sops/age, secret manager) mapped to stages; code, CI/OIDC, agent and rotation rules.
- `references/documentation-standard.md`: "What goes where" table, writing rules, ADR immutability,
  text diagrams, keeping documentation current.
- `templates/.claude/settings.json` (new) and `references/claude-code.md` "Project setup": deny
  rules for secret files and cloud credentials, read-only allow rules, with what deny rules do and do
  not cover (verified against the Claude Code permissions and sandboxing documentation).
- `templates/PROJECT.md` becomes a product brief; `templates/ROADMAP.md` uses milestones;
  `templates/AGENTS.md` cites requirements and forbids reading secret files.
- Stage 1 (`references/scaling-model.md`, `workflows/project-bootstrap.md`,
  `references/bootstrap-checklist.md`) gains: `PROJECT.md`, `ROADMAP.md`, `CHANGELOG.md` and a version
  source, ADRs for expensive decisions, a chosen secrets mechanism, CI secret scan,
  `.claude/settings.json`. Stage 2 gains shared secrets through rung 3–4; Stage 3 rung 4 with
  rotation and OIDC.
- `workflows/new-feature.md`, `references/project-health.md`, `references/security-policy.md`:
  link features to requirement IDs, check documentation and secrets drift.
- `SKILL.md`: router entries and trigger phrases for ideas, PRD, documentation and secrets.
- `scripts/check_skill.py`: JSON templates must parse.

## Compatibility impact

Existing repositories are not changed. At their next health review they may be offered the new
Stage 1 items; `references/project-health.md` reports gaps without blocking work.

## Security impact

Strengthens: secrets move off plaintext disk as projects grow, agents are denied secret files, CI
secret scanning moves to Stage 1. No control is weakened.

## Risks

- Ceremony creep at Stage 1. Mitigated: documents are kept short by rule, throwaway experiments stay
  at Stage 0, detailed feature plans are made just in time.
- Deny rules give a false sense of safety. Mitigated: the guidance states their limits and points to
  keeping plaintext off disk and the sandbox.

## Validation plan

`python scripts/check_skill.py`; read-through of Stage 0–3 across `references/scaling-model.md`,
`workflows/project-bootstrap.md` and `references/bootstrap-checklist.md` for contradictions;
walk-through of the inception workflow against the owner's scenario (empty folder, "j'ai une idée").

## Rollback plan

Revert the merge commit and tag a PATCH release.

## Versioning rationale

MINOR: new workflow, reference and template; changed Stage 1 defaults; no removed behavior.
