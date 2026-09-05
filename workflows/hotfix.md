# Workflow: Hotfix

Use only for urgent production-impacting defects or security issues.

## Principles

- minimize scope;
- restore safe service first;
- avoid opportunistic refactors;
- retain evidence;
- document follow-up work.

## Process

1. Confirm severity and impact.
2. Identify currently deployed version.
3. Create a focused hotfix branch from the correct release point.
4. Add the smallest safe fix.
5. Add regression coverage where feasible.
6. Run targeted tests plus critical smoke tests.
7. Document operational impact and rollback.
8. Release with a patch version unless policy requires otherwise.
9. Merge the fix back into active development branches.
10. Create follow-up issues for deeper remediation.

For security incidents, avoid exposing sensitive exploit details in public issue text.
