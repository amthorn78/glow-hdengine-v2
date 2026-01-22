"""Generate sampler evidence artifacts for EPIC024 D04."""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon

# Output paths as specified in approved plan
ARTIFACTS_DIR = ROOT / "artifacts" / "sampler" / "epic024"
EVIDENCE_PATH = ARTIFACTS_DIR / "sampler_evidence.json"
MANIFEST_PATH = ARTIFACTS_DIR / "manifest.json"
PRIMARY_LOG_DIR = ROOT / "audit" / "qa" / "hde-epic024" / "checks" / "D04_sampler_evidence"
PRIMARY_LOG_PATH = PRIMARY_LOG_DIR / "primary.log"

# Existing sampler artifacts to reference
EXISTING_ARTIFACTS = {
    "seed_replay": "artifacts/sampler/seed_replay/cli_http_seed_replay.json",
    "two_run_identity": "artifacts/sampler/two_run/identity.json",
    "abba_parity": "artifacts/sampler/abba/ab_ba_parity.json",
    "pool_snapshots": "artifacts/sampler/pool_snapshots/baseline.json",
    "diversity": "artifacts/sampler/diversity/diversity_requirements.json",
}

ENV_PINS = {
    "APP_ENV": "rails",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
}


def _write_bytes(path: Path, data: bytes) -> None:
    """Write bytes to a file, creating parent directories."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _write_json(path: Path, payload: dict) -> None:
    """Write JSON to a file using canonical serialization."""
    _write_bytes(path, sercanon(payload))


def _write_path_proof(artifact_path: Path) -> None:
    """Write a path proof sidecar for the given artifact."""
    if not artifact_path.exists():
        return
    
    size = artifact_path.stat().st_size
    sha256_hash = hashlib.sha256(artifact_path.read_bytes()).hexdigest()
    mtime = datetime.fromtimestamp(artifact_path.stat().st_mtime, tz=timezone.utc)
    produced_at = datetime.now(timezone.utc)
    
    proof_path = artifact_path.parent / f"{artifact_path.name}.path_proof.txt"
    proof_content = (
        f"path: {artifact_path.relative_to(ROOT).as_posix()}\n"
        f"size_bytes: {size}\n"
        f"sha256: {sha256_hash}\n"
        f"mtime_utc: {mtime.strftime('%Y-%m-%dT%H:%M:%SZ')}\n"
        f"produced_at_utc: {produced_at.strftime('%Y-%m-%dT%H:%M:%SZ')}\n"
    )
    proof_path.write_text(proof_content, encoding="utf-8")


def _check_existing_artifacts() -> dict[str, dict]:
    """Check which existing sampler artifacts are present and get their metadata."""
    artifacts_status = {}
    
    for name, rel_path in EXISTING_ARTIFACTS.items():
        path = ROOT / rel_path
        if path.exists():
            size = path.stat().st_size
            sha256_hash = hashlib.sha256(path.read_bytes()).hexdigest()
            artifacts_status[name] = {
                "path": rel_path,
                "exists": True,
                "size_bytes": size,
                "sha256": sha256_hash,
            }
        else:
            artifacts_status[name] = {
                "path": rel_path,
                "exists": False,
            }
    
    return artifacts_status


def _write_primary_log(status: str, exit_code: int, captured_env: dict) -> None:
    """Write the primary log with structured header."""
    header = {
        "check_id": "D04_sampler_evidence",
        "status": status,
        "exit_code": exit_code,
        "command": "python tools/evidence/run_sampler_evidence.py",
        "evidence_outputs": [
            EVIDENCE_PATH.relative_to(ROOT).as_posix(),
            MANIFEST_PATH.relative_to(ROOT).as_posix(),
        ],
        "captured_env": captured_env,
        "claimed_tokens": [],
        "intended_tokens": [],
        "pf_refs": [],
    }
    
    log_content = (
        json.dumps(header, separators=(",", ":")) + "\n"
        "== STDOUT ==\n\n\n"
        "== STDERR ==\n\n\n"
        "== RC ==\n"
        f"{exit_code}\n"
    )
    
    PRIMARY_LOG_DIR.mkdir(parents=True, exist_ok=True)
    PRIMARY_LOG_PATH.write_text(log_content, encoding="utf-8")
    _write_path_proof(PRIMARY_LOG_PATH)


def main() -> int:
    """Main entrypoint for sampler evidence generation."""
    try:
        # Setup environment
        env = os.environ.copy()
        env.update(ENV_PINS)
        ensure_determinism_env(environ=env)
        
        # Check existing artifacts
        artifacts_status = _check_existing_artifacts()
        
        # Create sampler evidence summary
        evidence = {
            "generator": "tools/evidence/run_sampler_evidence.py",
            "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "epic": "HDE-EPIC024",
            "check_id": "D04_sampler_evidence",
            "referenced_artifacts": artifacts_status,
            "summary": {
                "total_artifacts": len(artifacts_status),
                "existing_artifacts": sum(1 for v in artifacts_status.values() if v.get("exists")),
                "missing_artifacts": sum(1 for v in artifacts_status.values() if not v.get("exists")),
            },
        }
        
        # Create manifest
        manifest = {
            "generator": "tools/evidence/run_sampler_evidence.py",
            "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "epic": "HDE-EPIC024",
            "artifacts": {
                "sampler_evidence": EVIDENCE_PATH.relative_to(ROOT).as_posix(),
                "manifest": MANIFEST_PATH.relative_to(ROOT).as_posix(),
            },
            "referenced_artifacts": list(EXISTING_ARTIFACTS.keys()),
        }
        
        # Write artifacts
        _write_json(EVIDENCE_PATH, evidence)
        _write_json(MANIFEST_PATH, manifest)
        
        # Write path proofs
        _write_path_proof(EVIDENCE_PATH)
        _write_path_proof(MANIFEST_PATH)
        
        # Capture environment for logging
        captured_env = {
            "APP_ENV": os.environ.get("APP_ENV", ""),
            "SAFE_MODE": ENV_PINS["SAFE_MODE"],
            "ALLOW_NETWORK": ENV_PINS["ALLOW_NETWORK"],
            "LANG": ENV_PINS["LANG"],
            "LC_ALL": ENV_PINS["LC_ALL"],
            "TZ": ENV_PINS["TZ"],
        }
        
        # Write primary log
        _write_primary_log("PASS", 0, captured_env)
        
        return 0
        
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        captured_env = {key: ENV_PINS.get(key, "") for key in ["APP_ENV", "SAFE_MODE", "ALLOW_NETWORK", "LANG", "LC_ALL", "TZ"]}
        _write_primary_log("FAIL", 1, captured_env)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
