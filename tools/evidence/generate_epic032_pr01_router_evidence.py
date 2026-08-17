#!/usr/bin/env python3
"""Verify the frozen HDE-EPIC032 PR-01 narrative-router captures.

These artifacts record the retired narrative-router contract at EPIC032 capture
time. They are deliberately not regenerated from the current runtime because
the PF17 direction-native router no longer has the historical normalized
A-to-B/B-to-A behavior.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env

FROZEN_OUTPUTS: dict[str, tuple[str, int]] = {
    "artifacts/narratives/router/cli_http_parity.log": (
        "3faba2329fd9c30bf0e01bbb22df9b67746add90c9cc61e2533c962f70bee846",
        33285,
    ),
    "artifacts/narratives/router/parity_abba.log": (
        "283578d9ed224d8d8ed8cfb13bf8980e7427c6f975bad5caa70d36277410807b",
        27411,
    ),
    "audit/gates/narratives/keys_10x4.table.json": (
        "f7f5672a1cfc1b9feb1e94295805e85cb2b5bdf403b8e00f16197c202380eb6e",
        4746,
    ),
}


def _verify_frozen_outputs(root: Path = ROOT) -> None:
    drift: list[str] = []
    for name, (expected_sha256, expected_size) in FROZEN_OUTPUTS.items():
        path = root / name
        if not path.is_file() or path.is_symlink():
            drift.append(name)
            continue
        body = path.read_bytes()
        if (
            len(body) != expected_size
            or hashlib.sha256(body).hexdigest() != expected_sha256
        ):
            drift.append(name)
    if drift:
        raise SystemExit("FROZEN_EPIC032_ROUTER_DRIFT:" + ",".join(drift))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    if not args.check:
        raise SystemExit("HISTORICAL_EPIC032_ROUTER_WRITE_REFUSED")
    ensure_determinism_env()
    _verify_frozen_outputs()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
