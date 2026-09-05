# Git Workflow

## Goals

The Git history should be understandable, reversible, and safe for both humans and AI agents.

## Defaults

- Keep `main` deployable.
- Do not develop substantial features directly on `main`.
- Prefer short-lived branches.
- Prefer one coherent topic per branch.
- Use worktrees for parallel or risky work.
- Rebase or update from the target branch before final integration when appropriate.
- Never rewrite shared branch history without explicit authorization.

## Branch names

This is the authoritative branch-prefix list. The prefix matches the work classification (`feature` maps to `feat`):

- `feat/<slug>`
- `fix/<slug>`
- `refactor/<slug>`
- `docs/<slug>`
- `test/<slug>`
- `chore/<slug>` — also used for `build` and `ci` work
- `security/<slug>`
- `perf/<slug>`
- `release/<slug>`
- `spike/<slug>`

## Worktrees

Use worktrees when:

- multiple agents work in parallel;
- a risky change should remain isolated;
- a long-running feature should not block smaller work;
- comparing two implementation approaches;
- reviewing another branch while preserving current work.

Recommended convention:

`../worktrees/<repo>-<branch-slug>`

Before removing a worktree:

- ensure work is committed or intentionally discarded;
- verify no untracked valuable files remain;
- remove the worktree cleanly;
- prune stale metadata.

## Commits

Use Conventional Commit style.

Keep commits:

- focused;
- buildable where practical;
- free from debug artifacts;
- free from secrets;
- descriptive enough to understand without reading the diff.

Avoid meaningless messages such as `update`, `fix stuff`, or `changes`.

## Merge strategy

Default:
- squash merge for small feature/fix branches if commit history is noisy;
- regular merge or rebase merge when individual commits carry meaningful history.

Do not create unnecessary merge commits solely from local synchronization.

## Safety

Before destructive Git commands such as hard reset, branch deletion, forced push, or aggressive clean:

- verify the target;
- verify recoverability;
- ask the user when data loss is possible and intent is not already explicit.
