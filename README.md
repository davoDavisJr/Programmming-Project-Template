# MARIE Template

Reusable MARIE assembly starter workspace.

This branch keeps the MARIE workflow isolated from the clean `main` branch and
from the other course profiles:

- `src/main.mas` is the starter source file.
- `MARIE_ROOT` defaults to `$(HOME)/.MARIE` in `Makefile`.
- No personal simulator path is committed.
- No bundled course PDFs are included.

## Getting Started

1. Create your own repository from this template branch.
2. Open `project.code-workspace` in VS Code.
3. Install or clone the MARIE simulator required by your class.
4. Set `MARIE_ROOT` locally if your simulator is not in the default location.
5. Run the VS Code task `MARIE: Check Setup`.

PowerShell check:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/marie-check.ps1
```

Makefile check:

```powershell
make marie-check
```

## Local Paths

Use environment variables or shell-local overrides for machine-specific paths:

```powershell
$env:MARIE_ROOT = "<path-to-your-marie-simulator>"
```

Do not commit personal absolute paths.

## License

This repository uses The Unlicense.
