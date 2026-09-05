# Project Steward Self-Audit

Run periodically or when the skill feels repetitive, contradictory, or outdated.

## Audit questions

### Repeated manual work

- Which instructions have been repeated manually across repositories?
- Which user corrections recur?
- Which missing profiles/workflows recur?
- Which boilerplate is repeatedly recreated?

### Contradictions

- Do any references conflict with `SKILL.md`?
- Do technology profiles prescribe incompatible defaults?
- Do workflow requirements conflict with maturity stages?

### Obsolescence

- Have recommended tools changed materially?
- Are version-specific examples stale?
- Are ecosystem standards now different?
- Are security recommendations still appropriate?

### Excessive ceremony

- Is Stage 0/1 work receiving unnecessary governance?
- Are tiny fixes requiring too much process?
- Are approval gates creating friction without reducing risk?

### Missing safeguards

- Are agents bypassing tests?
- Are sensitive artifacts being committed?
- Are destructive actions sufficiently protected?
- Are project-specific exceptions leaking into global defaults?

## Output

Produce:

- keep;
- simplify;
- deprecate;
- add;
- investigate.

Reusable improvements should become SIPs.
