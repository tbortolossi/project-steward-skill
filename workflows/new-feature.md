# Workflow: New Feature

Use this workflow for new user-visible or operator-visible capability.

## 1. Intake

Capture:

- problem to solve;
- target user/operator;
- desired outcome;
- acceptance criteria;
- explicit non-goals;
- compatibility constraints;
- security implications.

Start from `PROJECT.md` when it exists: name the requirement (`FR-n`) the feature implements, or add
a new one with its acceptance criteria and have the owner confirm it.

If requirements are ambiguous in a way that changes product behavior, ask the user.

## 2. Scope control

Prefer the smallest coherent feature that delivers value.

Split the request if it includes:

- multiple unrelated capabilities;
- major refactoring plus feature delivery;
- migration plus unrelated cleanup;
- architectural changes that deserve an ADR.

## 3. Planning

Create a lightweight implementation plan.

Include:

- components/files likely affected;
- interface changes;
- data model changes;
- configuration changes;
- tests;
- documentation;
- migration/rollback if relevant.

## 4. Git isolation

Create a feature branch:

`feat/<short-name>`

Prefer a dedicated worktree when:

- another task is in progress;
- multiple agents are working;
- the feature is risky;
- experimentation is expected.

## 5. Implementation

Build the smallest end-to-end path first.

Avoid speculative abstractions unless there is clear reuse.

Maintain backward compatibility unless the feature intentionally introduces a breaking change.

## 6. Verification

At minimum:

- happy path;
- invalid input;
- relevant failure path;
- regression impact;
- integration behavior.

For public APIs or CLIs, verify examples manually when practical.

## 7. Documentation

Update all user-visible documentation affected by the feature, using the "What goes where" table in
`references/documentation-standard.md`: the requirement in `PROJECT.md`, the README, `.env.example`
for new settings, the architecture for new components or trust boundaries, and `ROADMAP.md` when a
milestone completes.

For UI changes, update screenshots/mockups if maintained.

## 8. Completion

Prepare PR with:

- problem;
- solution;
- testing;
- risks;
- screenshots/logs where useful;
- migration notes;
- linked issue and requirement ID.

A feature is not complete when code works but docs/tests are missing.

After integration, refresh and verify the environments that track the branch (`references/git-workflow.md`, "After integration").
