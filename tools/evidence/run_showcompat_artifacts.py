"""Run showcompat artifacts generation and produce evidence for EPIC024 D03."""
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
from engine.serializer.canon import sercanon

# Output paths as specified in approved plan
ARTIFACTS_DIR = ROOT / "artifacts" / "showcompat" / "epic024"
MANIFEST_PATH = ARTIFACTS_DIR / "showcompat_manifest.json"
SYMBOLS_PATH = ARTIFACTS_DIR / "showcompat_symbols.json"
PRIMARY_LOG_DIR = ROOT / "audit" / "qa" / "hde-epic024" / "checks" / "D03_showcompat_artifacts"
PRIMARY_LOG_PATH = PRIMARY_LOG_DIR / "primary.log"

ENV_PINS = {
    "APP_ENV": "rails",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
}

IDENTITY_ENV = {
    "ENGINE_TAG": "hdengine-dev",
    "RELEASE_ID": "0" * 64,
    "PRODUCT_INVOCATION_TAG": "INV-EPIC024-D03",
}

ENV_KEYS = (
    "APP_ENV",
    "SAFE_MODE",
    "ALLOW_NETWORK",
    "LC_ALL",
    "LANG",
    "TZ",
    "ENGINE_TAG",
    "RELEASE_ID",
    "PRODUCT_INVOCATION_TAG",
)

PAIR = {
    "left": {"birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US"},
    "right": {"birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE"},
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


def _cli_env() -> dict[str, str]:
    """Build the environment for running showcompat."""
    env = os.environ.copy()
    env.update(ENV_PINS)
    env.update(IDENTITY_ENV)
    ensure_determinism_env(environ=env)
    return env


def _stdin_bytes() -> bytes:
    """Generate stdin input for showcompat."""
    return (json.dumps(PAIR, separators=(",", ":")) + "\n").encode("utf-8")


def _run_showcompat() -> tuple[bytes, dict]:
    """Run the showcompat command and return stdout and metadata."""
    env = _cli_env()
    cmd = [sys.executable, "scripts/hdctl.py", "showcompat"]
    stdin_bytes = _stdin_bytes()
    stdin_sha = hashlib.sha256(stdin_bytes).hexdigest()

    result = subprocess.run(cmd, input=stdin_bytes, capture_output=True, env=env, cwd=ROOT)
    
    if result.returncode != 0:
        stderr_preview = result.stderr.decode("utf-8", errors="replace")[:200]
        raise SystemExit(f"showcompat failed (rc={result.returncode}): {stderr_preview}")
    
    if result.stderr:
        raise SystemExit(f"unexpected stderr from showcompat: {result.stderr!r}")
    
    stdout_bytes = result.stdout
    if not stdout_bytes.endswith(b"\n"):
        raise SystemExit("stdout missing trailing LF")

    metadata = {
        "cmd": cmd,
        "env": {key: env[key] for key in ENV_KEYS if key in env},
        "stdin_sha256": stdin_sha,
        "stdin_payload": PAIR,
        "stdout_sha256": hashlib.sha256(stdout_bytes).hexdigest(),
        "returncode": result.returncode,
    }
    
    return stdout_bytes, metadata


def _extract_symbols(stdout_bytes: bytes) -> dict:
    """Extract symbol information from showcompat output."""
    try:
        output = json.loads(stdout_bytes.decode("utf-8"))
        symbols = {
            "command": "scripts/hdctl.py showcompat",
            "output_keys": list(output.keys()) if isinstance(output, dict) else [],
            "has_bands": "bands" in output if isinstance(output, dict) else False,
            "output_size_bytes": len(stdout_bytes),
        }
        return symbols
    except Exception as e:
        return {"error": f"Failed to parse showcompat output: {e}"}


def _write_primary_log(status: str, exit_code: int, captured_env: dict) -> None:
    """Write the primary log with structured header."""
    header = {
        "check_id": "D03_showcompat_artifacts",
        "status": status,
        "exit_code": exit_code,
        "command": "python tools/cli/generate_showcompat_artifacts.py",
        "evidence_outputs": [
            MANIFEST_PATH.relative_to(ROOT).as_posix(),
            SYMBOLS_PATH.relative_to(ROOT).as_posix(),
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
    """Main entrypoint for showcompat artifacts generation."""
    try:
        # Run showcompat and get output
        stdout_bytes, metadata = _run_showcompat()
        
        # Parse showcompat output
        try:
            showcompat_output = json.loads(stdout_bytes.decode("utf-8"))
        except Exception as e:
            raise SystemExit(f"Failed to parse showcompat JSON output: {e}")
        
        # Create manifest
        manifest = {
            "generator": "tools/evidence/run_showcompat_artifacts.py",
            "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "command": metadata["cmd"],
            "env": metadata["env"],
            "input": {
                "source": "stdin",
                "payload": metadata["stdin_payload"],
                "stdin_sha256": metadata["stdin_sha256"],
            },
            "output": {
                "stdout_sha256": metadata["stdout_sha256"],
                "returncode": metadata["returncode"],
            },
            "artifacts": {
                "manifest": MANIFEST_PATH.relative_to(ROOT).as_posix(),
                "symbols": SYMBOLS_PATH.relative_to(ROOT).as_posix(),
            },
        }
        
        # Extract symbols
        symbols = _extract_symbols(stdout_bytes)
        
        # Write artifacts
        _write_json(MANIFEST_PATH, manifest)
        _write_json(SYMBOLS_PATH, symbols)
        
        # Write path proofs
        _write_path_proof(MANIFEST_PATH)
        _write_path_proof(SYMBOLS_PATH)
        
        # Write primary log
        captured_env = {
            "APP_ENV": os.environ.get("APP_ENV", ""),
            "SAFE_MODE": ENV_PINS["SAFE_MODE"],
            "ALLOW_NETWORK": ENV_PINS["ALLOW_NETWORK"],
            "LANG": ENV_PINS["LANG"],
            "LC_ALL": ENV_PINS["LC_ALL"],
            "TZ": ENV_PINS["TZ"],
        }
        _write_primary_log("PASS", 0, captured_env)
        
        return 0
        
    except SystemExit as e:
        # Write FAIL primary log
        captured_env = {key: ENV_PINS.get(key, "") for key in ["APP_ENV", "SAFE_MODE", "ALLOW_NETWORK", "LANG", "LC_ALL", "TZ"]}
        _write_primary_log("FAIL", 1, captured_env)
        raise


if __name__ == "__main__":
    raise SystemExit(main())
