# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working
with code in this repository.

## Project Overview

This is a collection of custom pre-commit hooks designed to be used with the
[pre-commit framework](https://github.com/pre-commit/pre-commit). The
repository provides hooks that wrap common linting and formatting tools.

## Architecture

The project is a dual-language repository:

- **Python hooks**: Located in [hooks/](hooks/) directory, packaged via Poetry
  - Currently contains [yamllint.py](hooks/yamllint.py) which wraps yamllint
    with custom encoding support
  - Entry points are defined in [pyproject.toml](pyproject.toml) under
    `[tool.poetry.scripts]`

- **Node.js hooks**: Managed via pnpm (required, not npm/yarn)
  - Currently provides the `pretty-quick` hook for formatting staged files

- **System hooks**: Require tools to be installed on the system
  - Currently provides `shellcheck` for shell script linting

Hook definitions are exported via
[.pre-commit-hooks.yaml](.pre-commit-hooks.yaml) for consumption by other
repositories.

### Key Implementation Detail: yamllint Hook

The [yamllint.py](hooks/yamllint.py) wrapper exists to handle encoding issues
on Windows:

- Accepts `--encoding` argument to set `PYTHONIOENCODING` environment variable
- Finds yamllint executable across different platforms (handles PATHEXT on Windows)
- Processes files one at a time, piping content to yamllint via stdin
- This design allows yamllint to work correctly with different file encodings

## Development Commands

### Initial Setup

```bash
mise run setup
```

This installs all tools via mise and configures pre-commit hooks.

### Testing Changes Locally

To test hooks in this repository:

```bash
pre-commit run --all-files
```

To test hooks in another repository before publishing:

```yaml
# In another repo's .pre-commit-config.yaml
- repo: local
  hooks:
    - id: yamllint
      name: yamllint
      entry: /path/to/pre-commit-hooks/hooks/yamllint.py
      language: python
      # ...
```

### Package Management

Python dependencies:

```bash
poetry install
poetry add <package>
```

Node.js dependencies (must use pnpm):

```bash
pnpm install
pnpm add <package>
```

### Version Bumping

When releasing a new version:

1. Update version in [pyproject.toml](pyproject.toml) (Python hooks)
2. Update version in [package.json](package.json) (Node hooks)
3. Update version in [README.md](README.md) example
4. Tag the release with `v<version>`

## Tool Configuration

- mise: [.mise.toml](.mise.toml) - defines Python 3.9+, latest Node.js/pnpm,
  and dev tools
- yamllint: [.yamllint.yaml](.yamllint.yaml)
- prettier: [.prettierrc](.prettierrc) and [.prettierignore](.prettierignore)
- markdownlint: [.markdownlint.yaml](.markdownlint.yaml)
- flake8: [.flake8](.flake8)
