# How to Use Project Steward

## Everyday use

The user should describe the desired outcome, not the engineering ceremony.

Examples:

- `Add JSON export for detected sessions.`
- `Fix the token refresh bug.`
- `Prepare a v0.4.0 release.`
- `Professionalize this repository without over-engineering it.`

Project Steward should infer and execute the appropriate workflow.

## Starting a new project from an idea

Open an empty folder and describe the idea: `J'ai une idée : une app qui…`. Project Steward then
runs `workflows/project-inception.md`:

1. restates the idea and asks a few questions that change what gets built (users, first version,
   shape, data sensitivity, hosting and budget, throwaway or lasting);
2. writes `PROJECT.md` — the product brief: vision, numbered functional and non-functional
   requirements with acceptance criteria, non-goals, security and privacy — for you to approve;
3. proposes a stack with one alternative; you choose, and the choice becomes the first ADR, together
   with where secrets will live (`references/secrets-management.md`);
4. writes `ROADMAP.md` as milestones, starting with a walking skeleton;
5. bootstraps the repository: README, CI with secret and vulnerability scans, `CHANGELOG.md` at
   `0.1.0`, `AGENTS.md` and `CLAUDE.md`, `.claude/settings.json` keeping secret files away from the
   agent;
6. builds the walking skeleton and shows it running.

Afterwards every feature cites its requirement (`FR-n`) and updates the documents it affects in the
same change.

## Expected behavior

For normal engineering work, Project Steward should automatically:

- inspect repository context;
- select workflow;
- select technology profiles;
- establish acceptance criteria;
- isolate non-trivial work in Git;
- implement;
- test;
- document;
- check security implications;
- prepare integration/release metadata.

## When to ask the user

Ask only when necessary for:

- product behavior;
- ambiguous requirements with meaningful consequences;
- destructive changes;
- architectural tradeoffs;
- security tradeoffs;
- production-impacting operations;
- meaningful recurring cost;
- breaking compatibility decisions.

Routine engineering hygiene should not require repeated approval.

## What the agent does on its own

Branching, editing, testing and committing on a topic branch never need approval. Pushing, opening a
pull request, merging, tagging, releasing and non-production deploys follow the "Agent autonomy"
section of the repository's `AGENTS.md`:

```markdown
## Agent autonomy

- push-topic-branches: yes
- open-pull-requests: yes
- merge-to-default-branch: ask
- tag-and-release: ask
- deploy-non-production: ask
```

Set an action to `yes` to stop being asked about it. Without the section, the agent asks once per
task, grouping every outward action into one question. Force-push, production deploys and data
deletion are always asked, whatever the section says.

## Using it from Claude Code

- Describe the outcome; the skill triggers on ordinary coding requests in any language. To force
  it, start the message with `/project-steward`, e.g. `/project-steward add CSV export`.
- For a repository you always delegate, keep the line "Agents should use the Project Steward skill
  for every code change" in its `AGENTS.md` (bootstrap adds it).
- Claude Code ignores `AGENTS.md` when a `CLAUDE.md` exists. Bootstrap adds `@AGENTS.md` at the top
  of `CLAUDE.md` so both are read.
- If Claude Code still prompts for an action you granted, add an allow rule to the repository's
  `.claude/settings.json` (examples in `references/claude-code.md`).
