"""sitecustomize hook: block non-allowlisted third-party imports from user code."""
# CRITICAL FILE FORMAT: keep UTF-8 without BOM and LF line endings only.
# If BOM/CRLF is introduced, runtime import guarding can fail at Python startup.
from __future__ import annotations

import builtins
import inspect
import os
from pathlib import Path
from typing import Any, Optional

from policy import (
    WORKSPACE_ROOT,
    is_local_module,
    is_stdlib_module,
    load_policy,
    normalize_module_root,
    validate_package_versions,
    validate_python_version,
)


def _is_under(path: Path, maybe_parent: Path) -> bool:
    try:
        path.resolve().relative_to(maybe_parent.resolve())
        return True
    except Exception:
        return False


def _is_user_origin(frame: Optional[inspect.FrameInfo]) -> bool:
    policy_tool_dir = (WORKSPACE_ROOT / "tools" / "python_policy").resolve()
    cursor = frame
    while cursor is not None:
        filename = cursor.f_code.co_filename
        if filename and not filename.startswith("<"):
            path = Path(filename)
            if _is_under(path, policy_tool_dir):
                return False
            if _is_under(path, WORKSPACE_ROOT):
                return True
            lowered = str(path).lower()
            if "site-packages" in lowered or "dist-packages" in lowered:
                return False
        cursor = cursor.f_back
    return True


def _install_guard() -> None:
    policy = load_policy()
    allowed = policy.allowed_import_roots

    py_ok, py_msg = validate_python_version(policy)
    pkg_failures = validate_package_versions(policy)
    if not py_ok or pkg_failures:
        details = [py_msg] if not py_ok else []
        details.extend(pkg_failures)
        raise ImportError(
            "[MONASH-POLICY] Runtime blocked due to non-compliant environment:\n"
            + "\n".join(f"- {item}" for item in details)
            + "\nDisable temporarily with MONASH_PYTHON_POLICY_ENFORCE=0"
        )

    original_import = builtins.__import__

    def guarded_import(
        name: str,
        globals_dict: Optional[dict[str, Any]] = None,
        locals_dict: Optional[dict[str, Any]] = None,
        fromlist: Any = (),
        level: int = 0,
    ) -> Any:
        if level == 0 and _is_user_origin(inspect.currentframe().f_back):
            root = normalize_module_root(name)
            if not is_stdlib_module(root) and not is_local_module(root):
                if root not in allowed:
                    raise ImportError(
                        "[MONASH-POLICY] Import blocked: '"
                        + root
                        + "' is not listed in docs/environment/eng1014.yaml. "
                        "Disable temporarily with MONASH_PYTHON_POLICY_ENFORCE=0"
                    )
        return original_import(name, globals_dict, locals_dict, fromlist, level)

    builtins.__import__ = guarded_import


if os.environ.get("MONASH_PYTHON_POLICY_ENFORCE", "1") == "1":
    _install_guard()
