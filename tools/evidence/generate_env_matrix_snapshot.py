#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.serializer import canon

OUT = ROOT / "artifacts/runtime/env_matrix.snapshot.json"

DEFAULT_RAILS = {
    "CI": {"ALLOW_NETWORK": "0", "SAFE_MODE": "1"},
    "dev": {"ALLOW_NETWORK": "0", "SAFE_MODE": "1"},
    "prod": {"ALLOW_NETWORK": "1", "SAFE_MODE": "0"},
    "stage": {"ALLOW_NETWORK": "0", "SAFE_MODE": "1"},
}
DETERMINISM_PINS = {"LANG": "C", "LC_ALL": "C", "TZ": "UTC"}

# This is a governed default-presence fixture, not a probe of operator secrets.
PRESENCE = {
    "DATABASE_URL": False,
    "DB_BRIDGE_URL": False,
    "db_allow_bridge_in_prod": False,
}
GENERATION_ENV = {
    **DEFAULT_RAILS["CI"],
    **DETERMINISM_PINS,
}


def require_closed_rails() -> None:
    bad = [key for key, value in GENERATION_ENV.items() if os.environ.get(key) != value]
    if bad:
        raise SystemExit("DETERMINISM_ENV:" + ",".join(bad))


def _payload() -> dict[str, object]:
    return {
        "schema_version": 3,
        "default_rails": DEFAULT_RAILS,
        "determinism_pins": DETERMINISM_PINS,
        "presence": PRESENCE,
        "notes": [],
    }


def _expected() -> bytes:
    require_closed_rails()
    return canon.sercanon(_payload(), sort_keys=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    expected = _expected()

    if args.check:
        if not OUT.exists() or OUT.read_bytes() != expected:
            raise SystemExit("DRIFT:" + OUT.as_posix())
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(expected)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
