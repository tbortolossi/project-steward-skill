# How to Use Project Steward

## Everyday use

The user should describe the desired outcome, not the engineering ceremony.

Examples:

- `Add JSON export for detected sessions.`
- `Fix the token refresh bug.`
- `Prepare a v0.4.0 release.`
- `Professionalize this repository without over-engineering it.`

Project Steward should infer and execute the appropriate workflow.

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
