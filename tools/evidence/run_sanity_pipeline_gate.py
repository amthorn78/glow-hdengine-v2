"""Run sanity pipeline gate and produce evidence for EPIC024 D07."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env

# Output paths as specified in approved plan
GATE_LOG_PATH = ROOT / "audit" / "gates" / "sanity_pipeline" / "sanity_pipeline.log"
PRIMARY_LOG_DIR = ROOT / "audit" / "qa" / "hde-epic024" / "checks" / "D07_sanity_pipeline"
PRIMARY_LOG_PATH = PRIMARY_LOG_DIR / "primary.log"

# The script writes to this default location
DEFAULT_SANITY_LOG = ROOT / "artifacts" / "sanity" / "sanity.log"

ENV_PINS = {
    "APP_ENV": "dev",
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


def _setup_env() -> dict[str, str]:
    """Build the environment for running the sanity pipeline."""
    env = os.environ.copy()
    env.update(ENV_PINS)
    ensure_determinism_env(environ=env)
    return env


def _write_primary_log(status: str, exit_code: int, captured_env: dict, gate_log_exists: bool) -> None:
    """Write the primary log with structured header."""
    evidence_outputs = []
    if gate_log_exists:
        evidence_outputs.append(GATE_LOG_PATH.relative_to(ROOT).as_posix())
    
    header = {
        "check_id": "D07_sanity_pipeline",
        "status": status,
        "exit_code": exit_code,
        "command": "python tools/evidence/run_sanity_pipeline.py",
        "evidence_outputs": evidence_outputs,
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
    """Main entrypoint for sanity pipeline gate runner."""
    try:
        # Setup environment
        env = _setup_env()
        
        # Run the sanity pipeline
        cmd = [sys.executable, "tools/evidence/run_sanity_pipeline.py"]
        result = subprocess.run(cmd, capture_output=True, env=env, cwd=ROOT)
        
        # Capture environment for logging
        captured_env = {
            "APP_ENV": os.environ.get("APP_ENV", ""),
            "SAFE_MODE": ENV_PINS["SAFE_MODE"],
            "ALLOW_NETWORK": ENV_PINS["ALLOW_NETWORK"],
            "LANG": ENV_PINS["LANG"],
            "LC_ALL": ENV_PINS["LC_ALL"],
            "TZ": ENV_PINS["TZ"],
        }
        
        # Check if the default sanity log was created
        if DEFAULT_SANITY_LOG.exists():
            # Copy it to the gate location
            GATE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(DEFAULT_SANITY_LOG, GATE_LOG_PATH)
            _write_path_proof(GATE_LOG_PATH)
        
        gate_log_exists = GATE_LOG_PATH.exists()
        
        # Determine status
        if result.returncode == 0 and gate_log_exists:
            status = "PASS"
        else:
            status = "FAIL"
        
        # Write primary log
        _write_primary_log(status, result.returncode, captured_env, gate_log_exists)
        
        return result.returncode
        
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        captured_env = {key: ENV_PINS.get(key, "") for key in ["APP_ENV", "SAFE_MODE", "ALLOW_NETWORK", "LANG", "LC_ALL", "TZ"]}
        _write_primary_log("FAIL", 1, captured_env, False)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
