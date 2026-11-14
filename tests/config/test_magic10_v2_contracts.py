"""HDE-EPIC042 WU-PR-02: Magic-10 v2 catalogs, schemas and labelled fixtures.

HDE-SEPA007.1 and HDE-SEPA007.2. Strict-schema, content and mutation proofs for the
inactive v2 contract. Expectations are transcribed independently from canon (HDE
Schemas and Artifacts §2.1, §2.6, §2.9; HDE Math Spec §5.2.11; the HDE Build Notes
offsets addendum), except where canon says a value is v1's, which is read from the
unchanged v1 release members. Nothing here imports or alters the v1 loader path; the
fail-closed v2 loader and its identity are a later work unit (HDE-SEPA007.3, .4).
"""
from __future__ import annotations

import copy
import functools
import hashlib
import json
from pathlib import Path

import jsonschema
import pytest
from jsonschema import validators
from referencing import Registry
from referencing.exceptions import NoSuchResource

from engine.serializer import canon

ROOT = Path(__file__).resolve().parents[2]
DRAFT_2020_12 = "https://json-schema.org/draft/2020-12/schema"

CENTERS_CATALOG = "catalog/centers_v1.json"
TYPE_PAIRING_CATALOG = "catalog/type_pairing_v1.json"
CENTERS_SCHEMA = "schemas/centers_v1.schema.json"
TYPE_PAIRING_SCHEMA = "schemas/type_pairing_v1.schema.json"
CONFIG_SCHEMA = "schemas/magic10_mechanics_v2.schema.json"
THRESHOLDS_SCHEMA = "schemas/thresholds_v2.schema.json"
RESULT_SCHEMA = "schemas/magic10_result_v2.schema.json"
COMPAT_RESULT_SCHEMA = "schemas/magic10_compat_result_v2.schema.json"
SCHEMAS = (
    CENTERS_SCHEMA,
    TYPE_PAIRING_SCHEMA,
    CONFIG_SCHEMA,
    THRESHOLDS_SCHEMA,
    RESULT_SCHEMA,
    COMPAT_RESULT_SCHEMA,
)
GOVERNED_FILES = (CENTERS_CATALOG, TYPE_PAIRING_CATALOG, *SCHEMAS)

FIXTURES = "tests/fixtures/magic10_v2"
THRESHOLDS_FIXTURE = f"{FIXTURES}/thresholds_v2.fixture.json"
CONFIG_FIXTURE = f"{FIXTURES}/magic10_mechanics_v2.fixture.json"
LABEL_FILE = f"{FIXTURES}/LABEL.txt"

V1_CONFIG = "catalog/magic10_mechanics_v1.json"

# HDE Schemas and Artifacts §2.1: the nine center IDs and the four motors.
EXPECTED_CENTERS = ("ajna", "ego", "g", "head", "root", "sacral", "solar_plexus", "spleen", "throat")
EXPECTED_MOTORS = frozenset({"sacral", "solar_plexus", "ego", "root"})
# HDE Schemas and Artifacts §2.9 "Type-pairing catalog", in canon's order.
EXPECTED_AURA_CLASSES = ["generator", "projector", "manifestor", "reflector"]
EXPECTED_RULES = [
    "same_class",
    "generator_with_nonsacral",
    "generator_manifestor",
    "generator_projector",
    "projector_manifestor",
    "reflector_present",
]
EXPECTED_CATEGORIES = [
    "harmony", "heat", "communication", "alignment", "comfort",
    "consistency", "expansion", "creativity", "drive", "balance",
]
# HDE Build Notes, the offsets addendum, R-1: every other cell is 0.
EXPECTED_NONZERO_OFFSETS = {
    ("generator_projector", "communication"): 50,
    ("generator_projector", "alignment"): 50,
    ("projector_manifestor", "alignment"): -50,
}
# HDE Math Spec §5.2.11 "Components": center profiles and center map.
EXPECTED_CENTER_PROFILES = [
    {"profile_id": "completion_bp_v2", "responses": {"mutual": 10000, "one_sided": 7500, "shared": 2500, "open": 0}},
    {"profile_id": "foundation_bp_v2", "responses": {"mutual": 5000, "one_sided": 7500, "shared": 10000, "open": 0}},
]
EXPECTED_CENTER_MAP = [
    {"category_id": "harmony", "profile_id": "completion_bp_v2", "weights": {"g": 3, "solar_plexus": 2, "spleen": 1}},
    {"category_id": "heat", "profile_id": "completion_bp_v2",
     "weights": {"sacral": 3, "solar_plexus": 2, "ego": 1, "root": 1, "motor_throat": 1}},
    {"category_id": "communication", "profile_id": "completion_bp_v2", "weights": {"throat": 3, "ajna": 2, "head": 1}},
    {"category_id": "alignment", "profile_id": "foundation_bp_v2", "weights": {"g": 3, "ajna": 1, "ego": 1}},
    {"category_id": "comfort", "profile_id": "completion_bp_v2", "weights": {"spleen": 3, "solar_plexus": 2, "g": 1}},
    {"category_id": "consistency", "profile_id": "foundation_bp_v2", "weights": {"sacral": 2, "root": 2, "spleen": 1}},
    {"category_id": "expansion", "profile_id": "completion_bp_v2", "weights": {"head": 2, "root": 2, "sacral": 1}},
    {"category_id": "creativity", "profile_id": "completion_bp_v2", "weights": {"throat": 2, "head": 2, "g": 1}},
    {"category_id": "drive", "profile_id": "completion_bp_v2",
     "weights": {"root": 3, "ego": 2, "sacral": 1, "motor_throat": 2}},
    {"category_id": "balance", "profile_id": "bilateral_completion_v2", "weights": {}},
]
# HDE Schemas and Artifacts §2.9 and HDE Math Spec §5.2.11 "Configuration, identity and validation".
V2_CONFIG_ID = "m10-relevance-centers-type-v2.0.0"
EXPECTED_ROUNDING = {
    "signal": "round_half_up_to_per_mille",
    "component": "round_half_up_to_per_mille",
    "category": "round_half_up_once",
}
EXPECTED_BLEND = {"channel": 60, "center": 25, "type": 15}
EXPECTED_SOURCE_PATHS = {
    "caps": "catalog/magic10_caps.json",
    "categories": "catalog/magic10.json",
    "centers": CENTERS_CATALOG,
    "channels": "catalog/channels_v1.json",
    "thresholds": "math/thresholds.json",
    "type_pairing": TYPE_PAIRING_CATALOG,
}
# Non-canon fixture maxima (Plan review v1.0 §3.2, Q-01 alternative A): v1's edges.
FIXTURE_MAXIMA = [24, 49, 74, 100]
EXPECTED_LABEL_LINES = (
    "NON-CANON TEST FIXTURES - HDE-EPIC042 WU-PR-02 (HDE-SEPA007.2)",
    "thresholds_v2.fixture.json and magic10_mechanics_v2.fixture.json are non-canon test fixtures.",
    "Their per-category maxima [24,49,74,100] are not the Magic-10 v2 cut and assert no canon value.",
    "magic10_mechanics_v2.fixture.json equals canon except sources.thresholds.sha256, which binds thresholds_v2.fixture.json.",
    'The governed thresholds (math/thresholds.json, "version": "2") and configuration '
    "(catalog/magic10_mechanics_v2.json) are written at the v2 release cut by HDE-DIST008.2.",
)

_STRICT = validators.extend(
    jsonschema.Draft202012Validator,
    type_checker=jsonschema.Draft202012Validator.TYPE_CHECKER.redefine(
        "integer", lambda checker, value: type(value) is int
    ),
)


def _load(relative_path: str) -> object:
    return json.loads((ROOT / relative_path).read_bytes())


def _sha256(relative_path: str) -> str:
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def _refuse_retrieval(uri: str) -> object:
    raise NoSuchResource(ref=uri)


def _reference_keys(node: object) -> list[str]:
    found: list[str] = []
    if isinstance(node, dict):
        for key, item in node.items():
            if key in {"$ref", "$dynamicRef", "$recursiveRef"}:
                found.append(key)
            found.extend(_reference_keys(item))
    elif isinstance(node, list):
        for item in node:
            found.extend(_reference_keys(item))
    return found


@functools.lru_cache(maxsize=None)
def _validator(schema_path: str) -> jsonschema.protocols.Validator:
    """The loader's local-schema rule (registry_loader._validate_local_schema), mirrored."""
    schema = _load(schema_path)
    assert isinstance(schema, dict)
    assert schema.get("$schema") == DRAFT_2020_12
    assert schema.get("$id") == schema_path
    assert _reference_keys(schema) == []
    _STRICT.check_schema(schema)
    return _STRICT(schema, registry=Registry(retrieve=_refuse_retrieval))


def _accepts(schema_path: str, data: object) -> bool:
    return not any(True for _ in _validator(schema_path).iter_errors(data))


def _object_paths(data: object, path: tuple = ()):
    if isinstance(data, dict):
        yield path
        for key, item in data.items():
            yield from _object_paths(item, path + (key,))
    elif isinstance(data, list):
        for index, item in enumerate(data):
            yield from _object_paths(item, path + (index,))


def _integer_paths(data: object, path: tuple = ()):
    if type(data) is int:
        yield path
    elif isinstance(data, dict):
        for key, item in data.items():
            yield from _integer_paths(item, path + (key,))
    elif isinstance(data, list):
        for index, item in enumerate(data):
            yield from _integer_paths(item, path + (index,))


def _get(data: object, path: tuple) -> object:
    for step in path:
        data = data[step]
    return data


def _set(data: object, path: tuple, value: object) -> None:
    _get(data, path[:-1])[path[-1]] = value


def _is_center_map_weights(path: tuple) -> bool:
    return len(path) == 3 and path[0] == "center_map" and path[2] == "weights"


def _channel_ids() -> list[str]:
    return sorted(row["id"] for row in _load("catalog/channels_v1.json")["channels"])


def _expected_config() -> dict:
    v1 = _load(V1_CONFIG)
    channels = _channel_ids()
    signals = []
    for row in v1["signals"]:
        if row["signal_id"] == "equilibrium_score":
            signals.append({"channels": [{"channel_id": c, "weight": 1} for c in channels],
                            "operation": "bilateral_owner_mass_v2", "signal_id": "equilibrium_score"})
        elif row["signal_id"] == "counterweight_ratio":
            signals.append({"channels": [{"channel_id": c, "weight": 1} for c in channels],
                            "operation": "mutual_state_share_v2", "signal_id": "counterweight_ratio"})
        else:
            assert row["operation"] == "weighted_state_sum_v1"
            signals.append({**copy.deepcopy(row), "operation": "saturating_state_sum_v2"})
    sources = {name: {"path": path, "sha256": _sha256(path)} for name, path in EXPECTED_SOURCE_PATHS.items()}
    sources["thresholds"]["sha256"] = _sha256(THRESHOLDS_FIXTURE)
    return {
        "blend": dict(EXPECTED_BLEND),
        "center_map": copy.deepcopy(EXPECTED_CENTER_MAP),
        "center_profiles": copy.deepcopy(EXPECTED_CENTER_PROFILES),
        "config_id": V2_CONFIG_ID,
        "profiles": copy.deepcopy(v1["profiles"]),
        "response_scale": 10000,
        "result_schema": "magic10_result.v2",
        "rounding": dict(EXPECTED_ROUNDING),
        "saturation_k_bp": 10000,
        "schema": "magic10_mechanics_config.v2",
        "signal_scale": 10,
        "signals": signals,
        "sources": sources,
    }


# --- T-01: strict, closed draft 2020-12 schema documents -------------------------------

def _unclosed_objects(node: object, path: tuple = ()) -> list[tuple]:
    found: list[tuple] = []
    if isinstance(node, dict):
        if node.get("type") == "object":
            closed = node.get("additionalProperties") is False or (
                "propertyNames" in node and isinstance(node.get("additionalProperties"), dict)
            )
            if not closed:
                found.append(path)
        for key, item in node.items():
            found.extend(_unclosed_objects(item, path + (key,)))
    elif isinstance(node, list):
        for index, item in enumerate(node):
            found.extend(_unclosed_objects(item, path + (index,)))
    return found


@pytest.mark.parametrize("schema_path", SCHEMAS)
def test_schema_documents_are_strict_closed_draft_2020_12(schema_path: str) -> None:
    schema = _load(schema_path)
    _validator(schema_path)
    assert schema["title"] == Path(schema_path).name.removesuffix(".schema.json")
    assert schema["type"] == "object"
    assert _unclosed_objects(schema) == []


def test_schema_enums_match_the_catalogs_they_close() -> None:
    gates_centers = sorted({row["center"] for row in _load("catalog/gates_v1.json")["gates"]})
    categories = _load("catalog/magic10.json")["order"]
    assert gates_centers == list(EXPECTED_CENTERS)
    assert categories == EXPECTED_CATEGORIES

    centers = _load(CENTERS_SCHEMA)["properties"]["centers"]
    assert centers["items"]["properties"]["center_id"]["enum"] == list(EXPECTED_CENTERS)
    pairing = _load(TYPE_PAIRING_SCHEMA)["properties"]
    assert pairing["aura_classes"]["items"]["enum"] == EXPECTED_AURA_CLASSES
    assert pairing["rules"]["items"]["properties"]["rule_id"]["enum"] == EXPECTED_RULES
    assert pairing["rules"]["items"]["properties"]["offsets"]["required"] == EXPECTED_CATEGORIES
    thresholds = _load(THRESHOLDS_SCHEMA)["properties"]["categories"]
    assert thresholds["items"]["properties"]["category_id"]["enum"] == EXPECTED_CATEGORIES

    config = _load(CONFIG_SCHEMA)["properties"]
    mapped, balance = config["center_map"]["items"]["oneOf"]
    assert mapped["properties"]["category_id"]["enum"] == EXPECTED_CATEGORIES[:-1]
    assert balance["properties"]["category_id"]["const"] == "balance"
    assert mapped["properties"]["weights"]["propertyNames"]["enum"] == [*EXPECTED_CENTERS, "motor_throat"]
    ordinary, equilibrium, counterweight = config["signals"]["items"]["oneOf"]
    v1_signal_ids = [row["signal_id"] for row in _load(V1_CONFIG)["signals"]]
    assert ordinary["properties"]["signal_id"]["enum"] == v1_signal_ids[:18]
    assert [equilibrium["properties"]["signal_id"]["const"], counterweight["properties"]["signal_id"]["const"]] == v1_signal_ids[18:]
    for variant in (ordinary, equilibrium, counterweight):
        assert variant["properties"]["channels"]["items"]["properties"]["channel_id"]["enum"] == _channel_ids()
    assert sorted(config["sources"]["required"]) == sorted(EXPECTED_SOURCE_PATHS)
    for name, path in EXPECTED_SOURCE_PATHS.items():
        assert config["sources"]["properties"][name]["properties"]["path"]["const"] == path


# --- T-02: canonical bytes -------------------------------------------------------------

@pytest.mark.parametrize("relative_path", (*GOVERNED_FILES, THRESHOLDS_FIXTURE, CONFIG_FIXTURE))
def test_new_json_files_are_canonical_bytes(relative_path: str) -> None:
    raw = (ROOT / relative_path).read_bytes()
    assert raw == canon.sercanon(json.loads(raw), sort_keys=True)


# --- T-03 and T-04: catalog content ----------------------------------------------------

def test_centers_catalog_holds_the_nine_centers_and_motor_flags() -> None:
    catalog = _load(CENTERS_CATALOG)
    assert _accepts(CENTERS_SCHEMA, catalog)
    rows = catalog["centers"]
    assert [row["center_id"] for row in rows] == list(EXPECTED_CENTERS)
    assert all(set(row) == {"center_id", "motor"} and type(row["motor"]) is bool for row in rows)
    assert {row["center_id"] for row in rows if row["motor"]} == EXPECTED_MOTORS


def test_type_pairing_catalog_holds_the_decided_offsets() -> None:
    catalog = _load(TYPE_PAIRING_CATALOG)
    assert _accepts(TYPE_PAIRING_SCHEMA, catalog)
    assert catalog["aura_classes"] == EXPECTED_AURA_CLASSES
    assert [row["rule_id"] for row in catalog["rules"]] == EXPECTED_RULES
    cells = {}
    for row in catalog["rules"]:
        assert set(row["offsets"]) == set(EXPECTED_CATEGORIES)
        for category, value in row["offsets"].items():
            assert type(value) is int
            cells[(row["rule_id"], category)] = value
    assert len(cells) == 60
    assert cells == {
        (rule, category): EXPECTED_NONZERO_OFFSETS.get((rule, category), 0)
        for rule in EXPECTED_RULES
        for category in EXPECTED_CATEGORIES
    }
    assert sum(1 for value in cells.values() if value != 0) == 3


# --- T-05: catalog mutations -----------------------------------------------------------

def _duplicate_rule_over_last(data: dict) -> None:
    data["rules"][5] = copy.deepcopy(data["rules"][0])
    data["rules"][5]["offsets"]["heat"] = 1


def _duplicate_center_over_next(data: dict) -> None:
    data["centers"][1] = {"center_id": "ajna", "motor": True}


CATALOG_MUTATIONS = {
    "unknown_aura_class": (TYPE_PAIRING_SCHEMA, TYPE_PAIRING_CATALOG,
                           lambda d: d["aura_classes"].__setitem__(3, "manifesting_generator")),
    "duplicate_aura_class": (TYPE_PAIRING_SCHEMA, TYPE_PAIRING_CATALOG,
                             lambda d: d["aura_classes"].__setitem__(3, "generator")),
    "missing_aura_class": (TYPE_PAIRING_SCHEMA, TYPE_PAIRING_CATALOG, lambda d: d["aura_classes"].pop()),
    "unknown_rule": (TYPE_PAIRING_SCHEMA, TYPE_PAIRING_CATALOG,
                     lambda d: d["rules"][0].__setitem__("rule_id", "same_type")),
    "missing_rule_row": (TYPE_PAIRING_SCHEMA, TYPE_PAIRING_CATALOG, lambda d: d["rules"].pop()),
    "duplicate_rule_hides_missing": (TYPE_PAIRING_SCHEMA, TYPE_PAIRING_CATALOG, _duplicate_rule_over_last),
    "missing_cell": (TYPE_PAIRING_SCHEMA, TYPE_PAIRING_CATALOG, lambda d: d["rules"][3]["offsets"].pop("balance")),
    "unknown_category_cell": (TYPE_PAIRING_SCHEMA, TYPE_PAIRING_CATALOG,
                              lambda d: d["rules"][3]["offsets"].__setitem__("romance", 0)),
    "unknown_center": (CENTERS_SCHEMA, CENTERS_CATALOG, lambda d: d["centers"][0].__setitem__("center_id", "heart")),
    "missing_center_row": (CENTERS_SCHEMA, CENTERS_CATALOG, lambda d: d["centers"].pop()),
    "tenth_center_row": (CENTERS_SCHEMA, CENTERS_CATALOG,
                         lambda d: d["centers"].append({"center_id": "heart", "motor": True})),
    "duplicate_center_hides_missing": (CENTERS_SCHEMA, CENTERS_CATALOG, _duplicate_center_over_next),
}


@pytest.mark.parametrize("name", sorted(CATALOG_MUTATIONS))
def test_catalog_mutations_are_refused(name: str) -> None:
    schema_path, catalog_path, mutate = CATALOG_MUTATIONS[name]
    data = copy.deepcopy(_load(catalog_path))
    mutate(data)
    assert not _accepts(schema_path, data)


@pytest.mark.parametrize("value", [True, False, 50.0, "50", None])
def test_offset_cells_are_strict_integers(value: object) -> None:
    data = copy.deepcopy(_load(TYPE_PAIRING_CATALOG))
    data["rules"][3]["offsets"]["alignment"] = value
    assert not _accepts(TYPE_PAIRING_SCHEMA, data)


@pytest.mark.parametrize("value", [0, 1, "true", None])
def test_motor_flag_is_a_strict_boolean(value: object) -> None:
    data = copy.deepcopy(_load(CENTERS_CATALOG))
    data["centers"][5]["motor"] = value
    assert not _accepts(CENTERS_SCHEMA, data)


# --- Generic closure sweeps over every catalog and fixture -------------------------------

INSTANCES = [
    (CENTERS_SCHEMA, CENTERS_CATALOG),
    (TYPE_PAIRING_SCHEMA, TYPE_PAIRING_CATALOG),
    (THRESHOLDS_SCHEMA, THRESHOLDS_FIXTURE),
    (CONFIG_SCHEMA, CONFIG_FIXTURE),
]


@pytest.mark.parametrize("schema_path,instance_path", INSTANCES)
def test_unknown_field_is_refused_at_every_object(schema_path: str, instance_path: str) -> None:
    data = _load(instance_path)
    assert _accepts(schema_path, data)
    paths = list(_object_paths(data))
    assert paths
    for path in paths:
        mutated = copy.deepcopy(data)
        _get(mutated, path)["unexpected_field"] = 0
        assert not _accepts(schema_path, mutated), path


@pytest.mark.parametrize("schema_path,instance_path", INSTANCES)
def test_every_required_field_dropped_is_refused(schema_path: str, instance_path: str) -> None:
    # Center-map weight keys are a closed optional set; their exact content is proved by
    # test_configuration_fixture_equals_canon_except_its_thresholds_binding.
    data = _load(instance_path)
    dropped = 0
    for path in _object_paths(data):
        if _is_center_map_weights(path):
            continue
        for key in list(_get(data, path)):
            mutated = copy.deepcopy(data)
            del _get(mutated, path)[key]
            assert not _accepts(schema_path, mutated), path + (key,)
            dropped += 1
    assert dropped


@pytest.mark.parametrize("schema_path,instance_path", INSTANCES)
@pytest.mark.parametrize("wrong_type", [True, False, 1.0, "1"])
def test_every_integer_position_refuses_coercible_types(schema_path: str, instance_path: str, wrong_type: object) -> None:
    data = _load(instance_path)
    paths = list(_integer_paths(data))
    if instance_path != CENTERS_CATALOG:
        assert paths
    for path in paths:
        mutated = copy.deepcopy(data)
        _set(mutated, path, wrong_type)
        assert not _accepts(schema_path, mutated), path


# --- T-06 and T-07: thresholds v2 --------------------------------------------------------

def test_thresholds_fixture_holds_one_ascending_maxima_set_per_category() -> None:
    data = _load(THRESHOLDS_FIXTURE)
    assert _accepts(THRESHOLDS_SCHEMA, data)
    assert set(data) == {"categories", "version"}
    assert data["version"] == "2"
    assert [row["category_id"] for row in data["categories"]] == EXPECTED_CATEGORIES
    for row in data["categories"]:
        maxima = row["maxima"]
        assert maxima == FIXTURE_MAXIMA
        assert maxima[-1] == 100
        assert all(lower < upper for lower, upper in zip(maxima, maxima[1:]))


def _duplicate_category_over_next(data: dict) -> None:
    data["categories"][1] = {"category_id": "harmony", "maxima": [20, 40, 60, 100]}


THRESHOLD_MUTATIONS = {
    "version_integer": lambda d: d.__setitem__("version", 2),
    "version_one": lambda d: d.__setitem__("version", "1"),
    "missing_category": lambda d: d["categories"].pop(),
    "duplicate_category_hides_missing": _duplicate_category_over_next,
    "unknown_category": lambda d: d["categories"][0].__setitem__("category_id", "romance"),
    "three_maxima": lambda d: d["categories"][0].__setitem__("maxima", [24, 49, 74]),
    "five_maxima": lambda d: d["categories"][0].__setitem__("maxima", [24, 49, 74, 99, 100]),
    "last_not_100": lambda d: d["categories"][0].__setitem__("maxima", [24, 49, 74, 99]),
    "element_over_100": lambda d: d["categories"][0].__setitem__("maxima", [24, 49, 101, 100]),
    "element_negative": lambda d: d["categories"][0].__setitem__("maxima", [-1, 49, 74, 100]),
    "v1_layout": lambda d: d.update({"clamp": [0, 100], "edges": [24, 49, 74, 100], "rounding": "ROUND_HALF_UP"}),
}


@pytest.mark.parametrize("name", sorted(THRESHOLD_MUTATIONS))
def test_thresholds_mutations_are_refused(name: str) -> None:
    data = copy.deepcopy(_load(THRESHOLDS_FIXTURE))
    THRESHOLD_MUTATIONS[name](data)
    assert not _accepts(THRESHOLDS_SCHEMA, data)


# --- T-08 and T-09: the v2 configuration ---------------------------------------------------

def test_configuration_fixture_equals_canon_except_its_thresholds_binding() -> None:
    fixture = _load(CONFIG_FIXTURE)
    assert _accepts(CONFIG_SCHEMA, fixture)
    assert fixture == _expected_config()
    assert "category_weights" not in fixture
    assert sum(fixture["blend"].values()) == 100
    thresholds = fixture["sources"]["thresholds"]
    assert thresholds["path"] == "math/thresholds.json"
    assert thresholds["sha256"] == _sha256(THRESHOLDS_FIXTURE)
    assert thresholds["sha256"] != _sha256("math/thresholds.json")


def test_configuration_schema_closed_member_set_has_no_category_weights() -> None:
    schema = _load(CONFIG_SCHEMA)
    members = {
        "blend", "center_map", "center_profiles", "config_id", "profiles", "response_scale", "result_schema",
        "rounding", "saturation_k_bp", "schema", "signal_scale", "signals", "sources",
    }
    assert set(schema["properties"]) == members
    assert set(schema["required"]) == members
    assert schema["additionalProperties"] is False


def _ordinary_with_seven_channels(data: dict) -> None:
    data["signals"][0]["channels"] = [{"channel_id": c, "weight": 1} for c in _channel_ids()[:7]]


def _duplicate_category_row_over_next(data: dict) -> None:
    data["center_map"][1] = copy.deepcopy(data["center_map"][0])
    data["center_map"][1]["weights"] = {"g": 1}


def _duplicate_signal_row_over_next(data: dict) -> None:
    data["signals"][1] = copy.deepcopy(data["signals"][0])
    data["signals"][1]["channels"][0]["weight"] = 2


def _duplicate_center_profile(data: dict) -> None:
    data["center_profiles"][1] = copy.deepcopy(data["center_profiles"][0])
    data["center_profiles"][1]["responses"]["mutual"] = 9000


def _row(index: int, key: str, value: object):
    return lambda d, i=index, k=key, v=value: d["center_map"][i].__setitem__(k, v)


CONFIG_MUTATIONS = {
    "category_weights_added": lambda d: d.__setitem__("category_weights", copy.deepcopy(_load(V1_CONFIG)["category_weights"])),
    "schema_v1": lambda d: d.__setitem__("schema", "magic10_mechanics_config.v1"),
    "result_schema_v1": lambda d: d.__setitem__("result_schema", "magic10_result.v1"),
    "config_id_empty": lambda d: d.__setitem__("config_id", ""),
    "signal_scale_v1": lambda d: d.__setitem__("signal_scale", 2),
    "response_scale_wrong": lambda d: d.__setitem__("response_scale", 1),
    "rounding_signal_v1": lambda d: d["rounding"].__setitem__("signal", "round_half_up_to_half_score_unit"),
    "rounding_component_v1": lambda d: d["rounding"].__setitem__("component", "round_half_up_to_half_score_unit"),
    "rounding_category_wrong": lambda d: d["rounding"].__setitem__("category", "round_half_up_to_per_mille"),
    "saturation_zero": lambda d: d.__setitem__("saturation_k_bp", 0),
    "saturation_negative": lambda d: d.__setitem__("saturation_k_bp", -1),
    "blend_channel_negative": lambda d: d["blend"].__setitem__("channel", -1),
    "blend_center_over_100": lambda d: d["blend"].__setitem__("center", 101),
    "blend_type_over_100": lambda d: d["blend"].__setitem__("type", 101),
    "center_weight_zero": lambda d: d["center_map"][0]["weights"].__setitem__("g", 0),
    "center_weight_four": lambda d: d["center_map"][0]["weights"].__setitem__("g", 4),
    "center_key_unknown": lambda d: d["center_map"][0]["weights"].__setitem__("motor_heart", 1),
    "mapped_row_without_weights": _row(0, "weights", {}),
    "mapped_row_bilateral_profile": _row(0, "profile_id", "bilateral_completion_v2"),
    "mapped_row_unknown_profile": _row(0, "profile_id", "completion_bp_v1"),
    "balance_row_with_weight": _row(9, "weights", {"g": 1}),
    "balance_row_completion_profile": _row(9, "profile_id", "completion_bp_v2"),
    "duplicate_category_row_hides_missing": _duplicate_category_row_over_next,
    "center_response_over": lambda d: d["center_profiles"][0]["responses"].__setitem__("mutual", 10001),
    "center_response_negative": lambda d: d["center_profiles"][0]["responses"].__setitem__("shared", -1),
    "center_open_nonzero": lambda d: d["center_profiles"][1]["responses"].__setitem__("open", 1),
    "center_profile_unknown": lambda d: d["center_profiles"][0].__setitem__("profile_id", "activation_bp_v1"),
    "duplicate_center_profile": _duplicate_center_profile,
    "v1_profile_none_nonzero": lambda d: d["profiles"][0]["responses"].__setitem__("none", 1),
    "v1_profile_missing": lambda d: d["profiles"].pop(),
    "ordinary_operation_v1": lambda d: d["signals"][0].__setitem__("operation", "weighted_state_sum_v1"),
    "ordinary_profile_unknown": lambda d: d["signals"][0].__setitem__("profile_id", "completion_bp_v2"),
    "ordinary_weight_zero": lambda d: d["signals"][0]["channels"][0].__setitem__("weight", 0),
    "ordinary_weight_four": lambda d: d["signals"][0]["channels"][0].__setitem__("weight", 4),
    "ordinary_seven_channels": _ordinary_with_seven_channels,
    "ordinary_no_channels": lambda d: d["signals"][0].__setitem__("channels", []),
    "ordinary_unknown_channel": lambda d: d["signals"][0]["channels"][0].__setitem__("channel_id", "65-66"),
    "ordinary_repeated_channel": lambda d: d["signals"][0]["channels"].__setitem__(1, copy.deepcopy(d["signals"][0]["channels"][0])),
    "equilibrium_operation_v1": lambda d: d["signals"][18].__setitem__("operation", "twice_min_owner_mass_v1"),
    "counterweight_operation_v1": lambda d: d["signals"][19].__setitem__("operation", "companionship_em_mass_v1"),
    "balance_signal_35_channels": lambda d: d["signals"][18]["channels"].pop(),
    "balance_signal_weight_two": lambda d: d["signals"][19]["channels"][0].__setitem__("weight", 2),
    "balance_signal_with_profile": lambda d: d["signals"][18].__setitem__("profile_id", "coherence_bp_v1"),
    "duplicate_signal_row_hides_missing": _duplicate_signal_row_over_next,
    "source_path_changed": lambda d: d["sources"]["centers"].__setitem__("path", "catalog/centers.json"),
    "source_sha256_upper_case": lambda d: d["sources"]["type_pairing"].__setitem__(
        "sha256", d["sources"]["type_pairing"]["sha256"].upper()),
    "source_sha256_short": lambda d: d["sources"]["caps"].__setitem__("sha256", d["sources"]["caps"]["sha256"][:63]),
}


@pytest.mark.parametrize("name", sorted(CONFIG_MUTATIONS))
def test_configuration_mutations_are_refused(name: str) -> None:
    data = copy.deepcopy(_load(CONFIG_FIXTURE))
    CONFIG_MUTATIONS[name](data)
    assert data != _load(CONFIG_FIXTURE)
    assert not _accepts(CONFIG_SCHEMA, data)


# --- T-10: v2 result schemas ---------------------------------------------------------------

RESULT_PAIRS = [
    ("schemas/magic10_result_v1.schema.json", RESULT_SCHEMA, "magic10_result.v2"),
    ("schemas/magic10_compat_result_v1.schema.json", COMPAT_RESULT_SCHEMA, "magic10_compat_result.v2"),
]


@pytest.mark.parametrize("v1_path,v2_path,identity", RESULT_PAIRS)
def test_v2_result_schema_is_the_v1_shape_with_q_widened(v1_path: str, v2_path: str, identity: str) -> None:
    v1 = _load(v1_path)
    reverted = copy.deepcopy(_load(v2_path))
    assert reverted["$id"] == v2_path
    reverted["$id"] = v1["$id"]
    assert reverted["title"] == Path(v2_path).name.removesuffix(".schema.json")
    reverted["title"] = v1["title"]
    assert reverted["properties"]["schema"]["const"] == identity
    reverted["properties"]["schema"]["const"] = v1["properties"]["schema"]["const"]
    q = reverted["properties"]["signals"]["items"]["properties"]["q"]
    assert q == {"maximum": 1000, "minimum": 0, "type": "integer"}
    q["maximum"] = 200
    assert reverted == v1


def _complete_result(identity: str, q: object) -> dict:
    compat = identity.startswith("magic10_compat_result")
    categories = []
    for category in EXPECTED_CATEGORIES:
        row = {"category_id": category, "score": 50, "band": "Warm"}
        if compat:
            row.update(shared_key=f"shared.{category}", personal_lo_to_hi_key=f"lo.{category}",
                       personal_hi_to_lo_key=f"hi.{category}")
        categories.append(row)
    signals = [{"signal_id": row["signal_id"], "q": 0} for row in _load(V1_CONFIG)["signals"]]
    signals[0]["q"] = q
    return {"schema": identity, "config_id": V2_CONFIG_ID, "release_id": "a" * 64, "pair_key": "b" * 64,
            "signals": signals, "categories": categories}


@pytest.mark.parametrize("v1_path,v2_path,identity", RESULT_PAIRS)
@pytest.mark.parametrize("q", [0, 1000])
def test_v2_result_schemas_accept_q_from_0_to_1000(v1_path: str, v2_path: str, identity: str, q: int) -> None:
    assert _accepts(v2_path, _complete_result(identity, q))


@pytest.mark.parametrize("v1_path,v2_path,identity", RESULT_PAIRS)
@pytest.mark.parametrize("q", [1001, -1, True, 1000.0, "5"])
def test_v2_result_schemas_refuse_q_outside_0_to_1000(v1_path: str, v2_path: str, identity: str, q: object) -> None:
    assert not _accepts(v2_path, _complete_result(identity, q))


@pytest.mark.parametrize("v1_path,v2_path,identity", RESULT_PAIRS)
def test_v2_result_schemas_refuse_the_v1_identity(v1_path: str, v2_path: str, identity: str) -> None:
    v1_identity = _load(v1_path)["properties"]["schema"]["const"]
    assert not _accepts(v2_path, _complete_result(v1_identity, 0))


# --- T-11: INV-4 guard -----------------------------------------------------------------------

def test_no_v2_thresholds_or_configuration_is_governed_data_before_the_cut() -> None:
    """INV-4 (HDE-EPIC042 Plan v1.1 §4): no maxima value is canon before the Magic-10 v2 cut.

    This guard fails by design once HDE-DIST008.2 writes the cut thresholds to
    math/thresholds.json and the configuration to catalog/magic10_mechanics_v2.json;
    that row retires it.
    """
    assert not (ROOT / "catalog/magic10_mechanics_v2.json").exists()
    assert _load("math/thresholds.json")["version"] == "1"
    offenders = []
    for base in ("catalog", "math"):
        for path in sorted((ROOT / base).rglob("*.json")):
            data = json.loads(path.read_bytes())
            if isinstance(data, dict) and (
                data.get("version") == "2" or data.get("schema") == "magic10_mechanics_config.v2"
            ):
                offenders.append(path.relative_to(ROOT).as_posix())
    assert offenders == []


# --- T-12: the label ---------------------------------------------------------------------------

def test_fixture_family_is_labelled_non_canon() -> None:
    names = sorted(path.name for path in (ROOT / FIXTURES).iterdir())
    assert names == ["LABEL.txt", "magic10_mechanics_v2.fixture.json", "thresholds_v2.fixture.json"]
    raw = (ROOT / LABEL_FILE).read_bytes()
    assert raw.endswith(b"\n") and not raw.endswith(b"\n\n") and b"\r" not in raw
    assert tuple(raw.decode("ascii").splitlines()) == EXPECTED_LABEL_LINES
