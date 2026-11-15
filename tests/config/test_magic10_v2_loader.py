"""HDE-EPIC042 WU-PR-03: fail-closed Magic-10 v2 loader and v2 configuration identity.

HDE-SEPA007.3 and HDE-SEPA007.4. Admission of the complete v2 bundle, one adverse
refusal per rule row of the Implementation Audit's R-04 rule set (LR-01 to LR-20),
removal of every required input with no default, the configuration and
source-bundle identity, the ``magic10:v2:`` key, the declared members, and the
import boundary.

Every bundle is assembled in a temporary root from the repository's ``catalog/``,
``math/`` and ``schemas/`` bytes, with the labelled non-canon fixtures of
``tests/fixtures/magic10_v2/`` placed at ``math/thresholds.json`` and
``catalog/magic10_mechanics_v2.json``. Each adverse case is one mutation of one
real input in that root; nothing is written under the repository's own tree, and
no maxima value is asserted as canon. Identity values computed here prove the
procedure; they are not the cutover identity. Expectations are transcribed from
canon (HDE Schemas and Artifacts §2.1 and §2.9; HDE Math Spec §5.2.11; HDE Build
Notes, the offsets addendum), not read back from the module under test.
"""
from __future__ import annotations

import ast
import dataclasses
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from types import MappingProxyType
from typing import Callable, NamedTuple

import pytest

from engine.config import magic10_v2_loader as v2
from engine.config.registry_loader import (
    ADMITTED_RELEASE_ROSTER,
    ManifestEntry,
    SchemaValidationError,
    SourceIdentity,
    load_active_mechanics_bundle,
)
from engine.serializer import canon

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests" / "fixtures" / "magic10_v2"
MODULE_PATH = "engine/config/magic10_v2_loader.py"
CONFIG = "catalog/magic10_mechanics_v2.json"
CENTERS = "catalog/centers_v1.json"
TYPE_PAIRING = "catalog/type_pairing_v1.json"
THRESHOLDS = "math/thresholds.json"
SOURCES = {
    "caps": "catalog/magic10_caps.json",
    "categories": "catalog/magic10.json",
    "centers": CENTERS,
    "channels": "catalog/channels_v1.json",
    "thresholds": THRESHOLDS,
    "type_pairing": TYPE_PAIRING,
}
CFG_SCHEMA = "schemas/magic10_mechanics_v2.schema.json"
CTR_SCHEMA = "schemas/centers_v1.schema.json"
TP_SCHEMA = "schemas/type_pairing_v1.schema.json"
THR_SCHEMA = "schemas/thresholds_v2.schema.json"
RESULT_SCHEMAS = ("schemas/magic10_result_v2.schema.json", "schemas/magic10_compat_result_v2.schema.json")

# HDE Schemas and Artifacts §2.1 and §2.9; HDE Build Notes, the offsets addendum.
EXPECTED_CENTERS = ("ajna", "ego", "g", "head", "root", "sacral", "solar_plexus", "spleen", "throat")
EXPECTED_MOTORS = frozenset({"sacral", "solar_plexus", "ego", "root"})
EXPECTED_AURA_CLASSES = ("generator", "projector", "manifestor", "reflector")
EXPECTED_RULES = (
    "same_class",
    "generator_with_nonsacral",
    "generator_manifestor",
    "generator_projector",
    "projector_manifestor",
    "reflector_present",
)
EXPECTED_CATEGORIES = (
    "harmony", "heat", "communication", "alignment", "comfort",
    "consistency", "expansion", "creativity", "drive", "balance",
)
EXPECTED_NONZERO_OFFSETS = {
    ("generator_projector", "communication"): 50,
    ("generator_projector", "alignment"): 50,
    ("projector_manifestor", "alignment"): -50,
}
# HDE Schemas and Artifacts §5.1: the new members (two catalogs, six schemas, the
# module, the cut-written configuration) and the rebound existing member.
EXPECTED_DECLARED_MEMBERS = (
    "catalog/centers_v1.json",
    "catalog/magic10_mechanics_v2.json",
    "catalog/type_pairing_v1.json",
    "engine/config/magic10_v2_loader.py",
    "schemas/centers_v1.schema.json",
    "schemas/magic10_compat_result_v2.schema.json",
    "schemas/magic10_mechanics_v2.schema.json",
    "schemas/magic10_result_v2.schema.json",
    "schemas/thresholds_v2.schema.json",
    "schemas/type_pairing_v1.schema.json",
)
CLOSED_RAILS_ENV = {
    "PATH": os.environ.get("PATH", ""),
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "APP_ENV": "test",
}
V1_THRESHOLD_MODULES = ("engine.compat.thresholds", "engine.magic10.thresholds")


# ---------------------------------------------------------------------------
# Temporary roots and mutation helpers. Every helper below edits one real input
# inside a temporary root; none writes under the repository's own tree.
# ---------------------------------------------------------------------------

def _root(tmp_path: Path, name: str = "root") -> Path:
    """Assemble a temporary root: repository catalog/, math/, schemas/ plus the fixtures."""
    root = tmp_path / name
    for directory in ("catalog", "math", "schemas"):
        shutil.copytree(ROOT / directory, root / directory)
    shutil.copyfile(FIXTURES / "thresholds_v2.fixture.json", root / THRESHOLDS)
    shutil.copyfile(FIXTURES / "magic10_mechanics_v2.fixture.json", root / CONFIG)
    return root


def _rows(root: Path, *extra: ManifestEntry) -> tuple[ManifestEntry, ...]:
    """Manifest rows binding the root's current configuration bytes, plus ``extra``."""
    raw = (root / CONFIG).read_bytes()
    rows = [ManifestEntry(CONFIG, hashlib.sha256(raw).hexdigest(), len(raw)), *extra]
    return tuple(sorted(rows, key=lambda row: row.path))


def _read(root: Path, path: str) -> object:
    return json.loads((root / path).read_bytes())


def _rewrite(root: Path, path: str, mutate: Callable[[object], None]) -> None:
    """Mutation input: load ``path``, apply ``mutate`` in place, write canonical bytes."""
    data = _read(root, path)
    mutate(data)
    (root / path).write_bytes(canon.sercanon(data, sort_keys=True))


def _rebind(root: Path, name: str) -> None:
    """Rebind the configuration's ``sources[name]`` to that source's current bytes."""
    digest = hashlib.sha256((root / SOURCES[name]).read_bytes()).hexdigest()
    _rewrite(root, CONFIG, lambda config: config["sources"][name].__setitem__("sha256", digest))


def _admit(root: Path, rows: tuple[ManifestEntry, ...] | None = None) -> v2.Magic10V2Bundle:
    return v2.load_magic10_v2_bundle_from_root(root, _rows(root) if rows is None else rows)


def _refusal(root: Path, rows: object = None) -> SchemaValidationError:
    with pytest.raises(SchemaValidationError) as caught:
        v2.load_magic10_v2_bundle_from_root(root, _rows(root) if rows is None else rows)
    return caught.value


def _assert_schema_refusal(error: SchemaValidationError, schema: str, pointer: str) -> None:
    assert error.code == "M10V2_SCHEMA_VALIDATION_FAILED", (error.code, error.details)
    assert set(error.details) == {"schema", "instance_path", "keyword"}
    assert error.details["schema"] == schema
    assert error.details["instance_path"].startswith(pointer), error.details


def _signal(config: dict, signal_id: str) -> dict:
    return next(row for row in config["signals"] if row["signal_id"] == signal_id)


def _center_row(config: dict, category: str) -> dict:
    return next(row for row in config["center_map"] if row["category_id"] == category)


def _set(container, key, value) -> None:
    container[key] = value


def _swap_first_two(items: list) -> None:
    items[0], items[1] = items[1], items[0]


def _config(mutate: Callable[[dict], None]) -> Callable[[Path], None]:
    """Mutation of the configuration."""
    return lambda root: _rewrite(root, CONFIG, mutate)


def _source(name: str, mutate: Callable[[object], None]) -> Callable[[Path], None]:
    """Mutation of one source, with the configuration's binding rebound to it."""
    def apply(root: Path) -> None:
        _rewrite(root, SOURCES[name], mutate)
        _rebind(root, name)
    return apply


def _one_byte(path: str, old: bytes, new: bytes) -> Callable[[Path], None]:
    """Mutation of one byte of a source, with no rebinding."""
    def apply(root: Path) -> None:
        raw = (root / path).read_bytes()
        assert old in raw and len(old) == len(new)
        (root / path).write_bytes(raw.replace(old, new, 1))
    return apply


def _seven_channels(config: dict) -> None:
    row = _signal(config, "rapport_delta")
    present = {channel["channel_id"] for channel in row["channels"]}
    added = [channel_id for channel_id in ("01-08", "02-14", "03-60", "04-63") if channel_id not in present][:3]
    row["channels"] = sorted(row["channels"] + [{"channel_id": c, "weight": 1} for c in added], key=lambda c: c["channel_id"])


def _duplicate_first(signal_id: str, weight: int | None = None) -> Callable[[dict], None]:
    def mutate(config: dict) -> None:
        channels = _signal(config, signal_id)["channels"]
        first = dict(channels[0])
        if weight is not None:
            first["weight"] = weight
        channels[1] = first
    return mutate


def _thaw(value: object) -> object:
    if isinstance(value, MappingProxyType):
        return {key: _thaw(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_thaw(item) for item in value]
    return value


# ---------------------------------------------------------------------------
# T-01, T-02: admission of the complete fixture bundle; the frozen result.
# ---------------------------------------------------------------------------

def test_complete_fixture_bundle_is_admitted(tmp_path: Path) -> None:
    root = _root(tmp_path)
    bundle = _admit(root)
    assert type(bundle) is v2.Magic10V2Bundle
    assert _thaw(bundle.configuration) == _read(root, CONFIG)
    assert tuple(bundle.maxima) == EXPECTED_CATEGORIES
    assert all(maxima == (24, 49, 74, 100) for maxima in bundle.maxima.values())
    assert tuple(sorted(bundle.centers)) == EXPECTED_CENTERS
    assert {center for center, motor in bundle.centers.items() if motor} == EXPECTED_MOTORS
    assert bundle.aura_classes == EXPECTED_AURA_CLASSES
    assert tuple(bundle.type_pairing) == EXPECTED_RULES
    for rule in EXPECTED_RULES:
        assert set(bundle.type_pairing[rule]) == set(EXPECTED_CATEGORIES)
        for category in EXPECTED_CATEGORIES:
            assert bundle.type_pairing[rule][category] == EXPECTED_NONZERO_OFFSETS.get((rule, category), 0)
    expected_paths = tuple(sorted([CONFIG, *SOURCES.values()]))
    assert tuple(identity.path for identity in bundle.source_identities) == expected_paths
    for identity in bundle.source_identities:
        raw = (root / identity.path).read_bytes()
        assert (identity.sha256, identity.size) == (hashlib.sha256(raw).hexdigest(), len(raw))
    assert bundle.config_sha256 == hashlib.sha256((root / CONFIG).read_bytes()).hexdigest()
    assert bundle.source_bundle_sha256 == v2.magic10_v2_source_bundle_sha256(bundle.source_identities)
    assert bundle.registry.centers == EXPECTED_CENTERS
    assert tuple(bundle.registry.magic10_order) == EXPECTED_CATEGORIES
    # Relaxed v1 rules: both Balance signals read all 36 Channels at weight 1 and
    # share them, a shape the v1 overlap and one-through-six rules refuse.
    balance = [row for row in bundle.configuration["signals"] if row["signal_id"] in ("equilibrium_score", "counterweight_ratio")]
    assert [len(row["channels"]) for row in balance] == [36, 36]
    assert balance[0]["channels"] == balance[1]["channels"]


def test_admitted_bundle_is_deeply_frozen(tmp_path: Path) -> None:
    bundle = _admit(_root(tmp_path))
    for mapping, key, value in (
        (bundle.configuration, "config_id", "x"),
        (bundle.maxima, "heat", ()),
        (bundle.centers, "g", True),
        (bundle.type_pairing, "same_class", {}),
        (bundle.type_pairing["generator_projector"], "alignment", 0),
        (bundle.configuration["blend"], "channel", 0),
    ):
        with pytest.raises(TypeError):
            mapping[key] = value
    with pytest.raises(AttributeError):
        bundle.configuration["signals"][0]["channels"].append({})
    with pytest.raises(dataclasses.FrozenInstanceError):
        bundle.config_sha256 = "0" * 64


# ---------------------------------------------------------------------------
# T-03: one adverse refusal per rule row (Implementation Audit R-04; the
# instruction's LR-01 to LR-20). Schema-stage refusals assert the refusing schema
# and the mutated object's pointer; rule-stage refusals assert their details.
# Signal indices: 0 rapport_delta, 18 equilibrium_score, 19 counterweight_ratio.
# ---------------------------------------------------------------------------

class Case(NamedTuple):
    case_id: str
    mutate: Callable[[Path], None]
    code: str
    schema: str | None = None
    pointer: str | None = None
    details: dict | None = None
    rows: Callable[[Path], object] | None = None


def _rapport(config: dict) -> list:
    return _signal(config, "rapport_delta")["channels"]


def _cm(config: dict, category: str) -> dict:
    return _center_row(config, category)["weights"]


SCHEMA = "M10V2_SCHEMA_VALIDATION_FAILED"
RULE_CASES = (
    Case("LR-01-unknown-channel", _config(lambda c: _set(_rapport(c), 0, {"channel_id": "01-02", "weight": 1})), SCHEMA, CFG_SCHEMA, "/signals/0"),
    Case("LR-02-signal-replaced", _config(lambda c: _set(_signal(c, "rapport_delta"), "signal_id", "rapport_deltaX")), SCHEMA, CFG_SCHEMA, "/signals"),
    Case("LR-02-signals-swapped", _config(lambda c: _swap_first_two(c["signals"])), "M10V2_SIGNAL_ORDER_MISMATCH", details={}),
    Case("LR-03-category-weights-present", _config(lambda c: _set(c, "category_weights", [{"category_id": "harmony", "weights": [1, 1]}])), SCHEMA, CFG_SCHEMA, "/"),
    Case("LR-03-center-map-order", _config(lambda c: _swap_first_two(c["center_map"])), "M10V2_CENTER_MAP_ORDER_MISMATCH", details={}),
    Case("LR-04-caps-min-above-max", _source("caps", lambda d: d["harmony"]["bounds"].update({"min": 60, "max": 50})), "INVALID_MAGIC10", details={}),
    Case("LR-05-seven-channels", _config(_seven_channels), SCHEMA, CFG_SCHEMA, "/signals/0"),
    Case("LR-06-balance-35-channels", _config(lambda c: _signal(c, "equilibrium_score")["channels"].pop()), SCHEMA, CFG_SCHEMA, "/signals/18"),
    Case("LR-06-balance-weight-2", _config(lambda c: _set(_signal(c, "equilibrium_score")["channels"][0], "weight", 2)), SCHEMA, CFG_SCHEMA, "/signals/18"),
    Case("LR-07-channel-weight-0", _config(lambda c: _set(_rapport(c)[0], "weight", 0)), SCHEMA, CFG_SCHEMA, "/signals/0"),
    Case("LR-07-channel-weight-4", _config(lambda c: _set(_rapport(c)[0], "weight", 4)), SCHEMA, CFG_SCHEMA, "/signals/0"),
    Case("LR-08-none-not-zero", _config(lambda c: _set(c["profiles"][0]["responses"], "none", 1)), SCHEMA, CFG_SCHEMA, "/profiles/0/responses/none"),
    Case("LR-08-ordering-broken", _config(lambda c: _set(c["profiles"][0]["responses"], "compromise", 6000)), "M10V2_PROFILE_INEQUALITY_MISMATCH", details={"profile": "activation_bp_v1"}),
    Case("LR-09-balance-with-profile", _config(lambda c: _set(_signal(c, "equilibrium_score"), "profile_id", "coherence_bp_v1")), SCHEMA, CFG_SCHEMA, "/signals/18"),
    Case("LR-09-balance-v1-operation", _config(lambda c: _set(_signal(c, "equilibrium_score"), "operation", "twice_min_owner_mass_v1")), SCHEMA, CFG_SCHEMA, "/signals/18"),
    Case("LR-10-channel-listed-twice", _config(_duplicate_first("rapport_delta")), SCHEMA, CFG_SCHEMA, "/signals/0"),
    Case("LR-10-channel-twice-other-weight", _config(_duplicate_first("rapport_delta", weight=2)), "M10V2_SIGNAL_MEMBERSHIP_INVALID", details={"signal": "rapport_delta"}),
    Case("LR-10-channels-out-of-order", _config(lambda c: _swap_first_two(_rapport(c))), "M10V2_SIGNAL_MEMBERSHIP_INVALID", details={"signal": "rapport_delta"}),
    Case("LR-11-balance-channel-listed-twice", _config(_duplicate_first("equilibrium_score")), SCHEMA, CFG_SCHEMA, "/signals/18"),
    Case("LR-12-balance-missing-a-channel", _config(lambda c: _signal(c, "counterweight_ratio")["channels"].pop(5)), SCHEMA, CFG_SCHEMA, "/signals/19"),
    Case("LR-13-v1-signal-scale", _config(lambda c: _set(c, "signal_scale", 2)), SCHEMA, CFG_SCHEMA, "/signal_scale"),
    Case("LR-13-v1-ordinary-operation", _config(lambda c: _set(_signal(c, "rapport_delta"), "operation", "weighted_state_sum_v1")), SCHEMA, CFG_SCHEMA, "/signals/0"),
    Case("LR-14-maxima-descending", _source("thresholds", lambda d: _set(d["categories"][0], "maxima", [49, 24, 74, 100])), "M10V2_MAXIMA_NOT_ASCENDING", details={"category": "harmony"}),
    Case("LR-14-maxima-repeated", _source("thresholds", lambda d: _set(d["categories"][0], "maxima", [24, 24, 74, 100])), "M10V2_MAXIMA_NOT_ASCENDING", details={"category": "harmony"}),
    Case("LR-14-fourth-not-100", _source("thresholds", lambda d: _set(d["categories"][0], "maxima", [24, 49, 74, 99])), SCHEMA, THR_SCHEMA, "/categories/0/maxima/3"),
    Case("LR-14-v1-shaped-thresholds", _source("thresholds", lambda d: (d.clear(), d.update({"clamp": [0, 100], "edges": [24, 49, 74, 100], "rounding": "ROUND_HALF_UP", "version": "1"}))), SCHEMA, THR_SCHEMA, "/"),
    Case("LR-15-caps-byte", _one_byte("catalog/magic10_caps.json", b'"max":100', b'"max":900'), "M10V2_SOURCE_MISMATCH", details={"source": "caps"}),
    Case("LR-15-categories-byte", _one_byte("catalog/magic10.json", b"harmony", b"harmonz"), "M10V2_SOURCE_MISMATCH", details={"source": "categories"}),
    Case("LR-15-centers-byte", _one_byte(CENTERS, b'"ajna"', b'"ajnb"'), "M10V2_SOURCE_MISMATCH", details={"source": "centers"}),
    Case("LR-15-channels-byte", _one_byte("catalog/channels_v1.json", b'"narrative"', b'"narrativf"'), "M10V2_SOURCE_MISMATCH", details={"source": "channels"}),
    Case("LR-15-thresholds-byte", _one_byte(THRESHOLDS, b"[24,49,74,100]", b"[24,49,75,100]"), "M10V2_SOURCE_MISMATCH", details={"source": "thresholds"}),
    Case("LR-15-type-pairing-byte", _one_byte(TYPE_PAIRING, b"50", b"51"), "M10V2_SOURCE_MISMATCH", details={"source": "type_pairing"}),
    Case("LR-15-source-path-changed", _config(lambda c: _set(c["sources"]["caps"], "path", "catalog/magic10_capz.json")), SCHEMA, CFG_SCHEMA, "/sources/caps/path"),
    Case("LR-16-maxima-above-100", _source("thresholds", lambda d: _set(d["categories"][0], "maxima", [24, 49, 101, 100])), SCHEMA, THR_SCHEMA, "/categories/0/maxima/2"),
    Case("LR-16-maxima-below-0", _source("thresholds", lambda d: _set(d["categories"][0], "maxima", [-1, 49, 74, 100])), SCHEMA, THR_SCHEMA, "/categories/0/maxima/0"),
    Case("LR-17-row-digest-differs", lambda root: None, "M10V2_MANIFEST_HASH_MISMATCH", details={},
         rows=lambda root: (ManifestEntry(CONFIG, "0" * 64, _rows(root)[0].size),)),
    Case("LR-17-row-size-differs", lambda root: None, "M10V2_MANIFEST_SIZE_MISMATCH", details={},
         rows=lambda root: (ManifestEntry(CONFIG, _rows(root)[0].sha256, _rows(root)[0].size + 1),)),
    Case("LR-17-row-absent", lambda root: None, "M10V2_CONFIGURATION_ROW_MISSING", details={}, rows=lambda root: ()),
    Case("LR-17-second-configuration", lambda root: None, "M10V2_MULTIPLE_CONFIGURATIONS", details={},
         rows=lambda root: _rows(root, ManifestEntry("catalog/magic10_mechanics_v1.json", "a" * 64, 1))),
    Case("LR-18a-key-motor-heart", _config(lambda c: _set(_cm(c, "heat"), "motor_heart", 1)), SCHEMA, CFG_SCHEMA, "/center_map/1"),
    Case("LR-18a-key-not-a-center", _config(lambda c: _set(_cm(c, "heat"), "brain", 1)), SCHEMA, CFG_SCHEMA, "/center_map/1"),
    Case("LR-18b-center-weight-0", _config(lambda c: _set(_cm(c, "harmony"), "g", 0)), SCHEMA, CFG_SCHEMA, "/center_map/0/weights/g"),
    Case("LR-18b-center-weight-4", _config(lambda c: _set(_cm(c, "harmony"), "g", 4)), SCHEMA, CFG_SCHEMA, "/center_map/0/weights/g"),
    Case("LR-18c-outcome-missing", _config(lambda c: c["center_profiles"][0]["responses"].pop("shared")), SCHEMA, CFG_SCHEMA, "/center_profiles/0/responses"),
    Case("LR-18c-open-not-zero", _config(lambda c: _set(c["center_profiles"][0]["responses"], "open", 1)), SCHEMA, CFG_SCHEMA, "/center_profiles/0/responses/open"),
    Case("LR-18d-blend-sums-to-101", _config(lambda c: _set(c["blend"], "channel", 61)), "M10V2_BLEND_SUM_MISMATCH", details={}),
    Case("LR-18e-saturation-zero", _config(lambda c: _set(c, "saturation_k_bp", 0)), SCHEMA, CFG_SCHEMA, "/saturation_k_bp"),
    Case("LR-18f-unknown-aura-class", _source("type_pairing", lambda d: _set(d["aura_classes"], 0, "manifesting_generator")), SCHEMA, TP_SCHEMA, "/aura_classes/0"),
    Case("LR-18f-unknown-rule-name", _source("type_pairing", lambda d: _set(d["rules"][0], "rule_id", "mystery")), SCHEMA, TP_SCHEMA, "/rules"),
    Case("LR-18g-cell-dropped", _source("type_pairing", lambda d: d["rules"][0]["offsets"].pop("heat")), SCHEMA, TP_SCHEMA, "/rules/0/offsets"),
    Case("LR-18g-rule-row-dropped", _source("type_pairing", lambda d: d["rules"].pop()), SCHEMA, TP_SCHEMA, "/rules"),
    Case("LR-18h-maxima-set-dropped", _source("thresholds", lambda d: d["categories"].pop()), SCHEMA, THR_SCHEMA, "/categories"),
    Case("LR-19-config-id", _config(lambda c: _set(c, "config_id", "m10-relevance-centers-type-v2.0.1")), "M10V2_PINNED_CONTENT_MISMATCH", details={"item": "config_id"}),
    Case("LR-19-profile-response", _config(lambda c: _set(c["profiles"][0]["responses"], "electromagnetic", 9000)), "M10V2_PINNED_CONTENT_MISMATCH", details={"item": "profiles"}),
    Case("LR-19-ordinary-map", _config(lambda c: _set(_rapport(c)[0], "weight", 2)), "M10V2_PINNED_CONTENT_MISMATCH", details={"item": "signals"}),
    Case("LR-19-center-profile-response", _config(lambda c: _set(c["center_profiles"][0]["responses"], "shared", 3000)), "M10V2_PINNED_CONTENT_MISMATCH", details={"item": "center_profiles"}),
    Case("LR-19-center-map-weight", _config(lambda c: _set(_cm(c, "harmony"), "g", 2)), "M10V2_PINNED_CONTENT_MISMATCH", details={"item": "center_map"}),
    Case("LR-19-blend-59-26-15", _config(lambda c: c["blend"].update({"channel": 59, "center": 26})), "M10V2_PINNED_CONTENT_MISMATCH", details={"item": "blend"}),
    Case("LR-19-saturation", _config(lambda c: _set(c, "saturation_k_bp", 9000)), "M10V2_PINNED_CONTENT_MISMATCH", details={"item": "saturation_k_bp"}),
    Case("LR-19-offset-cell", _source("type_pairing", lambda d: _set(d["rules"][3]["offsets"], "alignment", 100)), "M10V2_PINNED_CONTENT_MISMATCH", details={"item": "type_pairing"}),
    Case("LR-20-center-row-dropped", _source("centers", lambda d: d["centers"].pop()), SCHEMA, CTR_SCHEMA, "/centers"),
    Case("LR-20-unknown-center", _source("centers", lambda d: _set(d["centers"][0], "center_id", "brain")), SCHEMA, CTR_SCHEMA, "/centers"),
    Case("LR-20-duplicated-center-row", _source("centers", lambda d: _set(d["centers"], 1, dict(d["centers"][0]))), SCHEMA, CTR_SCHEMA, "/centers"),
    Case("LR-20-wrong-motor-flag", _source("centers", lambda d: _set(d["centers"][0], "motor", True)), "M10V2_CENTER_MOTOR_MISMATCH", details={}),
    # Order rules a schema cannot express, on the other ordered inputs.
    Case("profiles-out-of-order", _config(lambda c: _swap_first_two(c["profiles"])), "M10V2_PROFILE_ROSTER_MISMATCH", details={}),
    Case("center-profiles-out-of-order", _config(lambda c: _swap_first_two(c["center_profiles"])), "M10V2_PINNED_CONTENT_MISMATCH", details={"item": "center_profiles"}),
    Case("aura-classes-out-of-order", _source("type_pairing", lambda d: _swap_first_two(d["aura_classes"])), "M10V2_PINNED_CONTENT_MISMATCH", details={"item": "type_pairing"}),
)


@pytest.mark.parametrize("case", RULE_CASES, ids=[case.case_id for case in RULE_CASES])
def test_each_rule_row_has_an_adverse_refusal_with_a_stable_code(tmp_path: Path, case: Case) -> None:
    root = _root(tmp_path)
    case.mutate(root)
    error = _refusal(root, case.rows(root) if case.rows else None)
    if case.schema is not None:
        _assert_schema_refusal(error, case.schema, case.pointer)
    else:
        assert error.code == case.code, (error.code, error.details)
        assert error.details == case.details


# ---------------------------------------------------------------------------
# T-04: relaxed maxima admitted; thresholds rows carry no order rule.
# ---------------------------------------------------------------------------

def test_maxima_other_than_the_v1_edges_are_admitted(tmp_path: Path) -> None:
    """Mutation input: one category's fixture maxima changed in the temporary root, never committed."""
    fixture = _admit(_root(tmp_path, "fixture"))
    root = _root(tmp_path, "derived")
    _source("thresholds", lambda d: _set(d["categories"][0], "maxima", [20, 45, 80, 100]))(root)
    derived = _admit(root)
    assert derived.maxima["harmony"] == (20, 45, 80, 100)
    assert all(derived.maxima[category] == (24, 49, 74, 100) for category in EXPECTED_CATEGORIES[1:])
    assert derived.config_sha256 != fixture.config_sha256
    assert derived.source_bundle_sha256 != fixture.source_bundle_sha256


def test_thresholds_rows_are_keyed_by_category_not_ordered(tmp_path: Path) -> None:
    root = _root(tmp_path)
    _source("thresholds", lambda d: _swap_first_two(d["categories"]))(root)
    bundle = _admit(root)
    assert tuple(bundle.maxima) == EXPECTED_CATEGORIES


# ---------------------------------------------------------------------------
# T-05, T-06: no default substitutes for a missing input.
# ---------------------------------------------------------------------------

def _center_map_keys() -> list[tuple[int, str]]:
    config = json.loads((FIXTURES / "magic10_mechanics_v2.fixture.json").read_bytes())
    return [(index, key) for index, row in enumerate(config["center_map"]) for key in sorted(row["weights"])]


def _removals() -> dict[str, list[tuple[Callable[[Path], None], str | None, str]]]:
    """Each removal kind: (mutation, refusing schema or None, pointer or pinned item)."""
    kinds: dict[str, list] = {
        "center row": [(_source("centers", lambda d, i=i: d["centers"].pop(i)), CTR_SCHEMA, "/centers") for i in range(9)],
        "aura class": [(_source("type_pairing", lambda d, i=i: d["aura_classes"].pop(i)), TP_SCHEMA, "/aura_classes") for i in range(4)],
        "center-map weight": [
            (_config(lambda c, i=i, k=k: c["center_map"][i]["weights"].pop(k)), None, "center_map")
            for i, k in _center_map_keys()
        ],
        "center profile": [(_config(lambda c, i=i: c["center_profiles"].pop(i)), CFG_SCHEMA, "/center_profiles") for i in range(2)],
        "response profile": [(_config(lambda c, i=i: c["profiles"].pop(i)), CFG_SCHEMA, "/profiles") for i in range(3)],
        "maxima set": [(_source("thresholds", lambda d, i=i: d["categories"].pop(i)), THR_SCHEMA, "/categories") for i in range(10)],
        "rule row": [(_source("type_pairing", lambda d, i=i: d["rules"].pop(i)), TP_SCHEMA, "/rules") for i in range(6)],
        "offset cell": [
            (_source("type_pairing", lambda d, i=i, k=k: d["rules"][i]["offsets"].pop(k)), TP_SCHEMA, f"/rules/{i}/offsets")
            for i in range(6) for k in EXPECTED_CATEGORIES
        ],
        "sources row": [(_config(lambda c, n=n: c["sources"].pop(n)), CFG_SCHEMA, "/sources") for n in SOURCES],
    }
    return kinds


REMOVAL_COUNTS = {
    "center row": 9, "aura class": 4, "center-map weight": 30, "center profile": 2, "response profile": 3,
    "maxima set": 10, "rule row": 6, "offset cell": 60, "sources row": 6,
}


@pytest.mark.parametrize("kind", sorted(REMOVAL_COUNTS))
def test_removing_any_required_input_fails_closed_with_no_default(tmp_path: Path, kind: str) -> None:
    removals = _removals()[kind]
    assert len(removals) == REMOVAL_COUNTS[kind]
    for index, (mutate, schema, where) in enumerate(removals):
        root = _root(tmp_path, f"{index}")
        mutate(root)
        error = _refusal(root)
        if schema is not None:
            _assert_schema_refusal(error, schema, where)
        else:
            assert (error.code, error.details) == ("M10V2_PINNED_CONTENT_MISMATCH", {"item": where})
        shutil.rmtree(root)


ABSENT_INPUTS = (
    CONFIG, *SOURCES.values(), CFG_SCHEMA, CTR_SCHEMA, TP_SCHEMA, THR_SCHEMA, *RESULT_SCHEMAS,
    "catalog/gates_v1.json", "catalog/magic10_seeds.json", "catalog/manifest.json",
    "schemas/gates_v1.schema.json", "schemas/channels_v1.schema.json",
)


@pytest.mark.parametrize("path", sorted(set(ABSENT_INPUTS)))
def test_each_declared_input_absent_from_the_root_fails_closed(tmp_path: Path, path: str) -> None:
    root = _root(tmp_path)
    rows = _rows(root)
    (root / path).unlink()
    error = _refusal(root, rows)
    assert error.code == "MISSING_FILE"


# ---------------------------------------------------------------------------
# T-07, T-08, T-09: safe reads, owning-schema validation, manifest-row form.
# ---------------------------------------------------------------------------

def test_v2_inputs_are_read_through_the_safe_canonical_readers(tmp_path: Path) -> None:
    root = _root(tmp_path, "noncanonical")
    raw = (root / CONFIG).read_bytes()
    (root / CONFIG).write_bytes(raw.replace(b'{"blend"', b'{ "blend"', 1))
    assert _refusal(root).code == "NONCANONICAL_JSON"

    root = _root(tmp_path, "duplicate")
    raw = (root / CENTERS).read_bytes()
    (root / CENTERS).write_bytes(raw.replace(b'{"centers"', b'{"centers":[],"centers"', 1))
    assert _refusal(root).code == "DUPLICATE_JSON_KEY"

    root = _root(tmp_path, "symlink")
    rows = _rows(root)
    (root / CONFIG).rename(root / "catalog" / "real.json")
    (root / CONFIG).symlink_to("real.json")
    assert _refusal(root, rows).code == "UNSAFE_SOURCE_PATH"


@pytest.mark.parametrize(("schema", "mutate", "code"), [
    (CTR_SCHEMA, lambda s: _set(s, "$id", "schemas/other.schema.json"), "M10V2_SCHEMA_IDENTITY_MISMATCH"),
    (THR_SCHEMA, lambda s: _set(s, "$schema", "http://json-schema.org/draft-07/schema#"), "M10V2_SCHEMA_DRAFT_MISMATCH"),
    (TP_SCHEMA, lambda s: _set(s["properties"], "aura_classes", {"$ref": "https://example.org/aura.json"}), "NONLOCAL_SCHEMA_REFERENCE"),
    (RESULT_SCHEMAS[0], lambda s: _set(s, "$id", "schemas/other.schema.json"), "SCHEMA_IDENTITY_MISMATCH"),
    (CTR_SCHEMA, lambda s: _set(s, "type", 5), "M10V2_SCHEMA_INVALID"),
    (TP_SCHEMA, lambda s: _set(s["properties"], "aura_classes", {"$ref": "#/$defs/missing"}), "M10V2_SCHEMA_VALIDATION_FAILED"),
], ids=["data-schema-id", "data-schema-draft", "remote-reference", "result-schema-id",
        "schema-fails-check-schema", "dangling-local-reference"])
def test_owning_schemas_are_validated_without_retrieval(tmp_path: Path, schema: str, mutate, code: str) -> None:
    root = _root(tmp_path)
    _rewrite(root, schema, mutate)
    assert _refusal(root).code == code


def test_manifest_rows_must_be_sorted_entries_and_other_rows_are_ignored(tmp_path: Path) -> None:
    root = _root(tmp_path)
    unsorted = tuple(reversed(_rows(root, ManifestEntry("catalog/zzz.json", "a" * 64, 1))))
    assert _refusal(root, unsorted).code == "M10V2_INVALID_MANIFEST_ROWS"
    assert _refusal(root, ({"path": CONFIG},)).code == "M10V2_INVALID_MANIFEST_ROWS"
    bundle = _admit(root, _rows(root, ManifestEntry("engine/core/core.py", "b" * 64, 9)))
    assert bundle.config_sha256 == _rows(root)[0].sha256


# ---------------------------------------------------------------------------
# T-10 to T-14: the identity and the cache key.
# ---------------------------------------------------------------------------

_CHILD_ADMISSION = r"""
import hashlib, json, sys
sys.path.insert(0, sys.argv[2])
from pathlib import Path
from engine.config import magic10_v2_loader as v2
from engine.config.registry_loader import ManifestEntry
root = Path(sys.argv[1])
raw = (root / v2.MAGIC10_V2_CONFIGURATION_PATH).read_bytes()
rows = (ManifestEntry(v2.MAGIC10_V2_CONFIGURATION_PATH, hashlib.sha256(raw).hexdigest(), len(raw)),)
bundle = v2.load_magic10_v2_bundle_from_root(root, rows)
print(json.dumps({
    "config_sha256": bundle.config_sha256,
    "source_bundle_sha256": bundle.source_bundle_sha256,
    "v1_threshold_modules": sorted(m for m in sys.modules if m in ("engine.compat.thresholds", "engine.magic10.thresholds")),
}, sort_keys=True))
"""


@pytest.fixture(scope="module")
def admitted_in_two_processes(tmp_path_factory) -> tuple[v2.Magic10V2Bundle, list[dict]]:
    root = _root(tmp_path_factory.mktemp("two-process"))
    in_process = _admit(root)
    children = []
    for _ in range(2):
        completed = subprocess.run(
            [sys.executable, "-I", "-c", _CHILD_ADMISSION, str(root), str(ROOT)],
            capture_output=True, text=True, env=CLOSED_RAILS_ENV, cwd=root, check=False,
        )
        assert completed.returncode == 0, completed.stderr
        children.append(json.loads(completed.stdout))
    return in_process, children


def test_identity_repeats_byte_for_byte_in_one_and_two_processes(tmp_path: Path, admitted_in_two_processes) -> None:
    root = _root(tmp_path)
    first, second = _admit(root), _admit(root)
    assert (first.config_sha256, first.source_bundle_sha256, first.source_identities) == (
        second.config_sha256, second.source_bundle_sha256, second.source_identities
    )
    in_process, children = admitted_in_two_processes
    assert in_process.config_sha256 == first.config_sha256
    for child in children:
        assert (child["config_sha256"], child["source_bundle_sha256"]) == (
            in_process.config_sha256, in_process.source_bundle_sha256
        )


def test_v2_configuration_identity_differs_from_v1(tmp_path: Path) -> None:
    assert _admit(_root(tmp_path)).config_sha256 != load_active_mechanics_bundle().config_sha256


def test_a_one_byte_change_to_any_covered_source_changes_the_source_bundle_identity(tmp_path: Path) -> None:
    root = _root(tmp_path)
    bundle = _admit(root)
    identities = list(bundle.source_identities)
    assert len(identities) == 7
    for index, identity in enumerate(identities):
        changed = bytearray((root / identity.path).read_bytes())
        changed[len(changed) // 2] ^= 0x01
        altered = identities.copy()
        altered[index] = SourceIdentity(identity.path, hashlib.sha256(bytes(changed)).hexdigest(), len(changed))
        assert v2.magic10_v2_source_bundle_sha256(tuple(altered)) != bundle.source_bundle_sha256, identity.path


def test_source_bundle_identity_requires_unique_path_sorted_rows(tmp_path: Path) -> None:
    identities = _admit(_root(tmp_path)).source_identities
    for bad in (tuple(reversed(identities)), (identities[0], *identities)):
        with pytest.raises(SchemaValidationError) as caught:
            v2.magic10_v2_source_bundle_sha256(bad)
        assert caught.value.code == "M10V2_SOURCE_IDENTITY_ORDER"


def test_cache_key_is_the_v2_prefix_followed_by_the_pair_key() -> None:
    assert v2.MAGIC10_V2_INTRINSIC_CACHE_PREFIX == "magic10:v2:"
    pair_key = hashlib.sha256(b"pair").hexdigest()
    assert v2.magic10_v2_intrinsic_cache_key(pair_key) == "magic10:v2:" + pair_key
    for bad in (pair_key.upper(), pair_key[:-1], pair_key + "0", 5, None):
        with pytest.raises(SchemaValidationError) as caught:
            v2.magic10_v2_intrinsic_cache_key(bad)
        assert caught.value.code == "M10V2_INVALID_PAIR_KEY"


def test_v2_identity_constants() -> None:
    assert v2.MAGIC10_V2_CONFIG_ID == "m10-relevance-centers-type-v2.0.0"
    assert v2.MAGIC10_V2_CONFIG_SCHEMA == "magic10_mechanics_config.v2"
    assert v2.MAGIC10_V2_RESULT_SCHEMA == "magic10_result.v2"
    assert v2.MAGIC10_V2_COMPAT_RESULT_SCHEMA == "magic10_compat_result.v2"


# ---------------------------------------------------------------------------
# T-15: declared manifest membership.
# ---------------------------------------------------------------------------

def test_declared_members_are_the_new_governed_files_and_the_cut_written_configuration() -> None:
    assert v2.MAGIC10_V2_DECLARED_MEMBERS == EXPECTED_DECLARED_MEMBERS
    for path in EXPECTED_DECLARED_MEMBERS:
        assert path not in ADMITTED_RELEASE_ROSTER
        assert (ROOT / path).is_file() == (path != CONFIG), path
    assert v2.MAGIC10_V2_REBOUND_MEMBERS == (THRESHOLDS,)
    assert THRESHOLDS in ADMITTED_RELEASE_ROSTER


# ---------------------------------------------------------------------------
# T-16, T-17: the import boundary and no import-time file access.
# ---------------------------------------------------------------------------

def _imported_modules(tree: ast.AST) -> set[str]:
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            names.add("." * node.level + (node.module or ""))
            names.update(f"{node.module or ''}.{alias.name}" for alias in node.names)
    return names


def test_no_v1_release_member_or_the_config_package_imports_the_v2_loader() -> None:
    paths = [path for path in ADMITTED_RELEASE_ROSTER if path.endswith(".py")] + ["engine/config/__init__.py"]
    assert len(paths) == 24
    for path in paths:
        tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
        assert not any(name.endswith("magic10_v2_loader") for name in _imported_modules(tree)), path
        strings = [node.value for node in ast.walk(tree) if isinstance(node, ast.Constant) and isinstance(node.value, str)]
        assert not any("magic10_v2_loader" in value for value in strings), path


def test_the_v2_loader_imports_no_v1_threshold_engine_core_or_compat_module(admitted_in_two_processes) -> None:
    tree = ast.parse((ROOT / MODULE_PATH).read_text(encoding="utf-8"), filename=MODULE_PATH)
    imported = _imported_modules(tree)
    for prefix in ("engine.magic10", "engine.compat", "engine.core"):
        assert not any(name == prefix or name.startswith(prefix + ".") for name in imported), prefix
    _, children = admitted_in_two_processes
    assert all(child["v1_threshold_modules"] == [] for child in children)


_CHILD_IMPORT_AUDIT = r"""
import sys
sys.path.insert(0, sys.argv[1])
import engine.config.registry_loader, engine.serializer.canon, jsonschema, referencing
opened = []
def audit(event, args):
    if event == "open" and isinstance(args[0], (str, bytes)):
        path = args[0].decode() if isinstance(args[0], bytes) else args[0]
        if path.endswith(".json"):
            opened.append(path)
sys.addaudithook(audit)
import engine.config.magic10_v2_loader
print(len(opened))
"""


def test_the_v2_loader_reads_no_file_at_import(tmp_path: Path) -> None:
    completed = subprocess.run(
        [sys.executable, "-I", "-c", _CHILD_IMPORT_AUDIT, str(ROOT)],
        capture_output=True, text=True, env=CLOSED_RAILS_ENV, cwd=tmp_path, check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert completed.stdout.strip() == "0"
