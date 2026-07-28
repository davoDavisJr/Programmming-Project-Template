# ENG1005 LaTeX Template

Reusable LaTeX-first template for ENG1005 mathematics reports and related
technical writeups.

This branch keeps the LaTeX workflow focused:

- `LaTeX/main.tex` is the document entrypoint.
- Build output goes to `build/latex/`.
- Exported PDFs go to `docs/export/`.
- Generated files and exported PDFs are ignored by Git.
- No strict Python package/import policy is enforced.

## Getting Started

1. Create your own repository from this template branch.
2. Open `project.code-workspace` in VS Code.
3. Install a LaTeX distribution such as MiKTeX or TeX Live.
4. Run the VS Code task `LaTeX: Doctor`.
5. Run `LaTeX: Build Template`.

Command-line equivalents:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/latex-doctor.ps1
powershell -ExecutionPolicy Bypass -File scripts/build-latex.ps1
```

Export a PDF when needed:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/export-latex.ps1
```

## Repository Structure

`LaTeX/`
Report source, metadata, macros, bibliography, figures, data, and sections.

`scripts/`
LaTeX build, export, clean, and diagnostic helpers.

`build/`
Generated build output, ignored by Git.

`docs/export/`
Generated exported PDFs, ignored by Git except for `.gitkeep`.

## Privacy

Commit the source required to reproduce your report. Do not commit generated
logs, build folders, or private submission PDFs unless an external workflow
explicitly requires it.

## License

This repository uses The Unlicense.
