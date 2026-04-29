from __future__ import annotations

from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.compute import conjunction_public_resolved
from engine.presenter import emit_public


def _weights() -> dict[str, int]:
    return {cat: 10 for cat in CATEGORIES_ORDER_V1}


def test_no_user_boundary_accepts_birth_only_input_without_person_uid_or_user_id_and_is_ab_ba_stable():
    left_input = {"birthdate": "1990-01-01", "birthtime": "08:30", "location": "Amsterdam"}
    right_input = {"birthdate": "1991-02-02", "birthtime": "09:45", "location": "Berlin"}

    # Caller input intentionally omits person_uid and user_id; boundary derives deterministic IDs.
    ab = conjunction_public_resolved(
        left_input,
        right_input,
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights=_weights(),
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
        env={"SAFE_MODE": "1", "ALLOW_NETWORK": "0"},
        local_lookup=lambda *_: None,
    )
    ba = conjunction_public_resolved(
        right_input,
        left_input,
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights=_weights(),
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
        env={"SAFE_MODE": "1", "ALLOW_NETWORK": "0"},
        local_lookup=lambda *_: None,
    )

    assert "person_uid" not in left_input and "user_id" not in left_input
    assert "person_uid" not in right_input and "user_id" not in right_input
    assert ab["conjunction"]["left"]["person_uid"]
    assert ab["conjunction"]["right"]["person_uid"]

    ab_bytes = emit_public(ab)
    ba_bytes = emit_public(ba)
    assert ab_bytes == ba_bytes
    assert ab_bytes.endswith(b"\n")
    assert not ab_bytes.startswith(b"\xef\xbb\xbf")
