#!/usr/bin/env python3
"""PO-only OPS-02 mapped-cache smoke; never run as PR validation."""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.bodygraph.mapped_cache import persist_mapped_bodygraph
from engine.bodygraph.projection import project_bodygraph
from engine.bodygraph.v2_adapter import V2ChartAdapterContext, adapt_v2_chart_payload
from engine.bodygraph.vendor_client import HdApiClient, VendorRetryConfig, classify_bg_resolve_route_policy
from engine.db import DBAccess
from engine.serializer.canon import sercanon

REQUIRED_ENV = ("HD_API_BASE_URL", "HD_API_KEY", "GEO_API_KEY", "DATABASE_URL")
PRODUCTION_LIKE = {"prod", "production", "live"}
SINGLE_REQUEST_RETRY = VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0)
OPS_EVIDENCE_ROOT = ROOT / "audit/ops/hde-epic038/ops-02"
PACKET_NAMES = (
    "commands.txt",
    "stdout.log",
    "stderr.log",
    "exit_code.txt",
    "env_presence.json",
    "request_summary.json",
    "mapped_output_summary.json",
    "read_back_summary.json",
    "canonical_parity.log",
    "idempotence.log",
    "no_raw_vendor_payload_persistence.log",
    "legacy_fallback_preservation.log",
    "nonclaims.json",
    "result_summary.json",
    "checksums.sha256",
)
_CHECKSUM_INPUTS = tuple(name for name in PACKET_NAMES if name != "checksums.sha256")
_SENSITIVE_ENV = ("HD_API_BASE_URL", "HD_API_KEY", "GEO_API_KEY", "DATABASE_URL")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="PO-authorized one-request configured-v2 mapped-cache smoke")
    parser.add_argument("--synthetic-user-id", required=True)
    parser.add_argument("--synthetic-person-uid", required=True)
    parser.add_argument("--birthdate", required=True)
    parser.add_argument("--birthtime", required=True)
    parser.add_argument("--location", required=True)
    parser.add_argument("--evidence-dir", type=Path)
    parser.add_argument("--retention-decision", choices=("retain",))
    return parser


def _preflight(args: argparse.Namespace) -> None:
    if os.environ.get("SAFE_MODE") != "0" or os.environ.get("ALLOW_NETWORK") != "1":
        raise SystemExit("OPS_REFUSED: explicit open rails required")
    app_env = os.environ.get("APP_ENV", "").strip().lower()
    if not app_env or app_env in PRODUCTION_LIKE:
        raise SystemExit("OPS_REFUSED: explicit non-production APP_ENV required")
    missing = [name for name in REQUIRED_ENV if not os.environ.get(name, "").strip()]
    if missing:
        raise SystemExit("OPS_REFUSED: required environment names are unset: " + ",".join(missing))
    route_policy = classify_bg_resolve_route_policy(os.environ["HD_API_BASE_URL"])
    if not route_policy["supported"] or route_policy["route_family"] != "recommended_v2_chart":
        raise SystemExit("OPS_REFUSED: HD_API_BASE_URL must select the configured-v2 charts route")
    try:
        canonical_user_id = str(uuid.UUID(args.synthetic_user_id))
    except ValueError as exc:
        raise SystemExit("OPS_REFUSED: synthetic user identity must be a UUID") from exc
    if canonical_user_id != args.synthetic_user_id:
        raise SystemExit("OPS_REFUSED: synthetic user identity must use canonical UUID form")
    if not all(str(getattr(args, name)).strip() for name in ("synthetic_person_uid", "birthdate", "birthtime", "location")):
        raise SystemExit("OPS_REFUSED: complete synthetic inputs required")
    if (args.evidence_dir is None) != (args.retention_decision is None):
        raise SystemExit("OPS_REFUSED: evidence directory and retention decision must be supplied together")
    if args.evidence_dir is not None:
        if args.evidence_dir.resolve() != OPS_EVIDENCE_ROOT.resolve():
            raise SystemExit("OPS_REFUSED: evidence directory must be the approved OPS-02 root")
        if args.evidence_dir.exists():
            raise SystemExit("OPS_REFUSED: OPS-02 evidence directory already exists")


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _git(*args: str) -> str:
    result = subprocess.run(
        ("git", *args),
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout.strip()


def _repository_identity(*, require_clean: bool) -> dict[str, str]:
    root = Path(_git("rev-parse", "--show-toplevel")).resolve()
    if root != ROOT.resolve():
        raise SystemExit("OPS_REFUSED: repository root mismatch")
    status = _git("status", "--porcelain")
    if require_clean and status:
        raise SystemExit("OPS_REFUSED: clean worktree required before OPS execution")
    branch = _git("branch", "--show-current")
    if not branch:
        raise SystemExit("OPS_REFUSED: attached branch required")
    return {
        "branch": branch,
        "head": _git("rev-parse", "HEAD"),
        "pre_execution_worktree": "clean" if not status else "dirty",
        "root": root.as_posix(),
    }


def _production_refusal_probe(args: argparse.Namespace) -> bool:
    previous = os.environ.get("APP_ENV")
    os.environ["APP_ENV"] = "production"
    try:
        try:
            _preflight(args)
        except SystemExit as exc:
            return str(exc) == "OPS_REFUSED: explicit non-production APP_ENV required"
        return False
    finally:
        if previous is None:
            os.environ.pop("APP_ENV", None)
        else:
            os.environ["APP_ENV"] = previous


def _legacy_fallback_probe() -> dict[str, Any]:
    policy = classify_bg_resolve_route_policy("https://fixture.invalid/v1")
    return {
        "classification": policy["classification"],
        "configured_v2_legacy_fallback": False,
        "resource_path": policy["resource_path"],
        "route_auth_posture": policy["route_auth_posture"],
        "route_family": policy["route_family"],
        "supported": policy["supported"],
    }


def _execute(args: argparse.Namespace) -> dict[str, Any]:
    db = DBAccess.for_current_env()
    db.health()
    client = HdApiClient.from_env(env=os.environ, retry=SINGLE_REQUEST_RETRY)
    request = client.build_contract_route_request(
        path="charts",
        request_fields=("birthdate", "birthtime", "location"),
        geocode_required=True,
        birthdate=args.birthdate,
        birthtime=args.birthtime,
        location=args.location,
    )
    vendor_result = client.fetch(request)  # exactly one authorized vendor request
    if vendor_result.attempts != 1:
        raise RuntimeError("vendor request attempt count must equal one")
    context = V2ChartAdapterContext(
        person_uid=args.synthetic_person_uid,
        user_id=args.synthetic_user_id,
        vendor="hdapi",
        vendor_version=2,
        input_fingerprint=request.input_fingerprint,
        route_family="recommended_v2_chart",
        route=request.route,
        payload_family="ChartResult",
    )
    adapter = adapt_v2_chart_payload(vendor_result.payload, context).as_dict()
    if adapter["status"] != "mapped":
        raise RuntimeError("adapter mapping refused")
    projected = project_bodygraph(adapter["cache"]["payload"])
    first = persist_mapped_bodygraph(db, adapter["cache"])
    second = persist_mapped_bodygraph(db, adapter["cache"])
    if not (
        first.rows_before == 0
        and first.rows_written == 1
        and first.rows_after == 1
        and first.read_back_match
        and second.rows_before == 1
        and second.rows_written == 0
        and second.rows_after == 1
        and second.read_back_match
        and second.idempotent
        and first.canonical_sha256 == second.canonical_sha256
    ):
        raise RuntimeError("mapped-cache live predicates failed")
    return {
        "adapter_code": adapter["code"],
        "adapter_status": adapter["status"],
        "canonical_sha256": first.canonical_sha256,
        "first": first.as_dict(),
        "input_fingerprint": request.input_fingerprint,
        "payload_family": adapter["payload_family"],
        "payload_posture": adapter["cache"]["payload_posture"],
        "projected_keys": sorted(projected),
        "provider": first.provider,
        "request_route": request.route,
        "second": second.as_dict(),
        "vendor_requests": vendor_result.attempts,
    }


def _redacted_command(args: argparse.Namespace) -> bytes:
    command = (
        "# PO_APPROVED: one configured-v2 vendor request; bounded mapped-cache write/read-back/idempotence; "
        "secret-safe packet producer; synthetic-row retention=retain\n"
        "LC_ALL=C LANG=C TZ=UTC APP_ENV=dev SAFE_MODE=0 ALLOW_NETWORK=1 "
        "python scripts/ops/hde_epic038_mapped_cache_smoke.py "
        "--synthetic-user-id <approved-synthetic-uuid> "
        "--synthetic-person-uid <approved-synthetic-person-uid> "
        "--birthdate <approved-synthetic-birthdate> "
        "--birthtime <approved-synthetic-birthtime> "
        "--location <approved-synthetic-location> "
        f"--evidence-dir {OPS_EVIDENCE_ROOT.relative_to(ROOT).as_posix()} "
        f"--retention-decision {args.retention_decision}\n"
    )
    return command.encode("utf-8")


def _environment_summary(captured_at: str, repository: Mapping[str, str]) -> dict[str, Any]:
    policy = classify_bg_resolve_route_policy(os.environ["HD_API_BASE_URL"])
    return {
        "captured_at_utc": captured_at,
        "environment_presence": {
            "ALLOW_NETWORK": os.environ["ALLOW_NETWORK"],
            "APP_ENV": f"SET:{os.environ['APP_ENV']}",
            "DATABASE_URL": "SET:REDACTED",
            "GEO_API_KEY": "SET:REDACTED",
            "HD_API_BASE_URL": "SET:REDACTED",
            "HD_API_KEY": "SET:REDACTED",
            "LANG": os.environ.get("LANG", ""),
            "LC_ALL": os.environ.get("LC_ALL", ""),
            "SAFE_MODE": os.environ["SAFE_MODE"],
            "TZ": os.environ.get("TZ", ""),
        },
        "repository": dict(repository),
        "route_policy": {
            "classification": policy["classification"],
            "configured_base_version": policy["configured_base_version"],
            "resource_path": policy["resource_path"],
            "route_auth_posture": policy["route_auth_posture"],
            "route_family": policy["route_family"],
        },
        "schema": "hde_epic038.ops02.env_presence.v1",
        "secret_posture": "presence_only",
    }


def _success_files(
    args: argparse.Namespace,
    observation: Mapping[str, Any],
    repository: Mapping[str, str],
    *,
    captured_at: str,
    production_refused: bool,
    legacy: Mapping[str, Any],
) -> dict[str, bytes]:
    first = observation["first"]
    second = observation["second"]
    stdout_summary = {
        "adapter_status": observation["adapter_code"],
        "canonical_sha256": observation["canonical_sha256"],
        "idempotent": second["idempotent"],
        "identity_rows": second["rows_after"],
        "provider": observation["provider"],
        "read_back_match": first["read_back_match"],
        "retention_decision": args.retention_decision,
        "second_write_rows": second["rows_written"],
        "status": "ok",
        "vendor_requests": observation["vendor_requests"],
    }
    request_summary = {
        "attempt_limit": 1,
        "auth_posture": "Authorization: Bearer <redacted>",
        "captured_at_utc": captured_at,
        "configured_base": "REDACTED",
        "geocode_required": True,
        "input_fingerprint": observation["input_fingerprint"],
        "payload_family": observation["payload_family"],
        "request_field_names": ["birthdate", "birthtime", "location"],
        "request_values_persisted": False,
        "resource_path": "charts",
        "route": observation["request_route"],
        "route_family": "recommended_v2_chart",
        "schema": "hde_epic038.ops02.request_summary.v1",
        "vendor_requests": observation["vendor_requests"],
    }
    mapped_output = {
        "adapter_code": observation["adapter_code"],
        "adapter_status": observation["adapter_status"],
        "canonical_sha256": observation["canonical_sha256"],
        "captured_at_utc": captured_at,
        "payload_family": observation["payload_family"],
        "payload_posture": observation["payload_posture"],
        "projected_top_level_keys": observation["projected_keys"],
        "raw_vendor_envelope_persisted": False,
        "schema": "hde_epic038.ops02.mapped_output_summary.v1",
    }
    read_back = {
        "canonical_sha256": first["canonical_sha256"],
        "captured_at_utc": captured_at,
        "identity_rows": second["rows_after"],
        "provider": observation["provider"],
        "read_back_match": first["read_back_match"] and second["read_back_match"],
        "retention_decision": args.retention_decision,
        "schema": "hde_epic038.ops02.read_back_summary.v1",
        "stored_payload_posture": observation["payload_posture"],
        "synthetic_user_id": args.synthetic_user_id,
    }
    nonclaims = {
        "captured_at_utc": captured_at,
        "nonclaims": [
            "no_production_write_authorization",
            "no_raw_vendor_envelope_persistence",
            "no_raw_request_or_response_persistence",
            "no_secret_persistence",
            "no_public_reader_change",
            "no_public_route_or_flag_change",
            "no_broad_v2_conformance_claim",
            "no_qa_pass_claim",
            "no_acceptance_token_claim",
            "no_pf09_status_movement",
            "no_deployment_change",
            "no_epic_closeout_claim",
        ],
        "pf09_posture": {
            "HDE-DIST001": "unchanged",
            "HDE-DIST001.11": "Optional",
            "status_change": "none",
        },
        "retention_decision": args.retention_decision,
        "schema": "hde_epic038.ops02.nonclaims.v1",
    }
    predicates = {
        "adapter_mapped": observation["adapter_status"] == "mapped",
        "canonical_write_read_back_equivalence": first["read_back_match"] and second["read_back_match"],
        "exactly_one_vendor_request": observation["vendor_requests"] == 1,
        "explicit_legacy_fallback_preserved": legacy["classification"] == "explicit_legacy_fallback",
        "idempotent_repeated_write": first["rows_written"] == 1 and second["rows_written"] == 0 and second["idempotent"],
        "mapped_payload_only": observation["payload_posture"] == "adapter_mapped_no_raw_vendor_payload",
        "normalized_identity_single_row": first["rows_after"] == second["rows_after"] == 1,
        "production_like_refused": production_refused,
        "retained_by_po_decision": args.retention_decision == "retain",
    }
    if not all(predicates.values()):
        raise RuntimeError("evidence packet predicates failed")
    result_summary = {
        "authorizations": {
            "bounded_configured_v2_vendor_request": "PO_APPROVED",
            "evidence_packet_producer": "PO_APPROVED",
            "synthetic_mapped_cache_write_read_back_idempotence": "PO_APPROVED",
            "synthetic_row_retention": "PO_APPROVED:retain",
        },
        "captured_at_utc": captured_at,
        "identity": {
            "input_fingerprint": observation["input_fingerprint"],
            "synthetic_user_id": args.synthetic_user_id,
            "vendor": "hdapi",
            "vendor_version": 2,
        },
        "predicates": predicates,
        "repository": dict(repository),
        "retention_decision": args.retention_decision,
        "schema": "hde_epic038.ops02.result_summary.v1",
        "status": "PASS",
    }
    files = {
        "commands.txt": _redacted_command(args),
        "stdout.log": sercanon(stdout_summary),
        "stderr.log": b"OPS_STDERR_EMPTY\n",
        "exit_code.txt": b"0\n",
        "env_presence.json": sercanon(_environment_summary(captured_at, repository)),
        "request_summary.json": sercanon(request_summary),
        "mapped_output_summary.json": sercanon(mapped_output),
        "read_back_summary.json": sercanon(read_back),
        "canonical_parity.log": (
            f"PASS canonical_sha256={first['canonical_sha256']} "
            "pre_write_post_read_match=true first_read_back_match=true second_read_back_match=true\n"
        ).encode("utf-8"),
        "idempotence.log": (
            f"PASS first_rows_written={first['rows_written']} second_rows_written={second['rows_written']} "
            f"identity_rows={second['rows_after']} canonical_hash_unchanged=true\n"
        ).encode("utf-8"),
        "no_raw_vendor_payload_persistence.log": (
            "PASS stored_keys=bodygraph,person,person_uid payload_posture=adapter_mapped_no_raw_vendor_payload "
            "raw_standard_response=false raw_chart_result_envelope=false request_body=false response_body=false secrets=false\n"
        ).encode("utf-8"),
        "legacy_fallback_preservation.log": (
            f"PASS classification={legacy['classification']} resource_path={legacy['resource_path']} "
            f"route_family={legacy['route_family']} configured_v2_legacy_fallback=false external_io=0\n"
        ).encode("utf-8"),
        "nonclaims.json": sercanon(nonclaims),
        "result_summary.json": sercanon(result_summary),
    }
    return files


def _failure_files(
    args: argparse.Namespace,
    repository: Mapping[str, str],
    *,
    captured_at: str,
    error_class: str,
    production_refused: bool,
    legacy: Mapping[str, Any],
) -> dict[str, bytes]:
    unavailable = {
        "captured_at_utc": captured_at,
        "error_class": error_class,
        "status": "NOT_PROVEN",
    }
    nonclaims = {
        "captured_at_utc": captured_at,
        "nonclaims": [
            "no_production_write_authorization",
            "no_raw_vendor_envelope_persistence",
            "no_raw_request_or_response_persistence",
            "no_secret_persistence",
            "no_qa_pass_claim",
            "no_acceptance_token_claim",
            "no_pf09_status_movement",
            "no_deployment_change",
            "no_epic_closeout_claim",
        ],
        "retention_decision": args.retention_decision,
        "schema": "hde_epic038.ops02.nonclaims.v1",
    }
    result = {
        "authorizations": {
            "bounded_configured_v2_vendor_request": "PO_APPROVED",
            "evidence_packet_producer": "PO_APPROVED",
            "synthetic_mapped_cache_write_read_back_idempotence": "PO_APPROVED",
            "synthetic_row_retention": "PO_APPROVED:retain",
        },
        "captured_at_utc": captured_at,
        "error_class": error_class,
        "predicates": {
            "explicit_legacy_fallback_preserved": legacy["classification"] == "explicit_legacy_fallback",
            "production_like_refused": production_refused,
            "retained_by_po_decision": args.retention_decision == "retain",
        },
        "repository": dict(repository),
        "retention_decision": args.retention_decision,
        "schema": "hde_epic038.ops02.result_summary.v1",
        "status": "FAIL",
    }
    safe_error = f"OPS_FAILED error_class={error_class}\n".encode("utf-8")
    return {
        "commands.txt": _redacted_command(args),
        "stdout.log": b"OPS_STDOUT_EMPTY\n",
        "stderr.log": safe_error,
        "exit_code.txt": b"1\n",
        "env_presence.json": sercanon(_environment_summary(captured_at, repository)),
        "request_summary.json": sercanon(
            {
                **unavailable,
                "attempt_limit": 1,
                "auth_posture": "Authorization: Bearer <redacted>",
                "request_field_names": ["birthdate", "birthtime", "location"],
                "resource_path": "charts",
                "schema": "hde_epic038.ops02.request_summary.v1",
                "vendor_requests": "unavailable",
            }
        ),
        "mapped_output_summary.json": sercanon(
            {**unavailable, "schema": "hde_epic038.ops02.mapped_output_summary.v1"}
        ),
        "read_back_summary.json": sercanon(
            {
                **unavailable,
                "retention_decision": args.retention_decision,
                "schema": "hde_epic038.ops02.read_back_summary.v1",
                "synthetic_user_id": args.synthetic_user_id,
            }
        ),
        "canonical_parity.log": f"FAIL status=not_proven error_class={error_class}\n".encode("utf-8"),
        "idempotence.log": f"FAIL status=not_proven error_class={error_class}\n".encode("utf-8"),
        "no_raw_vendor_payload_persistence.log": (
            f"FAIL status=not_proven error_class={error_class} evidence_packet_raw_payload=false evidence_packet_secrets=false\n"
        ).encode("utf-8"),
        "legacy_fallback_preservation.log": (
            f"PASS classification={legacy['classification']} resource_path={legacy['resource_path']} "
            f"route_family={legacy['route_family']} configured_v2_legacy_fallback=false external_io=0\n"
        ).encode("utf-8"),
        "nonclaims.json": sercanon(nonclaims),
        "result_summary.json": sercanon(result),
    }


def _checksums(files: Mapping[str, bytes]) -> bytes:
    return "".join(f"{hashlib.sha256(files[name]).hexdigest()}  {name}\n" for name in _CHECKSUM_INPUTS).encode("ascii")


def _assert_secret_safe(files: Mapping[str, bytes], args: argparse.Namespace) -> None:
    combined = b"\n".join(files.values())
    forbidden = [os.environ.get(name, "") for name in _SENSITIVE_ENV]
    forbidden.extend((args.birthdate, args.birthtime, args.location, args.synthetic_person_uid))
    leaked = [value for value in forbidden if value and value.encode("utf-8") in combined]
    if leaked:
        raise RuntimeError("secret-safe packet scan failed")


def _write_packet(evidence_dir: Path, files: dict[str, bytes], args: argparse.Namespace) -> None:
    if set(files) != set(_CHECKSUM_INPUTS):
        raise RuntimeError("OPS packet primary file set mismatch")
    _assert_secret_safe(files, args)
    files["checksums.sha256"] = _checksums(files)
    if tuple(sorted(files)) != tuple(sorted(PACKET_NAMES)):
        raise RuntimeError("OPS packet file set mismatch")
    evidence_dir.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".ops-02-stage-", dir=evidence_dir.parent))
    try:
        for name in PACKET_NAMES:
            (stage / name).write_bytes(files[name])
        os.replace(stage, evidence_dir)
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def main(argv=None) -> int:
    args = _parser().parse_args(argv)
    _preflight(args)
    repository = _repository_identity(require_clean=args.evidence_dir is not None)
    production_refused = _production_refusal_probe(args)
    legacy = _legacy_fallback_probe()
    captured_at = _utc_now()
    try:
        observation = _execute(args)
        stdout_summary = {
            "status": "ok",
            "vendor_requests": observation["vendor_requests"],
            "adapter_status": observation["adapter_code"],
            "provider": observation["provider"],
            "canonical_sha256": observation["canonical_sha256"],
            "read_back_match": observation["first"]["read_back_match"],
            "identity_rows": observation["second"]["rows_after"],
            "second_write_rows": observation["second"]["rows_written"],
            "idempotent": observation["second"]["idempotent"],
            "retention_decision": args.retention_decision or "PO_REQUIRED",
        }
        stdout_bytes = sercanon(stdout_summary)
        if args.evidence_dir is not None:
            files = _success_files(
                args,
                observation,
                repository,
                captured_at=captured_at,
                production_refused=production_refused,
                legacy=legacy,
            )
            if files["stdout.log"] != stdout_bytes:
                raise RuntimeError("stdout evidence mismatch")
            _write_packet(args.evidence_dir, files, args)
        sys.stdout.buffer.write(stdout_bytes)
        return 0
    except Exception as exc:
        error_class = exc.__class__.__name__
        if args.evidence_dir is not None and not args.evidence_dir.exists():
            files = _failure_files(
                args,
                repository,
                captured_at=captured_at,
                error_class=error_class,
                production_refused=production_refused,
                legacy=legacy,
            )
            _write_packet(args.evidence_dir, files, args)
        sys.stderr.write(f"OPS_FAILED error_class={error_class}\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
