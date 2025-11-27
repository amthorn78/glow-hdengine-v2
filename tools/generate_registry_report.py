#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Mapping

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.config.registry_loader import (  # noqa: E402
    AliasPolicyError,
    DuplicateIdError,
    RegistryConfig,
    RegistryConfigError,
    SchemaValidationError,
    UnknownIdError,
    load_registry_config,
)
from engine.serializer import canon  # noqa: E402
from tools.config.artifacts import require_closed_rails  # noqa: E402


# Discovery note (PR3 / EPIC017): legacy registry_report lived at artifacts/reports/ with
# only category ranks. This generator emits the PF14-shaped registry_report at
# artifacts/registry/registry_report.json using the hardened loader, preserving canonical
# JSON rules and two-run identity. No HTTP or CLI surfaces change here.


REPORT_PATH = ROOT / "artifacts" / "registry" / "registry_report.json"


def _stable_generated_at(report_path: Path) -> str:
    env_epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if env_epoch:
        try:
            ts = _dt.datetime.fromtimestamp(int(env_epoch), tz=_dt.timezone.utc)
            return ts.replace(microsecond=0).isoformat().replace("+00:00", "Z")
        except ValueError:
            pass
    if report_path.exists():
        try:
            existing = json.loads(report_path.read_text(encoding="utf-8"))
            ts = existing.get("generated_at_utc")
            if isinstance(ts, str) and ts:
                return ts
        except Exception:
            pass
    return "1970-01-01T00:00:00Z"


def _sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _catalog_meta(path: Path, *, count: int) -> Mapping[str, object]:
    return {
        "path": str(path.relative_to(ROOT)),
        "count": count,
        "sha256": _sha256_path(path),
    }


def _build_registry_inputs(config: RegistryConfig) -> Mapping[str, object]:
    catalog_root = ROOT / "catalog"
    channels_path = catalog_root / "channels_v1.json"
    gates_path = catalog_root / "gates_v1.json"
    order_path = catalog_root / "magic10.json"
    caps_path = catalog_root / "magic10_caps.json"
    seeds_path = catalog_root / "magic10_seeds.json"
    manifest_path = catalog_root / "manifest.json"
    manifest_entries = [
        {"path": entry.path, "sha256": entry.sha256, "size_bytes": entry.size}
        for entry in config.manifest_entries
    ]
    return {
        "catalogs": {
            "channels_v1": _catalog_meta(channels_path, count=len(config.channels)),
            "gates_v1": _catalog_meta(gates_path, count=len(config.gates)),
            "magic10_order": {
                "path": str(order_path.relative_to(ROOT)),
                "sha256": _sha256_path(order_path),
                "order": list(config.magic10_order),
            },
            "magic10_caps": {
                "path": str(caps_path.relative_to(ROOT)),
                "sha256": _sha256_path(caps_path),
            },
            "magic10_seeds": {
                "path": str(seeds_path.relative_to(ROOT)),
                "sha256": _sha256_path(seeds_path),
            },
        },
        "manifest": {
            "path": str(manifest_path.relative_to(ROOT)),
            "sha256": _sha256_path(manifest_path),
            "entries": manifest_entries,
            "count": len(manifest_entries),
        },
    }


def _domain_counts(config: RegistryConfig) -> Mapping[str, int]:
    counts: dict[str, int] = {}
    for channel in config.channels.values():
        for domain in channel.domains:
            counts[domain] = counts.get(domain, 0) + 1
    return dict(sorted(counts.items()))


def _magic10_versions(config: RegistryConfig) -> Mapping[str, object]:
    seeds = {
        key: {
            "seed_version": value.seed_version,
            "updated_at_utc": value.updated_at_utc,
            "checksum_sha256": value.checksum_sha256,
        }
        for key, value in sorted(config.magic10_seeds.items())
    }
    caps = {
        key: {
            "inputs": list(value.inputs),
            "bounds": {"min": value.bounds["min"], "max": value.bounds["max"]},
        }
        for key, value in sorted(config.magic10_caps.items())
    }
    return {
        "order": list(config.magic10_order),
        "seeds": seeds,
        "caps": caps,
    }


def build_registry_report(root: Path | None = None, *, allow_aliases: bool = False, alias_ledger: Mapping[str, str] | None = None) -> Mapping[str, object]:
    base = root or ROOT
    config = load_registry_config(base, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    generated_at = _stable_generated_at(REPORT_PATH)
    return {
        "schema": "registry_report.v1",
        "generated_at_utc": generated_at,
        "inputs": _build_registry_inputs(config),
        "artifacts": {
            "registry": {
                "channel_ids": sorted(config.channels.keys()),
                "gate_centers": {str(k): v.center for k, v in sorted(config.gates.items())},
                "centers": list(config.centers),
                "domains": list(config.domains),
                "domain_counts": _domain_counts(config),
                "magic10": _magic10_versions(config),
                "alias_policy": {
                    "mode": "allow_list" if config.alias_map else "off",
                    "aliases": dict(sorted(config.alias_map.items())),
                },
            }
        },
        "notes": [
            "registry_report is generated programmatically; generated_at_utc is stable unless SOURCE_DATE_EPOCH is set.",
        ],
    }


def write_registry_report(root: Path | None = None, *, allow_aliases: bool = False, alias_ledger: Mapping[str, str] | None = None) -> Path:
    require_closed_rails()
    payload = build_registry_report(root, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    report_path = (root or ROOT) / REPORT_PATH.relative_to(ROOT)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_bytes(canon.sercanon(payload, sort_keys=True))
    return report_path


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate the canonical registry_report")
    parser.add_argument("--allow-aliases", action="store_true", help="enable alias allow-list mode")
    args = parser.parse_args(argv)
    try:
        write_registry_report(ROOT, allow_aliases=args.allow_aliases)
    except (RegistryConfigError, UnknownIdError, DuplicateIdError, SchemaValidationError, AliasPolicyError) as exc:
        raise SystemExit(f"registry_report generation failed: {exc.code}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(_main())

