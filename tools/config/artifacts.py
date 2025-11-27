from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Mapping

from engine.config.registry_loader import RegistryConfig
from engine.serializer import canon

ROOT = Path(__file__).resolve().parents[2]
BAND_SOURCE = ROOT / "math" / "thresholds.json"
ARTIFACTS_ROOT = ROOT / "artifacts"
THRESHOLDS_ROOT = ARTIFACTS_ROOT / "thresholds"
MAGIC10_CONFIG_PATH = THRESHOLDS_ROOT / "magic10_config.json"
BAND_EDGES_PATH = THRESHOLDS_ROOT / "band_edges.json"

_REQUIRED_RAILS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
}


def require_closed_rails(env: Mapping[str, str] | None = None) -> None:
    env_map = dict(os.environ if env is None else env)
    missing = {key: value for key, value in _REQUIRED_RAILS.items() if env_map.get(key) != value}
    if missing:
        raise SystemExit(f"RAILS_CLOSED_REQUIRED:{sorted(missing.items())}")


def build_magic10_config(config: RegistryConfig) -> Mapping[str, object]:
    caps = {
        key: {
            "inputs": list(value.inputs),
            "bounds": {"min": value.bounds["min"], "max": value.bounds["max"]},
        }
        for key, value in sorted(config.magic10_caps.items())
    }
    seeds = {
        key: {
            "template_id": value.template_id,
            "seed_version": value.seed_version,
            "updated_at_utc": value.updated_at_utc,
            "checksum_sha256": value.checksum_sha256,
        }
        for key, value in sorted(config.magic10_seeds.items())
    }
    return {
        "schema": "magic10_config.v1",
        "order": list(config.magic10_order),
        "caps": caps,
        "seeds": seeds,
    }


def build_band_edges(root: Path | None = None) -> Mapping[str, object]:
    base = root or ROOT
    raw = json.loads(BAND_SOURCE.read_text(encoding="utf-8"))
    edges = [int(edge) for edge in raw.get("edges", [])]
    clamp = [int(value) for value in raw.get("clamp", [])]
    rounding = str(raw.get("rounding", "ROUND_HALF_UP"))
    version = str(raw.get("version", ""))

    return {
        "schema": "band_edges.v1",
        "source": str(BAND_SOURCE.relative_to(base)),
        "bands": ["Cool", "Open", "Warm", "Glow"],
        "edges": edges,
        "clamp": clamp,
        "rounding": rounding,
        "version": version,
    }


def write_magic10_config(config: RegistryConfig, root: Path | None = None) -> Path:
    payload = build_magic10_config(config)
    root_path = root or ROOT
    target = root_path / MAGIC10_CONFIG_PATH.relative_to(ROOT)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(canon.sercanon(payload, sort_keys=True))
    return target


def write_band_edges(root: Path | None = None) -> Path:
    payload = build_band_edges(root)
    root_path = root or ROOT
    target = root_path / BAND_EDGES_PATH.relative_to(ROOT)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(canon.sercanon(payload, sort_keys=True))
    return target
