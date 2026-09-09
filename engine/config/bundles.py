from __future__ import annotations

import os
from pathlib import Path
from typing import Mapping

from engine.config.registry_loader import (RegistryConfig, _capture_registry_config, _validate_local_schema)
from engine.serializer import canon
from tools.config.artifacts import (
    ARTIFACTS_ROOT,
    BAND_EDGES_PATH,
    MAGIC10_CONFIG_PATH,
    build_band_edges,
    build_magic10_config,
    require_closed_rails,
    _destination_state,
    _publish_prepared,
)


ROOT = Path(__file__).resolve().parents[2]
CONFIG_BUNDLE_ROOT = ARTIFACTS_ROOT / "config_bundles"
REGISTRY_REPORT_PATH = ARTIFACTS_ROOT / "registry" / "registry_report.json"


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


def _prepare_bundles(base: Path, *, allow_aliases: bool = False,
                     alias_ledger: Mapping[str, str] | None = None):
    """Capture current primaries once; refuse stale sources before deriving either bundle."""
    from tools.config.generate_config_artifacts import _expected_config_artifacts

    capture = _capture_registry_config(base, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    expected = _expected_config_artifacts(capture)
    primaries = {}
    source_block = {}
    names = {
        "registry_report": "artifacts/registry/registry_report.json",
        "magic10_config": "artifacts/thresholds/magic10_config.json",
        "band_edges": "artifacts/thresholds/band_edges.json",
    }
    for key, relative in names.items():
        source = capture.read(relative)
        if source.raw != expected[capture.root / relative]:
            raise RuntimeError(f"STALE_CONFIG_PRIMARY:{relative}")
        primaries[key] = source.data
        source_block[key] = {"path": relative, "sha256": source.sha256,
                             "size_bytes": source.size_bytes}
    config = capture.config
    alias_map = dict(sorted(config.alias_map.items()))
    aliases = {"mode": "allow_list" if alias_map else "off", "aliases": alias_map}
    magic10, bands = primaries["magic10_config"], primaries["band_edges"]
    backend = {
        "schema": "config_bundle.be.v1", "magic10": magic10, "bands": bands,
        "channels": _sorted_channels(config), "centers": list(config.centers),
        "domains": list(config.domains), "alias_policy": aliases,
        "sources": source_block,
    }
    frontend = {
        "schema": "config_bundle.fe.v1",
        "magic10": {key: magic10[key] for key in ("order", "caps")},
        "bands": {key: bands[key] for key in ("bands", "edges", "clamp", "rounding", "version")},
        "channels": {"ids": sorted(config.channels), "alias_policy": aliases,
                     "domains": list(config.domains), "centers": list(config.centers)},
        "sources": source_block,
    }
    _validate_local_schema(capture, "docs/schemas/config_bundle_be.json", backend)
    _validate_local_schema(capture, "docs/schemas/config_bundle_fe.json", frontend)
    capture.verify_unchanged()
    from tools.generate_registry_report import _verify_report_source
    _verify_report_source(capture)
    return capture, {"be_bundle": backend, "fe_bundle": frontend}


def build_backend_bundle(root: Path | None = None, *, allow_aliases: bool = False,
                         alias_ledger: Mapping[str, str] | None = None) -> Mapping[str, object]:
    return _prepare_bundles(root or ROOT, allow_aliases=allow_aliases,
                            alias_ledger=alias_ledger)[1]["be_bundle"]


def build_frontend_bundle(root: Path | None = None, *, allow_aliases: bool = False,
                          alias_ledger: Mapping[str, str] | None = None) -> Mapping[str, object]:
    return _prepare_bundles(root or ROOT, allow_aliases=allow_aliases,
                            alias_ledger=alias_ledger)[1]["fe_bundle"]


def generate_bundles(root: Path | None = None, *, allow_aliases: bool = False,
                     alias_ledger: Mapping[str, str] | None = None) -> Mapping[str, Path]:
    """Prepare and schema-check both outputs before any paired publication."""
    require_closed_rails()
    base = Path(os.path.abspath(root or ROOT))
    targets = {name: base / f"artifacts/config_bundles/{name}.json"
               for name in ("be_bundle", "fe_bundle")}
    before = _destination_state(base, targets.values())
    capture, payloads = _prepare_bundles(base, allow_aliases=allow_aliases,
                                         alias_ledger=alias_ledger)
    _publish_prepared(base, {targets[name]: canon.sercanon(payload, sort_keys=True)
                            for name, payload in payloads.items()},
                      before=before, verify=capture.verify_unchanged)
    return targets
