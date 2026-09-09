#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as _dt
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
    _capture_registry_config,
)
from engine.serializer import canon  # noqa: E402
from tools.config.artifacts import require_closed_rails, _destination_state, _publish_prepared  # noqa: E402


# Discovery note (PR3 / EPIC017): legacy registry_report lived at artifacts/reports/ with
# only category ranks. This generator emits the PF14-shaped registry_report at
# artifacts/registry/registry_report.json using the hardened loader, preserving canonical
# JSON rules and two-run identity. No HTTP or CLI surfaces change here.


REPORT_PATH = ROOT / "artifacts" / "registry" / "registry_report.json"


def _stable_generated_at(report_path: Path, *, prior_state=None) -> str:
    if prior_state is None:
        prior_state = _destination_state(report_path.parents[2], [report_path])
    env_epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if env_epoch:
        try:
            ts = _dt.datetime.fromtimestamp(int(env_epoch), tz=_dt.timezone.utc)
            return ts.replace(microsecond=0).isoformat().replace("+00:00", "Z")
        except (ValueError, OverflowError, OSError):
            pass
    prior = prior_state[report_path]
    if prior is not None:
        try:
            existing = json.loads(prior[0].decode("utf-8"))
            ts = existing.get("generated_at_utc")
            if isinstance(ts, str) and ts:
                return ts
        except Exception:
            pass
    return "1970-01-01T00:00:00Z"


def _verify_report_source(capture) -> None:
    """Recheck the optional prior-report input, including its absence.

    This input supplies only stable timestamp precedence. It is deliberately
    separate from catalog validation so malformed historical report bytes keep
    their existing fixed-epoch fallback and an owner may replace its own output.
    """
    before = getattr(capture, "_registry_report_before", None)
    if before is not None and _destination_state(capture.root, before) != before:
        raise RuntimeError("REGISTRY_REPORT_SOURCE_CHANGED")


def _catalog_meta(source, *, count: int | None = None) -> Mapping[str, object]:
    result = {"path": source.relative_path, "sha256": source.sha256}
    if count is not None:
        result["count"] = count
    return result


def _build_registry_inputs(config: RegistryConfig, *, capture=None) -> Mapping[str, object]:
    capture = capture or _capture_registry_config(ROOT)
    rows = {
        "channels_v1": dict(_catalog_meta(capture.sources["catalog/channels_v1.json"], count=len(config.channels))),
        "gates_v1": dict(_catalog_meta(capture.sources["catalog/gates_v1.json"], count=len(config.gates))),
        "magic10_order": dict(_catalog_meta(capture.sources["catalog/magic10.json"])),
        "magic10_caps": dict(_catalog_meta(capture.sources["catalog/magic10_caps.json"])),
        "magic10_seeds": dict(_catalog_meta(capture.sources["catalog/magic10_seeds.json"])),
    }
    rows["magic10_order"]["order"] = list(config.magic10_order)
    return {"catalogs": rows}


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


def _build_registry_report(capture) -> Mapping[str, object]:
    config = capture.config
    report_path = capture.root / "artifacts/registry/registry_report.json"
    if not hasattr(capture, "_registry_report_before"):
        capture._registry_report_before = _destination_state(capture.root, [report_path])
    generated_at = _stable_generated_at(report_path, prior_state=capture._registry_report_before)
    return {
        "schema": "registry_report.v1",
        "generated_at_utc": generated_at,
        "inputs": _build_registry_inputs(config, capture=capture),
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


def build_registry_report(root: Path | None = None, *, allow_aliases: bool = False, alias_ledger: Mapping[str, str] | None = None) -> Mapping[str, object]:
    capture = _capture_registry_config(root or ROOT, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    payload = _build_registry_report(capture)
    capture.verify_unchanged()
    _verify_report_source(capture)
    return payload


def write_registry_report(root: Path | None = None, *, allow_aliases: bool = False, alias_ledger: Mapping[str, str] | None = None) -> Path:
    require_closed_rails()
    base = Path(os.path.abspath(root or ROOT))
    target = base / "artifacts/registry/registry_report.json"
    before = _destination_state(base, [target])
    capture = _capture_registry_config(base, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    payload = canon.sercanon(_build_registry_report(capture), sort_keys=True)
    _publish_prepared(base, {target: payload}, before=before, verify=capture.verify_unchanged)
    return target


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
