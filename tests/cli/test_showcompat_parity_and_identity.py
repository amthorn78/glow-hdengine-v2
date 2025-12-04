import hashlib
import json
import os
import subprocess
import sys
import sysconfig
from pathlib import Path

from engine.cli import main as cli_main
from engine.presenter import emitter
from engine.runtime import emit_reader_public_envelope

AB_ARTIFACT = Path("artifacts/cli/ab.json")
BA_ARTIFACT = Path("artifacts/cli/ba.json")
PRESENTER_AB_ARTIFACT = Path("artifacts/presenter/showcompat_ab.bytes")
PRESENTER_BA_ARTIFACT = Path("artifacts/presenter/showcompat_ba.bytes")
PRESENTER_READER_ARTIFACT = Path("artifacts/presenter/reader_cli_parity.bytes")
PRESENTER_PREIMAGE_LOG = Path("artifacts/presenter/preimage_recompute.log")

PAIR = {
    "left": {"birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US"},
    "right": {"birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE"},
}


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env.setdefault("PATH", f"{scripts_dir}:{env.get('PATH', '')}")
    env.update(
        {
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "ENGINE_TAG": "hdengine-dev",
            "RELEASE_ID": "0" * 64,
            "PRODUCT_INVOCATION_TAG": "INV-TEST",
        }
    )
    return env


def _run_showcompat(payload: dict[str, object], extra_args: list[str] | None = None, env: dict[str, str] | None = None):
    args = [sys.executable, "scripts/hdctl.py", "showcompat"]
    if extra_args:
        args.extend(extra_args)
    proc = subprocess.run(
        args,
        input=(json.dumps(payload, separators=(",", ":")) + "\n").encode(),
        capture_output=True,
        env=env or _cli_env(),
    )
    return proc


def _canonical_reader_bytes(pair: dict, env: dict[str, str] | None = None) -> bytes:
    left_norm = cli_main._normalize_party(pair["left"], "left")
    right_norm = cli_main._normalize_party(pair["right"], "right")
    left_person, left_chart = cli_main._party_from_normalized(left_norm)
    right_person, right_chart = cli_main._party_from_normalized(right_norm)
    left_person, right_person, left_chart, right_chart = cli_main._canonical_pair(
        left_person, right_person, left_chart, right_chart
    )
    env_map = env or os.environ
    engine_tag = env_map.get("ENGINE_TAG", "hdengine-dev")
    release_id = env_map.get("RELEASE_ID", "0" * 64)
    invocation_tag = env_map.get("PRODUCT_INVOCATION_TAG", "INV-LOCAL")
    reader_bytes, _ = emit_reader_public_envelope(
        left_chart,
        right_chart,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=release_id,
    )
    return reader_bytes


def test_two_run_identity_and_reemit():
    first = _run_showcompat(PAIR)
    second = _run_showcompat(PAIR)

    assert first.returncode == second.returncode == 0
    assert first.stderr == second.stderr == b""
    assert first.stdout == second.stdout
    assert first.stdout.endswith(b"\n") and b"\n\n" not in first.stdout

    assert PRESENTER_AB_ARTIFACT.read_bytes() == first.stdout

    payload = json.loads(first.stdout)
    re_emitted = emitter.emit_public(payload)
    assert re_emitted == first.stdout


def test_ab_ba_identity_and_artifacts():
    env = _cli_env()
    ab_proc = _run_showcompat(PAIR, env=env)
    swapped = {"left": PAIR["right"], "right": PAIR["left"]}
    ba_proc = _run_showcompat(swapped, env=env)

    assert ab_proc.returncode == ba_proc.returncode == 0
    assert ab_proc.stderr == ba_proc.stderr == b""
    assert ab_proc.stdout == ba_proc.stdout
    assert ab_proc.stdout.endswith(b"\n")

    assert AB_ARTIFACT.read_bytes() == ab_proc.stdout
    assert BA_ARTIFACT.read_bytes() == ba_proc.stdout
    assert PRESENTER_AB_ARTIFACT.read_bytes() == ab_proc.stdout
    assert PRESENTER_BA_ARTIFACT.read_bytes() == ba_proc.stdout


def test_reader_dump_matches_runtime(tmp_path: Path):
    pair_path = tmp_path / "pair.json"
    pair_path.write_text(json.dumps(PAIR, separators=(",", ":")) + "\n", encoding="utf-8")
    dump_path = tmp_path / "reader.json"

    env = _cli_env()
    proc = subprocess.run(
        [
            sys.executable,
            "scripts/hdctl.py",
            "showcompat",
            "--pair-file",
            str(pair_path),
            "--dump-reader",
            str(dump_path),
        ],
        capture_output=True,
        env=env,
    )

    assert proc.returncode == 0
    assert proc.stderr == b""
    assert proc.stdout.endswith(b"\n")

    dump_bytes = dump_path.read_bytes()
    expected = _canonical_reader_bytes(PAIR, env=env)
    assert dump_bytes == expected
    assert PRESENTER_READER_ARTIFACT.read_bytes() == expected

    envelope = json.loads(dump_bytes)
    preimage = {k: v for k, v in envelope.items() if k != "idempotence_hash"}
    digest = hashlib.sha256(emitter.emit_public(preimage)).hexdigest()
    assert digest == envelope["idempotence_hash"]


def _parse_preimage_log(path: Path) -> dict[str, str]:
    parts = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        parts[key.strip()] = value.strip()
    return parts


def test_preimage_artifact_matches_log():
    envelope = json.loads(PRESENTER_READER_ARTIFACT.read_bytes())
    preimage = {k: v for k, v in envelope.items() if k != "idempotence_hash"}
    digest = hashlib.sha256(emitter.emit_public(preimage)).hexdigest()
    log_parts = _parse_preimage_log(PRESENTER_PREIMAGE_LOG)
    assert log_parts.get("computed_sha256") == digest
    assert log_parts.get("stored_sha256") == envelope["idempotence_hash"]
    assert log_parts.get("match") == str(digest == envelope["idempotence_hash"]).lower()
