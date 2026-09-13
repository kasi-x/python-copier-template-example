# Agent Guide for `python-copier-template-example`

This file is for AI coding agents working in this repository. It states how
to run the checks and where edits belong. The human-facing contribution
guide is [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md).

## Commands

The `task` task runner drives the common commands:

```sh
task fix            # auto-fix formatting and lint
task lint           # ruff format --check + ruff check (check-only)
task test           # pytest
task type-check     # type checker + static analysis
task check          # everything above
```

Run `task fix` before committing to apply formatting
and lint fixes, then `task check` (or `lint` + `test`
+ `type-check` individually) before finishing a change.
The repo-hygiene checks (secrets, workflow linting, YAML validity,
conventional commit messages) run in CI, not as local hooks — the lint and
fix tasks work anywhere, including outside a git repository.

Type checking uses basedpyright plus `pyrefly`; `deptry`,
`vulture`, and `typos` also run as part of type-check.


Build the docs with `task docs`.

## Where to edit

- Application/package code: `src/python_copier_template_example/`
- Tests: `tests/`
- Docs: `README.md` and `docs/`

Keep 100% coverage where it exists; do not lower it.


Data, notebooks, and reports (`data/`, `notebooks/`, `models/`,
`reports/`) are analysis artifacts — keep generated outputs out of git.

## Commits and CI

- Use [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat:`, `fix:`, ...); the repository's hygiene CI enforces it on commit
  messages and the PR title.
- CI runs lint, type-check, and tests on every push
 plus a docs build; keep all of them green.
