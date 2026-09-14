import hashlib
import json

import pytest

from engine.bodygraph.gates import normalize_gates
from engine.config.registry_loader import _load_active_mechanics_bundle_from_root
from engine.core import compute_core
from engine.core.core import _chart_fingerprint
from engine.magic10.composite import _classify_channels
from engine.serializer.canon import sercanon
from tests.config.helpers import synthetic_complete_release_root


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return _load_active_mechanics_bundle_from_root(synthetic_complete_release_root(tmp_path_factory.mktemp("abba")))


@pytest.mark.parametrize("a,b", [
    ([5, 19, 20, 34, 43, 49], [9, 12, 15, 22, 23, 52]),
    ([1, 8], [1, 64]), ([1], [1]), (list(range(1, 65)), [1, 64]),
])
def test_complete_abba_and_intrinsic_identity(a, b, bundle):
    a, b = normalize_gates(a), normalize_gates(b)
    ab = compute_core(a, b, bundle, bundle.release_id)
    ba = compute_core(b, a, bundle, bundle.release_id)
    assert ab == ba
    assert sercanon(ab.to_payload()) == sercanon(ba.to_payload())
    assert _classify_channels(a.mask, b.mask, bundle.registry.channels) == _classify_channels(b.mask, a.mask, bundle.registry.channels)
    # Independent preimage construction; no call to core to derive expected data.
    fingerprints = []
    for member in sorted((a, b), key=lambda x: x.mask):
        raw = (json.dumps({"schema": "magic10_chart_fingerprint.v1", "gate_mask_hex": member.mask_hex},
                          sort_keys=True, separators=(",", ":")) + "\n").encode()
        fingerprint = hashlib.sha256(raw).hexdigest()
        assert _chart_fingerprint(member) == fingerprint
        fingerprints.append(fingerprint)
    preimage = {"schema": "magic10_pair_preimage.v1", "members": fingerprints,
                "config_id": bundle.mechanics["config_id"], "release_id": bundle.release_id,
                "result_schema": "magic10_result.v1"}
    raw = (json.dumps(preimage, sort_keys=True, separators=(",", ":")) + "\n").encode()
    assert ab.pair_key == hashlib.sha256(raw).hexdigest()
    if a == b:
        assert len(fingerprints) == 2 and fingerprints[0] == fingerprints[1]


def test_changed_gate_mask_changes_intrinsic_identity(bundle):
    a, b = normalize_gates([1]), normalize_gates([8])
    first = compute_core(a, b, bundle, bundle.release_id)
    changed = compute_core(a, normalize_gates([8, 64]), bundle, bundle.release_id)
    assert first.pair_key != changed.pair_key
    assert _chart_fingerprint(b) != _chart_fingerprint(normalize_gates([8, 64]))
    # Reconstructing equal values carries no person identity or object-ID seed.
    assert compute_core(normalize_gates([1]), normalize_gates([8]), bundle, bundle.release_id) == first


@pytest.mark.parametrize('gates,digest', [
    ([1], '7567338a3be5b35e00366bfe86f3f1ca8b89be1fd02be893abeb62a60dbc2d2b'),
    ([8], '048d5d37621e767fde5a035a5809027cb489168106e3993da3c5db2c89bf51ec'),
    (list(range(1, 65)), '3c98a9bcd9b872cfbf6fc35fde2e420d0b6dfeaf01d59884df3961d88b7a092f'),
])
def test_fixed_chart_fingerprint_oracles(gates, digest):
    assert _chart_fingerprint(normalize_gates(gates)) == digest
