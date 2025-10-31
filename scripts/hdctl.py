#!/usr/bin/env python3
#!/usr/bin/env python3
"""Fallback launcher for the Glow HD Engine CLI.

Use `hdctl showcompat --pair-file <pair.json> --dump-reader <out.json> --dump-admin-dir <dir>`
to capture QA artifacts. Admin dumps are written with mode 0600 alongside `.sha256` files.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure repo root on sys.path when invoked directly from source tree.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine.cli.main import cli  # noqa: E402


def main() -> int:
    return int(cli() or 0)


if __name__ == "__main__":
    sys.exit(main())
