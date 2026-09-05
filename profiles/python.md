# Profile: Python

Apply when Python project files are detected.

## Preferred modern baseline

For new Python projects, prefer:

- `pyproject.toml` for project metadata;
- `uv` for Python/runtime management, dependency resolution, environments, and lockfile;
- `pytest` as the default test runner;
- `ruff` for linting and formatting;
- `mypy` or `pyright` when static typing adds meaningful value.

Preserve a healthy existing toolchain rather than migrating solely for consistency.

## uv conventions

Commit `pyproject.toml` and `uv.lock`. Do not commit `.venv/`.

Prefer standardized dependency groups:

```toml
[dependency-groups]
test = ["pytest", "pytest-cov"]
lint = ["ruff"]
typecheck = ["mypy"]
dev = [
  { include-group = "test" },
  { include-group = "lint" },
  { include-group = "typecheck" },
]
```

For tiny projects, one `dev` group is acceptable.

Typical commands:

```bash
uv sync --locked
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

In CI, use locked dependency resolution. Fail if the lockfile is inconsistent rather than silently regenerating it.

## Testing

Use `pytest`.

A bug fix should normally add a regression test.
Test happy paths, failures, validation, security-sensitive behavior, and important integration boundaries.

## Structure

For reusable applications/libraries, prefer `src/<package>/`.
For very small utilities, a simpler structure is acceptable.

## Configuration

Never hardcode secrets. Use environment variables/configuration and provide `.env.example` when useful.

## Packaging

Document supported Python versions.

For applications, `uv.lock` is part of reproducibility.
For published libraries, maintain appropriate dependency constraints in project metadata because downstream users do not consume the repository lockfile.
