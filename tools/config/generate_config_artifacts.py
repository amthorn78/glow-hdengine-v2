#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Mapping

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.config.registry_loader import load_registry_config  # noqa: E402
from engine.serializer import canon  # noqa: E402
from tools.config.artifacts import (  # noqa: E402
    BAND_EDGES_PATH,
    MAGIC10_CONFIG_PATH,
    build_band_edges,
    build_magic10_config,
    require_closed_rails,
    write_band_edges,
    write_magic10_config,
)
from tools.generate_registry_report import (  # noqa: E402
    REPORT_PATH,
    build_registry_report,
    write_registry_report,
)


def expected_config_artifacts(
    root: Path | None = None,
    *,
    allow_aliases: bool = False,
    alias_ledger: Mapping[str, str] | None = None,
) -> dict[Path, bytes]:
    base = root or ROOT
    config = load_registry_config(
        base,
        allow_aliases=allow_aliases,
        alias_ledger=alias_ledger,
    )
    return {
        base / REPORT_PATH.relative_to(ROOT): canon.sercanon(
            build_registry_report(
                base,
                allow_aliases=allow_aliases,
                alias_ledger=alias_ledger,
            ),
            sort_keys=True,
        ),
        base / MAGIC10_CONFIG_PATH.relative_to(ROOT): canon.sercanon(
            build_magic10_config(config),
            sort_keys=True,
        ),
        base / BAND_EDGES_PATH.relative_to(ROOT): canon.sercanon(
            build_band_edges(base),
            sort_keys=True,
        ),
    }


def check_config_artifacts(
    root: Path | None = None,
    *,
    allow_aliases: bool = False,
    alias_ledger: Mapping[str, str] | None = None,
) -> None:
    require_closed_rails()
    base = root or ROOT
    expected = expected_config_artifacts(
        base,
        allow_aliases=allow_aliases,
        alias_ledger=alias_ledger,
    )
    stale = [
        path.relative_to(base).as_posix()
        for path, data in expected.items()
        if not path.is_file() or path.read_bytes() != data
    ]
    if stale:
        raise SystemExit("STALE:" + ",".join(stale))


def generate_config_artifacts(
    root: Path | None = None,
    *,
    allow_aliases: bool = False,
    alias_ledger: Mapping[str, str] | None = None,
) -> dict[str, Path]:
    require_closed_rails()
    base = root or ROOT
    config = load_registry_config(base, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    registry_report = write_registry_report(base, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    magic10_config = write_magic10_config(config, base)
    band_edges = write_band_edges(base)
    return {
        "registry_report": registry_report,
        "magic10_config": magic10_config,
        "band_edges": band_edges,
    }


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate governed config artifacts under closed rails")
    parser.add_argument("--allow-aliases", action="store_true", help="Enable channel alias allow-list mode")
    parser.add_argument("--check", action="store_true", help="Validate committed bytes without writing")
    args = parser.parse_args(argv)
    if args.check:
        check_config_artifacts(ROOT, allow_aliases=args.allow_aliases)
    else:
        generate_config_artifacts(ROOT, allow_aliases=args.allow_aliases)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(_main())
