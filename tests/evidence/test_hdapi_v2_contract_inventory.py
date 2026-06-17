from __future__ import annotations

import copy
import csv
import json
from pathlib import Path

import pytest

from tools.evidence import generate_hdapi_v2_contract_inventory as generator

ROOT = Path(__file__).resolve().parents[2]
VENDOR_DIR = ROOT / "artifacts" / "vendor" / "hdapi_v2"
REQUIRED_PRIMARY_ARTIFACTS = [
    VENDOR_DIR / "source_inventory.json",
    VENDOR_DIR / "source_inventory.md",
    VENDOR_DIR / "openapi_validation.log",
    VENDOR_DIR / "known_anomalies.md",
    VENDOR_DIR / "endpoint_reference.csv",
    VENDOR_DIR / "contract_map.json",
    ROOT / "docs" / "acceptance_map_epic033.json",
    ROOT / "audit" / "qa" / "hde-epic033" / "token_evidence_matrix.md",
    ROOT / "audit" / "qa" / "hde-epic033" / "acceptance_map_viability.log",
    ROOT / "audit" / "docdeltas" / "hde-epic033_doc_deltas.md",
    ROOT / "audit" / "qa" / "hde-epic033" / "00_meta" / "doc_deltas.md",
]
REQUIRED_SOURCE_CACHE = [
    VENDOR_DIR / "source_cache" / "source_metadata.json",
    VENDOR_DIR / "source_cache" / "robots_preflight.body",
    VENDOR_DIR / "source_cache" / "llms_txt.body",
    VENDOR_DIR / "source_cache" / "llms-full.endpoint-tiers.txt",
    VENDOR_DIR / "source_cache" / "v2-routes.yaml",
    VENDOR_DIR / "source_cache" / "v1-routes.yaml",
    VENDOR_DIR / "source_cache" / "api-reference.openapi.json",
    VENDOR_DIR / "source_cache" / "v2_overview.body",
    VENDOR_DIR / "source_cache" / "v1_overview.body",
    VENDOR_DIR / "source_cache" / "v2_full_chart_page.body",
    VENDOR_DIR / "source_cache" / "v2_simple_chart_page.body",
    VENDOR_DIR / "source_cache" / "v2_coordinates_chart_page.body",
    VENDOR_DIR / "source_cache" / "authentication.body",
    VENDOR_DIR / "source_cache" / "rate_limiting.body",
    VENDOR_DIR / "source_cache" / "response_format.body",
    VENDOR_DIR / "source_cache" / "migration_v1_to_v2.body",
    VENDOR_DIR / "source_cache" / "coordinates_guide.body",
]
REQUIRED_ENDPOINTS = {
    ("POST", "/v2/charts"): "recommended_v2_chart",
    ("POST", "/v2/charts/simple"): "recommended_v2_chart",
    ("POST", "/v2/charts/coordinates"): "recommended_v2_chart",
    ("POST", "/v1/bodygraphs"): "legacy_v1_bodygraph",
    ("POST", "/v1/bodygraphs/simple"): "legacy_v1_bodygraph",
}
ALLOWED_TOKENS = {
    "TESTS_PASS_OK",
    "DOC_DELTA_PRESENT_OK",
    "EVIDENCE_INDEX_UPDATED_OK",
    "MACHINE_MIRROR_UPDATED_OK",
    "EVIDENCE_INDEX_HASH_OK",
    "EVIDENCE_PATHS_VALIDATED_OK",
    "EVIDENCE_PATH_PROOFS_OK",
    "JSON_CANONICAL_CHECK_OK",
}


def _assert_canonical_json(path: Path) -> dict:
    raw = path.read_bytes()
    assert raw.endswith(b"\n")
    assert not raw.endswith(b"\n\n")
    assert not raw.startswith(b"\xef\xbb\xbf")
    payload = json.loads(raw.decode("utf-8"))
    expected = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
    assert raw == expected
    return payload


def test_hdapi_v2_primary_artifacts_exist_and_are_lf_terminated() -> None:
    for path in REQUIRED_PRIMARY_ARTIFACTS:
        assert path.exists(), path
        raw = path.read_bytes()
        assert raw, path
        assert raw.endswith(b"\n"), path
        assert b"\r\n" not in raw, path
    for path in REQUIRED_SOURCE_CACHE:
        assert path.exists(), path
        assert path.read_bytes(), path


def test_hdapi_v2_inventory_records_required_source_fields_and_ai_boundary() -> None:
    inventory = _assert_canonical_json(VENDOR_DIR / "source_inventory.json")
    assert "documentation-discovery-only" in inventory["ai_boundary"]
    assert inventory["source_mode"] == "closed-rails-source-cache"
    for key in ["llms_txt", "llms_full_txt", "v2_routes_yaml", "v1_routes_yaml", "suspect_openapi_json"]:
        source = inventory["sources"][key]
        for field in ["source_url", "final_url", "content_type", "fetch_status", "sha256", "discovered_from", "last_seen_utc", "source_classification"]:
            assert source[field] != "", (key, field)
    assert inventory["sources"]["llms_txt"]["source_classification"] == "documentation-discovery-only"
    assert inventory["sources"]["llms_full_txt"]["source_classification"] == "documentation-discovery-only"


def test_hdapi_v2_validation_and_anomaly_posture_are_consistent() -> None:
    log = (VENDOR_DIR / "openapi_validation.log").read_text(encoding="utf-8")
    assert "source_mode=closed-rails-source-cache" in log
    assert "Ruby Psych YAML parser" in log
    assert "[v2-routes.yaml] status=VALIDATED" in log
    assert "[v2-routes.yaml] openapi_3_parse=PASS" in log
    assert "[v1-routes.yaml] status=VALIDATED" in log
    assert "[route-spec-gate] status=PASS" in log
    anomalies = (VENDOR_DIR / "known_anomalies.md").read_text(encoding="utf-8")
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    if "[api-reference/openapi.json] status=VALIDATED" in log:
        assert "Decision: VALIDATED." in anomalies
        assert contract["quarantined_sources"] == []
    else:
        assert "[api-reference/openapi.json] status=QUARANTINED" in log
        assert "Decision: QUARANTINED." in anomalies
        assert contract["quarantined_sources"]
        assert contract["quarantined_sources"][0]["source_key"] == "suspect_openapi_json"


def test_hdapi_v2_endpoint_reference_distinguishes_v2_and_legacy_v1() -> None:
    rows = list(csv.DictReader((VENDOR_DIR / "endpoint_reference.csv").read_text(encoding="utf-8").splitlines()))
    observed = {(row["method"], row["path"]): row for row in rows}
    assert set(observed) == set(REQUIRED_ENDPOINTS)
    for key, family in REQUIRED_ENDPOINTS.items():
        assert observed[key]["route_family"] == family
    assert observed[("POST", "/v2/charts")]["success_envelope"].startswith("StandardResponse")
    assert "flat JSON" in observed[("POST", "/v1/bodygraphs")]["success_envelope"]
    assert observed[("POST", "/v2/charts/coordinates")]["geocode_key_requirement"] == "not needed"


def test_hdapi_v2_contract_map_is_canonical_and_non_conformance_only() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    assert "no HumanDesignAPI v2 runtime request shaping" in contract["non_conformance_claim"]
    routes = {(route["method"], route["path"]): route for route in contract["route_families"]}
    assert set(routes) == set(REQUIRED_ENDPOINTS)
    assert routes[("POST", "/v2/charts")]["route_family"] == "recommended_v2_chart"
    assert routes[("POST", "/v1/bodygraphs")]["route_family"] == "legacy_v1_bodygraph"
    if contract["quarantined_sources"]:
        assert contract["quarantined_sources"][0]["source_key"] == "suspect_openapi_json"


def test_epic033_acceptance_uses_only_allowed_existing_tokens() -> None:
    acceptance = _assert_canonical_json(ROOT / "docs" / "acceptance_map_epic033.json")
    tokens = {entry["name"] for entry in acceptance["tokens"]}
    assert tokens
    assert tokens <= ALLOWED_TOKENS
    assert all("V2" not in token and "HDAPI" not in token for token in tokens)
    text = (ROOT / "audit" / "qa" / "hde-epic033" / "token_evidence_matrix.md").read_text(encoding="utf-8")
    assert "does not mint a vendor-v2-specific token" in text


def test_hdapi_v2_index_and_path_proof_bindings_when_promoted() -> None:
    index = json.loads((ROOT / "docs" / "evidence" / "INDEX.json").read_text(encoding="utf-8"))
    mirror_lines = [json.loads(line) for line in (ROOT / "artifacts" / "evidence_index.jsonl").read_text(encoding="utf-8").splitlines() if line]
    index_paths = {entry["discovered_physical_path"] for entry in index}
    mirror_paths = {entry["discovered_physical_path"] for entry in mirror_lines}
    promoted = [path.relative_to(ROOT).as_posix() for path in REQUIRED_PRIMARY_ARTIFACTS]
    for rel in promoted:
        assert rel in index_paths
        assert rel in mirror_paths
        proof = ROOT / f"{rel}.path_proof.txt"
        assert proof.exists(), proof
        proof_text = proof.read_text(encoding="utf-8")
        assert f"path: {rel}" in proof_text
        assert "sha256: " in proof_text


def test_generator_default_closed_rails_uses_source_cache_without_network_fetch(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")

    def fail_fetch(_url: str) -> tuple[str, str, int | str, bytes]:
        raise AssertionError("network fetch must not run in closed-rails source-cache mode")

    monkeypatch.setattr(generator, "fetch_public_doc", fail_fetch)
    metadata, bodies = generator.load_source_cache()
    outputs = generator.render_outputs("2026-05-31T00:00:00Z", metadata, bodies, mode="closed-rails-source-cache")
    assert VENDOR_DIR / "source_inventory.json" in outputs


def test_generator_refresh_requires_explicit_open_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    with pytest.raises(SystemExit, match="OPEN_RAILS_REQUIRED"):
        generator.require_open_rails_for_refresh()


def test_generator_fails_before_promoting_contract_when_route_validation_fails() -> None:
    metadata, bodies = generator.load_source_cache()
    broken = dict(bodies)
    broken["v2_routes_yaml"] = "openapi: 3.0.3\ninfo:\n  title: Human Design API — v2\n  version: 2.0.0\npaths: {}\n".encode("utf-8")
    with pytest.raises(SystemExit, match="ROUTE_SPEC_VALIDATION_FAILED"):
        generator.render_outputs("2026-05-31T00:00:00Z", metadata, broken, mode="closed-rails-source-cache")


def test_endpoint_reference_matches_source_parsed_rows() -> None:
    _metadata, bodies = generator.load_source_cache()
    parsed_rows = generator.build_endpoint_rows(
        generator.parse_yaml_openapi(bodies["v2_routes_yaml"], "v2-routes.yaml"),
        generator.parse_yaml_openapi(bodies["v1_routes_yaml"], "v1-routes.yaml"),
        bodies["llms_full_txt"].decode("utf-8"),
    )
    csv_rows = list(csv.DictReader((VENDOR_DIR / "endpoint_reference.csv").read_text(encoding="utf-8").splitlines()))
    assert csv_rows == parsed_rows




def test_source_inventory_rows_have_verified_cache_bodies() -> None:
    metadata, _bodies = generator.load_source_cache()
    inventory = _assert_canonical_json(VENDOR_DIR / "source_inventory.json")
    for key, source in inventory["sources"].items():
        cache_path = source.get("cache_path")
        assert cache_path, key
        body = (ROOT / cache_path).read_bytes()
        assert generator.sha256_bytes(body) == metadata[key]["cache_sha256"]


def test_tiers_are_parsed_from_endpoint_tier_table_cells() -> None:
    metadata, bodies = generator.load_source_cache()
    changed = dict(bodies)
    changed["llms_full_txt"] = bodies["llms_full_txt"].replace(
        b"| `POST /v2/charts`             | Full chart with all properties                             | Advanced         | Required    |",
        b"| `POST /v2/charts`             | Full chart with all properties                             | Professional     | Required    |",
    )
    outputs = generator.render_outputs("2026-05-31T00:00:00Z", metadata, changed, mode="closed-rails-source-cache")
    rows = list(csv.DictReader(outputs[VENDOR_DIR / "endpoint_reference.csv"].decode("utf-8").splitlines()))
    assert {row["path"]: row["tier"] for row in rows}["/v2/charts"] == "Professional"


def test_unavailable_suspect_openapi_does_not_block_contract_generation() -> None:
    metadata, bodies = generator.load_source_cache()
    changed_metadata = copy.deepcopy(metadata)
    changed_bodies = dict(bodies)
    changed_metadata["suspect_openapi_json"]["fetch_status"] = "404"
    changed_metadata["suspect_openapi_json"]["sha256"] = ""
    changed_metadata["suspect_openapi_json"]["cache_sha256"] = generator.sha256_bytes(b"")
    changed_bodies["suspect_openapi_json"] = b""
    outputs = generator.render_outputs("2026-05-31T00:00:00Z", changed_metadata, changed_bodies, mode="closed-rails-source-cache")
    log = outputs[VENDOR_DIR / "openapi_validation.log"].decode("utf-8")
    assert "[route-spec-gate] status=PASS" in log
    assert "[api-reference/openapi.json] fetch_status=404" in log
    contract = json.loads(outputs[VENDOR_DIR / "contract_map.json"].decode("utf-8"))
    assert contract["quarantined_sources"][0]["source_key"] == "suspect_openapi_json"


def test_epic033_mirror_chronology_matches_artifact_generation_time() -> None:
    inventory = json.loads((VENDOR_DIR / "source_inventory.json").read_text(encoding="utf-8"))
    produced = inventory["generated_at_utc"]
    for rel in [
        "artifacts/vendor/hdapi_v2/source_inventory.json",
        "artifacts/vendor/hdapi_v2/contract_map.json",
        "docs/acceptance_map_epic033.json",
    ]:
        proof = (ROOT / f"{rel}.path_proof.txt").read_text(encoding="utf-8")
        assert f"produced_at_utc: {produced}" in proof
    mirror_rows = [json.loads(line) for line in (ROOT / "artifacts/evidence_index.jsonl").read_text(encoding="utf-8").splitlines() if line]
    for row in mirror_rows:
        if row["discovered_physical_path"] in {
            "artifacts/vendor/hdapi_v2/source_inventory.json",
            "artifacts/vendor/hdapi_v2/contract_map.json",
            "docs/acceptance_map_epic033.json",
        }:
            assert row["produced_at_utc"] == produced


def test_epic034_source_selection_snapshot_is_canonical_and_derived_from_contract_map() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    snapshot = _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json")
    assert snapshot == generator.build_source_selection_snapshot(snapshot["generated_at_utc"], contract)
    assert snapshot["source_selection_policy"]["classification_source"] == "governed contract inventory"
    assert snapshot["runtime_conformance_claim"] == "NONE"
    assert snapshot["request_shaping_claim"] == "NONE"
    assert snapshot["open_rails_vendor_smoke_claim"] == "NONE"
    assert snapshot["public_reader_change_claim"] == "NONE"
    assert snapshot["ai_scope_claim"] == "NONE"


def test_epic034_source_selection_distinguishes_v2_chart_variants_and_v1_legacy() -> None:
    snapshot = _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json")
    routes = {(route["method"], route["path"]): route for route in snapshot["route_families"]}
    assert set(routes) == set(REQUIRED_ENDPOINTS)
    assert routes[("POST", "/v2/charts")]["route_family"] == "recommended_v2_chart"
    assert routes[("POST", "/v2/charts/simple")]["route_family"] == "recommended_v2_chart"
    assert routes[("POST", "/v2/charts/coordinates")]["route_family"] == "recommended_v2_chart"
    assert routes[("POST", "/v1/bodygraphs")]["route_family"] == "legacy_v1_bodygraph"
    assert routes[("POST", "/v1/bodygraphs/simple")]["route_family"] == "legacy_v1_bodygraph"
    assert {
        routes[("POST", "/v2/charts")]["route_variant"],
        routes[("POST", "/v2/charts/simple")]["route_variant"],
        routes[("POST", "/v2/charts/coordinates")]["route_variant"],
    } == {"full_chart", "simple_chart", "coordinates_chart"}
    assert all(route["classification_source"] == "artifacts/vendor/hdapi_v2/contract_map.json route_families" for route in routes.values())
    assert "Authorization Bearer token" in routes[("POST", "/v2/charts")]["auth_model"]
    assert "Authorization Bearer token" in routes[("POST", "/v2/charts/simple")]["auth_model"]
    assert "Authorization Bearer token" in routes[("POST", "/v2/charts/coordinates")]["auth_model"]
    assert "HD-Api-Key header" not in routes[("POST", "/v2/charts")]["auth_model"]
    assert "HD-Api-Key header" not in routes[("POST", "/v2/charts/simple")]["auth_model"]
    assert "HD-Api-Key header" not in routes[("POST", "/v2/charts/coordinates")]["auth_model"]
    assert "HD-Api-Key header" in routes[("POST", "/v1/bodygraphs")]["auth_model"]
    assert "HD-Api-Key header" in routes[("POST", "/v1/bodygraphs/simple")]["auth_model"]
    assert "Authorization Bearer token" not in routes[("POST", "/v1/bodygraphs")]["auth_model"]
    assert "Authorization Bearer token" not in routes[("POST", "/v1/bodygraphs/simple")]["auth_model"]
    assert routes[("POST", "/v2/charts")]["geocode_key_requirement"] == "required"
    assert "HD-Geocode-Key header" in routes[("POST", "/v2/charts")]["auth_model"]
    assert routes[("POST", "/v2/charts/simple")]["geocode_key_requirement"] == "required"
    assert "HD-Geocode-Key header" in routes[("POST", "/v2/charts/simple")]["auth_model"]
    assert routes[("POST", "/v2/charts/coordinates")]["geocode_key_requirement"] == "not needed"
    assert "HD-Geocode-Key header" not in routes[("POST", "/v2/charts/coordinates")]["auth_model"]
    assert routes[("POST", "/v1/bodygraphs")]["geocode_key_requirement"] == "required"
    assert "HD-Geocode-Key header" in routes[("POST", "/v1/bodygraphs")]["auth_model"]
    assert routes[("POST", "/v1/bodygraphs/simple")]["geocode_key_requirement"] == "required"
    assert "HD-Geocode-Key header" in routes[("POST", "/v1/bodygraphs/simple")]["auth_model"]
    for (method, path), route in routes.items():
        assert route["source_precedence_rank"] == 1
        assert route["source_spec"] == generator.source_spec_for(path)


def test_epic034_v1_legacy_guard_log_proves_no_silent_v1_to_v2_collapse() -> None:
    log_path = VENDOR_DIR / "v1_legacy_guard.log"
    raw = log_path.read_bytes()
    assert raw.endswith(b"\n")
    assert b"\r\n" not in raw
    log = raw.decode("utf-8")
    assert "[/v1/bodygraphs] legacy_v1_bodygraph_explicit=PASS" in log
    assert "[/v1/bodygraphs/simple] legacy_v1_bodygraph_explicit=PASS" in log
    assert "[/v1/bodygraphs] collapsed_to_recommended_v2_chart=FAIL" in log
    assert "[/v1/bodygraphs/simple] collapsed_to_recommended_v2_chart=FAIL" in log
    assert "v2_chart_route_variants_distinct=PASS" in log
    assert "status=PASS" in log


def test_epic034_source_selection_check_log_exists_and_passes() -> None:
    log_path = ROOT / "audit" / "qa" / "hde-epic034" / "pr-01" / "source_selection_check.log"
    raw = log_path.read_bytes()
    assert raw.endswith(b"\n")
    assert b"\r\n" not in raw
    log = raw.decode("utf-8")
    for check in [
        "recommended_v2_full_chart",
        "recommended_v2_simple_chart",
        "recommended_v2_coordinates_chart",
        "legacy_v1_full_bodygraph",
        "legacy_v1_simple_bodygraph",
        "v2_variants_distinguished",
        "v1_not_collapsed_to_v2",
        "v2_auth_family_bearer_only",
        "v1_auth_family_hd_api_key_only",
        "v2_location_geocode_required",
        "v1_bodygraph_geocode_required",
        "coordinates_geocode_not_needed",
        "required_geocode_auth_header_present",
        "coordinates_geocode_auth_header_absent",
        "source_authority_validated_yaml_rank1",
    ]:
        assert f"[{check}] status=PASS" in log
    assert "network_posture=closed-rails-source-cache; no live vendor calls" in log


def test_epic034_source_selection_fails_when_contract_inventory_is_missing_required_route() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    broken = copy.deepcopy(contract)
    broken["route_families"] = [route for route in broken["route_families"] if route["path"] != "/v2/charts/coordinates"]
    with pytest.raises(ValueError, match="SOURCE_SELECTION_MISSING_CONTRACT_ROUTES"):
        generator.build_source_selection_snapshot("2026-06-16T00:00:00Z", broken)


def test_epic034_source_selection_check_log_reflects_public_docs_refresh_mode() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    snapshot = generator.build_source_selection_snapshot("2026-06-16T00:00:00Z", contract)
    log = generator.build_source_selection_check_log("2026-06-16T00:00:00Z", snapshot, mode="public-docs-refresh")
    assert "network_posture=public-docs-refresh; no credentialed runtime vendor calls" in log
    assert "network_posture=closed-rails-source-cache" not in log


def test_epic034_source_selection_fails_when_auth_family_collapses() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    broken = copy.deepcopy(contract)
    for route in broken["route_families"]:
        if route["path"] == "/v1/bodygraphs":
            route["auth_model"] = "Authorization Bearer token"
    with pytest.raises(ValueError, match="SOURCE_SELECTION_AUTH_FAMILY_MISMATCH"):
        generator.build_source_selection_snapshot("2026-06-16T00:00:00Z", broken)


def test_epic034_source_selection_fails_when_auth_family_is_mixed() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    mixed_v1 = copy.deepcopy(contract)
    for route in mixed_v1["route_families"]:
        if route["path"] == "/v1/bodygraphs":
            route["auth_model"] = "HD-Api-Key header plus Authorization Bearer token"
    with pytest.raises(ValueError, match="SOURCE_SELECTION_AUTH_FAMILY_MISMATCH"):
        generator.build_source_selection_snapshot("2026-06-16T00:00:00Z", mixed_v1)

    mixed_v2 = copy.deepcopy(contract)
    for route in mixed_v2["route_families"]:
        if route["path"] == "/v2/charts":
            route["auth_model"] = "Authorization Bearer token plus HD-Api-Key header"
    with pytest.raises(ValueError, match="SOURCE_SELECTION_AUTH_FAMILY_MISMATCH"):
        generator.build_source_selection_snapshot("2026-06-16T00:00:00Z", mixed_v2)


def test_epic034_source_selection_fails_when_source_authority_drifts() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    broken_spec = copy.deepcopy(contract)
    for route in broken_spec["route_families"]:
        if route["path"] == "/v2/charts":
            route["source_spec"] = "docs.humandesignapi.nl/quarantined#/paths/~1charts/post"
    with pytest.raises(ValueError, match="SOURCE_SELECTION_SOURCE_AUTHORITY_MISMATCH"):
        generator.build_source_selection_snapshot("2026-06-16T00:00:00Z", broken_spec)

    broken_rank = copy.deepcopy(contract)
    for route in broken_rank["route_families"]:
        if route["path"] == "/v1/bodygraphs":
            route["source_precedence_rank"] = 2
    with pytest.raises(ValueError, match="SOURCE_SELECTION_SOURCE_AUTHORITY_MISMATCH"):
        generator.build_source_selection_snapshot("2026-06-16T00:00:00Z", broken_rank)


def test_epic034_source_selection_fails_when_non_coordinate_geocode_drifts() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    broken = copy.deepcopy(contract)
    for route in broken["route_families"]:
        if route["path"] == "/v2/charts/simple":
            route["geocode_key_requirement"] = "not needed"
    with pytest.raises(ValueError, match="SOURCE_SELECTION_GEOCODE_REQUIREMENT_MISMATCH"):
        generator.build_source_selection_snapshot("2026-06-16T00:00:00Z", broken)


def test_epic034_source_selection_fails_when_geocode_auth_header_drifts() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    missing_required = copy.deepcopy(contract)
    for route in missing_required["route_families"]:
        if route["path"] == "/v2/charts":
            route["auth_model"] = "Authorization Bearer token"
    with pytest.raises(ValueError, match="SOURCE_SELECTION_GEOCODE_AUTH_MISMATCH"):
        generator.build_source_selection_snapshot("2026-06-16T00:00:00Z", missing_required)

    extra_coordinates = copy.deepcopy(contract)
    for route in extra_coordinates["route_families"]:
        if route["path"] == "/v2/charts/coordinates":
            route["auth_model"] = "Authorization Bearer token plus HD-Geocode-Key header"
    with pytest.raises(ValueError, match="SOURCE_SELECTION_GEOCODE_AUTH_MISMATCH"):
        generator.build_source_selection_snapshot("2026-06-16T00:00:00Z", extra_coordinates)


def test_epic034_request_shaping_snapshot_is_canonical_secret_safe_and_contract_derived() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    source_selection = _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json")
    ops = json.loads((ROOT / "audit" / "ops" / "hde-epic034" / "ops-01" / "fact_summary.json").read_text(encoding="utf-8"))
    snapshot = _assert_canonical_json(VENDOR_DIR / "request_shaping.snapshot.json")
    assert snapshot == generator.build_request_shaping_snapshot(snapshot["generated_at_utc"], contract, source_selection, ops)
    assert snapshot["base_url_env_var"] == "HD_API_BASE_URL"
    assert snapshot["deprecated_base_url_alias"]["env_var"] == "HDAPI_BASE_URL"
    assert snapshot["v2_auth_header_posture"] == "Authorization: Bearer <redacted>"
    assert snapshot["v1_legacy_auth_header_posture"] == "HD-Api-Key: <redacted>"
    assert "v2 chart birthdate remains YYYY-MM-DD" in snapshot["canonical_request_body_construction_proof"]
    assert "lat/lng are serialized as JSON numbers" in snapshot["canonical_request_body_construction_proof"]
    rendered = json.dumps(snapshot, sort_keys=True)
    for secret in ["api-key", "geo-key", "k_test", "Bearer api", "Bearer geo"]:
        assert secret not in rendered
    assert snapshot["live_vendor_call_claim"] == "NONE"
    assert snapshot["public_reader_change_claim"] == "NONE"
    assert snapshot["open_rails_vendor_smoke_claim"] == "NONE"
    assert snapshot["runtime_conformance_claim"] == "NONE"
    assert snapshot["ai_scope_claim"] == "NONE"


def test_epic034_request_shaping_auth_base_url_and_geocode_postures() -> None:
    snapshot = _assert_canonical_json(VENDOR_DIR / "request_shaping.snapshot.json")
    routes = {route["endpoint_path"]: route for route in snapshot["routes"]}
    for path in ["/v2/charts", "/v2/charts/simple", "/v2/charts/coordinates"]:
        assert routes[path]["auth_header_posture"] == "Authorization: Bearer <redacted>"
        assert "HD-Api-Key" not in routes[path]["auth_header_posture"]
        assert routes[path]["credential_env_var"] == "HD_API_KEY"
        assert routes[path]["content_type_posture"] == "application/json"
    for path in ["/v1/bodygraphs", "/v1/bodygraphs/simple"]:
        assert routes[path]["auth_header_posture"] == "HD-Api-Key: <redacted>"
        assert "Bearer" not in routes[path]["auth_header_posture"]
    assert routes["/v2/charts"]["geocode_env_var"] == "GEO_API_KEY"
    assert routes["/v2/charts"]["geocode_header_posture"] == "HD-Geocode-Key: <redacted>"
    assert routes["/v2/charts/simple"]["geocode_header_posture"] == "HD-Geocode-Key: <redacted>"
    assert routes["/v2/charts/coordinates"]["geocode_header_posture"] == "not applicable"


def test_epic034_request_shaping_check_log_exists_and_passes() -> None:
    log_path = ROOT / "audit" / "qa" / "hde-epic034" / "pr-02" / "request_shaping_check.log"
    raw = log_path.read_bytes()
    assert raw.endswith(b"\n")
    assert b"\r\n" not in raw
    log = raw.decode("utf-8")
    for check in [
        "closed_rails_generation", "no_live_vendor_call_attempted", "v2_bearer_auth_posture",
        "v1_legacy_hd_api_key_posture", "geocode_posture", "canonical_base_url_key_posture",
        "deprecated_alias_posture", "no_secret_values_emitted",
    ]:
        assert f"[{check}] status=PASS" in log
    assert "[evidence_index_and_path_proof_posture] status=PASS" not in log
    assert "evidence_index_and_path_proof_posture=validated_by_update_evidence_index_and_validate_evidence_paths_not_generator" in log
    assert "status=PASS" in log


def test_epic034_request_shaping_fails_on_ops_fact_summary_missing_required_fact() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    source_selection = _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json")
    with pytest.raises(ValueError, match="OPS01_FACT_SUMMARY_INCOMPLETE"):
        generator.build_request_shaping_snapshot("2026-06-17T00:00:00Z", contract, source_selection, {"PR-02": "proceed"})


def test_epic034_request_shaping_outputs_do_not_depend_on_existing_source_selection_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(generator, "SOURCE_SELECTION_SNAPSHOT", tmp_path / "missing-source-selection.snapshot.json")
    metadata, bodies = generator.load_source_cache()
    outputs = generator.render_outputs("2026-06-17T00:00:00Z", metadata, bodies, mode="closed-rails-source-cache")
    assert generator.REQUEST_SHAPING_SNAPSHOT in outputs
    assert generator.REQUEST_SHAPING_CHECK_LOG in outputs


def test_epic034_request_shaping_rejects_ops01_blocker_wording() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    source_selection = _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json")
    ops = json.loads((ROOT / "audit" / "ops" / "hde-epic034" / "ops-01" / "fact_summary.json").read_text(encoding="utf-8"))
    ops["pr02_can_proceed_safely"] = "blocker: PR-02 must not proceed until PO approval is recorded"
    with pytest.raises(ValueError, match="pr02_can_proceed_safely"):
        generator.build_request_shaping_snapshot("2026-06-17T00:00:00Z", contract, source_selection, ops)


def test_epic034_request_shaping_artifacts_are_closed_rails_only_for_public_doc_refresh() -> None:
    metadata, bodies = generator.load_source_cache()
    outputs = generator.render_outputs("2026-06-17T00:00:00Z", metadata, bodies, mode="public-docs-refresh")
    assert generator.REQUEST_SHAPING_SNAPSHOT not in outputs
    assert generator.REQUEST_SHAPING_CHECK_LOG not in outputs


def test_epic034_request_shaping_closed_rails_generation_requires_env_pins(monkeypatch: pytest.MonkeyPatch) -> None:
    metadata, bodies = generator.load_source_cache()
    monkeypatch.delenv("SAFE_MODE", raising=False)
    with pytest.raises(SystemExit, match="CLOSED_RAILS_REQUIRED_FOR_REQUEST_SHAPING"):
        generator.render_outputs("2026-06-17T00:00:00Z", metadata, bodies, mode="closed-rails-source-cache")


def test_epic034_public_doc_refresh_removes_stale_pr02_outputs(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    stale = [tmp_path / "request_shaping.snapshot.json", tmp_path / "request_shaping.snapshot.json.path_proof.txt", tmp_path / "request_shaping_check.log", tmp_path / "request_shaping_check.log.path_proof.txt"]
    for path in stale:
        path.write_text("stale\n", encoding="utf-8")
    monkeypatch.setattr(generator, "REQUEST_SHAPING_OUTPUTS", tuple(stale))
    generator.remove_request_shaping_outputs()
    assert all(not path.exists() for path in stale)
