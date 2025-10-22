import json, hashlib, pathlib, pytest, jsonschema
from presenter.reader_v1.emitter import emit_reader_v1
from engine.stable.sercanon import serialize

SCHEMA = json.loads(pathlib.Path("schemas/reader.v1.schema.json").read_text(encoding="utf-8"))

def _hex64(ch: str) -> str: return ch * 64

def _enriched(categories):
    return {
        "eligible": True,
        "categories": categories,
        "meta": {"engine_tag":"Isis5","invocation_tag":"INV-abc123"},
        "release_id": _hex64("a"),
    }

def _sha256(b: bytes) -> str: return hashlib.sha256(b).hexdigest()

def test_determinism_hash_lf_and_schema():
    # Same logical input, categories in different order → same bytes
    catA = [{"id":"cool_leader","band":"Cool"},{"id":"open_leader","band":"Open"}]
    catB = list(reversed(catA))

    b1, env1 = emit_reader_v1(_enriched(catA))
    b2, env2 = emit_reader_v1(_enriched(catB))

    # 1) determinism: two-run identity and order-insensitivity for categories
    assert b1 == b2
    # 2) LF: exactly one trailing newline
    assert b1.endswith(b"\n")
    assert b1.count(b"\n") == 1
    # 3) preimage hash coupling: hash equals sha256(sercanon(preimage))
    env = json.loads(b1.decode("utf-8"))
    pre = dict(env); pre.pop("idempotence_hash", None)
    pre_bytes = serialize(pre)
    assert env["idempotence_hash"] == _sha256(pre_bytes)
    # 4) schema valid
    jsonschema.validate(instance=env, schema=SCHEMA)

def test_duplicate_category_ids_fail():
    cats = [{"id":"cool_leader","band":"Cool"}, {"id":"cool_leader","band":"Cool"}]
    with pytest.raises(ValueError):
        emit_reader_v1(_enriched(cats))
