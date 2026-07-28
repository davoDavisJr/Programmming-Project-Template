# Contributing

This repository is maintained as a reusable Monash project template.

For most students and personal work, the recommended path is to click **Use this
template** on GitHub or create a fork for your own project copy.

## How to contribute back

Contributions are welcome via pull requests:

1. Fork this repository.
2. Create a branch for your change.
3. Open a pull request back to this repository.

## Good contribution examples

- Documentation improvements and clarifications.
- VS Code task or workspace quality-of-life improvements.
- Cross-platform compatibility fixes.
- Better starter scaffolding or helper code that is not an assessed solution.

## Academic integrity and content rules

Do not submit:

- Assignment solutions for assessed work.
- Copyrighted course content that you do not have permission to redistribute.
- Machine-specific paths, credentials, tokens, or private local artifacts.

## Contributor Python Setup

This repository checks Python version compatibility only. Use Python `3.10.11`
unless a profile branch documents additional requirements.

1. Enable hooks once per clone:

```powershell
git config core.hooksPath .githooks
```

2. Install or select Python `3.10.11`.

3. If Git cannot find the right interpreter, configure it locally:

```powershell
git config monash.pythonPath <path-to-python-3.10.11>
```

4. Validate before opening a pull request:

```powershell
git hook run pre-push
```

If this check fails, fix the selected Python interpreter or update
`monash.pythonPath`.

## Pull Request Expectations

- Keep pull requests focused on one main idea.
- Update docs when behavior or usage changes.
- Preserve `UTF-8 without BOM` and `LF` line endings for hooks and Python tools.
- Do not commit generated build output or exported submission artifacts.
