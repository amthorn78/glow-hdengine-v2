from __future__ import annotations

import copy
import csv
import json
from pathlib import Path

import pytest

from tools.evidence import generate_hdapi_v2_contract_inventory as generator
from tools.evidence import update_evidence_index as indexer

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
    monkeypatch.setattr(generator, "EPIC034_CLOSED_RAILS_DERIVED_OUTPUTS", tuple(stale))
    generator.remove_request_shaping_outputs()
    assert all(not path.exists() for path in stale)


def test_epic034_public_doc_refresh_removes_stale_pr03_response_mapping_outputs(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    stale = [
        tmp_path / "request_shaping.snapshot.json",
        tmp_path / "request_shaping.snapshot.json.path_proof.txt",
        tmp_path / "request_shaping_check.log",
        tmp_path / "request_shaping_check.log.path_proof.txt",
        tmp_path / "response_mapping.snapshot.json",
        tmp_path / "response_mapping.snapshot.json.path_proof.txt",
        tmp_path / "response_mapping_check.log",
        tmp_path / "response_mapping_check.log.path_proof.txt",
    ]
    for path in stale:
        path.write_text("stale\n", encoding="utf-8")
    monkeypatch.setattr(generator, "EPIC034_CLOSED_RAILS_DERIVED_OUTPUTS", tuple(stale))
    generator.remove_request_shaping_outputs()
    assert all(not path.exists() for path in stale)


def test_epic034_pr02_stale_index_rows_are_removed_when_outputs_are_absent(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    stale_payload = [
        {"artifact_key": "hdapi_v2.request_shaping", "discovered_physical_path": "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json"},
        {"artifact_key": "epic034.pr02.request_shaping_check", "discovered_physical_path": "audit/qa/hde-epic034/pr-02/request_shaping_check.log"},
        {"artifact_key": "keep", "discovered_physical_path": "artifacts/keep.txt"},
    ]
    index_path = tmp_path / "INDEX.json"
    index_path.write_text(json.dumps(stale_payload), encoding="utf-8")
    monkeypatch.setattr(indexer, "HUMAN_INDEX", index_path)
    monkeypatch.setattr(indexer, "_load_epic034_pr02_entries", lambda: [])
    loaded = indexer._load_human_index()
    keys = {(entry["artifact_key"], entry["discovered_physical_path"]) for entry in loaded}
    assert ("hdapi_v2.request_shaping", "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json") not in keys
    assert ("epic034.pr02.request_shaping_check", "audit/qa/hde-epic034/pr-02/request_shaping_check.log") not in keys
    assert ("keep", "artifacts/keep.txt") in keys


def test_epic034_pr03_stale_index_rows_are_removed_when_outputs_are_absent(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    stale_payload = [
        {"artifact_key": "hdapi_v2.response_mapping", "discovered_physical_path": "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"},
        {"artifact_key": "epic034.pr03.response_mapping_check", "discovered_physical_path": "audit/qa/hde-epic034/pr-03/response_mapping_check.log"},
        {"artifact_key": "epic034.pr03.doc_deltas", "discovered_physical_path": "audit/docdeltas/hde-epic034_doc_deltas.md"},
        {"artifact_key": "epic034.pr03.qa_meta_doc_deltas", "discovered_physical_path": "audit/qa/hde-epic034/00_meta/doc_deltas.md"},
        {"artifact_key": "keep", "discovered_physical_path": "artifacts/keep.txt"},
    ]
    index_path = tmp_path / "INDEX.json"
    index_path.write_text(json.dumps(stale_payload), encoding="utf-8")
    monkeypatch.setattr(indexer, "HUMAN_INDEX", index_path)
    monkeypatch.setattr(indexer, "_load_epic034_pr03_entries", lambda: [])
    loaded = indexer._load_human_index()
    keys = {(entry["artifact_key"], entry["discovered_physical_path"]) for entry in loaded}
    assert ("hdapi_v2.response_mapping", "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json") not in keys
    assert ("epic034.pr03.response_mapping_check", "audit/qa/hde-epic034/pr-03/response_mapping_check.log") not in keys
    assert ("epic034.pr03.doc_deltas", "audit/docdeltas/hde-epic034_doc_deltas.md") not in keys
    assert ("epic034.pr03.qa_meta_doc_deltas", "audit/qa/hde-epic034/00_meta/doc_deltas.md") not in keys
    assert ("keep", "artifacts/keep.txt") in keys


def test_epic034_pr02_request_shaping_check_index_row_does_not_claim_tests_pass() -> None:
    rows = {entry["artifact_key"]: entry for entry in indexer.EPIC034_PR02_PRIMARY_ARTIFACTS}

    row = rows["epic034.pr02.request_shaping_check"]
    assert row["tokens"] == ["EVIDENCE_PATH_PROOFS_OK"]
    assert "TESTS_PASS_OK" not in row["tokens"]
    assert "pytest" not in row["notes"].lower()
    assert "indexed separately" not in row["notes"].lower()


def test_epic034_response_mapping_snapshot_is_canonical_secret_safe_and_contract_derived() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    source_selection = _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json")
    request_shaping = _assert_canonical_json(VENDOR_DIR / "request_shaping.snapshot.json")
    ops = json.loads((ROOT / "audit" / "ops" / "hde-epic034" / "ops-01" / "fact_summary.json").read_text(encoding="utf-8"))
    snapshot = _assert_canonical_json(VENDOR_DIR / "response_mapping.snapshot.json")
    assert snapshot == generator.build_response_mapping_snapshot(snapshot["generated_at_utc"], contract, source_selection, request_shaping, ops)
    assert snapshot["response_envelope_mapping_scope"].startswith("HDE-FERM007.3")
    assert snapshot["live_vendor_call_claim"] == "NONE"
    assert snapshot["runtime_conformance_claim"] == "NONE"
    assert snapshot["public_reader_change_claim"] == "NONE"
    assert snapshot["open_rails_vendor_smoke_claim"] == "NONE"
    assert snapshot["normalized_data_path_proof_claim"] == "NONE"
    assert snapshot["ai_scope_claim"] == "NONE"
    assert snapshot["data_payload_body_emitted"] is False
    assert snapshot["no_compatibility_by_inference"] is True
    rendered = json.dumps(snapshot, sort_keys=True)
    for secret in ["api-key", "geo-key", "k_test", "Bearer api", "Bearer geo"]:
        assert secret not in rendered


def test_epic034_response_mapping_preserves_envelope_fields_and_route_variants() -> None:
    snapshot = _assert_canonical_json(VENDOR_DIR / "response_mapping.snapshot.json")
    routes = {row["endpoint_path"]: row for row in snapshot["routes"]}
    assert routes["/v2/charts"]["response_type"] == "ChartResult"
    assert routes["/v2/charts"]["data_schema"] == "ChartResult"
    assert routes["/v2/charts"]["route_variant"] == "full_chart"
    assert routes["/v2/charts/simple"]["response_type"] == "ChartSimpleResult"
    assert routes["/v2/charts/simple"]["data_schema"] == "ChartSimpleResult"
    assert routes["/v2/charts/simple"]["route_variant"] == "simple_chart"
    assert routes["/v2/charts/coordinates"]["response_type"] == "ChartResult"
    assert routes["/v2/charts/coordinates"]["route_variant"] == "coordinates_chart"
    for route in routes.values():
        assert set(["success", "errorCode", "type", "data"]) <= set(route["response_envelope_fields"])
        assert "StandardResponse.success" in route["success_status_handling"]
        assert "StandardResponse.errorCode" in route["errorCode_handling"]
        assert route["data_payload_identity_posture"].startswith("preserve data object identity")


def test_epic034_response_mapping_records_schema_gap_for_bodygraph_cache_and_compat() -> None:
    snapshot = _assert_canonical_json(VENDOR_DIR / "response_mapping.snapshot.json")
    posture = snapshot["internal_target_posture"]
    assert snapshot["schema_gap_status"] == "GAP_RECORDED"
    assert posture["bodygraph"]["mapping_result"] == "schema_gap_recorded"
    assert posture["cache"]["mapping_result"] == "not_truthfully_proven_for_v2_chart_data"
    assert posture["compatibility"]["mapping_result"] == "schema_gap_recorded"
    assert "adapter" in snapshot["schema_gap_summary"]
    assert snapshot["no_compatibility_by_inference"] is True


def test_epic034_response_mapping_check_log_exists_and_passes() -> None:
    log_path = ROOT / "audit" / "qa" / "hde-epic034" / "pr-03" / "response_mapping_check.log"
    raw = log_path.read_bytes()
    assert raw.endswith(b"\n")
    assert b"\r\n" not in raw
    log = raw.decode("utf-8")
    for check in [
        "closed_rails_generation", "no_live_vendor_call_attempted", "response_type_preservation",
        "success_status_handling", "errorCode_handling", "data_payload_identity_posture",
        "route_variant_preservation", "internal_target_posture_or_schema_gap_recorded",
        "internal_loci_inspected", "no_compatibility_by_inference_claim", "no_normalized_data_path_proof_claimed",
        "no_vendor_payload_bodies_emitted", "no_secret_values_emitted",
    ]:
        assert f"[{check}] status=PASS" in log
    assert "evidence_index_and_path_proof_posture=validated_by_update_evidence_index_and_validate_evidence_paths_not_generator" in log
    assert "status=PASS" in log


def test_epic034_response_mapping_rejects_unproven_data_schema() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    source_selection = _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json")
    request_shaping = _assert_canonical_json(VENDOR_DIR / "request_shaping.snapshot.json")
    ops = json.loads((ROOT / "audit" / "ops" / "hde-epic034" / "ops-01" / "fact_summary.json").read_text(encoding="utf-8"))
    broken = copy.deepcopy(contract)
    for route in broken["route_families"]:
        if route["path"] == "/v2/charts":
            route["success_envelope"] = "StandardResponse with type=ChartResult and data=BodygraphResponse"
    with pytest.raises(ValueError, match="RESPONSE_MAPPING_ROUTE_SCHEMA_MISMATCH"):
        generator.build_response_mapping_snapshot("2026-06-18T00:00:00Z", broken, source_selection, request_shaping, ops)


def test_epic034_response_mapping_rejects_route_specific_schema_drift_with_allowed_schema() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    source_selection = _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json")
    request_shaping = _assert_canonical_json(VENDOR_DIR / "request_shaping.snapshot.json")
    ops = json.loads((ROOT / "audit" / "ops" / "hde-epic034" / "ops-01" / "fact_summary.json").read_text(encoding="utf-8"))
    broken = copy.deepcopy(contract)
    for route in broken["route_families"]:
        if route["path"] == "/v2/charts/simple":
            route["success_envelope"] = "StandardResponse with type=ChartResult and data=ChartResult"
    with pytest.raises(ValueError, match="RESPONSE_MAPPING_ROUTE_SCHEMA_MISMATCH:/v2/charts/simple"):
        generator.build_response_mapping_snapshot("2026-06-18T00:00:00Z", broken, source_selection, request_shaping, ops)


def test_epic034_response_mapping_rejects_missing_standard_response_fields() -> None:
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    source_selection = _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json")
    request_shaping = _assert_canonical_json(VENDOR_DIR / "request_shaping.snapshot.json")
    ops = json.loads((ROOT / "audit" / "ops" / "hde-epic034" / "ops-01" / "fact_summary.json").read_text(encoding="utf-8"))
    broken = copy.deepcopy(contract)
    for route in broken["route_families"]:
        if route["path"] == "/v2/charts":
            route["response_envelope_fields"] = ["timestamp", "message", "type", "data"]
    with pytest.raises(ValueError, match="RESPONSE_MAPPING_ENVELOPE_FIELDS_MISSING:/v2/charts:success,errorCode"):
        generator.build_response_mapping_snapshot("2026-06-18T00:00:00Z", broken, source_selection, request_shaping, ops)


def test_epic034_contract_inventory_rejects_standard_response_field_drift() -> None:
    metadata, bodies = generator.load_source_cache()
    spec = generator.parse_yaml_openapi(bodies["v2_routes_yaml"], "v2-routes.yaml")
    spec["components"]["schemas"]["StandardResponse"]["required"].remove("success")
    with pytest.raises(ValueError, match="STANDARD_RESPONSE_FIELDS_MISSING:success"):
        generator.standard_response_fields(spec, version="v2")


def test_epic034_response_mapping_fails_when_internal_locus_missing(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    missing = "engine/bodygraph/missing_for_response_mapping.py"
    monkeypatch.setattr(generator, "RESPONSE_MAPPING_INTERNAL_LOCI", (missing,))
    contract = _assert_canonical_json(VENDOR_DIR / "contract_map.json")
    source_selection = _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json")
    request_shaping = _assert_canonical_json(VENDOR_DIR / "request_shaping.snapshot.json")
    ops = json.loads((ROOT / "audit" / "ops" / "hde-epic034" / "ops-01" / "fact_summary.json").read_text(encoding="utf-8"))
    with pytest.raises(ValueError, match="RESPONSE_MAPPING_INTERNAL_LOCUS_MISSING"):
        generator.build_response_mapping_snapshot("2026-06-18T00:00:00Z", contract, source_selection, request_shaping, ops)


def test_epic034_pr03_response_mapping_index_rows_use_approved_tokens_only() -> None:
    rows = {entry["artifact_key"]: entry for entry in indexer.EPIC034_PR03_PRIMARY_ARTIFACTS}
    approved = {
        "JSON_CANONICAL_CHECK_OK", "EVIDENCE_INDEX_UPDATED_OK", "MACHINE_MIRROR_UPDATED_OK",
        "EVIDENCE_PATHS_VALIDATED_OK", "EVIDENCE_PATH_PROOFS_OK", "TESTS_PASS_OK", "DOC_DELTA_PRESENT_OK",
    }
    assert set(rows["hdapi_v2.response_mapping"]["tokens"]) <= approved
    assert set(rows["epic034.pr03.response_mapping_check"]["tokens"]) <= approved
    assert set(rows["epic034.pr03.doc_deltas"]["tokens"]) <= approved
    assert set(rows["epic034.pr03.qa_meta_doc_deltas"]["tokens"]) <= approved
    assert "TESTS_PASS_OK" not in rows["epic034.pr03.response_mapping_check"]["tokens"]


def test_epic034_current_doc_deltas_are_not_indexed_as_pr01_after_pr03_update() -> None:
    pr01_rows = {entry["artifact_key"]: entry for entry in indexer.EPIC034_PR01_PRIMARY_ARTIFACTS}
    pr03_rows = {entry["artifact_key"]: entry for entry in indexer.EPIC034_PR03_PRIMARY_ARTIFACTS}
    assert "epic034.pr01.doc_deltas" not in pr01_rows
    assert "epic034.pr01.qa_meta_doc_deltas" not in pr01_rows
    assert pr03_rows["epic034.pr03.doc_deltas"]["record_type"] == "epic034_pr03_doc_delta"
    assert pr03_rows["epic034.pr03.qa_meta_doc_deltas"]["record_type"] == "epic034_pr03_doc_delta"


def test_epic034_adapter_boundary_proof_exists_and_passes() -> None:
    proof_path = VENDOR_DIR / "adapter_boundary_proof.log"
    proof = proof_path.read_text(encoding="utf-8")
    assert proof.endswith("\n")
    assert "\r\n" not in proof
    required = [
        "observed_adapter_http_home_posture=adapter package owns Flask HTTP home",
        "observed_presenter_emitter_posture=presenter/emitter remains byte-authoritative",
        "observed_vendor_seam_posture=engine.bodygraph.vendor_client remains sanctioned BodyGraph/vendor external-I/O seam",
        "no_second_http_home_claim=PASS",
        "no_adapter_bypass_claim=PASS",
        "no_presenter_bypass_claim=PASS",
        "no_ad_hoc_serialization_claim=PASS",
        "no_pure_compute_external_io_claim=PASS",
        "no_live_vendor_success_claim=NONE",
        "no_public_reader_change_claim=NONE",
        "no_open_rails_smoke_claim=NONE",
        "no_HDE-FERM007.5_claim=NONE",
        "no_HDE-FERM008_claim=NONE",
        "no_AI_scope_claim=NONE",
        "status=PASS",
    ]
    for needle in required:
        assert needle in proof


def test_epic034_boundary_check_log_exists_and_binds_prior_families() -> None:
    log_path = ROOT / "audit" / "qa" / "hde-epic034" / "pr-04" / "boundary_check.log"
    log = log_path.read_text(encoding="utf-8")
    assert log.endswith("\n")
    assert "\r\n" not in log
    for check in [
        "closed_rails_generation",
        "no_live_vendor_call_attempted",
        "adapter_http_home_posture_inspected",
        "presenter_emitter_posture_inspected",
        "vendor_seam_posture_inspected",
        "no_second_http_home_check_passed",
        "no_adapter_bypass_check_passed",
        "no_presenter_bypass_check_passed",
        "no_ad_hoc_serialization_check_passed",
        "no_pure_compute_external_io_check_passed",
        "pr01_pr02_pr03_pr04_evidence_family_binding_checked",
        "no_unsupported_scope_claim_emitted",
    ]:
        assert f"[{check}] status=PASS" in log
    assert "evidence_index_and_path_proof_posture=validated_by_update_evidence_index_and_validate_evidence_paths_not_generator" in log
    assert "status=PASS" in log


def test_epic034_adapter_boundary_builder_fails_closed_on_missing_locus(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", ("adapter/missing_for_boundary.py",))
    source_selection = _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json")
    request_shaping = _assert_canonical_json(VENDOR_DIR / "request_shaping.snapshot.json")
    response_mapping = _assert_canonical_json(VENDOR_DIR / "response_mapping.snapshot.json")
    with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_LOCUS_MISSING"):
        generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", source_selection, request_shaping, response_mapping)



def test_epic034_pr04_index_rows_use_approved_tokens_only() -> None:
    rows = {entry["artifact_key"]: entry for entry in json.loads((ROOT / "docs" / "evidence" / "INDEX.json").read_text(encoding="utf-8"))}
    approved = {"JSON_CANONICAL_CHECK_OK", "EVIDENCE_INDEX_UPDATED_OK", "MACHINE_MIRROR_UPDATED_OK", "EVIDENCE_PATHS_VALIDATED_OK", "EVIDENCE_PATH_PROOFS_OK", "TESTS_PASS_OK", "DOC_DELTA_PRESENT_OK"}
    for key in ["hdapi_v2.adapter_boundary_proof", "epic034.pr04.boundary_check", "epic034.pr04.doc_deltas", "epic034.pr04.qa_meta_doc_deltas"]:
        assert key in rows
        assert set(rows[key].get("tokens", [])) <= approved


def _epic034_boundary_inputs() -> tuple[dict, dict, dict]:
    return (
        _assert_canonical_json(VENDOR_DIR / "source_selection.snapshot.json"),
        _assert_canonical_json(VENDOR_DIR / "request_shaping.snapshot.json"),
        _assert_canonical_json(VENDOR_DIR / "response_mapping.snapshot.json"),
    )


def _write_boundary_temp(rel_dir: str, name: str, body: str) -> str:
    path = ROOT / rel_dir / name
    path.parent.mkdir(exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return path.relative_to(ROOT).as_posix()


def test_epic034_adapter_boundary_fails_closed_on_second_http_home_and_pure_io(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_vendor = _write_boundary_temp(rel_dir, "bad_vendor.py", "from flask import Flask\nfrom urllib import request as urlrequest\nALLOW_NETWORK='0'\nSAFE_MODE='1'\n")
        bad_compute = _write_boundary_temp(rel_dir, "bad_compute.py", "import requests\n")
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI", (bad_vendor,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PURE_COMPUTE_LOCI", (bad_compute,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_second_http_home.*no_pure_compute_external_io"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    "body",
    [
        "from flask import Flask\nimport requests\ndef route():\n    return requests.request('GET', 'https://example.invalid')\nSAFE_MODE='1'\n",
        "from flask import Flask\nimport requests\ndef route():\n    return requests.get('https://example.invalid')\nSAFE_MODE='1'\n",
        "from flask import Flask\nimport httpx\ndef route():\n    return httpx.Client().post('https://example.invalid')\nSAFE_MODE='1'\n",
        "from flask import Flask\nimport urllib.request\ndef route():\n    return urllib.request.urlopen('https://example.invalid')\nSAFE_MODE='1'\n",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_common_adapter_external_io(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "bad_adapter.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_requires_adapter_presenter_use_not_only_presenter_module(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "jsonify_adapter.py", "from flask import Flask, jsonify\napp = Flask(__name__)\nSAFE_MODE='1'\n@app.route('/bad')\ndef route():\n    return jsonify({'ok': True})\n")
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_json_dumps_serializer(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "serializer_adapter.py", "from flask import Flask\nfrom engine.presenter.emitter import emit_public\nimport json\ndef route():\n    return json.dumps({'ok': True})\nSAFE_MODE='1'\n")
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_ad_hoc_serialization"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_pr04_superseded_rows_are_removed_when_outputs_absent(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    stale_rows = [
        {"artifact_key": "hdapi_v2.adapter_boundary_proof", "discovered_physical_path": "artifacts/vendor/hdapi_v2/adapter_boundary_proof.log"},
        {"artifact_key": "epic034.pr04.boundary_check", "discovered_physical_path": "audit/qa/hde-epic034/pr-04/boundary_check.log"},
    ]
    human_index = tmp_path / "INDEX.json"
    human_index.write_text(json.dumps(stale_rows) + "\n", encoding="utf-8")
    monkeypatch.setattr(indexer, "ROOT", tmp_path)
    monkeypatch.setattr(indexer, "HUMAN_INDEX", human_index)
    rows = indexer._load_human_index()
    row_keys = {(row["artifact_key"], row["discovered_physical_path"]) for row in rows}
    assert not row_keys & indexer.EPIC034_PR04_SUPERSEDED_INDEX_KEYS


def test_epic034_adapter_boundary_proof_includes_compat_handler_locus() -> None:
    proof = (VENDOR_DIR / "adapter_boundary_proof.log").read_text(encoding="utf-8")
    assert "engine/http/compat_handler.py" in proof


@pytest.mark.parametrize(
    "body",
    [
        "from flask import Flask\nimport urllib3\ndef route():\n    return urllib3.PoolManager().request('GET', 'https://example.invalid')\nSAFE_MODE='1'\n",
        "from flask import Flask\nfrom urllib3 import PoolManager\ndef route():\n    return PoolManager().request('GET', 'https://example.invalid')\nSAFE_MODE='1'\n",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_urllib3_adapter_io(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "urllib3_adapter.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    "body",
    [
        "from flask import Flask\nfrom engine.presenter.emitter import emit_public\nimport json as j\ndef route():\n    return j.dumps({'ok': True})\nSAFE_MODE='1'\n",
        "from flask import Flask\nfrom engine.presenter.emitter import emit_public\nfrom json import dumps\ndef route():\n    return dumps({'ok': True})\nSAFE_MODE='1'\n",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_json_serializer_aliases(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "serializer_alias_adapter.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_ad_hoc_serialization"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_detects_one_route_bypassing_presenter_among_good_routes(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, jsonify
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
def bad():
    return jsonify({'ok': True})
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "mixed_routes.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    "body",
    [
        "import socket\ndef compute():\n    return socket.create_connection(('example.invalid', 443))\n",
        "import subprocess\ndef compute():\n    return subprocess.run(['curl', 'https://example.invalid'])\n",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_non_http_pure_compute_io(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_compute = _write_boundary_temp(rel_dir, "bad_compute.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PURE_COMPUTE_LOCI", (bad_compute,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_pure_compute_external_io"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    "body",
    [
        "from starlette.applications import Starlette\nfrom urllib import request as urlrequest\nALLOW_NETWORK='0'\nSAFE_MODE='1'\n",
        "import fastapi.routing\nfrom urllib import request as urlrequest\nALLOW_NETWORK='0'\nSAFE_MODE='1'\n",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_vendor_http_home_submodules(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_vendor = _write_boundary_temp(rel_dir, "bad_vendor_home.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI", (bad_vendor,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_second_http_home"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_when_presenter_uses_json_dumps(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_presenter = _write_boundary_temp(rel_dir, "bad_presenter.py", "import json\ndef emit_public(payload):\n    return json.dumps(payload).encode('utf-8')\n")
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PRESENTER_LOCI", (bad_presenter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_ad_hoc_serialization"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_uses_in_memory_prior_evidence_when_files_absent(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    adapter_dir = tmp_path / "adapter"
    adapter_dir.mkdir()
    presenter_dir = tmp_path / "engine" / "presenter"
    presenter_dir.mkdir(parents=True)
    vendor_dir = tmp_path / "engine" / "bodygraph"
    vendor_dir.mkdir(parents=True)
    compat_dir = tmp_path / "engine" / "compat"
    compat_dir.mkdir(parents=True)
    (adapter_dir / "app.py").write_text("from flask import Flask\nfrom engine.presenter.emitter import emit_public\nSAFE_MODE='1'\ndef route():\n    return emit_public({'ok': True})\n", encoding="utf-8")
    (presenter_dir / "emitter.py").write_text("def emit_public(payload):\n    return b'{}\\n'\n", encoding="utf-8")
    (vendor_dir / "vendor.py").write_text("from urllib import request as urlrequest\nALLOW_NETWORK='0'\nSAFE_MODE='1'\n", encoding="utf-8")
    (compat_dir / "compute.py").write_text("def compute():\n    return {}\n", encoding="utf-8")
    monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", ("adapter/app.py",))
    monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PRESENTER_LOCI", ("engine/presenter/emitter.py",))
    monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI", ("engine/bodygraph/vendor.py",))
    monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PURE_COMPUTE_LOCI", ("engine/compat/compute.py",))
    proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    assert checks["prior_evidence_families_bound"] is True
    assert "status=PASS" in proof


@pytest.mark.parametrize(
    "body",
    [
        "from flask import Flask\nimport socket\ndef route():\n    return socket.create_connection(('example.invalid', 443))\nSAFE_MODE='1'\n",
        "from flask import Flask\nimport subprocess\ndef route():\n    return subprocess.run(['curl', 'https://example.invalid'])\nSAFE_MODE='1'\n",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_adapter_socket_or_subprocess_io(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "adapter_non_http_io.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    "body",
    [
        "from flask import Flask\nfrom requests import get as rget\ndef route():\n    return rget('https://example.invalid')\nSAFE_MODE='1'\n",
        "from flask import Flask\nfrom urllib.request import urlopen as open_url\ndef route():\n    return open_url('https://example.invalid')\nSAFE_MODE='1'\n",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_aliased_http_helpers(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "aliased_http.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    "route_body",
    [
        "return {'ok': True}",
        "return [1, 2, 3]",
        "return make_response({'ok': True})",
        "return current_app.json.response({'ok': True})",
        "return Response('{\\\"ok\\\":true}', mimetype='application/json')",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_flask_implicit_json_responses(monkeypatch: pytest.MonkeyPatch, route_body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = f"""
from flask import Flask, Response, current_app, make_response
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({{'ok': True}})
@app.route('/bad')
def bad():
    {route_body}
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "implicit_json.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_detects_deep_helper_chain_presenter_bypass(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, jsonify
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
def helper2():
    return jsonify({'ok': True})
def helper1():
    return helper2()
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
def bad():
    return helper1()
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "deep_bypass.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_ignores_nested_closure_emit_public(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, jsonify
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/bad')
def bad():
    def nested_presenter():
        return emit_public({'ok': True})
    return jsonify({'ok': True})
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "nested_closure.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_checks_errorhandler_routes(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, jsonify
app = Flask(__name__)
SAFE_MODE='1'
@app.errorhandler(500)
def error_handler(exc):
    return jsonify({'error': 'boom'}), 500
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "errorhandler.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_alternate_json_branch(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, jsonify, request
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/maybe')
def maybe():
    if request.args.get('bad'):
        return jsonify({'ok': False})
    return emit_public({'ok': True})
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "alternate_branch.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_pr04_doc_delta_rows_supersede_pr03_doc_delta_rows() -> None:
    rows = {entry["artifact_key"]: entry for entry in json.loads((ROOT / "docs" / "evidence" / "INDEX.json").read_text(encoding="utf-8"))}
    assert "epic034.pr04.doc_deltas" in rows
    assert "epic034.pr04.qa_meta_doc_deltas" in rows
    assert "epic034.pr03.doc_deltas" not in rows
    assert "epic034.pr03.qa_meta_doc_deltas" not in rows


@pytest.mark.parametrize(
    "body",
    [
        "from flask import Flask\nimport requests\ndef route():\n    session = requests.Session()\n    return session.get('https://example.invalid')\nSAFE_MODE='1'\n",
        "from flask import Flask\nimport requests\ndef route():\n    session = requests.Session()\n    return session.post('https://example.invalid')\nSAFE_MODE='1'\n",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_session_variable_io(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "session_adapter.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_aliased_flask_jsonify(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from flask import jsonify as js
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/bad')
def bad():
    return js({'ok': True})
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "aliased_jsonify.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_checks_before_request_hooks(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
app = Flask(__name__)
SAFE_MODE='1'
@app.before_request
def guard():
    return {'error': 'blocked'}
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "before_request.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_helper_returning_dict(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
def helper():
    return {'ok': False}
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
def bad():
    return helper()
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "helper_dict.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_typed_session_variable_io(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
import requests
SAFE_MODE='1'
def route():
    session: requests.Session = requests.Session()
    return session.get('https://example.invalid')
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "typed_session_adapter.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_checks_add_url_rule_views(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, jsonify
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
def bad():
    return jsonify({'ok': False})
app.add_url_rule('/bad', 'bad', bad)
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "add_url_rule.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_helper_returned_via_local_variable(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
def helper():
    return {'ok': False}
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
def bad():
    resp = helper()
    return resp
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "local_var_helper.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_stdlib_http_client(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
import http.client
SAFE_MODE='1'
def route():
    conn = http.client.HTTPSConnection('example.invalid')
    conn.request('GET', '/')
    return 'ok'
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "stdlib_http_client.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_direct_canonical_bytes_response(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, Response
from engine.presenter.emitter import emit_public
from engine.util import canon
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
def bad():
    return Response(canon.sercanon({'ok': False}), mimetype='application/json')
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "canonical_response.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_vendor_guard_ignores_comment_only_safe_mode_mentions(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from urllib import request as urlrequest
# SAFE_MODE and ALLOW_NETWORK are mentioned here only, not as a guard.
def fetch():
    return urlrequest.urlopen('https://example.invalid')
"""
    try:
        bad_vendor = _write_boundary_temp(rel_dir, "unguarded_vendor.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI", (bad_vendor,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_VENDOR_GUARD_UNEXPECTED"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_boundary_fails_closed_on_prior_unsupported_scope_claim() -> None:
    source_selection, request_shaping, response_mapping = _epic034_boundary_inputs()
    drifted = dict(request_shaping)
    drifted["live_vendor_call_claim"] = "CLAIMED"
    with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_unsupported_scope_claim"):
        generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", source_selection, drifted, response_mapping)
