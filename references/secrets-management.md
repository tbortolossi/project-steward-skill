# Secrets Management

`references/security-policy.md` says what must never be committed. This file says where secrets live
instead, how they reach the code, and how that grows with the project.

## Principles

- A secret has one source of truth, outside the repository. Copies on disk are derived from it and
  disposable.
- One secret per environment and per purpose. Development never uses production credentials.
- Least privilege: a token can do what its consumer needs and nothing more.
- Prefer short-lived credentials (OIDC federation, temporary tokens) to long-lived keys.
- Every secret can be rotated without a code change, and someone knows how.
- Plaintext secrets on disk are a liability: anything that can read the file, including an AI agent
  or a backup, can read the secret.

## Choosing where secrets live

Pick the lowest rung that fits the project's stage (`references/scaling-model.md`) and the value of
what the secret protects. Record the choice in `README.md` ("Configuration") and, from Stage 2, in
an ADR.

| Rung | Mechanism | Fits |
|---|---|---|
| 1 | Local `.env`, gitignored, with `.env.example` listing names only | Stage 0–1, dev-only, low-value credentials |
| 2 | Password manager CLI injecting at run time (`op run --env-file=.env.tpl -- <cmd>`, Bitwarden `bws run`, `pass`, OS keychain) — no plaintext file | Stage 1 default when the owner has a password manager |
| 3 | Encrypted files committed with sops + age (or git-crypt); keys kept outside the repository | Stage 2, config shared between machines or people |
| 4 | Dedicated secret manager: HashiCorp Vault / OpenBao, Infisical, Doppler, or the cloud's own (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault) | Stage 2–3, deployed services, several environments |

Rules for choosing:

- Ask the owner which password manager or cloud they already use; reuse it rather than adding one.
- A self-hosted Vault is an operated service (unsealing, backups, upgrades). Do not propose it to a
  solo project unless the owner already runs one; a managed service or the cloud's secret manager is
  usually the better rung 4.
- Rungs 3 and 4 may cost money or add an account: follow `references/cost-policy.md`.
- Moving up a rung is a `security` change: migrate, rotate the old values, then delete the old
  copies.

## Getting secrets into the code

- Read configuration in one place (a settings module), validate it at startup, and fail fast with
  the *name* of a missing variable, never its value.
- Inject secrets as environment variables or mounted files at run time. Never bake them into
  container images, build artifacts, front-end bundles, or committed config.
- Keep `.env.example` (or `.env.tpl` for rung 2, which holds references such as
  `op://vault/item/field`, not values) current: it is the configuration reference.
- Redact secrets from logs, error messages, traces and crash reports.

## CI and deployment

- CI secrets live in the platform's secret store (GitHub Actions secrets, scoped to an environment
  when the secret deploys somewhere).
- Prefer OIDC federation from CI to the cloud over long-lived cloud keys stored as CI secrets.
- Pull-request workflows from forks must not receive secrets.
- Production secrets come from the rung-4 manager at deploy or run time, with access logged.

## AI agents and secrets

- The agent never needs a secret's value to write code that uses it. It works from names in
  `.env.example`.
- The agent does not read, print, or paste `.env` files, key files, or credential stores, and does
  not ask the owner to paste a secret into the conversation. When a command needs a secret, the
  owner runs it, or it runs through rung 2 injection.
- In Claude Code, deny rules in `.claude/settings.json` back this up (`references/claude-code.md`,
  "Project setup"). They are a guard rail, not a vault: rung 2 and above keep plaintext off the disk
  entirely, which is the real protection.

## Rotation and incidents

- Document for each secret: what it unlocks, where it is stored, how to rotate it.
- Rotate on suspicion of exposure, when someone with access leaves, and on the schedule the provider
  or stage requires (Stage 3).
- A secret that reached git, a log, a ticket or a chat is compromised: follow
  `references/data-leak-prevention.md`, "When a secret is found". Rotation comes first.
