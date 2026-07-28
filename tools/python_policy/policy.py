"""Shared helpers for enforcing the ENG1014 Python package policy."""
# CRITICAL FILE FORMAT: keep UTF-8 without BOM and LF line endings only.
# If BOM/CRLF is introduced, policy parsing/import checks can fail unexpectedly.
from __future__ import annotations

from dataclasses import dataclass
from importlib import metadata
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
import os
import re
import sys

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_POLICY_PATH = WORKSPACE_ROOT / "docs" / "environment" / "eng1014.yaml"

# Explicit aliases for packages whose import names do not always match the dist name.
PACKAGE_IMPORT_ALIASES: Dict[str, Set[str]] = {}

_DEPENDENCY_RE = re.compile(r"^\s*-\s*([A-Za-z0-9_.-]+)(?:=([^\s#]+))?\s*$")


@dataclass(frozen=True)
class Policy:
    name: str
    python_version: Optional[str]
    package_versions: Dict[str, Optional[str]]

    @property
    def allowed_import_roots(self) -> Set[str]:
        roots: Set[str] = set()
        for package_name in self.package_versions:
            if package_name == "python":
                continue
            roots.add(package_name.replace("-", "_").split(".")[0])
            roots.update(PACKAGE_IMPORT_ALIASES.get(package_name, set()))
        return roots


def _get_policy_path() -> Path:
    env = os.environ.get("MONASH_PYTHON_POLICY_FILE")
    if env:
        path = Path(env)
        if not path.is_absolute():
            path = WORKSPACE_ROOT / path
        return path.resolve()
    return DEFAULT_POLICY_PATH.resolve()


def load_policy(policy_path: Optional[Path] = None) -> Policy:
    path = (policy_path or _get_policy_path()).resolve()
    name = "eng1014"
    package_versions: Dict[str, Optional[str]] = {}
    python_version: Optional[str] = None
    in_dependencies = False

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("name:"):
            name = stripped.split(":", 1)[1].strip()
            continue
        if stripped == "dependencies:":
            in_dependencies = True
            continue
        if in_dependencies and stripped and not line.startswith("  -"):
            in_dependencies = False
        if not in_dependencies:
            continue

        match = _DEPENDENCY_RE.match(line)
        if not match:
            continue
        package = match.group(1)
        version = match.group(2)
        package_versions[package] = version
        if package == "python":
            python_version = version

    if not package_versions:
        raise ValueError(f"No dependencies parsed from policy file: {path}")

    return Policy(name=name, python_version=python_version, package_versions=package_versions)


def is_version_match(installed: str, required: str) -> bool:
    # Allow prefix-style YAML specs like "3.10" to match "3.10.14".
    return installed == required or installed.startswith(required + ".")


def validate_python_version(policy: Policy) -> Tuple[bool, str]:
    if not policy.python_version:
        return True, "Python version is not pinned in policy."

    installed = ".".join(str(part) for part in sys.version_info[:3])
    ok = is_version_match(installed, policy.python_version)
    if ok:
        return True, f"Python {installed} satisfies required {policy.python_version}."
    return False, f"Python {installed} does not satisfy required {policy.python_version}."


def validate_package_versions(policy: Policy) -> List[str]:
    failures: List[str] = []
    for package, required in policy.package_versions.items():
        if package == "python":
            continue
        try:
            installed = metadata.version(package)
        except metadata.PackageNotFoundError:
            failures.append(f"Missing required package: {package}")
            continue

        if required and not is_version_match(installed, required):
            failures.append(
                f"Package {package} version {installed} does not satisfy required {required}"
            )
    return failures


def is_stdlib_module(module_root: str) -> bool:
    if module_root in sys.builtin_module_names:
        return True
    stdlib = getattr(sys, "stdlib_module_names", set())
    return module_root in stdlib


def is_local_module(module_root: str, workspace_root: Optional[Path] = None) -> bool:
    root = workspace_root or WORKSPACE_ROOT
    return (root / f"{module_root}.py").exists() or (root / module_root / "__init__.py").exists()


def normalize_module_root(module_name: str) -> str:
    return module_name.split(".", 1)[0]
