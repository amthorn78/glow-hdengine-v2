#!/usr/bin/env python3
"""Harden the evidence index, hash sentinel, and machine mirror.

Discovery summary (PR2 — EPIC017):
- INDEX + sentinel already existed under docs/evidence with loose schema (title/path/proof).
- The machine mirror lived at artifacts/evidence_index.jsonl with the required keys already,
  enforced partially by ci/checks/check_mirror_schema.sh.
- Path-proofs were scattered as ``*.path_proof.txt`` files with path/sha/size/mtime lines
  written by helpers such as tools/evidence/generate_rails_closed_phase1.py.
- No topology orientation demo artifact existed yet; CI only checked the sentinel hash and
  mirror schema ordering.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path
from typing import Iterable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
HUMAN_INDEX = ROOT / "docs/evidence/INDEX.json"
HASH_SENTINEL = ROOT / "docs/evidence/INDEX.sha256"
MIRROR_PATH = ROOT / "artifacts/evidence_index.jsonl"
MIRROR_REL = MIRROR_PATH.relative_to(ROOT).as_posix()
MIRROR_SHA_PATH = ROOT / "artifacts/evidence_index.jsonl.sha256"
EPIC020_BUNDLE_DIR = ROOT / "artifacts" / "epic020" / "bundles"
EPIC020_ACCEPTANCE_MAP = ROOT / "docs" / "acceptance_map_epic020.json"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, ensure_determinism_env
BASELINE_ENTRIES: list[dict[str, object]] = [
    {
        "artifact_key": "registry.registry_report",
        "discovered_physical_path": "artifacts/registry/registry_report.json",
        "record_type": "registry_report",
        "schema_version": "1.0",
    },
    {
        "artifact_key": "sanity.pipeline.log",
        "discovered_physical_path": "artifacts/sanity/sanity.log",
        "record_type": "sanity_log",
        "schema_version": "1.0",
    },
]
EPIC022_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic022.close_report",
        "discovered_physical_path": "audit/EPIC-022_close_report.md",
        "epic_id": "HDE-EPIC022",
    },
    {
        "artifact_key": "epic022.manifest",
        "discovered_physical_path": "audit/EPIC-022_MANIFEST.json",
        "epic_id": "HDE-EPIC022",
    },
    {
        "artifact_key": "epic022.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic022/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC022",
    },
    {
        "artifact_key": "epic022.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic022.json",
        "epic_id": "HDE-EPIC022",
    },
    {
        "artifact_key": "audit.cli.two_run_identity",
        "discovered_physical_path": "artifacts/audit/cli/two_run_identity.log",
        "record_type": "audit_cli_log",
    },
]
EPIC024_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic024.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic024.json",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic024/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.acceptance_map_viability",
        "discovered_physical_path": "audit/qa/hde-epic024/acceptance_map_viability.log",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.qa_step_logs_manifest",
        "discovered_physical_path": "audit/qa/hde-epic024/qa_step_logs_manifest.json",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.qa_meta_doc_deltas",
        "discovered_physical_path": "audit/qa/hde-epic024/00_meta/doc_deltas.md",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.doc_deltas",
        "discovered_physical_path": "audit/docdeltas/hde-epic024_doc_deltas.md",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.close_report",
        "discovered_physical_path": "audit/EPIC-024_close_report.md",
        "epic_id": "HDE-EPIC024",
    },
    {
        "artifact_key": "epic024.manifest",
        "discovered_physical_path": "audit/EPIC-024_MANIFEST.json",
        "epic_id": "HDE-EPIC024",
    },
]

EPIC027_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic027.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic027.json",
        "epic_id": "HDE-EPIC027",
    },
    {
        "artifact_key": "epic027.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic027/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC027",
    },
    {
        "artifact_key": "epic027.acceptance_map_viability",
        "discovered_physical_path": "audit/qa/hde-epic027/acceptance_map_viability.log",
        "epic_id": "HDE-EPIC027",
    },
    {
        "artifact_key": "epic027.qa_step_logs_manifest",
        "discovered_physical_path": "audit/qa/hde-epic027/qa_step_logs_manifest.json",
        "epic_id": "HDE-EPIC027",
    },
    {
        "artifact_key": "epic027.close_report",
        "discovered_physical_path": "audit/EPIC-027_close_report.md",
        "epic_id": "HDE-EPIC027",
    },
    {
        "artifact_key": "epic027.manifest",
        "discovered_physical_path": "audit/EPIC-027_MANIFEST.json",
        "epic_id": "HDE-EPIC027",
    },
]

EPIC028_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "epic028.acceptance_map",
        "discovered_physical_path": "docs/acceptance_map_epic028.json",
        "epic_id": "HDE-EPIC028",
    },
    {
        "artifact_key": "epic028.token_matrix",
        "discovered_physical_path": "audit/qa/hde-epic028/token_evidence_matrix.md",
        "epic_id": "HDE-EPIC028",
    },
    {
        "artifact_key": "epic028.acceptance_map_viability",
        "discovered_physical_path": "audit/qa/hde-epic028/acceptance_map_viability.log",
        "epic_id": "HDE-EPIC028",
    },
]

A7_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "a7.success_encoding_invariance",
        "discovered_physical_path": "artifacts/proofs/success_encoding_invariance.txt",
    },
]

CLI_CONFORMANCE_ARTIFACTS: list[dict[str, object]] = [
    {"artifact_key": "cli.help.hdctl", "discovered_physical_path": "artifacts/cli/help/hdctl_help.txt"},
    {"artifact_key": "cli.help.showcompat", "discovered_physical_path": "artifacts/cli/help/showcompat_help.txt"},
    {"artifact_key": "cli.help.reject_nonjson", "discovered_physical_path": "artifacts/cli/help/reject_nonjson.txt"},
    {"artifact_key": "cli.install.entrypoints", "discovered_physical_path": "artifacts/cli/install/entrypoints.txt"},
    {"artifact_key": "cli.install.installability_summary", "discovered_physical_path": "artifacts/cli/install/installability_summary.json"},
    {"artifact_key": "cli.showcompat.ab", "discovered_physical_path": "artifacts/cli/ab.json"},
    {"artifact_key": "cli.showcompat.ba", "discovered_physical_path": "artifacts/cli/ba.json"},
    {"artifact_key": "cli.showcompat.summary", "discovered_physical_path": "artifacts/cli/summary.json"},
]

COMPAT_PRIMARY_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "compat.conjunction.identity_hash",
        "discovered_physical_path": "artifacts/compat/identity_hash.txt",
        "record_type": "compat_identity_hash",
        "schema_version": "1.0",
    }
]

CONJUNCTION_WRITER_ARTIFACTS: list[dict[str, object]] = [
    {
        "artifact_key": "conjunction.writer.write_readback",
        "discovered_physical_path": "artifacts/writer/conjunction_write_readback.log",
        "record_type": "writer_log",
        "schema_version": "1.0",
    },
    {
        "artifact_key": "conjunction.writer.summary",
        "discovered_physical_path": "artifacts/writer/conjunction_writer_summary.json",
        "record_type": "writer_summary",
        "schema_version": "1.0",
    },
]

FORCE_REFRESH_ARTIFACT_RELS: set[str] = {
    "artifacts/proofs/success_encoding_invariance.txt",
    "artifacts/evidence_index.jsonl",
    "artifacts/evidence_index.jsonl.sha256",
    "docs/evidence/INDEX.json",
    "docs/evidence/INDEX.sha256",
    "audit/gates/topology/orientation_demo.txt",
}


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_path(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _render_env_pins() -> str:
    ordered = [f"{key}={DETERMINISM_ENV_PINS[key]}" for key in sorted(DETERMINISM_ENV_PINS)]
    return ",".join(ordered)


def _isoformat(dt: _dt.datetime) -> str:
    return dt.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _isoformat_from_timestamp(ts: float) -> str:
    return _isoformat(_dt.datetime.fromtimestamp(ts, tz=_dt.timezone.utc))


def _parse_utc_iso8601(raw: str) -> _dt.datetime:
    dt = _dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
    if dt.tzinfo != _dt.timezone.utc:
        raise ValueError("expected UTC tzinfo")
    if dt.microsecond:
        raise ValueError("expected zero microseconds")
    return dt


def _load_mirror_roles() -> dict[tuple[str, str], str]:
    roles: dict[tuple[str, str], str] = {}
    if not MIRROR_PATH.exists():
        return roles
    for raw in MIRROR_PATH.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        obj = json.loads(raw)
        roles[(obj["artifact_key"], obj["discovered_physical_path"])] = obj.get("role", "snapshot")
    return roles


def _load_existing_proof(proof_path: Path) -> dict[str, str]:
    if not proof_path.exists():
        return {}
    data: dict[str, str] = {}
    for line in proof_path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def _write_path_proof(
    rel: str,
    *,
    sha256: str,
    size_bytes: int,
    mtime_utc: str | None,
    produced_at: str | None,
    default_produced_at: str,
    check: bool,
    stat_mtime: float,
    extra_fields: Mapping[str, str] | None = None,
) -> tuple[str, str]:
    """Write or validate a path-proof for the given relative path.

    NEW CANON (EPIC017 WS-D4 mtime semantics): mtime_utc captures the filesystem
    mtime at evidence refresh time, truncated to seconds. It is not required to
    remain equal to future stat() values across clones. Proof checks validate
    shape and monotonicity but do not fail solely due to mtime drift.
    """

    proof_rel = f"{rel}.path_proof.txt"
    proof_path = ROOT / proof_rel
    proof_path.parent.mkdir(parents=True, exist_ok=True)

    def _normalize_utc(raw: str | None) -> str | None:
        if not raw:
            return None
        try:
            _parse_utc_iso8601(raw)
        except Exception:  # noqa: BLE001
            return None
        return raw

    existing = _load_existing_proof(proof_path)
    stat_mtime_iso = _isoformat_from_timestamp(stat_mtime)
    extra_fields = dict(extra_fields or {})
    existing_produced = _normalize_utc(existing.get("produced_at_utc"))
    existing_mtime = _normalize_utc(existing.get("mtime_utc"))
    requested_produced = _normalize_utc(produced_at)
    requested_mtime = _normalize_utc(mtime_utc)
    if rel in FORCE_REFRESH_ARTIFACT_RELS and not check:
        existing_produced = None
        existing_mtime = None
    produced = requested_produced or existing_produced or default_produced_at

    if check:
        if not proof_path.exists():
            raise SystemExit(f"MISSING_PROOF:{proof_rel}")
        proof = existing
        if proof.get("path") != rel:
            raise SystemExit(f"PROOF_PATH:{proof_rel}")
        if proof.get("sha256") != sha256:
            raise SystemExit(f"PROOF_SHA:{proof_rel}")
        try:
            recorded_size = int(proof.get("size_bytes", ""))
        except ValueError as exc:  # pragma: no cover - defensive
            raise SystemExit(f"PROOF_SIZE:{proof_rel}") from exc
        if recorded_size != size_bytes:
            raise SystemExit(f"PROOF_SIZE:{proof_rel}")
        for key, value in extra_fields.items():
            if proof.get(key) != value:
                raise SystemExit(f"PROOF_FIELD:{proof_rel}:{key}")

        mtime_raw = proof.get("mtime_utc")
        produced_raw = proof.get("produced_at_utc")
        if not mtime_raw or not produced_raw:
            raise SystemExit(f"PROOF_FIELDS:{proof_rel}")
        try:
            mtime_parsed = _parse_utc_iso8601(mtime_raw)
            _parse_utc_iso8601(produced_raw)
        except Exception as exc:  # noqa: BLE001
            raise SystemExit(f"PROOF_MTIME:{proof_rel}") from exc

        stat_mtime_dt = _dt.datetime.fromtimestamp(stat_mtime, tz=_dt.timezone.utc)
        if mtime_parsed > stat_mtime_dt:
            raise SystemExit(f"PROOF_MTIME_FUTURE:{proof_rel}")
        return proof_rel, produced

    mtime = requested_mtime or existing_mtime or stat_mtime_iso
    proof_lines = [
        f"path: {rel}",
        f"size_bytes: {size_bytes}",
        f"sha256: {sha256}",
    ]
    for key, value in extra_fields.items():
        proof_lines.append(f"{key}: {value}")
    proof_lines.extend(
        [
        f"mtime_utc: {mtime}",
        f"produced_at_utc: {produced}",
        "",
        ]
    )
    proof_text = "\n".join(proof_lines)
    if proof_path.exists():
        existing_text = proof_path.read_text(encoding="utf-8")
        if existing_text == proof_text:
            return proof_rel, produced
    proof_path.write_text(proof_text, encoding="utf-8")
    return proof_rel, produced


_ALLOWED_INDEX_FIELDS = {
    "artifact_key",
    "discovered_physical_path",
    "epic_id",
    "record_type",
    "schema_version",
    "tokens",
    "notes",
    "produced_at_utc",
    "sha256",
    "size_bytes",
}


def _normalize_index_entry(entry: Mapping[str, object]) -> dict[str, object]:
    key = entry.get("artifact_key") or entry.get("title")
    path = entry.get("discovered_physical_path") or entry.get("path")
    if not isinstance(key, str) or not isinstance(path, str):
        raise ValueError(f"Invalid entry: {entry!r}")

    if "audit/qa/hde-epic024/checks/" in path:
        parts = path.split("/")
        normalized_parts = []
        for part in parts:
            if part.startswith("D") and len(part) > 1 and part[1].isdigit():
                normalized_parts.append(part.lower())
            else:
                normalized_parts.append(part)
        path = "/".join(normalized_parts)

    normalized: dict[str, object] = {
        "artifact_key": key,
        "discovered_physical_path": path,
    }

    for field in _ALLOWED_INDEX_FIELDS:
        if field in {"artifact_key", "discovered_physical_path"}:
            continue
        if field in entry:
            value = entry[field]
            if field == "tokens":
                if not isinstance(value, (list, tuple)):
                    raise ValueError(f"Invalid tokens for {key}: {value!r}")
                value = list(value)
            normalized[field] = value
    return normalized


def _dedupe_entries(entries: Iterable[Mapping[str, object]]) -> list[dict[str, object]]:
    deduped: dict[tuple[str, str], dict[str, object]] = {}
    for entry in entries:
        normalized = _normalize_index_entry(entry)
        deduped[(normalized["artifact_key"], normalized["discovered_physical_path"])] = normalized
    return sorted(deduped.values(), key=lambda item: (item["artifact_key"], item["discovered_physical_path"]))


def _load_human_index() -> list[dict[str, object]]:
    payload = json.loads(HUMAN_INDEX.read_text(encoding="utf-8"))
    return _dedupe_entries(
        [
            *payload,
            *BASELINE_ENTRIES,
            *EPIC022_PRIMARY_ARTIFACTS,
            *EPIC024_PRIMARY_ARTIFACTS,
            *EPIC027_PRIMARY_ARTIFACTS,
            *EPIC028_PRIMARY_ARTIFACTS,
            *A7_PRIMARY_ARTIFACTS,
            *COMPAT_PRIMARY_ARTIFACTS,
            *CLI_CONFORMANCE_ARTIFACTS,
            *CONJUNCTION_WRITER_ARTIFACTS,
        ]
    )


def _render_human_index(entries: Iterable[Mapping[str, object]]) -> bytes:
    normalized = _dedupe_entries(entries)
    return (json.dumps(normalized, separators=(",", ":"), sort_keys=True) + "\n").encode("utf-8")


def _role_for(entry: Mapping[str, str], roles: Mapping[tuple[str, str], str]) -> str:
    key = (entry["artifact_key"], entry["discovered_physical_path"])
    if key in roles:
        return roles[key]
    path = entry["discovered_physical_path"]
    if "/proofs/" in path or path.endswith(".proof.txt"):
        return "proof"
    if path.endswith(".log"):
        return "log"
    if "/audit/" in path:
        return "audit"
    return "snapshot"


def _load_epic020_tokens(epic_id: str) -> set[str]:
    if epic_id != "HDE-EPIC020":
        return set()
    if not EPIC020_ACCEPTANCE_MAP.exists():
        raise SystemExit("MISSING:docs/acceptance_map_epic020.json")
    data = json.loads(EPIC020_ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    if data.get("epic_id") != epic_id:
        raise SystemExit(f"EPIC_MISMATCH:{EPIC020_ACCEPTANCE_MAP}")
    tokens = set(data.get("token_status", {}))
    if not tokens:
        raise SystemExit("CANON_GAP:EPIC020_TOKENS")
    return tokens


def _load_epic020_bundle_entries(epic_id: str, allowed_tokens: Sequence[str]) -> list[dict[str, object]]:
    manifests = sorted(EPIC020_BUNDLE_DIR.glob("*.manifest.json"))
    if not manifests:
        raise SystemExit("MISSING_EPIC020_BUNDLES")

    allowed = set(allowed_tokens)
    if not allowed:
        raise SystemExit("CANON_GAP:EPIC020_TOKENS")

    entries: list[dict[str, object]] = []
    for manifest_path in manifests:
        manifest_rel = manifest_path.relative_to(ROOT).as_posix()
        manifest_payload = json.loads(manifest_path.read_text(encoding="utf-8"))
        bundle_key = manifest_payload.get("artifact_key")
        bundle_path_rel = manifest_payload.get("bundle_path")
        produced_at = manifest_payload.get("produced_at_utc")
        schema_version = manifest_payload.get("schema_version", "1.0")

        if not bundle_key or not bundle_path_rel:
            raise SystemExit(f"INVALID_MANIFEST:{manifest_rel}")
        if produced_at is None:
            raise SystemExit(f"MISSING_PRODUCED_AT:{manifest_rel}")
        if bundle_key not in allowed:
            raise SystemExit(f"CANON_GAP:{bundle_key}")

        bundle_path = ROOT / bundle_path_rel
        if not bundle_path.exists():
            raise SystemExit(f"MISSING_BUNDLE:{bundle_path_rel}")

        bundle_sha = _sha256_path(bundle_path)
        bundle_size = bundle_path.stat().st_size
        manifest_sha = _sha256_path(manifest_path)
        manifest_size = manifest_path.stat().st_size

        notes = f"EPIC020 Candidate 1 bundle for {bundle_key}"
        tokens = [bundle_key]

        entries.append(
            {
                "artifact_key": bundle_key,
                "discovered_physical_path": bundle_path_rel,
                "epic_id": epic_id,
                "record_type": "epic020_bundle",
                "schema_version": schema_version,
                "produced_at_utc": produced_at,
                "sha256": bundle_sha,
                "size_bytes": bundle_size,
                "tokens": tokens,
                "notes": notes,
            }
        )

        entries.append(
            {
                "artifact_key": bundle_key,
                "discovered_physical_path": manifest_rel,
                "epic_id": epic_id,
                "record_type": "epic020_bundle_manifest",
                "schema_version": schema_version,
                "produced_at_utc": produced_at,
                "sha256": manifest_sha,
                "size_bytes": manifest_size,
                "tokens": tokens,
                "notes": f"EPIC020 Candidate 1 manifest for {bundle_key}",
            }
        )

    return _dedupe_entries(entries)


def _render_mirror(
    entries: Iterable[Mapping[str, str]], *, produced_default: str, check: bool
) -> tuple[bytes, dict[str, object]]:
    """Render the machine mirror with a deterministic self-record.

    The self-record is derived only from the rendered body; it does not depend on
    any on-disk mirror or path-proof state so that a write pass followed by
    `--check` is idempotent when artifacts are unchanged.
    """

    raise_on_duplicate: set[tuple[str, str]] = set()
    records: list[dict[str, object]] = []
    roles = _load_mirror_roles()

    for entry in entries:
        path = entry["discovered_physical_path"]
        rel_path = ROOT / path
        key = (entry["artifact_key"], path)
        if key in raise_on_duplicate:
            raise SystemExit(f"DUPLICATE_MIRROR_KEY:{key}")
        raise_on_duplicate.add(key)

        record: dict[str, object] = dict(entry)
        record.setdefault("artifact_key", entry["artifact_key"])
        record.setdefault("discovered_physical_path", path)
        record.setdefault("produced_at_utc", None)
        record.setdefault("proof_anchor", f"{path}.path_proof.txt")
        record.setdefault("role", _role_for(entry, roles))
        record.setdefault("sha256", None)
        record.setdefault("size_bytes", None)

        if rel_path == MIRROR_PATH:
            record["role"] = "self_record"
            records.append(record)
            continue

        sha = _sha256_bytes(rel_path.read_bytes())
        stat = rel_path.stat()
        proof_anchor, produced_at = _write_path_proof(
            path,
            sha256=sha,
            size_bytes=stat.st_size,
            mtime_utc=None,
            produced_at=str(entry.get("produced_at_utc")) if entry.get("produced_at_utc") else None,
            default_produced_at=produced_default,
            check=check,
            stat_mtime=stat.st_mtime,
        )
        record.update({
            "sha256": sha,
            "size_bytes": stat.st_size,
            "produced_at_utc": produced_at,
            "proof_anchor": proof_anchor,
        })
        records.append(record)

    records.sort(key=lambda rec: (rec["artifact_key"], rec["discovered_physical_path"]))

    try:
        mirror_key = next(
            i
            for i, rec in enumerate(records)
            if rec["artifact_key"] == "index.machine_mirror"
            and rec["discovered_physical_path"] == MIRROR_REL
        )
    except StopIteration as exc:  # pragma: no cover - defensive
        raise SystemExit("MISSING_SELF_RECORD") from exc

    rendered_lines = [json.dumps(rec, separators=(",", ":"), sort_keys=True) for rec in records]
    body_lines = [line for i, line in enumerate(rendered_lines) if i != mirror_key]
    body_text = "\n".join(body_lines) + ("\n" if body_lines else "")

    mirror_rec = records[mirror_key]
    mirror_rec["produced_at_utc"] = produced_default
    mirror_rec["sha256"] = _sha256_bytes(body_text.encode("utf-8"))

    while True:
        rendered_lines = [json.dumps(rec, separators=(",", ":"), sort_keys=True) for rec in records]
        text = "\n".join(rendered_lines) + "\n"
        size = len(text.encode("utf-8"))
        if size == mirror_rec.get("size_bytes"):
            break
        mirror_rec["size_bytes"] = size

    return ("\n".join(rendered_lines) + "\n").encode("utf-8"), mirror_rec


def _write_if_changed(path: Path, content: bytes, *, check: bool) -> None:
    if path.exists():
        existing = path.read_bytes()
        if existing == content:
            return
        if check:
            raise SystemExit(f"STALE:{path}")
    elif check:
        raise SystemExit(f"STALE:{path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def _refresh_path_proof(path: Path, *, default_produced_at: str, check: bool) -> None:
    rel = path.relative_to(ROOT).as_posix()
    proof_existing = _load_existing_proof(ROOT / f"{rel}.path_proof.txt")
    stat = path.stat()
    _write_path_proof(
        rel,
        sha256=_sha256_path(path),
        size_bytes=stat.st_size,
        mtime_utc=proof_existing.get("mtime_utc"),
        produced_at=proof_existing.get("produced_at_utc"),
        default_produced_at=default_produced_at,
        check=check,
        stat_mtime=stat.st_mtime,
    )


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Maintain the evidence index and mirror")
    parser.add_argument("--check", action="store_true", help="Fail if files would change")
    parser.add_argument(
        "--epic-id",
        action="append",
        default=[],
        help="Integrate epic-specific governed artifacts (e.g. HDE-EPIC020)",
    )
    args = parser.parse_args(argv)

    ensure_determinism_env()
    print(f"[evidence-index] env pins: {_render_env_pins()}")

    produced_default = _isoformat(_dt.datetime.now(tz=_dt.timezone.utc))
    mirror_proof_path = MIRROR_PATH.with_suffix(".jsonl.path_proof.txt")
    mirror_proof_existing = _load_existing_proof(mirror_proof_path)
    mirror_produced = mirror_proof_existing.get("produced_at_utc")
    if mirror_produced:
        try:
            _parse_utc_iso8601(mirror_produced)
        except Exception:  # noqa: BLE001
            mirror_produced = None
    if mirror_produced:
        produced_default = mirror_produced

    def _stale_proof(rel: str) -> bool:
        proof = _load_existing_proof(ROOT / f"{rel}.path_proof.txt")
        mtime_raw = proof.get("mtime_utc")
        produced_raw = proof.get("produced_at_utc")
        if not mtime_raw or not produced_raw:
            return False
        try:
            return _parse_utc_iso8601(produced_raw) < _parse_utc_iso8601(mtime_raw)
        except Exception:  # noqa: BLE001
            return True

    if any(_stale_proof(rel) for rel in FORCE_REFRESH_ARTIFACT_RELS):
        produced_default = _isoformat(_dt.datetime.now(tz=_dt.timezone.utc))

    entries = _load_human_index()

    epic_ids = set(args.epic_id)
    if "HDE-EPIC020" in epic_ids:
        epic020_tokens = _load_epic020_tokens("HDE-EPIC020")
        entries = _dedupe_entries(entries + _load_epic020_bundle_entries("HDE-EPIC020", epic020_tokens))

    index_bytes = _render_human_index(entries)
    _write_if_changed(HUMAN_INDEX, index_bytes, check=args.check)

    hash_line = f"{_sha256_bytes(index_bytes)}  docs/evidence/INDEX.json\n".encode("utf-8")
    _write_if_changed(HASH_SENTINEL, hash_line, check=args.check)
    _refresh_path_proof(HUMAN_INDEX, default_produced_at=produced_default, check=args.check)
    _refresh_path_proof(HASH_SENTINEL, default_produced_at=produced_default, check=args.check)

    mirror_bytes, mirror_rec = _render_mirror(entries, produced_default=produced_default, check=args.check)
    mirror_size = len(mirror_bytes)
    mirror_rec["size_bytes"] = mirror_size
    _write_if_changed(MIRROR_PATH, mirror_bytes, check=args.check)

    mirror_stat = MIRROR_PATH.stat()
    mirror_file_sha = _sha256_path(MIRROR_PATH)
    mirror_sha_line = f"{mirror_file_sha}  {MIRROR_REL}\n".encode("utf-8")
    _write_if_changed(MIRROR_SHA_PATH, mirror_sha_line, check=args.check)
    _refresh_path_proof(MIRROR_SHA_PATH, default_produced_at=produced_default, check=args.check)

    mirror_body_sha = str(mirror_rec["sha256"])
    proof_anchor, produced_at = _write_path_proof(
        MIRROR_REL,
        sha256=mirror_file_sha,
        size_bytes=mirror_stat.st_size,
        mtime_utc=mirror_proof_existing.get("mtime_utc"),
        produced_at=str(mirror_rec.get("produced_at_utc")),
        default_produced_at=produced_default,
        check=args.check,
        stat_mtime=mirror_stat.st_mtime,
        extra_fields={"mirror_body_sha256": mirror_body_sha},
    )
    if proof_anchor != mirror_rec["proof_anchor"]:
        mirror_rec["proof_anchor"] = proof_anchor
        if args.check:
            raise SystemExit(f"STALE_PROOF:{proof_anchor}")
    if produced_at != mirror_rec["produced_at_utc"]:
        mirror_rec["produced_at_utc"] = produced_at
        if args.check:
            raise SystemExit(f"STALE_PRODUCED_AT:{MIRROR_REL}")
    if mirror_stat.st_size != int(mirror_rec["size_bytes"]):
        if args.check:
            raise SystemExit(f"STALE_SIZE:{MIRROR_REL}")
        mirror_rec["size_bytes"] = mirror_stat.st_size


if __name__ == "__main__":
    main()
