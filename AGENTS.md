# Agent Instructions — project-steward-skill

This repository *is* the Project Steward skill. It contains no application code: only Markdown
guidance, YAML templates, and one check script.

## What this means for changes here

- Editing a file here changes how the skill behaves in **every** repository that uses it. There is
  no such thing as a local-only fix.
- Follow `workflows/improve-skill.md` and `references/skill-evolution-policy.md`. Medium- and
  high-risk changes need a numbered SIP in `docs/skill-improvements/` before implementation.
- Every change bumps `VERSION` and `CHANGELOG.md` (SemVer) and is released with an annotated tag.
  CI enforces that `VERSION` has a matching changelog section.

## Structure

- `SKILL.md` is a **router**, not a manual. Keep it compact; detailed policy belongs in
  `references/`. If SKILL.md is growing past ~170 lines, extract rather than append.
- `references/` — reusable policy, one topic per file.
- `workflows/` — execution checklists per change type.
- `profiles/` — technology baselines, selected via `profiles/detection.md`.
- `templates/` — files copied into *target* repositories. Paths like `docs/architecture.md` inside
  guidance text refer to the target repo, not to this one.
- `docs/skill-improvements/` — accepted SIPs.

## Before committing

```bash
python scripts/check_skill.py
```

This verifies templates parse as YAML, internal references resolve, SKILL.md keeps its discovery
frontmatter, VERSION agrees with CHANGELOG.md, and the router points at real files.

## Watch for

- **Stale pins in `templates/`.** Dependabot scans this repo's own `.github/workflows/`, not the
  workflow files under `templates/`. Template pins go stale silently and every bootstrapped
  repository inherits it. Check them during each self-audit (`references/self-audit.md`).
- **Contradictions between the maturity stages.** `references/scaling-model.md` is authoritative for
  what belongs at which stage; `workflows/project-bootstrap.md` and
  `references/bootstrap-checklist.md` must agree with it.
- **Ceremony creep.** The skill's own value depends on Stage 0 work staying lightweight.
