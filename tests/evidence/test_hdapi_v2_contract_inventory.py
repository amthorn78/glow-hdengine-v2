from __future__ import annotations

import copy
import csv
import json
from pathlib import Path
from typing import Any

import pytest

from tools.evidence import generate_hdapi_v2_contract_inventory as generator
from tools.evidence import hdapi_v2_boundary_analyzer as boundary_analyzer
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


W003_REQUIRED_TAXONOMY_GROUPS = set(boundary_analyzer.REQUIRED_BOUNDARY_TAXONOMY_GROUPS)
W003_TAXONOMY_ROWS = [
    {
        "case_id": "W003-route-registration-direct-blueprint-hooks",
        "group": "route_registration_surfaces",
        "description": "direct route decorators, blueprint registration, error handlers, and request hooks are analyzer-owned route-registration evidence",
        "fixture": "current_repo",
        "locus_type": "adapter",
        "expected_classification": boundary_analyzer.BOUNDARY_ALLOWED,
        "expected_verdict": "PASS",
        "expected_category": "adapter_route_registration",
        "proof_fragment": "discovered Flask adapter registrations",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-public-route-signature-baseline",
        "group": "public_route_signatures",
        "description": "path/method/endpoint/source public signatures reconcile only through analyzer baseline truth",
        "fixture": "current_repo",
        "locus_type": "adapter",
        "expected_classification": boundary_analyzer.BOUNDARY_ALLOWED,
        "expected_verdict": "PASS",
        "expected_category": "public_routes",
        "proof_fragment": "reconcile with governed PR-04 baseline",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-route-drift-fail-closed",
        "group": "public_route_signatures",
        "description": "unreconciled public route drift remains unknown / fail-closed for W-004 follow-up, never PASS",
        "fixture": "unexpected_public_route",
        "locus_type": "adapter",
        "expected_classification": boundary_analyzer.BOUNDARY_UNKNOWN,
        "expected_verdict": "UNKNOWN",
        "expected_category": "public_routes",
        "proof_fragment": "route drift fails closed",
        "scope": "W-004 follow-up visible",
    },
    {
        "case_id": "W003-response-producing-presenter-valid",
        "group": "response_producing_paths",
        "description": "public response-producing paths require analyzer-proven presenter/emitter provenance",
        "fixture": "current_repo",
        "locus_type": "adapter",
        "expected_classification": boundary_analyzer.BOUNDARY_ALLOWED,
        "expected_verdict": "PASS",
        "expected_category": "response_producing_paths",
        "proof_fragment": "explicit presenter/emitter provenance",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-presenter-valid-cross-file-helper",
        "group": "presenter_valid_paths",
        "description": "valid presenter/emitter and helper provenance must be owned by the analyzer",
        "fixture": "current_repo",
        "locus_type": "adapter",
        "expected_classification": boundary_analyzer.BOUNDARY_ALLOWED,
        "expected_verdict": "PASS",
        "expected_category": "presenter_provenance",
        "proof_fragment": "sanctioned presenter/emitter calls",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-presenter-bypass-raw-string",
        "group": "presenter_bypass_paths",
        "description": "raw public route responses are presenter bypasses and cannot render as PASS",
        "fixture": "plain_response_route",
        "locus_type": "adapter",
        "expected_classification": boundary_analyzer.BOUNDARY_FORBIDDEN,
        "expected_verdict": "FAIL",
        "expected_category": "presenter_provenance",
        "proof_fragment": "presenter provenance is not proven",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-serializer-family-direct-json",
        "group": "serializer_families",
        "description": "direct ad-hoc JSON serializer families are forbidden outside allowed helpers",
        "fixture": "direct_json_serializer",
        "locus_type": "adapter",
        "expected_classification": boundary_analyzer.BOUNDARY_FORBIDDEN,
        "expected_verdict": "FAIL",
        "expected_category": "serializer_paths",
        "proof_fragment": "ad-hoc serializer path",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-external-io-alias-family",
        "group": "external_io_families",
        "description": "adapter HTTP client aliases and direct external-I/O families remain forbidden outside the vendor seam",
        "fixture": "adapter_requests_alias",
        "locus_type": "adapter",
        "expected_classification": boundary_analyzer.BOUNDARY_FORBIDDEN,
        "expected_verdict": "FAIL",
        "expected_category": "external_io_paths",
        "proof_fragment": "outside sanctioned vendor seam",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-import-alias-shadowing",
        "group": "import_and_alias_forms",
        "description": "import aliases and local shadowing are classified by analyzer provenance instead of renderer assumptions",
        "fixture": "fake_emit_fn",
        "locus_type": "adapter",
        "expected_classification": boundary_analyzer.BOUNDARY_FORBIDDEN,
        "expected_verdict": "FAIL",
        "expected_category": "presenter_provenance",
        "proof_fragment": "presenter provenance is not proven",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-cross-file-helper-chain",
        "group": "cross_file_helper_chains",
        "description": "helper pass-through chains are allowed only when presenter provenance remains proven",
        "fixture": "current_repo",
        "locus_type": "adapter",
        "expected_classification": boundary_analyzer.BOUNDARY_ALLOWED,
        "expected_verdict": "PASS",
        "expected_category": "presenter_provenance",
        "proof_fragment": "sanctioned presenter/emitter calls",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-vendor-guard-provenance",
        "group": "vendor_guard_provenance",
        "description": "vendor external-I/O must be tied to closed-rails guard provenance",
        "fixture": "current_repo",
        "locus_type": "vendor_seam",
        "expected_classification": boundary_analyzer.BOUNDARY_ALLOWED,
        "expected_verdict": "PASS",
        "expected_category": "guard_provenance",
        "proof_fragment": "closed-rails guard entrypoint",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-pure-compute-forbidden-operation",
        "group": "pure_compute_forbidden_operations",
        "description": "pure compute external-I/O operations are forbidden or fail-closed rather than presenter PASS",
        "fixture": "pure_compute_requests",
        "locus_type": "pure_compute",
        "expected_classification": boundary_analyzer.BOUNDARY_FORBIDDEN,
        "expected_verdict": "FAIL",
        "expected_category": "pure_compute_external_io",
        "proof_fragment": "pure compute external-I/O capability",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-public-internal-route-classification",
        "group": "public_internal_route_classification",
        "description": "internal/dev route posture is excluded from public signature claims while public drift stays fail-closed",
        "fixture": "current_repo",
        "locus_type": "adapter",
        "expected_classification": boundary_analyzer.BOUNDARY_ALLOWED,
        "expected_verdict": "PASS",
        "expected_category": "public_routes",
        "proof_fragment": "governed PR-04 baseline",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-pr01-pr04-evidence-family-binding",
        "group": "evidence_family_binding",
        "description": "PR-01 through PR-04 evidence-family binding remains analyzer-owned with index/path-proof validation delegated",
        "fixture": "current_repo",
        "locus_type": "evidence_tool",
        "expected_classification": boundary_analyzer.BOUNDARY_ALLOWED,
        "expected_verdict": "PASS",
        "expected_category": "evidence_binding_posture",
        "proof_fragment": "PR-01/PR-02/PR-03 dependency payloads are present",
        "scope": "W-003 in scope",
    },
    {
        "case_id": "W003-unsupported-scope-out-of-scope-visible",
        "group": "unsupported_scope_no_claims",
        "description": "HDE-FERM007.5, HDE-FERM008, runtime/live/open-rails/public-reader/new-home/AI scope remains visibly out of scope",
        "fixture": "current_repo",
        "locus_type": "evidence_tool",
        "expected_classification": boundary_analyzer.BOUNDARY_OUT_OF_SCOPE,
        "expected_verdict": "PASS",
        "expected_category": "hde_ferm007_5_runtime_v2_live_open_rails_ai_scope",
        "proof_fragment": "outside W-003 / HDE-FERM007.4",
        "scope": "follow-up/out of scope visible",
    },
]


def _finding_by_category(result: dict[str, Any], category: str) -> dict[str, Any]:
    return next(finding for finding in result["findings"] if finding["category"] == category)


def _w003_result_for_row(row: dict[str, str]) -> dict[str, Any]:
    import shutil

    source_selection, request_shaping, response_mapping = _epic034_boundary_inputs()
    rel_dir = "tmp_boundary_test"
    fixture = row["fixture"]
    bodies = {
        "unexpected_public_route": ("unexpected_public_route.py", "from flask import Flask\nfrom engine.presenter.emitter import emit_public\napp = Flask(__name__)\nSAFE_MODE='1'\n@app.route('/unexpected-public')\ndef unexpected_public():\n    return emit_public({'ok': True})\n"),
        "plain_response_route": ("plain_response_route.py", "from flask import Flask\nfrom engine.presenter.emitter import emit_public\napp = Flask(__name__)\nSAFE_MODE='1'\n@app.route('/good')\ndef good():\n    return emit_public({'ok': True})\n@app.route('/plain')\ndef plain():\n    return 'plain text response'\n"),
        "direct_json_serializer": ("direct_json_serializer.py", "import json\nfrom flask import Flask\nfrom engine.presenter.emitter import emit_public\napp = Flask(__name__)\nSAFE_MODE='1'\n@app.route('/good')\ndef good():\n    return emit_public({'ok': True})\ndef helper(payload):\n    return json.dumps(payload)\n"),
        "adapter_requests_alias": ("adapter_requests_alias.py", "import requests as rq\nfrom flask import Flask\nfrom engine.presenter.emitter import emit_public\napp = Flask(__name__)\nSAFE_MODE='1'\n@app.route('/good')\ndef good():\n    return emit_public({'ok': True})\ndef leak():\n    return rq.get('https://vendor.test')\n"),
        "fake_emit_fn": ("fake_emit_fn.py", "from flask import Flask\napp = Flask(__name__)\nSAFE_MODE='1'\ndef emit_fn(payload):\n    return 'plain'\n@app.route('/bad')\ndef bad():\n    return emit_fn({'ok': False})\n"),
        "pure_compute_requests": ("pure_compute_requests.py", "import requests\ndef compute():\n    return requests.get('https://vendor.test')\n"),
    }
    if fixture == "current_repo":
        return _epic034_analyzer_result()
    try:
        name, body = bodies[fixture]
        rel = _write_boundary_temp(rel_dir, name, body)
        adapter_loci = (rel,) if row["locus_type"] == "adapter" else generator.ADAPTER_BOUNDARY_ADAPTER_LOCI
        pure_loci = (rel,) if row["locus_type"] == "pure_compute" else generator.ADAPTER_BOUNDARY_PURE_COMPUTE_LOCI
        baseline = tuple(boundary_analyzer._adapter_public_route_signatures(adapter_loci))
        if fixture == "unexpected_public_route":
            baseline = ("adapter/other.py:app.route:/expected:GET:expected",)
        return boundary_analyzer.analyze_adapter_boundary(
            source_selection=source_selection,
            request_shaping=request_shaping,
            response_mapping=response_mapping,
            adapter_loci=adapter_loci,
            canonical_adapter_loci=generator.ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI,
            presenter_loci=generator.ADAPTER_BOUNDARY_PRESENTER_LOCI,
            vendor_seam_loci=generator.ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI,
            pure_compute_loci=pure_loci,
            public_route_baseline=baseline,
            evidence_tool_loci=("tools/evidence/generate_hdapi_v2_contract_inventory.py", "tools/evidence/hdapi_v2_boundary_analyzer.py"),
        )
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w003_taxonomy_required_groups_are_complete_and_visible() -> None:
    groups = {row["group"] for row in W003_TAXONOMY_ROWS}
    assert groups >= W003_REQUIRED_TAXONOMY_GROUPS
    result = _epic034_analyzer_result()
    assert set(result["required_taxonomy_groups"]) == W003_REQUIRED_TAXONOMY_GROUPS
    assert result["missing_taxonomy_groups"] == []
    assert set(result["boundary_taxonomy"]) == W003_REQUIRED_TAXONOMY_GROUPS
    assert result["checks"]["table_driven_boundary_taxonomy_applied"] is True
    assert result["checks"]["required_taxonomy_groups_visible"] is True
    for group, row in result["boundary_taxonomy"].items():
        expected_case_classes = set(boundary_analyzer.BOUNDARY_TAXONOMY_REQUIRED_CASE_CLASSIFICATIONS[group])
        assert set(row["required_case_classifications"]) == expected_case_classes
        assert row["coverage_status"] == "covered_by_w003_invariant_suite"
        assert "classification" not in row
        assert "verdict" not in row


def test_epic034_w003_taxonomy_covers_all_classifications_and_fail_closed() -> None:
    classifications = {row["expected_classification"] for row in W003_TAXONOMY_ROWS}
    assert classifications == {
        boundary_analyzer.BOUNDARY_ALLOWED,
        boundary_analyzer.BOUNDARY_FORBIDDEN,
        boundary_analyzer.BOUNDARY_UNKNOWN,
        boundary_analyzer.BOUNDARY_OUT_OF_SCOPE,
    }
    for row in W003_TAXONOMY_ROWS:
        if row["expected_classification"] in {boundary_analyzer.BOUNDARY_UNKNOWN, boundary_analyzer.BOUNDARY_FORBIDDEN}:
            finding = boundary_analyzer.boundary_finding(row["expected_category"], row["expected_classification"], "PASS", ["synthetic.py"], row["description"])
            assert boundary_analyzer.finding_passes(finding) is False, row["case_id"]


def test_epic034_w003_taxonomy_rendering_does_not_relabel_negative_groups_as_current_pass() -> None:
    proof, _checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    assert "boundary_taxonomy group=presenter_bypass_paths finding_category=presenter_provenance classification=allowed verdict=PASS" not in proof
    assert "boundary_taxonomy group=pure_compute_forbidden_operations finding_category=pure_compute_external_io classification=allowed verdict=PASS" not in proof
    assert "boundary_taxonomy group=presenter_bypass_paths" in proof
    assert "required_case_classifications=[\"forbidden\",\"unknown / fail-closed\"]" in proof
    assert "coverage_status=covered_by_w003_invariant_suite" in proof
    assert "presenter_bypass_path_taxonomy_verdict=covered:PASS required_case_classifications=[\"forbidden\",\"unknown / fail-closed\"]" in proof
    assert "presenter_bypass_path_taxonomy_verdict=covered:PASS current=allowed:PASS" not in proof


@pytest.mark.parametrize("row", W003_TAXONOMY_ROWS, ids=[row["case_id"] for row in W003_TAXONOMY_ROWS])
def test_epic034_w003_taxonomy_rows_are_analyzer_owned(row: dict[str, str]) -> None:
    result = _w003_result_for_row(row)
    finding = _finding_by_category(result, row["expected_category"])
    assert finding["classification"] == row["expected_classification"]
    assert finding["verdict"] == row["expected_verdict"]
    assert row["proof_fragment"] in finding["reason"]
    if finding["classification"] == boundary_analyzer.BOUNDARY_ALLOWED:
        assert finding["details"] or row["expected_category"] in {"serializer_paths", "pure_compute_external_io", "evidence_binding_posture"}
    if finding["classification"] in {boundary_analyzer.BOUNDARY_UNKNOWN, boundary_analyzer.BOUNDARY_FORBIDDEN}:
        assert result["verdict_status"] != "PASS"



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


def test_epic034_adapter_boundary_fails_closed_on_aiohttp_adapter_call(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
import aiohttp
SAFE_MODE='1'
def route():
    session = aiohttp.ClientSession()
    return session.get('https://example.invalid')
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "aiohttp_adapter.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_flask_tuple_json_response(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
def bad():
    return {'error': 'blocked'}, 400
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "tuple_response.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_pure_compute_detects_imported_os_system(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from os import system
def compute():
    return system('curl https://example.invalid')
"""
    try:
        bad_compute = _write_boundary_temp(rel_dir, "imported_system_compute.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PURE_COMPUTE_LOCI", (bad_compute,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_pure_compute_external_io"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_vendor_guard_fails_on_local_session_fetch_path(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
import requests
from urllib import request as urlrequest
def guarded_entry(env):
    if env.get('SAFE_MODE') and not env.get('ALLOW_NETWORK'):
        raise RuntimeError('refused')
def fetch():
    session = requests.Session()
    return session.get('https://example.invalid')
"""
    try:
        bad_vendor = _write_boundary_temp(rel_dir, "vendor_session_fetch.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI", (bad_vendor,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_VENDOR_GUARD_UNEXPECTED"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    "body",
    [
        """
import requests
SAFE_MODE='1'
def route(req):
    session = requests.Session()
    return session.send(req)
""",
        """
import httpx
SAFE_MODE='1'
def route():
    return httpx.stream('GET', 'https://example.invalid')
""",
        """
import httpx
SAFE_MODE='1'
def route():
    client = httpx.AsyncClient()
    return client.get('https://example.invalid')
""",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_send_stream_async_client(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "adapter_http_variants.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_module_qualified_flask_response(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
import flask
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
def bad():
    return flask.Response('{\"ok\":true}', mimetype='application/json')
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "flask_response.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_checks_blueprint_app_errorhandler(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Blueprint, Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
bp = Blueprint('bp', __name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
@bp.app_errorhandler(404)
def not_found(error):
    return {'error': 'missing'}, 404
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "bp_errorhandler.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_checks_after_request_hooks(monkeypatch: pytest.MonkeyPatch) -> None:
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
@app.after_request
def rewrite(response):
    return jsonify({'rewritten': True})
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "after_request.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    "body",
    [
        """
from os import popen
SAFE_MODE='1'
def route():
    return popen('curl https://example.invalid').read()
""",
        """
import subprocess
SAFE_MODE='1'
def route():
    return subprocess.check_output(['curl', 'https://example.invalid'])
""",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_shell_out_helpers(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "adapter_shell_out.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_follows_async_awaited_helper(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, jsonify
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
async def helper():
    return jsonify({'ok': False})
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
async def bad():
    return await helper()
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "async_await_helper.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_local_jsonish_return(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
def bad():
    resp = {'ok': False}
    return resp
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "local_jsonish.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_response_keyword_json(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, Response
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
def bad():
    return Response(response='{\"ok\":false}', mimetype='application/json')
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "response_keyword.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_pure_compute_detects_os_popen(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from os import popen
def compute():
    return popen('curl https://example.invalid').read()
"""
    try:
        bad_compute = _write_boundary_temp(rel_dir, "popen_compute.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PURE_COMPUTE_LOCI", (bad_compute,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_pure_compute_external_io"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    "body",
    [
        """
from urllib import request as urlrequest
import socket
def guarded_entry(env):
    if env.get('SAFE_MODE') and not env.get('ALLOW_NETWORK'):
        raise RuntimeError('refused')
def fetch():
    return socket.create_connection(('example.invalid', 443))
""",
        """
from urllib import request as urlrequest
import subprocess
def guarded_entry(env):
    if env.get('SAFE_MODE') and not env.get('ALLOW_NETWORK'):
        raise RuntimeError('refused')
def fetch():
    return subprocess.check_output(['curl', 'https://example.invalid'])
""",
    ],
)
def test_epic034_vendor_guard_fails_on_socket_or_subprocess_fetch(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_vendor = _write_boundary_temp(rel_dir, "vendor_non_http_fetch.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI", (bad_vendor,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_VENDOR_GUARD_UNEXPECTED"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    "body",
    [
        """
import requests
SAFE_MODE='1'
def route():
    with requests.Session() as session:
        return session.get('https://example.invalid')
""",
        """
import aiohttp
SAFE_MODE='1'
async def route():
    async with aiohttp.ClientSession() as session:
        return await session.post('https://example.invalid')
""",
    ],
)
def test_epic034_adapter_boundary_fails_closed_on_context_managed_clients(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "context_client.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_imported_build_opener(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from urllib.request import build_opener
SAFE_MODE='1'
def route(req):
    opener = build_opener()
    return opener.open(req)
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "build_opener_adapter.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_attribute_client(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
import requests
SAFE_MODE='1'
class Adapter:
    def __init__(self):
        self.session = requests.Session()
adapter = Adapter()
def route():
    return adapter.session.get('https://example.invalid')
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "attribute_client.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_adapter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    "body",
    [
        """
import orjson
def emit_public(payload):
    return orjson.dumps(payload)
""",
        """
import simplejson
def emit_public(payload):
    return simplejson.dumps(payload).encode('utf-8')
""",
    ],
)
def test_epic034_ad_hoc_serialization_detects_nonstdlib_json_modules(monkeypatch: pytest.MonkeyPatch, body: str) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        bad_presenter = _write_boundary_temp(rel_dir, "bad_presenter.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PRESENTER_LOCI", (bad_presenter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_ad_hoc_serialization"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_checks_class_based_add_url_rule(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, jsonify
from flask.views import MethodView
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
class Bad(MethodView):
    def get(self):
        return jsonify({'ok': False})
app.add_url_rule('/bad', view_func=Bad.as_view('bad'))
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "class_view.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_emitter_accepts_module_qualified_calls(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter import emitter
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emitter.emit_public_with_envelope({'ok': True})
"""
    try:
        good_adapter = _write_boundary_temp(rel_dir, "qualified_presenter.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (good_adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((good_adapter,))))
        proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
        assert checks["presenter_emitter_inspected"] is True
        assert "[presenter_emitter_inspected] status=PASS" in proof
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_raw_json_bytes_response(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = r"""
from flask import Flask, Response
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
def bad():
    return Response(b'{"ok":false}\n', mimetype='application/json')
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "raw_json_bytes_response.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_public_route_drift(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/reader')
def reader():
    return emit_public({'ok': True})
@app.route('/reader/new')
def new_reader():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "route_drift.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(
            generator,
            "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE",
            (f"{adapter}:app.route:/reader::reader",),
        )
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_public_reader_change"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_keeps_methodview_methods_qualified(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, jsonify
from flask.views import MethodView
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
class Bad(MethodView):
    def get(self):
        return jsonify({'ok': False})
class Good(MethodView):
    def get(self):
        return emit_public({'ok': True})
app.add_url_rule('/bad', view_func=Bad.as_view('bad'))
app.add_url_rule('/good', view_func=Good.as_view('good'))
"""
    try:
        bad_adapter = _write_boundary_temp(rel_dir, "methodview_collision.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (bad_adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_respects_methodview_add_url_rule_methods(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, jsonify
from flask.views import MethodView
from engine.presenter.emitter import emit_public
app = Flask(__name__)
class Mixed(MethodView):
    def get(self):
        return emit_public({'ok': True})
    def post(self):
        return jsonify({'ok': False})
app.add_url_rule('/mixed', view_func=Mixed.as_view('mixed'), methods=['GET'])
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "methodview_get_only.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
        assert checks["no_presenter_bypass"] is True
        assert "[no_presenter_bypass] status=PASS" in proof
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_blueprint_prefix_drift(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, Blueprint
from engine.presenter.emitter import emit_public
app = Flask(__name__)
bp = Blueprint('reader', __name__)
SAFE_MODE='1'
@bp.get('/reader')
def reader():
    return emit_public({'ok': True})
app.register_blueprint(bp, url_prefix='/v2')
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "blueprint_prefix.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(
            generator,
            "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE",
            (
                f"{adapter}:bp.get:/reader:GET:reader",
                f"{adapter}:register_blueprint:bp:",
            ),
        )
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_public_reader_change"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_public_route_signatures_include_blueprint_constructor_prefix() -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Blueprint
bp = Blueprint('reader', __name__, url_prefix='/v2')
@bp.get('/reader')
def reader():
    return b'ok'
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "blueprint_constructor_prefix.py", body)
        signatures = boundary_analyzer._adapter_public_route_signatures((adapter,))
        assert any(f"locus={adapter};registration=decorator;decorator=bp.get;path=/v2/reader;methods=GET;endpoint=reader" in item for item in signatures)
        assert f"{adapter}:bp.get:/reader:GET:reader" not in signatures
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_route_methods_drift(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/reader', methods=['GET', 'POST'])
def reader():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "method_drift.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(
            generator,
            "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE",
            (f"{adapter}:app.route:/reader:GET:reader",),
        )
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_public_reader_change"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_allows_make_response_wrapping_presenter(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, make_response
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return make_response(emit_public({'ok': True}), 202)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "make_response_presenter.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
        assert checks["no_presenter_bypass"] is True
        assert "[no_presenter_bypass] status=PASS" in proof
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_rejects_make_response_raw_body_with_presenter_status(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, make_response
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.route('/bad')
def bad():
    return make_response('raw', emit_public({'ok': True}))
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "make_response_raw_body.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_json_variable_response(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = r"""
from flask import Flask, Response
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/bad')
def bad():
    body = b'{"ok":false}\n'
    return Response(body, mimetype='application/json')
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "json_variable_response.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_call_must_resolve_to_sanctioned_import(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = r"""
from flask import Flask, Response
app = Flask(__name__)
SAFE_MODE='1'
def emit_public(payload):
    return b'{"ok":false}\n'
@app.route('/bad')
def bad():
    return Response(emit_public({'ok': False}), mimetype='application/json')
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "fake_emit_public.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*presenter_emitter_inspected"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_bypass_detects_imported_adapter_helper(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    helper_path = ROOT / "adapter" / "boundary_tmp_helper.py"
    route_path = ROOT / "adapter" / "boundary_tmp_route.py"
    try:
        helper_path.write_text(
            "from flask import jsonify\n"
            "def bad_response():\n"
            "    return jsonify({'ok': False})\n",
            encoding="utf-8",
        )
        route_path.write_text(
            "from flask import Flask\n"
            "from engine.presenter.emitter import emit_public\n"
            "from adapter.boundary_tmp_helper import bad_response\n"
            "app = Flask(__name__)\n"
            "SAFE_MODE='1'\n"
            "@app.route('/good')\n"
            "def good():\n"
            "    return emit_public({'ok': True})\n"
            "@app.route('/bad')\n"
            "def bad():\n"
            "    return bad_response()\n",
            encoding="utf-8",
        )
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", ("adapter/boundary_tmp_route.py", "adapter/boundary_tmp_helper.py"))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        helper_path.unlink(missing_ok=True)
        route_path.unlink(missing_ok=True)


def test_epic034_vendor_guard_symbols_ignore_docstrings(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
def fetch():
    \"\"\"Mentions SAFE_MODE and ALLOW_NETWORK without enforcing rails.\"\"\"
    raise RuntimeError('unrelated')
"""
    try:
        rel = _write_boundary_temp(rel_dir, "docstring_guard.py", body)
        assert boundary_analyzer._vendor_guard_entrypoints((rel,)) == []
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_plain_response_without_presenter(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/good')
def good():
    return emit_public({'ok': True})
@app.route('/plain')
def plain():
    return 'plain text response'
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "plain_response_route.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_before_request_plain_response(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.before_request
def maintenance():
    return 'maintenance'
@app.route('/good')
def good():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "plain_before_request.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_nested_plain_route(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
def make_app():
    app = Flask(__name__)
    SAFE_MODE='1'
    @app.route('/good')
    def good():
        return emit_public({'ok': True})
    @app.route('/nested')
    def nested():
        return 'plain nested response'
    return app
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "nested_plain_route.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_when_presenter_call_is_not_returned(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/unused')
def unused():
    emit_public({'unused': True})
    return 'plain response after unused presenter call'
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "unused_presenter_call.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_vendor_external_io_detects_alias_imports() -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from urllib.request import urlopen as open_url
from requests import get as rget

def first():
    return open_url('https://vendor.test')

def second():
    return rget('https://vendor.test')
"""
    try:
        rel = _write_boundary_temp(rel_dir, "vendor_alias_io.py", body)
        findings = boundary_analyzer._vendor_external_io_functions((rel,))
        assert any(item.startswith(f"{rel}:first@") and item.endswith(":open_url") for item in findings)
        assert any(item.startswith(f"{rel}:second@") and item.endswith(":rget") for item in findings)
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_does_not_trust_unresolved_emit_fn(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
app = Flask(__name__)
def emit_fn(payload):
    return 'plain'
@app.route('/bad')
def bad():
    return emit_fn({'ok': False})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "fake_emit_fn.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_fails_closed_on_after_request_replacement(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.after_request
def replace(resp):
    return 'raw replacement'
@app.route('/good')
def good():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "raw_after_request.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_presenter_alias_is_scoped_to_binding(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
def setup_alias():
    render = emit_public
    return render({'ok': True})
@app.route('/raw-shadow')
def raw_shadow():
    def render(payload):
        return 'raw'
    return render({'ok': False})
@app.route('/good')
def good():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "scoped_alias_shadow.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_public_route_signatures_exclude_internal_ops_dev() -> None:
    signatures = boundary_analyzer._adapter_public_route_signatures(generator.ADAPTER_BOUNDARY_ADAPTER_LOCI)
    assert not any(':/internal/' in item or ':/ops/' in item or ':/dev/' in item for item in signatures)
    proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    assert checks["no_public_reader_change"] is True
    assert ':/internal/' not in proof
    assert ':/ops/' not in proof
    assert ':/dev/' not in proof


def test_epic034_adapter_boundary_fails_closed_on_conditional_presenter_assignment(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, Response
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.route('/conditional')
def conditional():
    if False:
        body = emit_public({'ok': True})
    return Response(body)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "conditional_presenter_assignment.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_rejects_conditional_presenter_alias(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.route('/conditional-alias')
def conditional_alias():
    if False:
        render = emit_public
    return render({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "conditional_presenter_alias.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_vendor_guard_distinguishes_duplicate_function_names(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from urllib.request import urlopen

class Guarded:
    def call_vendor(self):
        import os
        safe_mode = os.environ.get('SAFE_MODE')
        allow_network = os.environ.get('ALLOW_NETWORK')
        if safe_mode != '0' or allow_network != '1':
            raise RuntimeError('refused')
        return urlopen('https://vendor.test/guarded')

class Unguarded:
    def call_vendor(self):
        return urlopen('https://vendor.test/unguarded')
"""
    try:
        rel = _write_boundary_temp(rel_dir, "duplicate_vendor_names.py", body)
        findings = boundary_analyzer._vendor_external_io_functions((rel,))
        assert any(item.startswith(f"{rel}:Guarded.call_vendor@") for item in findings)
        assert any(item.startswith(f"{rel}:Unguarded.call_vendor@") for item in findings)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI", (rel,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_VENDOR_GUARD_UNEXPECTED:.*Unguarded.call_vendor"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_vendor_guard_rejects_nested_raise_before_io(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from urllib.request import urlopen

def nested_guard(debug=False):
    safe_mode = '1'
    allow_network = '0'
    if safe_mode != '0' or allow_network != '1':
        if debug:
            raise RuntimeError('refused only in debug')
    return urlopen('https://vendor.test')
"""
    try:
        rel = _write_boundary_temp(rel_dir, "nested_vendor_guard.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI", (rel,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_VENDOR_GUARD_UNEXPECTED:.*nested_guard"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_public_route_prefix_filter_keeps_developer_like_routes(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.route('/developer/status')
def developer_status():
    return 'raw developer status'
@app.route('/good')
def good():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "developer_status_route.py", body)
        signatures = boundary_analyzer._adapter_public_route_signatures((adapter,))
        assert any('path=/developer/status;' in item for item in signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(signatures))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_public_route_prefix_filter_uses_full_blueprint_path(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, Blueprint
from engine.presenter.emitter import emit_public
app = Flask(__name__)
bp = Blueprint('api', __name__, url_prefix='/api')
@bp.route('/internal/raw')
def raw_public_under_api():
    return 'raw public under api'
@app.route('/good')
def good():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "public_blueprint_internal_segment.py", body)
        signatures = boundary_analyzer._adapter_public_route_signatures((adapter,))
        assert any('path=/api/internal/raw;' in item for item in signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(signatures))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_vendor_guard_rejects_open_rails_raise_before_io(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from urllib.request import urlopen

def inverted_guard():
    safe_mode = '1'
    allow_network = '0'
    if safe_mode == '0' and allow_network == '1':
        raise RuntimeError('wrong branch')
    return urlopen('https://vendor.test')
"""
    try:
        rel = _write_boundary_temp(rel_dir, "inverted_vendor_guard.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI", (rel,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_VENDOR_GUARD_UNEXPECTED:.*inverted_guard@.*:urlopen"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_vendor_guard_requires_rails_env_derived_predicate(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from urllib.request import urlopen

def local_lookalike_guard():
    safe_mode = '1'
    allow_network = '0'
    if safe_mode != '0' or allow_network != '1':
        raise RuntimeError('refused')
    return urlopen('https://vendor.test')
"""
    try:
        rel = _write_boundary_temp(rel_dir, "local_lookalike_vendor_guard.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI", (rel,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_VENDOR_GUARD_UNEXPECTED:.*local_lookalike_guard@.*:urlopen"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_vendor_guard_must_dominate_external_io(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
import os
from urllib.request import urlopen

def late_guard():
    response = urlopen('https://vendor.test')
    if os.environ.get('SAFE_MODE') != '0' or os.environ.get('ALLOW_NETWORK') != '1':
        raise RuntimeError('refused')
    return response
"""
    try:
        rel = _write_boundary_temp(rel_dir, "late_vendor_guard.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI", (rel,))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_VENDOR_GUARD_UNEXPECTED:.*late_guard@.*:urlopen"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_includes_installed_logging_filter_hooks() -> None:
    proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    assert checks["actual_repo_loci_discovered_before_classification"] is True
    assert "adapter/logging_filter.py" in proof
    assert "locus=adapter/logging_filter.py;registration=decorator;decorator=app.before_request;path=;methods=;endpoint=_start_timer_and_cid" in proof
    assert "locus=adapter/logging_filter.py;registration=decorator;decorator=app.after_request;path=;methods=;endpoint=_keys_only_after" in proof


def test_epic034_adapter_boundary_rejects_abort_response_exit(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, abort, request
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.route('/maybe-abort')
def maybe_abort():
    if request.args.get('maintenance'):
        abort(503)
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "abort_route.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_rejects_raise_response_exit(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, request
from werkzeug.exceptions import ServiceUnavailable
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.route('/maybe-raise')
def maybe_raise():
    if request.args.get('maintenance'):
        raise ServiceUnavailable()
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "raise_route.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)

def test_epic034_adapter_boundary_rejects_mixed_get_head_empty_error_response(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, Response
app = Flask(__name__)
@app.route('/mixed', methods=['GET', 'HEAD'])
def mixed():
    return Response(b'', status=503)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "mixed_get_head_empty.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_rejects_presenter_object_metadata_response(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, Response
from engine.narratives import emit_public_aux
app = Flask(__name__)
@app.route('/metadata')
def metadata():
    emission = emit_public_aux(category='x', band='y', perspective='z')
    return Response(emission.key, status=200)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "presenter_metadata.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_rejects_helper_with_raw_parameter_branch(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
def choose(raw, rendered):
    if raw:
        return raw
    return rendered
@app.route('/choose')
def choose_route():
    return choose('raw', emit_public({'ok': True}))
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "helper_raw_branch.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_rejects_presenter_variable_reassigned_raw(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, Response
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.route('/reassigned')
def reassigned():
    body = emit_public({'ok': True})
    body = b'raw'
    return Response(body, status=200)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "reassigned_raw.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_allows_before_request_without_response(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, g
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.before_request
def prepare():
    g.ready = True
    return None
@app.route('/good')
def good():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "before_request_none.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
        assert checks["no_presenter_bypass"] is True
        assert "no_presenter_bypass_claim=PASS" in proof
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_rejects_route_none_branch(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, request
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.route('/maybe')
def maybe():
    if request.args.get('ok'):
        return emit_public({'ok': True})
    return None
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "route_none_branch.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)

def test_epic034_adapter_boundary_rejects_after_request_body_mutation(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.after_request
def mutate(resp):
    resp.set_data(b'raw replacement')
    return resp
@app.route('/good')
def good():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "mutating_after_request.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_rejects_fallthrough_passthrough_helper(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
def maybe_passthrough(resp):
    if False:
        return resp
@app.after_request
def hook(resp):
    return maybe_passthrough(resp)
@app.route('/good')
def good():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "fallthrough_passthrough.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_allows_passthrough_helper_with_common_final_return(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
def maybe_passthrough(resp):
    if False:
        return resp
    return resp
@app.after_request
def hook(resp):
    return maybe_passthrough(resp)
@app.route('/good')
def good():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "common_final_passthrough.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
        assert checks["no_presenter_bypass"] is True
        assert "[no_presenter_bypass] status=PASS" in proof
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_allows_indexed_tuple_emitter_body(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, Response
from engine.presenter.emitter import emit_public_with_envelope
app = Flask(__name__)
@app.route('/direct')
def direct():
    return Response(emit_public_with_envelope({'ok': True})[0], status=200)
@app.route('/assigned')
def assigned():
    emitted = emit_public_with_envelope({'ok': True})
    return Response(emitted[0], status=200)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "indexed_tuple_emitter.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
        assert checks["no_presenter_bypass"] is True
        assert "[no_presenter_bypass] status=PASS" in proof
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_distinguishes_duplicate_nested_handler_names(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, Blueprint
from engine.presenter.emitter import emit_public
app = Flask(__name__)
def first_bp():
    bp = Blueprint('first', __name__)
    @bp.route('/first')
    def index():
        return emit_public({'ok': True})
    return bp
def second_bp():
    bp = Blueprint('second', __name__)
    @bp.route('/second')
    def index():
        return 'raw duplicate handler'
    return bp
app.register_blueprint(first_bp())
app.register_blueprint(second_bp())
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "duplicate_nested_index.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_rejects_empty_get_response_without_transport_context(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask, Response
app = Flask(__name__)
@app.get('/empty')
def empty():
    return Response(b'', status=503)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "empty_get_response.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_rejects_unscoped_errorhandler_returning_err(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.errorhandler(404)
def missing(err):
    if False:
        return emit_public({'ok': False})
    return err
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "unscoped_errorhandler_err.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer._adapter_public_route_signatures((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)

def test_epic034_adapter_boundary_fails_closed_when_repointed_route_loci_drift(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/unexpected-public')
def unexpected_public():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "unexpected_public_route.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ("adapter/other.py:app.route:/expected:GET:expected",))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_public_reader_change"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_adapter_boundary_requires_low_level_vendor_io_guard() -> None:
    proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    assert checks["guard_provenance_per_relevant_path"] is True
    assert "guarded_by=engine/bodygraph/vendor_client.py:HdApiClient._default_request@" in proof

def test_epic034_adapter_boundary_reports_positive_contract_classifications() -> None:
    proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    assert checks["conservative_positive_boundary_contract_applied"] is True
    assert "work_item=W-004" in proof
    assert "analyzer_rendering_separation=" in proof
    assert "renderer_only_posture=" in proof
    assert "analyzer_owned_verdict_status=PASS" in proof
    assert "classification_categories_used=allowed,forbidden,unknown / fail-closed,out of scope" in proof
    assert "unknown_current_categories_fail_closed=true" in proof
    for category in [
        "public_routes",
        "response_producing_paths",
        "presenter_provenance",
        "serializer_paths",
        "external_io_paths",
        "pure_compute_external_io",
        "guard_provenance",
        "evidence_binding_posture",
    ]:
        assert f"boundary_finding category={category}" in proof
    assert "classification=allowed verdict=PASS" in proof
    assert "classification=out of scope verdict=PASS" in proof


def test_epic034_boundary_unknown_category_is_fail_closed() -> None:
    finding = boundary_analyzer.boundary_finding("synthetic_unknown", boundary_analyzer.BOUNDARY_UNKNOWN, "UNKNOWN", ["synthetic.py"], "unresolved current category")
    assert boundary_analyzer.finding_passes(finding) is False
    bad_finding = boundary_analyzer.boundary_finding("synthetic_unknown", boundary_analyzer.BOUNDARY_UNKNOWN, "PASS", ["synthetic.py"], "would be false pass")
    assert boundary_analyzer.finding_passes(bad_finding) is False



def _epic034_analyzer_result() -> dict[str, Any]:
    source_selection, request_shaping, response_mapping = _epic034_boundary_inputs()
    return boundary_analyzer.analyze_adapter_boundary(
        source_selection=source_selection,
        request_shaping=request_shaping,
        response_mapping=response_mapping,
        adapter_loci=generator.ADAPTER_BOUNDARY_ADAPTER_LOCI,
        canonical_adapter_loci=generator.ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI,
        presenter_loci=generator.ADAPTER_BOUNDARY_PRESENTER_LOCI,
        vendor_seam_loci=generator.ADAPTER_BOUNDARY_VENDOR_SEAM_LOCI,
        pure_compute_loci=generator.ADAPTER_BOUNDARY_PURE_COMPUTE_LOCI,
        public_route_baseline=generator.ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE,
        evidence_tool_loci=("tools/evidence/generate_hdapi_v2_contract_inventory.py", "tools/evidence/hdapi_v2_boundary_analyzer.py"),
    )


def test_epic034_w002_generator_consumes_analyzer_output_without_recomputing(monkeypatch: pytest.MonkeyPatch) -> None:
    result = _epic034_analyzer_result()
    result["findings"][0]["details"] = ["sentinel_analyzer_owned_detail"]
    result["discovered_public_route_signatures"] = ["sentinel_analyzer_owned_route"]

    def fake_analyze(**_kwargs: Any) -> dict[str, Any]:
        return result

    monkeypatch.setattr(boundary_analyzer, "analyze_adapter_boundary", fake_analyze)
    proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    assert checks["conservative_positive_boundary_contract_applied"] is True
    assert "sentinel_analyzer_owned_detail" in proof
    assert "sentinel_analyzer_owned_route" in proof
    assert "renderer_only_posture=evidence generator does not rediscover" in proof


def test_epic034_w002_renderer_refuses_non_pass_analyzer_verdict_even_when_checks_pass() -> None:
    result = _epic034_analyzer_result()
    assert all(result["checks"].values())
    result["verdict_status"] = "UNKNOWN"
    with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_ANALYZER_VERDICT_NON_PASS:UNKNOWN"):
        generator.render_adapter_boundary_proof("2026-06-18T00:00:00Z", result)

    result = _epic034_analyzer_result()
    assert all(result["checks"].values())
    result["verdict_status"] = "FAIL"
    with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_ANALYZER_VERDICT_NON_PASS:FAIL"):
        generator.render_adapter_boundary_proof("2026-06-18T00:00:00Z", result)


def test_epic034_w002_renderer_refuses_unknown_or_forbidden_pass() -> None:
    result = _epic034_analyzer_result()
    result["findings"][0]["classification"] = boundary_analyzer.BOUNDARY_UNKNOWN
    result["findings"][0]["verdict"] = "PASS"
    with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_RENDERER_REFUSED_UNKNOWN_PASS"):
        generator.render_adapter_boundary_proof("2026-06-18T00:00:00Z", result)

    result = _epic034_analyzer_result()
    result["findings"][0]["classification"] = boundary_analyzer.BOUNDARY_FORBIDDEN
    result["findings"][0]["verdict"] = "PASS"
    with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_RENDERER_REFUSED_FORBIDDEN_PASS"):
        generator.render_adapter_boundary_proof("2026-06-18T00:00:00Z", result)


def test_epic034_w002_analyzer_findings_survive_rendering_and_no_claims_remain() -> None:
    result = _epic034_analyzer_result()
    proof, checks = generator.render_adapter_boundary_proof("2026-06-18T00:00:00Z", result)
    check_log = generator.build_adapter_boundary_check_log("2026-06-18T00:00:00Z", proof, checks, mode="closed-rails-source-cache")
    for needle in [
        "public_route_findings_and_verdict=allowed:PASS",
        "presenter_provenance_findings_and_verdict=allowed:PASS",
        "serializer_findings_and_verdict=allowed:PASS",
        "external_io_findings_and_verdict=allowed:PASS",
        "guard_provenance_findings_and_verdict=allowed:PASS",
        "no_HDE-FERM007.5_claim=NONE",
        "no_HDE-FERM008_claim=NONE",
        "no_runtime_v2_conformance_claim=NONE",
        "no_live_vendor_conformance_claim=NONE",
        "no_open_rails_smoke_claim=NONE",
        "no_public_reader_change_claim=NONE",
        "no_new_HTTP_home_claim=NONE",
        "no_AI_scope_claim=NONE",
    ]:
        assert needle in proof
    for needle in [
        "analyzer_rendering_separation_was_applied=true",
        "evidence_generator_rendered_analyzer_output_only=true",
        "renderer_did_not_recompute_boundary_truth=true",
        "public_route_findings_were_carried_from_analyzer_to_renderer=true",
        "presenter_provenance_findings_were_carried_from_analyzer_to_renderer=true",
        "external_io_findings_were_carried_from_analyzer_to_renderer=true",
        "guard_provenance_findings_were_carried_from_analyzer_to_renderer=true",
        "no_unsupported_scope_claim_was_emitted=true",
    ]:
        assert needle in check_log


def test_epic034_w004_route_drift_does_not_disable_when_adapter_loci_change(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
SAFE_MODE='1'
@app.route('/w004-new-public', methods=['GET'])
def w004_new_public():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_new_public.py", body)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ())
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_baseline_present.*no_public_reader_change"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


@pytest.mark.parametrize(
    ("filename", "body", "mutate"),
    [
        (
            "w004_blueprint_prefix.py",
            """
from flask import Blueprint
from engine.presenter.emitter import emit_public
bp = Blueprint('reader', __name__, url_prefix='/old')
@bp.get('/reader')
def reader():
    return emit_public({'ok': True})
""",
            lambda sig: sig.replace("blueprint_constructor_prefix=/old", "blueprint_constructor_prefix=/new"),
        ),
        (
            "w004_register_prefix.py",
            """
from flask import Flask, Blueprint
from engine.presenter.emitter import emit_public
app = Flask(__name__)
bp = Blueprint('reader', __name__)
@bp.get('/reader')
def reader():
    return emit_public({'ok': True})
app.register_blueprint(bp, url_prefix='/old')
""",
            lambda sig: sig.replace("register_blueprint_prefix=/old", "register_blueprint_prefix=/new"),
        ),
        (
            "w004_errorhandler.py",
            """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.errorhandler(404)
def missing(err):
    return emit_public({'ok': False})
""",
            lambda sig: sig.replace("errorhandler_key=404", "errorhandler_key=500"),
        ),
        (
            "w004_routing_keyword.py",
            """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.route('/kw', methods=['POST'], provide_automatic_options=False)
def kw():
    return emit_public({'ok': True})
""",
            lambda sig: sig.replace("routing_keywords=provide_automatic_options\\=False", "routing_keywords=provide_automatic_options\\=True"),
        ),
    ],
)
def test_epic034_w004_signature_field_drift_fails_closed(monkeypatch: pytest.MonkeyPatch, filename: str, body: str, mutate: Any) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    try:
        adapter = _write_boundary_temp(rel_dir, filename, body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        assert signatures
        stale_baseline = tuple(mutate(item) for item in signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", stale_baseline)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_baseline_reconciled.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_add_url_rule_imported_view_target_and_endpoint_are_signed() -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public as imported_emit
app = Flask(__name__)
def local_view():
    return imported_emit({'ok': True})
app.add_url_rule('/added', 'added_endpoint', view_func=local_view, methods=['POST'], provide_automatic_options=False)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_add_url_rule.py", body)
        signatures = boundary_analyzer._adapter_public_route_signatures((adapter,))
        joined = "\n".join(signatures)
        assert "registration=add_url_rule" in joined
        assert "path=/added" in joined
        assert "methods=POST" in joined
        assert "endpoint=added_endpoint" in joined
        assert "view=local_view" in joined
        assert "routing_keywords=provide_automatic_options\\=False" in joined
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_dynamic_route_classification_ambiguity_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
ROUTE = '/dynamic-public'
@app.route(ROUTE)
def dynamic_public():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_dynamic_route.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        assert any("public_internal_classification=unknown / fail-closed" in item for item in signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_route_findings_survive_renderer_output() -> None:
    result = _epic034_analyzer_result()
    proof, checks = generator.render_adapter_boundary_proof("2026-06-18T00:00:00Z", result)
    check_log = generator.build_adapter_boundary_check_log("2026-06-18T00:00:00Z", proof, checks, mode="closed-rails-source-cache")
    for needle in [
        "work_item=W-004",
        "route_comparison_cannot_disable_itself=true",
        "route_baseline_reconciliation_posture=reconciled",
        "current_public_route_signatures_inspected=",
        "route_baseline_signatures_inspected=",
        "blueprint_constructor_prefix_posture=encoded",
        "register_blueprint_url_prefix_posture=encoded",
        "add_url_rule_posture=encoded",
        "errorhandler_key_posture=encoded",
        "routing_keyword_posture=encoded",
        "endpoint_view_identity_posture=encoded",
        "imported_view_target_posture=encoded",
        "public_internal_classification_posture=encoded",
    ]:
        assert needle in proof
    for needle in [
        "w004_route_drift_repair_applied=true",
        "route_comparison_cannot_disable_itself=true",
        "changed_adapter_loci_cannot_bypass_route_drift_comparison=true",
        "route_baseline_mismatch_or_missing_baseline_fails_closed=true",
        "newly_discovered_public_routes_cannot_collapse_to_empty_comparison=true",
    ]:
        assert needle in check_log


def test_epic034_w004_dynamic_blueprint_and_register_prefixes_fail_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    cases = {
        "dynamic_blueprint_prefix.py": """
from flask import Blueprint
from engine.presenter.emitter import emit_public
PREFIX = '/dynamic'
bp = Blueprint('reader', __name__, url_prefix=PREFIX)
@bp.get('/reader')
def reader():
    return emit_public({'ok': True})
""",
        "dynamic_register_prefix.py": """
from flask import Flask, Blueprint
from engine.presenter.emitter import emit_public
PREFIX = '/dynamic'
app = Flask(__name__)
bp = Blueprint('reader', __name__)
@bp.get('/reader')
def reader():
    return emit_public({'ok': True})
app.register_blueprint(bp, url_prefix=PREFIX)
""",
    }
    rel_dir = "tmp_boundary_test"
    try:
        for filename, body in cases.items():
            adapter = _write_boundary_temp(rel_dir, filename, body)
            signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
            assert any("public_internal_classification=unknown / fail-closed" in item for item in signatures)
            monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
            monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
            with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
                generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_add_url_rule_without_literal_path_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
ROUTE = '/added-dynamic'
app = Flask(__name__)
def added():
    return emit_public({'ok': True})
app.add_url_rule(ROUTE, 'added', view_func=added, methods=['GET'])
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_dynamic_add_url.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        assert any("registration=add_url_rule" in item for item in signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_add_url_rule_imported_view_from_inspected_adapter_locus_is_signed() -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    view_body = """
from engine.presenter.emitter import emit_public
def imported_view():
    return emit_public({'ok': True})
"""
    route_body = """
from flask import Flask
from tmp_boundary_test.w004_view_targets import imported_view
app = Flask(__name__)
app.add_url_rule('/imported-added', 'imported_endpoint', view_func=imported_view, methods=['POST'])
"""
    try:
        view_rel = _write_boundary_temp(rel_dir, "w004_view_targets.py", view_body)
        route_rel = _write_boundary_temp(rel_dir, "w004_imported_add_url.py", route_body)
        signatures = boundary_analyzer._adapter_public_route_signatures((route_rel, view_rel))
        joined = "\n".join(signatures)
        assert "registration=add_url_rule" in joined
        assert "path=/imported-added" in joined
        assert "endpoint=imported_endpoint" in joined
        assert "view=imported_view" in joined
        assert "imported_view_target=tmp_boundary_test.w004_view_targets.imported_view" in joined
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_uninspected_imported_add_url_view_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from external_adapter.views import imported_view
app = Flask(__name__)
app.add_url_rule('/uninspected-import', 'uninspected', view_func=imported_view, methods=['GET'])
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_uninspected_import.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        assert any("imported_view_target=external_adapter.views.imported_view" in item for item in signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_import_module_alias_from_inspected_locus_is_not_unclassified() -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    view_body = """
from engine.presenter.emitter import emit_public
def imported_view():
    return emit_public({'ok': True})
"""
    route_body = """
from flask import Flask
import tmp_boundary_test.w004_module_alias_targets as target_views
app = Flask(__name__)
app.add_url_rule('/module-alias-added', 'module_alias_endpoint', view_func=target_views.imported_view, methods=['GET'])
"""
    try:
        view_rel = _write_boundary_temp(rel_dir, "w004_module_alias_targets.py", view_body)
        route_rel = _write_boundary_temp(rel_dir, "w004_module_alias_add_url.py", route_body)
        signatures = boundary_analyzer._adapter_public_route_signatures((route_rel, view_rel))
        joined = "\n".join(signatures)
        assert "view=target_views.imported_view" in joined
        assert "imported_view_target=tmp_boundary_test.w004_module_alias_targets.imported_view" in joined
        assert "public_internal_classification=public" in joined
        assert "public_internal_classification=unknown / fail-closed" not in joined
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_unsupported_getattr_route_decorator_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@getattr(app, 'route')('/getattr-added')
def added():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_getattr_route.py", body)
        parsed_signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        unsupported_signatures = tuple(boundary_analyzer._unsupported_route_registration_signatures((adapter,)))
        assert parsed_signatures == ()
        assert any("registration=unsupported_route_registration" in item for item in unsupported_signatures)
        assert any("path=/getattr-added" in item for item in unsupported_signatures)
        assert any("endpoint=added" in item for item in unsupported_signatures)
        assert any("view=added" in item for item in unsupported_signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in unsupported_signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ())
        expected_failure = (
            "ADAPTER_BOUNDARY_CHECK_FAILED:.*route_baseline_present.*"
            "route_signature_classification_unambiguous.*no_public_reader_change"
        )
        with pytest.raises(ValueError, match=expected_failure):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_function_style_route_registration_cannot_collapse_to_empty_comparison(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
def added():
    return emit_public({'ok': True})
app.route('/function-style-added', methods=['POST'])(added)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_function_style_route.py", body)
        parsed_signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        unsupported_signatures = tuple(boundary_analyzer._unsupported_route_registration_signatures((adapter,)))
        assert parsed_signatures == ()
        assert any("registration=unsupported_route_registration" in item for item in unsupported_signatures)
        assert any("path=/function-style-added" in item for item in unsupported_signatures)
        assert any("methods=POST" in item for item in unsupported_signatures)
        assert any("endpoint=added" in item for item in unsupported_signatures)
        assert any("view=added" in item for item in unsupported_signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in unsupported_signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ())
        expected_failure = (
            "ADAPTER_BOUNDARY_CHECK_FAILED:.*"
            "new_public_routes_cannot_collapse_to_empty_comparison.*no_public_reader_change"
        )
        with pytest.raises(ValueError, match=expected_failure):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_aliased_route_decorator_fails_closed_with_signed_fields(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
public_route = app.route
@public_route('/aliased-added', methods=['PUT'])
def added():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_aliased_route.py", body)
        parsed_signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        unsupported_signatures = tuple(boundary_analyzer._unsupported_route_registration_signatures((adapter,)))
        assert parsed_signatures == ()
        assert any("registration=unsupported_route_registration" in item for item in unsupported_signatures)
        assert any("path=/aliased-added" in item for item in unsupported_signatures)
        assert any("methods=PUT" in item for item in unsupported_signatures)
        assert any("endpoint=added" in item for item in unsupported_signatures)
        assert any("view=added" in item for item in unsupported_signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in unsupported_signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ())
        expected_failure = (
            "ADAPTER_BOUNDARY_CHECK_FAILED:.*route_baseline_present.*"
            "route_signature_classification_unambiguous.*no_public_reader_change"
        )
        with pytest.raises(ValueError, match=expected_failure):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_aliased_function_style_route_cannot_collapse_to_empty_comparison(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
public_post = app.post
def added():
    return emit_public({'ok': True})
public_post('/aliased-function-style')(added)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_aliased_function_style_route.py", body)
        parsed_signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        unsupported_signatures = tuple(boundary_analyzer._unsupported_route_registration_signatures((adapter,)))
        assert parsed_signatures == ()
        assert any("registration=unsupported_route_registration" in item for item in unsupported_signatures)
        assert any("path=/aliased-function-style" in item for item in unsupported_signatures)
        assert any("methods=POST" in item for item in unsupported_signatures)
        assert any("endpoint=added" in item for item in unsupported_signatures)
        assert any("view=added" in item for item in unsupported_signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in unsupported_signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ())
        expected_failure = (
            "ADAPTER_BOUNDARY_CHECK_FAILED:.*"
            "new_public_routes_cannot_collapse_to_empty_comparison.*no_public_reader_change"
        )
        with pytest.raises(ValueError, match=expected_failure):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_aliased_add_url_rule_direct_call_fails_closed_with_signed_fields(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
add_rule = app.add_url_rule
def added():
    return emit_public({'ok': True})
add_rule('/aliased-rule', 'aliased_endpoint', view_func=added, methods=['PATCH'])
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_aliased_add_url_rule.py", body)
        parsed_signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        unsupported_signatures = tuple(boundary_analyzer._unsupported_route_registration_signatures((adapter,)))
        assert parsed_signatures == ()
        assert any("registration=unsupported_route_registration" in item for item in unsupported_signatures)
        assert any("decorator=add_rule" in item for item in unsupported_signatures)
        assert any("path=/aliased-rule" in item for item in unsupported_signatures)
        assert any("methods=PATCH" in item for item in unsupported_signatures)
        assert any("endpoint=aliased_endpoint" in item for item in unsupported_signatures)
        assert any("view=added" in item for item in unsupported_signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in unsupported_signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ())
        expected_failure = (
            "ADAPTER_BOUNDARY_CHECK_FAILED:.*"
            "new_public_routes_cannot_collapse_to_empty_comparison.*no_public_reader_change"
        )
        with pytest.raises(ValueError, match=expected_failure):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_aliased_register_blueprint_direct_call_fails_closed_with_signed_fields(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Blueprint, Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
bp = Blueprint('bp', __name__)
register = app.register_blueprint
@bp.route('/aliased-blueprint-child')
def added():
    return emit_public({'ok': True})
register(bp, url_prefix='/aliased-prefix')
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_aliased_register_blueprint.py", body)
        unsupported_signatures = tuple(boundary_analyzer._unsupported_route_registration_signatures((adapter,)))
        joined = "\n".join(unsupported_signatures)
        assert "registration=unsupported_route_registration" in joined
        assert "decorator=register" in joined
        assert "blueprint=bp" in joined
        assert "register_blueprint_prefix=/aliased-prefix" in joined
        assert "public_internal_classification=unknown / fail-closed" in joined
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ())
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_public_reader_change"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_route_alias_detection_does_not_treat_non_flask_get_alias_as_route() -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
class Session:
    def get(self, path):
        return {'path': path}
session = Session()
client_get = session.get
client_get('/not-a-flask-route')
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_non_flask_get_alias.py", body)
        assert boundary_analyzer._unsupported_route_registration_signatures((adapter,)) == []
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_getattr_route_alias_from_flask_owner_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
public_route = getattr(app, 'route')
@public_route('/getattr-aliased-route')
def added():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_getattr_route_alias.py", body)
        parsed_signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        unsupported_signatures = tuple(boundary_analyzer._unsupported_route_registration_signatures((adapter,)))
        assert parsed_signatures == ()
        assert any("path=/getattr-aliased-route" in item for item in unsupported_signatures)
        assert any("endpoint=added" in item for item in unsupported_signatures)
        assert any("view=added" in item for item in unsupported_signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in unsupported_signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ())
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_public_reader_change"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_aliased_flask_constructor_route_alias_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask as FlaskCtor
from engine.presenter.emitter import emit_public
app = FlaskCtor(__name__)
public_route = app.route
@public_route('/constructor-alias-route', methods=['DELETE'])
def added():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_constructor_alias_route.py", body)
        parsed_signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        unsupported_signatures = tuple(boundary_analyzer._unsupported_route_registration_signatures((adapter,)))
        assert parsed_signatures == ()
        assert any("path=/constructor-alias-route" in item for item in unsupported_signatures)
        assert any("methods=DELETE" in item for item in unsupported_signatures)
        assert any("endpoint=added" in item for item in unsupported_signatures)
        assert any("view=added" in item for item in unsupported_signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in unsupported_signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ())
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_public_reader_change"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_aliased_blueprint_constructor_route_alias_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Blueprint as BlueprintCtor, Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
bp = BlueprintCtor('bp', __name__)
public_get = bp.get
@public_get('/blueprint-constructor-alias')
def added():
    return emit_public({'ok': True})
app.register_blueprint(bp)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_blueprint_constructor_alias_route.py", body)
        unsupported_signatures = tuple(boundary_analyzer._unsupported_route_registration_signatures((adapter,)))
        joined = "\n".join(unsupported_signatures)
        assert "path=/blueprint-constructor-alias" in joined
        assert "methods=GET" in joined
        assert "endpoint=added" in joined
        assert "view=added" in joined
        assert "public_internal_classification=unknown / fail-closed" in joined
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ())
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_public_reader_change"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_imported_inspected_blueprint_route_alias_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    owner_body = """
from flask import Blueprint
shared_bp = Blueprint('shared', __name__)
"""
    route_body = """
from flask import Flask
from engine.presenter.emitter import emit_public
from tmp_boundary_test.w004_imported_bp_owner import shared_bp
app = Flask(__name__)
public_route = shared_bp.route
@public_route('/imported-blueprint-alias', methods=['PUT'])
def added():
    return emit_public({'ok': True})
app.register_blueprint(shared_bp)
"""
    try:
        owner = _write_boundary_temp(rel_dir, "w004_imported_bp_owner.py", owner_body)
        adapter = _write_boundary_temp(rel_dir, "w004_imported_bp_route_alias.py", route_body)
        parsed_signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter, owner)))
        unsupported_signatures = tuple(boundary_analyzer._unsupported_route_registration_signatures((adapter, owner)))
        assert all("/imported-blueprint-alias" not in item for item in parsed_signatures)
        assert any("path=/imported-blueprint-alias" in item for item in unsupported_signatures)
        assert any("methods=PUT" in item for item in unsupported_signatures)
        assert any("endpoint=added" in item for item in unsupported_signatures)
        assert any("view=added" in item for item in unsupported_signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in unsupported_signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter, owner))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", ())
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_public_reader_change"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_imported_inspected_non_route_get_alias_is_not_route() -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    owner_body = """
class Session:
    def get(self, path):
        return {'path': path}
session = Session()
"""
    route_body = """
from tmp_boundary_test.w004_imported_non_route_owner import session
client_get = session.get
client_get('/still-not-a-flask-route')
"""
    try:
        owner = _write_boundary_temp(rel_dir, "w004_imported_non_route_owner.py", owner_body)
        adapter = _write_boundary_temp(rel_dir, "w004_imported_non_route_alias.py", route_body)
        assert boundary_analyzer._unsupported_route_registration_signatures((adapter, owner)) == []
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_route_decorator_endpoint_keyword_is_signed_and_drifts(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.route('/endpoint-keyword', endpoint='explicit_endpoint')
def added():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_endpoint_keyword.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        assert any("endpoint=explicit_endpoint" in item for item in signatures)
        assert any("view=added" in item for item in signatures)
        drifted_baseline = tuple(
            item.replace("endpoint=explicit_endpoint", "endpoint=added")
            for item in signatures
        )
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", drifted_baseline)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_baseline_reconciled.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_dynamic_route_decorator_endpoint_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
ENDPOINT = 'dynamic_endpoint'
@app.route('/dynamic-endpoint', endpoint=ENDPOINT)
def added():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_dynamic_endpoint.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        assert any("public_internal_classification=unknown / fail-closed" in item for item in signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_add_url_rule_endpoint_keyword_is_signed() -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
def added():
    return emit_public({'ok': True})
app.add_url_rule(
    '/add-url-endpoint-keyword',
    endpoint='explicit_add_endpoint',
    view_func=added,
    methods=['GET'],
)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_add_url_endpoint_keyword.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        assert any("registration=add_url_rule" in item for item in signatures)
        assert any("endpoint=explicit_add_endpoint" in item for item in signatures)
        assert any("view=added" in item for item in signatures)
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_dynamic_route_decorator_methods_fail_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
METHODS = ['GET', 'POST']
@app.route('/dynamic-methods', methods=METHODS)
def added():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_dynamic_methods.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        assert any("path=/dynamic-methods" in item for item in signatures)
        assert any("methods=" in item for item in signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_dynamic_add_url_rule_methods_fail_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
METHODS = ['PATCH']
def added():
    return emit_public({'ok': True})
app.add_url_rule(
    '/dynamic-add-url-methods',
    'added',
    view_func=added,
    methods=METHODS,
)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_dynamic_add_url_methods.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        assert any("registration=add_url_rule" in item for item in signatures)
        assert any("path=/dynamic-add-url-methods" in item for item in signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_dynamic_routing_keyword_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
AUTO_OPTIONS = False
@app.route('/dynamic-routing-keyword', provide_automatic_options=AUTO_OPTIONS)
def added():
    return emit_public({'ok': True})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_dynamic_routing_keyword.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        joined = "\n".join(signatures)
        assert "path=/dynamic-routing-keyword" in joined
        assert "routing_keywords=provide_automatic_options\\=" in joined
        assert "public_internal_classification=unknown / fail-closed" in joined
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_dynamic_register_blueprint_routing_keyword_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Blueprint, Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
bp = Blueprint('bp', __name__)
SUBDOMAIN = 'api'
@bp.route('/child')
def added():
    return emit_public({'ok': True})
app.register_blueprint(bp, subdomain=SUBDOMAIN)
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_dynamic_register_blueprint_keyword.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        assert any("registration=register_blueprint" in item for item in signatures)
        assert any("routing_keywords=subdomain\\=" in item for item in signatures)
        assert any("public_internal_classification=unknown / fail-closed" in item for item in signatures)
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_errorhandler_integer_key_is_signed() -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
@app.errorhandler(404)
def not_found(error):
    return emit_public({'ok': False})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_errorhandler_integer.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        assert any("decorator=app.errorhandler" in item for item in signatures)
        assert any("errorhandler_key=404" in item for item in signatures)
        assert all(
            "public_internal_classification=unknown / fail-closed" not in item
            for item in signatures
        )
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_dynamic_errorhandler_key_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
NOT_FOUND = 404
@app.errorhandler(NOT_FOUND)
def not_found(error):
    return emit_public({'ok': False})
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_dynamic_errorhandler.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        joined = "\n".join(signatures)
        assert "errorhandler_key=NOT_FOUND" in joined
        assert "public_internal_classification=unknown / fail-closed" in joined
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_dynamic_add_url_rule_view_factory_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
def make_view():
    def generated():
        return emit_public({'ok': True})
    return generated
app.add_url_rule('/factory-view', 'factory_view', view_func=make_view(), methods=['GET'])
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_dynamic_add_url_rule_view.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        joined = "\n".join(signatures)
        assert "registration=add_url_rule" in joined
        assert "view=make_view" in joined
        assert "public_internal_classification=unknown / fail-closed" in joined
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)


def test_epic034_w004_register_blueprint_factory_call_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    import shutil

    rel_dir = "tmp_boundary_test"
    body = """
from flask import Blueprint, Flask
from engine.presenter.emitter import emit_public
app = Flask(__name__)
def make_bp():
    bp = Blueprint('bp', __name__)
    @bp.get('/factory-bp')
    def factory_bp():
        return emit_public({'ok': True})
    return bp
app.register_blueprint(make_bp())
"""
    try:
        adapter = _write_boundary_temp(rel_dir, "w004_dynamic_register_blueprint_target.py", body)
        signatures = tuple(boundary_analyzer._adapter_public_route_signatures((adapter,)))
        joined = "\n".join(signatures)
        assert "registration=register_blueprint" in joined
        assert "blueprint=make_bp" in joined
        assert "public_internal_classification=unknown / fail-closed" in joined
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", signatures)
        with pytest.raises(
            ValueError,
            match="ADAPTER_BOUNDARY_CHECK_FAILED:.*route_signature_classification_unambiguous.*no_public_reader_change",
        ):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
    finally:
        shutil.rmtree(ROOT / rel_dir, ignore_errors=True)
