#!/usr/bin/env python3
"""Run the env pins gate and emit governed artifacts."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.evidence import update_evidence_index


def _write_path_proof(rel_path: str, *, produced_at: str) -> None:
    """Write path proof for a generated artifact."""
    path = ROOT / rel_path
    if not path.exists():
        return
    stat = path.stat()
    import hashlib
    sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
    update_evidence_index._write_path_proof(
        rel=rel_path,
        sha256=sha256,
        size_bytes=stat.st_size,
        mtime_utc=update_evidence_index._isoformat_from_timestamp(stat.st_mtime),
        produced_at=produced_at,
        default_produced_at=produced_at,
        check=False,
        stat_mtime=stat.st_mtime,
    )


def _run_gate(*, check_only: bool = False) -> int:
    """Run the env pins gate via the bash script."""
    from engine.runtime.determinism_env import ensure_determinism_env
    
    # Ensure determinism environment is set before running the check
    ensure_determinism_env(apply=True)
    
    script_path = ROOT / "ci" / "checks" / "check_env_pins.sh"
    
    if not script_path.exists():
        print(f"Error: {script_path} not found", file=sys.stderr)
        return 1
    
    # Run the bash script
    result = subprocess.run(
        [str(script_path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    
    # Print output
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    
    # Write path proof for the generated log if it exists
    if not check_only and result.returncode == 0:
        import datetime as _dt
        produced_at = _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        _write_path_proof("audit/gates/determinism/env_pins.log", produced_at=produced_at)
    
    return result.returncode


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the env pins gate")
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="validate without rewriting gate artifacts",
    )
    return parser.parse_args(list(argv) if argv is not None else None)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    return _run_gate(check_only=args.check_only)


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
