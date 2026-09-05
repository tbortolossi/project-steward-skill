# Language Policy

## Goal

Allow the user to interact naturally in their preferred language while keeping repository artifacts consistent and professional.

## User interaction

Project Steward should respond to the user in the language the user is using, unless the user explicitly requests another language.

Examples:

- French user request -> conversational explanations in French.
- English user request -> conversational explanations in English.

## Repository artifact language

By default, all repository artifacts must be written in English.

This includes:

- README files;
- CONTRIBUTING;
- SECURITY;
- PROJECT;
- ROADMAP;
- CHANGELOG;
- ADRs;
- issue titles and descriptions;
- pull request titles and descriptions;
- commit messages;
- release notes;
- architecture documentation;
- troubleshooting documentation;
- code comments;
- docstrings;
- generated examples;
- CI comments/messages where controlled by the project.

## Code identifiers

Prefer English for:

- variable names;
- function names;
- class names;
- module names;
- API fields;
- configuration keys;
- internal identifiers.

Do not rename established project conventions solely to enforce English unless there is a clear maintainability benefit.

## Exceptions

Use another language for repository artifacts only when:

- the user explicitly requests it;
- the product is intentionally localized;
- user-facing content must target a specific locale;
- legal/regulatory text requires another language.

Even in those cases, keep technical/internal project documentation in English unless there is a strong reason not to.

## Example

User says in French:

`Ajoute un export JSON des incidents et mets à jour la doc.`

Project Steward may answer conversationally in French, while producing repository artifacts in English, for example:

- commit: `feat: add JSON incident export`
- PR title: `Add JSON incident export`
- README section: written in English
- code comments/docstrings: written in English
