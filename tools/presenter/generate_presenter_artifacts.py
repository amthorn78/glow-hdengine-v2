#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import sysconfig
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.cli import main as cli_main
from engine.presenter import emitter
from engine.runtime import emit_reader_public_envelope

PAIR = {
    "left": {"birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US"},
    "right": {"birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE"},
}

ARTIFACT_DIR = Path("artifacts/presenter")


def _env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env["PATH"] = f"{scripts_dir}:{env.get('PATH', '')}"
    env.update(
        {
            "SAFE_MODE": env.get("SAFE_MODE", "0"),
            "ALLOW_NETWORK": env.get("ALLOW_NETWORK", "1"),
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "ENGINE_TAG": env.get("ENGINE_TAG", "hdengine-dev"),
            "RELEASE_ID": env.get("RELEASE_ID", "0" * 64),
            "PRODUCT_INVOCATION_TAG": env.get("PRODUCT_INVOCATION_TAG", "INV-TEST"),
        }
    )
    return env


def _birth_args(pair: dict[str, dict[str, str]]) -> list[str]:
    left = pair["left"]
    right = pair["right"]
    return [
        "--birthdate-a",
        left["birthdate"],
        "--birthtime-a",
        left["birthtime"],
        "--location-a",
        left["location"],
        "--birthdate-b",
        right["birthdate"],
        "--birthtime-b",
        right["birthtime"],
        "--location-b",
        right["location"],
        "--source",
        "vendor",
    ]


def _run_showcompat(
    payload: dict[str, object], extra_args: list[str] | None = None, env: dict[str, str] | None = None
) -> subprocess.CompletedProcess[bytes]:
    args = [sys.executable, "scripts/hdctl.py", "showcompat", *_birth_args(payload)]
    if extra_args:
        args.extend(extra_args)
    return subprocess.run(
        args,
        capture_output=True,
        env=env or _env(),
    )


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _canonical_reader(pair: dict[str, object]) -> tuple[bytes, dict[str, object]]:
    left_norm = cli_main._normalize_party(pair["left"], "left")
    right_norm = cli_main._normalize_party(pair["right"], "right")
    left_person, left_chart = cli_main._party_from_normalized(left_norm)
    right_person, right_chart = cli_main._party_from_normalized(right_norm)
    left_person, right_person, left_chart, right_chart = cli_main._canonical_pair(
        left_person, right_person, left_chart, right_chart
    )
    engine_tag, release_id, invocation_tag = cli_main._engine_identity()
    return emit_reader_public_envelope(
        left_chart,
        right_chart,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=release_id,
    )


def _identity_summary(ab_bytes: bytes, ba_bytes: bytes, two_run_bytes: bytes) -> bytes:
    summary = {
        "ab_sha256": hashlib.sha256(ab_bytes).hexdigest(),
        "ba_sha256": hashlib.sha256(ba_bytes).hexdigest(),
        "ab_ba_equal": ab_bytes == ba_bytes,
        "two_run_equal": ab_bytes == two_run_bytes,
        "two_run_sha256": hashlib.sha256(two_run_bytes).hexdigest(),
        "commands": {"ab": "showcompat", "ba": "showcompat_swapped", "two_run": "showcompat_repeat"},
    }
    return emitter.emit_public(summary)


def main() -> int:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

    env_map = _env()
    os.environ.update(env_map)

    ab_result = _run_showcompat(PAIR, env=env_map)
    ba_result = _run_showcompat({"left": PAIR["right"], "right": PAIR["left"]}, env=env_map)
    two_run = _run_showcompat(PAIR, env=env_map)

    for label, result in ("ab", ab_result), ("ba", ba_result), ("two", two_run):
        if result.returncode != 0 or result.stderr:
            raise SystemExit(f"showcompat {label} failed: rc={result.returncode}, stderr={result.stderr!r}")
        if not result.stdout.endswith(b"\n"):
            raise SystemExit(f"showcompat {label} missing trailing LF")

    if ab_result.stdout != two_run.stdout:
        raise SystemExit("two-run identity failed for presenter artifacts")

    _write_bytes(ARTIFACT_DIR / "showcompat_ab.bytes", ab_result.stdout)
    _write_bytes(ARTIFACT_DIR / "showcompat_ba.bytes", ba_result.stdout)

    reader_bytes, reader_env = _canonical_reader(PAIR)
    reader_dump_path = ARTIFACT_DIR / "reader_cli_parity.bytes"
    _write_bytes(reader_dump_path, reader_bytes)

    preimage = {k: v for k, v in reader_env.items() if k != "idempotence_hash"}
    digest = hashlib.sha256(emitter.emit_public(preimage)).hexdigest()
    log_body = (
        f"computed_sha256={digest}\n"
        f"stored_sha256={reader_env['idempotence_hash']}\n"
        f"match={str(digest == reader_env['idempotence_hash']).lower()}\n"
    )
    (ARTIFACT_DIR / "preimage_recompute.log").write_text(log_body, encoding="utf-8")

    summary_bytes = _identity_summary(ab_result.stdout, ba_result.stdout, two_run.stdout)
    _write_bytes(ARTIFACT_DIR / "showcompat_identity_summary.json", summary_bytes)

    return 0


if __name__ == "__main__":  # pragma: no cover - script entrypoint
    raise SystemExit(main())
