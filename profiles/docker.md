# Profile: Docker

Apply when `Dockerfile`, Compose files, or container build configuration exists.

## Image design

Prefer:

- small trusted base images;
- explicit versions where practical;
- multi-stage builds for compiled/build-heavy projects;
- non-root runtime user;
- minimal runtime packages;
- deterministic builds.

## Security

Do not:

- bake secrets into images;
- use `ADD` when `COPY` is sufficient;
- run as root without need;
- expose unnecessary ports;
- disable TLS verification;
- copy entire build context blindly if `.dockerignore` can reduce risk.

Maintain `.dockerignore`.

## Runtime

Define:

- health check where useful;
- graceful shutdown;
- log-to-stdout/stderr behavior;
- persistent volume expectations;
- environment configuration.

## CI

Build the container in CI when containers are part of the supported delivery model.

Scan built images with a container scanner such as Trivy or Grype. Dependency auditing covers
declared application dependencies only; it cannot see vulnerable operating-system packages in the
base image. Severity thresholds and triage follow `references/vulnerability-management.md`.

For production-grade projects, also consider:

- SBOM generation;
- image signing;
- immutable tags/digests.
