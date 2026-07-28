"""Validate the active Python runtime against docs/environment/eng1014.yaml."""
# CRITICAL FILE FORMAT: keep UTF-8 without BOM and LF line endings only.
# If BOM/CRLF is introduced, environment validation may fail before checks run.
from __future__ import annotations

from policy import load_policy, validate_package_versions, validate_python_version


def main() -> int:
    policy = load_policy()

    py_ok, py_msg = validate_python_version(policy)
    failures = []
    if not py_ok:
        failures.append(py_msg)

    failures.extend(validate_package_versions(policy))

    if failures:
        print("[MONASH-POLICY] Environment validation failed:")
        for failure in failures:
            print(f"  - {failure}")
        print("[MONASH-POLICY] Disable temporarily with MONASH_PYTHON_POLICY_ENFORCE=0")
        return 1

    print("[MONASH-POLICY] Environment validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
