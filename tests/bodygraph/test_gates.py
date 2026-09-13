from __future__ import annotations

import re
from dataclasses import FrozenInstanceError

import pytest

from engine.bodygraph.gates import (
    GateNormalizationError,
    NormalizedGates,
    normalize_gates,
)


@pytest.mark.parametrize(
    ("value", "gates", "mask", "mask_hex"),
    [
        ([1], (1,), 1, "0000000000000001"),
        ([64], (64,), 1 << 63, "8000000000000000"),
        ([64, "1", 32, "7"], (1, 7, 32, 64), (1 << 0) | (1 << 6) | (1 << 31) | (1 << 63), "8000000080000041"),
        (["10", "2", "64"], (2, 10, 64), (1 << 1) | (1 << 9) | (1 << 63), "8000000000000202"),
    ],
)
def test_normalize_gates_returns_exact_canonical_representation(value, gates, mask, mask_hex) -> None:
    result = normalize_gates(value)
    assert result == NormalizedGates(gates=gates, mask=mask, mask_hex=mask_hex)
    assert re.fullmatch(r"[0-9a-f]{16}", result.mask_hex)


def test_every_gate_has_the_governed_bit_position() -> None:
    for gate in range(1, 65):
        result = normalize_gates([gate])
        assert result.gates == (gate,)
        assert result.mask == 1 << (gate - 1)
        assert result.mask_hex == f"{1 << (gate - 1):016x}"


@pytest.mark.parametrize(
    "value",
    [None, 1, "1", (), (1,), {}, {1: True}, set(), {1}, iter([1]), range(1, 2), b"1", bytearray(b"1")],
)
def test_top_level_must_be_a_built_in_list(value) -> None:
    with pytest.raises(GateNormalizationError) as caught:
        normalize_gates(value)
    assert caught.value.code == "GATES_NOT_LIST"
    assert str(caught.value) == "GATES_NOT_LIST"


def test_list_subclasses_are_not_an_alternate_boundary() -> None:
    class GateList(list):
        pass

    with pytest.raises(GateNormalizationError) as caught:
        normalize_gates(GateList([1]))
    assert caught.value.code == "GATES_NOT_LIST"


def test_empty_list_is_refused() -> None:
    with pytest.raises(GateNormalizationError) as caught:
        normalize_gates([])
    assert caught.value.code == "GATES_EMPTY"


@pytest.mark.parametrize(
    "item",
    [
        True, False, 0, 65, -1, 1.0, 64.0, None, [], {}, (),
        "", "0", "65", "-1", "+1", " 1", "1 ", "01", "001", "1.0",
        "1e0", "0x1", "１", "١", "one", "1\n", b"1",
    ],
)
def test_prohibited_gate_forms_are_refused_without_echoing_input(item) -> None:
    with pytest.raises(GateNormalizationError) as caught:
        normalize_gates([item])
    assert caught.value.code == "GATE_VALUE_INVALID"
    assert str(caught.value) == "GATE_VALUE_INVALID"


@pytest.mark.parametrize("value", [[1, 1], ["1", "1"], [1, "1"], [64, "64"]])
def test_duplicates_are_refused_after_numeric_normalization(value) -> None:
    with pytest.raises(GateNormalizationError) as caught:
        normalize_gates(value)
    assert caught.value.code == "GATE_DUPLICATE"


def test_result_does_not_retain_or_mutate_the_callers_list() -> None:
    source = [3, "1", 2]
    before = list(source)
    result = normalize_gates(source)
    assert source == before
    source[:] = [64]
    assert result.gates == (1, 2, 3)
    assert result.mask == 7


def test_full_uint64_domain_and_frozen_result_without_io(monkeypatch) -> None:
    def refuse_io(*args, **kwargs):
        raise AssertionError("normalization must not perform I/O")

    monkeypatch.setattr("builtins.open", refuse_io)
    monkeypatch.setattr("os.open", refuse_io)
    result = normalize_gates(list(range(64, 0, -1)))
    assert result.gates == tuple(range(1, 65))
    assert result.mask == 2**64 - 1
    assert result.mask_hex == "ffffffffffffffff"
    with pytest.raises(FrozenInstanceError):
        result.mask = 0
    with pytest.raises(TypeError):
        result.gates[0] = 64


def test_numeric_and_text_subclasses_cannot_override_the_boundary() -> None:
    class GateInt(int):
        pass

    class GateString(str):
        pass

    for value in (GateInt(1), GateString("1")):
        with pytest.raises(GateNormalizationError) as caught:
            normalize_gates([value])
        assert caught.value.code == "GATE_VALUE_INVALID"
