from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable

from engine.serializer import canon
from tools.evidence import update_evidence_index


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT_DIR_REL = Path("artifacts/ops/internal_version")
MANIFEST_NAME = "request_chain_manifest.json"
DEFAULT_PRODUCED_AT = "2025-11-30T03:58:47Z"

_REQUEST_STEPS: list[dict[str, object]] = [
    {
        "name": "get",
        "request": {"method": "GET", "path": "/internal/version"},
        "artifacts": {
            "body": "body_get.json",
            "body_sha256": "body_get.sha256",
            "headers": "headers_get.txt",
        },
    },
    {
        "name": "head",
        "request": {"method": "HEAD", "path": "/internal/version"},
        "artifacts": {"headers": "headers_head.txt"},
    },
    {
        "name": "conditional_if_none_match",
        "request": {
            "headers": {"If-None-Match": "xyz"},
            "method": "GET",
            "path": "/internal/version",
        },
        "artifacts": {"headers": "headers_cond_if_none_match.txt"},
    },
    {
        "name": "conditional_if_modified_since",
        "request": {
            "headers": {"If-Modified-Since": "Wed, 21 Oct 2015 07:28:00 GMT"},
            "method": "GET",
            "path": "/internal/version",
        },
        "artifacts": {"headers": "headers_cond_if_modified_since.txt"},
    },
]


def _ensure_all_exist(paths: Iterable[Path]) -> None:
    missing = [p for p in paths if not p.is_file()]
    if missing:
        missing_list = ", ".join(str(p) for p in missing)
        raise AssertionError(f"missing required internal_version artifacts: {missing_list}")


def _sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _manifest_payload(artifact_dir: Path) -> dict[str, object]:
    return {
        "artifact_root": artifact_dir.relative_to(ROOT).as_posix(),
        "manifest_version": 1,
        "steps": _REQUEST_STEPS,
        "two_run_identity": {"log": "two_run_identity.log"},
    }


def ensure_request_chain_manifest(
    artifact_dir: Path | str,
    *,
    produced_at_utc: str = DEFAULT_PRODUCED_AT,
    allow_create: bool = False,
) -> tuple[Path, Path, str]:
    base_dir = Path(artifact_dir)
    if not base_dir.is_absolute():
        base_dir = ROOT / base_dir
    base_dir.mkdir(parents=True, exist_ok=True)

    body_path = base_dir / "body_get.json"
    digest_path = base_dir / "body_get.sha256"
    required = [
        body_path,
        digest_path,
        base_dir / "headers_get.txt",
        base_dir / "headers_head.txt",
        base_dir / "headers_cond_if_none_match.txt",
        base_dir / "headers_cond_if_modified_since.txt",
        base_dir / "two_run_identity.log",
    ]
    _ensure_all_exist(required)

    recorded_digest = digest_path.read_text(encoding="utf-8").strip()
    computed_digest = _sha256_path(body_path)
    if recorded_digest != computed_digest:
        raise AssertionError("body_get.sha256 does not match body_get.json")

    manifest_path = base_dir / MANIFEST_NAME
    payload = _manifest_payload(base_dir)
    manifest_bytes = canon.sercanon(payload, sort_keys=True)

    if manifest_path.exists():
        existing = manifest_path.read_bytes()
        if existing != manifest_bytes:
            if allow_create:
                manifest_path.write_bytes(manifest_bytes)
            else:
                raise AssertionError(
                    "request_chain_manifest.json is not canonical or is stale"
                )
    elif allow_create:
        manifest_path.write_bytes(manifest_bytes)
    else:
        raise AssertionError("request_chain_manifest.json is missing")

    if not manifest_path.exists():  # pragma: no cover - defensive
        raise AssertionError("request_chain_manifest.json could not be written")

    manifest_rel = manifest_path.relative_to(ROOT).as_posix()
    manifest_sha = hashlib.sha256(manifest_bytes).hexdigest()
    manifest_stat = manifest_path.stat()
    proof_kwargs = dict(
        rel=manifest_rel,
        sha256=manifest_sha,
        size_bytes=manifest_stat.st_size,
        mtime_utc=update_evidence_index._isoformat_from_timestamp(manifest_stat.st_mtime),
        produced_at=produced_at_utc,
        default_produced_at=produced_at_utc,
        stat_mtime=manifest_stat.st_mtime,
    )
    if allow_create:
        proof_rel, _ = update_evidence_index._write_path_proof(check=False, **proof_kwargs)
    proof_rel, _ = update_evidence_index._write_path_proof(check=True, **proof_kwargs)
    proof_path = ROOT / proof_rel
    proof_data = update_evidence_index._load_existing_proof(proof_path)
    if proof_data.get("sha256") != manifest_sha or int(proof_data.get("size_bytes", -1)) != manifest_stat.st_size:
        raise AssertionError("request_chain_manifest path proof does not match manifest bytes")

    return manifest_path, proof_path, manifest_sha
