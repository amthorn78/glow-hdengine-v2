import hashlib
import json
import os
import subprocess
import sys
import sysconfig
from pathlib import Path

import pytest

from engine.cli import main as cli_main
from engine.presenter import emitter
from engine.runtime import emit_reader_public_envelope, identity_meta
from tools.cli import generate_showcompat_artifacts as capture_generator

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
            "SAFE_MODE": env.get("SAFE_MODE", "0"),
            "ALLOW_NETWORK": env.get("ALLOW_NETWORK", "1"),
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
        }
    )
    return env


def _open_rails(env: dict[str, str]) -> bool:
    return env.get("ALLOW_NETWORK") == "1" or env.get("SAFE_MODE") == "0"


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


def _run_showcompat(payload: dict[str, object], extra_args: list[str] | None = None, env: dict[str, str] | None = None):
    args = [sys.executable, "scripts/hdctl.py", "showcompat", *_birth_args(payload)]
    if extra_args:
        args.extend(extra_args)
    proc = subprocess.run(
        args,
        capture_output=True,
        env=env or _cli_env(),
    )
    return proc


def _canonical_reader_bytes(pair: dict) -> bytes:
    left_norm = cli_main._normalize_party(pair["left"], "left")
    right_norm = cli_main._normalize_party(pair["right"], "right")
    left_person, left_chart = cli_main._party_from_normalized(left_norm)
    right_person, right_chart = cli_main._party_from_normalized(right_norm)
    left_person, right_person, left_chart, right_chart = cli_main._canonical_pair(
        left_person, right_person, left_chart, right_chart
    )
    meta = identity_meta()
    reader_bytes, _ = emit_reader_public_envelope(
        left_chart,
        right_chart,
        engine_tag=meta["engine_tag"],
        invocation_tag=meta["invocation_tag"],
        release_id=meta["release_id"],
    )
    return reader_bytes


def test_two_run_identity_and_reemit():
    env = _cli_env()
    if not _open_rails(env):
        pytest.skip("showcompat vendor calls require open rails")
    first = _run_showcompat(PAIR, env=env)
    second = _run_showcompat(PAIR, env=env)

    assert first.returncode == second.returncode == 0
    assert first.stderr == second.stderr == b""
    assert first.stdout == second.stdout
    assert first.stdout.endswith(b"\n") and b"\n\n" not in first.stdout

    if not _open_rails(env):
        assert PRESENTER_AB_ARTIFACT.read_bytes() == first.stdout

    payload = json.loads(first.stdout)
    re_emitted = emitter.emit_public(payload)
    assert re_emitted == first.stdout


def test_ab_ba_identity_and_artifacts():
    env = _cli_env()
    if not _open_rails(env):
        pytest.skip("showcompat vendor calls require open rails")
    ab_proc = _run_showcompat(PAIR, env=env)
    swapped = {"left": PAIR["right"], "right": PAIR["left"]}
    ba_proc = _run_showcompat(swapped, env=env)

    assert ab_proc.returncode == ba_proc.returncode == 0
    assert ab_proc.stderr == ba_proc.stderr == b""
    assert ab_proc.stdout == ba_proc.stdout
    assert ab_proc.stdout.endswith(b"\n")

    if not _open_rails(env):
        assert AB_ARTIFACT.read_bytes() == ab_proc.stdout
        assert BA_ARTIFACT.read_bytes() == ba_proc.stdout
        assert PRESENTER_AB_ARTIFACT.read_bytes() == ab_proc.stdout
        assert PRESENTER_BA_ARTIFACT.read_bytes() == ba_proc.stdout


def test_reader_dump_matches_runtime(tmp_path: Path):
    dump_path = tmp_path / "reader.json"

    env = _cli_env()
    if not _open_rails(env):
        pytest.skip("showcompat vendor calls require open rails")
    proc = subprocess.run(
        [
            sys.executable,
            "scripts/hdctl.py",
            "showcompat",
            *_birth_args(PAIR),
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
    envelope = json.loads(dump_bytes)
    assert isinstance(envelope, dict)
    assert "idempotence_hash" in envelope

    if not _open_rails(env):
        expected = _canonical_reader_bytes(PAIR)
        assert dump_bytes == expected
        assert PRESENTER_READER_ARTIFACT.read_bytes() == expected

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
    env = _cli_env()
    if _open_rails(env):
        pytest.skip("preimage artifact comparison skipped under open rails")
    envelope = json.loads(PRESENTER_READER_ARTIFACT.read_bytes())
    preimage = {k: v for k, v in envelope.items() if k != "idempotence_hash"}
    digest = hashlib.sha256(emitter.emit_public(preimage)).hexdigest()
    log_parts = _parse_preimage_log(PRESENTER_PREIMAGE_LOG)
    assert log_parts.get("computed_sha256") == digest
    assert log_parts.get("stored_sha256") == envelope["idempotence_hash"]
    assert log_parts.get("match") == str(digest == envelope["idempotence_hash"]).lower()

def test_governed_showcompat_capture_uses_immutable_identity():
    env = _cli_env()
    env.update(
        {
            "ENGINE_TAG": "poison-engine-tag",
            "RELEASE_ID": "f" * 64,
            "PRODUCT_INVOCATION_TAG": "POISON-INVOCATION",
        }
    )
    paths = [
        Path("artifacts/cli/showcompat/stdout.json"),
        Path("artifacts/cli/showcompat/stdout.json.sha256"),
        Path("artifacts/cli/showcompat/args.json"),
    ]
    before = {path: path.read_bytes() for path in paths}

    result = subprocess.run(
        [sys.executable, "tools/cli/generate_showcompat_artifacts.py", "--check"],
        capture_output=True,
        env=env,
    )

    assert result.returncode == 0, result.stderr.decode("utf-8")
    assert result.stdout == result.stderr == b""
    assert {path: path.read_bytes() for path in paths} == before

    args_payload = json.loads(paths[2].read_bytes())
    assert set(args_payload["env"]) == {"SAFE_MODE", "ALLOW_NETWORK", "LC_ALL", "LANG", "TZ"}
    assert args_payload["identity"] == {
        "source": "engine.runtime.identity",
        "meta": identity_meta(),
    }
    stdout_payload = json.loads(paths[0].read_bytes())
    assert stdout_payload["compat"]["meta"] == identity_meta()


def test_governed_showcompat_generator_uses_active_interpreter(monkeypatch):
    stdout = capture_generator.sercanon(
        {"compat": {"meta": capture_generator.identity_meta()}}
    )
    captured = {}

    def fake_run(args, *, input, capture_output, env):
        captured["args"] = args
        captured["input"] = input
        captured["capture_output"] = capture_output
        captured["env"] = env
        return subprocess.CompletedProcess(
            args=args,
            returncode=0,
            stdout=stdout,
            stderr=b"",
        )

    monkeypatch.setattr(capture_generator.subprocess, "run", fake_run)

    outputs = capture_generator._capture_outputs()
    args_payload = json.loads(outputs[capture_generator.ARGS_PATH])

    assert captured["args"] == [sys.executable, "scripts/hdctl.py", "showcompat"]
    assert captured["input"] == capture_generator._stdin_bytes()
    assert captured["capture_output"] is True
    assert {
        key: captured["env"][key] for key in capture_generator.ENV_KEYS
    } == capture_generator.ENV_PINS
    assert args_payload["argv"] == ["python", "scripts/hdctl.py", "showcompat"]
