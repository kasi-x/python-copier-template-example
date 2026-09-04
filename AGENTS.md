# Agent Guide for `python-copier-template-example`

This file is for AI coding agents working in this repository. It states how
to run the checks and where edits belong. The human-facing contribution
guide is [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md).

## Commands

The `task` task runner drives the common commands:

```sh
task lint           # pre-commit on all files
task test           # pytest
task type-check     # type checker + static analysis
task check          # everything above
```

Run `task check` (or `lint` + `test`
+ `type-check` individually) before finishing a change.

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
  (`feat:`, `fix:`, ...); the commit-msg hook enforces it.
- CI runs lint, type-check, and tests on every push
 plus a docs build; keep all of them green.
