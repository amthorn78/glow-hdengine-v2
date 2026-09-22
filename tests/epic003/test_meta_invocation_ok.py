"""Identity of the complete internal result is the admitted bundle's, not a caller tag."""
import pytest

from engine.bodygraph.resolver import ResolvedCompatChart
from engine.compat.compute import conjunction_public, evaluate_pair, evaluation_party
from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, build_bundle, build_pack, complete_chart, inject_seams


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-meta-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-meta-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)


def test_result_identity_comes_from_the_admitted_bundle(bundle):
    a = evaluation_party(ResolvedCompatChart(UUID_A, complete_chart(UUID_A, GATES_A), "resolved", None, None, None, None))
    b = evaluation_party(ResolvedCompatChart(UUID_B, complete_chart(UUID_B, GATES_B), "resolved", None, None, None, None))
    out = evaluate_pair(a, b)
    # No caller-supplied meta block: release and configuration identity are the bundle's.
    assert "meta" not in out
    assert out["release_id"] == bundle.release_id
    assert out["config_id"] == bundle.mechanics["config_id"]
    wrapped = conjunction_public(a, b, engine_tag="engX", release_id="relY", invocation_tag="INV-TEST")
    assert wrapped["conjunction"]["compat"]["release_id"] == bundle.release_id
    assert "relY" not in str(wrapped) and "engX" not in str(wrapped)
