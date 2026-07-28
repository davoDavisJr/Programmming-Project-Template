# LaTeX Template

This folder is a reusable mathematics/report template for Monash coursework.
It is general enough for technical reports, but its defaults are tuned for
ENG1005-style mathematical working.

## Main Files

- `main.tex` is the document entrypoint.
- `metadata.tex` stores the unit, assignment, student, semester, and abstract
  placeholders.
- `preamble.tex` loads document packages and layout settings.
- `macros.tex` defines mathematics helpers, theorem-like environments, and the
  `problem`/`solution` workflow.
- `sections/` contains modular content files.
- `figures/` and `data/` are tracked as empty input folders for assignment
  material.
- `references.bib` stores bibliography entries when references are needed.
  Uncomment `\printbibliography` in `main.tex` once the document cites sources.

## Common Commands

Run commands from the repository root.

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build-latex.ps1
powershell -ExecutionPolicy Bypass -File scripts/export-latex.ps1
powershell -ExecutionPolicy Bypass -File scripts/latex-doctor.ps1
powershell -ExecutionPolicy Bypass -File scripts/clean-latex.ps1
```

VSCode tasks expose the same workflow:

- `LaTeX: Build Template`
- `LaTeX: Export Template PDF`
- `LaTeX: Doctor`
- `LaTeX: Clean`
- `LaTeX: Word Count`

## Adapting for an Assignment

1. Replace placeholder values in `metadata.tex`.
2. Rename or add section files under `sections/`.
3. Put diagrams in `figures/` and source data in `data/`.
4. Keep problem statements, working, and final answers together using the
   `problem` and `solution` environments.
5. Add bibliography entries to `references.bib` only when the assignment uses
   external sources.

Do not commit private exported PDFs or generated build files. The template is
intended to keep source material reproducible while leaving submission artifacts
local unless a course process says otherwise.
