# Definition of Done

Use this default Definition of Done unless the repository overrides it.

- [ ] Requested behavior implemented
- [ ] Acceptance criteria satisfied
- [ ] Appropriate tests added or updated
- [ ] Tests pass
- [ ] Formatting/linting passes
- [ ] Type checking passes if configured
- [ ] Security checks pass if configured
- [ ] No new high/critical dependency advisory introduced by this change
- [ ] Documentation updated
- [ ] Config/example files updated if needed
- [ ] No secrets or debug artifacts committed
- [ ] Backward compatibility considered
- [ ] Changelog/release note impact assessed
- [ ] PR description complete
- [ ] Known risks documented
- [ ] Rollback path documented when relevant
- [ ] Environments tracking the integrated branch rebuilt or redeployed, and verified

## Completion criteria

A task is complete only when:

- Acceptance criteria are met.
- Tests pass.
- Required documentation is updated.
- CI is green or equivalent local checks pass.
- No known critical regression remains.
- Security impact has been considered.
- The change is committed cleanly.
- PR/release metadata is updated when applicable.
- Temporary worktrees/branches are cleaned after integration.
- Environments that track the integrated branch run the new version, verified (`references/git-workflow.md`, "After integration").

Documentation is part of the definition of done. A feature is not complete when code works but docs/tests are missing.
