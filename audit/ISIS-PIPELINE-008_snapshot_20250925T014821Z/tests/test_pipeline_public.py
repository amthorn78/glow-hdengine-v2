
from core.pipeline.compute import compute_pair

def _assert_no_public_numerics(d):
    assert "_admin_debug" not in d
    assert isinstance(d["eligible"], bool)
    assert isinstance(d["bands"], list) and all(isinstance(x, str) for x in d["bands"])
    assert isinstance(d["flags"], list) and all(isinstance(x, str) for x in d["flags"])
    assert isinstance(d["versions"], dict) and all(isinstance(v, str) for v in d["versions"].values())
    assert isinstance(d["idempotence_hash"], str) and len(d["idempotence_hash"]) == 64
    assert (isinstance(d["prompt"], str) or d["prompt"] is None)
    assert isinstance(d["uncertainty"], str)

def test_public_schema_and_no_numeric_leak():
    out = compute_pair({"gates":[1,2,3]}, {"gates":[4,5,6]}, debug=False)
    required = {"bands","eligible","prompt","uncertainty","flags","versions","idempotence_hash"}
    assert required.issubset(out.keys())
    _assert_no_public_numerics(out)

def test_public_has_required_keys():
    out = compute_pair({"gates":[1,2,3]}, {"gates":[4,5,6]}, debug=False)
    required = {"bands","eligible","prompt","uncertainty","flags","versions","idempotence_hash"}
    assert required.issubset(out.keys())
    assert "_admin_debug" not in out


def test_debug_does_not_change_hash():
    from core.pipeline.compute import compute_pair
    a={"gates":[1,2,3]}; b={"gates":[4,5,6]}
    outA = compute_pair(a,b, debug=False)
    outB = compute_pair(a,b, debug=True)
    assert outA["idempotence_hash"] == outB["idempotence_hash"]
