# FIT1045 C++ Template

Reusable C++ starter workspace for FIT1045-style programming work.

This branch keeps C++ tooling separate from the clean `main` branch and from
other profile-specific work:

- `src/main.cpp` is the starter entrypoint.
- C/C++ settings avoid hardcoded compiler paths.
- `Makefile` uses the compiler available on `PATH`.
- SplashKit can be added through the environment your class requires.
- VS Code AI helper settings are disabled by default for this profile.

## Getting Started

1. Create your own repository from this template branch.
2. Open `project.code-workspace` in VS Code.
3. Install the compiler/tooling required by your class environment.
4. Run the VS Code task `C++: Build src/main.cpp`.
5. Run `C++: Run`.

Command-line equivalent:

```powershell
make
```

If you use MSYS2 MINGW64, open the matching terminal before running `make` so
the compiler is available on `PATH`.

## SplashKit

This branch does not commit a machine-specific SplashKit path. Configure
SplashKit in your local environment, then adjust `CXX` or `CXXFLAGS` locally if
your setup requires it.

## AI Toggle

AI helper settings start disabled in `.vscode/settings.json`.

```powershell
powershell -ExecutionPolicy Bypass -File scripts/toggle-vscode-ai.ps1 -Mode status
powershell -ExecutionPolicy Bypass -File scripts/toggle-vscode-ai.ps1 -Mode enable
powershell -ExecutionPolicy Bypass -File scripts/toggle-vscode-ai.ps1 -Mode disable
```

## License

This repository uses The Unlicense.
