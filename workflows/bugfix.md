# Workflow: Bug Fix

## 1. Confirm the defect

Capture:

- observed behavior;
- expected behavior;
- reproduction steps;
- environment/version;
- logs or evidence;
- regression status if known.

Do not fix based only on a vague symptom when the failing behavior can be reproduced.

## 2. Minimize the reproduction

Identify the smallest failing path.

Separate root cause from secondary symptoms.

## 3. Add regression coverage

Where practical:

1. add a test that reproduces the bug;
2. confirm it fails before the fix;
3. implement the fix;
4. confirm the test passes afterward.

If automated regression coverage is not practical, document the manual verification.

## 4. Scope

Fix the root cause without unrelated refactors.

If a larger design flaw is discovered, record follow-up technical debt separately unless it is necessary for a safe fix.

## 5. Risk

Consider:

- data corruption;
- compatibility;
- security;
- concurrency;
- migration;
- deployment impact.

## 6. Completion

Use branch:

`fix/<short-name>`

Commit example:

`fix: handle expired session token correctly`

Update changelog when user-visible behavior changes.
