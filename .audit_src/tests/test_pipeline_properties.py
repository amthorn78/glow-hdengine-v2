# 5C — AB/BA surface symmetry & public payload hygiene
# Ensure repo root is importable during collection
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
p = str(ROOT)
if p not in sys.path:
    sys.path.insert(0, p)

from core.pipeline.compute import compute_pair  # repo layout uses 'core/'

PUBLIC_KEYS = {"bands", "eligible", "prompt", "uncertainty", "flags", "versions", "idempotence_hash"}

def _is_public_numeric_free(payload: dict) -> bool:
    # Booleans are allowed anywhere; numeric scalars elsewhere are not.
    for _, v in payload.items():
        if isinstance(v, bool):
            continue
        if isinstance(v, (int, float)):
            return False
    return "_admin_debug" not in payload

def test_ab_ba_symmetry_surface():
    a = {"gates": [1, 2, 3]}
    b = {"gates": [4, 5, 6]}

    ab = compute_pair(a, b, debug=False)
    ba = compute_pair(b, a, debug=False)

    # Contract keys identical on both sides
    assert set(ab.keys()) == set(ba.keys())
    # Must include at least the public keys we expose
    assert PUBLIC_KEYS.issubset(ab.keys())

    # Shape & hygiene checks on both sides
    for side in (ab, ba):
        assert isinstance(side["bands"], list)
        assert side["uncertainty"] in ("low", "medium", "high")
        assert isinstance(side["eligible"], bool)
        assert _is_public_numeric_free(side)
