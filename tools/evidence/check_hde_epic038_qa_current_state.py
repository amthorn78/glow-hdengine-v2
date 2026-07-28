#!/usr/bin/env python3
"""Validate the HDE-EPIC038 QA current-state ledger without writing files."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env
from tools.evidence import generate_open_rails_abba_proof, update_evidence_index

QA_ROOT = ROOT / "audit/qa/hde-epic038"
MANIFEST_PATH = QA_ROOT / "qa_step_logs_manifest.json"
PROOF_PATH = QA_ROOT / "qa_step_logs_manifest.json.path_proof.txt"
SUMMARY_PATH = QA_ROOT / "00_meta/qa_rca_doc_delta_summary.md"
HUMAN_INDEX_PATH = ROOT / "docs/evidence/INDEX.json"
MIRROR_PATH = ROOT / "artifacts/evidence_index.jsonl"
MANIFEST_REL = MANIFEST_PATH.relative_to(ROOT).as_posix()
MANIFEST_KEY = "epic038.qa_step_logs_manifest"
LIVE_PROOF_PATH = ROOT / "audit/gates/determinism/open_rails_vendor_abba.json"
LIVE_PROOF_PATH_PROOF = Path(f"{LIVE_PROOF_PATH}.path_proof.txt")
LIVE_PROOF_REL = LIVE_PROOF_PATH.relative_to(ROOT).as_posix()
LIVE_PROOF_KEY = "epic038.pr03.open_rails_vendor_abba"
LIVE_PROOF_PRODUCED_AT_UTC = "2026-07-27T23:38:09Z"
LIVE_PROOF_SHA256 = (
    "24068e135d24dcb7cc88c4431dfae62dbac236b708545307cba7b9e11278138b"
)
LIVE_PROOF_SIZE = 3419
PR_ROUTING_RECEIPT_PATTERN = re.compile(r"PR#[1-9][0-9]*@[0-9a-f]{40}")
QA08_ID = "qa-08-po-008"
QA08_PRIMARY_SHA256 = (
    "a951cf95094797a05415bf4b46c2031e53774b390ee300227e40870437f3f856"
)
QA08_PRIMARY_SIZE = 4021

CHECK_IDS = (
    "qa-00-step-0-discovery",
    "qa-01-po-001",
    "qa-02-po-002",
    "qa-03-po-003",
    "qa-04-po-004",
    "qa-05-po-005",
    "qa-06-po-006",
    "qa-07-po-007",
    "qa-08-po-008",
    "qa-09-po-009",
    "qa-10-po-010",
    "qa-11-po-011",
    "qa-12-po-012",
    "qa-13-po-013",
    "qa-14-po-014",
    "qa-15-po-015",
    "qa-16-po-016",
    "qa-17-po-017",
    "qa-18-po-018",
    "qa-19-po-019",
    "qa-20-po-020",
    "qa-21-po-021",
    "qa-22-po-022",
    "qa-23-po-023",
)
ALLOWED_STATUSES = {
    "PASS",
    "FAIL_BEHAVIOR",
    "FAIL_TOOLING",
    "TOOLING_BLOCKED",
    "SKIPPED",
    "WARN",
}
PROOF_KEYS = ("path", "sha256", "size_bytes", "mtime_utc", "produced_at_utc")


class CurrentStateError(ValueError):
    """Raised when the retained EPIC038 QA ledger is contradictory or stale."""


def _reject_duplicate_keys(pairs: Iterable[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CurrentStateError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _load_json_object(raw: bytes, *, label: str) -> dict[str, Any]:
    try:
        payload = json.loads(
            raw.decode("utf-8"), object_pairs_hook=_reject_duplicate_keys
        )
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise CurrentStateError(f"invalid JSON in {label}") from exc
    if not isinstance(payload, dict):
        raise CurrentStateError(f"{label} must be a JSON object")
    return payload


def _canonical_json_bytes(payload: dict[str, Any]) -> bytes:
    return (
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")


def build_expected_manifest(
    qa_root: Path = QA_ROOT,
) -> tuple[dict[str, dict[str, Any]], list[tuple[str, str, str | None]]]:
    checks_root = qa_root / "checks"
    discovered = {
        path.parent.name: path
        for path in checks_root.glob("*/primary.log")
        if path.is_file()
    }
    unknown = sorted(set(discovered) - set(CHECK_IDS))
    if unknown:
        raise CurrentStateError(f"unplanned primary logs: {unknown}")

    manifest: dict[str, dict[str, Any]] = {}
    coverage: list[tuple[str, str, str | None]] = []
    for check_id in CHECK_IDS:
        log_path = discovered.get(check_id)
        if log_path is None:
            coverage.append((check_id, "NOT RUN", None))
            continue
        raw = log_path.read_bytes()
        if not raw.splitlines():
            raise CurrentStateError(f"empty primary log: {check_id}")
        header = _load_json_object(raw.splitlines()[0], label=f"{check_id} header")
        if header.get("check_id") != check_id:
            raise CurrentStateError(f"check-id mismatch: {check_id}")
        status = header.get("status")
        if status not in ALLOWED_STATUSES:
            raise CurrentStateError(f"invalid status for {check_id}: {status}")
        relative = log_path.relative_to(qa_root).as_posix()
        manifest[check_id] = {
            "check_id": check_id,
            "log_path": relative,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "size_bytes": len(raw),
            "status": status,
        }
        coverage.append((check_id, status, relative))
    return manifest, coverage


def _parse_utc(value: str, *, label: str) -> None:
    if not value.endswith("Z"):
        raise CurrentStateError(f"{label} must end in Z")
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise CurrentStateError(f"invalid UTC timestamp: {label}") from exc
    if parsed.tzinfo is None:
        raise CurrentStateError(f"timezone missing: {label}")


def validate_manifest_and_proof(
    qa_root: Path = QA_ROOT,
    manifest_path: Path = MANIFEST_PATH,
    proof_path: Path = PROOF_PATH,
) -> tuple[
    dict[str, dict[str, Any]],
    list[tuple[str, str, str | None]],
    dict[str, str],
]:
    expected, coverage = build_expected_manifest(qa_root)
    manifest_raw = manifest_path.read_bytes()
    manifest = _load_json_object(manifest_raw, label="EPIC038 QA manifest")
    if manifest != expected:
        raise CurrentStateError("manifest does not match every current primary log")
    if manifest_raw != _canonical_json_bytes(manifest):
        raise CurrentStateError("manifest is not canonical JSON with one final LF")

    lines = proof_path.read_text(encoding="utf-8").splitlines()
    if len(lines) != len(PROOF_KEYS) or any(": " not in line for line in lines):
        raise CurrentStateError("invalid manifest path-proof shape")
    keys = tuple(line.split(": ", 1)[0] for line in lines)
    if keys != PROOF_KEYS:
        raise CurrentStateError("invalid manifest path-proof key order")
    proof = dict(line.split(": ", 1) for line in lines)
    if proof["path"] != manifest_path.relative_to(ROOT).as_posix():
        raise CurrentStateError("manifest path-proof path mismatch")
    if proof["sha256"] != hashlib.sha256(manifest_raw).hexdigest():
        raise CurrentStateError("manifest path-proof hash mismatch")
    if proof["size_bytes"] != str(len(manifest_raw)):
        raise CurrentStateError("manifest path-proof size mismatch")
    _parse_utc(proof["mtime_utc"], label="mtime_utc")
    _parse_utc(proof["produced_at_utc"], label="produced_at_utc")

    qa08 = manifest.get(QA08_ID)
    if qa08 is None:
        raise CurrentStateError("qa-08-po-008 is missing from the current manifest")
    if qa08["sha256"] != QA08_PRIMARY_SHA256 or qa08["size_bytes"] != QA08_PRIMARY_SIZE:
        raise CurrentStateError("accepted qa-08-po-008 primary log changed")
    return manifest, coverage, proof


def _unique_value(lines: list[str], prefix: str) -> str:
    matches = [line[len(prefix) :] for line in lines if line.startswith(prefix)]
    if len(matches) != 1 or not matches[0]:
        raise CurrentStateError(f"expected one summary line: {prefix}")
    return matches[0]


def _qa08_markers() -> tuple[dict[str, Any], dict[str, str]]:
    raw = (QA_ROOT / f"checks/{QA08_ID}/primary.log").read_bytes()
    header = _load_json_object(raw.splitlines()[0], label="qa-08 header")
    text_lines = raw.decode("utf-8").splitlines()
    prefixes = {
        "routing_type": "ROUTING_TYPE=",
        "routing_receipt": "ROUTING_PROOF=",
        "pre_routing_receipt": "PRE_ROUTING_RECEIPT=",
        "behavior_proof": "BEHAVIOR_PROOF=",
        "behavior_exit": "BEHAVIOR_EXIT_CODE=",
    }
    return header, {
        key: _unique_value(text_lines, prefix) for key, prefix in prefixes.items()
    }


def _validate_live_proof_path_proof(
    raw: bytes,
    proof_path: Path = LIVE_PROOF_PATH_PROOF,
    *,
    expected_path: str = LIVE_PROOF_REL,
) -> dict[str, str]:
    try:
        lines = proof_path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        raise CurrentStateError("qa-08 live-proof path proof is unavailable") from exc
    if len(lines) != len(PROOF_KEYS) or any(": " not in line for line in lines):
        raise CurrentStateError("invalid qa-08 live path-proof shape")
    pairs = [line.split(": ", 1) for line in lines]
    keys = [key for key, _ in pairs]
    if len(set(keys)) != len(PROOF_KEYS) or set(keys) != set(PROOF_KEYS):
        raise CurrentStateError("invalid qa-08 live path-proof keys")
    proof = dict(pairs)
    expected = {
        "path": expected_path,
        "sha256": LIVE_PROOF_SHA256,
        "size_bytes": str(LIVE_PROOF_SIZE),
        "produced_at_utc": LIVE_PROOF_PRODUCED_AT_UTC,
    }
    if any(proof.get(key) != value for key, value in expected.items()):
        raise CurrentStateError("qa-08 live path-proof binding is stale")
    if proof["sha256"] != hashlib.sha256(raw).hexdigest():
        raise CurrentStateError("qa-08 live path-proof hash mismatch")
    if proof["size_bytes"] != str(len(raw)):
        raise CurrentStateError("qa-08 live path-proof size mismatch")
    _parse_utc(proof["mtime_utc"], label="qa-08 live mtime_utc")
    _parse_utc(proof["produced_at_utc"], label="qa-08 live produced_at_utc")
    return proof


def validate_live_proof(
    path: Path = LIVE_PROOF_PATH,
    *,
    proof_path: Path = LIVE_PROOF_PATH_PROOF,
    semantic_check: bool = True,
) -> dict[str, Any]:
    raw = path.read_bytes()
    if (
        hashlib.sha256(raw).hexdigest() != LIVE_PROOF_SHA256
        or len(raw) != LIVE_PROOF_SIZE
    ):
        raise CurrentStateError("accepted qa-08-po-008 live proof changed")
    payload = _load_json_object(raw, label="qa-08 live proof")
    if payload.get("generated_at_utc") != LIVE_PROOF_PRODUCED_AT_UTC:
        raise CurrentStateError("accepted qa-08 live proof timestamp changed")
    _validate_live_proof_path_proof(raw, proof_path)
    if not semantic_check:
        return payload
    try:
        proof = generate_open_rails_abba_proof.generate_live(check=True)
    except SystemExit as exc:
        raise CurrentStateError(
            "accepted qa-08 live proof failed check-only validation"
        ) from exc
    if (
        proof.get("requests_attempted") != 2
        or proof.get("requests_completed") != 2
        or proof.get("top_level_pass") is not True
        or proof.get("result") != "pass"
        or proof.get("acceptance_token_satisfied") is not False
    ):
        raise CurrentStateError("accepted qa-08 live proof posture changed")
    return proof


def _reject_legacy_summary_lines(lines: list[str]) -> None:
    legacy_prefixes = (
        "- Generation command:",
        "- Finalization command:",
        "- Lookup status:",
        "- Lookup detail:",
        "- Pre-routing blocked or failed receipt:",
    )
    if any(line.startswith(legacy_prefixes) for line in lines):
        raise CurrentStateError("summary retains a legacy unscoped state line")
    if "- qa_step_logs_manifest lookup:" in "\n".join(lines):
        raise CurrentStateError(
            "summary retains an unqualified manifest lookup line"
        )


def validate_summary(coverage: list[tuple[str, str, str | None]]) -> str:
    lines = SUMMARY_PATH.read_text(encoding="utf-8").splitlines()
    _reject_legacy_summary_lines(lines)
    rows = [line for line in lines if line.startswith("| qa-")]
    expected_rows = [
        f"| {check_id} | {status} | {relative or 'Unknown'} |"
        for check_id, status, relative in coverage
    ]
    if rows != expected_rows:
        raise CurrentStateError("summary coverage table is stale")
    if any(line.startswith("- qa-08-po-008:") for line in lines):
        raise CurrentStateError("summary contradicts qa-08 PASS")

    header, markers = _qa08_markers()
    if header.get("status") != "PASS" or header.get("exit_code") != 0:
        raise CurrentStateError("qa-08 accepted header posture changed")
    if (
        markers["routing_type"] != "PR"
        or PR_ROUTING_RECEIPT_PATTERN.fullmatch(markers["routing_receipt"])
        is None
    ):
        raise CurrentStateError("qa-08 accepted PR routing provenance changed")
    qa08_values = {
        "- Step status: ": "PASS.",
        "- Step finalization: ": "COMPLETED.",
        "- Header exit code: ": "0.",
        "- Rails: ": "SAFE_MODE=1; ALLOW_NETWORK=0.",
        "- Routing type: ": f"{markers['routing_type']}.",
        "- Routing receipt: ": f"{markers['routing_receipt']}.",
        "- Pre-routing receipt: ": f"{markers['pre_routing_receipt']}.",
        "- Behavioral proof: ": (
            f"{markers['behavior_proof']}; exit code {markers['behavior_exit']}."
        ),
    }
    for prefix, expected in qa08_values.items():
        if _unique_value(lines, prefix) != expected:
            raise CurrentStateError(f"qa-08 summary mismatch: {prefix}")
    step_boundary = (
        "- This completed step record is distinct from epic-wide closeout and "
        "confers no authority for another live call."
    )
    if lines.count(step_boundary) != 1:
        raise CurrentStateError("qa-08 step boundary summary is incomplete")

    completed_moon_loop = (
        "- qa-08-po-008 used the bounded PO-approved Extended Moon Loop recorded "
        "in HDE Build Notes, Addendum 2.31."
    )
    moon_loop_state_lines = [
        line
        for line in lines
        if line.startswith(
            "- qa-08-po-008 used the bounded PO-approved Extended Moon Loop"
        )
        or line.startswith("- No completed qa-08-po-008 Extended Moon Loop")
    ]
    if moon_loop_state_lines != [completed_moon_loop]:
        raise CurrentStateError("summary Extended Moon Loop posture is contradictory")
    no_recurring_authority = (
        "- No retained record confers authority for another live call or later "
        "remediation."
    )
    authority_lines = [
        line
        for line in lines
        if line.startswith("- No retained record confers authority")
    ]
    if authority_lines != [no_recurring_authority]:
        raise CurrentStateError("summary recurring-authority boundary is stale")

    if _unique_value(lines, "- Epic-wide generation command: ") != (
        "qa_closeout generation."
    ):
        raise CurrentStateError("summary generation command is stale")
    finalization = _unique_value(
        lines, "- Epic-wide finalization command: "
    ).removesuffix(".")
    lookup_status = _unique_value(
        lines, "- Epic-wide lookup status: "
    ).removesuffix(".")
    lookup_detail = _unique_value(
        lines, "- Epic-wide lookup detail: "
    ).removesuffix(".")
    lookup_findings = [
        line
        for line in lines
        if line.startswith("- epic-wide qa_step_logs_manifest lookup: ")
    ]
    expected_lookup_findings = (
        []
        if lookup_status == "PASS"
        else [f"- epic-wide qa_step_logs_manifest lookup: {lookup_status}"]
    )
    if lookup_findings != expected_lookup_findings:
        raise CurrentStateError("summary manifest-lookup finding is stale")
    if _unique_value(lines, "- Required routing type: ") != "PR.":
        raise CurrentStateError("summary required routing type is stale")
    routing_receipt = _unique_value(
        lines, "- Epic-wide routing receipt: "
    ).removesuffix(".")
    pre_routing_receipt = _unique_value(
        lines, "- Epic-wide pre-routing blocked or failed receipt: "
    ).removesuffix(".")
    # The plan expressly permits literal NONE when no earlier blocked or failed
    # routing receipt exists; _unique_value already rejects an empty value.
    if finalization == "NOT RUN":
        if (
            lookup_status != "TOOLING_BLOCKED"
            or lookup_detail
            != "approved PR routing and required companion refresh pending"
            or routing_receipt != "NONE"
        ):
            raise CurrentStateError("generation-phase summary routing is incoherent")
    elif finalization == "qa_closeout finalize":
        if (
            lookup_status != "PASS"
            or PR_ROUTING_RECEIPT_PATTERN.fullmatch(routing_receipt) is None
        ):
            raise CurrentStateError("finalized summary routing is incoherent")
        detail_prefix = "updater_exit=0; lookup_hits="
        if not lookup_detail.startswith(detail_prefix):
            raise CurrentStateError("finalized summary lookup detail is unavailable")
        try:
            lookup_hits = json.loads(lookup_detail[len(detail_prefix) :])
        except json.JSONDecodeError as exc:
            raise CurrentStateError("finalized summary lookup detail is invalid") from exc
        expected_hits = {
            "Human Evidence Index": True,
            "Machine Mirror": True,
            "canonical evidence updater/source": True,
        }
        if lookup_hits != expected_hits:
            raise CurrentStateError("finalized summary lookup detail is incomplete")
    else:
        raise CurrentStateError("unknown epic-wide finalization state")

    if _unique_value(lines, "- Canon-drain completion: ") != "NOT CLAIMED.":
        raise CurrentStateError("summary canon-drain nonclaim is stale")
    if _unique_value(lines, "- Formal close-pack completion: ") != "NOT CLAIMED.":
        raise CurrentStateError("summary close-pack nonclaim is stale")

    all_pass = len(coverage) == len(CHECK_IDS) and all(
        status == "PASS" for _, status, _ in coverage
    ) and lookup_status == "PASS"
    completion = (
        "- Repo-supported completion: READY FOR CLOSEOUT REVIEW."
        if all_pass
        else "- Repo-supported completion: NOT READY."
    )
    completion_lines = [
        line for line in lines if line.startswith("- Repo-supported completion: ")
    ]
    if completion_lines != [completion]:
        raise CurrentStateError("summary completion state is stale")
    ready_recommendation = (
        "- Proceed to closeout review using the governed evidence pointers above."
    )
    not_ready_recommendation = (
        "- Do not claim QA closeout; resolve or formally disposition every "
        "non-PASS and NOT RUN item."
    )
    expected_recommendation = (
        ready_recommendation if all_pass else not_ready_recommendation
    )
    recommendation_lines = [
        line
        for line in lines
        if line in {ready_recommendation, not_ready_recommendation}
    ]
    if recommendation_lines != [expected_recommendation]:
        raise CurrentStateError("summary readiness recommendation is stale")
    return lookup_status


def _matching_rows(
    rows: Iterable[dict[str, Any]],
    *,
    artifact_key: str = MANIFEST_KEY,
    path: str = MANIFEST_REL,
) -> list[dict[str, Any]]:
    keyed = [row for row in rows if row.get("artifact_key") == artifact_key]
    if len(keyed) != 1 or keyed[0].get("discovered_physical_path") != path:
        return []
    return keyed


def validate_index_binding(proof: dict[str, str]) -> None:
    source_rows = _matching_rows(update_evidence_index.EPIC038_QA_PRIMARY_ARTIFACTS)
    if len(source_rows) != 1:
        raise CurrentStateError("canonical updater does not own the EPIC038 manifest")

    human_payload = json.loads(HUMAN_INDEX_PATH.read_text(encoding="utf-8"))
    if not isinstance(human_payload, list) or len(_matching_rows(human_payload)) != 1:
        raise CurrentStateError("Human Evidence Index lacks the EPIC038 manifest")

    mirror_rows = [
        json.loads(line)
        for line in MIRROR_PATH.read_text(encoding="utf-8").splitlines()
        if line
    ]
    matches = _matching_rows(mirror_rows)
    if len(matches) != 1:
        raise CurrentStateError("Machine Mirror lacks the EPIC038 manifest")
    record = matches[0]
    expected = {
        "sha256": proof["sha256"],
        "size_bytes": int(proof["size_bytes"]),
        "proof_anchor": f"{MANIFEST_REL}.path_proof.txt",
        "produced_at_utc": proof["produced_at_utc"],
    }
    if any(record.get(key) != value for key, value in expected.items()):
        raise CurrentStateError("Machine Mirror EPIC038 manifest binding is stale")

    live_source_rows = _matching_rows(
        update_evidence_index.EPIC038_PR03_PRIMARY_ARTIFACTS,
        artifact_key=LIVE_PROOF_KEY,
        path=LIVE_PROOF_REL,
    )
    if len(live_source_rows) != 1:
        raise CurrentStateError("canonical updater does not own the qa-08 live proof")
    live_human_rows = _matching_rows(
        human_payload, artifact_key=LIVE_PROOF_KEY, path=LIVE_PROOF_REL
    )
    if len(live_human_rows) != 1:
        raise CurrentStateError("Human Evidence Index lacks the qa-08 live proof")
    live_matches = _matching_rows(
        mirror_rows, artifact_key=LIVE_PROOF_KEY, path=LIVE_PROOF_REL
    )
    if len(live_matches) != 1:
        raise CurrentStateError("Machine Mirror lacks the qa-08 live proof")
    live_record = live_matches[0]
    live_expected = {
        "sha256": LIVE_PROOF_SHA256,
        "size_bytes": LIVE_PROOF_SIZE,
        "proof_anchor": f"{LIVE_PROOF_REL}.path_proof.txt",
        "produced_at_utc": LIVE_PROOF_PRODUCED_AT_UTC,
    }
    if live_human_rows[0].get("produced_at_utc") != LIVE_PROOF_PRODUCED_AT_UTC:
        raise CurrentStateError("Human Evidence Index qa-08 live-proof time is stale")
    if any(live_record.get(key) != value for key, value in live_expected.items()):
        raise CurrentStateError("Machine Mirror qa-08 live-proof binding is stale")


def validate_current_state(*, require_finalized: bool = False) -> None:
    _, coverage, proof = validate_manifest_and_proof()
    validate_live_proof()
    lookup_status = validate_summary(coverage)
    if require_finalized and lookup_status != "PASS":
        raise CurrentStateError("EPIC038 current-state ledger is not finalized")
    validate_index_binding(proof)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-finalized",
        action="store_true",
        help="require the routed current-state ledger lookup to be finalized",
    )
    args = parser.parse_args(argv)
    ensure_determinism_env()
    validate_current_state(require_finalized=args.require_finalized)
    print("HDE_EPIC038_QA_CURRENT_STATE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
