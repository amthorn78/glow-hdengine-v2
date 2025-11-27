#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.config.bundles import generate_bundles  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate governed FE/BE config bundles under closed rails")
    parser.add_argument("--allow-aliases", action="store_true", help="Enable channel alias allow-list mode")
    args = parser.parse_args(argv)

    generate_bundles(ROOT, allow_aliases=args.allow_aliases)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
