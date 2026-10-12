# AI Agent Collaboration Policy

## Goal

Multiple coding agents should behave like disciplined contributors, not independent developers editing the same repository blindly.

## Rules

- Read repository instructions before making changes.
- Inspect Git status before editing.
- Never overwrite unexplained user changes.
- Prefer isolated worktrees for parallel work.
- Avoid modifying files owned by another active task.
- Record important architectural decisions.
- Keep changes focused on the assigned task.
- Run relevant verification before claiming completion.
- Clearly report incomplete or unverified work.
- Never fabricate test results.
- Never claim a command succeeded unless it actually ran successfully.
- Never commit secrets.
- Never weaken safeguards simply to unblock CI.

## Autonomy

An owner who delegates coding should not have to approve every step, nor discover afterwards that
something was pushed or merged. Actions fall into three levels.

**Local and reversible — never ask.** Reading, running tests and linters, creating a topic branch or
worktree, editing files on it, committing on it. Asking for a code change authorizes these.

**Outward or shared — governed by the repository.** Pushing a branch, opening or updating a pull
request, merging into the default branch, pushing a tag, publishing a release, deploying a
non-production environment. The repository's "Agent autonomy" section (`templates/AGENTS.md`) says
which of these the agent may do on its own. Without that section, or for an action marked `ask`,
ask **once per task**, at the first outward action, with every remaining outward action in the same
question and a recommendation.

**Always explicit, never granted durably.** Force-pushing or rewriting shared history, deleting
remote branches that are not merged, production deploys, deleting data, recurring costs, weakening
a security control. Ask every time, whatever the autonomy section says.

A grant never relaxes the other rules: a merge still requires green checks and the Definition of
Done, and High-risk changes still require the user's decision (`references/risk-tiers.md`).

When the owner answers "always" or "from now on" to an outward action, offer to record it in the
repository's autonomy section, so the decision survives the session.

## Parallel work

When multiple agents are used:

- assign explicit task boundaries;
- assign files/components where possible;
- use separate branches/worktrees;
- integrate through PRs or controlled merges;
- resolve conflicts intentionally;
- rerun tests after integration.

## Agent handoff

A handoff should contain:

- task objective;
- current branch/worktree;
- completed work;
- remaining work;
- known issues;
- tests run;
- relevant files;
- decisions made.
