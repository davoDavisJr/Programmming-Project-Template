#!/usr/bin/env python3
"""Validate that the active interpreter is the template Python version."""

from __future__ import annotations

import os
import sys

REQUIRED_VERSION = os.environ.get("MONASH_PYTHON_REQUIRED_VERSION", "3.10.11")


def current_version() -> str:
    return ".".join(str(part) for part in sys.version_info[:3])


def main() -> int:
    if os.environ.get("MONASH_PYTHON_VERSION_ENFORCE", "1") != "1":
        print("[PYTHON-VERSION] Check bypassed by MONASH_PYTHON_VERSION_ENFORCE.")
        return 0

    installed = current_version()
    if installed == REQUIRED_VERSION:
        print(f"[PYTHON-VERSION] Python {installed} satisfies {REQUIRED_VERSION}.")
        return 0

    print(
        f"[PYTHON-VERSION] Python {installed} does not satisfy {REQUIRED_VERSION}.",
        file=sys.stderr,
    )
    print(
        "[PYTHON-VERSION] Select Python 3.10.11 or set "
        "MONASH_PYTHON_VERSION_ENFORCE=0 for one intentional bypass.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
