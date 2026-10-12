# Skill Evolution Policy

## Purpose

Project Steward should improve over time when repeated work exposes missing reusable guidance.

Self-improvement must be controlled, reviewable, versioned, and reversible.

The skill must never silently rewrite its own core behavior without recording the change.

## Core distinction

When a new pattern or missing capability is discovered, classify it first.

### Project-specific learning

Keep it inside the affected repository when it is specific to:

- one product;
- one architecture;
- one customer;
- one unusual dependency;
- one temporary migration;
- one team convention.

Store it in repository-local guidance such as:

- `AGENTS.md`
- `PROJECT.md`
- project-specific documentation
- local ADRs

Do not promote project-specific exceptions into global Project Steward behavior.

### Reusable learning

Promote it into Project Steward when it is likely to help multiple repositories.

Strong signals include:

- the same manual workaround appears in multiple projects;
- a missing workflow recurs;
- a common technology lacks a profile;
- a repeated engineering failure could be prevented globally;
- the same documentation/governance gap appears across repositories;
- a better default has become broadly accepted and stable.

## Gap detection

A skill gap exists when Project Steward cannot complete routine engineering stewardship cleanly with current rules.

Examples:

- unsupported technology profile;
- missing release workflow;
- missing repository policy;
- missing CI/security pattern;
- repeated ambiguity in existing guidance;
- obsolete guidance caused by ecosystem/tooling changes.

When a gap is detected, do not immediately expand the skill unless the improvement is clearly low risk.

## Skill Improvement Proposal

For reusable gaps, create a Skill Improvement Proposal (SIP).

A SIP should contain:

- title;
- observed gap;
- evidence/examples;
- why it is reusable;
- proposed change;
- affected files;
- compatibility impact;
- risks;
- migration impact;
- validation plan;
- rollback plan;
- proposed version bump.

Use the template under:

`templates/skill-improvements/SIP-template.md`

## Change risk levels

### Low risk

Examples:

- typo/documentation clarification;
- adding a missing reference link;
- adding a new technology detection hint;
- adding a non-breaking template;
- improving examples;
- adding a new optional profile without changing existing defaults.

May be auto-applied when confidence is high.

Requirements:

- record the change;
- commit it to the skill's own git repository, referencing the gap or SIP;
- validate references;
- update changelog;
- bump PATCH version when released.

### Medium risk

Examples:

- changing default tooling for new projects;
- changing Git workflow defaults;
- changing Definition of Done;
- adding new mandatory CI checks;
- changing release conventions.

Do not silently auto-apply.

Requirements:

- create SIP;
- obtain user approval;
- test representative workflows;
- update documentation;
- bump MINOR version when appropriate.

### High risk

Examples:

- weakening security controls;
- changing destructive-action policy;
- changing merge/release authorization behavior;
- introducing automatic external writes;
- changing rules that can cause data loss;
- breaking repository compatibility.

Never auto-apply.

Requirements:

- explicit user approval;
- detailed SIP;
- validation/rollback plan;
- potentially MAJOR version bump.

## Auto-upgrade rules

Project Steward may auto-apply only low-risk improvements when all conditions are true:

- the change is clearly reusable;
- it does not alter existing mandatory behavior;
- it does not weaken security or validation;
- it does not introduce destructive operations;
- it does not add external cost or credentials;
- it is backwards compatible;
- the change can be validated locally.

Otherwise, create a proposal and request approval.

## Owner-requested changes

When the owner explicitly asks for a change to the skill — "add this to the skill", "le skill doit
faire X", "fix the skill so that…" — the request is the approval, whatever the risk level. Do not
ask again whether to make the change. In one pass:

1. write the SIP with status "Accepted (requested by the owner)", quoting the request as evidence;
2. implement it in the skill's source repository on a topic branch and run `scripts/check_skill.py`;
3. merge, bump `VERSION`, update `CHANGELOG.md`, create the annotated tag;
4. push as the skill repository's "Agent autonomy" section allows;
5. update the installed copy (see below) and confirm its `VERSION`;
6. report what changed and the new version.

Limits:

- The request covers what the owner asked for. Adjacent improvements noticed on the way follow the
  normal risk levels.
- A change that weakens a security, testing or approval rule, or adds a destructive action, is
  stated in one sentence with its consequence and applied only after a yes. Never silent.
- A complaint or observation ("it keeps asking me") is not a request: propose the change and apply
  it when the owner agrees.
- The agent never grants itself autonomy: entries in an "Agent autonomy" section are written by the
  owner, or on the owner's explicit instruction for that entry.
- The agent's harness may still refuse to edit instructions the agent itself runs under. Do not work
  around it: hand the owner the exact change, or ask them to approve it interactively.

## Source and installed copies

The skill usually exists twice: the source repository where it is developed, and the installed copy
the agent loads (`~/.claude/skills/project-steward/` in Claude Code), a clone of the same remote.

- Change the source repository. If its location is unknown, ask the owner once and remember it.
- Never edit the installed copy directly: it diverges from the source and the next update conflicts.
- After a release, fast-forward the installed copy with `git pull --ff-only`, from the remote or, if
  the push has not happened, from the local source repository.

## Repetition heuristic

Repeated local adaptations are a signal for promotion.

Recommended heuristic:

- first occurrence: solve locally;
- second occurrence: note potential reusable pattern;
- third independent occurrence: strongly consider a SIP.

This is guidance, not a rigid threshold.

## Validation

Before releasing a skill change:

- verify links/references resolve;
- verify templates are syntactically valid;
- verify workflows remain coherent;
- check for contradictory instructions;
- check security impact;
- test at least one representative scenario for behavior-changing updates.

## Rollback

The skill directory itself must be a git repository. Every skill change — including auto-applied low-risk improvements — is committed, and every release is tagged, so any change is reversible through version control.

Do not delete prior releases/tags merely because guidance changed.

## Transparency

When Project Steward improves itself, report:

- what gap was found;
- whether the change was local or global;
- what changed;
- why it is safe;
- new skill version.
