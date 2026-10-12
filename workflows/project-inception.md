# Workflow: Project Inception

Use when the owner starts from an idea and no repository exists yet, or the repository is empty:
"j'ai une idée", "I want to build…", "new project", "write the PRD / spec / plan".

The output is a project that knows what it is building, why, in what order, and on what stack —
written down before code, kept short enough to stay current. Product decisions belong to the owner:
this workflow asks, proposes and writes; it never chooses the product for them.

## 1. Understand the idea

Restate the idea in the owner's language in a few sentences: the problem, who has it, what changes
for them when the project exists. Ask the owner to correct it.

Then ask only the questions whose answers change what gets built, at most four per round, with a
recommended option first (`AskUserQuestion` in Claude Code):

- who uses it, and is it only the owner;
- the first version: the smallest thing that would already be useful;
- the shape: web app, API, CLI, mobile, library, automation, AI/LLM feature;
- the data it handles: personal, customer, credentials, payment, health, or none of these;
- where it runs and the budget: local only, free tier, paid hosting;
- the intent: throwaway experiment (Stage 0) or a project meant to last (Stage 1 or above).

Use sensible defaults for everything else, and say which defaults you took.

A throwaway experiment stops here: go to `workflows/project-bootstrap.md` at Stage 0 and skip the
documents below.

## 2. Write the product brief

Create `PROJECT.md` from `templates/PROJECT.md`. It is the project's PRD, kept to what the owner can
read in a few minutes:

- vision, target users, problem;
- functional requirements, numbered `FR-1`, `FR-2`…, each with acceptance criteria phrased so a
  test can check them, and a priority (`must` for the first version, `should`, `could`);
- non-functional requirements, numbered `NFR-1`…: security, privacy, performance, availability,
  cost, accessibility, compatibility — only those that constrain this project;
- non-goals, which prevent scope creep later;
- security and privacy: data handled and its sensitivity, who authenticates and how, what is exposed
  to the internet, which secrets the project will need;
- constraints, risks, and open decisions.

Show the brief and get the owner's approval before moving on. Requirements are product decisions.

## 3. Choose the stack

Propose one recommended stack and one alternative, with the trade-offs in plain language: what each
costs, how well it fits the shape and the NFRs, how much operation it needs. Prefer mainstream,
well-maintained choices covered by a profile in `profiles/`, and the languages the owner already
uses.

The owner decides. Record the decision as `docs/adr/0001-<stack>.md` from
`templates/docs/adr/0000-template.md`, with the rejected alternative and its revisit conditions.

Choose the secrets rung in the same step (`references/secrets-management.md`), aiming for a vault
(rung 2 or above) so `.env` holds configuration only, and note it in the
ADR or the brief.

## 4. Plan the delivery

Write `ROADMAP.md` from `templates/ROADMAP.md` as milestones, each with its requirement IDs and an
exit criterion the owner can observe:

- **M0 — Walking skeleton**: repository, CI green, the thinnest end-to-end path running (for a web
  app, one page served from the real stack; for a CLI, one command). No feature yet.
- **M1 — First useful version**: the `must` requirements.
- **M2 and later**: `should` and `could`, in the order the owner prefers.

Keep milestones small enough to finish in days, not months. The detailed plan of each feature is
made when the feature starts (`workflows/new-feature.md`, step 3), not up front.

## 5. Bootstrap the repository

Run `workflows/project-bootstrap.md` at the stage chosen in step 1 — Stage 1 by default for a
project meant to last. Bundle the owner decisions it needs into one question:

- the "Agent autonomy" entries for `AGENTS.md`;
- installing the Claude Code project settings (`templates/.claude/settings.json`);
- whether to create a remote repository, and its visibility (private by default). Creating it and
  pushing are outward actions: ask, whatever autonomy says, because no autonomy section exists yet.

Commit the brief, ADR and roadmap with the bootstrap files.

## 6. Build the walking skeleton

Deliver M0 through `workflows/new-feature.md`: branch, smallest end-to-end path, one real test,
README run instructions that work from a clean checkout, CI green. This proves the stack, the
pipeline and the secrets mechanism before any feature depends on them.

## 7. Report

In plain language (`references/reporting-to-user.md`):

- what the project is, in two sentences, as recorded in `PROJECT.md`;
- decisions taken, and which were defaults the owner can still change;
- what exists now and how to run it;
- the next milestone and its first feature.

## Keeping the documents alive

- A feature that adds or changes behavior updates the matching `FR` in `PROJECT.md` in the same
  pull request; a new need gets a new ID.
- Pull requests and commits cite the requirement IDs they implement when there is one.
- When a milestone completes, move it in `ROADMAP.md` and record the release in `CHANGELOG.md`.
- When `PROJECT.md` passes about 30 requirements, move them to `docs/requirements.md` and leave a
  summary and a link.
