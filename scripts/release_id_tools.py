#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import release_id_recompute  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate freeze-pack manifest evidence and release_id")
    parser.add_argument("--manifest", default="catalog/manifest.json", help="Path to the source-of-truth manifest")
    parser.add_argument("--out", default="artifacts/math", help="Output directory for freeze-pack artifacts")
    args = parser.parse_args(argv)

    manifest_path = Path(args.manifest)
    out_dir = Path(args.out)
    freeze_path = out_dir / "freeze_pack_manifest.json"
    release_id_path = out_dir / "release_id.txt"
    schema_report_path = out_dir / "manifest_schema_report.json"
    snapshot_path = out_dir / "manifest_snapshot.json"
    checksums_path = out_dir / "checksums_audit.log"
    log_path = out_dir / "release_id_recompute.log"
    env_pins_path = ROOT / "artifacts" / "proofs" / "env_pins.txt"

    return release_id_recompute.recompute(
        manifest_path=manifest_path,
        freeze_path=freeze_path,
        release_id_path=release_id_path,
        manifest_snapshot_path=snapshot_path,
        checksums_path=checksums_path,
        env_pins_path=env_pins_path,
        log_path=log_path,
        schema_report_path=schema_report_path,
        check=False,
    )


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
