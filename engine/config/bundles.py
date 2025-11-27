from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from engine.config.registry_loader import RegistryConfig, load_registry_config
from engine.serializer import canon
from tools.config.artifacts import (
    ARTIFACTS_ROOT,
    BAND_EDGES_PATH,
    MAGIC10_CONFIG_PATH,
    build_band_edges,
    build_magic10_config,
    require_closed_rails,
)


ROOT = Path(__file__).resolve().parents[2]
CONFIG_BUNDLE_ROOT = ARTIFACTS_ROOT / "config_bundles"
REGISTRY_REPORT_PATH = ARTIFACTS_ROOT / "registry" / "registry_report.json"


@dataclass(frozen=True)
class SourceDigest:
    path: str
    sha256: str
    size_bytes: int


def _source_digest(path: Path, *, base: Path) -> SourceDigest:
    rel_path = path.relative_to(base)
    data = path.read_bytes()
    return SourceDigest(path=rel_path.as_posix(), sha256=hashlib.sha256(data).hexdigest(), size_bytes=len(data))


def _sorted_channels(config: RegistryConfig) -> list[dict[str, object]]:
    channels = []
    for channel in sorted(config.channels.values(), key=lambda item: item.id):
        channels.append(
            {
                "id": channel.id,
                "gates": list(channel.gates),
                "centers": list(channel.centers),
                "circuit_primary": channel.circuit_primary,
                "substream": channel.substream,
                "primary_domain": channel.primary_domain,
                "domains": list(channel.domains),
                "flags": list(channel.flags),
            }
        )
    return channels


def _magic10_payload(config: RegistryConfig) -> Mapping[str, object]:
    magic10 = build_magic10_config(config)
    # Normalize seed ordering for determinism
    seeds = magic10.get("seeds", {})
    magic10["seeds"] = {key: seeds[key] for key in sorted(seeds)}
    return magic10


def _band_payload(root: Path | None) -> Mapping[str, object]:
    return build_band_edges(root)


def _source_block(base: Path) -> Mapping[str, object]:
    paths = {
        "magic10_config": base / MAGIC10_CONFIG_PATH.relative_to(ROOT),
        "band_edges": base / BAND_EDGES_PATH.relative_to(ROOT),
        "registry_report": base / REGISTRY_REPORT_PATH.relative_to(ROOT),
    }
    return {key: _source_digest(path, base=base).__dict__ for key, path in paths.items()}


def build_backend_bundle(
    root: Path | None = None,
    *,
    allow_aliases: bool = False,
    alias_ledger: Mapping[str, str] | None = None,
) -> Mapping[str, object]:
    base = root or ROOT
    config = load_registry_config(base, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    magic10 = _magic10_payload(config)
    band_edges = _band_payload(base)
    sources = _source_block(base)

    alias_map = {key: value for key, value in sorted(config.alias_map.items())}
    return {
        "schema": "config_bundle.be.v1",
        "magic10": magic10,
        "bands": band_edges,
        "channels": _sorted_channels(config),
        "centers": list(config.centers),
        "domains": list(config.domains),
        "alias_policy": {"mode": "allow_list" if alias_map else "off", "aliases": alias_map},
        "sources": sources,
    }


def build_frontend_bundle(
    root: Path | None = None,
    *,
    allow_aliases: bool = False,
    alias_ledger: Mapping[str, str] | None = None,
) -> Mapping[str, object]:
    base = root or ROOT
    config = load_registry_config(base, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    magic10 = _magic10_payload(config)
    band_edges = _band_payload(base)
    sources = _source_block(base)
    alias_map = {key: value for key, value in sorted(config.alias_map.items())}

    return {
        "schema": "config_bundle.fe.v1",
        "magic10": {
            "order": magic10["order"],
            "caps": magic10["caps"],
        },
        "bands": {key: band_edges[key] for key in ("bands", "edges", "clamp", "rounding", "version") if key in band_edges},
        "channels": {
            "ids": sorted(config.channels.keys()),
            "alias_policy": {"mode": "allow_list" if alias_map else "off", "aliases": alias_map},
            "domains": list(config.domains),
            "centers": list(config.centers),
        },
        "sources": sources,
    }


def _write_bundle(path: Path, payload: Mapping[str, object]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canon.sercanon(payload, sort_keys=True))
    return path


def generate_bundles(
    root: Path | None = None,
    *,
    allow_aliases: bool = False,
    alias_ledger: Mapping[str, str] | None = None,
) -> Mapping[str, Path]:
    require_closed_rails()
    base = root or ROOT
    be_payload = build_backend_bundle(base, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    fe_payload = build_frontend_bundle(base, allow_aliases=allow_aliases, alias_ledger=alias_ledger)

    be_path = _write_bundle(base / CONFIG_BUNDLE_ROOT.relative_to(ROOT) / "be_bundle.json", be_payload)
    fe_path = _write_bundle(base / CONFIG_BUNDLE_ROOT.relative_to(ROOT) / "fe_bundle.json", fe_payload)
    return {"be_bundle": be_path, "fe_bundle": fe_path}
