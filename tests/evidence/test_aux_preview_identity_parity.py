from __future__ import annotations

from engine.runtime import identity_meta
from tools.evidence import generate_epic032_pr01_router_evidence as generator


def test_aux_preview_admin_evidence_uses_immutable_release_identity(
    tmp_path,
    monkeypatch,
):
    immutable_release = identity_meta()["release_id"]
    assert generator.RELEASE_ID == immutable_release

    monkeypatch.setenv("RELEASE_ID", "0" * 64)
    admin_out = tmp_path / "admin.json"
    payload = generator._run_cli_admin(
        generator.EXPECTED_CATEGORIES[0],
        generator.BANDS[0],
        generator.PERSPECTIVES[0],
        admin_out,
    )

    assert payload["release_id"] == immutable_release
    assert payload["release_id"] != "0" * 64
