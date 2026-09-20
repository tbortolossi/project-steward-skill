# SIP-0003: Refresh running environments after integrating into the default branch

- Status: Accepted (requested by the project owner during the task that exposed the gap)
- Risk: Medium
- Proposed version: 0.11.0
- Date: 2026-09-20

## Observed gap

The skill treats a change as complete once it is merged, documented and its
temporary branches are cleaned up. Nothing says that the environments which
track the default branch — a local preview container, a staging host, a
push-to-deploy target — must be brought up to date, or verified, after the
merge. `workflows/deploy.md` covers deploying when the user asks to deploy;
it is never reached from a feature or fix that simply lands on `main`.

## Evidence

A static-site repository with a Docker production preview. A content
feature was merged into `main`, verified with the full local pipeline, and
reported as done. The preview container on the owner's machine kept
serving the previous image for half an hour, until the owner asked
"rebuild du coup?". The rebuild was then done by hand, and the owner asked
for it to be automated and for the skill to carry the rule.

## Why this belongs in Project Steward

Any repository with a long-running environment built from a branch has the
same gap: after integration the running version silently lags the source.
It is not specific to Docker, to static sites or to a solo maintainer. The
hook or CI job that fixes it is project-local; the rule that it must exist,
be versioned and be verified is reusable.

## Proposed change

1. `references/git-workflow.md`, Merge strategy: after integrating into the
   default branch, bring every environment that tracks that branch up to
   date, preferably through an automated trigger, and verify it. Set the
   trigger up the first time it is missing.
2. `references/definition-of-done.md`: a checklist item and a completion
   criterion for environments tracking the integrated branch.
3. `workflows/deploy.md`: a section describing the refresh-after-integration
   pattern — versioned hooks directory enabled with `core.hooksPath`, or a
   CI job on push to the default branch — with its safety rules: act only on
   the default branch, run detached, log outside the tracked tree, skip
   silently when the tooling is absent, and never deploy to production
   without the checks of the same workflow.
4. `workflows/new-feature.md` and `workflows/bugfix.md`: the completion step
   points to the merge rule.

No existing rule is weakened or removed.

## Files affected

- `references/git-workflow.md`
- `references/definition-of-done.md`
- `workflows/deploy.md`
- `workflows/new-feature.md`
- `workflows/bugfix.md`
- `CHANGELOG.md`
- `VERSION`

## Compatibility impact

Additive. A repository with no environment tracking a branch has nothing to
refresh and the rule does not fire. A repository that already deploys
through CI on push already satisfies it.

## Security impact

A git hook that runs a build is code executed on every merge, so it must be
versioned, reviewed like any other script, and must not carry credentials.
The pattern restricts it to the default branch and to local or preview
targets. Production deployment keeps its own preconditions, approval and
rollback path in `workflows/deploy.md`; this SIP does not make production
deploys automatic.

## Risks

- A background rebuild that fails silently. Mitigated by the verify step:
  a smoke test or a request against the refreshed environment, reported to
  the user.
- Hooks are per-clone configuration. Mitigated by versioning the hooks
  directory and documenting the one-line enable command in the README.
- Reading the rule as "auto-deploy to production". The wording limits the
  automatic path to environments the developer owns; production goes
  through the deploy workflow.

## Validation plan

`scripts/check_skill.py` passes. Re-run a feature merge in the repository
that exposed the gap and confirm the preview rebuilds from the hook and the
report includes the verification.

## Rollback plan

`git revert` the implementing commit. Repositories that added a hook keep
working; the hook is theirs, not the skill's.

## Versioning rationale

MINOR: the Definition of Done gains a mandatory item, which is a medium-risk
change under the evolution policy; no existing rule changed or removed.
