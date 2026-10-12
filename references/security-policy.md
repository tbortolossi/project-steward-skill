# Security Engineering Policy

## Baseline rules

Never commit:

- passwords;
- API keys;
- private keys;
- access tokens;
- session cookies;
- cloud credentials;
- production `.env` files;
- sensitive customer data.

Provide `.env.example` with placeholders where configuration is required. Where secrets live instead,
how they reach the code, and how that grows with the project: `references/secrets-management.md`.

## Dependency security

Before adding a dependency, consider:

- necessity;
- maintenance health;
- license;
- known vulnerabilities;
- transitive dependency cost;
- whether equivalent capability already exists.

Adoption is only the first check. Dependencies must also be scanned continuously for advisories
published after they were adopted — see `references/vulnerability-management.md`. Never remove,
mute, or weaken a dependency audit merely to make CI green.

## Security-sensitive changes

Changes affecting authentication, authorization, cryptography, secrets, webhooks, deserialization, file upload, command execution, networking, or trust boundaries require elevated review.

## Input handling

Treat external input as untrusted.

Apply:

- validation;
- normalization where appropriate;
- safe parsing;
- output encoding;
- least privilege;
- bounded resource use.

## AI-assisted development

Never instruct an AI agent to bypass security controls just to complete a task.

Do not accept generated code that:

- disables TLS verification without explicit need;
- uses shell execution unnecessarily;
- logs secrets;
- stores plaintext credentials;
- introduces unsafe deserialization;
- broadens permissions without justification.

## Disclosure

Maintain `SECURITY.md` with a private reporting path or project-appropriate contact mechanism.
