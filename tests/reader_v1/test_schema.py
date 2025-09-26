import json, pathlib, pytest
import jsonschema

SCHEMA_PATH = pathlib.Path("schemas/reader.v1.schema.json")
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

def _validate(doc):
    jsonschema.validate(instance=doc, schema=SCHEMA)

def _hex64(ch: str) -> str:
    return ch * 64

def test_success_minimal_shape_valid():
    doc = {
        "reader_version": "v1",
        "eligible": False,
        "categories": [],
        "meta": {"engine_tag":"Isis5","invocation_tag":"INV-abc123"},
        "release_id": _hex64("a"),
        "idempotence_hash": _hex64("b"),
    }
    _validate(doc)

def test_error_shape_valid_with_retry_after_optional():
    err = {
        "ok": False,
        "code": "InvalidInput",
        "error": "bad gates",
        "retry_after_ms": 250
    }
    _validate(err)

def test_prompt_constraints_disallow_crlf_and_over_160():
    good = {
        "reader_version": "v1",
        "eligible": True,
        "categories": [{"id":"open_leader","band":"Open","prompt":"ok"}],
        "meta": {"engine_tag":"Isis5","invocation_tag":"INV-1"},
        "release_id": _hex64("a"),
        "idempotence_hash": _hex64("b"),
    }
    _validate(good)

    bad_nl = {
        **good,
        "categories": [{"id":"open_leader","band":"Open","prompt":"line1\nline2"}]
    }
    with pytest.raises(jsonschema.ValidationError):
        _validate(bad_nl)

    bad_long = {
        **good,
        "categories": [{"id":"open_leader","band":"Open","prompt":"x"*161}]
    }
    with pytest.raises(jsonschema.ValidationError):
        _validate(bad_long)

def test_additional_properties_closed_everywhere():
    base = {
        "reader_version": "v1",
        "eligible": True,
        "categories": [{"id":"cool_leader","band":"Cool"}],
        "meta": {"engine_tag":"Isis5","invocation_tag":"INV-1"},
        "release_id": _hex64("a"),
        "idempotence_hash": _hex64("b"),
    }
    # Root extra field → reject
    with pytest.raises(jsonschema.ValidationError):
        _validate({**base, "extra": 1})
    # Nested category extra → reject
    with pytest.raises(jsonschema.ValidationError):
        _validate({**base, "categories":[{"id":"cool_leader","band":"Cool","x":1}]})
    # Nested meta extra → reject
    with pytest.raises(jsonschema.ValidationError):
        _validate({**base, "meta":{"engine_tag":"Isis5","invocation_tag":"INV-1","x":1}})
