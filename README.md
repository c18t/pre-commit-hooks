# pre-commit-hooks

my hooks for pre-commit

See also: <https://github.com/pre-commit/pre-commit>

## Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/c18t/pre-commit-hooks
  rev: v1.2.0 # Use the ref you want to point at
  hooks:
    - id: shellcheck
    # - id: ...
```

## Hooks available

- `shellcheck` - Run [shellcheck](https://github.com/koalaman/shellcheck)
 against scripts.
- `yamllint` - Run [yamllint](https://github.com/adrienverge/yamllint)
 against YAML files.
- `hadolint` - Run [hadolint](https://github.com/hadolint/hadolint)
 against Dockerfile.
