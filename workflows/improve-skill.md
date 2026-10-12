# Workflow: Improve Project Steward

Use when a reusable capability gap is detected.

## 1. Capture the gap

Document:

- task that exposed the gap;
- current limitation;
- temporary workaround;
- whether similar cases have occurred before.

## 2. Classify scope

Decide:

- repository-local knowledge;
- reusable Project Steward capability.

If local, update only the repository guidance.

If reusable, continue with a Skill Improvement Proposal.

## 3. Assess risk

Classify the proposed skill change:

- Low
- Medium
- High

Use `references/skill-evolution-policy.md`.

## 4. Prepare SIP

Create a SIP using:

`templates/skill-improvements/SIP-template.md`

## 5. Approval behavior

### Requested by the owner

The explicit request is the approval: apply, release and install in one pass (`references/skill-evolution-policy.md`, "Owner-requested changes").

### Low risk

May auto-apply when confidence is high.

### Medium risk

Present SIP and obtain user approval before changing global defaults.

### High risk

Explicit approval is mandatory.

## 6. Implement

Keep the change focused.

Update as needed:

- `SKILL.md`
- `references/`
- `workflows/`
- `profiles/`
- `templates/`
- detection logic
- documentation

## 7. Validate

Check:

- no contradictory rules;
- no broken references;
- templates parse where applicable;
- security posture is not weakened;
- existing workflows still make sense.

## 8. Version

Update:

- `VERSION`
- `CHANGELOG.md`

Use Semantic Versioning for Project Steward itself. Tag the release, push it as the skill repository's autonomy section allows, and update the installed copy (`references/skill-evolution-policy.md`, "Source and installed copies").

## 9. Report

Summarize:

- gap;
- solution;
- risk classification;
- changed files;
- validation performed;
- new version.
