#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.config.bundles import (  # noqa: E402
    CONFIG_BUNDLE_ROOT,
    build_backend_bundle,
    build_frontend_bundle,
    generate_bundles,
)
from engine.serializer import canon  # noqa: E402
from tools.config.artifacts import require_closed_rails  # noqa: E402


def expected_bundles(root: Path | None = None, *, allow_aliases: bool = False) -> dict[Path, bytes]:
    base = root or ROOT
    bundle_root = base / CONFIG_BUNDLE_ROOT.relative_to(ROOT)
    return {
        bundle_root / "be_bundle.json": canon.sercanon(
            build_backend_bundle(base, allow_aliases=allow_aliases),
            sort_keys=True,
        ),
        bundle_root / "fe_bundle.json": canon.sercanon(
            build_frontend_bundle(base, allow_aliases=allow_aliases),
            sort_keys=True,
        ),
    }


def check_bundles(root: Path | None = None, *, allow_aliases: bool = False) -> None:
    require_closed_rails()
    base = root or ROOT
    expected = expected_bundles(base, allow_aliases=allow_aliases)
    stale = [
        path.relative_to(base).as_posix()
        for path, data in expected.items()
        if not path.is_file() or path.read_bytes() != data
    ]
    if stale:
        raise SystemExit("STALE:" + ",".join(stale))


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
