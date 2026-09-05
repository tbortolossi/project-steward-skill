# Reporting to the User

## Purpose

The project owner may not read code. The end-of-task report is their primary interface to the work — treat it as a deliverable, with the same care as tests or documentation.

Never assume the user will read the diff, the test output, or the commit history.

## End-of-task report

After every non-trivial task, report in plain language, in the user's language:

- **What changed**, in functional terms ("the app now rejects expired tokens"), not implementation terms ("refactored the middleware chain").
- **How it was verified** — which tests, which manual checks, what was demonstrated.
- **What could break** — known risks, untested paths, assumptions made.
- **Implications** — new or changed costs, security impact, maintenance burden, new dependencies.
- **Open questions** — decisions deferred to the user, with a recommendation.

Rules:

- Explain jargon on first use or avoid it.
- Keep it short enough to be read; a report that is skipped protects no one.
- For trivial changes, a one-sentence summary is enough — do not pad.

## Demonstration: show, don't tell

For any user-visible change (UI, CLI, API, generated output), demonstrate the real behavior:

- run the application or command and show the actual output;
- provide a screenshot for UI changes when possible;
- show a real request/response for API changes.

Passing tests protect against regressions; demonstration lets the owner confirm the change is what they wanted. They are not substitutes for each other.

When demonstration is impractical (long-running jobs, external environments), say so explicitly and describe what was verified instead.

## Decisions and tradeoffs

When presenting a decision to the user:

- state the options in terms of consequences for them (cost, risk, time, lock-in), not in terms of technology;
- give a recommendation and the reason for it;
- never bury a meaningful decision inside a routine report.
