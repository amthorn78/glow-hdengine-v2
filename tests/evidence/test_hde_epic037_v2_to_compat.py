import json
from pathlib import Path

from tools.evidence import generate_hde_epic037_v2_to_compat as generator
from tools.evidence import update_evidence_index as updater

ROOT = Path(__file__).resolve().parents[2]
VENDOR_DIR = ROOT / "artifacts/vendor/hdapi_v2"
ARTIFACTS = [
    VENDOR_DIR / "hde_epic037_v2_to_compat_proof.json",
    VENDOR_DIR / "hde_epic037_v2_to_compat_two_run.json",
    VENDOR_DIR / "hde_epic037_v2_to_compat_pair_order.json",
    VENDOR_DIR / "hde_epic037_admin_public_boundary.json",
]


def _assert_canonical_json(path: Path) -> dict:
    body = path.read_bytes()
    assert body.endswith(b"\n")
    payload = json.loads(body)
    assert body == generator.canonical_json_bytes(payload)
    assert path.with_name(path.name + ".path_proof.txt").exists()
    return payload


def test_epic037_pr04_artifacts_bind_required_identity() -> None:
    for path in ARTIFACTS:
        payload = _assert_canonical_json(path)
        assert payload["epic_id"] == "HDE-EPIC037"
        assert payload["pf09_task_id"] == "HDE-FERM008"
        assert payload["pf09_subtask_id"] == "HDE-FERM008.10"
        assert payload["rails"] == {"allow_network": "0", "closed_rails_only": True, "safe_mode": "1"}
        assert "live vendor success" in payload["nonclaims"]
        assert "PF09 status movement" in payload["nonclaims"]


def test_epic037_pr04_proof_shape_and_compat_acceptance() -> None:
    payload = _assert_canonical_json(VENDOR_DIR / "hde_epic037_v2_to_compat_proof.json")
    assert payload["artifact_kind"] == "hde_epic037_v2_to_compat_proof"
    assert payload["fixture_count"] == 2
    assert payload["raw_request_response_vendor_bodies_absent"] is True
    assert payload["compat_acceptance"]["function"] == "engine.compat.compute.conjunction_public"
    assert payload["compat_acceptance"]["accepted_mapped_resolved_parties"] is True
    assert len(payload["compat_acceptance"]["category_ids"]) == 10
    for result in payload["adapter_results"].values():
        assert result["status"] == "mapped"
        assert all(result["shape_sufficiency"].values())


def test_epic037_pr04_two_run_pair_order_and_public_boundary() -> None:
    two_run = _assert_canonical_json(VENDOR_DIR / "hde_epic037_v2_to_compat_two_run.json")
    assert two_run["canonical_bytes_identical"] is True
    assert two_run["first_run_sha256"] == two_run["second_run_sha256"]
    assert "TWO_RUN_IDENTITY_OK" in two_run["tokens"]

    pair_order = _assert_canonical_json(VENDOR_DIR / "hde_epic037_v2_to_compat_pair_order.json")
    assert pair_order["canonical_ab_ba_bytes_identical"] is True
    assert pair_order["normalized_left_person_uid"] < pair_order["normalized_right_person_uid"]
    assert "COMPOSITE_ABBA_IDENTITY_OK" in pair_order["tokens"]

    boundary = _assert_canonical_json(VENDOR_DIR / "hde_epic037_admin_public_boundary.json")
    assert boundary["public_reader_bands_only"] is True
    assert boundary["public_reader_numeric_free"] is True
    assert boundary["forbidden_public_term_hits"] == []
    assert all(value is False for value in boundary["new_public_reader_surface"].values())


def test_epic037_pr04_index_registration_is_fail_closed() -> None:
    keys = {entry["artifact_key"] for entry in updater.EPIC037_PR04_PRIMARY_ARTIFACTS}
    assert keys == {
        "hdapi_v2.hde_epic037_v2_to_compat_proof",
        "hdapi_v2.hde_epic037_v2_to_compat_two_run",
        "hdapi_v2.hde_epic037_v2_to_compat_pair_order",
        "hdapi_v2.hde_epic037_admin_public_boundary",
    }
    entries = updater._load_epic037_pr04_entries()
    assert {entry["artifact_key"] for entry in entries} == keys
