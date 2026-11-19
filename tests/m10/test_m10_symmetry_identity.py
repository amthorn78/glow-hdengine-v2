import pytest

from engine.bodygraph.gates import normalize_gates
from engine.core import compute_core
from engine.serializer.canon import sercanon
from tests.config.helpers import admit_synthetic_v2_candidate

pytestmark = pytest.mark.epic007


def test_magic10_actual_gate_symmetry_and_two_run_identity(tmp_path):
    # HDE-EPIC043 WU-PR-09: the switched core computes over the admitted v2 candidate bundle.
    bundle = admit_synthetic_v2_candidate(tmp_path)
    a, b = normalize_gates([5, 19, 20, 34, 43, 49]), normalize_gates([9, 12, 15, 22, 23, 52])
    results = [compute_core(x, y, bundle, bundle.release_id) for x, y in ((a, b), (b, a), (a, b))]
    assert results[0] == results[1] == results[2]
    assert len({sercanon(r.as_payload()) for r in results}) == 1
