#!/usr/bin/env python3
"""Retired compatibility guard for the former broad evidence generator."""
from __future__ import annotations

import sys

DIAGNOSTIC = "RETIRED_EVIDENCE_GENERATOR: use focused generators"


def main() -> int:
    sys.stderr.write(DIAGNOSTIC + "\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
