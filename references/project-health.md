# Project Health Review

Run periodically or before significant milestones.

## Scorecard

Assess each area as Green / Amber / Red.

### Repository hygiene

- clean default branch;
- stale branches/worktrees;
- clear ownership;
- useful README;
- current project status.

### Build reproducibility

- lockfile current;
- clean checkout builds;
- CI mirrors documented local commands.

### Test health

- tests pass;
- no unexplained skips;
- no persistent flaky tests;
- critical paths covered.

### Security

- secret scanning enabled;
- sensitive-data review policy present;
- Dependabot alerts enabled and triaged, not merely accumulating;
- dependency audit job present and running on schedule, not only on pull requests;
- no known leaked credentials;
- no unnecessary privileged CI permissions;
- security-sensitive changes documented.

### Dependencies

- unsupported dependencies;
- known vulnerabilities — run the ecosystem's audit command rather than assuming CI covered it
  (`references/vulnerability-management.md`);
- suppressed advisories: still justified, or expired and quietly permanent?
- stale major versions;
- abandoned packages.

### Documentation

- setup works;
- API/CLI docs current;
- screenshots current;
- architecture reflects reality;
- troubleshooting covers common failures.

### Agent instructions

- `AGENTS.md` present, with an "Agent autonomy" section;
- `CLAUDE.md` imports `@AGENTS.md` when both exist (`references/claude-code.md`).

A gap here does not block a task: mention it in one line of the end-of-task report and offer to fix
it.

### Delivery

- changelog current;
- releases reproducible;
- versioning coherent;
- rollback documented where relevant.

### Technical debt

Prioritize debt by:

1. security/risk;
2. reliability;
3. developer friction;
4. maintainability;
5. cosmetic cleanup.
