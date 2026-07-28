#!/usr/bin/env python3
"""Fail if text files contain UTF-8 BOM or CRLF/CR line endings."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def git_bytes(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], stderr=subprocess.STDOUT)


def git_text(*args: str) -> str:
    return git_bytes(*args).decode("utf-8", errors="replace")


def staged_paths() -> list[str]:
    out = git_text("diff", "--cached", "--name-only", "--diff-filter=ACMR")
    return [line.strip() for line in out.splitlines() if line.strip()]


def head_paths() -> list[str]:
    try:
        out = git_text("ls-tree", "-r", "--name-only", "HEAD")
    except subprocess.CalledProcessError:
        # Initial commit fallback.
        out = git_text("ls-files")
    return [line.strip() for line in out.splitlines() if line.strip()]


def read_staged(path: str) -> bytes | None:
    try:
        return git_bytes("show", f":{path}")
    except subprocess.CalledProcessError:
        return None


def read_head(path: str) -> bytes | None:
    try:
        return git_bytes("show", f"HEAD:{path}")
    except subprocess.CalledProcessError:
        return None


def is_binary(data: bytes) -> bool:
    return b"\x00" in data


def detect_issues(data: bytes) -> list[str]:
    issues: list[str] = []
    if data.startswith(b"\xef\xbb\xbf"):
        issues.append("UTF-8 BOM")
    if b"\r\n" in data:
        issues.append("CRLF line endings")
    elif b"\r" in data:
        issues.append("CR line endings")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed-only", action="store_true", help="check staged files only")
    args = parser.parse_args()

    if args.changed_only:
        paths = staged_paths()
        read_fn = read_staged
        scope_label = "staged files"
    else:
        paths = head_paths()
        read_fn = read_head
        scope_label = "tracked files in HEAD"

    failures: list[tuple[str, list[str]]] = []

    for path in paths:
        data = read_fn(path)
        if data is None or is_binary(data):
            continue
        issues = detect_issues(data)
        if issues:
            failures.append((path, issues))

    if failures:
        print(f"[TEXT-POLICY] Format violations detected in {scope_label}:", file=sys.stderr)
        for path, issues in failures:
            print(f"  - {path}: {', '.join(issues)}", file=sys.stderr)
        print("[TEXT-POLICY] Required: UTF-8 without BOM + LF line endings.", file=sys.stderr)
        return 1

    print(f"[TEXT-POLICY] Passed ({scope_label}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())