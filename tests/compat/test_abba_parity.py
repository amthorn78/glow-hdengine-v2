from __future__ import annotations

from engine.compat.compute import compat_public
from engine.compat.ordering import normalize_pair
from engine.presenter import emitter


def _person(uid: str, birthdate: str, birthtime: str, location: str) -> dict[str, str]:
    return {
        "person_uid": uid,
        "birthdate": birthdate,
        "birthtime": birthtime,
        "location": location,
    }


def _compat_payload(left: dict[str, str], right: dict[str, str]) -> dict[str, object]:
    left, right = normalize_pair(left, right)
    compat = compat_public(
        left,
        right,
        "harmony",
        {"harmony": 100},
        engine_tag="hdengine-dev",
        release_id="0" * 64,
        invocation_tag="INV-ABBA",
    )
    return {
        "a": left,
        "b": right,
        "viewer_prefs": {"top_category": "harmony", "weights": {"harmony": 100}},
        "compat": compat,
    }


def test_internal_compat_ab_ba_parity_is_canonical_bytes_identical() -> None:
    a = _person("alice", "1990-01-10", "14:05", "Chicago, US")
    b = _person("bob", "1992-03-04", "08:15", "Berlin, DE")

    ab_payload = _compat_payload(a, b)
    ba_payload = _compat_payload(b, a)

    ab_bytes = emitter.emit_public(ab_payload)
    ba_bytes = emitter.emit_public(ba_payload)

    assert ab_bytes.endswith(b"\n")
    assert ba_bytes.endswith(b"\n")
    assert b"\r\n" not in ab_bytes
    assert b"\r\n" not in ba_bytes
    assert ab_bytes == ba_bytes
