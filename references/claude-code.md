# Running in Claude Code

Project Steward is agent-neutral. This file maps its rules onto Claude Code, where most users run it.
Other agents can ignore it.

## Paths

Paths beginning with `references/`, `workflows/`, `profiles/`, `templates/` or `scripts/` are
relative to the skill's own directory (`${CLAUDE_SKILL_DIR}` in Claude Code). Every other path —
`AGENTS.md`, `CHANGELOG.md`, `docs/architecture.md` — names a file in the user's repository.

Read skill files from the skill directory; never copy them into the user's repository except the
files under `templates/` that bootstrap explicitly installs.

## Instruction files: AGENTS.md and CLAUDE.md

Claude Code reads `AGENTS.md` natively **only when no `CLAUDE.md` exists** in the working directory
or above. A repository with a `CLAUDE.md` silently drops the rules kept in `AGENTS.md`.

Keep the shared rules in `AGENTS.md`, readable by every agent, and make Claude Code load them:

- no `CLAUDE.md`: create one from `templates/CLAUDE.md` — its first line is `@AGENTS.md`;
- `CLAUDE.md` exists without the import: add `@AGENTS.md` as its first line, keep its content;
- `CLAUDE.md` holds the rules and there is no `AGENTS.md`: leave it, do not duplicate the rules.

An import never causes a double read. Claude-only rules go below the import line.

## Tool mapping

Use the native tool when it exists; fall back to the shell otherwise.

| Project Steward step | Claude Code |
|---|---|
| Follow a workflow checklist | Create one task per workflow step (`TaskCreate`/`TaskUpdate`, or `TodoWrite` where enabled) and mark each step as it completes |
| Ask a product, cost or risk decision | `AskUserQuestion`, recommended option first |
| Plan a High-risk change | `EnterPlanMode` before editing; the user approves the plan on exit |
| Isolate work in a worktree | `EnterWorktree` / `ExitWorktree`, or `git worktree` |
| Parallel agents | `Agent` with `isolation: "worktree"`, one task boundary per agent (`references/ai-agent-policy.md`) |
| Issues, pull requests, releases, CI status | `gh` CLI (`gh issue`, `gh pr create`, `gh pr checks`, `gh run watch`, `gh release create`) |
| Wait for CI | `gh run watch` or `gh pr checks --watch` in the background, not repeated polling |
| Code review before merge | the `code-review` skill when available, then the self-verification of solo mode |

Do not ask the user for routine engineering steps the harness lets you run. Ask through
`AskUserQuestion` only for the decisions listed in `SKILL.md`.

## Authorization and the harness

Claude Code confirms outward-facing actions — push, opening a pull request, merging, tagging,
releasing, deploying — unless the user has authorized them durably. Project Steward's autonomy
rules (`references/ai-agent-policy.md`, "Autonomy") are that durable authorization: read the
repository's "Agent autonomy" section before the first outward action of a task, and follow it.

When the section grants an action, the harness may still prompt because of its permission settings.
The user can remove that prompt with allow rules in the repository's `.claude/settings.json`, for
example:

```json
{
  "permissions": {
    "allow": ["Bash(git push origin feat/*)", "Bash(gh pr create *)", "Bash(gh pr checks *)"]
  }
}
```

Propose such rules; never write them to settings without the user's explicit request. Never add
allow rules for force-push, `git reset --hard`, branch deletion on the remote, or production deploys.

## Project setup

A repository worked on with Claude Code gets, from Stage 1 (`references/scaling-model.md`):

- `CLAUDE.md` importing `@AGENTS.md` (above);
- `.claude/settings.json`, committed, from `templates/.claude/settings.json`: deny rules that keep
  secret files and cloud credentials out of the agent's reach, and a few read-only allow rules. Add
  the allow rules matching the repository's "Agent autonomy" section. Install it when the owner
  agrees, as part of the bootstrap question;
- `.claude/settings.local.json` for personal settings, gitignored
  (`templates/.gitignore-security-snippet`).

What the deny rules cover, and what they do not:

- `deny` always wins over `allow`. That is why the template lists `.env` variants by name instead
  of `.env.*`, which would also hide `.env.example`.
- A bare filename such as `Read(.env)` matches at any depth. A `Read` deny also blocks editing and
  creating that file with the file tools. To set a non-secret variable, the agent runs
  `python3 ~/.claude/skills/project-steward/scripts/set_env.py KEY=VALUE` (allowed by the template,
  invoked with exactly that path so the allow rule matches); secret values stay the owner's to
  paste (`references/secrets-management.md`, "AI agents and secrets").
- Read rules also stop the shell commands Claude Code recognizes (`cat`, `head`, `tail`, `sed`,
  redirections), not a script or a recursive `grep` that reads the file indirectly. For OS-level
  enforcement, the owner can enable the sandbox (`sandbox.enabled` with
  `sandbox.filesystem.denyRead`, macOS/Linux/WSL2) in their user settings. Use both.
- The real protection is keeping plaintext secrets off the disk (`references/secrets-management.md`).

Further project configuration, added only when it earns its place:

- `.mcp.json`, committed, for MCP servers the project needs. Write secrets as `${VAR}` references,
  never as values.
- Project skills (`.claude/skills/`) or hooks for a procedure repeated across sessions. A hook
  that blocks something is a guard rail; document it in `AGENTS.md` so other agents follow the rule
  too.

## Commits and pull requests

Follow Conventional Commits (`references/git-workflow.md`) and end the message with the attribution
lines the harness specifies. Pass multi-line messages through a heredoc. Never use `--no-verify` to
get past a failing hook: fix the cause.

## Delegating whole tasks

The owner's normal request is an outcome ("add CSV export", "corrige le bug de connexion"). Run it
end to end with the matching workflow: branch, implement, test, document, commit, then stop at the
first outward action the autonomy section does not grant and ask once, with everything that still
needs approval in the same question (for example "push, open the pull request and merge?").
