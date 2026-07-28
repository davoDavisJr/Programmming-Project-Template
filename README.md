# ENG1013 Python Template

Reusable Python starter workspace for ENG1013-style coursework and small
engineering programming tasks.

This branch keeps the setup deliberately plain:

- Python `3.10.11` is checked explicitly.
- `src/main.py` is the starter entrypoint.
- No third-party package allowlist is enforced.
- No machine-specific interpreter or toolchain path is committed.

## Getting Started

1. Create your own repository from this template branch.
2. Open `project.code-workspace` in VS Code.
3. Select Python `3.10.11` with `Python: Select Interpreter`.
4. Run the VS Code task `Python: Run src/main.py`.

Command-line equivalent:

```powershell
python tools/python_version/run_with_version.py src/main.py
```

## Repository Structure

`src/`
Python source files.

`tools/python_version/`
Runtime version check helpers.

`docs/`
Setup notes and beginner guides.

`.vscode/`
VS Code tasks, launch configuration, and extension recommendations.

## Python Version

The required interpreter version is `3.10.11`.

Run the check directly:

```powershell
python tools/python_version/check_version.py
```

If a Git client cannot find your chosen interpreter, set a local-only path:

```powershell
git config monash.pythonPath <path-to-python-3.10.11>
```

## License

This repository uses The Unlicense.
