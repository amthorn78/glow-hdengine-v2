"""Generate deterministic showcompat CLI capture artifacts for EPIC022 D2."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon
ARTIFACTS_DIR = ROOT / "artifacts" / "cli" / "showcompat"
STDOUT_PATH = ARTIFACTS_DIR / "stdout.json"
SHA_PATH = ARTIFACTS_DIR / "stdout.json.sha256"
ARGS_PATH = ARTIFACTS_DIR / "args.json"

ENV_PINS = {
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
}

IDENTITY_ENV = {
    "ENGINE_TAG": "hdengine-dev",
    "RELEASE_ID": "0" * 64,
    "PRODUCT_INVOCATION_TAG": "INV-EPIC022-D2",
}

ENV_KEYS = (
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


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    env.update(ENV_PINS)
    env.update(IDENTITY_ENV)
    ensure_determinism_env(environ=env)
    return env


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _write_json(path: Path, payload: dict) -> None:
    _write_bytes(path, sercanon(payload))


def _stdin_bytes() -> bytes:
    return (json.dumps(PAIR, separators=(",", ":")) + "\n").encode("utf-8")


def main() -> int:
    env = _cli_env()
    cmd = [sys.executable, "scripts/hdctl.py", "showcompat"]
    stdin_bytes = _stdin_bytes()
    stdin_sha = hashlib.sha256(stdin_bytes).hexdigest()

    result = subprocess.run(cmd, input=stdin_bytes, capture_output=True, env=env)
    if result.returncode != 0:
        raise SystemExit(f"showcompat failed (rc={result.returncode}): {result.stderr!r}")
    if result.stderr:
        raise SystemExit(f"unexpected stderr from showcompat: {result.stderr!r}")
    stdout_bytes = result.stdout
    if not stdout_bytes.endswith(b"\n"):
        raise SystemExit("stdout missing trailing LF")

    _write_bytes(STDOUT_PATH, stdout_bytes)
    stdout_sha = hashlib.sha256(stdout_bytes).hexdigest()
    SHA_PATH.write_text(f"{stdout_sha}\n", encoding="utf-8")

    args_payload = {
        "generator": "tools/cli/generate_showcompat_artifacts.py",
        "argv": cmd,
        "env": {key: env[key] for key in ENV_KEYS},
        "input": {
            "source": "stdin",
            "stdin_payload": PAIR,
            "stdin_sha256": stdin_sha,
            "trailing_lf": True,
        },
        "artifacts": {
            "stdout": STDOUT_PATH.relative_to(ROOT).as_posix(),
            "stdout_sha256": SHA_PATH.relative_to(ROOT).as_posix(),
        },
    }
    _write_json(ARGS_PATH, args_payload)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
