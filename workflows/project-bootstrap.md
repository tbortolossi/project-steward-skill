# Workflow: Project Bootstrap

Use for a new repository or when professionalizing an existing one.

## 1. Detect project type

Inspect:

- language/runtime manifests;
- Docker files;
- Terraform files;
- API framework;
- AI/LLM dependencies;
- CI configuration;
- package structure.

Load relevant profiles only.

## 2. Assess maturity

Classify:

- Stage 0 Scratch
- Stage 1 Personal
- Stage 2 Shared
- Stage 3 Production

Do not impose Stage 3 controls on a Stage 0 experiment.

## 3. Establish baseline

Create or improve **only what the stage from step 2 justifies**. Creating every file below in a
Stage 0 experiment is the over-engineering that step 2 exists to prevent.

Stage 0 — Scratch:

- README;
- `.gitignore`;
- dependency manifest/lockfile.

Stage 1 — Personal, adding:

- `.editorconfig`;
- tests;
- lint/format;
- `.env.example`;
- LICENSE;
- SECURITY;
- CI, including a dependency vulnerability scan;
- GitHub issue/PR templates.

Stage 2 — Shared, adding:

- CONTRIBUTING;
- PROJECT;
- ROADMAP;
- CHANGELOG;
- CODEOWNERS;
- architecture documentation;
- ADR folder.

Stage 3 — Production: see `references/scaling-model.md`.

The full item list with checkboxes is in `references/bootstrap-checklist.md`.

## 4. Add technology-specific controls

Apply relevant profiles under `profiles/`.

## 5. Audit before changing aggressively

Preserve existing conventions where reasonable.

Produce a prioritized list:

- Critical
- Important
- Nice to have

Avoid refactoring the entire repository merely to match a preferred template.

## 6. Finish with a health summary

Report:

- what was added;
- what remains;
- current maturity stage;
- high-risk gaps;
- next recommended improvement.
