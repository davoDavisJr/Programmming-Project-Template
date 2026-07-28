# Monash Project Template

Reusable starter workspace for Monash coursework and small programming projects.

The `main` branch is the clean base template. It provides a beginner-friendly
repository layout, VS Code configuration, Git hygiene, and a Python `3.10.11`
version check without adding course-specific package rules or machine-specific
toolchain paths.

## Using This Repository

Most students should click **Use this template** on GitHub or create a fork for
personal use.

## Getting Started Guides

New to Git, GitHub, or VS Code? Start with:

- [Guides Landing Page](docs/guides/README.md)
- [First-Time Setup](docs/guides/first-time-setup.md)
- [Using GitHub Day to Day](docs/guides/using-github.md)
- [Using VS Code with This Repository](docs/guides/using-vscode.md)
- [Submitting Assignments Safely](docs/guides/submitting-assignments.md)

## Repository Structure

`src/`
Starter source files.

`tools/`
Small validation helpers used by this template.

`build/`
Generated output, ignored by Git except for `.gitkeep`.

`docs/`
Notes, diagrams, and documentation.

`.vscode/`
Project-specific VS Code configuration.

`.githooks/`
Optional repository-managed Git hooks for text and Python-version checks.

## Getting Started

1. Create your own copy with GitHub's **Use this template** button.
2. Open `project.code-workspace` in VS Code.
3. Select Python `3.10.11` with `Python: Select Interpreter`.
4. Enable hooks once per clone:

```powershell
git config core.hooksPath .githooks
```

5. Run the starter file with the VS Code task `Python: Run src/main.py`, or run:

```powershell
python tools/python_version/run_with_version.py src/main.py
```

## Python Version Check

This branch checks only the Python runtime version:

- Required version: `3.10.11`
- No third-party package allowlist is enforced on `main`
- Local virtual environments are ignored by Git

Run the check directly:

```powershell
python tools/python_version/check_version.py
```

If a Git client cannot find the right Python executable, set a local-only path:

```powershell
git config monash.pythonPath <path-to-python-3.10.11>
```

Disable the version hook for one command only when intentionally maintaining
template infrastructure:

```powershell
MONASH_PYTHON_VERSION_ENFORCE=0 git commit
```

## Documentation

Additional documentation is stored in `docs/`. Important files include:

- `docs/environment/python-3.10.11.md`
- `docs/guides/README.md`

## License

This repository uses The Unlicense.
