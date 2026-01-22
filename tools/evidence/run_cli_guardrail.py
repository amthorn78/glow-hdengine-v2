"""Run CLI serializer grep guard and produce evidence for EPIC024 D08."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env

# Output paths
GUARD_LOG_PATH = ROOT / "artifacts" / "cli" / "guards" / "serializer_grep_guard.log"
PRIMARY_LOG_DIR = ROOT / "audit" / "qa" / "hde-epic024" / "checks" / "D08_cli_guardrail"
PRIMARY_LOG_PATH = PRIMARY_LOG_DIR / "primary.log"
CLI_MAIN_PATH = ROOT / "engine" / "cli" / "main.py"

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
    """Build the environment for running the guard."""
    env = os.environ.copy()
    env.update(ENV_PINS)
    ensure_determinism_env(environ=env)
    return env


def _write_primary_log(status: str, exit_code: int, captured_env: dict, guard_log_exists: bool) -> None:
    """Write the primary log with structured header."""
    evidence_outputs = []
    if guard_log_exists:
        evidence_outputs.append(GUARD_LOG_PATH.relative_to(ROOT).as_posix())
    
    header = {
        "check_id": "D08_cli_guardrail",
        "status": status,
        "exit_code": exit_code,
        "command": "python tools/cli/serializer_grep_guard.py",
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
    """Main entrypoint for CLI serializer grep guard runner."""
    try:
        # Verify cli/main.py exists (actually at engine/cli/main.py)
        if not CLI_MAIN_PATH.exists():
            print(f"FAIL: {CLI_MAIN_PATH} does not exist", file=sys.stderr)
            captured_env = {key: ENV_PINS.get(key, "") for key in ["APP_ENV", "SAFE_MODE", "ALLOW_NETWORK", "LANG", "LC_ALL", "TZ"]}
            _write_primary_log("FAIL", 1, captured_env, False)
            return 1
        
        # Setup environment
        env = _setup_env()
        
        # Run the serializer grep guard
        cmd = [sys.executable, "tools/cli/serializer_grep_guard.py"]
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
        
        # Check if guard log was created
        guard_log_exists = GUARD_LOG_PATH.exists()
        
        # Write path proof for guard log if it exists
        if guard_log_exists:
            _write_path_proof(GUARD_LOG_PATH)
        
        # Determine status
        if result.returncode == 0:
            status = "PASS"
        else:
            status = "FAIL"
        
        # Write primary log
        _write_primary_log(status, result.returncode, captured_env, guard_log_exists)
        
        return result.returncode
        
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        captured_env = {key: ENV_PINS.get(key, "") for key in ["APP_ENV", "SAFE_MODE", "ALLOW_NETWORK", "LANG", "LC_ALL", "TZ"]}
        _write_primary_log("FAIL", 1, captured_env, False)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
