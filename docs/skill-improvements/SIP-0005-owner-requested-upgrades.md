# SIP-0005: Owner-requested skill changes, installed copy, and autonomy onboarding

- Status: Accepted (requested by the owner)
- Risk: Medium — changes the approval path for skill evolution
- Proposed version: 0.13.0
- Date: 2026-10-12

## Observed gap

1. When the owner explicitly asked for a skill change, the policy still routed it through the risk
   levels and asked for an approval the owner had just given.
2. Nothing distinguished the source repository from the installed copy the agent loads. An agent
   could edit the installed copy, which then diverges, or release without updating it, leaving the
   owner on the previous version.
3. Repositories created before 0.12.0 have no "Agent autonomy" section, and nothing made the agent
   notice it or propose a sensible preset.

## Evidence

Owner requests of 2026-10-12: "on peut faire un auto upgrade quand ça vient de moi ?" and "rien à
modifier dans le skill pour tes recommandations ?". During the 0.12.0 release the installed copy at
`~/.claude/skills/project-steward/` had to be updated by hand from the local source repository.

While implementing this SIP, Claude Code's auto-mode classifier refused edits that relax the
approval rules of a skill the agent runs under, including granting the agent autonomy in this
repository's `AGENTS.md`. Hence the limits below: the agent never grants itself autonomy and does
not work around a harness refusal.

## Proposed change

- `references/skill-evolution-policy.md`: "Owner-requested changes" — an explicit request is the
  approval; apply, release and install in one pass; limits: scope of the request only, security
  weakening needs a yes, observations are not requests, no self-granted autonomy, no working around
  the harness. "Source and installed copies" — change the source, never the installed copy, then
  fast-forward the installed copy.
- `workflows/improve-skill.md`: approval and version steps point to these sections.
- `references/ai-agent-policy.md`: when the autonomy section is missing, offer to create it with a
  recommended single-owner preset (push and pull requests `yes`, the rest `ask`), written only from
  the owner's answer.
- `references/project-health.md`: "Agent instructions" checks; a gap is reported in one line, not
  blocking.

## Compatibility impact

Additive. No default changes for repositories; the preset is only proposed.

## Security impact

No control is weakened. Weakening changes still need an explicit yes, and the agent cannot grant
itself autonomy.

## Validation plan

`python scripts/check_skill.py`; read-through against `SKILL.md` "Skill evolution", which already
requires explicit approval — an explicit owner request satisfies it.

## Rollback plan

Revert the merge commit and tag a PATCH release.

## Versioning rationale

MINOR: new policy sections, no removed behavior.
