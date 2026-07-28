# First-Time Setup

Install Git, VS Code, and Python `3.10.11`.

Create your own copy with GitHub's **Use this template** button, then open
`project.code-workspace` in VS Code.

Select the interpreter:

1. Open the Command Palette.
2. Run `Python: Select Interpreter`.
3. Choose Python `3.10.11`.

Enable the optional repository hooks:

```powershell
git config core.hooksPath .githooks
```

Run the starter program:

```powershell
python tools/python_version/run_with_version.py src/main.py
```
