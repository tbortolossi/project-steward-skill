# Documentation Standard

## Documentation is code

Documentation should change in the same pull request as the behavior it describes.

## Baseline documents

Recommended baseline:

- `README.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `LICENSE`
- `CHANGELOG.md`
- `PROJECT.md`
- `ROADMAP.md`
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
6. How do I configure it?
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

## Architecture

Architecture documentation should describe:

- components;
- boundaries;
- data flow;
- trust boundaries;
- external dependencies;
- persistence;
- authentication/authorization;
- deployment shape;
- major failure modes.

## ADRs

Use ADRs for decisions that are expensive to reverse or likely to be questioned later.

Examples:

- database choice;
- authentication model;
- message broker;
- deployment architecture;
- breaking API strategy;
- major dependency/framework choice.
