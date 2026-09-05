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

Create or improve:

- README;
- `.gitignore`;
- `.editorconfig`;
- dependency manifest/lockfile;
- tests;
- lint/format;
- `.env.example`;
- CONTRIBUTING;
- SECURITY;
- PROJECT;
- ROADMAP;
- CHANGELOG;
- architecture documentation;
- GitHub issue/PR templates;
- CI.

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
