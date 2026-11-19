import contextlib
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
    """Build a labeled, non-production 45-member admission fixture."""
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


# ---------------------------------------------------------------------------
# HDE-EPIC043 WU-PR-09: the test-only v2 candidate roster route.
#
# The switch admits the v2 bundle through the v2 loader's rules, but the release
# roster constant keeps its v1 value until the cut (WU-PR-10).  A temporary
# candidate root therefore admits only while a test swaps
# ``registry_loader.ADMITTED_RELEASE_ROSTER`` for the candidate roster below.
# The version and timestamp constants are not touched, no rule is relaxed, and
# no production path reaches this module (tests/m10_v2/test_switch.py proves it).
# The two labelled fixtures are non-canon; nothing here is the cutover release.
# ---------------------------------------------------------------------------

# The Magic10 v2 modules the switched core executes, beyond the v2 loader.
V2_CANDIDATE_EXECUTING_MODULES = (
    "engine/magic10_v2/calculation.py",
    "engine/magic10_v2/kernel.py",
    "engine/magic10_v2/signals.py",
)
_V1_CONFIGURATION_PATH = "catalog/magic10_mechanics_v1.json"
_V2_CANDIDATE_FIXTURES = {
    "catalog/magic10_mechanics_v2.json": "tests/fixtures/magic10_v2/magic10_mechanics_v2.fixture.json",
    "math/thresholds.json": "tests/fixtures/magic10_v2/thresholds_v2.fixture.json",
}


def v2_candidate_roster() -> tuple[str, ...]:
    """The 45-path roster without the v1 configuration, plus the v2 members (57 paths)."""
    from engine.config.magic10_v2_loader import MAGIC10_V2_DECLARED_MEMBERS
    from engine.config.registry_loader import ADMITTED_RELEASE_ROSTER

    paths = set(ADMITTED_RELEASE_ROSTER) - {_V1_CONFIGURATION_PATH}
    paths |= set(MAGIC10_V2_DECLARED_MEMBERS) | set(V2_CANDIDATE_EXECUTING_MODULES)
    return tuple(sorted(paths))


@contextlib.contextmanager
def v2_candidate_roster_admission():
    """Swap only the admission roster constant for the v2 candidate roster, then restore it."""
    from engine.config import registry_loader

    original = registry_loader.ADMITTED_RELEASE_ROSTER
    registry_loader.ADMITTED_RELEASE_ROSTER = v2_candidate_roster()
    try:
        yield registry_loader.ADMITTED_RELEASE_ROSTER
    finally:
        registry_loader.ADMITTED_RELEASE_ROSTER = original


def write_release_manifest(root: Path, roster: tuple[str, ...]) -> Path:
    """Write a canonical manifest over ``roster``'s current bytes with the adopted version and timestamp."""
    from engine.config.registry_loader import ADMITTED_RELEASE_BUILT_AT_UTC, ADMITTED_RELEASE_VERSION

    entries = []
    for relative_path in roster:
        raw = (root / relative_path).read_bytes()
        entries.append({"path": relative_path, "sha256": hashlib.sha256(raw).hexdigest(), "size": len(raw)})
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


def synthetic_v2_candidate_root(tmp_path: Path, *, source_root: Path | None = None) -> Path:
    """Build a labelled, non-production 57-member v2 candidate admission fixture."""
    source = (source_root or Path(__file__).resolve().parents[2]).resolve()
    root = (tmp_path / "synthetic-v2-candidate-only").resolve()
    assert root != source
    root.mkdir(parents=True, exist_ok=False)
    roster = v2_candidate_roster()
    for relative_path in roster:
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        if relative_path in _V2_CANDIDATE_FIXTURES:
            target.write_bytes((source / _V2_CANDIDATE_FIXTURES[relative_path]).read_bytes())
            continue
        raw = (source / relative_path).read_bytes()
        if relative_path in _SYNTHETIC_FUTURE_CANONICAL_JSON:
            raw = canon.sercanon(json.loads(raw), sort_keys=True)
        elif relative_path in _SYNTHETIC_FUTURE_SINGLE_LF_TEXT:
            raw = raw.rstrip(b"\r\n") + b"\n"
        target.write_bytes(raw)
    manifest = json.loads(write_release_manifest(root, roster).read_bytes())
    assert tuple(row["path"] for row in manifest["files"]) == roster
    return root


def admit_synthetic_v2_candidate(tmp_path: Path, *, source_root: Path | None = None):
    """Admit a fresh v2 candidate root through the unchanged admission path and the roster route."""
    from engine.config.registry_loader import _load_active_mechanics_bundle_from_root

    root = synthetic_v2_candidate_root(tmp_path, source_root=source_root)
    with v2_candidate_roster_admission():
        return _load_active_mechanics_bundle_from_root(root)
