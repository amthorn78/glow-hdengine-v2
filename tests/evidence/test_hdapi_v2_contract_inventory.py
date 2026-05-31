from __future__ import annotations

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
    VENDOR_DIR / "source_cache" / "v2-routes.yaml",
    VENDOR_DIR / "source_cache" / "v1-routes.yaml",
    VENDOR_DIR / "source_cache" / "api-reference.openapi.json",
    VENDOR_DIR / "source_cache" / "llms-full.endpoint-tiers.txt",
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


def test_hdapi_v2_validation_quarantines_suspect_openapi() -> None:
    log = (VENDOR_DIR / "openapi_validation.log").read_text(encoding="utf-8")
    assert "source_mode=closed-rails-source-cache" in log
    assert "Ruby Psych YAML parser" in log
    assert "[v2-routes.yaml] status=VALIDATED" in log
    assert "[v2-routes.yaml] openapi_3_parse=PASS" in log
    assert "[v1-routes.yaml] status=VALIDATED" in log
    assert "[route-spec-gate] status=PASS" in log
    assert "[api-reference/openapi.json] status=QUARANTINED" in log
    anomalies = (VENDOR_DIR / "known_anomalies.md").read_text(encoding="utf-8")
    assert "Decision: QUARANTINED." in anomalies
    assert "OpenAPI Plant Store" in anomalies
    assert "repository path `api-reference/openapi.json` is absent" in anomalies


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
