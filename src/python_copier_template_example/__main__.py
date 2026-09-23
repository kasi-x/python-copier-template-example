"""Interface for ``python -m python_copier_template_example``."""

from argparse import ArgumentParser
from collections.abc import Sequence

from . import __version__
from .logging_setup import logger

__all__ = ["main"]


def main(args: Sequence[str] | None = None) -> int | None:
    """Argument parser for the CLI."""
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=__version__,
    )
    parsed = parser.parse_args(args)
    logger.info("python_copier_template_example_invoked", args=parsed)
    return None


if __name__ == "__main__":
    raise SystemExit(main())
