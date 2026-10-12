# SIP-0004: Claude Code integration and explicit agent autonomy

- Status: Proposed (requested by the project owner; awaiting approval to merge)
- Risk: High — changes merge and release authorization behavior
- Proposed version: 0.12.0
- Date: 2026-10-12

## Observed gap

The owner uses Project Steward from Claude Code to delegate coding outright: describe an outcome,
get a branch, tests, docs, commits, a pull request and a release. Four things prevented that from
working reliably.

1. **Triggering.** The description listed process activities ("git workflow", "changelogs"). A plain
   request such as "corrige le bug de connexion" names none of them, so the skill was often not
   loaded for the work it exists to govern.
2. **Authorization conflict.** `SKILL.md` said not to ask approval for routine steps and to merge
   "when repository policy allows it", but no repository could express that policy. Claude Code
   confirms pushes, pull requests and merges unless durably authorized. The result was either a
   question at every step or an agent unsure whether it was allowed to finish.
3. **Ignored instructions.** Claude Code reads `AGENTS.md` only when no `CLAUDE.md` exists. Bootstrap
   installs `AGENTS.md`; in any repository that also has a `CLAUDE.md`, every rule in it was silently
   dropped.
4. **Path ambiguity and no tool mapping.** Nothing said that `references/…` paths are relative to the
   skill directory while `docs/…` paths are in the user's repository, and the checklists did not map
   onto Claude Code's task list, `AskUserQuestion`, plan mode, worktrees or `gh`.

## Evidence

Owner request of 2026-10-12: make the skill "more Claude compatible" so that coding can be delegated
to it. Gap 3 was confirmed against the Claude Code memory documentation (AGENTS.md is read only in
the absence of CLAUDE.md; an `@AGENTS.md` import does not cause a double read).

## Why this belongs in Project Steward

Every repository driven from Claude Code hits gaps 1–3; none is project-specific.

## Proposed change

1. `SKILL.md` frontmatter: description centered on "any code change in a git repository, even when
   only the outcome is described", plus `when_to_use` with natural trigger phrases in several
   languages and an `argument-hint` for `/project-steward <task>`. No `allowed-tools`: the skill
   grants itself no permissions.
2. `references/ai-agent-policy.md`, "Autonomy": three levels — local actions never asked; outward
   actions governed by the repository's "Agent autonomy" section, default `ask`, asked once per task
   and bundled; force-push, production deploys, data deletion and recurring costs always asked.
3. `templates/AGENTS.md`: an "Agent autonomy" section, every entry `ask` by default, and a line
   telling agents to use the skill for every code change.
4. `templates/CLAUDE.md`: `@AGENTS.md` import. Bootstrap, the bootstrap checklist and the scaling
   model (Stage 1) install both files.
5. `references/claude-code.md`: path convention, the AGENTS.md/CLAUDE.md rule, tool mapping,
   how the autonomy section relates to the harness and to `.claude/settings.json` allow rules.
6. `SKILL.md`: path rule, autonomy summary, router entries. Data-protection and dependency sections
   condensed into pointers to stay within the router size limit.
7. `scripts/check_skill.py`: description + `when_to_use` within Claude Code's 1,536-character
   listing limit; `templates/CLAUDE.md` starts with `@AGENTS.md`.

## Files affected

- `SKILL.md`, `OPERATING-GUIDE.md`, `README.md`
- `references/ai-agent-policy.md`, `references/claude-code.md` (new), `references/git-workflow.md`,
  `references/scaling-model.md`, `references/bootstrap-checklist.md`
- `workflows/project-bootstrap.md`
- `templates/AGENTS.md`, `templates/CLAUDE.md` (new)
- `scripts/check_skill.py`
- `VERSION`, `CHANGELOG.md`

## Compatibility impact

Existing repositories without an autonomy section get the default `ask`: one bundled question per
task before the first outward action. This replaces an undefined behavior, not a granted one.
Repositories with a `CLAUDE.md` and an `AGENTS.md` start receiving the `AGENTS.md` rules once the
import is added.

## Security impact

Tightens rather than relaxes. Outward actions now default to asking; the never-grantable list
(force-push, production deploys, data deletion, recurring costs, weakening security controls)
cannot be overridden by a repository. The skill does not write permission settings; it only
proposes allow rules, and never for destructive commands.

## Risks

- Owners who set everything to `yes` get merges without a question. Mitigated: merges still require
  green checks and the Definition of Done, and High-risk changes still require a user decision.
- Broader triggering may load the skill for trivial edits. Mitigated by the existing rule that
  trivial changes get a one-sentence report and no ceremony.
- Claude Code tool names change. They are confined to `references/claude-code.md`.

## Validation plan

- `python scripts/check_skill.py` passes, including the two new checks.
- Read-through for contradictions between `SKILL.md`, `references/ai-agent-policy.md`,
  `references/git-workflow.md`, `references/scaling-model.md` and the bootstrap files.

## Rollback plan

Revert the merge commit and tag a PATCH release. Repositories bootstrapped in between keep a
harmless `CLAUDE.md` import and an autonomy section that older versions ignore.

## Versioning rationale

MINOR: new reference, new template, new default behavior for outward actions, no removed capability.
The project is pre-1.0, so a behavior change of this kind does not require a MAJOR bump.
