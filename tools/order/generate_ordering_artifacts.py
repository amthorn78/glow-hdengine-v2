#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from engine.order import artifacts as order_artifacts


ARTIFACT_DIR = ROOT / "artifacts" / "engine" / "order"


def _write_if_changed(path: Path, payload: bytes, *, check: bool) -> None:
    if path.exists() and path.read_bytes() == payload:
        return
    if check:
        raise SystemExit(f"STALE:{path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate ordering artifacts")
    parser.add_argument("--check", action="store_true", help="Fail if artifacts would change")
    args = parser.parse_args(argv)

    ctx = order_artifacts.load_ordering_context(ROOT)

    channels = order_artifacts.channels_sorted(ctx)
    categories = order_artifacts.categories_sorted(ctx)
    props_lines = order_artifacts.props_total_order_lines(ctx)
    abba_digest = order_artifacts.abba_identity_digest(ctx)

    _write_if_changed(
        ARTIFACT_DIR / "channels_sorted.snapshot.json",
        order_artifacts.render_json_snapshot(channels),
        check=args.check,
    )
    _write_if_changed(
        ARTIFACT_DIR / "categories_iter.snapshot.json",
        order_artifacts.render_json_snapshot(categories),
        check=args.check,
    )
    _write_if_changed(
        ARTIFACT_DIR / "props_total_order.log",
        order_artifacts.render_props_log(props_lines),
        check=args.check,
    )
    _write_if_changed(
        ARTIFACT_DIR / "abba_identity.bytes",
        abba_digest,
        check=args.check,
    )


if __name__ == "__main__":
    main()
