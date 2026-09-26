"""schemas/reader.v1.schema.json (F05 conformance, PF10 §2.23) and schemas/reader.v2.schema.json."""
import hashlib, json, pathlib, pytest
import jsonschema

from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.compat.error_tokens import ERROR_TOKEN_MAP
from engine.serializer.canon import sercanon

SCHEMA_PATH = pathlib.Path("schemas/reader.v1.schema.json")
SIDECAR_PATH = pathlib.Path("schemas/reader.v1.schema.json.sha256")
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
SCHEMA_V2_PATH = pathlib.Path("schemas/reader.v2.schema.json")
SIDECAR_V2_PATH = pathlib.Path("schemas/reader.v2.schema.json.sha256")
SCHEMA_V2 = json.loads(SCHEMA_V2_PATH.read_text(encoding="utf-8"))
BANDS = ["Cool", "Open", "Warm", "Glow"]
V1_DEV_ROUTE_ERROR_PAIRS = [
    # dev GET /reader only (PF05 §5.2.4.1.4 tokens the production POST route never emits)
    ("ERR_READER_FORBIDDEN", "reader endpoint disabled"),
    ("ERR_READER_MISSING_PARAM", "missing required reader parameters"),
    ("ERR_READER_INVALID_PATH", "invalid chart path"),
    ("ERR_READER_MISSING_TZ_A", "missing tz for party A"),
    ("ERR_READER_MISSING_TZ_B", "missing tz for party B"),
]
V2_ERROR_PAIRS = [
    ("ERR_READER_INVALID_VERSION", "unsupported reader version"),
    ("ERR_READER_INVALID_INPUT", "invalid Reader request"),
    ("ERR_READER_INVALID_CHART", "invalid reader payload"),
    ("ERR_M10_PERSON_UNRESOLVED", "BodyGraph not found"),
    ("ERR_M10_RESOLVER_UNAVAILABLE", "BodyGraph resolver unavailable"),
    ("ERR_M10_BODYGRAPH_INCOMPLETE", "BodyGraph is incomplete"),
    ("ERR_M10_LEGACY_INPUT_UNSUPPORTED", "legacy scoring input is unsupported"),
    ("ERR_M10_CONFIG_MISMATCH", "Magic10 configuration mismatch"),
    ("ERR_M10_MANIFEST_MISMATCH", "Magic10 release manifest mismatch"),
    ("ERR_M10_RESULT_SCHEMA_MISMATCH", "Magic10 result schema mismatch"),
    ("ERR_M10_STALE_RESULT", "Magic10 cached result is stale"),
    ("ERR_NOT_FOUND", "not found"),
]
# PF10 §2.24 (C040-08, alternative A): the v1 error branch admits every governed pair either
# Reader v1 route can emit -- the production route's twelve (shared with v2) plus the dev route's five.
V1_ERROR_PAIRS = V2_ERROR_PAIRS + V1_DEV_ROUTE_ERROR_PAIRS


def _validate(doc):
    jsonschema.Draft202012Validator(SCHEMA).validate(doc)


def _validate_v2(doc):
    jsonschema.Draft202012Validator(SCHEMA_V2).validate(doc)


def _hex64(ch: str) -> str:
    return ch * 64


def _success_v1(eligible=True, categories=None):
    return {
        "reader_version": "v1",
        "eligible": eligible,
        "categories": [{"id": "harmony", "band": "Open"}] if categories is None else categories,
        "meta": {"engine_tag": "Isis5", "invocation_tag": "INV-abc123"},
        "release_id": _hex64("a"),
        "idempotence_hash": _hex64("b"),
    }


def _ten(bands=None):
    bands = bands or [BANDS[i % 4] for i in range(10)]
    return [{"id": cid, "band": band} for cid, band in zip(FROZEN_MAGIC10_ORDER, bands)]


def _success_v2(eligible=True, categories=None):
    return {
        "reader_version": "v2",
        "eligible": eligible,
        "categories": _ten() if categories is None else categories,
        "meta": {"engine_tag": "Isis5", "invocation_tag": "INV-abc123"},
        "release_id": _hex64("a"),
        "idempotence_hash": _hex64("b"),
    }


def _error_v2(code="ERR_READER_INVALID_VERSION", message="unsupported reader version"):
    return {"schema": "v1", "ok": False, "code": code, "error": message}


def _error_v1(code="ERR_READER_INVALID_INPUT", message="invalid Reader request"):
    return {"schema": "v1", "ok": False, "code": code, "error": message}


# --- Reader v1 --------------------------------------------------------------------------------------

def test_success_minimal_shape_valid():
    _validate(_success_v1(eligible=False, categories=[]))


@pytest.mark.parametrize("band", BANDS)
def test_success_harmony_item_valid_for_every_band(band):
    _validate(_success_v1(categories=[{"id": "harmony", "band": band}]))


@pytest.mark.parametrize(("code", "message"), V1_ERROR_PAIRS)
def test_v1_error_pairs_valid_and_bound_to_the_token_map(code, message):
    _validate(_error_v1(code, message))
    assert ERROR_TOKEN_MAP[code]["message"] == message


def test_v1_error_branch_is_exactly_the_reader_route_pairs():
    pairs = [(o["properties"]["code"]["const"], o["properties"]["error"]["const"]) for o in SCHEMA["$defs"]["error"]["oneOf"]]
    assert pairs == V1_ERROR_PAIRS and len(pairs) == 17
    assert SCHEMA["$defs"]["error"]["required"] == ["schema", "ok", "code", "error"]
    assert SCHEMA["$defs"]["error"]["additionalProperties"] is False
    assert set(SCHEMA["$defs"]["error"]["properties"]) == {"schema", "ok", "code", "error"}
    assert SCHEMA["$defs"]["error"]["properties"]["schema"] == {"const": "v1"}
    # the production route's pairs are the v2 branch's pairs
    v2_pairs = [(o["properties"]["code"]["const"], o["properties"]["error"]["const"]) for o in SCHEMA_V2["$defs"]["error"]["oneOf"]]
    assert pairs[: len(v2_pairs)] == v2_pairs


@pytest.mark.parametrize(
    "doc",
    [
        {k: v for k, v in _error_v1().items() if k != "schema"},
        {**_error_v1(), "schema": "v2"},
        {**_error_v1(), "schema": "V1"},
        _error_v1("ERR_WRITER_INVALID_INPUT", "schema validation failed"),
        _error_v1("ERR_M10_GATES_INVALID", "Gate data is invalid"),
        _error_v1("ERR_READER_INVALID_INPUT", "not found"),
        {"ok": False, "code": "InvalidInput", "error": "bad gates"},
        {**_error_v1(), "retry_after_ms": 250},
        {**_error_v1(), "details": {}},
        {**_error_v1(), "ok": True},
        {k: v for k, v in _error_v1().items() if k != "error"},
    ],
    ids=["no_schema", "wrong_schema_const", "schema_case", "ungoverned_writer_code", "internal_only_code", "wrong_message", "synthetic_legacy_golden", "retry_after_ms", "details", "ok_true", "missing_error"],
)
def test_v1_error_adverse_cases_invalid(doc):
    with pytest.raises(jsonschema.ValidationError):
        _validate(doc)


@pytest.mark.parametrize(
    "categories",
    [
        [{"id": "open_leader", "band": "Open"}],
        [{"id": "harmony", "band": "Open", "prompt": "ok"}],
        [{"id": "harmony", "band": "Open", "prompt": None}],
        [{"id": "harmony", "band": "Hot"}],
        [{"id": "heat", "band": "Open"}],
        [{"id": "harmony", "band": "Open"}, {"id": "harmony", "band": "Cool"}],
        [],
    ],
    ids=["leader_id", "prompt", "prompt_null", "unknown_band", "non_harmony_id", "two_items", "eligible_empty"],
)
def test_success_categories_are_exactly_one_harmony_item_when_eligible(categories):
    with pytest.raises(jsonschema.ValidationError):
        _validate(_success_v1(categories=categories))


def test_ineligible_with_an_item_is_invalid():
    with pytest.raises(jsonschema.ValidationError):
        _validate(_success_v1(eligible=False, categories=[{"id": "harmony", "band": "Open"}]))


def test_additional_properties_closed_everywhere():
    base = _success_v1()
    # Root extra field → reject
    with pytest.raises(jsonschema.ValidationError):
        _validate({**base, "extra": 1})
    # A success carrying an error-branch key → reject
    with pytest.raises(jsonschema.ValidationError):
        _validate({**base, "retry_after_ms": 250})
    with pytest.raises(jsonschema.ValidationError):
        _validate({**base, "ok": False})
    # Nested category extra → reject
    with pytest.raises(jsonschema.ValidationError):
        _validate({**base, "categories": [{"id": "harmony", "band": "Cool", "x": 1}]})
    # Nested meta extra → reject
    with pytest.raises(jsonschema.ValidationError):
        _validate({**base, "meta": {"engine_tag": "Isis5", "invocation_tag": "INV-1", "x": 1}})
    # Error extra → reject
    with pytest.raises(jsonschema.ValidationError):
        _validate({**_error_v1(), "details": {}})


def test_v1_schema_identity_and_canonical_bytes():
    assert SCHEMA["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert SCHEMA["$id"] == "https://example.org/schemas/reader.v1.schema.json"
    assert SCHEMA["$defs"]["category_id"]["enum"] == ["harmony"]
    assert set(SCHEMA["$defs"]["category"]["properties"]) == {"id", "band"}
    raw = SCHEMA_PATH.read_bytes()
    assert sercanon(json.loads(raw), sort_keys=True) == raw


def test_digest_sidecar_binds_the_schema_bytes():
    # sha256sum format: "<hex64>  schemas/reader.v1.schema.json\n", one line, LF-terminated.
    sidecar = SIDECAR_PATH.read_text(encoding="utf-8")
    assert sidecar.endswith("\n") and sidecar.count("\n") == 1
    digest, separator, name = sidecar[:-1].partition("  ")
    assert separator == "  "
    assert name == SCHEMA_PATH.as_posix()
    assert digest == hashlib.sha256(SCHEMA_PATH.read_bytes()).hexdigest()


# --- Reader v2 --------------------------------------------------------------------------------------

def test_v2_success_ten_in_order_valid_and_ineligible_valid():
    _validate_v2(_success_v2())
    _validate_v2(_success_v2(categories=_ten(["Glow"] * 10)))
    _validate_v2(_success_v2(eligible=False, categories=[]))


@pytest.mark.parametrize(
    "mutate",
    [
        lambda doc: doc.update(categories=list(reversed(doc["categories"]))),
        lambda doc: doc.update(categories=doc["categories"][:9]),
        lambda doc: doc.update(categories=doc["categories"] + [{"id": "balance", "band": "Cool"}]),
        lambda doc: doc["categories"][0].update(prompt="x"),
        lambda doc: doc["categories"][1].update(band="Hot"),
        lambda doc: doc["categories"][2].update(score=3),
        lambda doc: doc.update(categories=[]),
        lambda doc: doc.update(eligible=False),
        lambda doc: doc.update(reader_version="v1"),
        lambda doc: doc.update(extra=1),
        lambda doc: doc["meta"].update(x=1),
        lambda doc: doc.update(idempotence_hash="z" * 64),
        lambda doc: doc.pop("release_id"),
    ],
    ids=["wrong_order", "nine", "eleven", "prompt", "unknown_band", "score", "eligible_empty", "ineligible_with_items", "v1_tag", "root_extra", "meta_extra", "bad_hash", "missing_release_id"],
)
def test_v2_success_adverse_cases_invalid(mutate):
    doc = _success_v2()
    mutate(doc)
    with pytest.raises(jsonschema.ValidationError):
        _validate_v2(doc)


def test_v2_categories_are_the_canonical_order_by_construction():
    prefix = SCHEMA_V2["$defs"]["categories_eligible"]["prefixItems"]
    assert [item["properties"]["id"]["const"] for item in prefix] == list(FROZEN_MAGIC10_ORDER)
    assert SCHEMA_V2["$defs"]["categories_eligible"]["items"] is False
    assert SCHEMA_V2["$defs"]["categories_eligible"]["minItems"] == 10 == SCHEMA_V2["$defs"]["categories_eligible"]["maxItems"]


@pytest.mark.parametrize(("code", "message"), V2_ERROR_PAIRS)
def test_v2_error_pairs_valid_and_bound_to_the_token_map(code, message):
    _validate_v2(_error_v2(code, message))
    assert ERROR_TOKEN_MAP[code]["message"] == message


def test_v2_error_adverse_cases_invalid():
    with pytest.raises(jsonschema.ValidationError):
        _validate_v2(_error_v2("ERR_READER_INVALID_VERSION", "not found"))
    with pytest.raises(jsonschema.ValidationError):
        _validate_v2(_error_v2("ERR_WRITER_INVALID_INPUT", "invalid input"))
    with pytest.raises(jsonschema.ValidationError):
        _validate_v2({**_error_v2(), "details": {}})
    with pytest.raises(jsonschema.ValidationError):
        _validate_v2({**_error_v2(), "retry_after_ms": 1})
    with pytest.raises(jsonschema.ValidationError):
        _validate_v2({k: v for k, v in _error_v2().items() if k != "schema"})
    with pytest.raises(jsonschema.ValidationError):
        _validate_v2({**_error_v2(), "schema": "v2"})
    with pytest.raises(jsonschema.ValidationError):
        _validate_v2({**_error_v2(), "ok": True})


def test_v2_schema_identity_canonical_bytes_and_sidecar():
    assert SCHEMA_V2["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert SCHEMA_V2["$id"] == "https://example.org/schemas/reader.v2.schema.json"
    assert SCHEMA_V2["title"] == "Reader v2 — public envelope (success | error)"
    assert SCHEMA_V2["oneOf"] == [{"$ref": "#/$defs/success"}, {"$ref": "#/$defs/error"}]
    assert len(SCHEMA_V2["$defs"]["error"]["oneOf"]) == 12
    raw = SCHEMA_V2_PATH.read_bytes()
    assert sercanon(json.loads(raw), sort_keys=True) == raw
    sidecar = SIDECAR_V2_PATH.read_text(encoding="utf-8")
    assert sidecar.endswith("\n") and sidecar.count("\n") == 1
    digest, separator, name = sidecar[:-1].partition("  ")
    assert separator == "  " and name == SCHEMA_V2_PATH.as_posix()
    assert digest == hashlib.sha256(raw).hexdigest()
