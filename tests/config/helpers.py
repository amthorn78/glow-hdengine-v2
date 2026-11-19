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
        # HDE-EPIC043 WU-PR-10: the v2 release's configuration, its sources and
        # their owning schemas, and the v2 result schemas.  The version-2
        # thresholds at math/thresholds.json validate only against
        # schemas/thresholds_v2.schema.json.  The v1 inputs above stay in the
        # tree outside the roster, and v1-contrast tests still read them.
        "catalog/magic10_mechanics_v2.json", "catalog/centers_v1.json", "catalog/type_pairing_v1.json",
        "schemas/magic10_mechanics_v2.schema.json", "schemas/thresholds_v2.schema.json",
        "schemas/centers_v1.schema.json", "schemas/type_pairing_v1.schema.json",
        "schemas/magic10_result_v2.schema.json", "schemas/magic10_compat_result_v2.schema.json",
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
    """Build a labeled, non-production admission fixture of the admitted roster's member bytes."""
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
# HDE-EPIC043 WU-PR-09 introduced a test-only v2 candidate roster route: until the
# cut, a temporary candidate root admitted only while a test swapped
# ``registry_loader.ADMITTED_RELEASE_ROSTER`` for the candidate roster.
#
# HDE-EPIC043 WU-PR-10 (the cut) made that roster the admitted one, so:
# * ``v2_candidate_roster()`` returns ``ADMITTED_RELEASE_ROSTER`` itself;
# * ``v2_candidate_roster_admission()`` swaps nothing and yields that constant.
#   Both keep their names for their existing callers.
# * ``release_roster_route(roster)`` is the one remaining swap.  It is for
#   negative controls that need a roster other than the admitted one, such as
#   a roster without an executing source (``UNBOUND_SOURCE``).
# The version and timestamp constants are never touched, no rule is relaxed, and
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
# The labelled fixtures stand in for the two governed files by default.  HDE-EPIC043
# WU-PR-10: the goldens' positive runs pass ``fixture_maxima=False`` and copy the
# governed cut bytes of both files instead, so they run at the cut's maxima.
_V2_CANDIDATE_FIXTURES = {
    "catalog/magic10_mechanics_v2.json": "tests/fixtures/magic10_v2/magic10_mechanics_v2.fixture.json",
    "math/thresholds.json": "tests/fixtures/magic10_v2/thresholds_v2.fixture.json",
}


def v2_candidate_roster() -> tuple[str, ...]:
    """The admitted v2 release roster: ``ADMITTED_RELEASE_ROSTER``, read when called."""
    from engine.config import registry_loader

    return registry_loader.ADMITTED_RELEASE_ROSTER


@contextlib.contextmanager
def v2_candidate_roster_admission():
    """Yield the admitted roster; since the cut the candidate roster needs no swap."""
    from engine.config import registry_loader

    yield registry_loader.ADMITTED_RELEASE_ROSTER


@contextlib.contextmanager
def release_roster_route(roster: tuple[str, ...]):
    """Swap only the admission roster constant for ``roster``, then restore it (test-only)."""
    from engine.config import registry_loader

    original = registry_loader.ADMITTED_RELEASE_ROSTER
    registry_loader.ADMITTED_RELEASE_ROSTER = tuple(roster)
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


def synthetic_v2_candidate_root(
    tmp_path: Path, *, source_root: Path | None = None, fixture_maxima: bool = True,
) -> Path:
    """Build a labelled, non-production v2 candidate admission fixture over the admitted roster.

    ``fixture_maxima=False`` copies the governed configuration and thresholds bytes.
    """
    source = (source_root or Path(__file__).resolve().parents[2]).resolve()
    root = (tmp_path / "synthetic-v2-candidate-only").resolve()
    assert root != source
    root.mkdir(parents=True, exist_ok=False)
    roster = v2_candidate_roster()
    for relative_path in roster:
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        if fixture_maxima and relative_path in _V2_CANDIDATE_FIXTURES:
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
    """Admit a fresh v2 candidate root through the unchanged admission path and the admitted roster."""
    from engine.config.registry_loader import _load_active_mechanics_bundle_from_root

    root = synthetic_v2_candidate_root(tmp_path, source_root=source_root)
    with v2_candidate_roster_admission():
        return _load_active_mechanics_bundle_from_root(root)
