# ENG1014 Python Policy

This profile enforces the dependency list in `eng1014.yaml`.

The policy applies in three places:

1. VS Code terminals and debug sessions receive policy environment variables.
2. Git hooks run the static import checker before commits and pushes.
3. The validation task checks Python and package versions before running code.

Machine-specific interpreter paths belong in local Git config:

```powershell
git config monash.pythonPath <path-to-python-3.10.11>
```

Do not commit virtual environments, caches, package directories, or generated
notebooks with private local output.
