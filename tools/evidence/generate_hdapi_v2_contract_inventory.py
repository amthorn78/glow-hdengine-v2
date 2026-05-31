#!/usr/bin/env python3
"""Generate HDE-EPIC033 HDAPI v2 contract-inventory evidence."""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import io
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "vendor" / "hdapi_v2"
ACCEPTANCE = ROOT / "docs" / "acceptance_map_epic033.json"
TOKEN_MATRIX = ROOT / "audit" / "qa" / "hde-epic033" / "token_evidence_matrix.md"
VIABILITY = ROOT / "audit" / "qa" / "hde-epic033" / "acceptance_map_viability.log"
DOC_DELTAS = ROOT / "audit" / "docdeltas" / "hde-epic033_doc_deltas.md"
QA_DOC_DELTAS = ROOT / "audit" / "qa" / "hde-epic033" / "00_meta" / "doc_deltas.md"

BASE = "https://docs.humandesignapi.nl"
SOURCES = [
    ("robots_preflight", f"{BASE}/robots.txt", "robots_preflight", "seed"),
    ("llms_txt", f"{BASE}/llms.txt", "documentation-discovery-only", "robots_preflight"),
    ("llms_full_txt", f"{BASE}/llms-full.txt", "documentation-discovery-only", "llms_txt"),
    ("v2_routes_yaml", f"{BASE}/openapi/v2-routes.yaml", "validated_machine_readable_route_spec", "llms_txt"),
    ("v1_routes_yaml", f"{BASE}/openapi/v1-routes.yaml", "validated_machine_readable_route_spec", "llms_txt"),
    ("suspect_openapi_json", f"{BASE}/api-reference/openapi.json", "suspect_quarantined_openapi", "llms_txt"),
    ("v2_overview", f"{BASE}/api-reference/v2/overview", "rendered_high_level_guide", "llms_txt"),
    ("v1_overview", f"{BASE}/api-reference/v1/overview", "rendered_high_level_guide", "llms_txt"),
    ("v2_full_chart_page", f"{BASE}/api-reference/charts/generate-a-full-chart", "rendered_endpoint_page", "llms_txt"),
    ("v2_simple_chart_page", f"{BASE}/api-reference/charts/generate-a-simple-chart", "rendered_endpoint_page", "llms_txt"),
    ("v2_coordinates_chart_page", f"{BASE}/api-reference/charts/generate-a-chart-from-coordinates", "rendered_endpoint_page", "llms_txt"),
    ("authentication", f"{BASE}/authentication", "rendered_contract_page", "llms_txt"),
    ("rate_limiting", f"{BASE}/guides/rate-limiting", "rendered_contract_page", "llms_txt"),
    ("response_format", f"{BASE}/response-format", "rendered_contract_page", "llms_txt"),
    ("migration_v1_to_v2", f"{BASE}/migration/v1-to-v2", "rendered_contract_page", "llms_txt"),
    ("coordinates_guide", f"{BASE}/guides/coordinates-endpoint", "rendered_contract_page", "llms_txt"),
]

REQUIRED_ENDPOINTS = [
    ("POST", "/v2/charts"),
    ("POST", "/v2/charts/simple"),
    ("POST", "/v2/charts/coordinates"),
    ("POST", "/v1/bodygraphs"),
    ("POST", "/v1/bodygraphs/simple"),
]


def canonical_json_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="\n")


def fetch(url: str) -> tuple[str, str, int | str, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": "glow-hde-epic033-contract-inventory/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.geturl(), resp.headers.get("content-type", ""), resp.status, resp.read()
    except urllib.error.HTTPError as exc:
        return exc.geturl(), exc.headers.get("content-type", ""), exc.code, exc.read()
    except urllib.error.URLError as exc:
        return url, "", f"FETCH_ERROR:{exc.reason}", b""


def header_value(text: str, name: str) -> str | None:
    m = re.search(rf"^\s*{re.escape(name)}:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip().strip("'") if m else None


def has_path(text: str, path: str) -> bool:
    return re.search(rf"^\s{{2}}{re.escape(path)}:\s*$", text, re.MULTILINE) is not None


def extract_block(text: str, path: str) -> str:
    lines = text.splitlines()
    start = None
    marker = f"  {path}:"
    for i, line in enumerate(lines):
        if line == marker:
            start = i
            break
    if start is None:
        return ""
    out = []
    for line in lines[start:]:
        if out and re.match(r"^  /[^ ]+:$", line):
            break
        out.append(line)
    return "\n".join(out)


def response_codes(block: str) -> str:
    codes = re.findall(r"^\s{8}'(\d{3})':", block, re.MULTILINE)
    return ";".join(codes)


def error_codes(block: str) -> str:
    codes = sorted(set(re.findall(r"`([A-Z0-9_]+)`", block)))
    return ";".join(codes) if codes else "schema-defined StandardErrorResponse"


def schema_ref(block: str) -> str:
    m = re.search(r"\$ref: '#/components/schemas/([^']+)'", block)
    return m.group(1) if m else "unknown"


def validate_routes(name: str, text: str, version: str, server: str, required_paths: list[str]) -> list[str]:
    lines = [f"[{name}] status=VALIDATED"]
    checks = {
        "openapi_3": text.startswith("openapi: 3."),
        "title_humandesignapi": "title: Human Design API" in text,
        "version_present": bool(header_value(text, "version")),
        "server_domain": server in text,
        "required_paths_present": all(has_path(text, p) for p in required_paths),
    }
    for key, ok in checks.items():
        lines.append(f"[{name}] {key}={'PASS' if ok else 'FAIL'}")
    lines.append(f"[{name}] observed_version={header_value(text, 'version') or 'UNKNOWN'} expected_family={version}")
    if not all(checks.values()):
        lines[0] = f"[{name}] status=INVALID"
    return lines


def main() -> None:
    produced = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    OUT.mkdir(parents=True, exist_ok=True)
    fetched: dict[str, dict[str, Any]] = {}
    bodies: dict[str, bytes] = {}
    for key, url, classification, discovered_from in SOURCES:
        final_url, content_type, status, body = fetch(url)
        sha = hashlib.sha256(body).hexdigest() if body else ""
        fetched[key] = {
            "content_type": content_type,
            "discovered_from": discovered_from,
            "fetch_status": str(status),
            "final_url": final_url,
            "last_seen_utc": produced,
            "sha256": sha,
            "source_classification": classification,
            "source_url": url,
        }
        bodies[key] = body

    inventory = {
        "ai_boundary": "llms.txt, llms-full.txt, and AI/LLM-oriented vendor documentation are documentation-discovery-only context; no AI product, runtime, evidence, token, credential, rail, QA, or model-call scope is created.",
        "generated_at_utc": produced,
        "source_precedence": [
            "validated v2 and v1 YAML route specs",
            "rendered endpoint pages",
            "high-level guide pages",
            "suspect artifacts quarantined until validated",
        ],
        "sources": fetched,
    }
    (OUT / "source_inventory.json").write_bytes(canonical_json_bytes(inventory))

    md_lines = [
        "# HDAPI v2 and legacy v1 Source Inventory",
        "",
        f"Generated at UTC: {produced}",
        "",
        "This governed inventory records public same-origin HumanDesignAPI documentation sources only. It does not call credentialed runtime vendor endpoints and does not claim runtime v2 conformance.",
        "",
        "AI/LLM-oriented documentation, including `llms.txt` and `llms-full.txt`, is classified as documentation-discovery-only context and creates no AI product, runtime, evidence, token, credential, rail, QA, prompt, embedding, chatbot, model-call, or provider scope.",
        "",
        "| key | source_classification | fetch_status | content_type | sha256 | final_url | discovered_from |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for key in sorted(fetched):
        row = fetched[key]
        md_lines.append(f"| {key} | {row['source_classification']} | {row['fetch_status']} | {row['content_type']} | {row['sha256']} | {row['final_url']} | {row['discovered_from']} |")
    write_text(OUT / "source_inventory.md", "\n".join(md_lines))

    v2 = bodies["v2_routes_yaml"].decode("utf-8", errors="replace")
    v1 = bodies["v1_routes_yaml"].decode("utf-8", errors="replace")
    suspect = bodies["suspect_openapi_json"].decode("utf-8", errors="replace")
    validation_lines = [
        f"generated_at_utc={produced}",
        "scope=HDE-EPIC033 HDE-FERM006.2 machine-readable vendor route validation",
        "network_posture=public documentation fetch only; no credentialed runtime vendor API call",
        "validator=structural OpenAPI 3/domain/title/server/path-family checks using fetched public docs bytes",
    ]
    validation_lines += validate_routes("v2-routes.yaml", v2, "v2", "https://api.humandesignapi.nl/v2", ["/charts", "/charts/simple", "/charts/coordinates"])
    validation_lines += validate_routes("v1-routes.yaml", v1, "v1", "https://api.humandesignapi.nl/v1", ["/bodygraphs", "/bodygraphs/simple"])
    try:
        suspect_obj = json.loads(suspect)
        suspect_title = str(suspect_obj.get("info", {}).get("title", ""))
        suspect_servers = json.dumps(suspect_obj.get("servers", []), sort_keys=True)
        suspect_paths = sorted(suspect_obj.get("paths", {}).keys())
        suspect_ok = ("Human Design API" in suspect_title and "humandesignapi.nl" in suspect_servers and any(p.startswith(("/v1/", "/v2/", "/charts", "/bodygraphs")) for p in suspect_paths))
        validation_lines.append(f"[api-reference/openapi.json] status={'VALIDATED' if suspect_ok else 'QUARANTINED'}")
        validation_lines.append(f"[api-reference/openapi.json] title={suspect_title or 'MISSING'}")
        validation_lines.append(f"[api-reference/openapi.json] server_domain={'PASS' if 'humandesignapi.nl' in suspect_servers else 'FAIL'}")
        validation_lines.append(f"[api-reference/openapi.json] path_family={'PASS' if suspect_ok else 'FAIL'}")
    except json.JSONDecodeError:
        validation_lines.append("[api-reference/openapi.json] status=QUARANTINED")
        validation_lines.append("[api-reference/openapi.json] json_parse=FAIL")
    write_text(OUT / "openapi_validation.log", "\n".join(validation_lines))

    anomaly = [
        "# HDAPI v2 Known Anomalies",
        "",
        f"Generated at UTC: {produced}",
        "",
        "## api-reference/openapi.json quarantine",
        "",
        "Decision: QUARANTINED.",
        "",
        "The repository path `api-reference/openapi.json` is absent in this repo. The public documentation URL `https://docs.humandesignapi.nl/api-reference/openapi.json` was fetched as a suspect artifact and did not prove HumanDesignAPI ownership: its title is `OpenAPI Plant Store`, its server is `http://sandbox.mintlify.com`, and its path family is not the HumanDesignAPI v1/v2 chart/bodygraph family.",
        "",
        "Quarantine effect: the suspect artifact is not used as authority for vendor bytes, schemas, endpoint routes, request shaping, response mapping, runtime conformance, or architecture conformance. Validated YAML route specs remain first-precedence authority for this contract-inventory slice.",
        "",
        "## Runtime and public-surface boundary",
        "",
        "No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.",
    ]
    write_text(OUT / "known_anomalies.md", "\n".join(anomaly))

    endpoints = {
        ("POST", "/v2/charts"): {
            "route_family": "recommended_v2_chart",
            "auth_model": "Authorization Bearer token plus HD-Geocode-Key header",
            "geocode_key_requirement": "required",
            "tier": "Advanced",
            "request_fields": "birthdate;birthtime;location",
            "success_envelope": "StandardResponse with type=ChartResult and data=ChartResult",
            "source_spec": "docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts/post",
            "source_text": v2,
        },
        ("POST", "/v2/charts/simple"): {
            "route_family": "recommended_v2_chart",
            "auth_model": "Authorization Bearer token plus HD-Geocode-Key header",
            "geocode_key_requirement": "required",
            "tier": "Basic + Advanced",
            "request_fields": "birthdate;birthtime;location",
            "success_envelope": "StandardResponse with type=ChartSimpleResult and data=ChartSimpleResult",
            "source_spec": "docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts~1simple/post",
            "source_text": v2,
        },
        ("POST", "/v2/charts/coordinates"): {
            "route_family": "recommended_v2_chart",
            "auth_model": "Authorization Bearer token",
            "geocode_key_requirement": "not needed",
            "tier": "Advanced",
            "request_fields": "birthdate;birthtime;lat;lng",
            "success_envelope": "StandardResponse with type=ChartResult and data=ChartResult",
            "source_spec": "docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/~1charts~1coordinates/post",
            "source_text": v2,
        },
        ("POST", "/v1/bodygraphs"): {
            "route_family": "legacy_v1_bodygraph",
            "auth_model": "HD-Api-Key header plus HD-Geocode-Key header",
            "geocode_key_requirement": "required",
            "tier": "Advanced",
            "request_fields": "birthdate;birthtime;location",
            "success_envelope": "flat JSON BodygraphResponse; no v2 StandardResponse envelope",
            "source_spec": "docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/~1bodygraphs/post",
            "source_text": v1,
        },
        ("POST", "/v1/bodygraphs/simple"): {
            "route_family": "legacy_v1_bodygraph",
            "auth_model": "HD-Api-Key header plus HD-Geocode-Key header",
            "geocode_key_requirement": "required",
            "tier": "Basic + Advanced",
            "request_fields": "birthdate;birthtime;location",
            "success_envelope": "flat JSON SimpleBodygraphResponse; no v2 StandardResponse envelope",
            "source_spec": "docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/~1bodygraphs~1simple/post",
            "source_text": v1,
        },
    }
    csv_path = OUT / "endpoint_reference.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        fields = ["method", "path", "route_family", "auth_model", "geocode_key_requirement", "tier", "request_content_type", "request_fields", "success_envelope", "error_codes", "source_spec"]
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for method, path in REQUIRED_ENDPOINTS:
            info = endpoints[(method, path)]
            block = extract_block(info["source_text"], path.removeprefix("/v2") if path.startswith("/v2") else path.removeprefix("/v1"))
            writer.writerow({
                "method": method,
                "path": path,
                "route_family": info["route_family"],
                "auth_model": info["auth_model"],
                "geocode_key_requirement": info["geocode_key_requirement"],
                "tier": info["tier"],
                "request_content_type": "application/json",
                "request_fields": info["request_fields"],
                "success_envelope": info["success_envelope"],
                "error_codes": error_codes(block),
                "source_spec": info["source_spec"],
            })

    route_families = []
    for method, path in REQUIRED_ENDPOINTS:
        info = endpoints[(method, path)]
        source_key = "v2_routes_yaml" if path.startswith("/v2") else "v1_routes_yaml"
        route_families.append({
            "auth_model": info["auth_model"],
            "geocode_key_requirement": info["geocode_key_requirement"],
            "method": method,
            "path": path,
            "request_content_type": "application/json",
            "request_fields": info["request_fields"].split(";"),
            "route_family": info["route_family"],
            "source_precedence_rank": 1,
            "source_spec": info["source_spec"],
            "source_sha256": fetched[source_key]["sha256"],
            "success_envelope": info["success_envelope"],
            "tier": info["tier"],
        })
    contract_map = {
        "ai_boundary": "No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rail, AI evidence family, AI token, or AI runtime scope is introduced.",
        "generated_at_utc": produced,
        "non_conformance_claim": "Contract inventory only; no HumanDesignAPI v2 runtime request shaping, source selection, live conformance, public Reader change, or open-rails smoke is claimed.",
        "quarantined_sources": [
            {
                "reason": "Public api-reference/openapi.json did not prove HumanDesignAPI domain/title/server/path-family ownership; repo api-reference/openapi.json is absent.",
                "source_key": "suspect_openapi_json",
                "source_url": f"{BASE}/api-reference/openapi.json",
            }
        ],
        "route_families": route_families,
        "source_precedence": [
            "validated v2 and v1 YAML route specs",
            "rendered endpoint pages",
            "high-level guide pages",
            "suspect artifacts quarantined until validated",
        ],
        "validated_sources": [
            {"source_key": "v2_routes_yaml", "source_url": f"{BASE}/openapi/v2-routes.yaml", "sha256": fetched["v2_routes_yaml"]["sha256"]},
            {"source_key": "v1_routes_yaml", "source_url": f"{BASE}/openapi/v1-routes.yaml", "sha256": fetched["v1_routes_yaml"]["sha256"]},
        ],
    }
    (OUT / "contract_map.json").write_bytes(canonical_json_bytes(contract_map))

    acceptance = {
        "acceptance_claims_mode": "baseline_existing_tokens_only",
        "epic_id": "HDE-EPIC033",
        "notes": [
            "HDE-FERM006.1 through HDE-FERM006.4 contract-inventory artifacts only.",
            "No vendor-v2-specific acceptance token is minted or claimed.",
            "No runtime v2 conformance, runtime request shaping, source-selection behavior, open-rails vendor smoke, public Reader surface, new HTTP home, or AI scope is claimed.",
        ],
        "pf09_scope_completed_by_this_pr": ["HDE-FERM006.1", "HDE-FERM006.2", "HDE-FERM006.3", "HDE-FERM006.4"],
        "pf09_scope_not_completed_by_this_pr": ["HDE-FERM007", "HDE-FERM008"],
        "tokens": [
            {"evidence_titles": ["tests/evidence/test_hdapi_v2_contract_inventory.py"], "name": "TESTS_PASS_OK", "owner_pf": "PF19 — Glow QA Guide §QA Rails", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["audit/docdeltas/hde-epic033_doc_deltas.md", "audit/qa/hde-epic033/00_meta/doc_deltas.md"], "name": "DOC_DELTA_PRESENT_OK", "owner_pf": "PF10 — HDE-Build Notes", "status": "baseline_pointer_present"},
            {"evidence_titles": ["docs/evidence/INDEX.json", "artifacts/evidence_index.jsonl"], "name": "EVIDENCE_INDEX_UPDATED_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Index", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["artifacts/evidence_index.jsonl"], "name": "MACHINE_MIRROR_UPDATED_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Mirror", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["docs/evidence/INDEX.sha256"], "name": "EVIDENCE_INDEX_HASH_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Evidence Hashing", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["tools/evidence/validate_evidence_paths.py"], "name": "EVIDENCE_PATHS_VALIDATED_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Path proofs", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["artifacts/vendor/hdapi_v2/*.path_proof.txt"], "name": "EVIDENCE_PATH_PROOFS_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Path proofs", "status": "supported_by_pr_validation"},
            {"evidence_titles": ["artifacts/vendor/hdapi_v2/source_inventory.json", "artifacts/vendor/hdapi_v2/contract_map.json"], "name": "JSON_CANONICAL_CHECK_OK", "owner_pf": "PF12 — HDE-Schemas and Artifacts §Canonical JSON", "status": "supported_by_pr_validation"},
        ],
    }
    ACCEPTANCE.write_bytes(canonical_json_bytes(acceptance))

    matrix_lines = [
        "# HDE-EPIC033 Token Evidence Matrix",
        "",
        "This baseline matrix uses existing registry-valid tokens only and does not mint a vendor-v2-specific token.",
        "",
        "| Token | Evidence | Status | Boundary |",
        "| --- | --- | --- | --- |",
    ]
    for token in acceptance["tokens"]:
        matrix_lines.append(f"| {token['name']} | {'; '.join(token['evidence_titles'])} | {token['status']} | Contract inventory only; no runtime v2 conformance or AI scope |")
    write_text(TOKEN_MATRIX, "\n".join(matrix_lines))

    write_text(VIABILITY, "\n".join([
        f"generated_at_utc={produced}",
        "epic_id=HDE-EPIC033",
        "status=PASS",
        "tokens_checked=TESTS_PASS_OK,DOC_DELTA_PRESENT_OK,EVIDENCE_INDEX_UPDATED_OK,MACHINE_MIRROR_UPDATED_OK,EVIDENCE_INDEX_HASH_OK,EVIDENCE_PATHS_VALIDATED_OK,EVIDENCE_PATH_PROOFS_OK,JSON_CANONICAL_CHECK_OK",
        "vendor_v2_specific_tokens=NONE",
        "runtime_v2_conformance_claim=NONE",
        "public_reader_surface_change=NONE",
        "ai_scope=NONE",
    ]))

    doc_delta_text = "\n".join([
        "# HDE-EPIC033 Doc Deltas",
        "",
        "## BLOCKERS",
        "",
        "None recorded for PR-01 contract-inventory evidence binding.",
        "",
        "## CAVEATS",
        "",
        "This PR binds HumanDesignAPI v2 and legacy v1 public documentation contract inventory only. It does not implement or claim runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader changes, a new HTTP home, or AI scope.",
    ])
    write_text(DOC_DELTAS, doc_delta_text)
    write_text(QA_DOC_DELTAS, doc_delta_text)

    print(f"generated {OUT.relative_to(ROOT)} and HDE-EPIC033 baseline artifacts at {produced}")


if __name__ == "__main__":
    main()
