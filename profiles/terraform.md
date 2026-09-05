# Profile: Terraform

Apply when `.tf` files are detected.

## Principles

- infrastructure changes are code changes;
- avoid manual drift;
- keep modules focused;
- separate environment-specific values from reusable logic;
- never commit secrets into `.tf`, `.tfvars`, or state.

## Quality

Run as appropriate:

- `terraform fmt`
- `terraform validate`
- static/security analysis if configured
- `terraform plan`

Never claim infrastructure is safe solely because validation succeeds.

## State

Treat Terraform state as sensitive.

Document:

- backend;
- locking;
- recovery;
- import strategy;
- workspace/environment strategy.

## Modules

Use modules when they create meaningful reuse or isolation.

Avoid premature module abstraction for tiny one-off resources.

## Changes

For high-impact changes, inspect plan for:

- destroy/recreate;
- network/security rule changes;
- identity/permission expansion;
- public exposure;
- data loss;
- replacement of stateful services.

Require explicit user confirmation before destructive production changes unless already explicitly authorized.
