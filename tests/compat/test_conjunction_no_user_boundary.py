from __future__ import annotations

from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.bodygraph.ingest import resolve_db_user_id
from engine.compat.compute import conjunction_public_resolved
from engine.presenter import emit_public


def _weights() -> dict[str, int]:
    return {cat: 10 for cat in CATEGORIES_ORDER_V1}


def test_no_user_boundary_accepts_user_id_without_person_uid_and_is_ab_ba_stable():
    store = {
        resolve_db_user_id("left-user"): {"id": "left-user", "mechanics": {"type": "generator"}},
        resolve_db_user_id("right-user"): {"id": "right-user", "mechanics": {"type": "generator"}},
    }

    def _lookup(user_id: str):
        return store.get(user_id)

    left_input = {"user_id": "left-user", "birthdate": "1990-01-01", "birthtime": "08:30", "location": "Amsterdam"}
    right_input = {"user_id": "right-user", "birthdate": "1991-02-02", "birthtime": "09:45", "location": "Berlin"}

    # Caller input intentionally omits person_uid; boundary derives deterministic IDs.
    ab = conjunction_public_resolved(
        left_input,
        right_input,
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights=_weights(),
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
        env={"SAFE_MODE": "1", "ALLOW_NETWORK": "0"},
        local_lookup=_lookup,
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
        local_lookup=_lookup,
    )

    assert "person_uid" not in left_input
    assert "person_uid" not in right_input
    assert ab["conjunction"]["left"]["person_uid"]
    assert ab["conjunction"]["right"]["person_uid"]

    ab_bytes = emit_public(ab)
    ba_bytes = emit_public(ba)
    assert ab_bytes == ba_bytes
    assert ab_bytes.endswith(b"\n")
    assert not ab_bytes.startswith(b"\xef\xbb\xbf")
