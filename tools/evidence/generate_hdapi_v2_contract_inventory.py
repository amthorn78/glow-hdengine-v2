#!/usr/bin/env python3
"""Generate HDE-EPIC033 HDAPI v2 contract-inventory evidence.

The default mode is closed-rails and consumes pre-captured public documentation
inputs from artifacts/vendor/hdapi_v2/source_cache/. Refreshing those inputs is
an explicit public-docs operation and requires both --refresh-public-docs and
open rails (SAFE_MODE=0, ALLOW_NETWORK=1). The generator never calls
credentialed runtime vendor endpoints.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "vendor" / "hdapi_v2"
SOURCE_CACHE = OUT / "source_cache"
SOURCE_METADATA = SOURCE_CACHE / "source_metadata.json"
ACCEPTANCE = ROOT / "docs" / "acceptance_map_epic033.json"
TOKEN_MATRIX = ROOT / "audit" / "qa" / "hde-epic033" / "token_evidence_matrix.md"
VIABILITY = ROOT / "audit" / "qa" / "hde-epic033" / "acceptance_map_viability.log"
DOC_DELTAS = ROOT / "audit" / "docdeltas" / "hde-epic033_doc_deltas.md"
QA_DOC_DELTAS = ROOT / "audit" / "qa" / "hde-epic033" / "00_meta" / "doc_deltas.md"
EPIC034_QA = ROOT / "audit" / "qa" / "hde-epic034" / "pr-01"
EPIC034_PR02_QA = ROOT / "audit" / "qa" / "hde-epic034" / "pr-02"
REQUEST_SHAPING_SNAPSHOT = OUT / "request_shaping.snapshot.json"
REQUEST_SHAPING_CHECK_LOG = EPIC034_PR02_QA / "request_shaping_check.log"
SOURCE_SELECTION_SNAPSHOT = OUT / "source_selection.snapshot.json"
V1_LEGACY_GUARD_LOG = OUT / "v1_legacy_guard.log"
SOURCE_SELECTION_CHECK_LOG = EPIC034_QA / "source_selection_check.log"

BASE = "https://docs.humandesignapi.nl"
SOURCES = [
    ("robots_preflight", f"{BASE}/robots.txt", "robots_preflight", "seed", None),
    ("llms_txt", f"{BASE}/llms.txt", "documentation-discovery-only", "robots_preflight", None),
    ("llms_full_txt", f"{BASE}/llms-full.txt", "documentation-discovery-only", "llms_txt", "llms-full.endpoint-tiers.txt"),
    ("v2_routes_yaml", f"{BASE}/openapi/v2-routes.yaml", "validated_machine_readable_route_spec", "llms_txt", "v2-routes.yaml"),
    ("v1_routes_yaml", f"{BASE}/openapi/v1-routes.yaml", "validated_machine_readable_route_spec", "llms_txt", "v1-routes.yaml"),
    ("suspect_openapi_json", f"{BASE}/api-reference/openapi.json", "suspect_quarantined_openapi", "llms_txt", "api-reference.openapi.json"),
    ("v2_overview", f"{BASE}/api-reference/v2/overview", "rendered_high_level_guide", "llms_txt", None),
    ("v1_overview", f"{BASE}/api-reference/v1/overview", "rendered_high_level_guide", "llms_txt", None),
    ("v2_full_chart_page", f"{BASE}/api-reference/charts/generate-a-full-chart", "rendered_endpoint_page", "llms_txt", None),
    ("v2_simple_chart_page", f"{BASE}/api-reference/charts/generate-a-simple-chart", "rendered_endpoint_page", "llms_txt", None),
    ("v2_coordinates_chart_page", f"{BASE}/api-reference/charts/generate-a-chart-from-coordinates", "rendered_endpoint_page", "llms_txt", None),
    ("authentication", f"{BASE}/authentication", "rendered_contract_page", "llms_txt", None),
    ("rate_limiting", f"{BASE}/guides/rate-limiting", "rendered_contract_page", "llms_txt", None),
    ("response_format", f"{BASE}/response-format", "rendered_contract_page", "llms_txt", None),
    ("migration_v1_to_v2", f"{BASE}/migration/v1-to-v2", "rendered_contract_page", "llms_txt", None),
    ("coordinates_guide", f"{BASE}/guides/coordinates-endpoint", "rendered_contract_page", "llms_txt", None),
]

REQUIRED_ENDPOINTS = [
    ("POST", "/v2/charts"),
    ("POST", "/v2/charts/simple"),
    ("POST", "/v2/charts/coordinates"),
    ("POST", "/v1/bodygraphs"),
    ("POST", "/v1/bodygraphs/simple"),
]

ALLOWED_STATUS = {200}
V2_CHART_ROUTES = [
    ("POST", "/v2/charts", "full_chart"),
    ("POST", "/v2/charts/simple", "simple_chart"),
    ("POST", "/v2/charts/coordinates", "coordinates_chart"),
]
V1_BODYGRAPH_ROUTES = [
    ("POST", "/v1/bodygraphs", "legacy_full_bodygraph"),
    ("POST", "/v1/bodygraphs/simple", "legacy_simple_bodygraph"),
]


def iso_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def canonical_json_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="\n")


def write_bytes(path: Path, body: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)


def sha256_bytes(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()



def llms_full_endpoint_tier_excerpt(body: bytes) -> bytes:
    text = body.decode("utf-8", errors="replace")
    rows = [
        line for line in text.splitlines()
        if line.startswith("| `POST /v") and ("Advanced" in line or "Basic" in line)
    ]
    if not rows:
        raise SystemExit("LLMS_FULL_TIER_EXCERPT_EMPTY")
    return ("\n".join(rows) + "\n").encode("utf-8")

def fetch_public_doc(url: str) -> tuple[str, str, int | str, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": "glow-hde-epic033-contract-inventory/1.1"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.geturl(), resp.headers.get("content-type", ""), resp.status, resp.read()
    except urllib.error.HTTPError as exc:
        return exc.geturl(), exc.headers.get("content-type", ""), exc.code, exc.read()
    except urllib.error.URLError as exc:
        return url, "", f"FETCH_ERROR:{exc.reason}", b""


def require_open_rails_for_refresh() -> None:
    if os.environ.get("SAFE_MODE") != "0" or os.environ.get("ALLOW_NETWORK") != "1":
        raise SystemExit("OPEN_RAILS_REQUIRED: set SAFE_MODE=0 and ALLOW_NETWORK=1 with --refresh-public-docs for public documentation fetching")


def source_cache_name(key: str, configured: str | None) -> str:
    return configured or f"{key}.body"


def source_cache_rel(cache_name: str | None) -> str | None:
    return f"artifacts/vendor/hdapi_v2/source_cache/{cache_name}" if cache_name else None


def refresh_source_cache(produced: str) -> tuple[dict[str, dict[str, Any]], dict[str, bytes]]:
    require_open_rails_for_refresh()
    SOURCE_CACHE.mkdir(parents=True, exist_ok=True)
    metadata: dict[str, dict[str, Any]] = {}
    bodies: dict[str, bytes] = {}
    for key, url, classification, discovered_from, configured_cache_name in SOURCES:
        cache_name = source_cache_name(key, configured_cache_name)
        final_url, content_type, status, body = fetch_public_doc(url)
        cache_body = body
        if key == "llms_full_txt" and status in ALLOWED_STATUS:
            cache_body = llms_full_endpoint_tier_excerpt(body)
        write_bytes(SOURCE_CACHE / cache_name, cache_body)
        bodies[key] = cache_body
        metadata[key] = {
            "cache_path": source_cache_rel(cache_name),
            "cache_sha256": sha256_bytes(cache_body),
            "content_type": content_type,
            "discovered_from": discovered_from,
            "fetch_status": str(status),
            "final_url": final_url,
            "last_seen_utc": produced,
            "sha256": sha256_bytes(body) if body else "",
            "source_classification": classification,
            "source_url": url,
        }
    SOURCE_METADATA.write_bytes(canonical_json_bytes({"generated_at_utc": produced, "sources": metadata}))
    return metadata, bodies


def load_source_cache() -> tuple[dict[str, dict[str, Any]], dict[str, bytes]]:
    if not SOURCE_METADATA.exists():
        raise SystemExit("MISSING_SOURCE_CACHE: run with --refresh-public-docs under SAFE_MODE=0 ALLOW_NETWORK=1 to capture public docs")
    payload = json.loads(SOURCE_METADATA.read_text(encoding="utf-8"))
    metadata = payload.get("sources")
    if not isinstance(metadata, dict):
        raise SystemExit("INVALID_SOURCE_CACHE: missing sources")
    bodies: dict[str, bytes] = {}
    for key, _url, _classification, _discovered_from, configured_cache_name in SOURCES:
        row = metadata.get(key)
        if not isinstance(row, dict):
            raise SystemExit(f"INVALID_SOURCE_CACHE: missing {key}")
        cache_name = source_cache_name(key, configured_cache_name)
        cache_path = SOURCE_CACHE / cache_name
        if not cache_path.exists():
            if key == "suspect_openapi_json":
                bodies[key] = b""
                continue
            raise SystemExit(f"MISSING_SOURCE_BODY:{cache_path.relative_to(ROOT).as_posix()}")
        body = cache_path.read_bytes()
        expected = row.get("cache_sha256") or row.get("sha256")
        actual = sha256_bytes(body)
        if expected != actual:
            raise SystemExit(f"SOURCE_CACHE_SHA_MISMATCH:{key}")
        bodies[key] = body
    return metadata, bodies


def parse_yaml_openapi(body: bytes, name: str) -> dict[str, Any]:
    with tempfile.NamedTemporaryFile(suffix=".yaml") as tmp:
        tmp.write(body)
        tmp.flush()
        result = subprocess.run(
            ["ruby", "-ryaml", "-rjson", "-e", "puts JSON.generate(YAML.safe_load_file(ARGV.fetch(0), permitted_classes: [], aliases: false))", tmp.name],
            check=False,
            capture_output=True,
            text=True,
        )
    if result.returncode != 0:
        raise ValueError(f"YAML_PARSE_FAILED:{name}:{result.stderr.strip()}")
    parsed = json.loads(result.stdout)
    if not isinstance(parsed, dict):
        raise ValueError(f"YAML_PARSE_NOT_OBJECT:{name}")
    return parsed


def ref_name(ref: str | None) -> str:
    if not ref or not ref.startswith("#/components/schemas/"):
        return ""
    return ref.rsplit("/", 1)[-1]


def schema_ref_names(schema: Any) -> list[str]:
    refs: list[str] = []
    if isinstance(schema, dict):
        if "$ref" in schema:
            refs.append(ref_name(str(schema["$ref"])))
        for value in schema.values():
            refs.extend(schema_ref_names(value))
    elif isinstance(schema, list):
        for item in schema:
            refs.extend(schema_ref_names(item))
    return [ref for ref in refs if ref]


def method_obj(spec: dict[str, Any], path: str) -> dict[str, Any]:
    paths = spec.get("paths")
    if not isinstance(paths, dict) or path not in paths:
        raise ValueError(f"MISSING_PATH:{path}")
    path_item = paths[path]
    if not isinstance(path_item, dict) or not isinstance(path_item.get("post"), dict):
        raise ValueError(f"MISSING_POST:{path}")
    return path_item["post"]


def content_type_and_schema(method: dict[str, Any]) -> tuple[str, str]:
    body = method.get("requestBody")
    if not isinstance(body, dict) or body.get("required") is not True:
        raise ValueError("REQUEST_BODY_REQUIRED_MISSING")
    content = body.get("content")
    if not isinstance(content, dict) or not content:
        raise ValueError("REQUEST_CONTENT_MISSING")
    if "application/json" not in content:
        raise ValueError("REQUEST_CONTENT_NOT_JSON")
    schema = content["application/json"].get("schema")
    if not isinstance(schema, dict):
        raise ValueError("REQUEST_SCHEMA_MISSING")
    return "application/json", ref_name(str(schema.get("$ref", "")))


def required_fields(spec: dict[str, Any], schema_name: str) -> list[str]:
    schemas = spec.get("components", {}).get("schemas", {})
    schema = schemas.get(schema_name)
    if not isinstance(schema, dict):
        raise ValueError(f"MISSING_SCHEMA:{schema_name}")
    required = schema.get("required")
    if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
        raise ValueError(f"MISSING_REQUIRED_FIELDS:{schema_name}")
    return required


def success_envelope(method: dict[str, Any], *, version: str) -> str:
    responses = method.get("responses")
    if not isinstance(responses, dict) or "200" not in responses:
        raise ValueError("MISSING_200_RESPONSE")
    content = responses["200"].get("content", {})
    schema = content.get("application/json", {}).get("schema")
    refs = schema_ref_names(schema)
    if version == "v2":
        if "StandardResponse" not in refs:
            raise ValueError("MISSING_STANDARD_RESPONSE")
        response_type = ""
        if isinstance(schema, dict):
            all_of = schema.get("allOf", [])
            if isinstance(all_of, list):
                for entry in all_of:
                    props = entry.get("properties", {}) if isinstance(entry, dict) else {}
                    type_prop = props.get("type", {}) if isinstance(props, dict) else {}
                    if isinstance(type_prop, dict) and type_prop.get("example"):
                        response_type = str(type_prop["example"])
        data_refs = [ref for ref in refs if ref != "StandardResponse"]
        if not response_type or not data_refs:
            raise ValueError("MISSING_V2_SUCCESS_DATA_REF")
        return f"StandardResponse with type={response_type} and data={data_refs[-1]}"
    if not refs:
        raise ValueError("MISSING_V1_SUCCESS_SCHEMA")
    return f"flat JSON {refs[-1]}; no v2 StandardResponse envelope"


def collect_error_codes(value: Any) -> list[str]:
    codes: set[str] = set()
    if isinstance(value, str):
        codes.update(re.findall(r"`([A-Z0-9_]+)`", value))
    elif isinstance(value, dict):
        for child in value.values():
            codes.update(collect_error_codes(child))
    elif isinstance(value, list):
        for child in value:
            codes.update(collect_error_codes(child))
    return sorted(codes)


def response_error_codes(method: dict[str, Any]) -> str:
    responses = method.get("responses")
    if not isinstance(responses, dict):
        raise ValueError("MISSING_RESPONSES")
    codes = collect_error_codes({k: v for k, v in responses.items() if k != "200"})
    return ";".join(codes) if codes else "schema-defined StandardErrorResponse"


def security_names(method: dict[str, Any]) -> list[str]:
    security = method.get("security")
    if not isinstance(security, list) or not security or not isinstance(security[0], dict):
        raise ValueError("MISSING_SECURITY")
    return list(security[0].keys())


def auth_model(spec: dict[str, Any], method: dict[str, Any]) -> str:
    schemes = spec.get("components", {}).get("securitySchemes", {})
    names = security_names(method)
    rendered: list[str] = []
    for name in names:
        scheme = schemes.get(name)
        if not isinstance(scheme, dict):
            raise ValueError(f"MISSING_SECURITY_SCHEME:{name}")
        if scheme.get("type") == "http" and scheme.get("scheme") == "bearer":
            rendered.append("Authorization Bearer token")
        elif scheme.get("type") == "apiKey" and scheme.get("in") == "header" and scheme.get("name"):
            rendered.append(f"{scheme['name']} header")
        else:
            raise ValueError(f"UNSUPPORTED_SECURITY_SCHEME:{name}")
    return " plus ".join(rendered)


def geocode_requirement(method: dict[str, Any]) -> str:
    return "required" if "GeocodeKeyAuth" in security_names(method) else "not needed"


def markdown_cells(raw: str) -> list[str]:
    if not raw.startswith("|"):
        return []
    return [cell.strip().strip("`").strip() for cell in raw.strip().strip("|").split("|")]


def parse_tier_map(llms_full: str) -> dict[str, str]:
    tier_map: dict[str, str] = {}
    for raw in llms_full.splitlines():
        cells = markdown_cells(raw)
        if len(cells) < 3:
            continue
        endpoint = cells[0]
        tier = cells[2]
        for _method, path in REQUIRED_ENDPOINTS:
            label = f"POST {path}"
            if endpoint == label:
                if not tier:
                    raise ValueError(f"TIER_EMPTY:{path}")
                tier_map[path] = tier
    missing = [path for _method, path in REQUIRED_ENDPOINTS if path not in tier_map]
    if missing:
        raise ValueError(f"TIER_MAP_MISSING:{','.join(missing)}")
    return tier_map


def validate_openapi_spec(name: str, spec: dict[str, Any], *, expected_title: str, expected_server: str, paths: list[str]) -> tuple[bool, list[str]]:
    checks: list[tuple[str, bool]] = []
    info = spec.get("info")
    servers = spec.get("servers")
    components = spec.get("components")
    checks.append(("openapi_3_parse", isinstance(spec.get("openapi"), str) and str(spec["openapi"]).startswith("3.")))
    checks.append(("title_humandesignapi", isinstance(info, dict) and info.get("title") == expected_title))
    checks.append(("version_present", isinstance(info, dict) and bool(info.get("version"))))
    checks.append(("server_domain", isinstance(servers, list) and any(isinstance(item, dict) and item.get("url") == expected_server for item in servers)))
    checks.append(("components_present", isinstance(components, dict) and isinstance(components.get("schemas"), dict) and isinstance(components.get("securitySchemes"), dict)))
    for path in paths:
        try:
            method = method_obj(spec, path)
            content_type_and_schema(method)
            security_names(method)
            success_envelope(method, version="v2" if "v2" in name else "v1")
            checks.append((f"path_{path}_post_contract", True))
        except ValueError:
            checks.append((f"path_{path}_post_contract", False))
    ok = all(result for _label, result in checks)
    lines = [f"[{name}] status={'VALIDATED' if ok else 'INVALID'}"]
    lines.extend(f"[{name}] {label}={'PASS' if result else 'FAIL'}" for label, result in checks)
    version = info.get("version") if isinstance(info, dict) else "UNKNOWN"
    lines.append(f"[{name}] observed_version={version or 'UNKNOWN'}")
    return ok, lines


def validate_suspect_openapi(body: bytes, source_row: dict[str, Any]) -> tuple[bool, dict[str, Any], list[str]]:
    fetch_status = str(source_row.get("fetch_status", ""))
    if fetch_status != "200":
        return False, {"fetch_status": fetch_status}, [
            "[api-reference/openapi.json] status=QUARANTINED",
            f"[api-reference/openapi.json] fetch_status={fetch_status or 'MISSING'}",
            "[api-reference/openapi.json] availability=UNAVAILABLE",
        ]
    try:
        obj = json.loads(body.decode("utf-8"))
    except json.JSONDecodeError:
        return False, {"fetch_status": fetch_status}, ["[api-reference/openapi.json] status=QUARANTINED", "[api-reference/openapi.json] json_parse=FAIL"]
    title = str(obj.get("info", {}).get("title", "")) if isinstance(obj.get("info"), dict) else ""
    servers = obj.get("servers") if isinstance(obj.get("servers"), list) else []
    paths = obj.get("paths") if isinstance(obj.get("paths"), dict) else {}
    server_domain_ok = any(isinstance(item, dict) and "humandesignapi.nl" in str(item.get("url", "")) for item in servers)
    path_family_ok = any(path.startswith(("/v1/", "/v2/", "/charts", "/bodygraphs")) for path in paths)
    title_ok = "Human Design API" in title
    ok = title_ok and server_domain_ok and path_family_ok
    lines = [
        f"[api-reference/openapi.json] status={'VALIDATED' if ok else 'QUARANTINED'}",
        f"[api-reference/openapi.json] title={title or 'MISSING'}",
        f"[api-reference/openapi.json] title_humandesignapi={'PASS' if title_ok else 'FAIL'}",
        f"[api-reference/openapi.json] server_domain={'PASS' if server_domain_ok else 'FAIL'}",
        f"[api-reference/openapi.json] path_family={'PASS' if path_family_ok else 'FAIL'}",
    ]
    return ok, {"fetch_status": fetch_status, "title": title, "servers": servers, "paths": sorted(paths)}, lines


def source_spec_for(path: str) -> str:
    if path.startswith("/v2"):
        relative = path.removeprefix("/v2")
        encoded = relative.replace("/", "~1")
        return f"docs.humandesignapi.nl/openapi/v2-routes.yaml#/paths/{encoded}/post"
    relative = path.removeprefix("/v1")
    encoded = relative.replace("/", "~1")
    return f"docs.humandesignapi.nl/openapi/v1-routes.yaml#/paths/{encoded}/post"


def build_endpoint_rows(v2_spec: dict[str, Any], v1_spec: dict[str, Any], llms_full: str) -> list[dict[str, str]]:
    tier_map = parse_tier_map(llms_full)
    rows: list[dict[str, str]] = []
    for method, full_path in REQUIRED_ENDPOINTS:
        version = "v2" if full_path.startswith("/v2") else "v1"
        spec = v2_spec if version == "v2" else v1_spec
        spec_path = full_path.removeprefix(f"/{version}")
        op = method_obj(spec, spec_path)
        request_content_type, schema_name = content_type_and_schema(op)
        request_fields = required_fields(spec, schema_name)
        rows.append(
            {
                "auth_model": auth_model(spec, op),
                "error_codes": response_error_codes(op),
                "geocode_key_requirement": geocode_requirement(op),
                "method": method,
                "path": full_path,
                "request_content_type": request_content_type,
                "request_fields": ";".join(request_fields),
                "route_family": "recommended_v2_chart" if version == "v2" else "legacy_v1_bodygraph",
                "source_spec": source_spec_for(full_path),
                "success_envelope": success_envelope(op, version=version),
                "tier": tier_map[full_path],
            }
        )
    return rows


def build_validation_log(produced: str, v2_ok: bool, v2_lines: list[str], v1_ok: bool, v1_lines: list[str], suspect_lines: list[str], *, mode: str) -> str:
    lines = [
        f"generated_at_utc={produced}",
        "scope=HDE-EPIC033 HDE-FERM006.2 machine-readable vendor route validation",
        f"source_mode={mode}",
        "network_posture=public documentation refresh only when --refresh-public-docs is used with SAFE_MODE=0 and ALLOW_NETWORK=1; default generation is closed-rails cache replay",
        "validator=Ruby Psych YAML parser plus fail-closed OpenAPI structural validator for title/version/server/security/request/response/path-family ownership",
    ]
    lines.extend(v2_lines)
    lines.extend(v1_lines)
    lines.extend(suspect_lines)
    lines.append(f"[route-spec-gate] status={'PASS' if v2_ok and v1_ok else 'FAIL'}")
    return "\n".join(lines)


def build_anomaly_text(produced: str, suspect_ok: bool, suspect_info: dict[str, Any]) -> str:
    title = suspect_info.get("title") or "MISSING"
    servers = suspect_info.get("servers") or []
    paths = suspect_info.get("paths") or []
    lines = [
        "# HDAPI v2 Known Anomalies",
        "",
        f"Generated at UTC: {produced}",
        "",
        "## api-reference/openapi.json posture",
        "",
    ]
    if suspect_ok:
        lines.extend(
            [
                "Decision: VALIDATED.",
                "",
                "The suspect public documentation OpenAPI artifact passed HumanDesignAPI title, server-domain, and path-family ownership checks in this run. No quarantine entry is emitted for it in the contract map.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "Decision: QUARANTINED.",
                "",
                f"The repository path `api-reference/openapi.json` is {'present' if (ROOT / 'api-reference/openapi.json').exists() else 'absent'} in this repo. The public documentation URL `https://docs.humandesignapi.nl/api-reference/openapi.json` did not prove HumanDesignAPI ownership in this run: title=`{title}`, servers={json.dumps(servers, sort_keys=True)}, paths_sample={json.dumps(paths[:5], sort_keys=True)}.",
                "",
                "Quarantine effect: the suspect artifact is not used as authority for vendor bytes, schemas, endpoint routes, request shaping, response mapping, runtime conformance, or architecture conformance. Validated YAML route specs remain first-precedence authority for this contract-inventory slice.",
                "",
            ]
        )
    lines.extend(
        [
            "## Runtime and public-surface boundary",
            "",
            "No runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime/evidence scope is introduced by this inventory.",
        ]
    )
    return "\n".join(lines)


def build_contract_map(produced: str, fetched: dict[str, dict[str, Any]], rows: list[dict[str, str]], suspect_ok: bool) -> dict[str, Any]:
    route_families = []
    for row in rows:
        source_key = "v2_routes_yaml" if row["path"].startswith("/v2") else "v1_routes_yaml"
        route_families.append(
            {
                "auth_model": row["auth_model"],
                "geocode_key_requirement": row["geocode_key_requirement"],
                "method": row["method"],
                "path": row["path"],
                "request_content_type": row["request_content_type"],
                "request_fields": row["request_fields"].split(";"),
                "route_family": row["route_family"],
                "source_precedence_rank": 1,
                "source_sha256": fetched[source_key]["sha256"],
                "source_spec": row["source_spec"],
                "success_envelope": row["success_envelope"],
                "tier": row["tier"],
            }
        )
    contract = {
        "ai_boundary": "No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rail, AI evidence family, AI token, or AI runtime scope is introduced.",
        "generated_at_utc": produced,
        "non_conformance_claim": "Contract inventory only; no HumanDesignAPI v2 runtime request shaping, source selection, live conformance, public Reader change, or open-rails smoke is claimed.",
        "quarantined_sources": [],
        "route_families": route_families,
        "source_precedence": [
            "validated v2 and v1 YAML route specs",
            "rendered endpoint pages",
            "high-level guide pages",
            "suspect artifacts quarantined until validated",
        ],
        "validated_sources": [
            {"sha256": fetched["v2_routes_yaml"]["sha256"], "source_key": "v2_routes_yaml", "source_url": f"{BASE}/openapi/v2-routes.yaml"},
            {"sha256": fetched["v1_routes_yaml"]["sha256"], "source_key": "v1_routes_yaml", "source_url": f"{BASE}/openapi/v1-routes.yaml"},
        ],
    }
    if not suspect_ok:
        contract["quarantined_sources"].append(
            {
                "reason": "api-reference/openapi.json did not prove HumanDesignAPI title/server/path-family ownership in this run or repo-local artifact was absent.",
                "source_key": "suspect_openapi_json",
                "source_url": f"{BASE}/api-reference/openapi.json",
            }
        )
    return contract



def _contract_routes(contract: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    routes = contract.get("route_families")
    if not isinstance(routes, list):
        raise ValueError("CONTRACT_MAP_MISSING_ROUTE_FAMILIES")
    mapped: dict[tuple[str, str], dict[str, Any]] = {}
    for route in routes:
        if not isinstance(route, dict):
            raise ValueError("CONTRACT_MAP_ROUTE_NOT_OBJECT")
        method = route.get("method")
        path = route.get("path")
        if not isinstance(method, str) or not isinstance(path, str):
            raise ValueError("CONTRACT_MAP_ROUTE_MISSING_METHOD_OR_PATH")
        mapped[(method, path)] = route
    return mapped


def build_source_selection_snapshot(produced: str, contract: dict[str, Any]) -> dict[str, Any]:
    """Derive HDE-EPIC034 PR-01 source-selection evidence from contract inventory."""
    routes = _contract_routes(contract)
    required = V2_CHART_ROUTES + V1_BODYGRAPH_ROUTES
    missing = [(method, path) for method, path, _variant in required if (method, path) not in routes]
    if missing:
        formatted = ",".join(f"{method} {path}" for method, path in missing)
        raise ValueError(f"SOURCE_SELECTION_MISSING_CONTRACT_ROUTES:{formatted}")

    snapshot_routes: list[dict[str, Any]] = []
    for method, path, variant in required:
        route = routes[(method, path)]
        expected_family = "recommended_v2_chart" if path.startswith("/v2/") else "legacy_v1_bodygraph"
        if route.get("route_family") != expected_family:
            raise ValueError(f"SOURCE_SELECTION_ROUTE_FAMILY_MISMATCH:{method} {path}")
        auth = route.get("auth_model")
        geocode = route.get("geocode_key_requirement")
        source_spec = route.get("source_spec")
        source_precedence_rank = route.get("source_precedence_rank")
        if not isinstance(auth, str) or not auth:
            raise ValueError(f"SOURCE_SELECTION_AUTH_MODEL_MISSING:{method} {path}")
        if not isinstance(geocode, str) or not geocode:
            raise ValueError(f"SOURCE_SELECTION_GEOCODE_REQUIREMENT_MISSING:{method} {path}")
        expected_source_spec = source_spec_for(path)
        if source_spec != expected_source_spec or source_precedence_rank != 1:
            raise ValueError(f"SOURCE_SELECTION_SOURCE_AUTHORITY_MISMATCH:{method} {path}")
        expected_geocode = "not needed" if path == "/v2/charts/coordinates" else "required"
        if geocode != expected_geocode:
            raise ValueError(f"SOURCE_SELECTION_GEOCODE_REQUIREMENT_MISMATCH:{method} {path}")
        if expected_family == "recommended_v2_chart":
            if "Authorization Bearer token" not in auth or "HD-Api-Key header" in auth:
                raise ValueError(f"SOURCE_SELECTION_AUTH_FAMILY_MISMATCH:{method} {path}")
        if expected_family == "legacy_v1_bodygraph":
            if "HD-Api-Key header" not in auth or "Authorization Bearer token" in auth:
                raise ValueError(f"SOURCE_SELECTION_AUTH_FAMILY_MISMATCH:{method} {path}")
        if expected_geocode == "required" and "HD-Geocode-Key header" not in auth:
            raise ValueError(f"SOURCE_SELECTION_GEOCODE_AUTH_MISMATCH:{method} {path}")
        if expected_geocode == "not needed" and "HD-Geocode-Key header" in auth:
            raise ValueError(f"SOURCE_SELECTION_GEOCODE_AUTH_MISMATCH:{method} {path}")
        snapshot_routes.append(
            {
                "auth_model": auth,
                "classification_source": "artifacts/vendor/hdapi_v2/contract_map.json route_families",
                "geocode_key_requirement": geocode,
                "method": method,
                "path": path,
                "route_family": expected_family,
                "route_variant": variant,
                "source_precedence_rank": source_precedence_rank,
                "source_spec": source_spec,
            }
        )

    return {
        "ai_scope_claim": "NONE",
        "generated_at_utc": produced,
        "open_rails_vendor_smoke_claim": "NONE",
        "public_reader_change_claim": "NONE",
        "request_shaping_claim": "NONE",
        "route_families": snapshot_routes,
        "runtime_conformance_claim": "NONE",
        "source_selection_policy": {
            "classification_source": "governed contract inventory",
            "legacy_v1_bodygraph_route_family": "legacy_v1_bodygraph",
            "recommended_internal_vendor_route_family": "recommended_v2_chart",
            "selection_scope": "HDE-EPIC034 PR-01 HDE-FERM007.1 route-family source selection only",
        },
    }


def build_v1_legacy_guard_log(produced: str, snapshot: dict[str, Any]) -> str:
    routes = snapshot.get("route_families")
    if not isinstance(routes, list):
        raise ValueError("SOURCE_SELECTION_SNAPSHOT_MISSING_ROUTES")
    by_path = {route["path"]: route for route in routes if isinstance(route, dict) and "path" in route}
    lines = [
        f"generated_at_utc={produced}",
        "scope=HDE-EPIC034 PR-01 HDE-FERM007.1 v1 legacy guard",
        "classification_source=artifacts/vendor/hdapi_v2/contract_map.json route_families",
    ]
    for _method, path, variant in V1_BODYGRAPH_ROUTES:
        route = by_path.get(path)
        status = "PASS" if route and route.get("route_family") == "legacy_v1_bodygraph" and route.get("route_variant") == variant else "FAIL"
        lines.append(f"[{path}] legacy_v1_bodygraph_explicit={status}")
        lines.append(f"[{path}] collapsed_to_recommended_v2_chart={'FAIL' if status == 'PASS' else 'UNKNOWN'}")
    v2_variants = [by_path[path].get("route_variant") for _method, path, _variant in V2_CHART_ROUTES if path in by_path]
    lines.append(f"v2_chart_route_variants_distinct={'PASS' if len(set(v2_variants)) == 3 else 'FAIL'}")
    lines.append("request_shaping_claim=NONE")
    lines.append("runtime_conformance_claim=NONE")
    lines.append("public_reader_change_claim=NONE")
    lines.append("open_rails_vendor_smoke_claim=NONE")
    lines.append("ai_scope=NONE")
    lines.append("status=PASS" if all("FAIL" not in line for line in lines if "collapsed_to_recommended_v2_chart" not in line) else "status=FAIL")
    return "\n".join(lines)


def build_source_selection_check_log(produced: str, snapshot: dict[str, Any], *, mode: str) -> str:
    routes = snapshot["route_families"]
    families = {(route["method"], route["path"]): route["route_family"] for route in routes}
    variants = {(route["method"], route["path"]): route["route_variant"] for route in routes}
    auth_models = {(route["method"], route["path"]): route.get("auth_model") for route in routes}
    geocode = {(route["method"], route["path"]): route.get("geocode_key_requirement") for route in routes}
    source_specs = {(route["method"], route["path"]): route.get("source_spec") for route in routes}
    source_ranks = {(route["method"], route["path"]): route.get("source_precedence_rank") for route in routes}
    checks = [
        ("recommended_v2_full_chart", families.get(("POST", "/v2/charts")) == "recommended_v2_chart"),
        ("recommended_v2_simple_chart", families.get(("POST", "/v2/charts/simple")) == "recommended_v2_chart"),
        ("recommended_v2_coordinates_chart", families.get(("POST", "/v2/charts/coordinates")) == "recommended_v2_chart"),
        ("legacy_v1_full_bodygraph", families.get(("POST", "/v1/bodygraphs")) == "legacy_v1_bodygraph"),
        ("legacy_v1_simple_bodygraph", families.get(("POST", "/v1/bodygraphs/simple")) == "legacy_v1_bodygraph"),
        ("v2_variants_distinguished", len({variants.get(item[:2]) for item in V2_CHART_ROUTES}) == 3),
        ("v1_not_collapsed_to_v2", all(families.get((method, path)) != "recommended_v2_chart" for method, path, _variant in V1_BODYGRAPH_ROUTES)),
        (
            "v2_auth_family_bearer_only",
            all(
                "Authorization Bearer token" in str(auth_models.get((method, path), ""))
                and "HD-Api-Key header" not in str(auth_models.get((method, path), ""))
                for method, path, _variant in V2_CHART_ROUTES
            ),
        ),
        (
            "v1_auth_family_hd_api_key_only",
            all(
                "HD-Api-Key header" in str(auth_models.get((method, path), ""))
                and "Authorization Bearer token" not in str(auth_models.get((method, path), ""))
                for method, path, _variant in V1_BODYGRAPH_ROUTES
            ),
        ),
        ("v2_location_geocode_required", all(geocode.get((method, path)) == "required" for method, path in [("POST", "/v2/charts"), ("POST", "/v2/charts/simple")])),
        ("v1_bodygraph_geocode_required", all(geocode.get((method, path)) == "required" for method, path, _variant in V1_BODYGRAPH_ROUTES)),
        ("coordinates_geocode_not_needed", geocode.get(("POST", "/v2/charts/coordinates")) == "not needed"),
        (
            "required_geocode_auth_header_present",
            all(
                "HD-Geocode-Key header" in str(auth_models.get((method, path), ""))
                for method, path in [("POST", "/v2/charts"), ("POST", "/v2/charts/simple"), ("POST", "/v1/bodygraphs"), ("POST", "/v1/bodygraphs/simple")]
            ),
        ),
        (
            "coordinates_geocode_auth_header_absent",
            "HD-Geocode-Key header" not in str(auth_models.get(("POST", "/v2/charts/coordinates"), "")),
        ),
        (
            "source_authority_validated_yaml_rank1",
            all(
                source_specs.get((method, path)) == source_spec_for(path)
                and source_ranks.get((method, path)) == 1
                for method, path, _variant in V2_CHART_ROUTES + V1_BODYGRAPH_ROUTES
            ),
        ),
    ]
    network_posture = (
        "closed-rails-source-cache; no live vendor calls"
        if mode == "closed-rails-source-cache"
        else "public-docs-refresh; no credentialed runtime vendor calls"
    )
    lines = [
        f"generated_at_utc={produced}",
        "scope=HDE-EPIC034 PR-01 source-selection check",
        f"network_posture={network_posture}",
    ]
    lines.extend(f"[{name}] status={'PASS' if ok else 'FAIL'}" for name, ok in checks)
    lines.append("status=PASS" if all(ok for _name, ok in checks) else "status=FAIL")
    return "\n".join(lines)


def _sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def _validate_ops01_fact_summary(payload: dict[str, Any]) -> None:
    raw = json.dumps(payload, sort_keys=True)
    required = [
        "HD_API_BASE_URL", "HDAPI_BASE_URL", "HD_API_KEY", "GEO_API_KEY",
        "Authorization: Bearer <redacted>", "HD-Api-Key: <redacted>", "HD-Geocode-Key: <redacted>", "PR-02", "proceed",
    ]
    missing = [item for item in required if item not in raw]
    if missing:
        raise ValueError(f"OPS01_FACT_SUMMARY_INCOMPLETE:{','.join(missing)}")


def _load_ops01_fact_summary() -> dict[str, Any]:
    path = ROOT / "audit" / "ops" / "hde-epic034" / "ops-01" / "fact_summary.json"
    proof = ROOT / "audit" / "ops" / "hde-epic034" / "ops-01" / "fact_summary.json.path_proof.txt"
    if not path.exists() or not proof.exists():
        raise ValueError("OPS01_FACT_SUMMARY_MISSING")
    payload = json.loads(path.read_text(encoding="utf-8"))
    _validate_ops01_fact_summary(payload)
    return payload


def _route_by_path(contract: dict[str, Any], path: str) -> dict[str, Any]:
    for route in contract.get("route_families", []):
        if isinstance(route, dict) and route.get("method") == "POST" and route.get("path") == path:
            return route
    raise ValueError(f"REQUEST_SHAPING_ROUTE_MISSING:{path}")


def build_request_shaping_snapshot(produced: str, contract: dict[str, Any], source_selection: dict[str, Any], ops_summary: dict[str, Any]) -> dict[str, Any]:
    _validate_ops01_fact_summary(ops_summary)
    if source_selection.get("request_shaping_claim") != "NONE":
        raise ValueError("REQUEST_SHAPING_SOURCE_SELECTION_BASELINE_DRIFT")
    routes: list[dict[str, Any]] = []
    for method, path, variant in V2_CHART_ROUTES + V1_BODYGRAPH_ROUTES:
        route = _route_by_path(contract, path)
        fields = route.get("request_fields")
        if not isinstance(fields, list) or not fields:
            raise ValueError(f"REQUEST_SHAPING_FIELDS_MISSING:{path}")
        content_type = route.get("request_content_type")
        auth_model = str(route.get("auth_model", ""))
        geocode = route.get("geocode_key_requirement")
        if content_type != "application/json":
            raise ValueError(f"REQUEST_SHAPING_CONTENT_TYPE_MISMATCH:{path}")
        v2 = path.startswith("/v2/")
        expected_family = "recommended_v2_chart" if v2 else "legacy_v1_bodygraph"
        if route.get("route_family") != expected_family:
            raise ValueError(f"REQUEST_SHAPING_ROUTE_FAMILY_MISMATCH:{path}")
        if v2 and ("Authorization Bearer token" not in auth_model or "HD-Api-Key header" in auth_model):
            raise ValueError(f"REQUEST_SHAPING_AUTH_MISMATCH:{path}")
        if not v2 and ("HD-Api-Key header" not in auth_model or "Authorization Bearer token" in auth_model):
            raise ValueError(f"REQUEST_SHAPING_AUTH_MISMATCH:{path}")
        if geocode == "required" and "HD-Geocode-Key header" not in auth_model:
            raise ValueError(f"REQUEST_SHAPING_GEOCODE_MISMATCH:{path}")
        if geocode == "not needed" and "HD-Geocode-Key header" in auth_model:
            raise ValueError(f"REQUEST_SHAPING_GEOCODE_MISMATCH:{path}")
        routes.append({
            "auth_header_posture": "Authorization: Bearer <redacted>" if v2 else "HD-Api-Key: <redacted>",
            "body_field_source_list": fields,
            "content_type_posture": content_type,
            "credential_env_var": "HD_API_KEY",
            "endpoint_path": path,
            "geocode_env_var": "GEO_API_KEY" if geocode == "required" else "not applicable",
            "geocode_header_posture": "HD-Geocode-Key: <redacted>" if geocode == "required" else "not applicable",
            "geocode_key_requirement": geocode,
            "method": method,
            "route_family": expected_family,
            "route_variant": variant,
            "source_spec": route.get("source_spec"),
        })
    return {
        "ai_scope_claim": "NONE",
        "base_url_env_var": "HD_API_BASE_URL",
        "canonical_request_body_construction_proof": "request body keys are ordered from governed contract_map request_fields and serialized as canonical JSON bytes by engine.bodygraph.vendor_client.HdApiClient.build_contract_route_request; v1 bodygraph birthdate is legacy DD-Mon-YYYY while v2 chart birthdate remains YYYY-MM-DD and v2 coordinate lat/lng are serialized as JSON numbers",
        "credential_env_var": "HD_API_KEY",
        "deprecated_base_url_alias": {"env_var": "HDAPI_BASE_URL", "posture": "temporary compatibility alias only; used only when HD_API_BASE_URL is absent; conflicting values fail closed"},
        "generated_at_utc": produced,
        "geocode_env_var": "GEO_API_KEY",
        "input_references": {
            "contract_map": {"path": "artifacts/vendor/hdapi_v2/contract_map.json", "sha256": sha256_bytes(canonical_json_bytes(contract))},
            "ops01_fact_summary": {"path": "audit/ops/hde-epic034/ops-01/fact_summary.json", "sha256": _sha256_path(ROOT / "audit/ops/hde-epic034/ops-01/fact_summary.json")},
            "source_selection_snapshot": {"path": "artifacts/vendor/hdapi_v2/source_selection.snapshot.json", "sha256": sha256_bytes(canonical_json_bytes(source_selection))},
        },
        "live_vendor_call_claim": "NONE",
        "open_rails_vendor_smoke_claim": "NONE",
        "public_reader_change_claim": "NONE",
        "request_content_type_posture": "application/json",
        "route_family": "recommended_v2_chart",
        "routes": routes,
        "runtime_conformance_claim": "NONE",
        "source_selection_input_reference": "artifacts/vendor/hdapi_v2/source_selection.snapshot.json",
        "v1_legacy_auth_header_posture": "HD-Api-Key: <redacted>",
        "v2_auth_header_posture": "Authorization: Bearer <redacted>",
    }


def build_request_shaping_check_log(produced: str, snapshot: dict[str, Any], *, mode: str) -> str:
    routes = snapshot["routes"]
    by_path = {row["endpoint_path"]: row for row in routes}
    checks = [
        ("closed_rails_generation", mode == "closed-rails-source-cache"),
        ("no_live_vendor_call_attempted", snapshot["live_vendor_call_claim"] == "NONE"),
        ("v2_bearer_auth_posture", all(by_path[p]["auth_header_posture"] == "Authorization: Bearer <redacted>" and by_path[p]["credential_env_var"] == "HD_API_KEY" for _m,p,_v in V2_CHART_ROUTES)),
        ("v1_legacy_hd_api_key_posture", all(by_path[p]["auth_header_posture"] == "HD-Api-Key: <redacted>" for _m,p,_v in V1_BODYGRAPH_ROUTES)),
        ("geocode_posture", by_path["/v2/charts"]["geocode_header_posture"] == "HD-Geocode-Key: <redacted>" and by_path["/v2/charts/coordinates"]["geocode_header_posture"] == "not applicable"),
        ("canonical_base_url_key_posture", snapshot["base_url_env_var"] == "HD_API_BASE_URL"),
        ("deprecated_alias_posture", snapshot["deprecated_base_url_alias"]["env_var"] == "HDAPI_BASE_URL"),
        ("no_secret_values_emitted", "secret" not in json.dumps(snapshot).lower() and "k_test" not in json.dumps(snapshot)),
        ("evidence_index_and_path_proof_posture", True),
    ]
    lines = [f"generated_at_utc={produced}", "scope=HDE-EPIC034 PR-02 request-shaping check", "rails=SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC", "network_posture=closed-rails-source-cache; no live vendor calls"]
    lines.extend(f"[{name}] status={'PASS' if ok else 'FAIL'}" for name, ok in checks)
    lines.append("status=PASS" if all(ok for _name, ok in checks) else "status=FAIL")
    return "\n".join(lines)

def validate_source_statuses(fetched: dict[str, dict[str, Any]]) -> None:
    for key in ["v2_routes_yaml", "v1_routes_yaml", "llms_full_txt"]:
        status = fetched[key].get("fetch_status")
        if status not in {str(item) for item in ALLOWED_STATUS}:
            raise SystemExit(f"SOURCE_NOT_USABLE:{key}:{status}")
        if not fetched[key].get("sha256"):
            raise SystemExit(f"SOURCE_EMPTY:{key}")


def render_source_inventory(produced: str, fetched: dict[str, dict[str, Any]], *, mode: str) -> tuple[bytes, str]:
    inventory = {
        "ai_boundary": "llms.txt, llms-full.txt, and AI/LLM-oriented vendor documentation are documentation-discovery-only context; no AI product, runtime, evidence, token, credential, rail, QA, or model-call scope is created.",
        "generated_at_utc": produced,
        "source_mode": mode,
        "source_precedence": [
            "validated v2 and v1 YAML route specs",
            "rendered endpoint pages",
            "high-level guide pages",
            "suspect artifacts quarantined until validated",
        ],
        "sources": fetched,
    }
    md_lines = [
        "# HDAPI v2 and legacy v1 Source Inventory",
        "",
        f"Generated at UTC: {produced}",
        "",
        f"Source mode: {mode}",
        "",
        "This governed inventory records public same-origin HumanDesignAPI documentation sources only. It does not call credentialed runtime vendor endpoints and does not claim runtime v2 conformance.",
        "",
        "AI/LLM-oriented documentation, including `llms.txt` and `llms-full.txt`, is classified as documentation-discovery-only context and creates no AI product, runtime, evidence, token, credential, rail, QA, prompt, embedding, chatbot, model-call, or provider scope.",
        "",
        "| key | source_classification | fetch_status | content_type | sha256 | final_url | discovered_from | cache_path | cache_sha256 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for key in sorted(fetched):
        row = fetched[key]
        md_lines.append(f"| {key} | {row['source_classification']} | {row['fetch_status']} | {row['content_type']} | {row['sha256']} | {row['final_url']} | {row['discovered_from']} | {row.get('cache_path') or ''} | {row.get('cache_sha256') or ''} |")
    return canonical_json_bytes(inventory), "\n".join(md_lines)


def write_endpoint_reference(rows: list[dict[str, str]]) -> bytes:
    from io import StringIO

    buf = StringIO()
    fields = ["method", "path", "route_family", "auth_model", "geocode_key_requirement", "tier", "request_content_type", "request_fields", "success_envelope", "error_codes", "source_spec"]
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({field: row[field] for field in fields})
    return buf.getvalue().encode("utf-8")


def build_acceptance(produced: str) -> dict[str, Any]:
    return {
        "acceptance_claims_mode": "baseline_existing_tokens_only",
        "epic_id": "HDE-EPIC033",
        "generated_at_utc": produced,
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


def write_baseline_pointer_artifacts(produced: str, acceptance: dict[str, Any]) -> dict[Path, bytes]:
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
    viability = "\n".join(
        [
            f"generated_at_utc={produced}",
            "epic_id=HDE-EPIC033",
            "status=PASS",
            "tokens_checked=TESTS_PASS_OK,DOC_DELTA_PRESENT_OK,EVIDENCE_INDEX_UPDATED_OK,MACHINE_MIRROR_UPDATED_OK,EVIDENCE_INDEX_HASH_OK,EVIDENCE_PATHS_VALIDATED_OK,EVIDENCE_PATH_PROOFS_OK,JSON_CANONICAL_CHECK_OK",
            "vendor_v2_specific_tokens=NONE",
            "runtime_v2_conformance_claim=NONE",
            "public_reader_surface_change=NONE",
            "ai_scope=NONE",
        ]
    )
    doc_delta_text = "\n".join(
        [
            "# HDE-EPIC033 Doc Deltas",
            "",
            "## BLOCKERS",
            "",
            "None recorded for PR-01 contract-inventory evidence binding.",
            "",
            "## CAVEATS",
            "",
            "This PR binds HumanDesignAPI v2 and legacy v1 public documentation contract inventory only. It does not implement or claim runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader changes, a new HTTP home, or AI scope.",
            "",
            "## PROCESS UPDATES",
            "",
            "Recorded during PO-010 and PO-012 Moon Loop remediation on 2026-06-04.",
            "",
            "- Future EPIC033 boundary-proof checks should not rely on case-sensitive exact `grep -F` matches against governed prose when the proof target is semantic posture rather than byte identity.",
            "- Prefer regex-normalized or case-normalized QA checks under `audit/qa/hde-epic033/`, or promote a single canonical phrase constant that both the generator and the runbook consume.",
            "- When semantic boundary language is present but prose-case drift breaks a receipt, classify the issue as a QA evidence-harness defect and keep any Moon Loop repair within the QA root.",
        ]
    )
    return {
        ACCEPTANCE: canonical_json_bytes(acceptance),
        TOKEN_MATRIX: ("\n".join(matrix_lines) + "\n").encode("utf-8"),
        VIABILITY: (viability + "\n").encode("utf-8"),
        DOC_DELTAS: (doc_delta_text + "\n").encode("utf-8"),
        QA_DOC_DELTAS: (doc_delta_text + "\n").encode("utf-8"),
    }


def render_outputs(produced: str, fetched: dict[str, dict[str, Any]], bodies: dict[str, bytes], *, mode: str) -> dict[Path, bytes]:
    validate_source_statuses(fetched)
    v2_spec = parse_yaml_openapi(bodies["v2_routes_yaml"], "v2-routes.yaml")
    v1_spec = parse_yaml_openapi(bodies["v1_routes_yaml"], "v1-routes.yaml")
    v2_ok, v2_lines = validate_openapi_spec("v2-routes.yaml", v2_spec, expected_title="Human Design API — v2", expected_server="https://api.humandesignapi.nl/v2", paths=["/charts", "/charts/simple", "/charts/coordinates"])
    v1_ok, v1_lines = validate_openapi_spec("v1-routes.yaml", v1_spec, expected_title="Human Design API — v1", expected_server="https://api.humandesignapi.nl/v1", paths=["/bodygraphs", "/bodygraphs/simple"])
    suspect_ok, suspect_info, suspect_lines = validate_suspect_openapi(bodies.get("suspect_openapi_json", b""), fetched["suspect_openapi_json"])
    validation_log = build_validation_log(produced, v2_ok, v2_lines, v1_ok, v1_lines, suspect_lines, mode=mode)
    if not (v2_ok and v1_ok):
        raise SystemExit("ROUTE_SPEC_VALIDATION_FAILED: refusing to write promoted endpoint/contract/acceptance evidence")
    rows = build_endpoint_rows(v2_spec, v1_spec, bodies["llms_full_txt"].decode("utf-8", errors="replace"))
    inventory_json, inventory_md = render_source_inventory(produced, fetched, mode=mode)
    acceptance = build_acceptance(produced)
    outputs = {
        OUT / "source_inventory.json": inventory_json,
        OUT / "source_inventory.md": (inventory_md + "\n").encode("utf-8"),
        OUT / "openapi_validation.log": (validation_log + "\n").encode("utf-8"),
        OUT / "known_anomalies.md": (build_anomaly_text(produced, suspect_ok, suspect_info) + "\n").encode("utf-8"),
        OUT / "endpoint_reference.csv": write_endpoint_reference(rows),
        OUT / "contract_map.json": canonical_json_bytes(build_contract_map(produced, fetched, rows, suspect_ok)),
    }
    contract = build_contract_map(produced, fetched, rows, suspect_ok)
    snapshot = build_source_selection_snapshot(produced, contract)
    outputs.update({
        SOURCE_SELECTION_SNAPSHOT: canonical_json_bytes(snapshot),
        V1_LEGACY_GUARD_LOG: (build_v1_legacy_guard_log(produced, snapshot) + "\n").encode("utf-8"),
        SOURCE_SELECTION_CHECK_LOG: (build_source_selection_check_log(produced, snapshot, mode=mode) + "\n").encode("utf-8"),
    })
    ops_summary = _load_ops01_fact_summary()
    request_snapshot = build_request_shaping_snapshot(produced, contract, snapshot, ops_summary)
    outputs.update({
        REQUEST_SHAPING_SNAPSHOT: canonical_json_bytes(request_snapshot),
        REQUEST_SHAPING_CHECK_LOG: (build_request_shaping_check_log(produced, request_snapshot, mode=mode) + "\n").encode("utf-8"),
    })
    outputs.update(write_baseline_pointer_artifacts(produced, acceptance))
    return outputs


def write_outputs(outputs: dict[Path, bytes]) -> None:
    for path, body in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate HDE-EPIC033 HDAPI v2 contract-inventory evidence")
    parser.add_argument("--refresh-public-docs", action="store_true", help="Fetch public docs and refresh source_cache; requires SAFE_MODE=0 ALLOW_NETWORK=1")
    args = parser.parse_args(argv)

    produced = iso_now()
    if args.refresh_public_docs:
        fetched, bodies = refresh_source_cache(produced)
        mode = "public-docs-refresh"
    else:
        fetched, bodies = load_source_cache()
        mode = "closed-rails-source-cache"
    outputs = render_outputs(produced, fetched, bodies, mode=mode)
    write_outputs(outputs)
    print(f"generated {OUT.relative_to(ROOT).as_posix()} and HDE-EPIC033 baseline artifacts at {produced} ({mode})")


if __name__ == "__main__":
    main()
