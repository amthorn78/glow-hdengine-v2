from __future__ import annotations

import stat
from contextlib import nullcontext
import os
from pathlib import Path
from typing import Callable, Mapping

from engine.config.registry_loader import RegistryConfig, _capture_registry_config, _validate_thresholds
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


def build_band_edges(root: Path | None = None, *, _capture=None) -> Mapping[str, object]:
    """Build the lower-level projection from exact selected-root thresholds."""
    capture = _capture or _capture_registry_config(root or ROOT)
    raw = capture.read("math/thresholds.json").data
    _validate_thresholds(raw)
    payload = {
        "schema": "band_edges.v1",
        "source": "math/thresholds.json",
        "bands": ["Cool", "Open", "Warm", "Glow"],
        "edges": list(raw["edges"]),
        "clamp": list(raw["clamp"]),
        "rounding": raw["rounding"],
        "version": raw["version"],
    }
    if _capture is None:
        capture.verify_unchanged()
    return payload


def _destination_state(root: Path, paths) -> dict[Path, object]:
    """Check lexical containment and capture exact destination preimages, read-only."""
    root = Path(os.path.abspath(root))
    states = {}
    for path in paths:
        path = Path(os.path.abspath(path))
        if not path.is_relative_to(root) or path == root:
            raise RuntimeError(f"CONFIG_OUTPUT_ESCAPES_ROOT:{path}")
        for parent in (path, *path.parents):
            if parent.is_symlink():
                raise RuntimeError(f"CONFIG_OUTPUT_SYMLINK:{parent}")
            if parent != path and parent.exists() and not parent.is_dir():
                raise RuntimeError(f"CONFIG_OUTPUT_PARENT_NOT_DIRECTORY:{parent}")
        if not path.exists():
            states[path] = None
        else:
            meta = path.lstat()
            if not stat.S_ISREG(meta.st_mode):
                raise RuntimeError(f"CONFIG_OUTPUT_NOT_REGULAR:{path}")
            def identity(info):
                return (info.st_dev, info.st_ino, info.st_mode, info.st_size,
                        info.st_mtime_ns, info.st_ctime_ns)
            descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
            with os.fdopen(descriptor, "rb") as handle:
                opened = os.fstat(handle.fileno())
                raw = handle.read()
                finished = os.fstat(handle.fileno())
            if not (identity(meta) == identity(opened) == identity(finished) == identity(path.lstat())):
                raise RuntimeError(f"CONFIG_DESTINATION_CHANGED_DURING_CAPTURE:{path}")
            states[path] = (raw, *identity(meta))
    return states


def _publish_prepared(root: Path, payloads: Mapping[Path, bytes], *,
                      before: Mapping[Path, object], verify: Callable[[], None]) -> None:
    """Replace a prepared family with caught-failure restoration through its owner.

    This provides no crash-atomic or multi-file visibility guarantee. The outer
    configuration/evidence coordinator may supply the same active transaction.
    """
    from tools.evidence import update_evidence_index as updater

    root = Path(os.path.abspath(root))
    if set(before) != set(payloads):
        raise RuntimeError("CONFIG_DESTINATION_ROSTER_CHANGED")
    verify()
    if _destination_state(root, payloads) != dict(before):
        raise RuntimeError("CONFIG_DESTINATION_CHANGED_DURING_PREPARATION")
    active = updater._ACTIVE_WRITE_TRANSACTION
    if active is not None and active.root != root:
        raise RuntimeError("CONFIG_TRANSACTION_ROOT_MISMATCH")
    if active is not None:
        if not isinstance(active, updater._ConfigWriteTransaction):
            raise RuntimeError("CONFIG_TRANSACTION_OWNER_MISMATCH")
        active.assert_unchanged(payloads)
    context = nullcontext(active) if active is not None else updater._ConfigWriteTransaction(
        root, allowed_paths=set(payloads)
    )
    with context as transaction:
        transaction.prepare(payloads)
        verify()
        if _destination_state(root, payloads) != dict(before):
            raise RuntimeError("CONFIG_DESTINATION_CHANGED_BEFORE_PUBLICATION")
        for path, content in payloads.items():
            verify()
            if _destination_state(root, [path])[path] != before[path]:
                raise RuntimeError(f"CONFIG_DESTINATION_CHANGED_BEFORE_REPLACEMENT:{path}")
            updater._publish_staged({path: content})
        verify()
        for path, expected in payloads.items():
            _destination_state(root, [path])
            if path.read_bytes() != expected:
                raise RuntimeError(f"CONFIG_OUTPUT_CHANGED:{path}")


def write_magic10_config(config: RegistryConfig, root: Path | None = None) -> Path:
    require_closed_rails()
    base = Path(os.path.abspath(root or ROOT))
    target = base / "artifacts/thresholds/magic10_config.json"
    before = _destination_state(base, [target])
    capture = _capture_registry_config(base, allow_aliases=bool(config.alias_map),
                                        alias_ledger=config.alias_map or None)
    if capture.config != config:
        raise RuntimeError("CONFIG_WRITER_SOURCE_MISMATCH")
    payload = canon.sercanon(build_magic10_config(capture.config), sort_keys=True)
    _publish_prepared(base, {target: payload}, before=before, verify=capture.verify_unchanged)
    return target


def write_band_edges(root: Path | None = None) -> Path:
    require_closed_rails()
    base = Path(os.path.abspath(root or ROOT))
    target = base / "artifacts/thresholds/band_edges.json"
    before = _destination_state(base, [target])
    capture = _capture_registry_config(base)
    payload = canon.sercanon(build_band_edges(base, _capture=capture), sort_keys=True)
    _publish_prepared(base, {target: payload}, before=before, verify=capture.verify_unchanged)
    return target
