from __future__ import annotations

import sys

from .main import cli


def main() -> None:
    code = cli()
    if isinstance(code, int):
        sys.exit(code)


if __name__ == "__main__":
    main()
