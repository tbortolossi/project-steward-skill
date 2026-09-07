# Self-Audit — 2026-09-07

First run of `references/self-audit.md`. Skill version at audit time: 0.8.0.

Scope: all 18 references, 7 workflows, 7 profiles, 14 templates, `SKILL.md`, `OPERATING-GUIDE.md`,
`README.md`. Pinned tool versions were checked against upstream release data rather than assumed.

## Summary

Five findings, all addressed in 0.9.0. The most serious was invisible from inside the repository:
every pinned tool version in `templates/` was stale, some by three or four major versions, and
nothing existed to detect it.

| # | Finding | Severity | Action |
|---|---|---|---|
| 1 | All pinned versions in `templates/` stale; no mechanism to notice | High | Fixed + safeguard added |
| 2 | `workflows/project-bootstrap.md` contradicts itself on staging | Medium | Fixed |
| 3 | Skill prescribed CI, secret scanning and agent instructions it did not apply to itself | Medium | Fixed |
| 4 | `OPERATING-GUIDE.md` orphaned — referenced from nowhere | Low | Fixed |
| 5 | `SKILL.md` router creeping back toward pre-0.6.0 size | Low | Watch |

---

## 1. Stale version pins in templates — Obsolescence

Every pinned version in the repository was behind upstream, checked 2026-09-07:

| Pin | Was | Current | Behind |
|---|---|---|---|
| `actions/checkout` | v4 | v7.0.1 | 3 majors |
| `actions/setup-python` | v5 | v7.0.0 | 2 majors |
| `actions/setup-node` | v4 | v7.0.0 | 3 majors |
| `astral-sh/setup-uv` | v6 | v10.0.1 | 4 majors |
| `gitleaks/gitleaks-action` | v2 | v3.0.0 | 1 major |
| `gitleaks` (pre-commit) | v8.28.0 | v8.30.1 | patch/minor |
| `ruff-pre-commit` | v0.12.11 | v0.16.6 | 4 minors |

This is worse than ordinary drift. Templates are *copied into other repositories*, so every project
bootstrapped from them inherited stale pins, and the staleness propagated silently.

**Root cause.** Dependabot's `github-actions` ecosystem scans a repository's real
`.github/workflows/`. It does not scan workflow files sitting inside a `templates/` directory, since
those are inert text from its point of view. So the one mechanism that would normally catch this was
structurally blind to it — and the repository had no Dependabot configuration of its own anyway.

**Action.** All pins updated. Two upgrades carried real breakage risk and were verified against
upstream before applying rather than assumed safe:

- `setup-uv` v6 → v10 (four majors): confirmed the `enable-cache` input still exists.
- `ruff-pre-commit` 0.12 → 0.16: confirmed the `ruff-check` and `ruff-format` hook ids still exist.

`gitleaks-action` v2 → v3 is a Node 20 → 24 runtime migration with no input/output changes.

**Safeguard.** `references/self-audit.md` now carries an explicit obsolescence question naming the
`templates/` blind spot and why Dependabot cannot cover it.

**Residual risk.** The safeguard is a checklist item, not automation. It relies on the self-audit
actually being run. Automating it would mean querying upstream release APIs from CI — network
dependency and rate limits for a check that only needs to run a few times a year. Accepted
deliberately; revisit if pins go stale again.

## 2. Bootstrap workflow contradicts its own staging — Contradiction / Excessive ceremony

`workflows/project-bootstrap.md` step 2 classified the repository into Stage 0–3 and warned "Do not
impose Stage 3 controls on a Stage 0 experiment". Step 3, immediately after, listed a flat baseline
of fifteen files to create — CONTRIBUTING, PROJECT, ROADMAP, CHANGELOG, architecture documentation,
issue/PR templates — with no reference to the stage just determined.

Following the workflow literally meant burying every scratch experiment in Stage 2 governance, which
is precisely the failure mode the skill exists to avoid. It also contradicted
`references/scaling-model.md`, which places those documents at Stage 2.

**Action.** Step 3 rewritten as a stage-aware baseline, with `references/scaling-model.md` as the
authority and `references/bootstrap-checklist.md` as the full checkbox list.

## 3. The skill did not apply its own rules — Missing safeguards

The repository prescribed CI, secret scanning, dependency hygiene, and `AGENTS.md` for every project
while having none of them. No `.github/` directory existed at all.

The practical cost was not hypothetical: the structural errors this audit found — a self-contradicting
workflow, an orphaned document, seven stale pins — are exactly what a check would have surfaced
earlier.

**Action.** Added `.github/workflows/ci.yml` (structural checks), `.github/workflows/gitleaks.yml`
(secret scan, on schedule), `.github/dependabot.yml` (GitHub Actions ecosystem), `AGENTS.md`, and
`scripts/check_skill.py`.

The check script verifies templates parse as YAML, internal references resolve, `SKILL.md` keeps the
frontmatter Claude Code needs for discovery, `VERSION` agrees with `CHANGELOG.md`, and every router
entry points at a real file. It was validated by deliberately breaking four things and confirming all
four were caught — a check that cannot fail is not a check.

## 4. `OPERATING-GUIDE.md` orphaned — Documentation

Referenced from nowhere: not in `README.md`'s file list, not in `SKILL.md`, not in any reference. A
44-line guide on how to work with the skill, effectively invisible.

**Action.** Listed in `README.md`. Now covered by the reference check, so it cannot silently
disappear again.

## 5. `SKILL.md` size creep — Excessive ceremony

0.6.0 rewrote `SKILL.md` as a compact router of ~165 lines, down from ~530. It is now 168 lines and
the router lists 18 references, having gained a section in each of 0.7.0 and 0.8.0.

Not yet a problem, but the growth is one-directional and the router is the file most likely to
regress toward the pre-0.6.0 wall of text.

**Action.** No change. Recorded in `AGENTS.md` as a standing constraint: extract to `references/`
rather than append. Re-check at the next audit.

---

## Audit questions with no findings

- **Repeated manual work.** No recurring corrections or workarounds observed yet. Usage history is
  short; this question needs more real projects before it can be answered meaningfully.
- **Profile conflicts.** Python, Node, Docker, Terraform, FastAPI, AI/LLM and GitHub Actions profiles
  prescribe no incompatible defaults. Each defers to existing healthy repository conventions.
- **Agents bypassing tests / committing sensitive artifacts / unprotected destructive actions.**
  `references/ai-agent-policy.md`, `references/data-leak-prevention.md` and
  `references/git-workflow.md` cover these; no gaps found.
- **Project-specific exceptions leaking into global defaults.** None found. The local-versus-global
  distinction in `references/skill-evolution-policy.md` is holding.

## Open question for the next audit

`references/risk-tiers.md` specifies "PR review recommended" (Medium) and "Security review" (High)
without saying who performs them in a single-maintainer repository. Solo maintainer mode in
`references/scaling-model.md` replaces human code review with agent self-verification plus owner
behavior validation, and states that security checks do not relax — but it does not spell out what a
"security review" concretely means when the only reviewer is the agent that wrote the change.

Not contradictory, but under-specified. Left open deliberately rather than resolved by guesswork:
the right answer depends on how solo mode performs in practice.
