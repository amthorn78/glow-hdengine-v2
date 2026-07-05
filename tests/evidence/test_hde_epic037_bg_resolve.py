from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACTS = [
    ROOT / "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_v2_route_policy.snapshot.json",
    ROOT / "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_request_shape.snapshot.json",
    ROOT / "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_closed_rails_no_io.json",
    ROOT / "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_legacy_fallback.snapshot.json",
]


def _load(path: Path) -> dict[str, object]:
    assert path.exists()
    assert path.with_name(path.name + ".path_proof.txt").exists()
    return json.loads(path.read_text(encoding="utf-8"))


def test_epic037_pr03_bg_resolve_artifacts_bind_required_identity() -> None:
    for path in ARTIFACTS:
        payload = _load(path)
        assert payload["epic_id"] == "HDE-EPIC037"
        assert payload["pf09_task_id"] == "HDE-FERM008"
        assert payload["pf09_subtask_id"] == "HDE-FERM008.9"
        assert payload["rails"] == {"allow_network": "0", "closed_rails_only": True, "safe_mode": "1"}
        assert "live vendor success" in payload["nonclaims"]
        assert "AI scope" in payload["nonclaims"]


def test_epic037_pr03_route_policy_and_request_shape_are_v2_chart_backed() -> None:
    route = _load(ARTIFACTS[0])
    policy = route["route_policy"]
    assert policy["classification"] == "adapter_backed_v2_chart"
    assert policy["resource_path"] == "charts"
    assert policy["route_family"] == "recommended_v2_chart"
    assert policy["route_auth_posture"] == "Authorization: Bearer <redacted>"
    assert route["resolver_output_proof"]["adapter"]["code"] == "ADAPTER_MAPPED"

    request = _load(ARTIFACTS[1])["request_shape"]
    assert request["resource_path"] == "charts"
    assert request["route"] == "vendor.hdapi.post:/charts"
    assert request["configured_base_url"] == "<redacted>"
    assert request["url_posture"] == "configured_base_url/charts"
    assert "url" not in request
    assert request["no_double_version_prefix"] is True
    assert request["no_legacy_bodygraph_request_against_v2"] is True
    assert request["auth_header_posture"] == "Authorization: Bearer <redacted>"
    assert request["geocode_header_posture"] == "HD-Geocode-Key: <redacted>"


def test_epic037_pr03_closed_rails_and_legacy_fallback_are_explicit() -> None:
    closed = _load(ARTIFACTS[2])
    assert closed["closed_rails_result"]["error"]["code"] == "PROVIDER_REFUSED"
    assert all(value is False for value in closed["no_io_before_refusal"].values())

    legacy = _load(ARTIFACTS[3])
    assert legacy["legacy_fallback_policy"]["classification"] == "explicit_legacy_fallback"
    assert legacy["legacy_fallback_policy"]["resource_path"] == "bodygraphs"
    assert legacy["legacy_request_auth_posture"] == "HD-Api-Key: <redacted>"
