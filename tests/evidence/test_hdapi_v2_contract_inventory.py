from __future__ import annotations

import csv
import json
from pathlib import Path

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


def test_hdapi_v2_inventory_records_required_source_fields_and_ai_boundary() -> None:
    inventory = _assert_canonical_json(VENDOR_DIR / "source_inventory.json")
    assert "documentation-discovery-only" in inventory["ai_boundary"]
    for key in ["llms_txt", "llms_full_txt", "v2_routes_yaml", "v1_routes_yaml", "suspect_openapi_json"]:
        source = inventory["sources"][key]
        for field in ["source_url", "final_url", "content_type", "fetch_status", "sha256", "discovered_from", "last_seen_utc", "source_classification"]:
            assert source[field] != "", (key, field)
    assert inventory["sources"]["llms_txt"]["source_classification"] == "documentation-discovery-only"
    assert inventory["sources"]["llms_full_txt"]["source_classification"] == "documentation-discovery-only"


def test_hdapi_v2_validation_quarantines_suspect_openapi() -> None:
    log = (VENDOR_DIR / "openapi_validation.log").read_text(encoding="utf-8")
    assert "[v2-routes.yaml] status=VALIDATED" in log
    assert "[v1-routes.yaml] status=VALIDATED" in log
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
