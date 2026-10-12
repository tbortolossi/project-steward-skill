#!/usr/bin/env python3
"""Set non-secret variables in a .env file without ever showing its content.

The agent may write configuration such as a project id, a region, a file path or a model name, but
it must not read the file: whatever it reads enters the model's context and the session transcript,
including the secrets that sit next to the setting it wanted. This script is the narrow door:

    set_env.py [--file .env] KEY=VALUE [KEY=VALUE ...]   add or replace each variable
    set_env.py [--file .env] --check KEY [KEY ...]       print "KEY set" or "KEY -", never values
    set_env.py [--file .env] --unset KEY [KEY ...]       remove each variable and its comments

`--header TEXT` puts a "# TEXT" comment above the variables appended by one call. `--unset` also
removes the comment lines directly above the variable (up to a blank line), which describe it.

It prints variable names only. It refuses secret-looking names (API keys, tokens, passwords...) and
secret-looking values (provider key prefixes, JWTs, PEM blocks, JSON, long random strings): secrets
are pasted by the owner. Other lines, comments and file permissions are kept; a new file is created
with mode 0600. See references/secrets-management.md, "AI agents and secrets".
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from pathlib import Path

NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
# A name made of one of these words names a secret, unless it ends with _FILE, _PATH or _DIR
# (then the value is where a secret lives, not the secret).
SECRET_WORDS = re.compile(
    r"(^|_)(API_?KEY|KEY|TOKEN|SECRET|PASSWORD|PASSWD|PASS|PWD|PRIVATE|AUTH|COOKIE|SESSION|DSN)(_|$)",
    re.IGNORECASE,
)
PATH_SUFFIXES = ("_FILE", "_PATH", "_DIR")
SECRET_PREFIXES = (
    "sk-", "sk_", "pk_", "rk_", "ghp_", "gho_", "ghs_", "github_pat_", "glpat-", "xox",
    "AKIA", "ASIA", "AIza", "ya29.", "eyJ", "-----BEGIN", "ssh-", "npm_", "pypi-",
)
LONG_TOKEN = re.compile(r"^[A-Za-z0-9_\-+=]{40,}$")


class Refused(ValueError):
    pass


def check_secret(name: str, value: str) -> None:
    if not NAME.match(name):
        raise Refused(f"{name!r} is not a valid variable name")
    if SECRET_WORDS.search(name) and not name.upper().endswith(PATH_SUFFIXES):
        raise Refused(f"{name} names a secret: the owner sets it")
    stripped = value.strip()
    if stripped.startswith(SECRET_PREFIXES) or stripped.startswith(("{", "[")):
        raise Refused(f"the value for {name} looks like a secret: the owner sets it")
    if LONG_TOKEN.match(stripped):
        raise Refused(f"the value for {name} looks like a token: the owner sets it")
    if "\n" in value:
        raise Refused(f"the value for {name} spans several lines")


def render(name: str, value: str) -> str:
    if value and not re.search(r"[\s#'\"\\$`]", value):
        return f"{name}={value}"
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("$", "\\$").replace("`", "\\`")
    return f'{name}="{escaped}"'


def assignment(line: str, name: str) -> bool:
    return re.match(rf"^\s*(export\s+)?{re.escape(name)}\s*=", line) is not None


def unset(lines: list[str], names: list[str]) -> tuple[list[str], dict[str, str]]:
    """Drop each assignment of the names, with the comment block right above it."""
    result: list[str] = []
    outcome = {name: "absent" for name in names}
    for line in lines:
        name = next((n for n in names if assignment(line, n)), None)
        if name is None:
            result.append(line)
            continue
        outcome[name] = "removed"
        while result and result[-1].lstrip().startswith("#"):
            result.pop()
    # Collapse the blank lines left behind.
    tidy: list[str] = []
    for line in result:
        if line.strip() or (tidy and tidy[-1].strip()):
            tidy.append(line)
    while tidy and not tidy[-1].strip():
        tidy.pop()
    return tidy, outcome


def apply(
    lines: list[str], updates: dict[str, str], header: str | None = None
) -> tuple[list[str], dict[str, str]]:
    """Replace the first assignment of each name, drop later duplicates, append the missing ones."""
    result: list[str] = []
    outcome: dict[str, str] = {}
    for line in lines:
        name = next((n for n in updates if assignment(line, n)), None)
        if name is None:
            result.append(line)
        elif name not in outcome:
            ending = "\n" if line.endswith("\n") else ""
            result.append(render(name, updates[name]) + ending)
            outcome[name] = "replaced"
    missing = [n for n in updates if n not in outcome]
    if missing and result and not result[-1].endswith("\n"):
        result[-1] += "\n"
    if missing and header:
        if result and result[-1].strip():
            result.append("\n")
        result.append(f"# {header}\n")
    for name in missing:
        result.append(render(name, updates[name]) + "\n")
        outcome[name] = "added"
    return result, outcome


def write(path: Path, lines: list[str]) -> None:
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o600
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
        with os.fdopen(fd, "w") as handle:
            handle.writelines(lines)
        os.chmod(tmp, mode)
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def defined(lines: list[str], name: str) -> bool:
    for line in lines:
        match = re.match(rf"^\s*(export\s+)?{re.escape(name)}\s*=(.*)$", line.rstrip("\n"))
        if match and match.group(2).strip() not in ("", '""', "''"):
            return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--file", default=".env", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="report which names are set")
    mode.add_argument("--unset", action="store_true", help="remove the named variables")
    parser.add_argument("--header", help="comment placed above the appended variables")
    parser.add_argument("items", nargs="+", metavar="KEY=VALUE | KEY")
    args = parser.parse_args(argv)
    lines = args.file.read_text().splitlines(keepends=True) if args.file.exists() else []

    if args.check:
        for name in args.items:
            print(f"{name} {'set' if defined(lines, name) else '-'}")
        return 0

    if args.unset:
        bad = [name for name in args.items if not NAME.match(name)]
        if bad:
            print(f"refused: not variable names: {bad}", file=sys.stderr)
            return 2
        new_lines, outcome = unset(lines, args.items)
        if args.file.exists():
            write(args.file, new_lines)
        for name, what in outcome.items():
            print(f"{name} {what}")
        return 0

    if args.header and ("\n" in args.header or args.header.startswith(SECRET_PREFIXES)):
        print("refused: the header must be one line of plain text", file=sys.stderr)
        return 2
    updates: dict[str, str] = {}
    try:
        for item in args.items:
            name, sep, value = item.partition("=")
            if not sep:
                raise Refused(f"{item!r} is not KEY=VALUE")
            check_secret(name, value)
            updates[name] = value
    except Refused as refused:
        print(f"refused: {refused}", file=sys.stderr)
        return 2

    new_lines, outcome = apply(lines, updates, args.header)
    write(args.file, new_lines)
    for name, what in outcome.items():
        print(f"{name} {what}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
