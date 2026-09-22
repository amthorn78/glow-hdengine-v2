"""HDE-EPIC040-PR04: strict raw-Gate ingress and identity binding at the projection seam."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from engine.bodygraph.gates import normalize_gates
from engine.bodygraph.projection import (
    BodyGraphProjectionError,
    accepted_identity_labels,
    bind_projection_identity,
    canonical_uuid,
    is_gate_ingress_code,
    project_bodygraph,
    strict_canonical_uuid,
    validate_raw_gates,
)

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "tests/fixtures/bodygraph/source_invariance/db_cached_payload.v1.json"
UUID_A = "00000000-0000-4000-8000-000000000038"
UUID_HEX = "3fa85f64-5717-4562-b3fc-2c963f66afaa"


def _payload() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))["payload"]


@pytest.mark.parametrize(
    ("gates", "code"),
    [
        ([], "GATES_EMPTY"),
        ([10, "10"], "GATE_DUPLICATE"),
        (["10", "10"], "GATE_DUPLICATE"),
        ([True], "GATE_VALUE_INVALID"),
        (["010"], "GATE_VALUE_INVALID"),
        ([" 10"], "GATE_VALUE_INVALID"),
        (["+10"], "GATE_VALUE_INVALID"),
        ([10.0], "GATE_VALUE_INVALID"),
        ([0], "GATE_VALUE_INVALID"),
        ([65], "GATE_VALUE_INVALID"),
        (["65"], "GATE_VALUE_INVALID"),
        ([None], "GATE_VALUE_INVALID"),
        ("10", "GATES_NOT_LIST"),
        (None, "GATES_NOT_LIST"),
    ],
)
def test_raw_gate_ingress_refuses_before_projection(gates, code):
    payload = _payload()
    payload["bodygraph"]["gates"] = gates
    with pytest.raises(BodyGraphProjectionError) as raised:
        project_bodygraph(payload)
    assert raised.value.code == code
    assert raised.value.field_path == "root.bodygraph.gates"
    assert is_gate_ingress_code(code)
    with pytest.raises(BodyGraphProjectionError) as direct:
        validate_raw_gates(gates)
    assert direct.value.code == code


def test_non_json_gate_container_is_refused_by_shape_then_by_ingress():
    payload = _payload()
    payload["bodygraph"]["gates"] = ("10",)
    with pytest.raises(BodyGraphProjectionError) as raised:
        project_bodygraph(payload)
    assert raised.value.code == "INVALID_SHAPE"
    with pytest.raises(BodyGraphProjectionError) as direct:
        validate_raw_gates(("10",))
    assert direct.value.code == "GATES_NOT_LIST"


def test_missing_gates_field_is_a_missing_field_refusal():
    payload = _payload()
    payload["bodygraph"].pop("gates")
    with pytest.raises(BodyGraphProjectionError) as raised:
        project_bodygraph(payload)
    assert (raised.value.code, raised.value.field_path) == ("MISSING_FIELD", "root.bodygraph.gates")


@pytest.mark.parametrize("gates", [["10", "20", "34"], [34, 10, 20], ["64", 1], list(range(1, 65))])
def test_valid_gates_project_unchanged_and_normalize_after_validation(gates):
    payload = _payload()
    payload["bodygraph"]["gates"] = list(gates)
    projected = project_bodygraph(payload)
    # The projection keeps the exact source spelling; sorting is the evaluator's step.
    assert projected["bodygraph"]["gates"] == list(gates)
    normalized = validate_raw_gates(projected["bodygraph"]["gates"])
    assert normalized == normalize_gates(list(gates))
    assert normalized.gates == tuple(sorted(int(g) for g in gates))


def test_projection_output_keys_and_nonmutation_are_preserved():
    payload = _payload()
    original = copy.deepcopy(payload)
    projected = project_bodygraph(payload)
    assert set(projected) == {"bodygraph", "person", "person_uid"}
    assert payload == original


def test_bind_identity_accepts_uuid_label_and_person_prefixed_label():
    projected = project_bodygraph(_payload())
    bound = bind_projection_identity(projected, UUID_A)
    assert bound["person_uid"] == UUID_A and bound["person"] == {"person_uid": UUID_A}
    prefixed = dict(projected, person_uid=f"person-{UUID_A}", person={"person_uid": f"person-{UUID_A}"})
    assert bind_projection_identity(prefixed, UUID_A)["person_uid"] == UUID_A
    upper = dict(projected, person_uid=UUID_HEX.upper(), person={"person_uid": UUID_HEX.upper()})
    assert bind_projection_identity(upper, UUID_HEX)["person_uid"] == UUID_HEX


def test_bind_identity_accepts_only_trusted_seed_labels():
    projected = project_bodygraph(_payload())
    aliased = dict(projected, person_uid="person-operator", person={"person_uid": "person-operator"})
    labels = accepted_identity_labels(UUID_A, ["operator"])
    assert bind_projection_identity(aliased, UUID_A, accepted_labels=labels)["person_uid"] == UUID_A
    with pytest.raises(BodyGraphProjectionError) as raised:
        bind_projection_identity(aliased, UUID_A)
    assert raised.value.code == "IDENTITY_CONFLICT"


def test_bind_identity_refuses_conflicting_uuid_and_mismatched_slots():
    projected = project_bodygraph(_payload())
    other = "00000000-0000-4000-8000-000000000039"
    with pytest.raises(BodyGraphProjectionError) as raised:
        bind_projection_identity(projected, other)
    assert raised.value.code == "IDENTITY_CONFLICT"
    mismatched = dict(projected, person={"person_uid": other})
    with pytest.raises(BodyGraphProjectionError) as raised:
        bind_projection_identity(mismatched, UUID_A)
    assert raised.value.code == "PERSON_UID_MISMATCH"
    with pytest.raises(BodyGraphProjectionError) as raised:
        bind_projection_identity(projected, "person-" + UUID_A)
    assert raised.value.code == "IDENTITY_INVALID"


@pytest.mark.parametrize(
    ("value", "canonical", "strict"),
    [
        (UUID_A, UUID_A, UUID_A),
        (UUID_HEX, UUID_HEX, UUID_HEX),
        (UUID_HEX.upper(), UUID_HEX, None),
        ("{" + UUID_HEX + "}", UUID_HEX, None),
        (UUID_HEX.replace("-", ""), UUID_HEX, None),
        (" " + UUID_HEX + " ", UUID_HEX, None),
        ("person-" + UUID_A, None, None),
        ("alice", None, None),
        ("", None, None),
        (None, None, None),
        (12, None, None),
    ],
)
def test_uuid_grammar_helpers(value, canonical, strict):
    assert canonical_uuid(value) == canonical
    assert strict_canonical_uuid(value) == strict
