# Workflow: Project Bootstrap

Use for a new repository or when professionalizing an existing one.

When the owner starts from an idea and the repository is empty, run `workflows/project-inception.md`
first: it writes the brief, the stack ADR and the roadmap, then comes back here. Step 1 then reads
the stack from that ADR instead of detecting it.

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
- `.env.example`, and the secrets mechanism chosen with the owner (`references/secrets-management.md`);
- LICENSE;
- SECURITY;
- `PROJECT.md` and `ROADMAP.md` from `templates/` — short; filled by inception, or from the README and the owner's answers;
- `CHANGELOG.md` with `[Unreleased]`, and a version source at `0.1.0`;
- CI, including a secret scan and a dependency vulnerability scan;
- GitHub issue/PR templates;
- `AGENTS.md` from `templates/AGENTS.md`, with the owner's choices in "Agent autonomy", `CLAUDE.md` from `templates/CLAUDE.md`, and `.claude/settings.json` from `templates/.claude/settings.json` once the owner agrees (`references/claude-code.md`, "Project setup").

Stage 2 — Shared, adding:

- CONTRIBUTING;
- CODEOWNERS;
- shared secrets through encrypted files or a secret manager;
- architecture documentation;
- ADR folder.

Stage 3 — Production: see `references/scaling-model.md`.

If the repository publishes an artifact others install, add the release
items — version source, `CHANGELOG.md` with `[Unreleased]`, tag convention
— whatever its stage. See "Publishing changes the requirement" in
`references/scaling-model.md`.

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

## 6. Release, if the repository publishes

A bootstrap is not finished at the last file created. If the repository
publishes something others install, hand off to `workflows/release.md` and
cut the first release: version in the manifest, changelog entry, annotated
tag, release notes.

A published artifact whose version exists in no tag cannot be reported
against, bisected, or rolled back to.

## 7. Finish with a health summary

Report:

- what was added;
- what remains;
- current maturity stage, and the released version if the repository publishes;
- high-risk gaps;
- next recommended improvement.
