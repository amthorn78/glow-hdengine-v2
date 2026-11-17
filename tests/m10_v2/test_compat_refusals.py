"""HDE-EPIC043 WU-PR-03: the dormant layer's refusals (HDE-CONJ010.4).

Each refusal the work unit's instruction requires, shown once:

* a ``release_id`` that is not a lowercase 64-character hexadecimal digest is
  refused by the calculation (``M10V2_CALC_RELEASE_ID_INVALID``), propagated
  unchanged and never echoed; the layer adds no second rule;
* a narrative key that is missing, or two ``shared_key`` values that disagree,
  is refused (``M10V2_COMPAT_NARRATIVE_KEY_INVALID``). The governed pack answers
  every category, band and direction, so this is shown through the ``router``
  seam, the same seam ``evaluate_pair`` exposes and v1's equivalent test uses;
* a Reader version the existing projection function refuses becomes
  ``M10V2_COMPAT_PROJECTION_REFUSED`` with that function's reason.

A compat value that does not validate (``M10V2_COMPAT_RESULT_INVALID``) is shown
in ``test_compat_result.py``.
"""
from __future__ import annotations

import pytest

from engine.config.registry_loader import SchemaValidationError
from engine.magic10_v2 import compat
from engine.narratives.constants import MISSING_NARRATIVE_KEY
from engine.narratives.router import route_keys

RID = "2d5a4ec485fde5dd51004e0286fff1cb1211e4ee79fa71bc62b2a5ecd0b6c129"
FULL = (1 << 64) - 1


def test_release_id_refusal_is_the_calculations(v2_bundle) -> None:
    with pytest.raises(SchemaValidationError) as caught:
        compat.evaluate_magic10_v2(FULL, FULL, v2_bundle, RID.upper())
    assert caught.value.code == "M10V2_CALC_RELEASE_ID_INVALID"
    assert RID.upper() not in repr(caught.value.details)


def _missing_personal_key(category: str, band: str, perspective: str) -> dict[str, str]:
    keys = dict(route_keys(category, band, perspective))
    if perspective == "b_to_a":
        keys["personal_key"] = MISSING_NARRATIVE_KEY
    return keys


def _disagreeing_shared_key(category: str, band: str, perspective: str) -> dict[str, str]:
    keys = dict(route_keys(category, band, perspective))
    if perspective == "b_to_a":
        keys["shared_key"] = keys["shared_key"] + "_other"
    return keys


@pytest.mark.parametrize(
    ("router", "field"), [(_missing_personal_key, "personal_key"), (_disagreeing_shared_key, "shared_key")]
)
def test_missing_or_disagreeing_narrative_key_is_refused(v2_bundle, router, field) -> None:
    with pytest.raises(SchemaValidationError) as caught:
        compat.evaluate_magic10_v2(FULL, FULL, v2_bundle, RID, router=router)
    assert caught.value.code == compat.NARRATIVE_KEY_INVALID
    assert caught.value.details == {"category_id": "harmony", "field": field}


def test_unsupported_reader_version_is_refused(v2_bundle) -> None:
    result = compat.evaluate_magic10_v2(FULL, FULL, v2_bundle, RID).result
    with pytest.raises(SchemaValidationError) as caught:
        compat.reader_projection_v2(result, "v3")
    assert caught.value.code == compat.PROJECTION_REFUSED
    assert caught.value.details == {"reason": "reader_version_unsupported"}
