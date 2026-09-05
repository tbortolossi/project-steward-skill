# Risk Tiers

Classify every managed change into one of three tiers. The tier drives how much process and approval the change requires.

## Low risk

Examples:

- Documentation-only changes
- Small test improvements
- Internal refactors with strong coverage

Action:

- Standard workflow
- Lightweight review

## Medium risk

Examples:

- New feature
- CLI/API behavior change
- Dependency updates
- Infrastructure/config changes
- Authentication-adjacent work

Action:

- Explicit acceptance criteria
- Tests required
- Documentation required
- PR review recommended

## High risk

Examples:

- Authentication or authorization
- Cryptography
- Secrets handling
- Database migrations
- Destructive operations
- Production deployment logic
- Security controls
- Major architectural rewrites
- Breaking public API changes

Action:

- Explicit user decision where tradeoffs exist
- ADR required for architectural impact
- Stronger test coverage
- Rollback plan
- Security review
- No silent merge
