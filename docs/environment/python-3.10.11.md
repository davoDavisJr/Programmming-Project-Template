# Python 3.10.11 Runtime

The base template expects Python `3.10.11`.

This branch checks only the interpreter version. It does not pin third-party
packages and does not restrict imports.

Recommended setup:

1. Install Python `3.10.11`.
2. Select that interpreter in VS Code.
3. Run `python tools/python_version/check_version.py`.

If your Git client cannot find the interpreter selected in VS Code, configure a
local-only path:

```powershell
git config monash.pythonPath <path-to-python-3.10.11>
```

Local Git config is not committed, so every collaborator can use their own
machine-specific path without leaking it into the template.
