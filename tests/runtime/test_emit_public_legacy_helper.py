"""`engine.emit_public.emit_public_envelope` — the legacy helper's call contract.

The helper is used two ways, and PR04 broke both by making ``eligible`` a required
keyword-only argument of ``emit_reader_public_bytes``: ``VERIFY.sh`` calls it with
five positional arguments, and ``dev/reader_harness/app.py`` injects it as the
Reader blueprint's ``emit_fn``, which the routes call with ``eligible=`` and
``harmony_band=``. Neither shape reaches CI, so these tests own that contract.
"""
from __future__ import annotations

import inspect
import json
from pathlib import Path

import pytest

from adapter import http_reader
from engine.emit_public import emit_public_envelope

FIXTURES = Path("fixtures/charts")


def _charts() -> tuple[dict, dict]:
    a = json.loads((FIXTURES / "alice.json").read_text(encoding="utf-8"))
    b = json.loads((FIXTURES / "bob.json").read_text(encoding="utf-8"))
    return a, b


def test_five_positional_arguments_still_emit_the_ineligible_envelope() -> None:
    """The VERIFY.sh call shape: five positional arguments and no keywords."""

    a, b = _charts()
    body = emit_public_envelope(a, b, "Isis6", "INV-1", "rel_dev")
    payload = json.loads(body)
    assert payload["eligible"] is False
    assert payload["categories"] == []
    assert body.endswith(b"\n")


def test_direct_call_is_two_run_and_ab_ba_byte_identical() -> None:
    a, b = _charts()
    first = emit_public_envelope(a, b, "Isis6", "INV-1", "rel_dev")
    second = emit_public_envelope(a, b, "Isis6", "INV-1", "rel_dev")
    swapped = emit_public_envelope(b, a, "Isis6", "INV-1", "rel_dev")
    assert first == second == swapped


@pytest.mark.parametrize("eligible, band", [(False, None), (True, "Warm")])
def test_it_accepts_and_forwards_the_injected_emit_fn_keywords(eligible: bool, band: str | None) -> None:
    """The dev-harness injection shape: the routes call emit_fn with both keywords."""

    a, b = _charts()
    payload = json.loads(
        emit_public_envelope(a, b, "Isis6", "INV-1", "rel_dev", eligible=eligible, harmony_band=band)
    )
    assert payload["eligible"] is eligible
    assert payload["categories"] == ([{"id": "harmony", "band": band}] if eligible else [])


def test_its_signature_satisfies_the_blueprint_emit_fn_contract() -> None:
    """Whatever the routes pass to emit_fn, this helper must accept."""

    parameters = inspect.signature(emit_public_envelope).parameters
    for required in ("engine_tag", "invocation_tag", "release_id", "eligible", "harmony_band"):
        assert required in parameters, required
    # The blueprint factory takes it as emit_fn, so the injection itself must work.
    assert http_reader.get_reader_bp(emit_public_envelope) is not None
