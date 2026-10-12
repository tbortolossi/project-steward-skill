#!/usr/bin/env python3
"""Structural checks for the Project Steward skill repository.

The skill prescribes CI, so it runs CI on itself. There is no application code
here, but there is plenty that can break silently: a template that stops being
valid YAML, a reference to a file that was renamed, a version that disagrees
with the changelog, a skill file without the frontmatter Claude Code needs to
discover it.

Run locally with:

    python scripts/check_skill.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

# Skill-internal directories. A path reference into one of these must resolve.
INTERNAL_PREFIXES = ("references/", "workflows/", "profiles/", "templates/", "scripts/")

# Paths that name files inside a *target* repository rather than this one.
# `docs/architecture.md` is advice to the user's project, not a file here.
TARGET_REPO_PREFIXES = ("docs/architecture", "docs/adr", "docs/troubleshooting")

# Claude Code truncates description + when_to_use beyond this many characters.
LISTING_LIMIT = 1536

REFERENCE_PATTERN = re.compile(
    r"`((?:references|workflows|profiles|templates|scripts|docs)/[A-Za-z0-9_./-]+)`"
)


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.checks = 0

    def check(self, name: str, ok: bool, detail: str = "") -> None:
        self.checks += 1
        if ok:
            print(f"  ok    {name}")
        else:
            print(f"  FAIL  {name}{': ' + detail if detail else ''}")
            self.failures.append(name)


def markdown_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md") if ".git" not in p.parts and "node_modules" not in p.parts
    )


def yaml_files() -> list[Path]:
    return sorted(
        p
        for p in list(ROOT.rglob("*.yml")) + list(ROOT.rglob("*.yaml"))
        if ".git" not in p.parts
    )


def check_yaml(report: Report) -> None:
    print("\nYAML templates parse")
    for path in yaml_files():
        rel = path.relative_to(ROOT).as_posix()
        try:
            yaml.safe_load(path.read_text(encoding="utf-8"))
            report.check(rel, True)
        except yaml.YAMLError as exc:
            report.check(rel, False, str(exc).splitlines()[0])


def check_references(report: Report) -> None:
    print("\nInternal file references resolve")
    broken: list[str] = []
    total = 0
    sources = markdown_files() + yaml_files()
    for path in sources:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for match in REFERENCE_PATTERN.findall(text):
            target = match.rstrip(".")
            if target.startswith(TARGET_REPO_PREFIXES):
                continue
            if not target.startswith(INTERNAL_PREFIXES) and not target.startswith("docs/"):
                continue
            if target.endswith("/"):
                continue
            total += 1
            if not (ROOT / target).exists():
                broken.append(f"{rel} -> {target}")
    report.check(
        f"{total} references checked",
        not broken,
        "; ".join(sorted(set(broken))),
    )


def check_skill_frontmatter(report: Report) -> None:
    print("\nSKILL.md is discoverable")
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        report.check("frontmatter present", False, "SKILL.md does not open with ---")
        return
    _, _, rest = text.partition("---\n")
    raw, sep, _ = rest.partition("\n---")
    report.check("frontmatter present", bool(sep))
    if not sep:
        return
    try:
        meta = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        report.check("frontmatter parses", False, str(exc).splitlines()[0])
        return
    report.check("frontmatter parses", True)
    report.check("has name", meta.get("name") == "project-steward", repr(meta.get("name")))
    description = meta.get("description") or ""
    report.check("has description", bool(description.strip()))
    # Claude Code truncates description + when_to_use in its skill listing; past
    # the limit the trigger phrases at the end silently stop matching.
    listing = len(description) + len(meta.get("when_to_use") or "")
    report.check(
        f"trigger text fits the listing ({listing}/{LISTING_LIMIT} chars)",
        listing <= LISTING_LIMIT,
    )


def check_claude_template(report: Report) -> None:
    """Claude Code ignores AGENTS.md when a CLAUDE.md exists, unless it imports it."""
    print("\nCLAUDE.md template imports AGENTS.md")
    path = ROOT / "templates" / "CLAUDE.md"
    first = path.read_text(encoding="utf-8").splitlines()[:1] if path.exists() else []
    report.check("templates/CLAUDE.md starts with @AGENTS.md", first == ["@AGENTS.md"])


def check_version_consistency(report: Report) -> None:
    print("\nVersion metadata is consistent")
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    report.check("VERSION is SemVer", bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), version)
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    report.check(
        f"CHANGELOG has a [{version}] section",
        f"## [{version}]" in changelog,
        f"no '## [{version}]' heading found",
    )


def check_referenced_policies_exist(report: Report) -> None:
    """Every reference listed in SKILL.md's router must be a real file."""
    print("\nSKILL.md router points at real files")
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    listed = re.findall(r"^- `((?:references|workflows|profiles)/[^`]+)`", text, re.MULTILINE)
    missing = [t for t in listed if not (ROOT / t).exists()]
    report.check(f"{len(listed)} router entries", not missing, ", ".join(missing))


def main() -> int:
    report = Report()
    check_yaml(report)
    check_references(report)
    check_skill_frontmatter(report)
    check_claude_template(report)
    check_version_consistency(report)
    check_referenced_policies_exist(report)

    print(f"\n{report.checks} checks run")
    if report.failures:
        print(f"{len(report.failures)} failed:")
        for name in report.failures:
            print(f"  - {name}")
        return 1
    print("all passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
