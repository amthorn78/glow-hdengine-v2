"""Generate deterministic showcompat CLI capture artifacts for EPIC022 D2."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime import identity_meta
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

ENV_KEYS = tuple(ENV_PINS)

PAIR = {
    "left": {"birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US"},
    "right": {"birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE"},
}


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    env.update(ENV_PINS)
    ensure_determinism_env(environ=env)
    return env


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _stdin_bytes() -> bytes:
    return (json.dumps(PAIR, separators=(",", ":")) + "\n").encode("utf-8")


def _capture_outputs() -> dict[Path, bytes]:
    env = _cli_env()
    recorded_cmd = ["python", "scripts/hdctl.py", "showcompat"]
    execution_cmd = [sys.executable, *recorded_cmd[1:]]
    stdin_bytes = _stdin_bytes()
    stdin_sha = hashlib.sha256(stdin_bytes).hexdigest()

    result = subprocess.run(execution_cmd, input=stdin_bytes, capture_output=True, env=env)
    if result.returncode != 0:
        raise SystemExit(f"showcompat failed (rc={result.returncode}): {result.stderr!r}")
    if result.stderr:
        raise SystemExit(f"unexpected stderr from showcompat: {result.stderr!r}")
    stdout_bytes = result.stdout
    if not stdout_bytes.endswith(b"\n"):
        raise SystemExit("stdout missing trailing LF")

    try:
        payload = json.loads(stdout_bytes)
        emitted_meta = payload["compat"]["meta"]
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        raise SystemExit("showcompat identity metadata missing or invalid") from exc
    immutable_meta = identity_meta()
    if emitted_meta != immutable_meta:
        raise SystemExit("showcompat identity metadata does not match immutable identity")

    stdout_sha = hashlib.sha256(stdout_bytes).hexdigest()
    args_payload = {
        "generator": "tools/cli/generate_showcompat_artifacts.py",
        "argv": recorded_cmd,
        "env": {key: env[key] for key in ENV_KEYS},
        "identity": {
            "source": "engine.runtime.identity",
            "meta": immutable_meta,
        },
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
    return {
        STDOUT_PATH: stdout_bytes,
        SHA_PATH: f"{stdout_sha}\n".encode("utf-8"),
        ARGS_PATH: sercanon(args_payload),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    expected = _capture_outputs()

    if args.check:
        drift = [
            path.relative_to(ROOT).as_posix()
            for path, body in expected.items()
            if not path.exists() or path.read_bytes() != body
        ]
        if drift:
            raise SystemExit("DRIFT:" + ",".join(drift))
        return 0

    for path, body in expected.items():
        _write_bytes(path, body)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
