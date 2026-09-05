# Cost Policy

## Purpose

Delegated engineering must not create financial surprises. Any change that introduces or increases spending is at least medium risk and follows the corresponding approval rules in `references/risk-tiers.md`.

## Before introducing anything that costs money

Signal to the user, before implementing, whenever a change introduces:

- a paid API or a free API with quotas that the project could realistically exceed;
- a cloud resource (compute, database, storage, hosting) — especially anything always-on;
- a paid dependency, service tier, or license;
- an LLM/AI model choice with per-call pricing.

Provide a rough estimate of one-time and **recurring** monthly cost under realistic usage, and a cheaper alternative when one exists.

Recurring costs always require explicit user approval. Never silently upgrade a service tier or switch to a more expensive model.

## Defaults

- Prefer free, local, or already-paid-for options when they are adequate.
- Prefer the cheapest adequate model/tier; upgrading is a user decision.
- Prefer scale-to-zero or on-demand resources over always-on ones for small projects.
- Watch the classic silent cost sources: always-on servers, per-call APIs in loops, storage growth, data egress, CI minutes, log retention.

## Documentation

Record in `PROJECT.md`:

- every paid service the project depends on;
- expected monthly cost and what drives it;
- where the billing/usage dashboard is.

Recommend budget alerts on any cloud or API account the project uses.

## Cleanup

When work is abandoned or an experiment ends, identify resources that keep billing (instances, databases, scheduled jobs) and either remove them or list them explicitly for the user.
