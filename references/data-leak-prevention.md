# Repository Data Leak Prevention

## Purpose

Prevent credentials, secrets, confidential artifacts, personal data, customer data, and accidental diagnostic exports from entering Git history.

Git history must be treated as durable. Deleting a file in a later commit does not remove the original leak.

## Defense in depth

Use several layers:

1. developer/agent review before staging;
2. `.gitignore` and artifact exclusions;
3. pre-commit secret scanning where practical;
4. CI secret scanning;
5. GitHub native secret scanning;
6. GitHub push protection when available;
7. periodic full-history scans for important repositories.

No individual scanner is sufficient.

## Before staging files

Review new files and unusual binary/large files.

Look specifically for:

- `.env` files;
- credentials;
- API tokens;
- private keys;
- certificates with private material;
- Terraform state;
- kubeconfig files;
- cloud credential files;
- database dumps;
- packet captures;
- support bundles;
- logs;
- HAR files;
- browser/session exports;
- spreadsheets/CSV exports;
- screenshots;
- configuration backups;
- model/provider debug traces.

## Dangerous filename patterns

Do not commit without explicit review:

- `.env`
- `.env.*` except `.env.example`
- `*.pem`
- `*.key`
- `*.p12`
- `*.pfx`
- `terraform.tfstate*`
- `*.pcap`
- `*.pcapng`
- `*.har`
- `*.sqlite`
- `*.db`
- `*.sql`
- `*.dump`
- `*.bak`
- `credentials*.json`
- `service-account*.json`
- `kubeconfig*`

Use sanitized synthetic fixtures when such formats are required by tests.

## Content review

Flag possible:

- bearer tokens;
- passwords;
- authorization headers;
- cookies/session IDs;
- cloud API keys;
- SSH/private keys;
- JWTs;
- database connection strings;
- customer names/emails/phone numbers;
- internal ticket/support data.

Automated PII detection is heuristic. A clean scan does not prove that a repository contains no sensitive data.

## Recommended scanner

Use Gitleaks as a portable repository-level baseline unless the project already has a comparable scanner.

Recommended checks:

- pre-commit or pre-push for fast developer feedback;
- CI on pull requests;
- full-history scan periodically or before making a repository public.

Do not silently add broad allowlists to make scans pass.

## When a secret is found

Assume a committed credential may be compromised.

1. Stop propagation.
2. Revoke/rotate the credential.
3. Determine exposure scope.
4. Remove the secret from current files.
5. Rewrite Git history if appropriate.
6. Coordinate force-push/history cleanup carefully.
7. Verify forks, caches, artifacts, CI logs, and release assets as applicable.
8. Document the incident privately where appropriate.

History rewriting does not replace credential rotation.

## AI agents

AI agents must not:

- paste credentials into issue/PR descriptions;
- paste sensitive logs without sanitization;
- upload local `.env` or cloud credential files;
- include secrets in generated screenshots/examples;
- treat a private GitHub repository as a secret-management system.

Use synthetic/redacted examples by default.
