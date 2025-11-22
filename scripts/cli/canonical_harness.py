"""Generate canonical CLI/Reader parity artifacts for PR1."""
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

from engine.cli import main as cli_main
from engine.presenter import emitter
from engine.runtime import emit_reader_public_envelope

PAIR_A = {
    "birthdate": "1990-01-10",
    "birthtime": "14:05",
    "location": "Chicago, US",
}
PAIR_B = {
    "birthdate": "1992-03-04",
    "birthtime": "08:15",
    "location": "Berlin, DE",
}

ARTIFACTS_DIR = Path("artifacts/cli")
GUARDS_DIR = ARTIFACTS_DIR / "guards"


def _env() -> dict[str, str]:
    env = os.environ.copy()
    env.update(
        {
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "ENGINE_TAG": env.get("ENGINE_TAG", "hdengine-dev"),
            "RELEASE_ID": env.get("RELEASE_ID", "0" * 64),
            "PRODUCT_INVOCATION_TAG": env.get("PRODUCT_INVOCATION_TAG", "INV-HARNESS"),
        }
    )
    return env


def _run_showcompat(payload: dict, extra_args: list[str] | None = None) -> subprocess.CompletedProcess[bytes]:
    args = [sys.executable, "scripts/hdctl.py", "showcompat"]
    if extra_args:
        args.extend(extra_args)
    return subprocess.run(
        args,
        input=(json.dumps(payload, separators=(",", ":")) + "\n").encode(),
        capture_output=True,
        env=_env(),
    )


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _write_json(path: Path, obj: dict) -> None:
    data = emitter.emit_public(obj)
    _write_bytes(path, data)


def _canonical_reader(pair: dict) -> tuple[bytes, dict]:
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


def main() -> int:
    ab = {"left": PAIR_A, "right": PAIR_B}
    ba = {"left": PAIR_B, "right": PAIR_A}

    ab_result = _run_showcompat(ab)
    ba_result = _run_showcompat(ba)
    if ab_result.returncode or ba_result.returncode:
        raise SystemExit("showcompat failed during harness")

    ab_path = ARTIFACTS_DIR / "ab.json"
    ba_path = ARTIFACTS_DIR / "ba.json"
    _write_bytes(ab_path, ab_result.stdout)
    _write_bytes(ba_path, ba_result.stdout)

    two_run = _run_showcompat(ab)
    two_run_repeat = _run_showcompat(ab)
    if two_run.stdout != two_run_repeat.stdout:
        raise SystemExit("two-run identity failed")

    summary = {
        "ab_sha256": _sha(ab_result.stdout),
        "ba_sha256": _sha(ba_result.stdout),
        "ab_ba_equal": ab_result.stdout == ba_result.stdout,
        "two_run_sha256": _sha(two_run.stdout),
        "two_run_equal": two_run.stdout == two_run_repeat.stdout,
        "commands": {
            "ab": ab_result.args,
            "ba": ba_result.args,
            "two_run": two_run.args,
        },
    }
    _write_json(ARTIFACTS_DIR / "summary.json", summary)

    reader_bytes, reader_env = _canonical_reader(ab)
    dump_result = _run_showcompat(ab, ["--dump-reader", str(ARTIFACTS_DIR / "reader_dump.json")])
    if dump_result.returncode:
        raise SystemExit("dump-reader run failed")
    dump_path = ARTIFACTS_DIR / "reader_dump.json"
    if not dump_path.exists():
        raise SystemExit("reader dump missing")
    dump_bytes = dump_path.read_bytes()
    _write_bytes(ARTIFACTS_DIR / "reader_cli_parity.bytes", dump_bytes)

    preimage = {k: v for k, v in reader_env.items() if k != "idempotence_hash"}
    digest = _sha(emitter.emit_public(preimage))
    preimage_log = ARTIFACTS_DIR / "preimage_recompute.log"
    preimage_log.write_text(
        f"computed_sha256={digest}\nstored_sha256={reader_env['idempotence_hash']}\nmatch={digest == reader_env['idempotence_hash']}\n",
        encoding="utf-8",
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
