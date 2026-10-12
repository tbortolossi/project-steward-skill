# Documentation Standard

## Documentation is code

Documentation changes in the same pull request as the behavior it describes. A pull request that
changes behavior without touching the documents that describe it is incomplete
(`references/definition-of-done.md`).

## What goes where

Each fact lives in one place; other documents link to it rather than copy it. Which files exist at
which stage is set by `references/scaling-model.md`.

| Question | Document |
|---|---|
| What is this, how do I install, run, configure and test it? | `README.md` |
| What are we building, for whom, which requirements (`FR`/`NFR`)? | `PROJECT.md` |
| In what order, what is the current milestone? | `ROADMAP.md` |
| What changed in each release? | `CHANGELOG.md` |
| How is the system built and where are its trust boundaries? | `docs/architecture.md` |
| Why was this expensive-to-reverse choice made? | `docs/adr/NNNN-*.md` |
| Which settings and secrets exist? | `.env.example`, with the README "Configuration" section |
| What goes wrong and how do I fix it? | `docs/troubleshooting.md` |
| How do I contribute, how do I report a vulnerability? | `CONTRIBUTING.md`, `SECURITY.md` |
| How must agents work here? | `AGENTS.md`, imported by `CLAUDE.md` |
| Why does this code do something surprising? | a comment next to the code |

Anything that is not in this table is probably either a comment or not worth writing.

## Writing rules

- Write for the reader of that document: the README for a newcomer, `PROJECT.md` for the owner,
  architecture for the next maintainer. One document, one audience.
- Lead with the answer. Background comes after, if at all.
- Prefer short documents that are true over long ones that drift. Delete what is no longer true
  rather than marking it outdated.
- Every command in the documentation is copy-pasteable and has been run. Setup instructions are
  verified from a clean checkout when they change.
- Use relative links between documents so they survive forks and renames of the host.
- Date or version anything likely to drift (screenshots, benchmarks, compatibility tables).
- Code comments explain why, not what. Public functions and modules get docstrings when their
  contract is not obvious from the signature.
- Requirement IDs (`FR-n`, `NFR-n`) are stable: never renumber, mark removed ones as dropped.

## Baseline documents

Recommended baseline (stage by stage in `references/scaling-model.md`):

- `README.md`
- `PROJECT.md` and `ROADMAP.md`
- `CHANGELOG.md`
- `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`
- `docs/architecture.md`
- `docs/troubleshooting.md`
- `docs/adr/`

## README

The README should answer quickly:

1. What is this?
2. Why does it exist?
3. What does it do?
4. How do I install it?
5. How do I run it?
6. How do I configure it, and where do secrets come from?
7. How do I test it?
8. What are the security considerations?
9. Where is deeper documentation?

## Screenshots and mockups

For UI or visual workflows:

- keep screenshots current;
- avoid exposing secrets, internal tokens, private URLs, or personal data;
- use stable filenames;
- document when screenshots were captured if UI drift is likely;
- prefer diagrams or mockups when real screenshots expose sensitive data.

Recommended path:

`docs/assets/`

Prefer diagrams as text (Mermaid in Markdown) so they are versioned and reviewed like code.

## Architecture

Architecture documentation should describe:

- components;
- boundaries;
- data flow;
- trust boundaries;
- external dependencies;
- persistence;
- authentication/authorization;
- secrets handling (`references/secrets-management.md`);
- deployment shape;
- major failure modes.

Before `docs/architecture.md` exists, a few lines in the README or `PROJECT.md` are enough.

## ADRs

Use ADRs for decisions that are expensive to reverse or likely to be questioned later. Write the ADR
when the decision is made, not afterwards.

Examples:

- language and framework (the first ADR of a project started with `workflows/project-inception.md`);
- database choice;
- authentication model;
- secrets mechanism;
- message broker;
- deployment architecture;
- breaking API strategy;
- major dependency/framework choice.

ADRs are immutable once accepted: a changed decision gets a new ADR that supersedes the old one.

## Keeping documentation current

At the end of each task, check the table above against what changed: new setting → `.env.example`
and README; new behavior → `PROJECT.md` requirement and README; new component or trust boundary →
architecture; new failure seen in practice → troubleshooting. `references/project-health.md`
checks drift periodically.
