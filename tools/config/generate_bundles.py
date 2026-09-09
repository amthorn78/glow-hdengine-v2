#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.config.bundles import (  # noqa: E402
    CONFIG_BUNDLE_ROOT,
    _prepare_bundles,
    generate_bundles,
)
from engine.serializer import canon  # noqa: E402
from tools.config.artifacts import require_closed_rails, _destination_state  # noqa: E402
from tools.config.generate_config_artifacts import _check_expected, _verify_checked_outputs  # noqa: E402
from tools.generate_registry_report import _verify_report_source  # noqa: E402


def expected_bundles(root: Path | None = None, *, allow_aliases: bool = False) -> dict[Path, bytes]:
    base = root or ROOT
    capture, payloads = _prepare_bundles(base, allow_aliases=allow_aliases)
    expected = {capture.root / f"artifacts/config_bundles/{name}.json":
            canon.sercanon(payload, sort_keys=True)
            for name, payload in payloads.items()}
    capture.verify_unchanged()
    _verify_report_source(capture)
    return expected


def check_bundles(root: Path | None = None, *, allow_aliases: bool = False) -> None:
    require_closed_rails()
    base = Path(os.path.abspath(root or ROOT))
    capture, payloads = _prepare_bundles(base, allow_aliases=allow_aliases)
    expected = {base / f"artifacts/config_bundles/{name}.json":
                canon.sercanon(payload, sort_keys=True)
                for name, payload in payloads.items()}
    before = _check_expected(base, expected)
    _verify_checked_outputs(base, before, capture)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate governed FE/BE config bundles under closed rails")
    parser.add_argument("--allow-aliases", action="store_true", help="Enable channel alias allow-list mode")
    parser.add_argument("--check", action="store_true", help="Validate committed bytes without writing")
    args = parser.parse_args(argv)

    if args.check:
        check_bundles(ROOT, allow_aliases=args.allow_aliases)
    else:
        generate_bundles(ROOT, allow_aliases=args.allow_aliases)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
