# Workflow: Deploy

Use when putting a project online or updating a deployed environment. Deployment to production is at least medium risk; first-time production setup and anything destructive is high risk (`references/risk-tiers.md`).

## 1. Preconditions

Verify before deploying:

- tests and CI are green;
- the deployed version is committed and tagged or otherwise identifiable;
- no secrets in the repository; production secrets live in the platform's secret store or environment configuration;
- cost impact of the target infrastructure is known and approved (`references/cost-policy.md`).

## 2. Environments

- Keep configuration out of code: environment variables, documented in `.env.example`.
- Separate at minimum a local/dev setup from production; never test against production data or credentials.
- Document which environment exists, where it runs, and who can access it.

## 3. Deploy

- Prefer the platform's standard, repeatable mechanism (a deploy command, a push-to-deploy branch, a CI job) over manual steps.
- Record the exact procedure in a runbook (`docs/` or `templates/docs/troubleshooting.md` structure) the first time; reuse it afterwards.
- For databases: back up before schema migrations, and treat irreversible migrations as high risk requiring explicit approval.

## 4. Verify after deploying

- Run a smoke test against the deployed environment: the app starts, the main path works, authentication works if present.
- Show the user the deployed result (URL, real request/response, screenshot) per `references/reporting-to-user.md`.

## 5. Rollback

Before the first production deploy, establish and document:

- how to return to the previous version;
- how to restore data if a migration went wrong;
- how long a rollback takes.

A deploy without a known rollback path is incomplete.

## 6. Minimum operations

For anything users depend on:

- error logging that persists and is readable;
- a way to know the service is down (uptime check or platform alert);
- documented location of logs and dashboards.

## 7. Report

Tell the user in plain language: what is deployed and where, the URL, what it costs per month, how to check it is healthy, and how to roll back.
