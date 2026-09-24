import hashlib
import json
import os
import shutil
from pathlib import Path

from engine.serializer import canon


_CLOSED_RAILS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
}


def closed_rails_env() -> dict[str, str]:
    env = os.environ.copy()
    env.update(_CLOSED_RAILS)
    return env


def write_canonical(path: Path, payload: object) -> None:
    """Write one owning test input; malformed-byte tests write bytes explicitly."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canon.sercanon(payload, sort_keys=True))


def catalog_root(tmp_path: Path, *, source_root: Path | None = None) -> Path:
    """Copy complete selected local inputs; generated primaries need their owners."""
    source = source_root or Path(__file__).resolve().parents[2]
    paths = (
        "catalog/channels_v1.json", "catalog/gates_v1.json", "catalog/magic10.json",
        "catalog/magic10_caps.json", "catalog/magic10_seeds.json", "catalog/manifest.json",
        "catalog/magic10_mechanics_v1.json", "math/thresholds.json",
        "schemas/channels_v1.schema.json", "schemas/gates_v1.schema.json",
        "schemas/magic10_mechanics_v1.schema.json", "schemas/magic10_result_v1.schema.json",
        "schemas/magic10_compat_result_v1.schema.json",
        "docs/schemas/config_bundle_be.json", "docs/schemas/config_bundle_fe.json",
    )
    for name in paths:
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / name, target)
    return tmp_path


# HDE-EPIC040-PR05 landed the last future-owner member
# (tools/bodygraph/check_magic10_gate_readiness.py), so the synthetic release
# now copies every roster member's real bytes; no placeholder remains.
_SYNTHETIC_PLACEHOLDERS: dict[str, bytes] = {}

_SYNTHETIC_FUTURE_CANONICAL_JSON = {
    "adapter/schemas/error_v1.schema.json",
    "errors/token_map/token_map.json",
    "schemas/reader.v1.schema.json",
}

_SYNTHETIC_FUTURE_SINGLE_LF_TEXT = {
    "engine/bodygraph/projection.py",
}


def write_synthetic_release_manifest(root: Path) -> Path:
    """Write the isolated fixture's exact manifest from its current member bytes."""
    from engine.config.registry_loader import (
        ADMITTED_RELEASE_BUILT_AT_UTC,
        ADMITTED_RELEASE_ROSTER,
        ADMITTED_RELEASE_VERSION,
    )

    entries = []
    for relative_path in ADMITTED_RELEASE_ROSTER:
        raw = (root / relative_path).read_bytes()
        entries.append(
            {
                "path": relative_path,
                "sha256": hashlib.sha256(raw).hexdigest(),
                "size": len(raw),
            }
        )
    path = root / "catalog/manifest.json"
    write_canonical(
        path,
        {
            "root": "catalog/",
            "version": ADMITTED_RELEASE_VERSION,
            "built_at_utc": ADMITTED_RELEASE_BUILT_AT_UTC,
            "files": entries,
        },
    )
    return path


def synthetic_complete_release_root(
    tmp_path: Path,
    *,
    source_root: Path | None = None,
) -> Path:
    """Build a labeled, non-production 44-member admission fixture."""
    from engine.config.registry_loader import (
        ADMITTED_RELEASE_BUILT_AT_UTC,
        ADMITTED_RELEASE_ROSTER,
        ADMITTED_RELEASE_VERSION,
    )

    source = (source_root or Path(__file__).resolve().parents[2]).resolve()
    root = (tmp_path / "synthetic-complete-release-only").resolve()
    assert root != source
    root.mkdir(parents=True, exist_ok=False)
    for relative_path in ADMITTED_RELEASE_ROSTER:
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        if relative_path in _SYNTHETIC_PLACEHOLDERS:
            target.write_bytes(_SYNTHETIC_PLACEHOLDERS[relative_path])
            continue
        raw = (source / relative_path).read_bytes()
        if relative_path in _SYNTHETIC_FUTURE_CANONICAL_JSON:
            raw = canon.sercanon(json.loads(raw), sort_keys=True)
        elif relative_path in _SYNTHETIC_FUTURE_SINGLE_LF_TEXT:
            raw = raw.rstrip(b"\r\n") + b"\n"
        target.write_bytes(raw)

    manifest_path = write_synthetic_release_manifest(root)
    manifest = json.loads(manifest_path.read_bytes())
    assert "synthetic-complete-release-only" in root.name
    assert manifest["version"] == ADMITTED_RELEASE_VERSION
    assert manifest["built_at_utc"] == ADMITTED_RELEASE_BUILT_AT_UTC
    assert tuple(row["path"] for row in manifest["files"]) == ADMITTED_RELEASE_ROSTER
    return root
