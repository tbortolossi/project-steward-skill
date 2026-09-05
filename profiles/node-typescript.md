# Profile: Node / TypeScript

Apply when Node.js or TypeScript project files are detected.

## Preferred modern baseline

For new projects, prefer:

- TypeScript over plain JavaScript for anything beyond a throwaway script;
- `npm` by default (universally available); `pnpm` is a fine choice when the user or repo already uses it — do not migrate an existing healthy setup;
- `vitest` as the default test runner;
- `eslint` for linting and `prettier` for formatting (or `biome` as a single-tool alternative in new projects);
- `tsconfig.json` with `"strict": true` for new projects.

Preserve a healthy existing toolchain rather than migrating solely for consistency.

## Conventions

- Commit the lockfile (`package-lock.json` or `pnpm-lock.yaml`); never mix package managers in one repository.
- Do not commit `node_modules/`, `dist/`, or build output.
- Declare the supported Node version (`engines` field, optionally `.nvmrc`).
- Use the standard script names so any agent or human can operate the project:

```json
{
  "scripts": {
    "dev": "…",
    "build": "…",
    "test": "vitest run",
    "lint": "eslint ."
  }
}
```

In CI, install with the lockfile (`npm ci`) and fail on lockfile inconsistency rather than regenerating it.

## Dependencies

The npm ecosystem invites dependency sprawl. Before adding a package:

- prefer the standard library and built-in Node/browser APIs;
- prefer well-maintained, widely used packages over micro-packages;
- check license and maintenance status for anything load-bearing.

## Testing

A bug fix should normally add a regression test. Test happy paths, failures, input validation, and security-sensitive behavior.

## Configuration

Never hardcode secrets. Use environment variables and provide `.env.example`. For front-end code, remember that anything shipped to the browser is public — secrets must stay server-side.
