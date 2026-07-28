# Submitting Assignments Safely

Before submitting, check that your source files are saved and committed, and
that generated output stays out of Git.

Do not commit local virtual environments, Python caches, build folders, exported
PDFs, screenshots containing private information, or files with absolute paths
from your own computer.

Run:

```powershell
git status --short --branch
git hook run pre-push
```
