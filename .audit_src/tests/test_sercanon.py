import math, json
from core.stable.sercanon import (
    stable_normalize, stable_dumps, stable_dumps_str, stable_hash,
    mask_paths, _prune_masked, _drop_empty, DEFAULT_IDEMPOTENCE_MASKS,
    stable_idempotence_hash
)

def test_dict_keys_and_string_nfc():
    x = {"b":"cafe\u0301", "a":"z"}
    n = stable_normalize(x)
    assert list(n.keys()) == ["a","b"]
    # NFC: "café"
    assert n["b"] == "café"

def test_non_finite_float_rejected():
    for v in [math.nan, math.inf, -math.inf]:
        try:
            stable_normalize({"x": v})
        except ValueError:
            pass
        else:
            raise AssertionError("non-finite float must raise")

def test_sets_sorted_by_stable_bytes():
    s = {"b", "a"}
    n = stable_normalize({"s": set(s)})
    assert n["s"] == ["a","b"]

def test_stable_dumps_is_byte_deterministic():
    payload = {"x":[3,2,1], "s":{"b","a"}}
    b1 = stable_dumps(payload)
    b2 = stable_dumps(payload)
    assert b1 == b2
    assert json.loads(b1) == json.loads(b2)

def test_masking_and_idempotence_invariance():
    base = {"data":{"y":2}}
    diag = {"data":{"y":2}, "_diagnostics":{"why":"reason"}}
    trace= {"data":{"y":2}, "meta":{"trace":"t-123"}}
    h0 = stable_idempotence_hash(base)
    h1 = stable_idempotence_hash(diag)
    h2 = stable_idempotence_hash(trace)
    assert h0 == h1 == h2

def test_mask_paths_prune_drop_pipeline():
    obj = {"a":1,"_diagnostics":{"x":1},"meta":{"trace":"id"},"b":[]}
    m = mask_paths(obj, DEFAULT_IDEMPOTENCE_MASKS)
    p = _prune_masked(m); d = _drop_empty(p)
    assert d == {"a":1}
