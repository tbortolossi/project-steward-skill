# Profile: FastAPI

Apply when FastAPI is detected.

## Structure

Separate:

- API routing;
- business logic;
- persistence;
- external integrations;
- configuration;
- schemas/models.

Avoid putting substantial business logic directly in route handlers.

## API behavior

Define:

- request validation;
- response models;
- status codes;
- error schema;
- authentication/authorization;
- versioning strategy when public.

## Security

Review:

- CORS;
- authentication;
- authorization;
- input validation;
- file uploads;
- SSRF risk;
- webhook verification;
- rate/resource limits;
- sensitive error leakage.

Do not expose stack traces or secrets in production responses.

## Tests

Use:

- route-level tests;
- service-level tests;
- auth failure tests;
- invalid input tests;
- dependency override/mocking where appropriate.

## Documentation

Keep OpenAPI descriptions useful.

Document non-obvious authentication, headers, rate limits, and examples.
