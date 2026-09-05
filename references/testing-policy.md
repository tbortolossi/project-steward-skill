# Testing Policy

## Principle

Tests protect behavior, not implementation details.

Every meaningful behavior change should include a test strategy.

## Test layers

Use the smallest appropriate combination:

- unit tests for logic;
- integration tests for component interaction;
- contract tests for APIs and external interfaces;
- end-to-end tests for critical workflows;
- smoke tests for deployment or packaging;
- regression tests for bugs.

## Bug fixes

A bug fix should normally include a regression test that fails before the fix and passes after it.

## Feature work

Test:

- happy path;
- expected errors;
- boundary conditions;
- invalid inputs;
- permission/security failures when relevant;
- backward compatibility when relevant.

## Reliability

Do not:

- delete a failing test merely to make CI green;
- weaken assertions without justification;
- mock away the behavior being tested;
- silently skip flaky tests.

Flaky tests should be fixed, isolated, or explicitly tracked.

## Coverage

Coverage percentage is a signal, not the goal.

Prioritize coverage of:

- security-sensitive code;
- business-critical behavior;
- parsing/validation;
- error handling;
- public interfaces;
- previously buggy areas.
