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
from tools.config.artifacts import (  # noqa: E402
    require_closed_rails,
    write_band_edges,
    write_magic10_config,
)
from tools.generate_registry_report import write_registry_report  # noqa: E402


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
    args = parser.parse_args(argv)
    generate_config_artifacts(ROOT, allow_aliases=args.allow_aliases)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(_main())
