"""Static import checker used by Git hooks to enforce ENG1014 import allowlist."""
# CRITICAL FILE FORMAT: keep UTF-8 without BOM and LF line endings only.
# If BOM/CRLF is introduced, Python parsing can fail and block commit/push checks.
from __future__ import annotations

import argparse
import ast
from pathlib import Path
from subprocess import CalledProcessError, run
from typing import Iterable, List, Set

from policy import (
    WORKSPACE_ROOT,
    is_local_module,
    is_stdlib_module,
    load_policy,
    normalize_module_root,
    validate_package_versions,
    validate_python_version,
)


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(WORKSPACE_ROOT).as_posix()
    except ValueError:
        return path.name


def staged_python_files() -> List[Path]:
    tools_dir = (WORKSPACE_ROOT / "tools").resolve()
    try:
        result = run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            cwd=WORKSPACE_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except CalledProcessError:
        return []

    files = []
    for line in result.stdout.splitlines():
        if not line.endswith(".py"):
            continue
        path = (WORKSPACE_ROOT / line).resolve()
        if path.is_relative_to(tools_dir):
            continue
        files.append(path)
    return files


def all_python_files() -> List[Path]:
    excluded_dirs = {
        ".git",
        "build",
        "tools",
        ".venv",
        "venv",
        "env",
        "__pycache__",
        "site-packages",
    }
    return [
        path
        for path in WORKSPACE_ROOT.rglob("*.py")
        if all(part not in excluded_dirs for part in path.parts)
    ]


def imported_roots(path: Path) -> Set[str]:
    roots: Set[str] = set()
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=display_path(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                roots.add(normalize_module_root(alias.name))
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            roots.add(normalize_module_root(node.module))
    return roots


def check_files(files: Iterable[Path]) -> List[str]:
    policy = load_policy()
    allowed = policy.allowed_import_roots

    failures: List[str] = []

    py_ok, py_msg = validate_python_version(policy)
    if not py_ok:
        failures.append(py_msg)
    failures.extend(validate_package_versions(policy))

    for file_path in files:
        if not file_path.exists():
            continue
        label = display_path(file_path)
        try:
            roots = imported_roots(file_path)
        except SyntaxError as exc:
            failures.append(f"{label}: syntax error prevents policy check ({exc})")
            continue
        except UnicodeDecodeError as exc:
            failures.append(
                f"{label}: file is not valid UTF-8 ({exc}); exclude it from the scan or re-encode it"
            )
            continue

        for root in sorted(roots):
            if is_stdlib_module(root) or is_local_module(root):
                continue
            if root not in allowed:
                failures.append(
                    f"{label}: blocked import '{root}' is not allowlisted in docs/environment/eng1014.yaml"
                )

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed-only", action="store_true", help="Check only staged Python files.")
    args = parser.parse_args()

    files = staged_python_files() if args.changed_only else all_python_files()
    failures = check_files(files)

    if failures:
        print("[MONASH-POLICY] Import/version policy check failed:")
        for failure in failures:
            print(f"  - {failure}")
        print("[MONASH-POLICY] Disable temporarily with MONASH_PYTHON_POLICY_ENFORCE=0")
        return 1

    print("[MONASH-POLICY] Import/version policy check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
