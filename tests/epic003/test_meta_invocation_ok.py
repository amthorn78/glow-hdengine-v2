from engine.compat.compute import compat_public
from engine.compat.categories import CATEGORIES_ORDER_V1
def test_meta_invocation_ok():
    a = {"person_uid":"amy"}; b={"person_uid":"zoe"}
    weights = {k:50 for k in CATEGORIES_ORDER_V1}
    out = compat_public(a,b, CATEGORIES_ORDER_V1[0], weights,
                        engine_tag="engX", release_id="relY", invocation_tag="INV-TEST")
    assert "meta" in out and isinstance(out["meta"], dict)
    m = out["meta"]
    assert m["engine_tag"] == "engX"
    assert m["release_id"] == "relY"
    assert m["invocation_tag"] == "INV-TEST"
    # top-level must NOT carry a separate release_id (we keep it inside meta)
    assert "release_id" not in {k for k in out.keys() if k != "meta"}
