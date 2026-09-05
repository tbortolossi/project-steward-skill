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
