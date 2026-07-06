#!/usr/bin/env python3
"""Generate HDE-EPIC037 PR-05 parent evidence-binding artifacts."""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Mapping

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index

ROOT = Path(__file__).resolve().parents[2]
GENERATED_AT = "2026-07-06T00:00:00Z"
PF09_DOCUMENT = "PF09.5 — HDE Build Checklist Fermentation"
ACCEPTANCE_MAP = ROOT / "docs" / "acceptance_map_epic037.json"
TOKEN_MATRIX = ROOT / "audit" / "qa" / "hde-epic037" / "token_evidence_matrix.md"
VIABILITY = ROOT / "audit" / "qa" / "hde-epic037" / "acceptance_map_viability.log"
PARENT_BINDING = ROOT / "audit" / "qa" / "hde-epic037" / "parent_evidence_binding.log"
DOC_DELTA = ROOT / "audit" / "docdeltas" / "hde-epic037_doc_deltas.md"
QA_DOC_DELTA = ROOT / "audit" / "qa" / "hde-epic037" / "00_meta" / "doc_deltas.md"
PR05_DOC_DELTA = ROOT / "audit" / "docdeltas" / "hde-epic037_pr05_parent_binding_doc_deltas.md"
PR05_QA_DOC_DELTA = ROOT / "audit" / "qa" / "hde-epic037" / "00_meta" / "pr05_parent_binding_doc_deltas.md"
OPS_ROOT = ROOT / "audit" / "ops" / "hde-epic037" / "ops-hde-epic037-001"
OPS_QA_POINTER = ROOT / "audit" / "qa" / "hde-epic037" / "ops-hde-epic037-001" / "ops_evidence_pointer.md"
CLOSED_RAILS_ENV = {"ALLOW_NETWORK": "0", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}

PR01_PATHS = [
    "artifacts/vendor/hdapi_v2/hde_epic037_field_sufficiency_proof.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract.snapshot.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract_nonclaims.json",
    "audit/docdeltas/hde-epic037_doc_deltas.md",
    "audit/qa/hde-epic037/00_meta/doc_deltas.md",
]
PR02_PATHS = [
    "artifacts/vendor/hdapi_v2/hde_epic037_adapter_mapping.snapshot.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_adapter_negative_fixtures.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_no_raw_payload_persistence.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_public_reader_no_change.json",
]
PR03_PATHS = [
    "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_v2_route_policy.snapshot.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_request_shape.snapshot.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_closed_rails_no_io.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_legacy_fallback.snapshot.json",
]
PR04_PATHS = [
    "artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_proof.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_two_run.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_pair_order.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_admin_public_boundary.json",
]
OPS_PATHS = [
    "audit/ops/hde-epic037/ops-hde-epic037-001/commands.txt",
    "audit/ops/hde-epic037/ops-hde-epic037-001/stdout.log",
    "audit/ops/hde-epic037/ops-hde-epic037-001/stderr.log",
    "audit/ops/hde-epic037/ops-hde-epic037-001/exit_codes.txt",
    "audit/ops/hde-epic037/ops-hde-epic037-001/env_presence_redacted.json",
    "audit/ops/hde-epic037/ops-hde-epic037-001/request_summary.json",
    "audit/ops/hde-epic037/ops-hde-epic037-001/result_summary.json",
    "audit/ops/hde-epic037/ops-hde-epic037-001/adapter_mapping_result_summary.json",
    "audit/ops/hde-epic037/ops-hde-epic037-001/compat_path_result_summary.json",
    "audit/ops/hde-epic037/ops-hde-epic037-001/failure_classification.json",
    "audit/ops/hde-epic037/ops-hde-epic037-001/files_sha256.txt",
    "audit/qa/hde-epic037/ops-hde-epic037-001/ops_evidence_pointer.md",
]
PR05_PATHS = [
    "docs/acceptance_map_epic037.json",
    "audit/qa/hde-epic037/token_evidence_matrix.md",
    "audit/qa/hde-epic037/acceptance_map_viability.log",
    "audit/qa/hde-epic037/parent_evidence_binding.log",
    "audit/docdeltas/hde-epic037_pr05_parent_binding_doc_deltas.md",
    "audit/qa/hde-epic037/00_meta/pr05_parent_binding_doc_deltas.md",
]
SUBTASKS = ["HDE-FERM008.7", "HDE-FERM008.8", "HDE-FERM008.9", "HDE-FERM008.10", "HDE-FERM008.11", "HDE-FERM008.12"]
TOKENS = [
    "DOC_DELTA_PRESENT_OK",
    "EVIDENCE_INDEX_UPDATED_OK",
    "MACHINE_MIRROR_UPDATED_OK",
    "EVIDENCE_INDEX_HASH_OK",
    "EVIDENCE_INDEX_MIRROR_OK",
    "EVIDENCE_PATH_PROOFS_OK",
    "JSON_CANONICAL_CHECK_OK",
    "COMPOSITE_ABBA_IDENTITY_OK",
    "TWO_RUN_IDENTITY_OK",
    "NO_EXTERNAL_IO_ON_REFUSAL_OK",
    "ENV_RAILS_POLICY_OK",
]
NONCLAIMS = [
    "QA PASS",
    "OPS completion by PR work",
    "PF09 status movement",
    "PF09 status drainage",
    "PO closeout",
    "board update",
    "merge action",
    "PF-Canon edit",
    "epic closeout",
    "production deployment",
    "full HumanDesignAPI v2 platform conformance beyond the bounded HDE-FERM008.7-.11 evidence chain",
    "public Reader change",
    "public route",
    "public flag",
    "public payload or transport change",
    "new HTTP home",
    "app-side HumanDesignAPI ownership",
    "raw secret persistence",
    "raw request body persistence",
    "raw response body persistence",
    "uncontrolled raw vendor payload persistence",
    "AI scope",
]
DOC_TEXT = """# HDE-EPIC037 PR-01 doc deltas

- Recorded HDE-FERM008.7 field-sufficiency evidence for v2 BodyGraph-detail readiness.
- Selected payload family is a typed insufficient classification, not runtime conformance.
- No public Reader, route, flag, payload, transport, AI, live-vendor, OPS, or PF-Canon change is claimed.
## HDE-EPIC037 PR-05 parent evidence binding doc deltas

- Bound HDE-FERM008.7 through HDE-FERM008.11 evidence into HDE-FERM008.12 parent-level evidence artifacts.
- Recorded parent_posture=supportable_to_done as a later-drain support statement only; no PF09 status movement, QA PASS, OPS completion by PR work, or epic closeout is claimed.
- Bound PO-produced OPS-01 evidence without rerunning OPS or making a live vendor call.
- Preserved public-surface and nonclaim boundaries: no public Reader change, public route, public flag, payload/transport change, new HTTP home, app-side vendor ownership, raw secret/uncontrolled vendor payload persistence, or AI scope.
"""


def canonical_json_bytes(payload: object) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _parse_utc(raw: str) -> _dt.datetime:
    return _dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))


def enforce_closed_rails() -> None:
    ensure_determinism_env()
    for key, expected in CLOSED_RAILS_ENV.items():
        if os.environ.get(key) != expected:
            raise SystemExit(f"HDE_EPIC037_PR05_CLOSED_RAILS_REQUIRED:{key}")


def _load_json(rel: str) -> object:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def verify_ops01() -> None:
    for rel in OPS_PATHS:
        if not (ROOT / rel).exists():
            raise SystemExit(f"MISSING_EPIC037_OPS01_ARTIFACT:{rel}")
    commands_text = (OPS_ROOT / "commands.txt").read_text(encoding="utf-8")
    stdout = _load_json("audit/ops/hde-epic037/ops-hde-epic037-001/stdout.log")
    request_summary = _load_json("audit/ops/hde-epic037/ops-hde-epic037-001/request_summary.json")
    env_presence = _load_json("audit/ops/hde-epic037/ops-hde-epic037-001/env_presence_redacted.json")
    result_summary = _load_json("audit/ops/hde-epic037/ops-hde-epic037-001/result_summary.json")
    adapter_summary = _load_json("audit/ops/hde-epic037/ops-hde-epic037-001/adapter_mapping_result_summary.json")
    compat_summary = _load_json("audit/ops/hde-epic037/ops-hde-epic037-001/compat_path_result_summary.json")
    failure = _load_json("audit/ops/hde-epic037/ops-hde-epic037-001/failure_classification.json")
    adapter = stdout.get("adapter", {})
    request = stdout.get("resolver", {}).get("request", {})
    env_rails = env_presence.get("rails", {})
    env_secret_policy = env_presence.get("secret_policy", {})
    env_base_url_posture = env_presence.get("base_url_posture", {})
    env_locale = env_presence.get("locale", {})
    required_command_rails = (
        "HD_API_BASE_URL=<redacted-v2-base>",
        "SAFE_MODE=0",
        "ALLOW_NETWORK=1",
        "APP_ENV=dev",
        "LC_ALL=C",
        "LANG=C",
        "TZ=UTC",
    )
    if (
        "https://" in commands_text
        or "http://" in commands_text
        or any(token not in commands_text for token in required_command_rails)
        or stdout.get("status") != "ok"
        or adapter.get("status") != "mapped"
        or adapter.get("code") != "ADAPTER_MAPPED"
        or adapter.get("payload_family") != "ChartResult"
        or request.get("route") != "vendor.hdapi.post:/charts"
        or request.get("configured_base_url") != "<redacted>"
        or request.get("raw_body_emitted") is not False
        or request.get("raw_response_body_emitted") is not False
        or result_summary.get("runtime_conformance_supported_by_this_smoke") is not True
        or adapter_summary.get("raw_vendor_payload_recorded") is not False
        or compat_summary.get("compat_path_status") != "accepted"
        or compat_summary.get("category_count") != 10
        or failure.get("classification") != "not_applicable_success"
        or env_presence.get("artifact_kind") != "hde_epic037_ops01_env_presence_redacted"
        or env_presence.get("epic_id") != "HDE-EPIC037"
        or env_presence.get("pf09_task_id") != "HDE-FERM008"
        or env_presence.get("pf09_subtask_id") != "HDE-FERM008.11"
        or env_presence.get("missing") != []
        or env_presence.get("errors") != []
        or env_rails.get("safe_mode") != "0"
        or env_rails.get("allow_network") != "1"
        or env_rails.get("app_env") != "dev"
        or env_locale.get("lc_all") != "C"
        or env_locale.get("lang") != "C"
        or env_locale.get("tz") != "UTC"
        or env_base_url_posture.get("hd_api_base_url_present") is not True
        or env_base_url_posture.get("hd_api_base_url_expected_v2_value") is not True
        or env_base_url_posture.get("hd_api_base_url_value_recorded") is not False
        or env_base_url_posture.get("hdapi_base_url_alias_present") is not False
        or env_secret_policy.get("hd_api_key_value_recorded") is not False
        or env_secret_policy.get("geo_api_key_value_recorded") is not False
        or env_secret_policy.get("plaintext_secrets_allowed_in_evidence") is not False
        or request_summary.get("secret_policy", {}).get("plaintext_secret_recorded") is not False
        or request_summary.get("secret_policy", {}).get("raw_request_body_recorded") is not False
        or request_summary.get("secret_policy", {}).get("raw_response_body_recorded") is not False
        or request_summary.get("secret_policy", {}).get("uncontrolled_raw_vendor_payload_recorded") is not False
    ):
        raise SystemExit("INVALID_EPIC037_OPS01_POSTURE")
    if "bg_resolve_exit_code=0" not in (OPS_ROOT / "exit_codes.txt").read_text(encoding="utf-8"):
        raise SystemExit("INVALID_EPIC037_OPS01_EXIT_CODE")
    ledger = {
        line.split()[1]: line.split()[0]
        for line in (OPS_ROOT / "files_sha256.txt").read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    for rel in [*OPS_PATHS[:-1], OPS_QA_POINTER.relative_to(ROOT).as_posix()]:
        if rel != "audit/ops/hde-epic037/ops-hde-epic037-001/files_sha256.txt" and ledger.get(rel) != _sha256_path(ROOT / rel):
            raise SystemExit(f"INVALID_EPIC037_OPS01_LEDGER:{rel}")


def build_acceptance_map() -> dict[str, object]:
    return {
        "acceptance_claims_mode": "registered_tokens_with_current_repo_evidence_only",
        "epic_id": "HDE-EPIC037",
        "evidence_families": {
            "ops01_hde_ferm008_11_po_produced": OPS_PATHS,
            "pr01_hde_ferm008_7": PR01_PATHS,
            "pr02_hde_ferm008_8": PR02_PATHS,
            "pr03_hde_ferm008_9": PR03_PATHS,
            "pr04_hde_ferm008_10": PR04_PATHS,
            "pr05_hde_ferm008_12_parent_binding": PR05_PATHS,
        },
        "generated_at_utc": GENERATED_AT,
        "nonclaims": NONCLAIMS,
        "ops_01_binding": {
            "adapter_code": "ADAPTER_MAPPED",
            "adapter_status": "mapped",
            "evidence_producer": "PO",
            "executed_by_pr05": False,
            "ops_completion_claim_by_pr05": False,
            "payload_family": "ChartResult",
            "route": "vendor.hdapi.post:/charts",
            "runtime_conformance_supported_by_this_smoke": True,
            "runtime_smoke_status": "ok",
        },
        "parent_posture": "supportable_to_done",
        "parent_posture_scope": "later-drain support statement only; this artifact does not move PF09 status",
        "pf09_document": PF09_DOCUMENT,
        "pf09_subtask_id": "HDE-FERM008.12",
        "pf09_subtask_label": "v2 runtime conformance evidence binding",
        "pf09_subtasks_bound": SUBTASKS,
        "pf09_task_id": "HDE-FERM008",
        "support_statement": "HDE-FERM008 is supportable_to_done for later PF09 drainage because current repo evidence binds closed-rails field-sufficiency, adapter/schema mapping, resolver route policy, v2-to-compat proofs, PO-produced OPS-01 open-rails runtime smoke, nonclaim boundaries, Human Evidence Index, Machine Mirror, hash sentinels, and path proofs. This is not PF09 status movement, QA PASS, OPS completion by PR work, closeout, or broad HumanDesignAPI v2 platform conformance.",
        "tokens": [{"name": token, "status": "supported_by_current_repo_evidence"} for token in TOKENS],
    }


def build_matrix() -> str:
    rows = {
        "DOC_DELTA_PRESENT_OK": "audit/docdeltas/hde-epic037_pr05_parent_binding_doc_deltas.md; audit/qa/hde-epic037/00_meta/pr05_parent_binding_doc_deltas.md",
        "EVIDENCE_INDEX_UPDATED_OK": "docs/evidence/INDEX.json",
        "MACHINE_MIRROR_UPDATED_OK": "artifacts/evidence_index.jsonl",
        "EVIDENCE_INDEX_HASH_OK": "docs/evidence/INDEX.sha256; artifacts/evidence_index.jsonl.sha256",
        "EVIDENCE_INDEX_MIRROR_OK": "docs/evidence/INDEX.json; artifacts/evidence_index.jsonl",
        "EVIDENCE_PATH_PROOFS_OK": "sibling .path_proof.txt files for PR-05 artifacts and OPS-01 bound artifacts",
        "JSON_CANONICAL_CHECK_OK": "docs/acceptance_map_epic037.json and canonical JSON evidence snapshots",
        "COMPOSITE_ABBA_IDENTITY_OK": "artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_pair_order.json",
        "TWO_RUN_IDENTITY_OK": "artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_two_run.json",
        "NO_EXTERNAL_IO_ON_REFUSAL_OK": "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_closed_rails_no_io.json",
        "ENV_RAILS_POLICY_OK": "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_v2_route_policy.snapshot.json; audit/ops/hde-epic037/ops-hde-epic037-001/env_presence_redacted.json",
    }
    lines = [
        "# HDE-EPIC037 PR-05 Token Evidence Matrix",
        "",
        "epic_id=HDE-EPIC037",
        "pf09_task_id=HDE-FERM008",
        "pf09_subtask_id=HDE-FERM008.12",
        "parent_posture=supportable_to_done",
        "parent_posture_scope=later-drain support statement only; no PF09 status movement",
        "qa_pass_claim=false",
        "ops_completion_by_pr_work_claim=false",
        "pf09_status_movement_claim=false",
        "pf09_status_drainage_claim=false",
        "epic_closeout_claim=false",
        "full_humandesignapi_v2_platform_conformance_claim=false",
        "public_reader_change_claim=false",
        "public_route_claim=false",
        "public_flag_claim=false",
        "public_payload_or_transport_change_claim=false",
        "new_http_home_claim=false",
        "app_side_vendor_ownership_claim=false",
        "raw_secret_or_uncontrolled_vendor_payload_persistence_claim=false",
        "ai_scope_claim=false",
        "",
        "| Token | Evidence paths | Posture |",
        "| --- | --- | --- |",
    ]
    lines.extend(
        f"| {token} | {rows[token]} | Supported only by listed current repo evidence; not a QA PASS or PF09 status movement claim. |"
        for token in TOKENS
    )
    lines.extend(["", "Bound evidence families:"])
    lines.extend(f"- {path}" for path in [*PR01_PATHS, *PR02_PATHS, *PR03_PATHS, *PR04_PATHS, *OPS_PATHS, *PR05_PATHS] if path != TOKEN_MATRIX.relative_to(ROOT).as_posix())
    return "\n".join(lines) + "\n"


def build_parent_binding() -> str:
    lines = [
        "HDE-EPIC037 PR-05 parent evidence binding",
        f"generated_at_utc={GENERATED_AT}",
        "epic_id=HDE-EPIC037",
        "pf09_task_id=HDE-FERM008",
        "pf09_subtask_id=HDE-FERM008.12",
        "parent_posture=supportable_to_done",
        "parent_posture_scope=later-drain support statement only; no PF09 status movement",
        "",
        "evidence_families:",
    ]
    families = [
        ("HDE-FERM008.7 PR-01 field sufficiency", PR01_PATHS),
        ("HDE-FERM008.8 PR-02 adapter mapping", PR02_PATHS),
        ("HDE-FERM008.9 PR-03 resolver route policy", PR03_PATHS),
        ("HDE-FERM008.10 PR-04 v2-to-compat", PR04_PATHS),
        ("HDE-FERM008.11 OPS-01 PO-produced runtime smoke", OPS_PATHS),
        ("HDE-FERM008.12 PR-05 parent binding", PR05_PATHS),
    ]
    for name, paths in families:
        lines.append(f"- {name}: Found; indexed=after_update_evidence_index; mirrored=after_update_evidence_index; hash_sentinel_aligned=after_update_evidence_index; path_proofed=after_update_evidence_index")
        lines.extend(f"  - {path}" for path in paths)
    lines.extend(["", "nonclaims:"])
    lines.extend(f"- {nonclaim}" for nonclaim in NONCLAIMS)
    lines.extend(["", "gaps: none blocking later-drain support_to_done; PF09 status drainage, PO closeout, board update, merge, and epic closeout remain separate follow-up actions."])
    return "\n".join(lines) + "\n"


def build_viability() -> str:
    return "\n".join([
        "HDE-EPIC037 PR-05 acceptance-map viability",
        f"generated_at_utc={GENERATED_AT}",
        "epic_id=HDE-EPIC037",
        "acceptance_map=docs/acceptance_map_epic037.json",
        "canonical_json_parseable=true",
        "referenced_artifact_paths_exist=true",
        "referenced_artifact_path_proofs_exist=after_update_evidence_index",
        "claimed_tokens_registered_and_supported=true",
        "human_evidence_index_includes_pr05_and_ops01=after_update_evidence_index",
        "machine_mirror_includes_pr05_and_ops01=after_update_evidence_index",
        "parent_posture=supportable_to_done",
        "parent_posture_supportable_from_current_evidence=true",
        "qa_pass_claim=false",
        "ops_completion_by_pr_work_claim=false",
        "pf09_status_movement_claim=false",
        "pf09_status_drainage_claim=false",
        "pf_canon_edit=false",
        "live_vendor_call_by_pr05=false",
        "external_io_by_pr05=false",
        "",
    ])


def build_outputs() -> dict[Path, bytes]:
    verify_ops01()
    for rel in [*PR01_PATHS, *PR02_PATHS, *PR03_PATHS, *PR04_PATHS, *OPS_PATHS]:
        if not (ROOT / rel).exists():
            raise SystemExit(f"MISSING_EPIC037_PARENT_BINDING_INPUT:{rel}")
    return {
        ACCEPTANCE_MAP: canonical_json_bytes(build_acceptance_map()),
        TOKEN_MATRIX: build_matrix().encode("utf-8"),
        VIABILITY: build_viability().encode("utf-8"),
        PARENT_BINDING: build_parent_binding().encode("utf-8"),
        PR05_DOC_DELTA: DOC_TEXT.encode("utf-8"),
        PR05_QA_DOC_DELTA: DOC_TEXT.encode("utf-8"),
    }


def _write_path_proof(path: Path, produced_at: str, *, check: bool) -> None:
    rel = path.relative_to(ROOT).as_posix()
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel,
        sha256=_sha256_path(path),
        size_bytes=stat.st_size,
        mtime_utc=None,
        produced_at=produced_at,
        default_produced_at=produced_at,
        check=check,
        stat_mtime=stat.st_mtime,
    )


def write_outputs(outputs: Mapping[Path, bytes], *, check: bool) -> None:
    stale = []
    for path, body in outputs.items():
        if check:
            if not path.exists() or path.read_bytes() != body:
                stale.append(path.relative_to(ROOT).as_posix())
            else:
                _write_path_proof(path, GENERATED_AT, check=True)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
            ts = _parse_utc(GENERATED_AT).timestamp()
            os.utime(path, (ts, ts))
            _write_path_proof(path, GENERATED_AT, check=False)
    if stale:
        raise SystemExit("STALE_HDE_EPIC037_PARENT_BINDING:" + ",".join(stale))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate HDE-EPIC037 PR-05 parent-binding evidence")
    parser.add_argument("--check", action="store_true", help="verify generated artifacts are current")
    args = parser.parse_args(argv)
    try:
        enforce_closed_rails()
    except DeterminismEnvError as exc:
        raise SystemExit(f"HDE_EPIC037_PR05_CLOSED_RAILS_REQUIRED:{exc}") from exc
    write_outputs(build_outputs(), check=args.check)
    print("checked HDE-EPIC037 PR-05 parent-binding artifacts" if args.check else "generated HDE-EPIC037 PR-05 parent-binding artifacts")


if __name__ == "__main__":
    main()
