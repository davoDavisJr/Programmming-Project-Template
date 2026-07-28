# ENG1014 Python VS Code Template

Reusable Python workspace for ENG1014-style numerical analysis work.

This profile adds strict Python environment checks to the clean Monash base:

- Python must be `3.10.11`.
- Packages must match `docs/environment/eng1014.yaml`.
- Third-party imports are blocked unless listed in that YAML file.
- VS Code terminals, debug sessions, tasks, and Git hooks use the same policy.

## Getting Started

1. Create your own repository from this template branch.
2. Open `project.code-workspace` in VS Code.
3. Select a Python `3.10.11` interpreter with the required packages installed.
4. Run `ENG1014: Validate Environment`.
5. Run `Python: Run src/main.py`.

## Required Packages

The source of truth is `docs/environment/eng1014.yaml`.

Current declared dependencies:

- `python=3.10.11`
- `numpy=2.2.2`
- `matplotlib=3.10`
- `jupyterlab`
- `pandas=2.2.3`

## Hooks

Enable repository hooks once per clone:

```powershell
git config core.hooksPath .githooks
```

The hooks check text-file formatting and the ENG1014 Python policy.

Use local Git config for machine-specific interpreter paths:

```powershell
git config monash.pythonPath <path-to-python-3.10.11>
```

## Temporary Bypass

Use bypasses only for intentional template maintenance:

```powershell
MONASH_PYTHON_POLICY_ENFORCE=0 git commit
```

## License

This repository uses The Unlicense.
